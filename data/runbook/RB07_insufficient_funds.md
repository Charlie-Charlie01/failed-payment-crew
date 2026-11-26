# RB07: Insufficient funds (no debit)

## RB07.1 Signals
- `status = failed`
- `failure_code = INSUFFICIENT_FUNDS`
- `customer_debited = false`

## RB07.2 Meaning
The transfer was declined before any debit, so no money left the wallet. The customer may be confusing a balance hold or a different transaction with this one.

## RB07.3 Action
Don't escalate. Explain that no debit happened for this reference, and ask the customer to share a statement line if they still see a deduction.

## RB07.4 Customer-safe wording
"This transfer was declined because the wallet balance was too low at the time, so no money was taken for it. If you still see a deduction, please send us the statement entry and we'll look into it."
