# Current verification — Claim 3

**Reviewer verdict: FALSIFIED.**

Corollary 26 states, for every `lambda>0`, that the output obeys

`||Ax-b||_2^2 + lambda||x||_1 <= (1+epsilon) min_x (||Ax-b||_2^2 + ||x||_1)`.

The right minimand omits lambda. On `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`, the left objective is at least 1 for every real `x`; the
printed right bound is exactly `33/40`. The strict gap is `7/40`, so no output
exists.

The result uses exact rational arithmetic. An independent piecewise checker
confirms both global minima. The `lambda=1` control restores the same objective
on both sides and passes at `x=1/2`.

Source: pinned arXiv lines 1164–1168. The missing lambda is likely a typo; this
falsifies the exact published corollary, not the obvious corrected statement.

Reproduce with the project’s fixed command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```
