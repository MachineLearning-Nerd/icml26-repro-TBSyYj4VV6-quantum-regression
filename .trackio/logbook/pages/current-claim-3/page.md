# Current verification — Claim 3

**Reviewer verdict: FALSIFIED.**

> Exact claim tested: Corollary 26 states, for query access to `A,b`,
> `r≤n`, every `lambda>0`, and every `epsilon>0`, that the output obeys

`||Ax-b||_2^2 + lambda||x||_1 <= (1+epsilon) min_x (||Ax-b||_2^2 + ||x||_1)`.

## Assumptions and exact output

The right minimand omits lambda. On `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`, the left objective is at least 1 for every real `x`; the
printed right bound is exactly `33/40`. The strict gap is `7/40`, so no output
exists.

The result uses exact rational arithmetic. An independent piecewise checker
confirms both global minima. The `lambda=1` control restores the same objective
on both sides and passes at `x=1/2`.

Source: pinned arXiv lines 1164–1168. The missing lambda is likely a typo; this
falsifies the exact published corollary, not the obvious corrected statement.

Download: [claim contract](../../evidence/claim_3/claim_contract.json),
[exact raw counterexample](../../evidence/claim_3/counterexample.json),
[checker output](../../evidence/claim_3/independent_checker.json), and
[negative control](../../evidence/claim_3/negative_control.json). Executable
sources: [verifier](../../code/claim3_lasso_counterexample.py) and
[independent checker](../../code/claim3_independent_checker.py). Both exit
nonzero if the evidence changes.

## Reproduce

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Run `4dcc3ef6-b753-4ee5-8f92-85ac07cf001a`, commit
`5d50739d3625e94b7efbf7a8ccf9ed3c15b857d3`, deterministic/no seeds, local
single-process CPU, 5 seconds. Environment: Python `3.12.*`,
[pyproject](../../code/pyproject.toml), [uv lock](../../code/uv.lock), and
[CPU record](../../evidence/claim_3/runtime_cpu.json).

## Limit

This falsifies the literal displayed inequality. The preceding prose suggests
that omitting lambda on the right is an editorial error; a corrected corollary
is a different claim.
