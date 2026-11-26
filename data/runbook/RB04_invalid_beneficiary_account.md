# RB04: Invalid beneficiary account

## RB04.1 Signals
- `failure_code = INVALID_ACCOUNT`
- Usually `reversal_status = completed`

## RB04.2 Meaning
The receiving bank rejected the account number or the name doesn't match. The money has been returned to the customer.

## RB04.3 Action
Don't escalate. Ask the customer to confirm the account number and bank with the recipient before retrying. If `reversal_status` is `pending`, apply RB02.3 for the reversal timing.

## RB04.4 Customer-safe wording
"The receiving bank couldn't match the account details, so the transfer was returned to your wallet. Please confirm the account number and bank with the recipient, then try again."
