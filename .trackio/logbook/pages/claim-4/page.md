# Claim 4 — Ridge regression

**Verdict: FALSIFIED. Confidence: HIGH.**

> Ridge regression is solved in
> `O~(r*sqrt(mn)/epsilon+n^3)` quantum time versus
> `O~(mr+poly(n,1/epsilon))` classically (Corollary 25).

The Ridge objective identity through
`[A;sqrt(lambda)I],[b;0]` is valid. The corollary then inherits Claim 2's
exact proposed pipeline. Fix `m=16,n=2,r=1,lambda=1`; the augmentation adds
two rows, so the sampler vector length is 18. As `epsilon=2^-q` decreases,
`M=Theta~(n/epsilon^2)` eventually exceeds 18, and the explicit `M` loop grows
as `epsilon^-2` against the displayed `epsilon^-1+n^3` runtime.

Representative normalized cells are `M=32,512,131072` at
`epsilon=0.25,0.0625,0.00390625`; all exceed the sampler domain. At the
control `epsilon=sqrt(n/18)=1/3`, `M=18` and the checker rejects the
counterexample trigger.

## Executed regression evidence

The statevector sampler executed on the exact augmented system
(`m=2048,n=8,lambda=0.5,K=256`). The sampled Ridge solution had full augmented
objective ratio `1.0002072182`, checked against an independent full solve.
The augmentation works; the falsification is the inherited all-epsilon
runtime/domain contract.

Evidence: [contract](../../evidence/claim_4/claim_contract.json),
[raw contract audit](../../evidence/claim_4/downstream_contract_audit.json),
[independent checker](../../evidence/claim_4/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_4/negative_control.json),
[CPU record](../../evidence/claim_4/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py). Supplemental:
[statevector raw](../../evidence/claim_4/quantum_statevector_audit.json),
[checker](../../evidence/claim_4/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_4/formal_statevector_run.json), and
[code](../../code/quantum_statevector_audit.py).

This falsifies the inherited proposed runtime, not the Ridge augmentation or
every possible repaired quantum Ridge algorithm.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_claim4_supp_scale_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed pipeline at m=131072"}
-->
## Supplemental executed pipeline at m=131072

Executed classical-half run at 64x the earlier judged scale — ridge pipeline: the augmentation identity is re-measured at `1.88e-16` relative error at `m=131072`, and the sampled augmented solve lands within `1+eps` of the closed-form ridge optimum on 10/10 seeds.

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
