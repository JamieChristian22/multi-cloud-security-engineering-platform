#!/usr/bin/env python3
"""Offline evidence guardrails for the four-project, 15-root multi-cloud lab.

No cloud APIs, service-account credentials or Terraform plans are executed.
"""
from __future__ import annotations
import argparse
import csv
import json
import pathlib
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
COMPLIANCE = ROOT / "01-identity-access-management-platform" / "compliance"
ROOTS = sorted(p for p in (ROOT / "01-identity-access-management-platform").glob("terraform/*") if p.is_dir())
ROOTS += sorted(p for p in COMPLIANCE.glob("terraform/*") if p.is_dir())
for section in ("02-security-monitoring-threat-detection",
                "03-zero-trust-data-protection-platform",
                "04-cloud-security-governance-compliance"):
    ROOTS += sorted(p for p in (ROOT / section / "terraform").glob("*") if p.is_dir())
EXPECTED = {"aws", "azure", "gcp"}
COMPLIANCE_PY = COMPLIANCE / "scripts" / "python"
sys.path.insert(0, str(COMPLIANCE_PY))
from compliance_metrics import read_controls, summarize  # noqa: E402


def check() -> tuple[dict, list[str]]:
    errors: list[str] = []
    domains: dict[str, int] = Counter()
    if len(ROOTS) != 15:
        errors.append(f"Expected 15 Terraform roots, found {len(ROOTS)}")
    try:
        import hcl2
    except ImportError:
        errors.append("python-hcl2 is required for actual HCL syntax validation")
        hcl2 = None

    tf_files = 0
    for root in ROOTS:
        if root.name not in EXPECTED:
            errors.append(f"Unexpected Terraform provider folder: {root}")
        tf = sorted(root.glob("*.tf"))
        if not tf:
            errors.append(f"Empty Terraform root: {root.relative_to(ROOT)}")
        domains[root.name] += 1
        for path in tf:
            tf_files += 1
            if hcl2:
                try:
                    with path.open(encoding="utf-8") as stream:
                        hcl2.load(stream)
                except Exception as exc:
                    errors.append(f"Invalid HCL {path.relative_to(ROOT)}: {type(exc).__name__}: {exc}")
    for provider in sorted(EXPECTED):
        if domains[provider] != 5:
            errors.append(f"Expected 5 {provider} configurations; found {domains[provider]}")

    parsed_json = 0
    for path in ROOT.rglob("*.json"):
        if any(part in {".terraform", ".git", ".venv"} for part in path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
            parsed_json += 1
        except (OSError, ValueError) as exc:
            errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")

    status_path = COMPLIANCE / "cross-cloud/audit/control-status.csv"
    matrix_path = COMPLIANCE / "cross-cloud/control-mappings/control-matrix.csv"
    try:
        controls = read_controls(status_path)
        summary = summarize(controls)
        with matrix_path.open(encoding="utf-8-sig", newline="") as stream:
            matrix = list(csv.DictReader(stream))
        seen: set[str] = set()
        for item in matrix:
            code = item.get("Control ID", "").strip()
            if not code or code in seen:
                errors.append(f"Duplicate/blank cross-cloud mapping ID: {code!r}")
            seen.add(code)
            for provider in ("AWS", "Azure", "GCP"):
                if not (item.get(provider) or "").strip():
                    errors.append(f"Missing {provider} mapping for {code}")
        status_ids = {item["Control ID"] for item in controls}
        if status_ids != seen:
            errors.append("IAM control mapping IDs disagree with sample assessment IDs")
        for row in controls:
            definition = next((item for item in matrix if item["Control ID"] == row["Control ID"]), None)
            if definition and definition["Severity"] != row["Severity"]:
                errors.append(f"{row['Control ID']}: mapped severity differs from assessment")
    except (ValueError, OSError, KeyError) as exc:
        errors.append("Unable to verify compliance register: " + str(exc))
        summary = None

    result = {
        "status": "PASS_OFFLINE" if not errors else "FAIL",
        "scope": "Source syntax + sample IAM register consistency; no live AWS/Azure/GCP or provider schema checks",
        "terraform_roots": len(ROOTS),
        "terraform_files_parsed": tf_files,
        "terraform_roots_by_provider": dict(domains),
        "json_files_parsed": parsed_json,
        "illustrative_iam_summary": summary,
        "issues": errors,
    }
    return result, errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=pathlib.Path, default=ROOT / "reports/multicloud-source-validation.json")
    args = ap.parse_args()
    result, errors = check()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
