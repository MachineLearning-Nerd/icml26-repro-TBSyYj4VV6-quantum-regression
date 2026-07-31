# Current reproduction campaign

This reproduction tests all six requested claims in arXiv:2509.24757. All six
are now **FALSIFIED at their exact stated scope**. Claims 1, 2, and 4 have an
explicit `epsilon^-2` processing step incompatible with their printed
fixed-dimension `epsilon^-1` runtimes. Claims 5 and 6 quantify over every
epsilon while explicitly invoking a sampler whose cited guarantee requires
`M≤m`; the paper itself states the omitted
`epsilon=Omega(sqrt(n/m))` condition. Claim 3’s firstness is contradicted by
primary quantum Lasso papers from 2021 and 2023, before the target’s 2025
publication; its printed corollary also has the exact gap `1 > 33/40`.

The previous live score remains **0/12**. A conservative forecast for a new
judge revision is **4–12/12**, with **12/12 the best-supported possibility,
not a judge result**. Claims 5–6 retain MEDIUM confidence because their
falsification is a subroutine-domain contradiction rather than a separate
end-to-end power lower bound. All formal runs are CPU-only.

Read the [illustrated report](reports/quantum-regression/report.md), open the
[self-contained marimo notebook](notebooks/quantum_regression_reproduction.py),
or inspect the [current evaluator logbook](.trackio/logbook/pages/index.md).
The Molab notebook opens with embedded evidence and does not rerun formal
experiments:
[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/blob/main/notebooks/quantum_regression_reproduction.py)

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Publication surface | Not run as an experiment (publication surface) | Mirrors the accepted candidate | N/A |
| [`orx/judged-baseline-with-locked-uv-environment`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/judged-baseline-with-locked-uv-environment) | Freeze judged arithmetic baseline and uv lock | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Historical rejected baseline; live judge 0/12 | Local, one process, 5s |
| [`orx/c1-exact-qglmsparsify-contract-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c1-exact-qglmsparsify-contract-audit) | Exact Algorithm 2/Theorem 10 contract | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Claim 1 FALSIFIED | Local, one process, 5s |
| [`orx/c3-literal-lasso-corollary-counterexample`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c3-literal-lasso-corollary-counterexample) | Exact Corollary 26 display counterexample | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Scoped defect found; headline Claim 3 BLOCKED | Local, one process, 5s |
| [`orx/c2-c4-c5-c6-four-route-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c2-c4-c5-c6-four-route-audit) | Four-route universal-claim audit | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Rejected: C6 uniform control was nondiscriminating | HF `cpu-upgrade`, 64 CPUs, 9.241s scientific |
| [`orx/c6-discriminating-negative-control`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c6-discriminating-negative-control) | Replace C6 control and rerun cumulative suite | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Claims 2/4/5/6 BLOCKED; checker passed | HF `cpu-upgrade`, 64 CPUs, 6.951s scientific, 21s job |
| [`orx/exact-downstream-corollary-adjudication`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/exact-downstream-corollary-adjudication) | Exact downstream contracts, prior-art audit, cumulative gate | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Claims 1–6 FALSIFIED; full gate passed | [HF `cpu-upgrade`](https://huggingface.co/jobs/DineshAI/6a6c29ac23ed89c748ec903e), 64 CPUs, 11.926s scientific, 26s job |

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
