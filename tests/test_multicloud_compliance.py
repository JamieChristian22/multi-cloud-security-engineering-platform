"""Regression tests for sample compliance math, control integrity and honest evidence limits."""
from __future__ import annotations
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COMPLIANCE = ROOT / "01-identity-access-management-platform/compliance"
MOD = COMPLIANCE / "scripts/python"
sys.path.insert(0, str(MOD))
from compliance_metrics import read_controls, summarize

SOURCE = COMPLIANCE / "cross-cloud/audit/control-status.csv"

def test_sample_weighted_score_matches_manual_expected():
    result = summarize(read_controls(SOURCE))
    assert result["control_count"] == 10
    assert result["weighted_compliance_score"] == 91.9  # (37 - 2*1.5) / 37
    assert result["status_breakdown"]["Partially Compliant"] == 2
    assert result["open_findings_by_severity"]["High"] == 2
    assert result["open_findings_by_severity"]["Critical"] == 0
    assert result["weight_possible"] == 37
    assert result["weight_earned"] == 34

def test_no_applicable_controls_is_not_falsely_100_percent():
    result = summarize([{"Status": "Not Applicable", "Severity": "Critical", "Assessment Date": "2026-08-03"}])
    assert result["weighted_compliance_score"] is None
    assert result["excluded_not_applicable"] == 1
    assert result["open_findings_by_severity"]["Critical"] == 0

@pytest.mark.parametrize("bad_column,bad_value", [
    ("Status", "Unknown"), ("Severity", "Trivial"), ("Control ID", ""),
    ("Control", ""), ("Assessment Date", "")
])
def test_invalid_status_records_fail_closed(tmp_path, bad_column, bad_value):
    import csv
    rows = read_controls(SOURCE)
    rows[0][bad_column] = bad_value
    test_file = tmp_path / "bad.csv"
    with test_file.open("w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError):
        read_controls(test_file)

def test_duplicate_control_id_and_empty_input_rejected(tmp_path):
    import csv
    rows = read_controls(SOURCE)
    rows[1]["Control ID"] = rows[0]["Control ID"]
    p = tmp_path / "dup.csv"
    with p.open("w", newline="") as out:
        w = csv.DictWriter(out, fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    with pytest.raises(ValueError):
        read_controls(p)
    p.write_text("Control ID,Control,Severity,Status,Assessment Date,Assessor\n")
    with pytest.raises(ValueError):
        read_controls(p)

def test_executive_score_matches_cli_logic(tmp_path):
    from build_executive_dashboard import main
    old = sys.argv
    try:
        path = tmp_path / "dashboard.json"
        sys.argv = ["build_executive_dashboard.py", str(SOURCE), "--output", str(path)]
        assert main() == 0
        report = json.loads(path.read_text())
        assert report == summarize(read_controls(SOURCE))
    finally:
        sys.argv = old

def test_source_checker_counts_all_cloud_roots_and_no_unknown_status():
    spec = importlib.util.spec_from_file_location("validate_multicloud", ROOT / "scripts/validate_multicloud.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    result, errors = m.check()
    assert not errors, errors
    assert result["terraform_roots"] == 15
    assert result["terraform_roots_by_provider"] == {"aws": 5, "azure": 5, "gcp": 5}
    assert result["illustrative_iam_summary"]["control_count"] == 10
