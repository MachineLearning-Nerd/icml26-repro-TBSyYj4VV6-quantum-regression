# C3 evaluation

Verdict: **FALSIFIED**

For the source-valid instance `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`, the smallest possible left side in Corollary 26 is exactly 1.
The right-hand side printed in the corollary is exactly `33/40`. Because
`1>33/40`, no output can satisfy the universally quantified promise.

The independent checker re-derives both global minima by separate piecewise
completion-of-square arguments. With `lambda=1`, the control output `x=1/2`
has left value `3/4 <= 33/40`, so the checker does not reject the corrected
special case.

The missing lambda is likely a paper typo. This verdict applies to the exact
published corollary and not to the obvious corrected statement.
