#!/usr/bin/env python3
from __future__ import annotations
import csv, json, argparse
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("status_csv", type=Path)
    ap.add_argument("--output", type=Path, default=Path("executive-dashboard.json"))
    args = ap.parse_args()

    counts = {"Compliant":0,"Partially Compliant":0,"Noncompliant":0,"Not Applicable":0}
    severity = {"Critical":0,"High":0,"Medium":0,"Low":0}
    rows = list(csv.DictReader(args.status_csv.open(encoding="utf-8")))
    for row in rows:
        counts[row["Status"]] = counts.get(row["Status"], 0) + 1
        if row["Status"] != "Compliant":
            severity[row["Severity"]] = severity.get(row["Severity"], 0) + 1

    total = sum(counts.values())
    score = round(((counts["Compliant"] + 0.5*counts["Partially Compliant"]) / total) * 100, 1) if total else 100
    payload = {
        "control_count": total,
        "compliance_score": score,
        "status_breakdown": counts,
        "open_findings_by_severity": severity
    }
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
