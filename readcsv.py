import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute("SELECT * FROM ooh_maindatabase")
rows = cur.fetchall()
for row in rows:
  print(row)