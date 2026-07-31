# Method

Use one-dimensional data `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`.

For `x>=0`, the left objective is
`(x-1)^2+100x=x^2+98x+1>=1`. For `x<0`, it is
`(x-1)^2-100x=x^2-102x+1>1`. Its global minimum is therefore 1 at `x=0`.

The unweighted right minimand is `(x-1)^2+|x|`. For `x>=0`, completing the
square gives `(x-1/2)^2+3/4`; for `x<0` it exceeds 1. Its global minimum is
`3/4`, so the stated right bound is `(11/10)(3/4)=33/40<1`.

The display verifier and a separately implemented piecewise checker use exact
`Fraction` arithmetic and exit nonzero unless the contradiction and
`lambda=1` control both hold.

For firstness, the verifier compares primary arXiv publication timestamps,
checks that arXiv:2312.14141 writes the penalized squared-loss/L1 objective,
maps its `lambda` family exactly to the target family, and checks that it
actually supplies quantum algorithms and classical Lasso outputs. A second
pre-target quantum Lasso paper, arXiv:2110.13086, is checked independently.
A later matching paper and an earlier Ridge-only paper are negative controls.
