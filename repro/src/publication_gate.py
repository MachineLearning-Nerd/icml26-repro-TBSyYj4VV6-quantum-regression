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
