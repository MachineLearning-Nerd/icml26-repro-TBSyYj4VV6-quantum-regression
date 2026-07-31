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

Evidence: [contract](../../evidence/claim_5/claim_contract.json),
[raw contract audit](../../evidence/claim_5/downstream_contract_audit.json),
[independent checker](../../evidence/claim_5/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_5/negative_control.json),
[CPU record](../../evidence/claim_5/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py).

This does not rule out a repaired Huber algorithm with the omitted epsilon
restriction.
