# Claim 2 evaluation

Verdict: **FALSIFIED**. Confidence: **HIGH**.

The exact proposed chain explicitly processes
`M=Theta~(n/epsilon^2)` samples. For fixed valid `m=16,n=2,r=1`, the corollary
permits `epsilon=2^-q`; `M` then leaves the cited sampler's `M<=m` domain and
grows one full inverse-epsilon power faster than the displayed runtime.

The independent checker confirms the exact source chain, assumptions,
universal epsilon quantifier, power gap, and a control at
`epsilon=sqrt(n/m)` where no contradiction is triggered. Historical finite
sampling results remain corroborative only.

The supplemental quantum-sampled linear solve reaches objective ratio
`1.0000041750` at `m=2048,n=8,K=256`; the same executable rejects the three
larger exact all-epsilon calls. This answers the live judge's absence-of-
quantum-execution criticism without using finite success as the falsification.
