# RB00: How to use this runbook

> **Synthetic internal policy.** These thresholds and wording rules are invented for this portfolio project. The status meanings are based on public Paystack and Flutterwave transfer documentation. The timelines are not real provider guarantees.

## RB00.1 Transaction fields

| Field | Meaning |
|---|---|
| `status` | `pending`, `success`, `failed`, or `reversed` |
| `failure_code` | Set only when `status` is `failed` or `reversed` |
| `customer_debited` | `true` if the customer's wallet was debited |
| `reversal_status` | `none`, `pending`, or `completed`. Only meaningful after a debit on a transfer that didn't complete |
| `duplicate_of_ref` | Set when this debit repeats an earlier transfer |

## RB00.2 Age

Age is the number of hours between the transaction's `created_at` and the ticket's `created_at`. Every age threshold in this runbook uses this definition.

## RB00.3 Citing

Cite sections by ID, for example `RB02.3`. Every claim in a reply or internal note must cite either a transaction field or a runbook section.
