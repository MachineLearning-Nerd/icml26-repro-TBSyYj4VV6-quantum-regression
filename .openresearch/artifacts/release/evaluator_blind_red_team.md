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

## Pass 4 after exact six-claim adjudication

The reviewer started from a fresh allowlisted candidate and used only
`pages/index.md`. Files opened, in traversal order:

- `pages/executive-summary/page.md` and `poster_embed.html`
- `pages/claim-{1,2,3,4,5,6}/page.md`
- each linked claim contract, source audit, verifier, independent checker,
  negative control, raw JSON result, and runtime record
- `pages/conclusion/page.md`
- the linked illustrated report and self-contained notebook

Conclusions:

- All six exact claim statements, assumptions, quantifiers, and current
  FALSIFIED verdicts are directly discoverable.
- Claims 1–4 expose HIGH-confidence independent contradictions.
- Claims 5–6 explicitly expose their MEDIUM-confidence scope: the paper's
  all-epsilon algorithm leaves the cited sampler domain; no universal lower
  bound against repaired algorithms is claimed.
- The fixed command, locked environment, Git SHA, seeds, nominal 8-vCPU HF
  Job (64 container-visible logical CPUs), raw results, checker outputs,
  failing controls, and limitations are linked.
- Historical rejected pages remain reachable but cannot be mistaken for the
  current verifier.
- No conclusion required hidden repository knowledge or an inaccessible file.

## Pass 5 after statevector evidence

Starting only from `logbook.json` and `pages/index.md`, the reviewer followed
the eight fixed-order canonical routes and every relative link. The traversal
opened 67 evaluator-visible text files with zero missing links, including:

- all six canonical claim pages;
- six directly linked statevector raw files;
- six independently generated statevector checker outputs;
- six formal HF run records;
- both new executable source files; and
- the current release forecast/risk report.

The reviewer located the non-toy `M=4m` witnesses, valid `M=m` control,
quantum-sampled regression objectives, 40-cell quantum LARS/KKT result,
oracle-disabled control, exact fixed command, source hashes, simulator
limitations, CPU allocation, job link, current `4/12` live score, and forecast
without repository-only knowledge. `marimo check` passed. No missing
visibility-matrix cell or stale current verdict was found.
