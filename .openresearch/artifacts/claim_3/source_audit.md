# Claim 3 source audit

Corollary 26 is at lines 1164–1168 of the pinned arXiv source. It assumes
`lambda>0`, query access to `A` and `b`, row sparsity `r<=n`, and
`epsilon>0`. Its left side contains `lambda ||x||_1`, but its right-hand
minimand contains `||x||_1` without `lambda`.

The preceding prose describes the intended standard Lasso reduction with
lambda, so the display defect is likely editorial. The headline firstness
claim is independently contradicted by primary sources:

- arXiv:2312.14141, initially published 2023-12-21, writes
  `(1/2)||y-X beta||_2^2+lambda||beta||_1` and gives quantum LARS algorithms.
  Multiplying by two maps it exactly to the target objective family.
- arXiv:2110.13086, initially published 2021-10-25, proves a quantum Lasso
  algorithm and explicitly relates constrained and penalized formulations.

Both predate the target's 2025-09-29 publication. The target source also
acknowledges the earlier Chen–de Wolf quantum Lasso work at lines 329–330.
