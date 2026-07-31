# Claim 4 — Ridge regression

**Verdict: BLOCKED. Confidence: LOW.**

> Ridge regression is solved in
> `O~(r*sqrt(mn)/epsilon+n^3)` quantum time versus
> `O~(mr+poly(n,1/epsilon))` classically (Corollary 25).

The exact source assumes `lambda>0`, query access, `r<=n`, and
`epsilon>0`, and transfers Corollary 23 through
`[A;sqrt(lambda)I],[b;0]`.

Four routes checked the proof chain, the exact augmentation, finite sampled
solves, calibrated first-hit distributions, negative controls, and a scalar
counterexample search. At `lambda=0.5,m=2048,k=256`, the full-objective ratio
was `1.0002072182`; the augmentation remained exact. No valid counterexample
or quantum runtime certificate was found.

Evidence: [contract](../../evidence/claim_4/claim_contract.json),
[four routes](../../evidence/claim_4/routes.json),
[independent checker](../../evidence/claim_4/independent_checker.json),
[negative control](../../evidence/claim_4/negative_control.json), and
[CPU record](../../evidence/claim_4/runtime_cpu.json).

The reduction is verified, but the inherited universal quantum runtime is
BLOCKED.
