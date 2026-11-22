"""Poke the database layer with good and bad inputs."""

from failed_payment_crew import db

print("own record    :", db.get_transaction("TXN-000103", "ACC-1001") is not None)
print("other account :", db.get_transaction("TXN-000140", "ACC-1001"))
print("messy typing  :", db.get_transaction(" txn-000103 ", "ACC-1001") is not None)
print("no reference  :", db.get_transaction(None, "ACC-1001"))
print("sql injection :", db.get_transaction("TXN-000103' OR '1'='1", "ACC-9999"))