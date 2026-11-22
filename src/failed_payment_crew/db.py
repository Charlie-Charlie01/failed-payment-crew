"""SQLite store for the synthetic transactions.

The CSV is the source of truth. The database is rebuilt from it whenever
the CSV is newer, so there's nothing to set up by hand.
"""

from __future__ import annotations

import csv
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # db.py -> failed_payment_crew -> src -> project
CSV_PATH = ROOT / "data" / "transactions.csv"
DB_PATH = ROOT / "data" / "transactions.db"


def build() -> None:
    """Create the transactions table from the CSV, replacing any old copy."""
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    columns = list(rows[0].keys())

    con = sqlite3.connect(DB_PATH)
    with con:                                       # commits the changes at the end
        con.execute("DROP TABLE IF EXISTS transactions")
        col_defs = ", ".join("ref TEXT PRIMARY KEY" if c == "ref" else f"{c} TEXT" for c in columns)
        con.execute(f"CREATE TABLE transactions ({col_defs})")
        placeholders = ", ".join("?" for _ in columns)
        con.executemany(
            f"INSERT INTO transactions VALUES ({placeholders})",
            [tuple(row[c] for c in columns) for row in rows],
        )
    con.close()


def connect() -> sqlite3.Connection:
    """Open the database, rebuilding it first if it's missing or older than the CSV."""
    if not DB_PATH.exists() or DB_PATH.stat().st_mtime < CSV_PATH.stat().st_mtime:
        build()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row                  # rows behave like dictionaries
    return con


def get_transaction(ref: str | None, account_id: str) -> dict | None:
    """Return the record only if it exists AND belongs to this customer."""
    if not ref:
        return None
    con = connect()
    try:
        row = con.execute(
            "SELECT * FROM transactions WHERE ref = ? AND account_id = ?",
            (ref.strip().upper(), account_id),
        ).fetchone()
    finally:
        con.close()
    return dict(row) if row else None


def age_hours(record: dict, ticket_created_at: str) -> float:
    """Hours between the transfer and the ticket, e.g. 2.0."""
    created = datetime.fromisoformat(record["created_at"])
    asked = datetime.fromisoformat(ticket_created_at)
    return round((asked - created).total_seconds() / 3600, 1)