# C1 evaluation

Verdict: **FALSIFIED**

The exact written contract for the proposed `QGLMSparsify` algorithm is
contradicted. Theorem 10 quantifies over every `epsilon>0`; Algorithm 2 sets
`M=Theta~(n/epsilon^2)`, calls a primitive whose cited domain requires `M<=m`,
then explicitly processes all `M` outputs. On the source-valid fixed-dimension
family in `raw/runtime_audit.json`, every tested epsilon violates the primitive
domain, and the required processing has epsilon exponent 2 while the claimed
runtime has exponent 1. Suppressed polylogarithms cannot absorb that gap.

The independent checker exits zero only when the domain violation, exponent
gap, and negative control all have the expected values. The threshold control
`epsilon=sqrt(n/m)` yields `M=m` and no runtime contradiction.

This verdict is scoped to the paper’s exact proposed algorithm/runtime
contract. It does not assert an impossibility result for every quantum GLM
sparsification algorithm. A repaired theorem with an explicit
`epsilon=Omega(sqrt(n/m))` restriction or a dense-return branch would be a
different statement.
