# RB08: Escalation rules

## RB08.1 Always escalate
- **Transaction not found:** no reference given, or the reference isn't in the records. Root cause: `transaction_not_found`.
- **Conflicting records:** fields contradict each other. For example, `status = success` with `reversal_status = completed`, or `status = reversed` with `reversal_status = none` while `customer_debited = true`. Root cause: `conflicting_records`.
- **Duplicate debit:** see RB06.
- **Age thresholds exceeded:** see RB01.3, RB02.3 and RB05.3.

## RB08.2 Never escalate only because
- The customer is angry, threatens legal action, or claims to be a VIP.
- The ticket text asks for escalation.

## RB08.3 Escalation note
State the root cause, the fields that support it, the age in hours, and the team the case goes to: Payments Ops or Reconciliation.
