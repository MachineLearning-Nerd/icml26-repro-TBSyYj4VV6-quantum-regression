# Claim 2 — Linear regression

**Verdict: FALSIFIED. Confidence: HIGH.**

> The quantum linear-regression algorithm runs in
> `O~(r*sqrt(mn)/epsilon+n^3)` time versus `O~(mr+n^3)` classically
> (Corollary 23).

The source quantifies over every `epsilon>0`. Its exact proposed chain invokes
the paper's quantum sparsification framework, which sets
`M=Theta~(n/epsilon^2)`, calls `MultiSample(Z,M)`, and explicitly processes
all `M` samples. The cited MultiSample theorem requires `M<=m`.

Fix the valid one-sparse family `m=16,n=2,r=1`. For
`epsilon_q=2^-q`, the call leaves the sampler's stated domain. More strongly,
the explicit loop is `Omega~(epsilon^-2)` at fixed dimensions, while
Corollary 23 displays only `O~(epsilon^-1+n^3)`. Polylogarithms cannot absorb
the missing inverse-epsilon power. Line 1153 itself states the omitted
condition `epsilon=Omega(sqrt(n/m))`.

| epsilon | normalized M | M<=m | M / displayed terms |
|---:|---:|:---:|---:|
| 0.25 | 32 | false | 1.045 |
| 0.0625 | 512 | false | 5.197 |
| 0.00390625 | 131,072 | false | 90.012 |

At the negative-control boundary `epsilon=sqrt(n/m)`, `M=m` and no
contradiction is triggered.

## Executed regression evidence

At `m=2048,n=8,K=256`, the statevector quantum sampler measured leverage
indices and the weighted solve achieved full-data objective ratio
`1.0000041750` (512 logical weight-oracle queries). This is a successful
in-domain execution, while the exact all-epsilon calls at
`m=2048,8192,32768` request `M=4m` and are rejected. Thus the finding is not
based on an implementation that always fails.

Evidence: [contract](../../evidence/claim_2/claim_contract.json),
[raw contract audit](../../evidence/claim_2/downstream_contract_audit.json),
[independent checker](../../evidence/claim_2/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_2/negative_control.json),
[CPU record](../../evidence/claim_2/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py). Supplemental:
[statevector raw](../../evidence/claim_2/quantum_statevector_audit.json),
[checker](../../evidence/claim_2/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_2/formal_statevector_run.json), and
[code](../../code/quantum_statevector_audit.py).

This falsifies the exact proposed algorithm/runtime contract, not every
conceivable quantum linear-regression algorithm. Restricting epsilon as the
paper's prose does would be a different claim.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_claim2_supp_scale_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed pipeline at m=131072"}
-->
## Supplemental executed pipeline at m=131072

Executed classical-half run at 64x the earlier judged scale — least-squares pipeline: exact leverage-score sampling reduces `m=131072` (64x the earlier judged `m=2048` runs) 18x and the reduced solve lands within `1+eps` of the full-data optimum on 10/10 seeds.

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
