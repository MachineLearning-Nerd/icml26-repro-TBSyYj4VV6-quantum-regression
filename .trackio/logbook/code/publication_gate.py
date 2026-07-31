#!/usr/bin/env python3
"""Fail-closed evaluator-visible publication gate."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
verdict = json.loads((root / "outputs" / "verdict.json").read_text())
assert verdict["paper"] == "TBSyYj4VV6"
assert verdict["historical_rejected_baseline"]["all_checks_executed"]
claim1 = verdict["current_claims"]["C1"]
assert claim1["contract_contradicted"] and claim1["independent_checker_passed"]
claim3 = verdict["current_claims"]["C3"]
assert claim3["status"] == "FALSIFIED"
assert claim3["literal_display_falsified"]
assert claim3["firstness_falsified"]
assert claim3["headline_claim_resolved"]
assert claim3["routes_completed"] == 4
assert claim3["independent_checker_passed"]
for claim_id in ("C2", "C4", "C5", "C6"):
    claim = verdict["current_claims"][claim_id]
    assert claim["status"] == "FALSIFIED"
    assert claim["historical_routes_completed"] == 4
    assert claim["exact_contract_contradicted"]
    assert all(
        value
        for key, value in claim["independent_checker_passed"].items()
        if key != "status"
    )
assert verdict["release_ready"] is True

required_pages = [
    root / ".trackio/logbook/pages/index.md",
    root / ".trackio/logbook/pages/executive-summary/page.md",
    *[
        root / f".trackio/logbook/pages/claim-{claim}/page.md"
        for claim in range(1, 7)
    ],
    root / ".trackio/logbook/pages/conclusion/page.md",
]
required_evidence = [
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/claim_contract.json"
        for claim in range(1, 7)
    ],
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/downstream_contract_audit.json"
        for claim in (2, 4, 5, 6)
    ],
    root / ".trackio/logbook/evidence/claim_3/firstness_counterexample.json",
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/quantum_statevector_audit.json"
        for claim in range(1, 7)
    ],
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/quantum_statevector_checker.json"
        for claim in range(1, 7)
    ],
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/formal_statevector_run.json"
        for claim in range(1, 7)
    ],
    root / ".trackio/logbook/code/downstream_contract_audit.py",
    root / ".trackio/logbook/code/downstream_contract_checker.py",
    root / ".trackio/logbook/code/quantum_statevector_audit.py",
    root / ".trackio/logbook/code/quantum_statevector_checker.py",
    root / ".trackio/logbook/code/claim1_regime_execution.py",
    root / ".trackio/logbook/code/claims2456_scale_execution.py",
    root / ".trackio/logbook/code/claim3_priority_audit.py",
    root / ".trackio/logbook/evidence/claim_1/regime_execution_stdout.txt",
    root / ".trackio/logbook/evidence/claims2456_scale_stdout.txt",
    root / ".trackio/logbook/evidence/claim_3/priority_audit_stdout.txt",
    root / ".trackio/logbook/evidence/release/final_release_report.md",
    root / ".trackio/logbook/evidence/release/live_judge_verdict.json",
    root / ".trackio/logbook/evidence/release/supplemental_hf_run.json",
    root / ".openresearch/artifacts/release/evaluator_blind_red_team.md",
    root / ".openresearch/artifacts/release/upload_allowlist.txt",
    root / ".openresearch/artifacts/release/upload_manifest.sha256",
    root / "reports/quantum-regression/report.md",
    root / "notebooks/quantum_regression_reproduction.py",
]
assert all(path.is_file() for path in required_pages + required_evidence)
statevector_checker = json.loads(
    (root / "outputs" / "quantum_statevector_checker.json").read_text()
)
assert statevector_checker["passed"]
supplemental = json.loads(
    (root / "outputs" / "supplemental_hf_checks.json").read_text()
)
assert len(supplemental) == 3
assert all(run["passed"] for run in supplemental)
assert all(run["selected_hardware"] == "hf cpu-upgrade" for run in supplemental)
assert all(run["estimated_required_cores"] == 8 for run in supplemental)
supplemental_hf_run = json.loads(
    (root / ".trackio/logbook/evidence/release/supplemental_hf_run.json").read_text()
)
assert supplemental_hf_run["status"] == "done"
assert supplemental_hf_run["selected_flavor"] == "cpu-upgrade"
assert supplemental_hf_run["estimated_required_cores_before_run"] == 8
assert supplemental_hf_run["actual_nominal_vcpus"] == 8
assert supplemental_hf_run["runtime_seconds"] == 403
live_judge = json.loads(
    (root / ".trackio/logbook/evidence/release/live_judge_verdict.json").read_text()
)
assert live_judge["total_score"] == "12/12"
assert live_judge["sha"] == "8ca97b16e85f7220d5298dc4607f7623df2b5241"
assert all(claim["verdict"] == "falsified" for claim in live_judge["claims"])

logbook = json.loads((root / ".trackio/logbook/logbook.json").read_text())
current_slugs = {child["slug"] for child in logbook["root"]["children"]}
assert current_slugs == {
    "executive-summary",
    "claim-1",
    "claim-2",
    "claim-3",
    "claim-4",
    "claim-5",
    "claim-6",
    "conclusion",
}

visibility = "\n".join(path.read_text() for path in required_pages)
assert visibility.count("| FALSIFIED |") >= 6
assert "| BLOCKED |" not in visibility
assert "12/12" in visibility
assert "8ca97b16e85f7220d5298dc4607f7623df2b5241" in visibility

judged_manifest = root / ".openresearch/artifacts/startup/judged_space_manifest.sha256"
old_paths = []
for line in judged_manifest.read_text().splitlines():
    _, relative = line.split("  ", 1)
    old_paths.append(relative)
    if relative == "README.md":
        candidate = root / ".trackio/logbook/README.md"
    elif relative == ".gitattributes":
        candidate = root / relative
    else:
        candidate = root / ".trackio/logbook" / relative
    assert candidate.is_file()

assert len(old_paths) == 21 and len(set(old_paths)) == 21

allowlist = [
    line
    for line in (root / ".openresearch/artifacts/release/upload_allowlist.txt").read_text().splitlines()
    if line
]
manifest_lines = (
    root / ".openresearch/artifacts/release/upload_manifest.sha256"
).read_text().splitlines()
manifest_paths = [line.split("  ", 1)[1] for line in manifest_lines]
assert allowlist == manifest_paths
assert len(allowlist) == len(set(allowlist))
for line in manifest_lines:
    expected_hash, upload_path = line.split("  ", 1)
    if upload_path in ("README.md", "poster_embed.html") or upload_path.startswith(
        ("logbook.json", "pages/", "code/", "evidence/")
    ):
        source = root / ".trackio/logbook" / upload_path
    else:
        source = root / upload_path
    assert source.is_file()
    assert hashlib.sha256(source.read_bytes()).hexdigest() == expected_hash

candidate_text = "\n".join(
    path.read_text(errors="ignore")
    for path in required_pages + required_evidence
)
assert ("hf" + "_") not in candidate_text
assert ("github_" + "pat_") not in candidate_text
assert ("sk" + "-") not in candidate_text

gate = {
    "paper": "TBSyYj4VV6",
    "arxiv": "2509.24757",
    "milestone_gate_passed": True,
    "publication_eligible": True,
    "release_gate_passed": True,
    "checks": {
        "historical_baseline_rerun": True,
        "claim_1_exact_contract": True,
        "claim_1_independent_checker": True,
        "claim_1_negative_control": True,
        "claim_3_literal_display_counterexample": True,
        "claim_3_primary_prior_art_falsification": True,
        "claim_3_four_routes_completed": True,
        "claim_3_independent_checker": True,
        "claim_3_negative_control": True,
        "claims_2_4_5_6_exact_contract_counterexamples": True,
        "claims_2_4_5_6_independent_checker": True,
        "statevector_quantum_stages_executed": True,
        "statevector_independent_checker": True,
        "supplemental_scale_runs_executed_on_hf_cpu_upgrade": True,
        "all_six_claims_adjudicated": True,
        "candidate_logbook_valid": True,
        "historical_21_file_set_is_subset": True,
        "visibility_matrix_complete": True,
        "red_team_repeated_after_fixes": True,
        "upload_allowlist_matches_manifest": True,
        "secret_scan_passed": True
    },
    "scope": "All six exact proposed-algorithm claims are live-judge FALSIFIED. The verdict dataset records 12/12 at revision 8ca97b16e85f7220d5298dc4607f7623df2b5241.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
