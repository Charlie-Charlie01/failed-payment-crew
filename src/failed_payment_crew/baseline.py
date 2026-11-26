"""Rule-based diagnosis, written straight from data/runbook/. No AI involved.

Used to check the answer key, as a fallback when the AI crew fails,
and as the baseline the crew is scored against.
"""

from __future__ import annotations

from dataclasses import dataclass

from . import db

PENDING_ESCALATE_H = 24     # RB01.3
REVERSAL_ESCALATE_H = 72    # RB02.3
SUCCESS_ESCALATE_H = 24     # RB05.3


@dataclass
class Diagnosis:
    root_cause: str
    escalate: bool
    citation: str
    age_hours: float | None = None


def diagnose(ticket: dict, record: dict | None) -> Diagnosis:
    # RB08.1: no record means we can't investigate, so a human must.
    if record is None:
        return Diagnosis("transaction_not_found", True, "RB08.1")

    age = db.age_hours(record, ticket["created_at"])
    status = record["status"]
    code = record["failure_code"]
    reversal = record["reversal_status"]
    debited = record["customer_debited"] == "true"

    # RB06: a repeated debit always needs a person.
    if record["duplicate_of_ref"]:
        return Diagnosis("duplicate_debit", True, "RB06.3", age)

    # RB08.1: fields that contradict each other.
    conflict = (
        (status in ("success", "pending") and reversal != "none")
        or (status == "reversed" and reversal != "completed")
        or (status == "failed" and code != "INSUFFICIENT_FUNDS" and debited and reversal == "none")
    )
    if conflict:
        return Diagnosis("conflicting_records", True, "RB08.1", age)

    # RB07: declined before any money left.
    if status == "failed" and code == "INSUFFICIENT_FUNDS" and not debited:
        return Diagnosis("insufficient_funds", False, "RB07.3", age)

    # RB04: wrong account details.
    if code == "INVALID_ACCOUNT":
        stuck = reversal == "pending" and age > REVERSAL_ESCALATE_H
        return Diagnosis("invalid_beneficiary_account", stuck, "RB04.3", age)

    # RB03: money already back in the wallet.
    if status == "reversed" or (status == "failed" and reversal == "completed"):
        return Diagnosis("reversed_funds_returned", False, "RB03.3", age)

    # RB02: failed, money on its way back.
    if status == "failed" and reversal == "pending":
        return Diagnosis("reversal_in_progress", age > REVERSAL_ESCALATE_H, "RB02.3", age)

    # RB01: still processing.
    if status == "pending":
        return Diagnosis("pending_bank_delay", age > PENDING_ESCALATE_H, "RB01.3", age)

    # RB05: delivered on our side, recipient says not credited.
    if status == "success":
        return Diagnosis("success_recipient_not_credited", age > SUCCESS_ESCALATE_H, "RB05.3", age)

    # Anything else doesn't fit the runbook: let a human look.
    return Diagnosis("conflicting_records", True, "RB08.1", age)