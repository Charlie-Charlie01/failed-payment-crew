# RB05: Successful on our side, recipient says not credited

## RB05.1 Signals
- `status = success`
- The customer says the recipient hasn't received the money

## RB05.2 Meaning
`success` means the platform delivered the transfer to the receiving bank. It doesn't guarantee the recipient's bank credited the account straight away.

## RB05.3 Action
- **Age ≤ 24h:** don't escalate. Advise that the recipient check with their bank, quoting the transaction reference.
- **Age > 24h:** escalate to Payments Ops for a session-ID trace with the beneficiary bank.

## RB05.4 Customer-safe wording
"Our records show this transfer was delivered to the receiving bank. Please ask the recipient to contact their bank with the reference below."

Never tell the customer the money will be refunded. The transfer succeeded.
