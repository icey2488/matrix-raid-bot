from matrix_raid_bot.services.wowaudit import WoWAuditService


class RosterCommand:
    def __init__(self, audit: WoWAuditService) -> None:
        self.audit = audit

    async def fetch_roster(self, guild_id: str) -> dict:
        return await self.audit.get_roster(guild_id)