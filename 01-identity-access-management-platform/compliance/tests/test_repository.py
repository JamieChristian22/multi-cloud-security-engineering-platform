from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parents[1]

def test_required_files_exist():
    required = [
        ROOT / "README.md",
        ROOT / "cross-cloud/control-mappings/control-matrix.csv",
        ROOT / "cross-cloud/risk-register/risk-register.csv",
        ROOT / "terraform/aws/main.tf",
        ROOT / "terraform/azure/main.tf",
        ROOT / "terraform/gcp/main.tf",
    ]
    assert all(path.exists() for path in required)

def test_control_ids_unique():
    path = ROOT / "cross-cloud/control-mappings/control-matrix.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    ids = [r["Control ID"] for r in rows]
    assert len(ids) == len(set(ids))

def test_json_files_valid():
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
