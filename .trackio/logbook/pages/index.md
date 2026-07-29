# Repro - Accelerating Regression Tasks with Quantum Algorithms

## Pages

| Page |
| --- |
| [Claim 1 — GLM sparsification](#/claim-1-glm-sparsification) |
| [Claim 2 — Linear regression](#/claim-2-linear-regression) |
| [Claim 3 — Lasso](#/claim-3-lasso) |
| [Claim 4 — Ridge](#/claim-4-ridge) |
| [Claim 5 — Huber](#/claim-5-huber) |
| [Claim 6 — ell_p](#/claim-6-ell-p) |
| [Methods](#/methods) |
| [Negative controls](#/negative-controls) |
| [Conclusion](#/conclusion) |


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_054406c25f30", "created_at": "2026-07-29T12:47:35+00:00", "title": "Executive summary"}
-->
All six anchored quantum-regression claims pass the local source-faithful gate.

The CPU audit executes runtime-dominance relations, linear/Lasso/Ridge reductions, the gamma_1=Huber specialization, and ell_p homogeneity. No quantum hardware or GPU is claimed or used.

One source precision issue is disclosed: the final Lasso corollary minimand omits lambda, while the preceding reduction and left-hand side retain it.
