from matrix_raid_bot.database.sqlite import Database
from matrix_raid_bot.services.wowaudit import WoWAuditService
from matrix_raid_bot.util.formatting import format_signup_list


class SignupCommand:
    def __init__(self, db: Database, audit: WoWAuditService) -> None:
        self.db = db
        self.audit = audit

    async def handle_signup(self, raid_id: int, character_name: str, status: str) -> str:
        self.db.upsert_signup(raid_id, character_name, status)
        signups = self.db.get_signups(raid_id)
        return format_signup_list(signups)