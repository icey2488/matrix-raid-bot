import asyncio
import json
import os
from datetime import datetime, timedelta
from nio import AsyncClient, MatrixRoom, RoomMessageText, ReactionEvent
from dotenv import load_dotenv
import database as db
import wcl_api

load_dotenv()
HOMESERVER = os.getenv("HOMESERVER", "https://matrix.org")
USER_ID = os.getenv("MATRIX_USER_ID")
PASSWORD = os.getenv("MATRIX_PASSWORD")
RAID_ROOM_ID = os.getenv("RAID_ROOM_ID")

WEEKLY_SCHEDULE = [
    {"day": 1, "time": "20:00", "title": "Tuesday Farm Raid"},
    {"day": 3, "time": "20:00", "title": "Thursday Progression"}
]

EMOJIS = {'✅': 'ATTENDING', '❔': 'TENTATIVE', '❌': 'ABSENT'}
REVERSE_EMOJIS = {v: k for k, v in EMOJIS.items()}

CLASS_COLORS = {
    "Death Knight": "#C41E3A", "Demon Hunter": "#A330C9", "Druid": "#FF7D0A",
    "Evoker": "#33937F", "Hunter": "#ABD473", "Mage": "#3FC7EB",
    "Monk": "#00FF98", "Paladin": "#F48CBA", "Priest": "#FFFFFF",
    "Rogue": "#FFF468", "Shaman": "#0070DD", "Warlock": "#8788EE", "Warrior": "#C69B6D"
}

class MatrixRaidBot:
    def __init__(self):
        self.client = AsyncClient(HOMESERVER, USER_ID)
        db.init_db()

    async def generate_html(self, raid_id):
        raid = db.get_raid(raid_id)
        locked = bool(raid['locked'])
        roster_data = db.get_roster(raid_id)

        categories = {"ATTENDING": [], "TENTATIVE": [], "ABSENT": []}
        for row in roster_data:
            if row['char_name']:
                color = CLASS_COLORS.get(row['class'], "#FFFFFF")
                display = f"<span style='color: {color};'>{row['char_name']}</span>"
            else:
                display = f"<span style='color: #888888;'>{row['matrix_id']}</span>"
            categories[row['status']].append(display)

        border = "#555555" if locked else "#00FF00"
        html = f"<div style='border-left: 5px solid {border}; padding: 10px; background-color: #121212; color: white;'>"
        html += f"<h3 style='color: {border};'>{raid['title']}</h3><b>Time:</b> {raid['timestamp']}<br/>"
        if locked: html += "<i>🔒 Signups Closed</i>"
        html += "<hr/>"
        for cat, members in categories.items():
            html += f"<p>{REVERSE_EMOJIS[cat]} <b>{cat}:</b> {', '.join(members) or '-'}</p>"
        html += "</div>"
        return html

    async def background_loop(self):
        while True:
            now = datetime.now()
            # Auto-Lock Logic
            active_raids = db.get_active_raids()
            for r in active_raids:
                if now >= datetime.fromisoformat(r['timestamp']):
                    db.lock_raid(r['event_id'])
                    await self.update_ui(r['room_id'], r['event_id'])
            await asyncio.sleep(60)

    async def update_ui(self, room_id, event_id):
        html = await self.generate_html(event_id)
        content = {
            "body": "Raid Update", "msgtype": "m.text", "format": "org.matrix.custom.html", "formatted_body": html,
            "m.new_content": {"body": "Raid Update", "msgtype": "m.text", "format": "org.matrix.custom.html", "formatted_body": html},
            "m.relates_to": {"rel_type": "m.replace", "event_id": event_id}
        }
        await self.client.room_send(room_id, "m.room.message", content)

    async def message_callback(self, room, event):
        if event.sender == USER_ID: return
        if event.body == "!help":
            # (Insert handle_help HTML here)
            pass

    async def start(self):
        await self.client.login(PASSWORD)
        self.client.add_event_callback(self.message_callback, RoomMessageText)
        asyncio.create_task(self.background_loop())
        await self.client.sync_forever(30000)

if __name__ == "__main__":
    asyncio.run(MatrixRaidBot().start())