# Evaluator-blind red-team record

## Pass 1

Starting only at the candidate `README.md` and `pages/index.md`, the reviewer
opened all six current claim pages, the release report, each linked source
file, raw JSON file, checker output, control output, runtime record, and the
historical-baseline wrapper.

Initial findings:

- Claim 3 lacked full run provenance and explicit source/code/raw links.
- Claims 2, 4, 5, and 6 were not present in current-first navigation.
- No evaluator-visible visibility matrix existed.

Those failures were treated as missing evidence and fixed.

## Pass 2 after fixes

Files opened:

- `README.md`, `pages/index.md`, `pages/release-report/page.md`
- `pages/current-claim-{1,2,3,4,5,6}/page.md`
- `code/{verify,publication_gate,claim1_runtime_audit,claim1_independent_checker,claim3_lasso_counterexample,claim3_independent_checker,remaining_claim_routes,remaining_claim_checker}.py`
- every `evidence/claim_{1,2,3,4,5,6}/*.json`
- `pages/historical-rejected-baseline/page.md`

Conclusions: the current verifier is first in navigation; every displayed
number is present in linked raw data; every claim exposes its exact statement,
assumptions, command, environment, code, checker, control, limitations, Git/run
provenance, seeds, and CPU/runtime record. Claims 2/4/5/6 are visibly BLOCKED,
not promoted from finite simulations. No conclusion required repository or
OpenResearch-only knowledge.

## Pass 3 after fixed-order and Claim 3 scope correction

The reviewer used only the clean staged artifact produced for the official
ICML validator. Files opened, in traversal order:

- `pages/index.md`
- `pages/executive-summary/page.md` and `poster_embed.html`
- `pages/claim-{1,2,3,4,5,6}/page.md`
- every code, raw JSON, checker, control, and CPU record linked from those six pages
- `pages/conclusion/page.md`

Conclusions:

- The sidebar order is exactly Executive summary, Claims 1–6, Conclusion.
- Claim 1 is the sole headline FALSIFIED result.
- Claim 3 is visibly BLOCKED; its lambda counterexample is labeled as a
  display-level subfinding and cannot be mistaken for full headline evidence.
- Claims 2–6 do not promote finite classical checks to quantum-runtime proof.
- The poster, fixed command, accepted HF Jobs, GitHub repository, raw data,
  controls, and `0–2/12` forecast are discoverable from the canonical pages.
- No missing cell remained in the conclusion’s evaluator-visible matrix.
