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
| Compute time | Statevector HF run: 1.484 seconds; preceding cumulative routes: 8.003 seconds; no GPU | Not reported by the paper and not presently available |
| Cost | HF `cpu-upgrade`; exact billing was not exposed by the run record | Unknown; suitable fault-tolerant quantum hardware is unavailable |
| Outcome | Claims 1–6 FALSIFIED at stated scope; Claims 1–4 HIGH confidence and Claims 5–6 MEDIUM confidence | Not attempted |

Resources: [paper](https://arxiv.org/abs/2509.24757),
[OpenReview](https://openreview.net/forum?id=TBSyYj4VV6),
[statevector HF Job](https://huggingface.co/jobs/DineshAI/6a6c3c8523ed89c748ec91ce),
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

Live judge result for revision `1d7460599344b8c93d085a9b283213a9d677ded3`
is `4/12` (Claims 2, 4, 5, 6 received toy credit; Claims 1 and 3 remained
inconclusive). After adding statevector execution, the conservative projected
range remains `4–12/12`; best-supported possible is `12/12`. These are
forecasts only; only a new live judge verdict can change the score.

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
