# Method

Use one-dimensional data `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`.

For `x>=0`, the left objective is
`(x-1)^2+100x=x^2+98x+1>=1`. For `x<0`, it is
`(x-1)^2-100x=x^2-102x+1>1`. Its global minimum is therefore 1 at `x=0`.

The unweighted right minimand is `(x-1)^2+|x|`. For `x>=0`, completing the
square gives `(x-1/2)^2+3/4`; for `x<0` it exceeds 1. Its global minimum is
`3/4`, so the stated right bound is `(11/10)(3/4)=33/40<1`.

The main verifier and a separately implemented piecewise checker use exact
`Fraction` arithmetic and exit nonzero unless the contradiction and
`lambda=1` control both hold.

This is route 2 of a four-route headline audit. Route 1 reconstructs the exact
source statement and quantifiers. Route 3 audits the corrected proof chain
and available implementation evidence. Route 4 attempts to falsify the
repaired headline runtime and records that no oracle-model lower bound or
other assumption-satisfying counterexample was established. Machine-readable
results are in `raw/routes.json`.
