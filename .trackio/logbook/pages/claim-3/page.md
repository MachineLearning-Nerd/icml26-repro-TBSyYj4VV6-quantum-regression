# Claim 3 — Lasso regression

**Verdict: FALSIFIED. Confidence: HIGH.**

> The paper gives the first quantum algorithm for Lasso regression in
> `O~(r*sqrt(mn)/epsilon + poly(n,1/epsilon))` time, versus
> `O~(mn^2+n^3)` classically (Corollary 26).

The exact corollary specializes the polynomial term to `n^3/epsilon^2` and
quantifies over query access to `A,b`, `r<=n`, `lambda>0`, and
`epsilon>0`, with high-probability output.

The firstness component has a direct primary-source counterexample:
[Quantum Algorithms for the Pathwise Lasso](https://arxiv.org/abs/2312.14141)
was initially published on 2023-12-21, before this target's 2025-09-29 date.
It writes
`(1/2)||y-X beta||_2^2+lambda_prior||beta||_1` and provides quantum LARS
algorithms that output exact or approximate Lasso paths. Multiplying by two
gives the target family under the bijection
`lambda_target=2*lambda_prior`. An independent earlier paper,
[Chen and de Wolf](https://arxiv.org/abs/2110.13086), initially published in
2021, also proves a quantum Lasso algorithm. The target itself acknowledges
that work at source lines 329–330.

The reproduction also executes the 2023 simple quantum LARS algorithm:
statevector BBHT Grover search performs each joining-variable search inside
Dürr–Høyer threshold improvement. All 40 seeded cells
(`features=16,32,64,128`, ten seeds each) passed independent KKT and
coordinate-descent objective checks. Mean measured logical oracle queries in
the canonical regeneration were `21.0,29.6,56.0,76.9`; disabling the Grover
oracle found the correct initial feature only `2/40` times.

Independently, the target's approximation inequality omits `lambda` from the
right minimand. For `A=[1],b=[1],lambda=100,epsilon=1/10`, the smallest left
side is exactly `1` and the printed right bound is `33/40`, an impossibility
gap of `7/40`. The display defect is likely editorial; firstness remains
falsified without relying on it.

Evidence: [headline contract](../../evidence/claim_3/claim_contract.json),
[primary-source firstness counterexample](../../evidence/claim_3/firstness_counterexample.json),
[literal-display counterexample](../../evidence/claim_3/counterexample.json),
[independent checker](../../evidence/claim_3/independent_checker.json),
[checker code](../../code/claim3_independent_checker.py),
[negative control](../../evidence/claim_3/negative_control.json),
[CPU record](../../evidence/claim_3/runtime_cpu.json), and
[counterexample code](../../code/claim3_lasso_counterexample.py).
Supplemental: [quantum LARS raw](../../evidence/claim_3/quantum_statevector_audit.json),
[checker](../../evidence/claim_3/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_3/formal_statevector_run.json), and
[implementation](../../code/quantum_statevector_audit.py).

The checker recomputes both publication-date orderings, the exact objective
mapping, required semantic matches, the rational gap, and two controls: a
later matching paper and an earlier Ridge-only paper must not falsify
firstness.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_c3_supp_audit_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed priority audit"}
-->
## Supplemental executed priority audit (deterministic)

The firstness falsification is additionally established by a fully executed, offline, exact-arithmetic audit over cached primary sources committed under `evidence/claim_3/sources/` (SHA-256-fingerprinted arXiv abstract pages and a verbatim ar5iv excerpt of the target). It recomputes the date orderings, the content tests, the exact objective bijection `lambda_target = 2*lambda_prior` (independent closed forms on both sides, `fractions.Fraction` only), the exact `7/40` display gap, and two negative controls (an earlier Ridge-only record and the target itself must not count as prior art).

```bash
python code/claim3_priority_audit.py
```

````output
Claim 3 / Corollary 26 priority + display audit (exact arithmetic)
  source arxiv_2110.13086_abs.html sha256=c384c804076dd79b...
  source arxiv_2312.14141_abs.html sha256=bc4dedeb62c55596...
  source target_2509.24757_excerpts.txt sha256=e2bccc1cbd5bbb17...
Step 1-2: primary-source date and content audit
  arXiv:2110.13086 v1=2021-10-25 earlier_than_target=True
    title: Quantum Algorithms and Lower Bounds for Linear Regression with Norm Constraints
    abstract mentions quantum=True lasso=True penalized-form=False
  arXiv:2312.14141 v1=2023-12-21 earlier_than_target=True
    title: Quantum Algorithms for the Pathwise Lasso
    abstract mentions quantum=True lasso=True penalized-form=True
  prior quantum-Lasso records earlier than target: 2 of 2
Step 3: objective bijection, exact 1-d soft-threshold instance
  argmin[(1/2)(x-1)^2+(1/2)|x|] = 1/2; argmin[(x-1)^2+(1)|x|] = 1/2; equal under lambda_target=2*t: True
Step 4: target self-citation of prior quantum Lasso work
  excerpt contains 'studied by Chen and de Wolf': True
  excerpt contains 'quantum algorithms for Lasso': True
Step 5: printed-inequality counterexample, exact fractions
  min_x[(x-1)^2+100|x|] = 1 at x=0
  (1+eps)*min_y[(y-1)^2+|y|] = 33/40 at y=1/2
  printed guarantee requires 1 <= 33/40: False; impossibility gap = 7/40
Step 6: negative controls
  Ridge-only earlier record (Shao 2023, IJMLC 14(1):117-124) mentions lasso=False -> does not falsify firstness: True
  target-vs-itself earlier_than_target=False -> not prior art: True
AUDIT RESULT: firstness falsified by >=1 earlier primary source (found 2), display inequality falsified exactly: True
RESULTS_SHA256=4972f9be23b807065ac2e2d8a682ee492c60a17ab80d5b701a588e052d3c3a08
````

Environment: HF `cpu-upgrade`, nominal 8 vCPU (64 visible logical CPUs),
Python 3.12.12, NumPy 2.3.2; the exact-arithmetic audit is deterministic. The
cumulative
[formal run](https://huggingface.co/jobs/DineshAI/6a6c487223ed89c748ec92d4)
finished in 6m43s. See the
[compute record](../../evidence/release/supplemental_hf_run.json).

Supplemental evidence: [executed stdout](../../evidence/claim_3/priority_audit_stdout.txt), [executed script](../../code/claim3_priority_audit.py), [cached arXiv:2110.13086](../../evidence/claim_3/sources/arxiv_2110.13086_abs.html), [cached arXiv:2312.14141](../../evidence/claim_3/sources/arxiv_2312.14141_abs.html), and [target excerpts](../../evidence/claim_3/sources/target_2509.24757_excerpts.txt).
