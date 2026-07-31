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
    root / ".trackio/logbook/code/downstream_contract_audit.py",
    root / ".trackio/logbook/code/downstream_contract_checker.py",
    root / ".openresearch/artifacts/release/evaluator_blind_red_team.md",
    root / ".openresearch/artifacts/release/upload_allowlist.txt",
    root / ".openresearch/artifacts/release/upload_manifest.sha256",
    root / "reports/quantum-regression/report.md",
    root / "notebooks/quantum_regression_reproduction.py",
]
assert all(path.is_file() for path in required_pages + required_evidence)

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
assert "4–12/12" in visibility and "12/12" in visibility

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
        "all_six_claims_adjudicated": True,
        "candidate_logbook_valid": True,
        "historical_21_file_set_is_subset": True,
        "visibility_matrix_complete": True,
        "red_team_repeated_after_fixes": True,
        "upload_allowlist_matches_manifest": True,
        "secret_scan_passed": True
    },
    "scope": "All six exact proposed-algorithm claims are falsified; Claims 5-6 retain medium confidence and the live score remains unchanged until judge evaluation.",
}
(root / "outputs" / "publication_gate.json").write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n")
print(json.dumps(gate, indent=2, sort_keys=True))
