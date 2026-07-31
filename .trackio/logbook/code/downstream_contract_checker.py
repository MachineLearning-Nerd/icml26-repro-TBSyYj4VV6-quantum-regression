#!/usr/bin/env python3
"""Independent fail-closed checker for Claims 2, 4, 5, and 6."""
from __future__ import annotations

import json
from pathlib import Path


def check(root: Path) -> dict:
    checks = {}
    for claim_id in ("C2", "C4", "C5", "C6"):
        path = (
            root
            / ".openresearch"
            / "artifacts"
            / f"claim_{claim_id[1]}"
            / "raw"
            / "downstream_contract_audit.json"
        )
        audit = json.loads(path.read_text())
        cells = audit["normalized_witness_cells"]
        domain_violations = sum(not cell["M_le_m"] for cell in cells)
        control = audit["negative_control"]
        runtime_expected = claim_id in ("C2", "C4")
        runtime_check = (
            audit["asymptotic_certificate"]["runtime_power_contradiction"]
            == runtime_expected
        )
        controls_reject = (
            control["M_le_m"]
            and control["M_le_advertised_terms"]
            and not control["counterexample_triggered"]
        )
        checks[claim_id] = {
            "assumptions_satisfied": audit["assumption_satisfying_family"][
                "assumptions_satisfied"
            ],
            "universal_epsilon_quantifier_present": (
                audit["assumption_satisfying_family"]["epsilon_domain_in_corollary"]
                == "epsilon > 0"
            ),
            "eventual_domain_violation_certified": (
                audit["asymptotic_certificate"]["eventual_M_gt_m"]
                and domain_violations > 0
            ),
            "claim_specific_dependency_chain_present": bool(
                audit["exact_proposed_algorithm_chain"]
            ),
            "runtime_basis_scoped_correctly": runtime_check,
            "negative_control_rejects_false_positive": controls_reject,
            "status": audit["status"],
        }
    passed = all(
        row["status"] == "FALSIFIED"
        and all(value for key, value in row.items() if key != "status")
        for row in checks.values()
    )
    result = {
        "checker": "downstream_contract_checker.py",
        "checks": checks,
        "passed": passed,
    }
    assert passed
    for claim_id in checks:
        raw = (
            root
            / ".openresearch"
            / "artifacts"
            / f"claim_{claim_id[1]}"
            / "raw"
        )
        raw.joinpath("independent_checker.json").write_text(
            json.dumps(
                {"claim_id": claim_id, **checks[claim_id], "passed": True},
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
    output = root / "outputs" / "downstream_contract_checker.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("DOWNSTREAM_CONTRACT_CHECKER")
    print(json.dumps(result, sort_keys=True))
    return result
