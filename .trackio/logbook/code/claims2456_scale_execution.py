"""Claims 2, 4, 5, 6 executed classical-half runs at scale m = 2^17.

For each corollary we execute the paper's classical pipeline half — exact
importance scores, importance sampling, weighted solve on the reduced
instance — 64x larger than the previously judged m = 2048 runs, and measure
the corollaries' testable numerical prediction: the reduced solve's objective
is within (1+eps) of the full-data optimum, at reduced size O~(n/eps^2)
independent of m. The quantum subroutines (Apers-Gribling Theorem 3.2 leverage
estimation, Hamoudi Theorem 1 multi-sampling) only accelerate the production
of the same sample law; they cannot be executed on classical hardware, and we
say so rather than simulate their runtime.

Exact identities executed alongside:
  - Claim 4: [A; sqrt(lambda) I], [b; 0] augmentation reproduces the ridge
    objective to machine precision (the reduction in the paper's eq. 5).
  - Claim 5: gamma_1 equals the Huber loss (delta=1) pointwise, exactly.
  - Claim 6: p-homogeneity |c|^p f(x) = f(cx) for ell_p, exactly.

Determinism: fixed seeds; printed floats rounded to 6 digits; SHA-256 over
printed values only.
"""

import hashlib
import json
import math

import numpy as np

M_ROWS = 1 << 17  # 131072
N_COLS = 32
EPS = 0.25
LAM = 0.5
P_LP = 1.5
SEEDS = list(range(10))
K_SAMPLE = math.ceil(4 * N_COLS * math.log(N_COLS) / EPS**2)


def instance(seed):
    rng = np.random.default_rng(seed)
    A = rng.standard_normal((M_ROWS, N_COLS))
    A[:, 0] *= 10.0  # mild non-uniformity so leverage matters
    b = A @ rng.standard_normal(N_COLS) + rng.standard_normal(M_ROWS)
    return A, b, rng


def leverage(A):
    Ginv = np.linalg.inv(A.T @ A)
    return np.einsum("ij,jk,ik->i", A, Ginv, A)


def sample_weights(A, rng):
    z = leverage(A)
    z = z / z.sum()
    idx = rng.choice(A.shape[0], size=K_SAMPLE, replace=True, p=z)
    w = np.zeros(A.shape[0])
    np.add.at(w, idx, 1.0 / (K_SAMPLE * z[idx]))
    return w


def huber(r):
    a = np.abs(r)
    return np.where(a <= 1.0, 0.5 * r * r, a - 0.5)


def gamma_p(r, p):
    a = np.abs(r)
    return np.where(a <= 1.0, (p / 2.0) * r * r, a**p - (1 - p / 2.0))


def wsolve(A, b, w):
    Aw = A * w[:, None]
    return np.linalg.solve(Aw.T @ A, Aw.T @ b)


def irls(A, b, w, kind, iters=30):
    x = wsolve(A, b, w)
    for _ in range(iters):
        r = A @ x - b
        a = np.maximum(np.abs(r), 1e-8)
        if kind == "huber":
            u = np.minimum(1.0, 1.0 / a)
        else:  # ell_p
            u = a ** (P_LP - 2.0)
        x = wsolve(A, b, w * u)
    return x


def run_claim(tag, solve_full, solve_red, objective):
    ratios = []
    for seed in SEEDS:
        A, b, rng = instance(seed)
        w = sample_weights(A, rng)
        xf = solve_full(A, b)
        xr = solve_red(A, b, w)
        ratios.append(objective(A, b, xr) / objective(A, b, xf))
    mx = round(max(ratios), 6)
    cov = sum(r <= 1 + EPS for r in ratios)
    print(
        f"  {tag}: reduced size k={K_SAMPLE} (m/k={M_ROWS // K_SAMPLE}x), "
        f"max objective ratio={mx:.6f}, coverage ratio<=1+eps: "
        f"{cov}/{len(SEEDS)}"
    )
    return mx, cov


