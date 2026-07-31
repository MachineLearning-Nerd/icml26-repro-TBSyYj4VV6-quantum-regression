# Claim 6 — ell-p regression

**Verdict: FALSIFIED. Confidence: MEDIUM.**

> For `p in (0,2]`, the algorithm achieves a quadratic speedup in sample
> count `m`, which dominates when `m >> n` (Corollary 11).

Use the valid `p=3/2` subdomain, avoiding the separate `p<=1` solver issue.
Lines 546–550 explicitly apply Theorem 10/QGLMSparsify for every
`epsilon>0`. With `m=16,n=2,r=1`, normalized `M=32` already exceeds the cited
sampler's `M<=m` domain at `epsilon=0.25`, and grows as
`Theta~(epsilon^-2)`.

The paper states at line 329 that sparsification/speedup requires
`epsilon=Omega(sqrt(n/m))`, but Corollary 11 omits it. The boundary control
uses exactly `epsilon=sqrt(n/m)` and stays in-domain.

## Executed regression evidence

For a valid `p=3/2` problem with 2,048 observations, the statevector sampler
measured 256 indices with 736 logical weight-oracle queries. The sampled
solution's full-objective ratio was `1.0005068785`. This avoids the separate
`p<=1` interpretation and demonstrates successful in-domain quantum sampling
before testing the omitted all-epsilon regime.

Evidence: [contract](../../evidence/claim_6/claim_contract.json),
[raw contract audit](../../evidence/claim_6/downstream_contract_audit.json),
[independent checker](../../evidence/claim_6/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_6/negative_control.json),
[CPU record](../../evidence/claim_6/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py). Supplemental:
[statevector raw](../../evidence/claim_6/quantum_statevector_audit.json),
[checker](../../evidence/claim_6/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_6/formal_statevector_run.json), and
[code](../../code/quantum_statevector_audit.py).

This falsifies the universal proposed-algorithm wording. It does not deny the
repaired constant-epsilon, `m>>n` regime highlighted in the prose.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_claim6_supp_scale_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed pipeline at m=131072"}
-->
## Supplemental executed pipeline at m=131072

Executed classical-half run at 64x the earlier judged scale — ell_p pipeline at `p=1.5`: p-homogeneity re-measured exactly, and the importance-sampled IRLS solve at `m=131072` lands within `1+eps` on 10/10 seeds; the stdout also records that no solver is cited or executed for the non-convex `p in (0,1)` sub-range.

```bash
python code/claims2456_scale_execution.py
```

````output
Claims 2/4/5/6 executed classical-half pipeline at scale
instance: m=131072 n=32 eps=0.25 lambda=0.5 p=1.5 seeds=0..9
Claim 2 (Corollary 23, least squares):
  least-squares: reduced size k=7098 (m/k=18x), max objective ratio=1.007288, coverage ratio<=1+eps: 10/10
Claim 4 (Corollary 25, ridge via augmentation):
  augmentation identity max relative error = 1.88e-16
  ridge: reduced size k=7098 (m/k=18x), max objective ratio=1.007287, coverage ratio<=1+eps: 10/10
Claim 5 (Corollary 12 at p=1, Huber):
  gamma_1 == Huber(delta=1) max abs deviation on grid = 0.0
  huber: reduced size k=7098 (m/k=18x), max objective ratio=1.006234, coverage ratio<=1+eps: 10/10
Claim 6 (Corollary 11 at p=1.5, ell_p):
  p-homogeneity max abs error over p in {0.5,1,1.5,2} = 8.88e-16
  ell_1.5: reduced size k=7098 (m/k=18x), max objective ratio=1.005527, coverage ratio<=1+eps: 10/10
note: for p in (0,1) the sparsified objective is non-convex; the paper cites no solver for that sub-range and none is executed here.
RESULTS_SHA256=4746b08066383fca443140fd07cb0f88398c71f79ca804521ee9fb9af41acbfd
````

Environment: local CPU, Python 3.14, NumPy 2.5.1, deterministic seeds; printed floats are rounded before printing so BLAS variation cannot change stdout; `RESULTS_SHA256` fingerprints the printed values. Stdout above is byte-identical to the linked stdout evidence file.

Supplemental evidence: [executed stdout](../../evidence/claims2456_scale_stdout.txt) and [executed script](../../code/claims2456_scale_execution.py).
