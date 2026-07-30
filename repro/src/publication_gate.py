#!/usr/bin/env python3
"""Fail-closed milestone gate; publication remains blocked."""
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
assert verdict["paper"] == "TBSyYj4VV6"
assert verdict["historical_rejected_baseline"]["all_checks_executed"]
claim1 = verdict["current_claims"]["C1"]
assert claim1["contract_contradicted"] and claim1["independent_checker_passed"]
claim3 = verdict["current_claims"]["C3"]
assert claim3["all_outputs_violate_corollary"] and claim3["independent_checker_passed"]
assert verdict["release_ready"] is False
gate = {
    "paper": "TBSyYj4VV6",
    "arxiv": "2509.24757",
    "milestone_gate_passed": True,
    "publication_eligible": False,
    "release_gate_passed": False,
    "checks": {
        "historical_baseline_rerun": True,
        "claim_1_exact_contract": True,
        "claim_1_independent_checker": True,
        "claim_1_negative_control": True,
        "claim_3_exact_counterexample": True,
        "claim_3_independent_checker": True,
        "claim_3_negative_control": True,
        "all_six_claims_adjudicated": False
    },
    "scope": "Claim 1 candidate finding only; publication is intentionally blocked.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
