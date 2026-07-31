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
