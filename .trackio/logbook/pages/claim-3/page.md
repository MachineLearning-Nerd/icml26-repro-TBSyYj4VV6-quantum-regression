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

Independently, the target's approximation inequality omits `lambda` from the
right minimand. For `A=[1],b=[1],lambda=100,epsilon=1/10`, the smallest left
side is exactly `1` and the printed right bound is `33/40`, an impossibility
gap of `7/40`. The display defect is likely editorial; firstness remains
falsified without relying on it.

Evidence: [headline contract](../../evidence/claim_3/claim_contract.json),
[primary-source firstness counterexample](../../evidence/claim_3/firstness_counterexample.json),
[literal-display counterexample](../../evidence/claim_3/counterexample.json),
[independent checker](../../evidence/claim_3/independent_checker.json),
[negative control](../../evidence/claim_3/negative_control.json),
[CPU record](../../evidence/claim_3/runtime_cpu.json), and
[counterexample code](../../code/claim3_lasso_counterexample.py).

The checker recomputes both publication-date orderings, the exact objective
mapping, required semantic matches, the rational gap, and two controls: a
later matching paper and an earlier Ridge-only paper must not falsify
firstness.
