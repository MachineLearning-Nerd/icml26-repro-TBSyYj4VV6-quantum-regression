#!/usr/bin/env python3
"""Independent fail-closed checker for Claim 1 evidence."""
from __future__ import annotations

import json
from pathlib import Path


def check(root: Path) -> dict:
    raw = root / ".openresearch" / "artifacts" / "claim_1" / "raw" / "runtime_audit.json"
    audit = json.loads(raw.read_text())

    obligations = audit["source_obligations"]
    power_gap = (
        obligations["explicit_loop_epsilon_power"]
        > obligations["claimed_epsilon_power"]
    )
    domain_violations = [
        cell for cell in audit["cells"]
        if not cell["multisample_precondition_M_le_m"]
    ]
    control = audit["negative_control"]
    control_rejects_false_positive = (
        control["multisample_precondition_M_le_m"]
        and control["M_le_r_sqrt_mn_over_epsilon"]
        and not control["contradiction_detected"]
    )

    result = {
        "claim_id": "C1",
        "independent_checker": "claim1_independent_checker.py",
        "power_gap_confirmed": power_gap,
        "domain_violation_count": len(domain_violations),
        "negative_control_rejects_false_positive": control_rejects_false_positive,
        "passed": power_gap and bool(domain_violations) and control_rejects_false_positive,
    }
    assert result["passed"]
    raw.parent.joinpath("independent_checker.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    raw.parent.joinpath("negative_control.json").write_text(
        json.dumps(control, indent=2, sort_keys=True) + "\n"
    )
    print("C1_INDEPENDENT_CHECKER")
    print(json.dumps(result, sort_keys=True))
    return result
