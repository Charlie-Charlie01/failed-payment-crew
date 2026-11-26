# RB02: Failed transfer, reversal in progress

## RB02.1 Signals
- `status = failed`
- `customer_debited = true`
- `reversal_status = pending`
- Typical `failure_code`: `BENEFICIARY_BANK_UNAVAILABLE`, `PROCESSOR_TIMEOUT`, or `SWITCH_ERROR`

## RB02.2 Meaning
The transfer didn't reach the recipient. The debit is being reversed automatically to the customer's wallet.

## RB02.3 Action
- **Age ≤ 72h:** don't escalate. Confirm that the reversal is in progress.
- **Age > 72h:** escalate to Reconciliation. A reversal stuck this long needs manual handling.

## RB02.4 Customer-safe wording
"Your transfer didn't go through, and a reversal to your wallet has already started. Reversals usually complete within 24 hours."

"Usually" is required in that sentence. Never guarantee a time, and never say "refund approved".
