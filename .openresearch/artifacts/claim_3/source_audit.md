# Claim 3 source audit

Corollary 26 is at lines 1164–1168 of the pinned arXiv source. It assumes
`lambda>0`, query access to `A` and `b`, row sparsity `r<=n`, and
`epsilon>0`. Its left side contains `lambda ||x||_1`, but its right-hand
minimand contains `||x||_1` without `lambda`.

The preceding prose describes the intended standard Lasso reduction with
lambda. That likely makes the display an editorial error, but the evaluator
claim cites Corollary 26 and the exact displayed universal statement is what
this contract tests. A corrected corollary is a different claim.
