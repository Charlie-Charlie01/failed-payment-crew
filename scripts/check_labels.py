"""Do the labels in evals/labels.json agree with the runbook rules?"""

import json
from pathlib import Path

from failed_payment_crew import db
from failed_payment_crew.baseline import diagnose

ROOT = Path(__file__).resolve().parents[1]
labels = {l["ticket_id"]: l for l in json.loads((ROOT / "evals" / "labels.json").read_text(encoding="utf-8"))}

passed = 0
for path in sorted((ROOT / "data" / "tickets").glob("t*.json")):
    ticket = json.loads(path.read_text(encoding="utf-8"))
    record = db.get_transaction(ticket["transaction_ref"], ticket["account_id"])
    d = diagnose(ticket, record)
    if d.age_hours is not None and d.age_hours < 0:
        print(f"WARN  {ticket['ticket_id']}  ticket is dated BEFORE its transaction ({d.age_hours}h)")
    label = labels[ticket["ticket_id"]]

    ok = (d.root_cause, d.escalate) == (label["expected_root_cause"], label["expected_escalate"])
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {ticket['ticket_id']}  {d.root_cause:<30} escalate={d.escalate!s:<5}  age={d.age_hours}h  cite={d.citation}")
    if not ok:
        print(f"      expected: {label['expected_root_cause']}  escalate={label['expected_escalate']}")

print(f"\n{passed}/{len(labels)} labels agree with the runbook rules")