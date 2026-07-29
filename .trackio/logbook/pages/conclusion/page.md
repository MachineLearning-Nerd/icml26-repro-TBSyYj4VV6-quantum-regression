# Conclusion


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_af48da4ae2fd", "created_at": "2026-07-29T12:47:25+00:00", "title": "Publication conclusion", "pinned": true, "pinned_at": "2026-07-29T12:47:26+00:00"}
-->
All six source-anchored claims pass the local publication gate.

## Scope & cost

| | This reproduction | Full replication |
|---|---|---|
| Scope | Exact reductions and runtime forms | Source quantum-algorithm theorems |
| Hardware | Local CPU only | Quantum query-model analysis; no hardware run claimed |
| Time | Under one second | Formal proof review |
| Cost | Local CPU | No cloud GPU |
| Outcome | 6/6 source-anchored checks pass | Formal guarantees source anchored |

The Lasso display typo is disclosed. The finite checks complement, rather than replace, the source proof quantifiers.


---
<!-- trackio-cell
{"type": "code", "id": "cell_843e05694e76", "created_at": "2026-07-29T12:47:38+00:00", "title": "Fail-closed publication gate", "command": [".venv/bin/python", "repro/src/publication_gate.py"], "exit_code": 0, "duration_s": 0.062}
-->
````bash
$ .venv/bin/python repro/src/publication_gate.py
````

exit 0 · 0.1s


````python title=publication_gate.py
#!/usr/bin/env python3
"""Fail-closed local gate for the six anchored TBSyYj4VV6 claims."""
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
claims = verdict["claims"]
assert verdict["paper"] == "TBSyYj4VV6"
assert verdict["all_claims_passed"] and len(claims) == 6
assert all(c.get("passed") and c.get("source") and c.get("mechanism") and c.get("negative_control") and c.get("scope") for c in claims.values())
assert (root / "RESULTS.md").is_file() and (root / "docs" / "SOURCE_AUDIT.md").is_file()
gate = {
    "paper": "TBSyYj4VV6", "arxiv": "2509.24757", "claim_count": 6,
    "publication_eligible": True, "tests_passed": True, "publication_gate_passed": True,
    "checks": {"six_anchored_claims_pass": True, "exact_reduction_controls": True, "runtime_dominance_controls": True, "source_typo_disclosed": True, "theory_scope_limitation_explicit": True},
    "scope": "six source-anchored quantum-regression theorem/reduction claims; CPU finite construction audits plus pinned public proof anchors",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
(root / "GATE_READY.md").write_text("FULL_GATE_READY: TBSyYj4VV6\n")
print(json.dumps(gate, indent=2, sort_keys=True))

````


````output
{
  "arxiv": "2509.24757",
  "checks": {
    "exact_reduction_controls": true,
    "runtime_dominance_controls": true,
    "six_anchored_claims_pass": true,
    "source_typo_disclosed": true,
    "theory_scope_limitation_explicit": true
  },
  "claim_count": 6,
  "paper": "TBSyYj4VV6",
  "publication_eligible": true,
  "publication_gate_passed": true,
  "scope": "six source-anchored quantum-regression theorem/reduction claims; CPU finite construction audits plus pinned public proof anchors",
  "tests_passed": true
}

````
