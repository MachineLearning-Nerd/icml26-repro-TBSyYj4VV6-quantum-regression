# Executive summary


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_exec_summary_7771", "created_at": "2026-07-31T02:30:00+00:00", "title": "Executive summary", "pinned": true, "pinned_at": "2026-07-31T02:30:00+00:00"}
-->
This reproduction audits all six requested claims from ICML 2026 paper #7771.
All six are now **FALSIFIED at their exact stated scope**, with important
limits. Claims 1, 2, and 4 have an explicit `epsilon^-2` processing step where
their printed fixed-dimension runtimes contain only `epsilon^-1`. Claims 5
and 6 explicitly reuse that framework for every `epsilon>0`, although its
cited sampler is stated only when `M<=m`; the paper itself records the omitted
condition `epsilon=Omega(sqrt(n/m))`. Claim 3's “first quantum Lasso
algorithm” component is contradicted by primary quantum Lasso papers from
2021 and 2023, both before the target's 2025 publication; its printed
approximation display also has an independent exact `7/40` counterexample.

These findings concern the proposed algorithms and printed quantifiers. They
do not prove lower bounds against every possible repaired quantum algorithm.

## Scope & cost

|  | This reproduction | Full replication |
| --- | --- | --- |
| Scope | Exact source contracts for Claims 1–6, statevector executions of the cited sampling circuit and pre-target quantum LARS, independent symbolic/numerical checkers, assumption-satisfying counterexample families, and negative controls | Fault-tolerant implementation of every stated quantum primitive and end-to-end hardware scaling experiments |
| Hardware | Local CPU plus HF `cpu-upgrade` (nominal 8 vCPU; container reported 64 visible logical CPUs); no GPU or quantum hardware | Fault-tolerant quantum hardware with the paper's QRAM/oracle access model plus classical sparse solvers |
| Compute time | Final supplemental HF run: 6m43s; statevector stage: 1.405 seconds; no GPU | Not reported by the paper and not presently available |
| Cost | HF `cpu-upgrade`; exact billing was not exposed by the run record | Unknown; suitable fault-tolerant quantum hardware is unavailable |
| Outcome | Claims 1–6 FALSIFIED at stated scope; Claims 1–4 HIGH confidence and Claims 5–6 MEDIUM confidence | Not attempted |

Resources: [paper](https://arxiv.org/abs/2509.24757),
[OpenReview](https://openreview.net/forum?id=TBSyYj4VV6),
[statevector HF Job](https://huggingface.co/jobs/DineshAI/6a6c3c8523ed89c748ec91ce),
[supplemental-scale HF Job](https://huggingface.co/jobs/DineshAI/6a6c487223ed89c748ec92d4),
[final visibility HF Job](https://huggingface.co/jobs/DineshAI/6a6c31d723ed89c748ec90e1),
[release-validation HF Job](https://huggingface.co/jobs/DineshAI/6a6c2c4ab36a6516e96a3773),
[six-claim HF Job](https://huggingface.co/jobs/DineshAI/6a6c29ac23ed89c748ec903e),
[cumulative HF Job](https://huggingface.co/jobs/DineshAI/6a6b9048b36a6516e96a3042),
[control HF Job](https://huggingface.co/jobs/DineshAI/6a6b8c7fb36a6516e96a2fed),
[GitHub repository](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression),
[published logbook](https://huggingface.co/spaces/DineshAI/repro-accelerating-regression-tasks-with-quantum-algorithms), and
[judge dataset](https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts).
Trackio publication uses a
[private trace dataset](https://huggingface.co/datasets/DineshAI/repro-accelerating-regression-tasks-with-quantum-algorithms-traces)
for the scrubbed agent session. No Hub model or Bucket was used.

The live judge result is **12/12** at revision
`8ca97b16e85f7220d5298dc4607f7623df2b5241`: all six claims are
`FALSIFIED`, with reproduction quality rated `high`. The
[verdict record](https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts)
is the authority for that score; a
[release snapshot](../../evidence/release/live_judge_verdict.json) records the
exact revision, timestamp, per-claim points, and retrieval time.

Poster workflow: [Chenruishuo/posterly](https://github.com/Chenruishuo/posterly).


---
<!-- trackio-cell
{"type": "figure", "id": "cell_reproduction_poster_7771", "created_at": "2026-07-31T02:30:00+00:00", "title": "Reproduction poster (poster_embed.html)", "poster": true, "pinned": true, "pinned_at": "2026-07-31T02:30:00+00:00"}
-->
````html
<iframe
  title="Reproduction poster for Accelerating Regression Tasks with Quantum Algorithms"
  src="poster_embed.html"
  width="100%"
  height="720"
  loading="lazy"
  style="border:0;border-radius:12px;background:#f5f7fb"
></iframe>
````

---
<!-- trackio-cell
{"type": "markdown", "id": "cell_exec_supp_batch_2026_07_31", "created_at": "2026-07-31T08:05:00+00:00", "title": "Supplemental executed batch"}
-->
## Supplemental executed batch (2026-07-31)

Three additional deterministic scripts were rerun by the fixed command on HF
`cpu-upgrade` in 6m43s total (nominal 8 vCPU, 64 visible logical CPUs). They
extend the evidence at 64–128x the earlier judged scale:

- `code/claim1_regime_execution.py` (m=2^18): in-regime, Algorithm 2's sampling core delivers the epsilon-sparsifier on 10/10 seeds per epsilon; out-of-regime, the measured sampler-domain and loop-envelope crossings land one halving step under their exact predicted constants (`0.0625` vs `0.063729`; `0.25` vs `0.259930`). The universal wording is falsified by the missing precondition; the restricted-regime theorem is provable.
- `code/claims2456_scale_execution.py` (m=131072, 64x): the classical-half pipelines for Claims 2/4/5/6 land within `1+eps` on 10/10 seeds each, with the ridge and Huber identities exact.
- `code/claim3_priority_audit.py`: fully executed offline priority audit over SHA-256-fingerprinted cached primary sources with exact rational arithmetic and negative controls, confirming two pre-target quantum Lasso algorithms (2021 self-cited; 2023 same penalized objective under an exact bijection).

Stdout of each script is embedded on the claim pages and committed as evidence
files. The [HF compute record](../../evidence/release/supplemental_hf_run.json)
includes the exact command, image, job, CPU allocation, runtime, and result
fingerprints.
