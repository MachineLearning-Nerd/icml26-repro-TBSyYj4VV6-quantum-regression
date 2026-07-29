# Primary-source audit

Paper: **Accelerating Regression Tasks with Quantum Algorithms**, OpenReview
`TBSyYj4VV6`, arXiv [`2509.24757`](https://arxiv.org/abs/2509.24757).

Pinned public source archive SHA-256:
`bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549`.

The e-print provides all theorem statements, runtime expressions, assumptions,
and the Ridge/Lasso augmentations. The anchored contract is source-complete and
does not depend on unavailable quantum hardware or an empirical benchmark.

| Claim | Primary source anchor | CPU reproduction route |
|---|---|---|
| C1 | Theorem 10 / formal Theorem 10 source statement | Symbolic GLM sparsifier size/runtime and `m`-speedup dominance checks |
| C2 | Corollary 23 (linear regression) | Exact runtime reduction and classical-comparator inequalities |
| C3 | Corollary 26 (Lasso) | Literal augmented-loss reduction and runtime-family audit |
| C4 | Corollary 25 (Ridge) | Exact augmented matrix identity and linear-regression runtime transfer |
| C5 | Corollary 12 / `γ_p`, `p=1` Huber specialization | Piecewise loss/properness and runtime specialization checks |
| C6 | Corollary 11 (`ℓ_p`) | Parameter-grid checks for `p∈(0,2]` and the `m≫n` quadratic-speedup regime |

Finite executable checks will validate each explicit construction and reject a
removed assumption or wrong reduction. They will be reported as finite
construction audits, not replacements for the paper's universal quantum
algorithm proofs.

## Source precision note

The displayed Lasso corollary's right-hand minimand omits `λ` on its final
`‖x‖₁` term, while the preceding reduction and the corollary's left-hand side
both use the standard `λ‖x‖₁` objective. This project therefore audits the
anchored runtime claim and the explicitly stated preceding reduction with
`λ` retained; it does not silently treat the display typo as a different Lasso
objective.
