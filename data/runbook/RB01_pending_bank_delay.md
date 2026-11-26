# RB01: Pending transfer (bank delay)

## RB01.1 Signals
- `status = pending`
- `customer_debited = true`

## RB01.2 Meaning
The transfer is still being processed. This is usually because the platform can't get a final answer from the beneficiary bank yet. Pending is not a final state. The system keeps retrying and the transfer eventually ends as `success` or `failed`. A failed transfer is then reversed.

## RB01.3 Action
- **Age ≤ 24h:** don't escalate. Tell the customer the transfer is still processing and that no action is needed from them.
- **Age > 24h:** escalate to Payments Ops with the reference and the destination bank. The case needs a manual status query.

## RB01.4 Customer-safe wording
"Your transfer is still being processed with the receiving bank. If it doesn't go through, the amount will be returned to your wallet automatically. We'll update you once the status changes."

Don't say when the transfer will complete or when a refund will arrive.
