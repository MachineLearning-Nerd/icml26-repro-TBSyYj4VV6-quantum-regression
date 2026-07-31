"""Claim 1 (Theorem 10) executed audit at non-toy scale.

Two executed parts, one deterministic conclusion:

Part A (in-regime execution, m = 2^18): run the exact classical realization of
Algorithm 2's sampling core (steps 5-10) for the quadratic proper loss family,
where quantum MultiSample (Hamoudi 2022, Theorem 1) is replaced by a classical
sampler with the *identical output law* (i.i.d. draws proportional to z_i; the
quantum part changes only the query cost, not the distribution). We verify the
epsilon-approximate sparsifier guarantee spectrally and end-to-end.

Part B (boundary sweep): with the explicit constant M = ceil(C n ln(n) / eps^2)
(C = 4), sweep eps downward and record where the MultiSample precondition
(sample count <= vector length, Theorem 20 as cited by the paper) fails, and
where the algorithm's explicit M-iteration classical loop (steps 7-10) exceeds
the sqrt(mn)/eps envelope of the claimed runtime. Both measured boundaries must
equal the predicted eps* = sqrt(C n ln(n) / m).

Negative control: at eps = eps* exactly, the call is in-domain.

Determinism: fixed seeds, printed floats rounded so BLAS variation cannot
change stdout; SHA-256 fingerprint over the printed results only.
"""

import hashlib
import json
import math

import numpy as np

M_ROWS = 1 << 18  # 262144 data points
N_COLS = 64
ROW_SPARSITY = 8
C_CONST = 4  # explicit constant in M = ceil(C n ln n / eps^2)
SEEDS = list(range(10))


def build_instance(seed):
    rng = np.random.default_rng(seed)
    A = np.zeros((M_ROWS, N_COLS))
    cols = rng.integers(0, N_COLS, size=(M_ROWS, ROW_SPARSITY))
    vals = rng.standard_normal((M_ROWS, ROW_SPARSITY))
    rows = np.repeat(np.arange(M_ROWS), ROW_SPARSITY)
    A[rows, cols.ravel()] = vals.ravel()
    b = A @ rng.standard_normal(N_COLS) + 0.1 * rng.standard_normal(M_ROWS)
    return A, b, rng


def leverage_scores(A):
    G = A.T @ A
    Ginv = np.linalg.inv(G)
    return np.einsum("ij,jk,ik->i", A, Ginv, A)


def sample_size(eps):
    return math.ceil(C_CONST * N_COLS * math.log(N_COLS) / eps**2)


def run_part_a():
    results = []
    for eps in (0.5, 0.25, 0.125):
        M = sample_size(eps)
        spectral_devs, ratios = [], []
        for seed in SEEDS:
            A, b, rng = build_instance(seed)
            lev = leverage_scores(A)
            z = lev / lev.sum()
            idx = rng.choice(M_ROWS, size=M, replace=True, p=z)
            # Algorithm 2 line 9 with exact sum (spectral test):
            w = np.zeros(M_ROWS)
            np.add.at(w, idx, 1.0 / (M * z[idx]))
            G = A.T @ A
            Gs = (A * w[:, None]).T @ A
            B = np.linalg.inv(np.linalg.cholesky(G))
            eigs = np.linalg.eigvalsh(B @ Gs @ B.T)
            spectral_devs.append(max(abs(eigs.max() - 1), abs(eigs.min() - 1)))
            # Algorithm 2 line 9 exactly as printed (SumEstimate error 0.1,
            # deterministic worst-ish draw per seed), end-to-end argmin test:
            nu_err = 1.0 + 0.1 * (2 * (seed % 2) - 1)
            w_alg = np.zeros(M_ROWS)
            np.add.at(w_alg, idx, nu_err / (1.1 * M * z[idx]))
            mask = w_alg > 0
            sw = np.sqrt(w_alg[mask])
            xs = np.linalg.lstsq(A[mask] * sw[:, None], b[mask] * sw, rcond=None)[0]
            xf = np.linalg.lstsq(A, b, rcond=None)[0]
            f = lambda x: float(np.sum((A @ x - b) ** 2))
            ratios.append(f(xs) / f(xf))
        results.append(
            {
                "eps": eps,
                "M": M,
                "M_le_m": M <= M_ROWS,
                "max_spectral_dev": round(max(spectral_devs), 6),
                "spectral_within_eps": bool(max(spectral_devs) <= eps),
                "max_objective_ratio": round(max(ratios), 6),
                "ratio_within_1plus_eps": bool(max(ratios) <= (1 + eps)),
            }
        )
    return results


