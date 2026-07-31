# Claim 1 — GLM sparsification

**Verdict: FALSIFIED. Confidence: HIGH.**

> The proposed quantum algorithm constructs epsilon-approximate GLM
> sparsifiers in
> `O~((r*sqrt(mn)/epsilon + poly(n))*log(s_max/s_min))` time, giving a
> quadratic speedup in `m` over classical `O~(mr)` (Theorem 10).

The exact source expands `poly(n)` as `n^omega+n*r^2`. Its quantifiers cover
every `epsilon>0`, row sparsity `r<=n`, every proper loss family, and
`s_max>s_min>=0`, with high-probability output.

For the proper quadratic-loss family with `n=2,m=16,r=1`, Algorithm 2 sets
`M=Theta~(n/epsilon^2)`, passes `M` to `MultiSample`, and explicitly processes
all `M` samples. The paper's cited `MultiSample` statement requires `M<=m`.
For eleven source-valid epsilon cells, `M>m`; at fixed dimensions the explicit
loop is `Omega(epsilon^-2)`, which polylogarithms cannot fit inside the claimed
`O~(epsilon^-1)` runtime. At the negative-control threshold
`epsilon=sqrt(n/m)`, both contradictions disappear.

Representative raw results:

| epsilon | M | M<=m | M / displayed runtime terms |
|---:|---:|:---:|---:|
| 0.25 | 32 | false | 0.981 |
| 0.0625 | 512 | false | 5.094 |
| 0.00390625 | 131,072 | false | 89.889 |
| 0.000244140625 | 33,554,432 | false | 1,447.530 |

## Executed quantum stage

The supplemental statevector verifier reconstructs the cited Hamoudi
good/bad circuit and performs its amplitude-amplification reflections and
measurements. Across four in-domain cells up to `N=2048,K=256`, coarse
distribution TV was `0.0881, 0.0295, 0.0259, 0.0207`. It then executed the
target call contract on non-toy witnesses:

| m | n | epsilon | requested M | M/m | result |
|---:|---:|---:|---:|---:|---|
| 2,048 | 8 | 0.03125 | 8,192 | 4 | rejected: `K>N` |
| 8,192 | 8 | 0.015625 | 32,768 | 4 | rejected: `K>N` |
| 32,768 | 8 | 0.0078125 | 131,072 | 4 | rejected: `K>N` |

At `m=M=8,192`, the circuit constructs, so the control distinguishes the
paper's valid and invalid regimes.

Evidence: [contract](../../evidence/claim_1/claim_contract.json),
[11-cell raw audit](../../evidence/claim_1/runtime_audit.json),
[independent checker](../../evidence/claim_1/independent_checker.json),
[checker code](../../code/claim1_independent_checker.py),
[negative control](../../evidence/claim_1/negative_control.json),
[CPU record](../../evidence/claim_1/runtime_cpu.json), and
[verifier](../../code/claim1_runtime_audit.py). Supplemental:
[statevector raw data](../../evidence/claim_1/quantum_statevector_audit.json),
[independent checker](../../evidence/claim_1/quantum_statevector_checker.json),
[formal HF run](../../evidence/claim_1/formal_statevector_run.json),
[statevector code](../../code/quantum_statevector_audit.py), and
[checker code](../../code/quantum_statevector_checker.py).

Fixed command:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

This falsifies the published named-algorithm/runtime contract, not every
possible quantum sparsification algorithm. A new dense-return branch or an
`epsilon=Omega(sqrt(n/m))` restriction would be a repaired claim.

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_c1_supp_scale_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed audit at m=2^18"}
-->
## Supplemental executed audit at m=2^18

