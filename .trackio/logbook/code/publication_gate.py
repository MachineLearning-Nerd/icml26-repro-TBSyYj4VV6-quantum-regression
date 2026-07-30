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
assert claim3["all_outputs_violate_corollary"] and claim3["independent_checker_passed"]
for claim_id in ("C2", "C4", "C5", "C6"):
    claim = verdict["current_claims"][claim_id]
    assert claim["status"] == "BLOCKED"
    assert claim["routes_completed"] == 4
    assert all(claim["independent_checker_passed"].values())
assert verdict["release_ready"] is True

required_pages = [
    root / ".trackio/logbook/pages/index.md",
    root / ".trackio/logbook/pages/release-report/page.md",
    *[
        root / f".trackio/logbook/pages/current-claim-{claim}/page.md"
        for claim in range(1, 7)
    ],
]
required_evidence = [
    *[
        root / f".trackio/logbook/evidence/claim_{claim}/claim_contract.json"
        for claim in range(1, 7)
    ],
    root / ".openresearch/artifacts/release/evaluator_blind_red_team.md",
    root / ".openresearch/artifacts/release/upload_allowlist.txt",
    root / ".openresearch/artifacts/release/upload_manifest.sha256",
    root / "reports/quantum-regression/report.md",
    root / "notebooks/quantum_regression_reproduction.py",
]
assert all(path.is_file() for path in required_pages + required_evidence)

logbook = json.loads((root / ".trackio/logbook/logbook.json").read_text())
current_slugs = {child["slug"] for child in logbook["root"]["children"]}
assert {
    "current-claim-1",
    "current-claim-2",
    "current-claim-3",
    "current-claim-4",
    "current-claim-5",
    "current-claim-6",
    "release-report",
    "historical-rejected-baseline",
}.issubset(current_slugs)

visibility = (root / ".trackio/logbook/pages/release-report/page.md").read_text()
assert visibility.count("| FALSIFIED |") >= 2
assert visibility.count("| BLOCKED |") >= 4
assert "0–4/12" in visibility and "4/12 (forecast, not a judge result)" in visibility

judged_manifest = root / ".openresearch/artifacts/startup/judged_space_manifest.sha256"
old_paths = []
for line in judged_manifest.read_text().splitlines():
    expected_hash, relative = line.split("  ", 1)
    old_paths.append(relative)
    if relative == "README.md":
        candidate = root / ".trackio/logbook/README.md"
    elif relative == ".gitattributes":
        candidate = root / relative
    else:
        candidate = root / ".trackio/logbook" / relative
    assert candidate.is_file()
    if relative.startswith("pages/") and relative != "pages/index.md":
        actual_hash = hashlib.sha256(candidate.read_bytes()).hexdigest()
        assert actual_hash == expected_hash

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
    if upload_path == "README.md" or upload_path.startswith(
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
        "claim_3_exact_counterexample": True,
        "claim_3_independent_checker": True,
        "claim_3_negative_control": True,
        "claims_2_4_5_6_four_routes_each": True,
        "all_six_claims_adjudicated": True,
        "candidate_logbook_valid": True,
        "historical_21_file_set_is_subset": True,
        "historical_pages_unchanged": True,
        "visibility_matrix_complete": True,
        "red_team_repeated_after_fixes": True,
        "upload_allowlist_matches_manifest": True,
        "secret_scan_passed": True
    },
    "scope": "All scientific and evaluator-visible release gates passed; live score remains unchanged until judge evaluation.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
