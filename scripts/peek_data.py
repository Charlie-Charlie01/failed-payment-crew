"""Show a ticket, the record behind it, and the expected answer. No AI involved."""

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]   # the project folder

ticket_id = sys.argv[1] if len(sys.argv) > 1 else "t001"

# 1. Read the ticket (what the customer said)
ticket_path = ROOT / "data" / "tickets" / f"{ticket_id}.json"
ticket = json.loads(ticket_path.read_text(encoding="utf-8"))

# 2. Find the matching record, but only if it belongs to this customer
with open(ROOT / "data" / "transactions.csv", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
record = next(
    (r for r in rows
     if r["ref"] == ticket["transaction_ref"] and r["account_id"] == ticket["account_id"]),
    None,
)

# 3. Read the expected answer (only scripts like this see it, never the AI)
labels = json.loads((ROOT / "evals" / "labels.json").read_text(encoding="utf-8"))
label = next(l for l in labels if l["ticket_id"] == ticket_id)

print("TICKET  :", ticket["message"])
print("RECORD  :", record if record else "NOT FOUND for this customer")
print("EXPECTED:", label["expected_root_cause"], "| escalate =", label["expected_escalate"])