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

Evidence: [contract](../../evidence/claim_4/claim_contract.json),
[raw contract audit](../../evidence/claim_4/downstream_contract_audit.json),
[independent checker](../../evidence/claim_4/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_4/negative_control.json),
[CPU record](../../evidence/claim_4/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py).

This falsifies the inherited proposed runtime, not the Ridge augmentation or
every possible repaired quantum Ridge algorithm.
