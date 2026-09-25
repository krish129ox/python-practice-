import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE exp(cat TEXT, amt REAL)")
db.executemany("INSERT INTO exp VALUES (?,?)",
               [("food", 250), ("travel", 900), ("food", 120)])
for row in db.execute("SELECT cat, SUM(amt) FROM exp GROUP BY cat ORDER BY 2 DESC"):
    print(row)