def run_part_b():
    pred_dom = math.sqrt(C_CONST * N_COLS * math.log(N_COLS) / M_ROWS)
    pred_loop = C_CONST * math.log(N_COLS) * math.sqrt(N_COLS / M_ROWS)
    rows = []
    eps = 0.5
    first_out = None
    first_loop_break = None
    while eps > 1e-4:
        M = sample_size(eps)
        envelope = math.ceil(math.sqrt(M_ROWS * N_COLS) / eps)
        in_dom = M <= M_ROWS
        loop_ok = M <= envelope
        if first_out is None and not in_dom:
            first_out = eps
        if first_loop_break is None and not loop_ok:
            first_loop_break = eps
        rows.append((eps, M, in_dom, loop_ok))
        eps /= 2
    return pred_dom, pred_loop, first_out, first_loop_break, rows


def main():
    print("Claim 1 / Theorem 10 executed audit")
    print(
        f"instance: m={M_ROWS} n={N_COLS} r={ROW_SPARSITY} "
        f"M=ceil({C_CONST}*n*ln(n)/eps^2) seeds={SEEDS[0]}..{SEEDS[-1]}"
    )
    part_a = run_part_a()
    print("Part A - in-regime execution of Algorithm 2 sampling core:")
    for row in part_a:
        print(
            f"  eps={row['eps']:<6} M={row['M']:<6} M<=m={row['M_le_m']} "
            f"max_spectral_dev={row['max_spectral_dev']:.6f} "
            f"within_eps={row['spectral_within_eps']} "
            f"max_obj_ratio={row['max_objective_ratio']:.6f} "
            f"within_1+eps={row['ratio_within_1plus_eps']}"
        )
    pred_dom, pred_loop, first_out, first_loop_break, rows = run_part_b()
    print("Part B - boundary sweep (MultiSample domain and loop envelope):")
    for eps, M, in_dom, loop_ok in rows:
        print(
            f"  eps={eps:<12.6g} M={M:<12} M<=m={str(in_dom):<5} "
            f"M<=sqrt(mn)/eps={loop_ok}"
        )
    print(
        f"predicted domain boundary eps*_dom = sqrt(C n ln n / m) = "
        f"{pred_dom:.6f}"
    )
    print(
        f"predicted loop-envelope boundary eps*_loop = C ln(n) sqrt(n/m) = "
        f"{pred_loop:.6f}"
    )
    print(
        f"measured first out-of-domain eps = {first_out:.6g}; "
        f"measured first loop>envelope eps = {first_loop_break:.6g}"
    )
    both = (first_out < pred_dom <= 2 * first_out) and (
        first_loop_break < pred_loop <= 2 * first_loop_break
    )
    print(
        "each measured boundary sits one halving step under its prediction: "
        f"{both}"
    )
    control_eps = pred_dom
    print(
        f"negative control: eps=eps*={control_eps:.6f} gives "
        f"M={sample_size(control_eps)} <= m={M_ROWS}: "
        f"{sample_size(control_eps) <= M_ROWS}"
    )
    fp = {
        "part_a": part_a,
        "predicted_boundary_dom": round(pred_dom, 6),
        "predicted_boundary_loop": round(pred_loop, 6),
        "first_out_of_domain": first_out,
        "first_loop_break": first_loop_break,
    }
    digest = hashlib.sha256(
        json.dumps(fp, sort_keys=True).encode()
    ).hexdigest()
    print(f"RESULTS_SHA256={digest}")


if __name__ == "__main__":
    main()
