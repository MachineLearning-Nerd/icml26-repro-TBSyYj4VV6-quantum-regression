# Claim 2 source audit

Corollary 23 is at lines 1150–1153 of the pinned arXiv source. The statement
quantifies over query-access matrices and vectors, `r ≤ n`, and every
`epsilon > 0`; success is with high probability. Its proof invokes the quantum
leverage-score routine from Theorem 19, samples a spectral approximation, and
then uses a classical linear solver.

The proposed chain invokes the paper's quantum sparsification framework.
Algorithm 2 sets `M=Theta~(n/epsilon^2)`, calls `MultiSample(Z,M)`, and loops
over all `M` results. The cited MultiSample theorem requires `M<=m`.
Corollary 23 nevertheless quantifies over every `epsilon>0`; line 1153 then
states the missing condition `epsilon=Omega(sqrt(n/m))`.

For fixed valid `m,n,r`, `M` grows as `epsilon^-2` up to polylogarithms while
the displayed runtime grows only as `epsilon^-1`. This directly contradicts
the exact proposed pipeline, without making an all-algorithms lower-bound
claim.

The cited sampler was independently retrieved from arXiv:2207.11014
(SHA-256
`53f2c291c4f4521f019da57a7492684dc09c7f81b0bf09de2ff8536a03e6df5a`);
Theorem 1 and the circuit construction are anchored at
`PRA.tex:108–109,199–215,229–261`.
