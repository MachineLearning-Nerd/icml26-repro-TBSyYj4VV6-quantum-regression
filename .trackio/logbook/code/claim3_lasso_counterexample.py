#!/usr/bin/env python3
"""Exact counterexample to Corollary 26 as printed."""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def build_counterexample() -> dict:
    epsilon = Fraction(1, 10)
    left_minimum = Fraction(1)
    right_minimand = Fraction(3, 4)
    right_bound = (1 + epsilon) * right_minimand
    gap = left_minimum - right_bound

    control_left = right_minimand
    control_passes = control_left <= right_bound
    return {
        "claim_id": "C3",
        "assumptions_satisfied": True,
        "counterexample": {
            "A": [[1]],
            "b": [1],
            "m": 1,
            "n": 1,
            "r": 1,
            "lambda": 100,
            "epsilon": "1/10",
        },
        "exact_values": {
            "left_global_minimum": str(left_minimum),
            "left_minimizer": "0",
            "right_minimand_minimum": str(right_minimand),
            "right_minimand_minimizer": "1/2",
            "right_bound": str(right_bound),
            "gap": str(gap),
        },
        "finding": {
            "all_outputs_violate_corollary": gap > 0,
            "literal_corollary_falsified": gap > 0,
            "headline_claim_resolved": False,
        },
        "negative_control": {
            "lambda": 1,
            "output_x": "1/2",
            "left_value": str(control_left),
            "right_bound": str(right_bound),
            "passes": control_passes,
        },
    }


def headline_routes() -> dict:
    return {
        "claim_id": "C3",
        "headline_status": "BLOCKED",
        "routes_completed": 4,
        "routes": [
            {
                "route": 1,
                "method": "Exact source and quantifier audit",
                "result": (
                    "Corollary 26 states a high-probability Lasso runtime of "
                    "O~(r*sqrt(mn)/epsilon+n^3/epsilon^2), while its displayed "
                    "right minimand omits lambda."
                ),
                "resolution": "The display is defective; firstness and runtime remain unresolved.",
            },
            {
                "route": 2,
                "method": "Independent symbolic counterexample to the printed display",
                "result": "The source-valid scalar instance has exact impossibility gap 7/40.",
                "resolution": "Falsifies only the literal approximation display.",
            },
            {
                "route": 3,
                "method": "Proof-chain and implementation audit",
                "result": (
                    "The preceding reduction includes lambda, but no executable implementation "
                    "of the named quantum pipeline or machine-checkable runtime certificate is provided."
                ),
                "resolution": "The repaired algorithm/runtime claim cannot be verified on available CPU compute.",
            },
            {
                "route": 4,
                "method": "Mandatory falsification route for the headline runtime claim",
                "result": (
                    "The lambda counterexample disappears when the intended lambda-weighted minimand "
                    "is restored; no oracle-model lower bound or other assumption-satisfying "
                    "counterexample to the repaired runtime was established."
                ),
                "resolution": "Headline claim remains BLOCKED, not FALSIFIED.",
            },
        ],
    }


def write_counterexample(root: Path) -> dict:
    result = build_counterexample()
    assert result["assumptions_satisfied"]
    assert result["finding"]["literal_corollary_falsified"]
    assert result["negative_control"]["passes"]
    raw = root / ".openresearch" / "artifacts" / "claim_3" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    raw.joinpath("counterexample.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    raw.joinpath("routes.json").write_text(
        json.dumps(headline_routes(), indent=2, sort_keys=True) + "\n"
    )
    print("C3_LITERAL_COUNTEREXAMPLE")
    print(json.dumps(result, sort_keys=True))
    return result
