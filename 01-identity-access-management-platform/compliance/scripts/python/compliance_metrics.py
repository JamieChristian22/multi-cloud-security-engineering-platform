"""Validated *illustrative* control scoring, not cloud-provider attestation.

The checked-in control status CSV describes a sample IAM assessment. Statuses
do not establish live AWS/Azure/GCP configuration or audit certification.
"""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

WEIGHTS = {"Critical": 5, "High": 3, "Medium": 2, "Low": 1}
FACTORS = {"Compliant": 1.0, "Partially Compliant": 0.5,
           "Noncompliant": 0.0, "Not Applicable": None}
REQUIRED = {"Control ID", "Control", "Severity", "Status",
            "Assessment Date", "Assessor"}


def read_controls(path: Path) -> list[dict[str, str]]:
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not REQUIRED.issubset(set(reader.fieldnames)):
            raise ValueError("Missing required control-status CSV columns")
        rows = list(reader)
    if not rows:
        raise ValueError("Control-status CSV is empty; no compliance score is defined")
    ids: set[str] = set()
    for row in rows:
        identifier = (row.get("Control ID") or "").strip()
        if not identifier or identifier in ids:
            raise ValueError("Missing or duplicate control ID")
        ids.add(identifier)
        if not (row.get("Control") or "").strip():
            raise ValueError(f"{identifier}: missing control label")
        if row.get("Severity") not in WEIGHTS:
            raise ValueError(f"{identifier}: unknown severity {row.get('Severity')!r}")
        if row.get("Status") not in FACTORS:
            raise ValueError(f"{identifier}: unknown status {row.get('Status')!r}")
        if not (row.get("Assessment Date") or "").strip():
            raise ValueError(f"{identifier}: missing assessment date")
    return rows


def summarize(rows: list[dict[str, str]]) -> dict:
    if not rows:
        raise ValueError("Cannot score an empty assessment")
    counts = Counter({status: 0 for status in FACTORS})
    open_by_severity = Counter({severity: 0 for severity in WEIGHTS})
    earned, possible = 0.0, 0.0
    for row in rows:
        status = row["Status"]
        severity = row["Severity"]
        if status not in FACTORS or severity not in WEIGHTS:
            raise ValueError("Unrecognized status or severity")
        counts[status] += 1
        if status in {"Partially Compliant", "Noncompliant"}:
            open_by_severity[severity] += 1
        factor = FACTORS[status]
        if factor is not None:
            possible += WEIGHTS[severity]
            earned += WEIGHTS[severity] * factor
    return {
        "schema_version": 1,
        "source_kind": "Sample IAM control-status register, not verified live cloud findings",
        "control_count": len(rows),
        "weighted_compliance_score": round(earned / possible * 100, 1) if possible else None,
        "weight_earned": earned,
        "weight_possible": possible,
        "status_breakdown": dict(counts),
        "open_findings_by_severity": dict(open_by_severity),
        "assessed_dates": sorted({row["Assessment Date"] for row in rows}),
        "excluded_not_applicable": counts["Not Applicable"],
        "interpretation": "Illustrative weighted score only. Validate live configuration and evidence separately."
    }