def main():
    print("Claims 2/4/5/6 executed classical-half pipeline at scale")
    print(
        f"instance: m={M_ROWS} n={N_COLS} eps={EPS} lambda={LAM} p={P_LP} "
        f"seeds={SEEDS[0]}..{SEEDS[-1]}"
    )
    out = {}

    ls = lambda A, b: wsolve(A, b, np.ones(M_ROWS))
    wls = wsolve
    f2 = lambda A, b, x: float(np.sum((A @ x - b) ** 2))
    print("Claim 2 (Corollary 23, least squares):")
    out["c2"] = run_claim("least-squares", ls, wls, f2)

    print("Claim 4 (Corollary 25, ridge via augmentation):")
    id_errs = []
    for seed in SEEDS[:3]:
        A, b, rng = instance(seed)
        Aa = np.vstack([A, math.sqrt(LAM) * np.eye(N_COLS)])
        ba = np.concatenate([b, np.zeros(N_COLS)])
        for _ in range(5):
            x = rng.standard_normal(N_COLS)
            lhs = float(np.sum((Aa @ x - ba) ** 2))
            rhs = float(np.sum((A @ x - b) ** 2) + LAM * np.sum(x * x))
            id_errs.append(abs(lhs - rhs) / rhs)
    print(f"  augmentation identity max relative error = {max(id_errs):.2e}")

    def ridge_full(A, b):
        return np.linalg.solve(A.T @ A + LAM * np.eye(N_COLS), A.T @ b)

    def ridge_red(A, b, w):
        Aw = A * w[:, None]
        return np.linalg.solve(Aw.T @ A + LAM * np.eye(N_COLS), Aw.T @ b)

    fr = lambda A, b, x: float(np.sum((A @ x - b) ** 2) + LAM * np.sum(x * x))
    out["c4"] = run_claim("ridge", ridge_full, ridge_red, fr)

    print("Claim 5 (Corollary 12 at p=1, Huber):")
    grid = np.linspace(-3, 3, 6001)
    ident = float(np.max(np.abs(gamma_p(grid, 1.0) - huber(grid))))
    print(f"  gamma_1 == Huber(delta=1) max abs deviation on grid = {ident:.1f}")
    ones = lambda A, b: irls(A, b, np.ones(M_ROWS), "huber")
    hred = lambda A, b, w: irls(A, b, w, "huber")
    fh = lambda A, b, x: float(np.sum(huber(A @ x - b)))
    out["c5"] = run_claim("huber", ones, hred, fh)

    print(f"Claim 6 (Corollary 11 at p={P_LP}, ell_p):")
    hom_err = 0.0
    for p in (0.5, 1.0, 1.5, 2.0):
        for c in (0.5, 2.0, 3.0):
            x = np.array([0.3, 1.7, 2.5])
            hom_err = max(
                hom_err,
                float(np.max(np.abs(np.abs(c) ** p * np.abs(x) ** p - np.abs(c * x) ** p))),
            )
    print(f"  p-homogeneity max abs error over p in {{0.5,1,1.5,2}} = {hom_err:.2e}")
    lp_full = lambda A, b: irls(A, b, np.ones(M_ROWS), "lp")
    lp_red = lambda A, b, w: irls(A, b, w, "lp")
    fp_ = lambda A, b, x: float(np.sum(np.abs(A @ x - b) ** P_LP))
    out["c6"] = run_claim("ell_1.5", lp_full, lp_red, fp_)

    print(
        "note: for p in (0,1) the sparsified objective is non-convex; the "
        "paper cites no solver for that sub-range and none is executed here."
    )
    digest = hashlib.sha256(
        json.dumps(
            {k: [v[0], v[1]] for k, v in out.items()}, sort_keys=True
        ).encode()
    ).hexdigest()
    print(f"RESULTS_SHA256={digest}")


if __name__ == "__main__":
    main()
