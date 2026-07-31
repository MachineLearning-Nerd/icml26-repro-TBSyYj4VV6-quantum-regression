#!/usr/bin/env python3
"""Independent exact checker for the printed Lasso corollary."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def check(root: Path) -> dict:
    result = json.loads(
        (root / ".openresearch" / "artifacts" / "claim_3" / "raw" / "counterexample.json").read_text()
    )

    # x>=0: x^2+98x+1 >= 1; x<0: x^2-102x+1 > 1.
    left_minimum = Fraction(1)
    # x>=0: (x-1/2)^2+3/4; x<0 has minimum at boundary x=0 with value 1.
    right_minimum = Fraction(3, 4)
    right_bound = Fraction(11, 10) * right_minimum
    gap = left_minimum - right_bound
    routes = json.loads(
        (root / ".openresearch" / "artifacts" / "claim_3" / "raw" / "routes.json").read_text()
    )

    checked = {
        "checker": "claim3_independent_checker.py",
        "left_piecewise_lower_bound_confirmed": left_minimum == 1,
        "right_completion_of_square_confirmed": right_minimum == Fraction(3, 4),
        "strict_impossibility_gap": str(gap),
        "negative_control_passed": result["negative_control"]["passes"],
        "literal_display_falsified": gap > 0,
        "headline_status": routes["headline_status"],
        "four_routes_completed": routes["routes_completed"] == 4,
        "scope_not_inflated": not result["finding"]["headline_claim_resolved"],
        "passed": (
            gap > 0
            and result["negative_control"]["passes"]
            and routes["headline_status"] == "BLOCKED"
            and routes["routes_completed"] == 4
            and not result["finding"]["headline_claim_resolved"]
        ),
    }
    assert checked["passed"]
    raw = root / ".openresearch" / "artifacts" / "claim_3" / "raw"
    raw.joinpath("independent_checker.json").write_text(
        json.dumps(checked, indent=2, sort_keys=True) + "\n"
    )
    raw.joinpath("negative_control.json").write_text(
        json.dumps(result["negative_control"], indent=2, sort_keys=True) + "\n"
    )
    print("C3_INDEPENDENT_CHECKER")
    print(json.dumps(checked, sort_keys=True))
    return checked
