#!/usr/bin/env python3
"""Build an evidence-limited executive summary from a sample control CSV."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from compliance_metrics import read_controls, summarize

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("status_csv", type=Path)
    ap.add_argument("--output", type=Path, default=Path("executive-dashboard.json"))
    args = ap.parse_args()
    payload = summarize(read_controls(args.status_csv))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
