#!/usr/bin/env python3
"""Independent fail-closed checker for the four-route remaining-claim audit."""
from __future__ import annotations

import json
from pathlib import Path


def check(root: Path) -> dict:
    data = json.loads((root / "outputs" / "remaining_claim_routes.json").read_text())
    checks = {}
    for claim in ("C2", "C4", "C5", "C6"):
        record = data["claims"][claim]
        checks[claim] = {
            "exactly_four_routes": record["routes_completed"] == 4,
            "honest_blocked_status": record["status"] == "BLOCKED",
            "proof_certificate_absent": record["route_1_proof_chain"]["certificate_found"] is False,
            "finite_route_scoped": "no quantum subroutine" in record["route_2_finite_simulation"]["scope"],
            "negative_control_failed_as_intended": record["route_3_calibrated_first_hit"]["negative_control_failed_as_intended"],
            "no_counterexample_mislabeled": record["route_4_falsification"]["valid_counterexample_found"] is False,
            "blocker_recorded": bool(record["blocker"]),
        }
    passed = all(all(row.values()) for row in checks.values())
    result = {"passed": passed, "checks": checks}
    output = root / "outputs" / "remaining_claim_checker.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("REMAINING_CLAIMS_CHECKER=" + json.dumps(result, separators=(",", ":"), sort_keys=True))
    if not passed:
        raise SystemExit(1)
    return result


if __name__ == "__main__":
    check(Path(__file__).resolve().parents[2])
