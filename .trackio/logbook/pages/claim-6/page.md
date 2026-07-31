# Claim 6 — ell-p regression

**Verdict: BLOCKED. Confidence: LOW.**

> For `p in (0,2]`, the algorithm achieves a quadratic speedup in sample
> count `m`, which dominates when `m >> n` (Corollary 11).

The full source contract is a high-probability `(1+epsilon)` ell-p regression
solution in `O~(r*sqrt(mn)/epsilon+poly(n,1/epsilon))` time for every
`p in (0,2]`.

Four routes reconstructed the source/reference domain, tested finite sampled
solves at `p=0.5` and `p=1.5`, swept 20-seed first-hit distributions, and
searched for counterexamples over `p={0.25,0.5,1,1.5,2}`. The `p=0.5`
finite objective ratio was `1.0029825893`. A single-row-support negative
control was `0/20` at every horizon.

The primary cited solver application states ell-p regression for
`p in (1,2]`, while this corollary claims `(0,2]`. That is an unresolved
proof-chain gap, not a counterexample.

Evidence: [contract](../../evidence/claim_6/claim_contract.json),
[four routes](../../evidence/claim_6/routes.json),
[independent checker](../../evidence/claim_6/independent_checker.json),
[negative control](../../evidence/claim_6/negative_control.json), and
[CPU record](../../evidence/claim_6/runtime_cpu.json).

Finite classical scaling cannot verify the universal quantum speedup; the
claim remains BLOCKED.
