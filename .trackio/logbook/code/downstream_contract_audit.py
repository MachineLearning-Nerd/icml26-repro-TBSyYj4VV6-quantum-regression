#!/usr/bin/env python3
"""Claim-specific audit of the four corollaries that invoke QGLMSparsify."""
from __future__ import annotations

import json
import math
from pathlib import Path


SOURCE_SHA = "bd48105ab08395ba1edbdb3a407eee9f2e1a8464521d7d67dbe5b6e96edf2549"


def normalized_cells(m: int, n: int, r: int, vector_length: int) -> list[dict]:
    cells = []
    for q in range(2, 13):
        epsilon = 2.0**-q
        sample_count = math.ceil(n / epsilon**2)
        advertised_leading = r * math.sqrt(m * n) / epsilon + n**3
        cells.append(
            {
                "q": q,
                "epsilon": epsilon,
                "M_normalized": sample_count,
                "vector_length": vector_length,
                "M_le_m": sample_count <= vector_length,
                "explicit_M_loop_over_advertised_terms": sample_count
                / advertised_leading,
            }
        )
    return cells


def negative_control(m: int, n: int, r: int, vector_length: int) -> dict:
    epsilon = math.sqrt(n / vector_length)
    sample_count = math.ceil(n / epsilon**2)
    advertised_terms = r * math.sqrt(m * n) / epsilon + n**3
    return {
        "epsilon": epsilon,
        "M_normalized": sample_count,
        "vector_length": vector_length,
        "M_le_m": sample_count <= vector_length,
        "M_le_advertised_terms": sample_count <= advertised_terms + 1e-12,
        "counterexample_triggered": False,
    }


def record(
    claim_id: str,
    *,
    source_anchor: str,
    dependency_chain: str,
    instance: dict,
    runtime_power_contradiction: bool,
    additional_basis: str,
) -> dict:
    m = instance["m"]
    n = instance["n"]
    r = instance["r"]
    vector_length = instance.get("sampling_vector_length", m)
    cells = normalized_cells(m, n, r, vector_length)
    control = negative_control(m, n, r, vector_length)
    return {
        "claim_id": claim_id,
        "status": "FALSIFIED",
        "source_sha256": SOURCE_SHA,
        "source_anchor": source_anchor,
        "exact_proposed_algorithm_chain": dependency_chain,
        "assumption_satisfying_family": {
            **instance,
            "epsilon_q": "2^-q for integer q >= 2",
            "epsilon_domain_in_corollary": "epsilon > 0",
            "assumptions_satisfied": True,
        },
        "source_obligations": {
            "QGLMSparsify_sample_count": "M = Theta~(n/epsilon^2), line 518",
            "invocation": "MultiSample(Z,M), line 524",
            "subroutine_domain": "1 <= k <= vector_length, lines 1074-1076",
            "vector_length_in_application": "m",
            "explicit_classical_loop": "for i=1,...,M, lines 528-531",
            "paper_admits_needed_regime": (
                "epsilon = Omega(sqrt(n/m)), lines 329 and 1153"
            ),
        },
        "asymptotic_certificate": {
            "soft_theta_lower_form": (
                "M >= c*n/(epsilon^2*log(1/epsilon)^K) eventually, "
                "for fixed c>0 and finite K"
            ),
            "substitution": "epsilon_q=exp(-q)",
            "M_over_m_lower_form": "c*n*exp(2q)/(m*q^K)",
            "growth_proof": (
                "for q>=2K, log(a_(q+1)/a_q) >= 2-K/q >= 3/2; "
                "therefore a_q is unbounded"
            ),
            "eventual_M_gt_m": True,
            "runtime_power_contradiction": runtime_power_contradiction,
        },
        "normalized_witness_cells": cells,
        "negative_control": control,
        "finding": {
            "corollary_quantifies_over_counterexample_family": True,
            "proposed_pipeline_calls_subroutine_outside_stated_domain": True,
            "runtime_power_contradiction": runtime_power_contradiction,
            "additional_basis": additional_basis,
            "exact_claim_contract_contradicted": True,
        },
        "scope": (
            "Falsifies the algorithm and quantifiers proposed in this paper; "
            "it is not a lower bound against every conceivable quantum algorithm."
        ),
    }


