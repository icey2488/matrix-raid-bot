Moves the existing database logic into matrix_raid_bot/database/sqlite.py
as part of the modular architecture refactor. This commit preserves all
current functionality while relocating the persistence layer into the
new package structure. No behavioral changes introduced; this is a
straight migration to support future service and command integration.

matrix_raid_bot/database/sqlite.py

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional, Any


class Database:
    def __init__(self, path: str) -> None:
        self._path = Path(path)
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    @contextmanager
    def _conn(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self._path)
        try:
            yield conn
        finally:
            conn.close()

    def _init_schema(self) -> None:
        with self._conn() as conn:
            cur = conn.cursor()

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS raids (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    external_id TEXT,
                    name TEXT,
                    start_time TEXT,
                    signup_message_event_id TEXT
                )
                """
            )

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS signups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    raid_id INTEGER,
                    character_name TEXT,
                    status TEXT,
                    UNIQUE(raid_id, character_name)
                )
                """
            )

            conn.commit()

    # -------------------------
    # RAID QUERIES
    # -------------------------

    def get_upcoming_raids(self) -> list[tuple]:
        with self._conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT id, external_id, name, start_time, signup_message_event_id
                FROM raids
                ORDER BY start_time ASC
                """
            )
            return cur.fetchall()

    def insert_raid(
        self,
        external_id: str,
        name: str,
        start_time: str,
        signup_message_event_id: Optional[str] = None,
    ) -> int:
        with self._conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO raids (external_id, name, start_time, signup_message_event_id)
                VALUES (?, ?, ?, ?)
                """,
                (external_id, name, start_time, signup_message_event_id),
            )
            conn.commit()
            return cur.lastrowid

    # -------------------------
    # SIGNUP QUERIES
    # -------------------------

    def upsert_signup(self, raid_id: int, character_name: str, status: str) -> None:
        with self._conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO signups (raid_id, character_name, status)
                VALUES (?, ?, ?)
                ON CONFLICT(raid_id, character_name)
                DO UPDATE SET status=excluded.status
                """,
                (raid_id, character_name, status),
            )
            conn.commit()

    def get_signups(self, raid_id: int) -> list[dict[str, Any]]:
        with self._conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT character_name, status
                FROM signups
                WHERE raid_id = ?
                ORDER BY character_name ASC
                """,
                (raid_id,),
            )
            rows = cur.fetchall()

        return [
            {"character_name": row[0], "status": row[1]}
            for row in rows
        ]
        
git add matrix_raid_bot/database/sqlite.py
git commit -m "refactor: migrate database layer into new modular structure"

Step 3 — Migrate WCL API into services/wcl.py
This is another safe, self‑contained migration.
If you want, I’ll generate:
- the full WCL service module
- the commit message
- and a VS Code walkthrough
Just say “Proceed to Step 3”.
