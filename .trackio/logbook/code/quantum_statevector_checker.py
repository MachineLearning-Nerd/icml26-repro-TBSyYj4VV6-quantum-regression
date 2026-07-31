#!/usr/bin/env python3
"""Independent fail-closed checks for the statevector evidence."""
from __future__ import annotations

import json
import math
from pathlib import Path


TARGET_SHA = "bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549"
FORMAL_RUN = "c827a21a-d44a-4616-ac18-85b7064c7290"
FORMAL_COMMIT = "862268e8b1a122f6044d7440cce19e37892c9b2a"


def check(root: Path) -> dict:
    raw = json.loads((root / "outputs" / "quantum_statevector_audit.json").read_text())
    formal = json.loads((root / "repro" / "formal_statevector_run.json").read_text())
    distribution = raw["multisample"]["distribution_checks"]
    witnesses = raw["multisample"]["domain_witnesses"]
    boundary = raw["multisample"]["negative_control_boundary"]
    lasso = raw["prior_quantum_lasso"]

    checks = {
        "target_source_hash_matches": raw["target_source_sha256"] == TARGET_SHA,
        "formal_run_matches": formal["run_id"] == FORMAL_RUN,
        "formal_commit_matches": formal["git_sha"] == FORMAL_COMMIT,
        "formal_run_succeeded": formal["status"] == "done",
        "no_gpu": formal["gpu_count"] == 0,
        "distribution_has_four_cells": len(distribution) == 4,
        "distribution_matches_target": max(
            row["coarse_total_variation"] for row in distribution
        ) < 0.12,
        "three_non_toy_domain_witnesses": len(witnesses) == 3
        and min(row["m"] for row in witnesses) >= 2048,
        "every_witness_has_M_gt_m": all(row["M"] > row["m"] for row in witnesses),
        "every_exact_call_rejected": all(
            row["exact_named_subroutine_rejected_call"] for row in witnesses
        ),
        "boundary_is_M_equal_m": boundary["M"] == boundary["m"],
        "boundary_constructs": boundary["circuit_constructed"],
        "regression_outputs_checked": all(
            raw["regression"][claim]["objective_ratio"] < 1.01
            for claim in (
                "C2_linear",
                "C4_ridge",
                "C5_huber",
                "C6_lp_p_3_over_2",
            )
        ),
        "lasso_has_40_seeded_cells": sum(
            row["seeds"] for row in lasso["cells"]
        ) == 40,
        "lasso_kkt_checks_pass": lasso["all_kkt_checks_passed"],
        "lasso_objective_checks_pass": lasso["all_objective_checks_passed"],
        "lasso_queries_measured": all(
            row["mean_quantum_oracle_queries"] > 0 for row in lasso["cells"]
        ),
        "oracle_removed_control_fails": lasso["negative_control_failed_as_intended"]
        and sum(
            row["oracle_removed_control_success_rate"] * row["seeds"]
            for row in lasso["cells"]
        )
        < 20,
        "query_slope_is_finite": math.isfinite(
            lasso["log_log_query_slope_vs_features"]
        ),
    }
    result = {
        "checker": "quantum_statevector_checker.py",
        "checks": checks,
        "passed": all(checks.values()),
    }
    assert result["passed"], result
    return result


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    result = check(root)
    output = root / "outputs" / "quantum_statevector_checker.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("QUANTUM_STATEVECTOR_CHECKER")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
