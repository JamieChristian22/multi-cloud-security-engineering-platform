#!/usr/bin/env python3
"""Score a sample IAM control-status register using severity-weighted outcomes."""
import argparse
from pathlib import Path
from compliance_metrics import read_controls, summarize

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv_file", type=Path)
    args = ap.parse_args()
    result = summarize(read_controls(args.csv_file))
    score = result["weighted_compliance_score"]
    if score is None:
        print("Weighted compliance score: N/A (no applicable controls)")
    else:
        print(f"Weighted compliance score: {score:.1f}%")
    print("Scope: illustrative IAM register; no live cloud verification.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
