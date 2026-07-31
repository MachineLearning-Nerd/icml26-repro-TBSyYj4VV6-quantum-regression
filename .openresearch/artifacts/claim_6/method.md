# Claim 6 method

The current verifier chooses `p=3/2`, avoiding the separate nonconvex
`p<=1` issue, and follows the source's explicit QGLMSparsify application on
`m=16,n=2,r=1,epsilon_q=2^-q`. It checks the eventual sampler-domain
violation and the boundary control `epsilon=sqrt(n/m)`.

Preserved historical routes were: reconstruct the proof and cited solver domains; solve finite
`p=0.5` and `p=1.5` sampled problems; calibrate `p=0.5` first-hit behavior over
20 seeds, three `m` values, and seven horizons; and exhaustively check
subadditivity for `p={0.25,0.5,1,1.5,2}` on a scalar grid while searching for a
valid counterexample.

The accepted negative control has support on only one row and therefore cannot
represent the full loss family. The earlier uniform control was rejected
because it passed this easy instance.
