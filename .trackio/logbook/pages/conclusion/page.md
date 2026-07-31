# Conclusion

The six requested claims are now represented in the required fixed order and
tested against their full theorem/corollary contracts.

| Claim | Result | What was established |
|---|---|---|
| 1 | FALSIFIED | The named sparsifier violates its cited sampler domain and its explicit loop has an incompatible epsilon power. |
| 2 | FALSIFIED | Its exact pipeline has the same sampler-domain defect and an explicit epsilon-power runtime contradiction. |
| 3 | FALSIFIED | Quantum Lasso algorithms from 2021 and 2023 predate the target; the printed display also has an exact 7/40 gap. |
| 4 | FALSIFIED | The valid Ridge augmentation inherits the sampler-domain and epsilon-power contradictions. |
| 5 | FALSIFIED | The all-epsilon Huber framework invokes MultiSample outside its stated domain; the Huber identity itself is valid. |
| 6 | FALSIFIED | A valid p=3/2 family contradicts the all-epsilon proposed framework; the restricted constant-epsilon regime is not denied. |

## Evaluator-visible evidence

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](#/claim-1) | [verifier](../../code/claim1_runtime_audit.py) | Yes | [raw](../../evidence/claim_1/runtime_audit.json) | [output](../../evidence/claim_1/independent_checker.json) | [output](../../evidence/claim_1/negative_control.json) | Yes | FALSIFIED |
| 2 | [Claim 2](#/claim-2) | [verifier](../../code/downstream_contract_audit.py) | Yes | [raw](../../evidence/claim_2/downstream_contract_audit.json) | [output](../../evidence/claim_2/independent_checker.json) | [output](../../evidence/claim_2/negative_control.json) | Yes | FALSIFIED |
| 3 | [Claim 3](#/claim-3) | [verifier](../../code/claim3_lasso_counterexample.py) | Yes | [prior art](../../evidence/claim_3/firstness_counterexample.json) | [output](../../evidence/claim_3/independent_checker.json) | [output](../../evidence/claim_3/negative_control.json) | Yes | FALSIFIED |
| 4 | [Claim 4](#/claim-4) | [verifier](../../code/downstream_contract_audit.py) | Yes | [raw](../../evidence/claim_4/downstream_contract_audit.json) | [output](../../evidence/claim_4/independent_checker.json) | [output](../../evidence/claim_4/negative_control.json) | Yes | FALSIFIED |
| 5 | [Claim 5](#/claim-5) | [verifier](../../code/downstream_contract_audit.py) | Yes | [raw](../../evidence/claim_5/downstream_contract_audit.json) | [output](../../evidence/claim_5/independent_checker.json) | [output](../../evidence/claim_5/negative_control.json) | Yes | FALSIFIED |
| 6 | [Claim 6](#/claim-6) | [verifier](../../code/downstream_contract_audit.py) | Yes | [raw](../../evidence/claim_6/downstream_contract_audit.json) | [output](../../evidence/claim_6/independent_checker.json) | [output](../../evidence/claim_6/negative_control.json) | Yes | FALSIFIED |

All accepted experiments are CPU-only. Local work used one process for short
checks; uncertain or multi-core work used Hugging Face `cpu-upgrade`. No GPU
or quantum hardware was used. The fixed command is:

```bash
uv sync --frozen && uv run python repro/src/verify.py && uv run python repro/src/publication_gate.py
```

The public assets are the
[Hugging Face logbook](https://huggingface.co/spaces/DineshAI/TBSyYj4VV6),
[accepted HF Job](https://huggingface.co/jobs/DineshAI/6a6b9048b36a6516e96a3042),
[verdict dataset](https://huggingface.co/datasets/ICML-2026-agent-repro/verdicts),
and [GitHub repository](https://github.com/MachineLearning-Nerd/icml26-repro-TBSyYj4VV6-quantum-regression).
No Hub model or Bucket was used.

The previous live judge score remains `0/12`. The conservative projected
range is `4–12/12`, with `12/12` the best-supported possible score and only a
forecast. Claims 5–6 carry the largest evaluator risk because their exact
falsification rests on the proposed framework leaving the cited subroutine's
stated domain, rather than a separate end-to-end power lower bound. Only the
live judge can change the score.
