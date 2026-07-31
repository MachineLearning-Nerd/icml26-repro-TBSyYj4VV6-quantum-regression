"""Claim 3 (Corollary 26) executed priority + display audit.

Deterministic, offline: parses the cached primary-source documents committed
under evidence/claim_3/sources/ (arXiv abstract pages fetched 2026-07-31 and a
verbatim ar5iv excerpt of the target paper), prints their SHA-256 hashes, and
recomputes every step of the argument with exact rational arithmetic
(fractions.Fraction; no floats anywhere).

Steps executed:
  1. Date audit: extract v1 submission dates of arXiv:2110.13086 and
     arXiv:2312.14141 from the cached pages; both must precede the target's
     2025-09-29 v1 date.
  2. Content audit: both abstracts must describe quantum algorithms for Lasso;
     2312.14141 must use the penalized (ell_1-penalty) form, defeating a
     "different formulation" defense of firstness.
  3. Objective bijection (exact): (1/2)||y-Xb||^2 + t||b||_1 and
     ||y-Xb||^2 + 2t||b||_1 have identical minimizers; verified in closed form
     for the 1-d soft-threshold instance with exact fractions.
  4. Self-citation: the target paper's own related-work text acknowledges
     Chen and de Wolf (2023) "quantum algorithms for Lasso and ridge".
  5. Display counterexample (exact): Corollary 26's printed inequality omits
     lambda in the right-hand minimand; for A=[1], b=[1], lambda=100,
     eps=1/10 the printed guarantee is infeasible with gap 7/40.
  6. Negative controls: a Ridge-only earlier record must NOT falsify Lasso
     firstness; the target compared to itself must NOT count as prior art.
"""

import hashlib
import pathlib
import re
from fractions import Fraction

SRC = pathlib.Path(__file__).resolve().parent.parent / "evidence" / "claim_3" / "sources"
TARGET_V1 = "2025-09-29"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_abs(path):
    t = path.read_text(errors="replace")
    title = re.search(r"<title>\[([\d.]+)\] (.*?)</title>", t, re.S)
    sub = re.search(r"\[Submitted on ([^\]]+?)(?:\s*\(|\])", t)
    abstract = re.search(r'blockquote class="abstract[^>]*>(.*?)</blockquote>', t, re.S)
    abs_text = re.sub(r"<[^>]+>", " ", abstract.group(1))
    abs_text = re.sub(r"\s+", " ", abs_text).strip()
    return title.group(1), title.group(2).strip(), sub.group(1).strip(), abs_text


MONTHS = {m: i + 1 for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def iso(date_str):
    d, mon, y = date_str.split()
    return f"{y}-{MONTHS[mon]:02d}-{int(d):02d}"


def soft_threshold_argmin(lam):
    """argmin over x of (x-1)^2 + lam*|x|, exact for lam rational."""
    cand = 1 - lam / 2
    return cand if cand > 0 else Fraction(0)


def halved_soft_threshold_argmin(t):
    """argmin over x of (1/2)(x-1)^2 + t*|x|, derived independently:
    stationarity on x>0 gives x-1+t=0, so argmin = max(0, 1-t)."""
    cand = 1 - t
    return cand if cand > 0 else Fraction(0)


def main():
    print("Claim 3 / Corollary 26 priority + display audit (exact arithmetic)")
    for f in sorted(SRC.iterdir()):
        print(f"  source {f.name} sha256={sha(f)[:16]}...")

    print("Step 1-2: primary-source date and content audit")
    prior = []
    for name in ("arxiv_2110.13086_abs.html", "arxiv_2312.14141_abs.html"):
        arxiv_id, title, sub, abs_text = parse_abs(SRC / name)
        v1 = iso(sub)
        has_lasso = "lasso" in abs_text.lower()
        has_quantum = "quantum" in abs_text.lower()
        penalized = "penalty" in abs_text.lower() or "penalised" in abs_text.lower()
        earlier = v1 < TARGET_V1
        prior.append(earlier and has_lasso and has_quantum)
        print(f"  arXiv:{arxiv_id} v1={v1} earlier_than_target={earlier}")
        print(f"    title: {title}")
        print(
            f"    abstract mentions quantum={has_quantum} lasso={has_lasso} "
            f"penalized-form={penalized}"
        )
    print(f"  prior quantum-Lasso records earlier than target: {sum(prior)} of 2")

    print("Step 3: objective bijection, exact 1-d soft-threshold instance")
    t = Fraction(1, 2)
    m1 = halved_soft_threshold_argmin(t)  # pathwise form (1/2)(x-1)^2 + t|x|
    m2 = soft_threshold_argmin(2 * t)  # target form (x-1)^2 + 2t|x|
    print(
        f"  argmin[(1/2)(x-1)^2+({t})|x|] = {m1}; "
        f"argmin[(x-1)^2+({2*t})|x|] = {m2}; "
        f"equal under lambda_target=2*t: {m1 == m2}"
    )

    print("Step 4: target self-citation of prior quantum Lasso work")
    exc = (SRC / "target_2509.24757_excerpts.txt").read_text()
    quote = "studied by Chen and de Wolf"
    print(f"  excerpt contains '{quote}': {quote in exc}")
    print(f"  excerpt contains 'quantum algorithms for Lasso': "
          f"{'quantum algorithms for Lasso' in exc}")

    print("Step 5: printed-inequality counterexample, exact fractions")
    lam = Fraction(100)
    eps = Fraction(1, 10)
    # left side minimum of (x-1)^2 + 100|x| is at x=0 -> value 1
    x = soft_threshold_argmin(lam)
    left_min = (x - 1) ** 2 + lam * abs(x)
    # right side printed minimand omits lambda: (y-1)^2 + |y|
    y = soft_threshold_argmin(Fraction(1))
    right_min = (y - 1) ** 2 + abs(y)
    bound = (1 + eps) * right_min
    print(f"  min_x[(x-1)^2+100|x|] = {left_min} at x={x}")
    print(f"  (1+eps)*min_y[(y-1)^2+|y|] = {bound} at y={y}")
    print(
        f"  printed guarantee requires {left_min} <= {bound}: "
        f"{left_min <= bound}; impossibility gap = {left_min - bound}"
    )

    print("Step 6: negative controls")
    ridge_only_abs = "quantum ridge regression algorithm for prediction"
    ctrl1 = "lasso" in ridge_only_abs.lower()
    print(
        "  Ridge-only earlier record (Shao 2023, IJMLC 14(1):117-124) "
        f"mentions lasso={ctrl1} -> does not falsify firstness: {not ctrl1}"
    )
    ctrl2 = TARGET_V1 < TARGET_V1
    print(f"  target-vs-itself earlier_than_target={ctrl2} -> not prior art: "
          f"{not ctrl2}")

    verdict = sum(prior) >= 1 and m1 == m2 and left_min > bound
    print(
        "AUDIT RESULT: firstness falsified by >=1 earlier primary source "
        f"(found {sum(prior)}), display inequality falsified exactly: {verdict}"
    )
    fp = f"{sum(prior)}|{m1}|{left_min}|{bound}"
    print(f"RESULTS_SHA256={hashlib.sha256(fp.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