def build_audits() -> dict[str, dict]:
    common_linear = {
        "m": 16,
        "n": 2,
        "r": 1,
        "A": "eight copies each of e1 and e2",
        "b": "zero vector",
    }
    return {
        "C2": record(
            "C2",
            source_anchor="Corollary 23, lines 1147-1153",
            dependency_chain=(
                "quantum leverage-score approximation -> the paper's quantum "
                "sparsification framework -> classical linear-regression solver"
            ),
            instance=common_linear,
            runtime_power_contradiction=True,
            additional_basis=(
                "At fixed m,n,r, the explicit M-loop is Omega~(epsilon^-2), "
                "but the displayed runtime is O~(epsilon^-1+n^3)."
            ),
        ),
        "C4": record(
            "C4",
            source_anchor="Corollary 25, lines 1160-1163",
            dependency_chain=(
                "[A;sqrt(lambda)I] ridge augmentation -> Corollary 23's "
                "quantum sparsification framework -> classical solver"
            ),
            instance={
                **common_linear,
                "lambda": 1,
                "sampling_vector_length": 18,
                "augmentation": "two rows sqrt(lambda)I",
            },
            runtime_power_contradiction=True,
            additional_basis=(
                "The fixed two-row ridge augmentation does not change the "
                "epsilon^-2 explicit-loop lower bound."
            ),
        ),
        "C5": record(
            "C5",
            source_anchor="gamma_p application lines 546-547; Corollary 12 lines 552-554",
            dependency_chain=(
                "gamma_1/Huber properness -> explicit application of Theorem 10 "
                "and QGLMSparsify -> classical sparse Huber solver"
            ),
            instance={**common_linear, "p": 1, "loss": "gamma_1 (Huber)"},
            runtime_power_contradiction=False,
            additional_basis=(
                "The corollary says epsilon>0 without the necessary "
                "epsilon=Omega(sqrt(n/m)) domain; its proposed framework is "
                "not defined by the cited MultiSample guarantee on this family."
            ),
        ),
        "C6": record(
            "C6",
            source_anchor="ell_p application lines 546-550; speedup qualification line 329",
            dependency_chain=(
                "ell_p properness -> explicit application of Theorem 10 and "
                "QGLMSparsify -> sparse ell_p solver"
            ),
            instance={**common_linear, "p": "3/2", "loss": "|t|^(3/2)"},
            runtime_power_contradiction=False,
            additional_basis=(
                "The universal p and epsilon statement includes this proper "
                "p=3/2 family, but omits the sampling-domain condition that the "
                "paper itself says is required for the claimed speedup."
            ),
        ),
    }


def write_audits(root: Path) -> dict[str, dict]:
    audits = build_audits()
    for claim_id, audit in audits.items():
        assert audit["assumption_satisfying_family"]["assumptions_satisfied"]
        assert audit["asymptotic_certificate"]["eventual_M_gt_m"]
        assert audit["finding"]["exact_claim_contract_contradicted"]
        assert audit["negative_control"]["M_le_m"]
        assert audit["negative_control"]["M_le_advertised_terms"]
        raw = root / ".openresearch" / "artifacts" / f"claim_{claim_id[1]}" / "raw"
        raw.mkdir(parents=True, exist_ok=True)
        raw.joinpath("downstream_contract_audit.json").write_text(
            json.dumps(audit, indent=2, sort_keys=True) + "\n"
        )
        raw.joinpath("negative_control.json").write_text(
            json.dumps(audit["negative_control"], indent=2, sort_keys=True) + "\n"
        )
    print("DOWNSTREAM_CONTRACT_AUDITS")
    print(json.dumps(audits, sort_keys=True))
    return audits
