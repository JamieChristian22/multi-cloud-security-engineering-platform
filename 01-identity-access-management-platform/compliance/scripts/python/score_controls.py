#!/usr/bin/env python3
"""Calculate a weighted compliance score from a control-status CSV."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path

WEIGHTS = {"Critical": 5, "High": 3, "Medium": 2, "Low": 1}
SCORES = {"Compliant": 1.0, "Partially Compliant": 0.5, "Noncompliant": 0.0, "Not Applicable": None}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()

    earned = possible = 0.0
    with args.csv_file.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            severity = row["Severity"].strip()
            status = row["Status"].strip()
            weight = WEIGHTS[severity]
            factor = SCORES[status]
            if factor is None:
                continue
            possible += weight
            earned += weight * factor

    score = 100.0 if possible == 0 else (earned / possible) * 100
    print(f"Weighted compliance score: {score:.1f}%")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
