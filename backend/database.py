import sqlite3

def init_db():

    conn = sqlite3.connect("users.db")

    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS scans(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    result TEXT
    )
    """)

    conn.commit()

    conn.close()