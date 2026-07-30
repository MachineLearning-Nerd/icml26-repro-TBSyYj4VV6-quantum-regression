# Quantum regression: exact defects amid unresolved speedups

![Six-claim result](images/headline.svg)

The paper asks whether sampling-based quantum algorithms can reduce the sample
dimension of regression runtimes from linear in `m` to roughly `sqrt(m)`.
The previous reproduction earned 0/12 because it only recomputed formulas and
loss identities. This campaign replaced those checks with exact source
contracts, fail-closed verifiers, finite mechanism tests, calibrated controls,
and dedicated falsification routes.

## Strongest evidence

Claim 1 fails as the named algorithm is written. Algorithm 2 sets
`M=O~(n/epsilon²)`, invokes `MultiSample(k=M)` although the cited primitive
requires `M≤m`, and then explicitly processes all `M` outputs. For fixed
dimensions, this creates an `epsilon^-2` cost that polylogarithmic suppression
cannot reconcile with Theorem 10’s displayed `epsilon^-1` runtime.

![Claim 1 scaling](images/claim1-scaling.svg)

Claim 3 has a separate exact defect. Printed Corollary 26 compares a
lambda-weighted Lasso objective to an unweighted minimand. With `A=[1]`,
`b=[1]`, `lambda=100`, and `epsilon=0.1`, every output has left side at least
`1`, while the allowed right side is `33/40`. Exact rational arithmetic gives
a strict impossibility gap of `7/40`. Setting `lambda=1` is the negative
control and restores a satisfiable inequality.

## What was implemented

The consequential path is compact:

1. `claim1_runtime_audit.py` parses the explicit obligations of Algorithm 2
   into an assumption-valid family and an epsilon-power certificate.
2. `claim3_lasso_counterexample.py` computes both global minima with exact
   fractions.
3. `remaining_claim_routes.py` computes exact classical leverage or grid
   sensitivities, samples and reweights rows, solves finite regressions, then
   performs first-hit sweeps over 20 seeds.
4. Independent checkers reject missing routes, nondiscriminating controls,
   scope inflation, or mislabeled falsification.

Every node inherits the same command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

Python 3.12 and NumPy 2.3.2 are locked with uv.

## Finite mechanism checks

The horizons `8..512` were selected before observing results rather than
derived from the formula under test. The success target was a spectral or
loss-family error at most 0.5 in at least 80% of 20 seeds. High-leverage
matrices made uniform sampling a useful negative control.

![First-hit calibration](images/first-hit.svg)

The sampled solutions were numerically close to their full-data optima:

![Finite objective ratios](images/finite-objectives.svg)

Those numbers show that the implemented finite sampling distributions can
preserve the tested objectives. They do not measure the quantum
leverage-score or QMLSO subroutines, so they cannot verify the universal
runtime claims.

## Claim-by-claim assessment

| Claim | Paper statement | Observed evidence | Assessment |
|---|---|---|---|
| 1 | QGLMSparsify in `O~(…+r√mn/epsilon)` | Sampler precondition fails for 11 source-valid epsilon cells; explicit loop has the wrong epsilon power | FALSIFIED |
| 2 | Linear regression in `O~(r√mn/epsilon+n³)` | Finite ratio `1.000004`; no quantum-runtime certificate or counterexample | BLOCKED |
| 3 | Lasso Corollary 26 | Exact minimum `1` exceeds bound `33/40` | FALSIFIED |
| 4 | Ridge inherits linear quantum time | Finite ratio `1.000207`; inherited runtime unresolved | BLOCKED |
| 5 | Huber via gamma loss | Finite ratio `1.002026`; named quantum runtime unresolved | BLOCKED |
| 6 | ell-p for every `p∈(0,2]` | Finite p=0.5 ratio `1.002983`; cited solver application states p>1 | BLOCKED |

## Compute and limits

Baseline, Claim 1, and Claim 3 were deterministic one-process local runs of
five seconds each. The multi-core audit ran on HF `cpu-upgrade`: 8 cores were
estimated, 64 were scheduler-visible, scientific runtime was 6.951 seconds,
and the full job lasted 21 seconds. No GPU was used.

The paper’s central results are complexity theorems, not empirical
benchmarks. Full verification of Claims 2/4/5/6 needs an exact executable
implementation of the named quantum subroutines or a machine-checkable proof
certificate. The finite checks are deliberately not promoted to full credit.

## Assessment

The strongest supported forecast is 4/12 from the two exact falsifications;
the conservative range is 0–4/12 because only the live evaluator assigns
points. The live score remains 0/12 until that evaluation occurs.

Branches:
[Claim 1](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c1-exact-qglmsparsify-contract-audit),
[Claim 3](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c3-literal-lasso-corollary-counterexample),
[accepted four-route audit](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression/tree/orx/c6-discriminating-negative-control).
