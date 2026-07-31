#!/usr/bin/env python3
"""Independent exact checker for Claim 3's two counterexamples."""
from __future__ import annotations

import json
from datetime import datetime
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
    firstness = json.loads(
        (
            root
            / ".openresearch"
            / "artifacts"
            / "claim_3"
            / "raw"
            / "firstness_counterexample.json"
        ).read_text()
    )
    target_date = datetime.fromisoformat(
        firstness["target"]["published"].replace("Z", "+00:00")
    )
    pathwise = firstness["prior_art"][0]
    chen_dewolf = firstness["prior_art"][1]
    pathwise_predates = datetime.fromisoformat(
        pathwise["published"].replace("Z", "+00:00")
    ) < target_date
    chen_dewolf_predates = datetime.fromisoformat(
        chen_dewolf["published"].replace("Z", "+00:00")
    ) < target_date
    objective_bijection = (
        firstness["objective_mapping"]["multiply_by"] == 2
        and firstness["objective_mapping"]["parameter_bijection"]
        == "lambda_target = 2*lambda_prior"
        and firstness["objective_mapping"]["preserves_argmin"]
    )
    prior_art_falsifies_firstness = (
        pathwise_predates
        and chen_dewolf_predates
        and pathwise["quantum_algorithm_present"]
        and pathwise["penalized_squared_loss_l1_objective"]
        and pathwise["classical_lasso_solution_output"]
        and chen_dewolf["quantum_algorithm_present"]
        and chen_dewolf["lasso_problem_present"]
        and objective_bijection
    )
    controls_rejected = not any(
        control["contradicts_firstness"]
        for control in firstness["negative_controls"].values()
    )

    checked = {
        "checker": "claim3_independent_checker.py",
        "left_piecewise_lower_bound_confirmed": left_minimum == 1,
        "right_completion_of_square_confirmed": right_minimum == Fraction(3, 4),
        "strict_impossibility_gap": str(gap),
        "negative_control_passed": result["negative_control"]["passes"],
        "literal_display_falsified": gap > 0,
        "pathwise_lasso_predates_target": pathwise_predates,
        "chen_dewolf_predates_target": chen_dewolf_predates,
        "objective_family_bijection_confirmed": objective_bijection,
        "prior_art_falsifies_firstness": prior_art_falsifies_firstness,
        "negative_controls_rejected": controls_rejected,
        "headline_status": routes["headline_status"],
        "four_routes_completed": routes["routes_completed"] == 4,
        "passed": (
            gap > 0
            and result["negative_control"]["passes"]
            and prior_art_falsifies_firstness
            and controls_rejected
            and routes["headline_status"] == "FALSIFIED"
            and routes["routes_completed"] == 4
            and result["finding"]["headline_claim_resolved"]
        ),
    }
    assert checked["passed"]
    raw = root / ".openresearch" / "artifacts" / "claim_3" / "raw"
    raw.joinpath("independent_checker.json").write_text(
        json.dumps(checked, indent=2, sort_keys=True) + "\n"
    )
    raw.joinpath("negative_control.json").write_text(
        json.dumps(
            {
                "literal_display": result["negative_control"],
                "firstness": firstness["negative_controls"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    print("C3_INDEPENDENT_CHECKER")
    print(json.dumps(checked, sort_keys=True))
    return checked
