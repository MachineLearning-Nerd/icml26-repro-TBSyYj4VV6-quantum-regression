# Visibility matrix and release report

Previous live judged score: `0/12`

Conservative projected score range after this change: **0–4/12**.

Best-supported possible new score: **4/12 (forecast, not a judge result)**.

## Claim forecast

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 0 | 2 | HIGH | FALSIFIED | Exact named Algorithm 2 violates its cited sampler domain and has an explicit epsilon-power contradiction. Judge may interpret an unstated dense fallback as repairing the theorem. |
| 2 | 0 | 0 | LOW | BLOCKED | Four routes corroborate finite sampling but provide no quantum leverage-runtime certificate or counterexample. |
| 3 | 0 | 2 | HIGH | FALSIFIED | Exact rational counterexample makes literal Corollary 26 impossible; risk is that the judge elects to silently repair the omitted lambda. |
| 4 | 0 | 0 | LOW | BLOCKED | Ridge augmentation works, but the inherited Claim 2 quantum runtime remains uncertified. |
| 5 | 0 | 0 | LOW | BLOCKED | Huber coreset simulation works; named quantum subroutines are not implemented or certified. |
| 6 | 0 | 0 | LOW | BLOCKED | Four routes find no counterexample; cited solver’s stated p-range does not cover the full corollary. |

Claims 1 and 3 changed from INCONCLUSIVE to candidate FALSIFIED findings.
Claims 2, 4, 5, and 6 changed from weak arithmetic checks to rigorously
documented BLOCKED results. The current score is still `0/12`.

## Evaluator-visible matrix

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](#/current-claim-1) | [verifier](../../code/claim1_runtime_audit.py) | 6 representative cells | [11 cells](../../evidence/claim_1/runtime_audit.json) | [output](../../evidence/claim_1/independent_checker.json) | [output](../../evidence/claim_1/negative_control.json) | Yes | FALSIFIED |
| 2 | [Claim 2](#/current-claim-2) | [routes](../../code/remaining_claim_routes.py) | Ratios and first hits | [four routes](../../evidence/claim_2/routes.json) | [output](../../evidence/claim_2/independent_checker.json) | [output](../../evidence/claim_2/negative_control.json) | Yes | BLOCKED |
| 3 | [Claim 3](#/current-claim-3) | [verifier](../../code/claim3_lasso_counterexample.py) | Exact fractions | [counterexample](../../evidence/claim_3/counterexample.json) | [output](../../evidence/claim_3/independent_checker.json) | [output](../../evidence/claim_3/negative_control.json) | Yes | FALSIFIED |
| 4 | [Claim 4](#/current-claim-4) | [routes](../../code/remaining_claim_routes.py) | Ratio and first hits | [four routes](../../evidence/claim_4/routes.json) | [output](../../evidence/claim_4/independent_checker.json) | [output](../../evidence/claim_4/negative_control.json) | Yes | BLOCKED |
| 5 | [Claim 5](#/current-claim-5) | [routes](../../code/remaining_claim_routes.py) | Ratio and first hits | [four routes](../../evidence/claim_5/routes.json) | [output](../../evidence/claim_5/independent_checker.json) | [output](../../evidence/claim_5/negative_control.json) | Yes | BLOCKED |
| 6 | [Claim 6](#/current-claim-6) | [routes](../../code/remaining_claim_routes.py) | Ratio and p-domain gap | [four routes](../../evidence/claim_6/routes.json) | [output](../../evidence/claim_6/independent_checker.json) | [output](../../evidence/claim_6/negative_control.json) | Yes | BLOCKED |

All pages expose the fixed command, pinned environment, raw results,
independent checker, negative control, limitations, Git/run provenance, seeds,
and CPU/runtime information directly or through one labeled link.

## Release facts

- Baseline HF Head and Judge Head: `69210c3e5b45e365cb218b0ffd88948bfe81c18e`.
- Winning experiment branch: `orx/evaluator-visible-complete-candidate`.
- Accepted scientific ancestor: commit `e15aace`, run
  `7d8f2bf0-adb1-4e49-940f-df81da9cf5a5`.
- HF compute: `cpu-upgrade`, estimated 8 cores, actual allocation 64 CPUs,
  6.951 seconds scientific runtime, 21-second job. No GPU.
- Local accepted checks: three 5-second one-process runs for baseline, Claim 1,
  and Claim 3.

The exact publication action, after all gates pass, is a text-only update of
the existing Space `DineshAI/TBSyYj4VV6`; no second Space will be created.
