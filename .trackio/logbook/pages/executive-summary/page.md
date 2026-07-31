# Executive summary


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_exec_summary_7771", "created_at": "2026-07-31T02:30:00+00:00", "title": "Executive summary", "pinned": true, "pinned_at": "2026-07-31T02:30:00+00:00"}
-->
This reproduction audits all six requested claims from ICML 2026 paper #7771.
Claim 1 is **FALSIFIED** for the exact named Algorithm 2/runtime contract:
the algorithm calls its cited sampler outside the sampler's stated domain and
has an explicit `epsilon^-2` processing cost where the theorem displays
`epsilon^-1`, at fixed dimensions. Claims 2–6 are **BLOCKED**: finite CPU
experiments, four-route audits, independent checkers, and falsification
searches do not establish their universally quantified quantum runtimes.
Claim 3's missing `lambda` is retained as a verified editorial counterexample,
but it is not presented as settling the broader “first quantum Lasso
algorithm/runtime” claim.

## Scope & cost

| Item | Value |
| --- | --- |
| Paper | [arXiv:2509.24757](https://arxiv.org/abs/2509.24757) · [OpenReview TBSyYj4VV6](https://openreview.net/forum?id=TBSyYj4VV6) |
| Compute | CPU only; local one-process checks and Hugging Face `cpu-upgrade`; no GPU or quantum hardware |
| HF jobs | [final cumulative run](https://huggingface.co/jobs/DineshAI/6a6c0cee23ed89c748ec8dfb) · [environment-only failed attempt](https://huggingface.co/jobs/DineshAI/6a6c0cb723ed89c748ec8df7) · [prior cumulative release run](https://huggingface.co/jobs/DineshAI/6a6b9048b36a6516e96a3042) · [four-route/control run](https://huggingface.co/jobs/DineshAI/6a6b8c7fb36a6516e96a2fed) |
| Runtime | 5-second local checks; final HF run used 11.661 seconds scientific time in a 32-second job |
| Code | [MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression) |
| Published logbook | [DineshAI/TBSyYj4VV6](https://huggingface.co/spaces/DineshAI/TBSyYj4VV6) |
| Judge data | [ICML-2026-agent-repro/verdicts](https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts) |
| Models / Buckets | No Hub model or Bucket was used |
| Forecast | Conservative `0–2/12`; `2/12` is a forecast, not a judge result |

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