A second, independent executed audit at `m=262144, n=64, r=8` establishes both halves of the picture. **In-regime** (`epsilon >= sqrt(n/m)`): the executed realization of Algorithm 2's sampling core (steps 5-10; identical output law to the quantum sampler, which changes only query cost) delivers the promised epsilon-sparsifier — spectral deviation at most `0.61*eps` and end-to-end solve ratio within `1+eps` on 10/10 seeds at each epsilon. **Out-of-regime**: the sweep measures the first `MultiSample` domain violation at `epsilon=0.0625` and the first crossing of the `sqrt(mn)/epsilon` runtime envelope by the explicit loop at `epsilon=0.25` — each exactly one halving step under its predicted constant (`eps*_dom = sqrt(C n ln n/m) = 0.063729`; `eps*_loop = C ln(n) sqrt(n/m) = 0.259930`). Together: the universal `epsilon>0` wording is falsified by the missing precondition, while the restricted-regime theorem — with the `epsilon = Omega(sqrt(n/m))` condition the paper itself derives after Corollary 23, plus a one-line dense fallback (`if M >= m return w=1`, cost `O(m) <= O~(sqrt(mn)/epsilon)` there) — is provable.

```bash
python code/claim1_regime_execution.py
```

````output
Claim 1 / Theorem 10 executed audit
instance: m=262144 n=64 r=8 M=ceil(4*n*ln(n)/eps^2) seeds=0..9
Part A - in-regime execution of Algorithm 2 sampling core:
  eps=0.5    M=4259   M<=m=True max_spectral_dev=0.303842 within_eps=True max_obj_ratio=1.019357 within_1+eps=True
  eps=0.25   M=17035  M<=m=True max_spectral_dev=0.151221 within_eps=True max_obj_ratio=1.005346 within_1+eps=True
  eps=0.125  M=68140  M<=m=True max_spectral_dev=0.069271 within_eps=True max_obj_ratio=1.001416 within_1+eps=True
Part B - boundary sweep (MultiSample domain and loop envelope):
  eps=0.5          M=4259         M<=m=True  M<=sqrt(mn)/eps=True
  eps=0.25         M=17035        M<=m=True  M<=sqrt(mn)/eps=False
  eps=0.125        M=68140        M<=m=True  M<=sqrt(mn)/eps=False
  eps=0.0625       M=272557       M<=m=False M<=sqrt(mn)/eps=False
  eps=0.03125      M=1090227      M<=m=False M<=sqrt(mn)/eps=False
  eps=0.015625     M=4360905      M<=m=False M<=sqrt(mn)/eps=False
  eps=0.0078125    M=17443620     M<=m=False M<=sqrt(mn)/eps=False
  eps=0.00390625   M=69774480     M<=m=False M<=sqrt(mn)/eps=False
  eps=0.00195312   M=279097920    M<=m=False M<=sqrt(mn)/eps=False
  eps=0.000976562  M=1116391677   M<=m=False M<=sqrt(mn)/eps=False
  eps=0.000488281  M=4465566708   M<=m=False M<=sqrt(mn)/eps=False
  eps=0.000244141  M=17862266831  M<=m=False M<=sqrt(mn)/eps=False
  eps=0.00012207   M=71449067324  M<=m=False M<=sqrt(mn)/eps=False
predicted domain boundary eps*_dom = sqrt(C n ln n / m) = 0.063729
predicted loop-envelope boundary eps*_loop = C ln(n) sqrt(n/m) = 0.259930
measured first out-of-domain eps = 0.0625; measured first loop>envelope eps = 0.25
each measured boundary sits one halving step under its prediction: True
negative control: eps=eps*=0.063729 gives M=262144 <= m=262144: True
RESULTS_SHA256=7430ab58474ebb87dbe5eb8f07399438c2fa0bb2aeff8892679d6129c145dff0
````

Environment: HF `cpu-upgrade`, nominal 8 vCPU (64 visible logical CPUs),
Python 3.12.12, NumPy 2.3.2, deterministic seeds; the cumulative
[formal run](https://huggingface.co/jobs/DineshAI/6a6c487223ed89c748ec92d4)
finished in 6m43s. Printed floats are rounded before printing, and
`RESULTS_SHA256` fingerprints the results. See the
[compute record](../../evidence/release/supplemental_hf_run.json).

Supplemental evidence: [executed stdout](../../evidence/claim_1/regime_execution_stdout.txt) and [executed script](../../code/claim1_regime_execution.py).
