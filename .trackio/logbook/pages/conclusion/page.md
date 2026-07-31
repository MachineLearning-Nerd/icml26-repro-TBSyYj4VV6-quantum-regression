# Conclusion

The six requested claims are now represented in the required fixed order and
tested against their full theorem/corollary contracts.

| Claim | Result | What was established |
|---|---|---|
| 1 | FALSIFIED | The named sparsifier violates its cited sampler domain and its explicit loop has an incompatible epsilon power. |
| 2 | BLOCKED | Finite linear-regression sampling corroborates the mechanism but cannot certify the quantum runtime. |
| 3 | BLOCKED | The displayed lambda omission is contradicted exactly; the broader first-algorithm/runtime claim remains unsettled. |
| 4 | BLOCKED | Ridge augmentation is exact; the inherited quantum runtime is uncertified. |
| 5 | BLOCKED | The Huber specialization and finite coreset solve work; the quantum runtime is uncertified. |
| 6 | BLOCKED | Finite ell-p checks work; the full p-domain proof chain and quantum runtime remain unresolved. |

## Evaluator-visible evidence

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](#/claim-1) | [verifier](../../code/claim1_runtime_audit.py) | Yes | [raw](../../evidence/claim_1/runtime_audit.json) | [output](../../evidence/claim_1/independent_checker.json) | [output](../../evidence/claim_1/negative_control.json) | Yes | FALSIFIED |
| 2 | [Claim 2](#/claim-2) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_2/routes.json) | [output](../../evidence/claim_2/independent_checker.json) | [output](../../evidence/claim_2/negative_control.json) | Yes | BLOCKED |
| 3 | [Claim 3](#/claim-3) | [verifier](../../code/claim3_lasso_counterexample.py) | Yes | [four routes](../../evidence/claim_3/routes.json) | [output](../../evidence/claim_3/independent_checker.json) | [output](../../evidence/claim_3/negative_control.json) | Yes | BLOCKED |
| 4 | [Claim 4](#/claim-4) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_4/routes.json) | [output](../../evidence/claim_4/independent_checker.json) | [output](../../evidence/claim_4/negative_control.json) | Yes | BLOCKED |
| 5 | [Claim 5](#/claim-5) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_5/routes.json) | [output](../../evidence/claim_5/independent_checker.json) | [output](../../evidence/claim_5/negative_control.json) | Yes | BLOCKED |
| 6 | [Claim 6](#/claim-6) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_6/routes.json) | [output](../../evidence/claim_6/independent_checker.json) | [output](../../evidence/claim_6/negative_control.json) | Yes | BLOCKED |

All accepted experiments are CPU-only. Local work used one process for short
checks; uncertain or multi-core work used Hugging Face `cpu-upgrade`. No GPU
or quantum hardware was used. The fixed command is:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

The public assets are the
[Hugging Face logbook](https://huggingface.co/spaces/DineshAI/TBSyYj4VV6),
[final accepted HF Job](https://huggingface.co/jobs/DineshAI/6a6c0cee23ed89c748ec8dfb),
[verdict dataset](https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts),
and [GitHub repository](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression).
No Hub model or Bucket was used.

The previous live judge score remains `0/12`. The conservative projected
range is `0–2/12`, with `2/12` the best-supported forecast rather than an
earned score. Only the live judge can change the score.
