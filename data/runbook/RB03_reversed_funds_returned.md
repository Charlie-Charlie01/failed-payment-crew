# RB03: Transfer reversed, funds returned

## RB03.1 Signals
- `status = reversed`, or `status = failed` with `reversal_status = completed`
- Any `failure_code` other than `INVALID_ACCOUNT` (RB04 covers that code)

## RB03.2 Meaning
The receiving side couldn't credit the recipient, and the money has already been returned to the customer's wallet.

## RB03.3 Action
Don't escalate. Tell the customer the funds are back in their wallet and that they can retry the transfer.

## RB03.4 Customer-safe wording
"This transfer couldn't be completed, and the full amount has been returned to your wallet. You can try the transfer again."
