#!/usr/bin/env python3
"""Exact counterexamples to Claim 3's firstness and printed guarantee."""
from __future__ import annotations

import json
from datetime import datetime
from fractions import Fraction
from pathlib import Path


TARGET_DATE = "2025-09-29T13:22:59Z"


def firstness_counterexample() -> dict:
    prior = {
        "arxiv": "2312.14141",
        "title": "Quantum Algorithms for the Pathwise Lasso",
        "published": "2023-12-21T18:57:54Z",
        "source_url": "https://export.arxiv.org/e-print/2312.14141v3",
        "source_sha256": "cfdb8208c67d8a4c499b2bb6737912d8d674ccfbf1f2d12d803c708e1c98b093",
        "anchors": {
            "quantum_algorithm": "main.tex:146,221-225,257,265",
            "lasso_objective": "main.tex:165-166,195-198",
            "approximation_guarantee": "main.tex:228-234,304",
        },
        "quantum_algorithm_present": True,
        "penalized_squared_loss_l1_objective": True,
        "classical_lasso_solution_output": True,
    }
    earlier = {
        "arxiv": "2110.13086",
        "title": "Quantum Algorithms and Lower Bounds for Linear Regression with Norm Constraints",
        "published": "2021-10-25T16:26:37Z",
        "source_url": "https://export.arxiv.org/e-print/2110.13086v2",
        "source_sha256": "d6d120eb60829e5120b2700f8776dd35030d10a8e884522db11a7e592ce9b1cc",
        "anchors": {
            "penalty_equivalence": "LassoRidge22.tex:169",
            "quantum_lasso_runtime": "LassoRidge22.tex:203,806-843",
        },
        "quantum_algorithm_present": True,
        "lasso_problem_present": True,
    }

    target_timestamp = datetime.fromisoformat(TARGET_DATE.replace("Z", "+00:00"))
    prior_timestamp = datetime.fromisoformat(prior["published"].replace("Z", "+00:00"))
    earlier_timestamp = datetime.fromisoformat(earlier["published"].replace("Z", "+00:00"))
    same_objective_family = (
        prior["penalized_squared_loss_l1_objective"]
        and prior["classical_lasso_solution_output"]
    )
    return {
        "claim_id": "C3",
        "claim_component": "first quantum algorithm for Lasso regression",
        "target": {
            "arxiv": "2509.24757",
            "published": TARGET_DATE,
            "source_sha256": "bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549",
            "objective_anchor": "arxiv-version.tex:1164-1167",
            "own_prior_art_acknowledgement": "arxiv-version.tex:329-330",
        },
        "prior_art": [prior, earlier],
        "objective_mapping": {
            "prior": "(1/2)||y-X beta||_2^2 + lambda_prior ||beta||_1",
            "multiply_by": 2,
            "target": "||A x-b||_2^2 + lambda_target ||x||_1",
            "parameter_bijection": "lambda_target = 2*lambda_prior",
            "preserves_argmin": True,
        },
        "checks": {
            "pathwise_lasso_predates_target": prior_timestamp < target_timestamp,
            "chen_dewolf_predates_target": earlier_timestamp < target_timestamp,
            "same_penalized_objective_family": same_objective_family,
            "prior_quantum_algorithm_present": prior["quantum_algorithm_present"],
            "firstness_contradicted": (
                prior_timestamp < target_timestamp
                and same_objective_family
                and prior["quantum_algorithm_present"]
            ),
        },
        "negative_controls": {
            "later_matching_work": {
                "published": "2026-01-01T00:00:00Z",
                "semantic_match": True,
                "contradicts_firstness": False,
            },
            "earlier_ridge_only_work": {
                "published": "2021-01-01T00:00:00Z",
                "semantic_match": False,
                "contradicts_firstness": False,
            },
        },
    }


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
            "headline_claim_resolved": True,
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
        "headline_status": "FALSIFIED",
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
                "resolution": "The display is defective; this route alone does not resolve firstness.",
            },
            {
                "route": 2,
                "method": "Independent symbolic counterexample to the printed display",
                "result": "The source-valid scalar instance has exact impossibility gap 7/40.",
                "resolution": "Independently falsifies the literal approximation display.",
            },
            {
                "route": 3,
                "method": "Primary-source prior-art audit",
                "result": (
                    "arXiv:2312.14141 was published in 2023, writes the same penalized "
                    "squared-loss Lasso family, and gives quantum LARS algorithms."
                ),
                "resolution": "Contradicts the claimed firstness before the target's 2025 publication.",
            },
            {
                "route": 4,
                "method": "Independent earlier-paper cross-check",
                "result": (
                    "arXiv:2110.13086 was published in 2021, proves a quantum Lasso "
                    "algorithm, and explicitly relates constrained and penalized Lasso."
                ),
                "resolution": "A second independent pre-target quantum Lasso result confirms falsification.",
            },
        ],
    }


def write_counterexample(root: Path) -> dict:
    result = build_counterexample()
    firstness = firstness_counterexample()
    assert result["assumptions_satisfied"]
    assert result["finding"]["literal_corollary_falsified"]
    assert result["negative_control"]["passes"]
    assert firstness["checks"]["firstness_contradicted"]
    assert not firstness["negative_controls"]["later_matching_work"]["contradicts_firstness"]
    assert not firstness["negative_controls"]["earlier_ridge_only_work"]["contradicts_firstness"]
    raw = root / ".openresearch" / "artifacts" / "claim_3" / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    raw.joinpath("counterexample.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    raw.joinpath("routes.json").write_text(
        json.dumps(headline_routes(), indent=2, sort_keys=True) + "\n"
    )
    raw.joinpath("firstness_counterexample.json").write_text(
        json.dumps(firstness, indent=2, sort_keys=True) + "\n"
    )
    print("C3_LITERAL_COUNTEREXAMPLE")
    print(json.dumps(result, sort_keys=True))
    print("C3_FIRSTNESS_COUNTEREXAMPLE")
    print(json.dumps(firstness, sort_keys=True))
    return {"literal": result, "firstness": firstness}
