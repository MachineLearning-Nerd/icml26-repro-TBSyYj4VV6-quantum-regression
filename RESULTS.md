# Results

Run the CPU verification from this directory:

```bash
.venv/bin/python repro/src/verify.py
.venv/bin/python repro/src/publication_gate.py
```

All six anchored claims pass. Machine-readable evidence is in [`outputs/verdict.json`](outputs/verdict.json).

| Claim | Executable construction audit | Negative control |
|---|---|---|
| C1 — GLM sparsification | Theorem-10 leading terms in three `m≫n` regimes | Small-`m` / high-`n` rejects m-dominant speedup |
| C2 — linear regression | Source `m→√m` leading-term change: 64× `m` gives 2× quantum-leading growth | A linear-in-`m` term would leave the ratio constant |
| C3 — Lasso | Stated quadratic-plus-`λℓ₁` loss-family augmentation | Dropping `λ` changes the objective |
| C4 — Ridge | `A'=[A;√λI]`, `b'=[b;0]` objective identity | `λI` rather than `√λI` fails |
| C5 — Huber | `γ₁` exactly equals Huber and joins continuously | Wrong outer offset fails |
| C6 — `ℓ_p` | Homogeneity over `p∈(0,2]` | `p=0` is rejected by the source domain |

## Scope

This executes the finite reductions and runtime relations from the source; it does not run quantum hardware or replace universal quantum-algorithm proofs. The Lasso display typo is disclosed in the source audit, while the source's preceding intended `λℓ₁` reduction is used for the executable identity.
