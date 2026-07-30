# Current reproduction campaign

This reproduction tests all six claimed quantum regression runtimes in
arXiv:2509.24757. Claims 1 and 3 are **FALSIFIED as literally published**:
Algorithm 2 violates its cited sampler’s `M≤m` domain and has an explicit
`epsilon^-2` loop despite Theorem 10’s `O~(epsilon^-1)` bound; Corollary 26
omits lambda from its right minimand and has an exact one-dimensional
counterexample (`1 > 33/40`). Claims 2, 4, 5, and 6 are **BLOCKED** after four
distinct routes each because finite coreset simulations cannot certify
universal quantum runtimes and no valid counterexample was found.

The previous live score remains **0/12**. A conservative forecast for a new
judge revision is **0–4/12**, with **4/12 the best-supported possibility, not
a judge result**. All formal runs were CPU-only: short one-process checks ran
locally; the multi-core four-route audit used Hugging Face `cpu-upgrade`
(estimated 8 cores, allocated 64, 6.951 seconds scientific runtime).

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
| [`orx/c3-literal-lasso-corollary-counterexample`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c3-literal-lasso-corollary-counterexample) | Exact Corollary 26 counterexample | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Claim 3 FALSIFIED | Local, one process, 5s |
| [`orx/c2-c4-c5-c6-four-route-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c2-c4-c5-c6-four-route-audit) | Four-route universal-claim audit | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Rejected: C6 uniform control was nondiscriminating | HF `cpu-upgrade`, 64 CPUs, 9.241s scientific |
| [`orx/c6-discriminating-negative-control`](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c6-discriminating-negative-control) | Replace C6 control and rerun cumulative suite | `uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py` | Claims 2/4/5/6 BLOCKED; checker passed | HF `cpu-upgrade`, 64 CPUs, 6.951s scientific, 21s job |

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
