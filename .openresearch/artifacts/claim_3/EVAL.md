# C3 evaluation

Headline verdict: **FALSIFIED**

For the source-valid instance `A=[1]`, `b=[1]`, `lambda=100`, and
`epsilon=1/10`, the smallest possible left side in Corollary 26 is exactly 1.
The right-hand side printed in the corollary is exactly `33/40`. Because
`1>33/40`, no output can satisfy the approximation display as printed.

The independent checker re-derives both global minima by separate piecewise
completion-of-square arguments. With `lambda=1`, the control output `x=1/2`
has left value `3/4 <= 33/40`, so the checker does not reject the corrected
special case.

The missing lambda is likely a paper typo. The headline firstness component
is independently falsified: arXiv:2312.14141 (2023) gives quantum algorithms
for the same penalized Lasso objective family, and arXiv:2110.13086 (2021)
gives another quantum Lasso algorithm. Both predate the target (2025).
Date ordering, objective mapping, semantic requirements, and two negative
controls are recomputed by the independent checker.

The pre-target simple quantum LARS algorithm is also executed with
statevector Grover/Dürr–Høyer search. All 40 seeded cells pass independent
KKT and objective checks; the oracle-disabled control succeeds only 2/40
times.
