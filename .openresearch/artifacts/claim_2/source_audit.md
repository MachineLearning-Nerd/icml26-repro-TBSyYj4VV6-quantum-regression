# Claim 2 source audit

Corollary 23 is at lines 1150–1153 of the pinned arXiv source. The statement
quantifies over query-access matrices and vectors, `r ≤ n`, and every
`epsilon > 0`; success is with high probability. Its proof invokes the quantum
leverage-score routine from Theorem 19, samples a spectral approximation, and
then uses a classical linear solver.

The corollary is a universal algorithmic/runtime theorem. A finite CPU
simulation can test the target sampling distribution and regression output,
but cannot verify the quantum query/runtime bound or an all-algorithms lower
bound.
