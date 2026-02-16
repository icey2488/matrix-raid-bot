import sqlite3
from contextlib import contextmanager

DB_PATH = "data/raidbot.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try: yield conn
    finally:
        conn.commit()
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (matrix_id TEXT PRIMARY KEY, char_name TEXT, server TEXT, class TEXT)")
        conn.execute("CREATE TABLE IF NOT EXISTS raids (event_id TEXT PRIMARY KEY, title TEXT, timestamp TEXT, room_id TEXT, locked INTEGER DEFAULT 0)")
        conn.execute("CREATE TABLE IF NOT EXISTS signups (event_id TEXT, matrix_id TEXT, status TEXT, PRIMARY KEY (event_id, matrix_id))")

def get_raid(event_id):
    with get_db() as conn: return conn.execute("SELECT * FROM raids WHERE event_id = ?", (event_id,)).fetchone()

def lock_raid(event_id):
    with get_db() as conn: conn.execute("UPDATE raids SET locked = 1 WHERE event_id = ?", (event_id,))

def get_active_raids():
    with get_db() as conn: return conn.execute("SELECT * FROM raids WHERE locked = 0").fetchall()

def get_roster(event_id):
    with get_db() as conn:
        return conn.execute("SELECT s.*, u.char_name, u.class FROM signups s LEFT JOIN users u ON s.matrix_id = u.matrix_id WHERE s.event_id = ?", (event_id,)).fetchall()