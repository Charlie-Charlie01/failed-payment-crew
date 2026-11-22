"""Show a ticket, the record behind it, and the expected answer. No AI involved."""

import json
import sys
from pathlib import Path

from failed_payment_crew import db

ROOT = Path(__file__).resolve().parents[1]
ticket_id = sys.argv[1] if len(sys.argv) > 1 else "t001"

ticket = json.loads((ROOT / "data" / "tickets" / f"{ticket_id}.json").read_text(encoding="utf-8"))
record = db.get_transaction(ticket["transaction_ref"], ticket["account_id"])

labels = json.loads((ROOT / "evals" / "labels.json").read_text(encoding="utf-8"))
label = next(l for l in labels if l["ticket_id"] == ticket_id)

print("TICKET  :", ticket["message"])
if record:
    print("RECORD  :", record["ref"], "|", record["status"],
          "| debited =", record["customer_debited"], "| reversal =", record["reversal_status"])
    print("AGE     :", db.age_hours(record, ticket["created_at"]), "hours")
else:
    print("RECORD  : NOT FOUND for this customer")
print("EXPECTED:", label["expected_root_cause"], "| escalate =", label["expected_escalate"])