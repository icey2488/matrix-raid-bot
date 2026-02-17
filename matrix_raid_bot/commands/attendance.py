from matrix_raid_bot.database.sqlite import Database
from matrix_raid_bot.services.wcl import WCLService


class AttendanceCommand:
    def __init__(self, db: Database, wcl: WCLService) -> None:
        self.db = db
        self.wcl = wcl

    async def summarize_attendance(self, report_id: str) -> dict:
        report = await self.wcl.get_report(report_id)
        # Future: correlate report data with signups
        return report