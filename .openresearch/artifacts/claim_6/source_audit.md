# Claim 6 source audit

Corollary 11 is at lines 549–551 and quantifies over every `p in (0,2]` and
`epsilon>0`. Lines 546–547 explicitly derive it through
Theorem 10/QGLMSparsify. A valid `p=3/2` instance avoids the separate
`p<=1` solver gap.

For fixed `m=16,n=2,r=1`, its `M=Theta~(n/epsilon^2)` call eventually violates
the cited MultiSample requirement `M<=m`. Line 329 says the speedup requires
`epsilon=Omega(sqrt(n/m))`, but the corollary omits that restriction. The
counterexample therefore targets the universal proposed-algorithm contract,
not the repaired constant-epsilon, `m`-dominant regime.
