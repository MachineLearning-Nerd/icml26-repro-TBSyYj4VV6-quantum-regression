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

Evidence: [contract](../../evidence/claim_2/claim_contract.json),
[raw contract audit](../../evidence/claim_2/downstream_contract_audit.json),
[independent checker](../../evidence/claim_2/independent_checker.json),
[checker code](../../code/downstream_contract_checker.py),
[negative control](../../evidence/claim_2/negative_control.json),
[CPU record](../../evidence/claim_2/runtime_cpu.json), and
[verifier](../../code/downstream_contract_audit.py).

This falsifies the exact proposed algorithm/runtime contract, not every
conceivable quantum linear-regression algorithm. Restricting epsilon as the
paper's prose does would be a different claim.
