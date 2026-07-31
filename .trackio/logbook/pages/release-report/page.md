# Historical release report — superseded

This page is retained for historical reachability. The canonical current
navigation is [Index](#/index), and the current claim pages are Claim 1
through Claim 6 in that fixed order.

Previous live judged score: `0/12`

Conservative projected score range after this change: **0–2/12**.

Best-supported possible new score: **2/12 (forecast, not a judge result)**.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 0 | 2 | HIGH | FALSIFIED | The exact named Algorithm 2 violates its cited sampler domain and has an incompatible explicit epsilon-power cost. |
| 2 | 0 | 0 | LOW | BLOCKED | Four routes provide finite corroboration but no quantum runtime certificate or valid counterexample. |
| 3 | 0 | 0 | LOW | BLOCKED | The printed minimand’s lambda omission is contradicted exactly, but firstness and the repaired runtime remain unresolved. |
| 4 | 0 | 0 | LOW | BLOCKED | Ridge augmentation is exact; the inherited Claim 2 runtime is uncertified. |
| 5 | 0 | 0 | LOW | BLOCKED | Huber specialization works; the named quantum subroutines are not implemented or certified. |
| 6 | 0 | 0 | LOW | BLOCKED | Finite checks do not certify the universal quantum speedup, and the full p-domain proof chain remains unresolved. |

Claim 1 changed from INCONCLUSIVE to a candidate FALSIFIED result. Claims
2–6 are BLOCKED at headline scope. Claim 3’s exact display-level defect is
retained as a scoped subfinding. The current score remains `0/12`.

## Evaluator-visible matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](#/claim-1) | [verifier](../../code/claim1_runtime_audit.py) | Yes | [raw](../../evidence/claim_1/runtime_audit.json) | [output](../../evidence/claim_1/independent_checker.json) | [output](../../evidence/claim_1/negative_control.json) | Yes | FALSIFIED |
| 2 | [Claim 2](#/claim-2) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_2/routes.json) | [output](../../evidence/claim_2/independent_checker.json) | [output](../../evidence/claim_2/negative_control.json) | Yes | BLOCKED |
| 3 | [Claim 3](#/claim-3) | [verifier](../../code/claim3_lasso_counterexample.py) | Yes | [four routes](../../evidence/claim_3/routes.json) | [output](../../evidence/claim_3/independent_checker.json) | [output](../../evidence/claim_3/negative_control.json) | Yes | BLOCKED |
| 4 | [Claim 4](#/claim-4) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_4/routes.json) | [output](../../evidence/claim_4/independent_checker.json) | [output](../../evidence/claim_4/negative_control.json) | Yes | BLOCKED |
| 5 | [Claim 5](#/claim-5) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_5/routes.json) | [output](../../evidence/claim_5/independent_checker.json) | [output](../../evidence/claim_5/negative_control.json) | Yes | BLOCKED |
| 6 | [Claim 6](#/claim-6) | [routes](../../code/remaining_claim_routes.py) | Yes | [raw](../../evidence/claim_6/routes.json) | [output](../../evidence/claim_6/independent_checker.json) | [output](../../evidence/claim_6/negative_control.json) | Yes | BLOCKED |

The exact publication action is a text-only update to the existing Space
`DineshAI/TBSyYj4VV6`. No second Space is created.
