# Failed Payment Crew

A CrewAI multi-agent system that investigates "debited but transfer failed" complaints:
it looks up the transaction, diagnoses the cause from a runbook, and drafts a reply
for a human to review.

Built step by step, in public. All data is synthetic.

## Progress
- [x] Lesson 1: project skeleton and environment
- [x] Lesson 2: synthetic data (transactions, tickets, answer key)
- [ ] Lesson 3: database lookup

## Setup
    uv venv --python 3.12
    .venv\Scripts\activate
    uv pip install -e ".[dev]"
    copy .env.example .env   # add your OPENAI_API_KEY

## Try it
    python scripts\peek_data.py t001