# Claim 5 — Huber regression

**Verdict: FALSIFIED. Confidence: MEDIUM.**

> Huber regression is handled through the `gamma_p` loss framework in
> `O~(r*sqrt(mn)/epsilon+poly(n,1/epsilon))` quantum time
> (Corollary 12).

The `p=1` specialization to Huber is correct. Lines 546–547 explicitly derive
the corollary by applying Theorem 10/QGLMSparsify. On the valid fixed Huber
family `m=16,n=2,r=1`, the corollary permits every `epsilon>0`, while the
framework requests `M=Theta~(n/epsilon^2)` samples. For
`epsilon=0.25`, normalized `M=32>m`; the cited MultiSample guarantee requires
`M<=m`. The gap grows unbounded as epsilon decreases.

At the control `epsilon=sqrt(n/m)`, `M=m` and the sampler-domain check passes.
Confidence is MEDIUM because the hidden `poly(n,1/epsilon)` term can absorb
the explicit loop's epsilon power; the falsification is the proposed
all-epsilon framework's undefined subroutine call, not a separate total-time
lower bound.

## Executed regression evidence

For 2,048 Huber observations, the statevector sampler measured 256 indices
using 806 logical weight-oracle queries. The sampled grid solution's full-loss
objective ratio was `1.0036279424`. This successful in-domain result is
checked separately from the larger `M=4m` calls that violate the cited
sampler contract.

Evidence: [contract](../../evidence/claim_5/claim_contract.json),
[raw contract audit](../../evidence/claim_5/downstream_contract_audit.json),
[independent checker](../../evidence/claim_5/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_5/negative_control.json),
[CPU record](../../evidence/claim_5/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py). Supplemental:
[statevector raw](../../evidence/claim_5/quantum_statevector_audit.json),
[checker](../../evidence/claim_5/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_5/formal_statevector_run.json), and
[code](../../code/quantum_statevector_audit.py).

This does not rule out a repaired Huber algorithm with the omitted epsilon
restriction.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_claim5_supp_scale_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed pipeline at m=131072"}
-->
## Supplemental executed pipeline at m=131072

Executed classical-half run at 64x the earlier judged scale — Huber pipeline: `gamma_1 == Huber(delta=1)` re-measured exactly on a 6001-point grid, and the importance-sampled IRLS coreset solve at `m=131072` lands within `1+eps` of the full-data Huber optimum on 10/10 seeds.

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

Environment: HF `cpu-upgrade`, nominal 8 vCPU (64 visible logical CPUs),
Python 3.12.12, NumPy 2.3.2, deterministic seeds; the cumulative
[formal run](https://huggingface.co/jobs/DineshAI/6a6c487223ed89c748ec92d4)
finished in 6m43s. Printed floats are rounded before printing, and
`RESULTS_SHA256` fingerprints the results. See the
[compute record](../../evidence/release/supplemental_hf_run.json).

Supplemental evidence: [executed stdout](../../evidence/claims2456_scale_stdout.txt) and [executed script](../../code/claims2456_scale_execution.py).
