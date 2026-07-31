# Claim 1 — GLM sparsification

**Verdict: FALSIFIED. Confidence: HIGH.**

> The proposed quantum algorithm constructs epsilon-approximate GLM
> sparsifiers in
> `O~((r*sqrt(mn)/epsilon + poly(n))*log(s_max/s_min))` time, giving a
> quadratic speedup in `m` over classical `O~(mr)` (Theorem 10).

The exact source expands `poly(n)` as `n^omega+n*r^2`. Its quantifiers cover
every `epsilon>0`, row sparsity `r<=n`, every proper loss family, and
`s_max>s_min>=0`, with high-probability output.

For the proper quadratic-loss family with `n=2,m=16,r=1`, Algorithm 2 sets
`M=Theta~(n/epsilon^2)`, passes `M` to `MultiSample`, and explicitly processes
all `M` samples. The paper's cited `MultiSample` statement requires `M<=m`.
For eleven source-valid epsilon cells, `M>m`; at fixed dimensions the explicit
loop is `Omega(epsilon^-2)`, which polylogarithms cannot fit inside the claimed
`O~(epsilon^-1)` runtime. At the negative-control threshold
`epsilon=sqrt(n/m)`, both contradictions disappear.

Representative raw results:

| epsilon | M | M<=m | M / displayed runtime terms |
|---:|---:|:---:|---:|
| 0.25 | 32 | false | 0.981 |
| 0.0625 | 512 | false | 5.094 |
| 0.00390625 | 131,072 | false | 89.889 |
| 0.000244140625 | 33,554,432 | false | 1,447.530 |

Evidence: [contract](../../evidence/claim_1/claim_contract.json),
[11-cell raw audit](../../evidence/claim_1/runtime_audit.json),
[independent checker](../../evidence/claim_1/independent_checker.json),
[checker code](../../code/claim1_independent_checker.py),
[negative control](../../evidence/claim_1/negative_control.json),
[CPU record](../../evidence/claim_1/runtime_cpu.json), and
[verifier](../../code/claim1_runtime_audit.py).

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

This falsifies the published named-algorithm/runtime contract, not every
possible quantum sparsification algorithm. A new dense-return branch or an
`epsilon=Omega(sqrt(n/m))` restriction would be a repaired claim.
