import sqlite3

conn = sqlite3.connect('board.sqlite')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    message TEXT NOT NULL
)
""")

conn.commit()
conn.close()