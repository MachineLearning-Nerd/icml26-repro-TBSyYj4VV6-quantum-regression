# Claim 4 source audit

Corollary 25 is at lines 1160–1163 of the pinned source. It reduces Ridge to
linear regression by appending `sqrt(lambda) I` to `A` and zeros to `b`, then
inherits Corollary 23. The objective identity is valid.

The fixed `n`-row augmentation does not repair the inherited contract:
the proposed sparsification chain still explicitly processes
`M=Theta~(n/epsilon^2)` samples and invokes a sampler stated only for
`M<=m+n`, while the corollary permits every `epsilon>0` and displays only
`epsilon^-1` dependence at fixed dimensions.
