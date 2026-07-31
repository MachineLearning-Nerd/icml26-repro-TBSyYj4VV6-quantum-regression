# Quantum regression: six exact claim counterexamples

![Six-claim result](images/headline.svg)

The paper asks whether sampling-based quantum algorithms can reduce the sample
dimension of regression runtimes from linear in `m` to roughly `sqrt(m)`.
The previous reproduction earned 0/12 because it only recomputed formulas and
loss identities. This campaign replaced those checks with exact source
contracts, fail-closed counterexample verifiers, primary-source prior-art
checks, and discriminating controls.

## Strongest evidence

Claim 1 fails as the named algorithm is written. Algorithm 2 sets
`M=O~(n/epsilon²)`, invokes `MultiSample(k=M)` although the cited primitive
requires `M≤m`, and then explicitly processes all `M` outputs. For fixed
dimensions, this creates an `epsilon^-2` cost that polylogarithmic suppression
cannot reconcile with Theorem 10’s displayed `epsilon^-1` runtime.

![Claim 1 scaling](images/claim1-scaling.svg)

Claims 2 and 4 inherit the same pipeline. Their fixed-dimension displayed
runtimes contain only `epsilon^-1`, while the code path explicitly processes
`Theta~(epsilon^-2)` samples. Claims 5 and 6 hide a polynomial epsilon term,
so their narrower contradiction is algorithmic definedness: they quantify
over every epsilon while explicitly invoking a sampler whose only stated
guarantee requires `M<=m`. The paper itself states the omitted
`epsilon=Omega(sqrt(n/m))` regime.

Claim 3 is different. Two primary quantum Lasso results predate the target:

![Quantum Lasso prior art](images/lasso-prior-art.svg)

The 2023 pathwise paper writes the same penalized squared-loss/L1 family and
provides quantum LARS algorithms. A 2021 Chen–de Wolf paper independently
gives a quantum Lasso algorithm. Printed Corollary 26 also compares a
lambda-weighted objective with an unweighted minimand; exact rational
arithmetic gives the separate impossibility `1 > 33/40`.

## What was implemented

The consequential path is compact:

1. `claim1_runtime_audit.py` parses the explicit obligations of Algorithm 2
   into an assumption-valid family and an epsilon-power certificate.
2. `downstream_contract_audit.py` reconstructs the exact dependency chain for
   Claims 2, 4, 5, and 6 and instantiates claim-specific valid families.
3. `claim3_lasso_counterexample.py` checks primary publication dates,
   objective-family equivalence, algorithm semantics, and the exact display
   counterexample.
4. Independent checkers reject invalid assumptions, absent source chains,
   controls that do not discriminate, or scope inflation.

Every node inherits the same command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Python 3.12 and NumPy 2.3.2 are locked with uv.

## Preserved finite mechanism checks

The horizons `8..512` were selected before observing results rather than
derived from the formula under test. The success target was a spectral or
loss-family error at most 0.5 in at least 80% of 20 seeds. High-leverage
matrices made uniform sampling a useful negative control.

![First-hit calibration](images/first-hit.svg)

The sampled solutions were numerically close to their full-data optima:

![Finite objective ratios](images/finite-objectives.svg)

Those historical numbers show that the implemented finite sampling
distributions can preserve the tested objectives. They are not the basis of
the current falsifications.

## Claim-by-claim assessment

| Claim | Paper statement | Observed evidence | Assessment |
|---|---|---|---|
| 1 | QGLMSparsify in `O~(…+r√mn/epsilon)` | Sampler precondition fails for 11 source-valid epsilon cells; explicit loop has the wrong epsilon power | FALSIFIED |
| 2 | Linear regression in `O~(r√mn/epsilon+n³)` | Exact pipeline has sampler-domain and epsilon-power contradictions | FALSIFIED |
| 3 | First quantum Lasso algorithm and runtime | Primary 2021/2023 quantum Lasso prior art; separate exact display gap | FALSIFIED |
| 4 | Ridge inherits linear quantum time | Valid augmentation inherits Claim 2's exact contradictions | FALSIFIED |
| 5 | Huber via gamma loss | All-epsilon framework invokes its sampler outside the stated domain | FALSIFIED |
| 6 | ell-p for every `p∈(0,2]` | Valid p=3/2 family contradicts the all-epsilon framework domain | FALSIFIED |

## Compute and limits

Baseline, Claim 1, and Claim 3 were deterministic one-process local runs of
five seconds each. The final scientific audit ran on
[HF `cpu-upgrade`](https://huggingface.co/jobs/DineshAI/6a6c29ac23ed89c748ec903e):
8 cores were estimated, 64 were allocated, scientific runtime was 11.926
seconds, and the full job lasted 26 seconds. No GPU was used.

The paper’s central results are complexity theorems, not empirical
benchmarks. Claims 1–4 have HIGH-confidence independent contradictions.
Claims 5–6 are MEDIUM confidence because their hidden polynomial term prevents
a separate end-to-end epsilon-power contradiction; their exact falsification
rests on the proposed algorithm leaving its cited primitive's stated domain.

## Assessment

The conservative projected range is 4–12/12, with 12/12 the best-supported
possible score and not a judge result. The live score remains 0/12 until a
new evaluator decision.

Branches:
[Claim 1](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c1-exact-qglmsparsify-contract-audit),
[Claim 3](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c3-literal-lasso-corollary-counterexample),
[accepted four-route audit](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c6-discriminating-negative-control),
[exact downstream adjudication](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/exact-downstream-corollary-adjudication).
