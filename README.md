# Current reproduction campaign

Claim 1 is **FALSIFIED** for the exact written `QGLMSparsify`
algorithm/runtime contract: Algorithm 2 invokes its cited sampling primitive
outside the primitive’s stated domain for theorem-valid epsilon values, and its
explicit processing cost grows as `epsilon^-2` while Theorem 10 claims only
`O~(epsilon^-1)` dependence at fixed dimensions. Claims 2–6 remain under
audit; publication is blocked.

Current evidence is in
[`.openresearch/artifacts/claim_1/EVAL.md`](.openresearch/artifacts/claim_1/EVAL.md).
The fixed command is:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

## Historical rejected baseline

The material below describes the preserved verifier that received 0/12 from
the live judge. It is not the current verification.

Source-faithful CPU verification project for ICML 2026 paper `TBSyYj4VV6`
(arXiv `2509.24757`). This project audits six source-anchored quantum
complexity and reduction claims for GLM, linear, Lasso, Ridge, Huber, and
`ℓ_p` regression.

The primary-source audit is in [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md).
