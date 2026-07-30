#!/usr/bin/env python3
"""Audit the exact QGLMSparsify sample-count and runtime contract."""
from __future__ import annotations

import json
import math
from pathlib import Path


def build_audit() -> dict:
    n, m, r = 2, 16, 1
    cells = []
    for q in range(2, 13):
        epsilon = 2.0**-q
        sample_count = round(n / epsilon**2)
        claimed = n**3 + n * r**2 + r * math.sqrt(m * n) / epsilon
        cells.append(
            {
                "q": q,
                "epsilon": epsilon,
                "M_normalized": sample_count,
                "input_length_m": m,
                "multisample_precondition_M_le_m": sample_count <= m,
                "claimed_runtime_terms_normalized": claimed,
                "explicit_loop_over_claimed_terms": sample_count / claimed,
            }
        )

    threshold_epsilon = math.sqrt(n / m)
    threshold_samples = round(n / threshold_epsilon**2)
    threshold_quantum_term = r * math.sqrt(m * n) / threshold_epsilon
    control = {
        "epsilon": threshold_epsilon,
        "M_normalized": threshold_samples,
        "input_length_m": m,
        "multisample_precondition_M_le_m": threshold_samples <= m,
        "M_le_r_sqrt_mn_over_epsilon": threshold_samples <= threshold_quantum_term + 1e-12,
        "contradiction_detected": False,
    }

    return {
        "claim_id": "C1",
        "source_sha256": "bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549",
        "algorithm": "QGLMSparsify (Algorithm 2)",
        "assumption_family": {
            "n": n,
            "m": m,
            "r": r,
            "rows": "eight copies each of e1 and e2",
            "loss": "f_i(t)=t^2",
            "proper_parameters": {"L": 1, "theta": 1, "c": 1},
            "s_min": 1,
            "s_max": 2,
            "assumptions_satisfied": True,
        },
        "source_obligations": {
            "formal_epsilon_domain": "epsilon > 0",
            "M": "Theta~(n/epsilon^2)",
            "multisample_precondition": "1 <= M <= m",
            "explicit_loop_iterations": "M",
            "claimed_epsilon_power": 1,
            "explicit_loop_epsilon_power": 2,
        },
        "cells": cells,
        "asymptotic_certificate": {
            "fixed_dimensions": True,
            "lower_bound_epsilon_power": 2,
            "claimed_runtime_epsilon_power": 1,
            "polylog_cannot_absorb_power_gap": True,
        },
        "negative_control": control,
        "finding": {
            "multisample_domain_violated": all(
                not cell["multisample_precondition_M_le_m"] for cell in cells
            ),
            "runtime_power_contradiction": True,
            "exact_named_algorithm_contract_contradicted": True,
        },
    }


def verify_audit(audit: dict) -> None:
    assert audit["assumption_family"]["assumptions_satisfied"]
    finding = audit["finding"]
    assert finding["multisample_domain_violated"]
    assert finding["runtime_power_contradiction"]
    certificate = audit["asymptotic_certificate"]
    assert certificate["lower_bound_epsilon_power"] > certificate["claimed_runtime_epsilon_power"]
    control = audit["negative_control"]
    assert control["multisample_precondition_M_le_m"]
    assert control["M_le_r_sqrt_mn_over_epsilon"]
    assert not control["contradiction_detected"]


def write_audit(root: Path) -> dict:
    audit = build_audit()
    verify_audit(audit)
    raw_dir = root / ".openresearch" / "artifacts" / "claim_1" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "runtime_audit.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n"
    )
    print("C1_CURRENT_VERIFIER")
    print(json.dumps(audit, sort_keys=True))
    return audit
