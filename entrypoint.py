from matrix_raid_bot.database.sqlite import Database
from matrix_raid_bot.services.wcl import WCLService
from matrix_raid_bot.services.wowaudit import WoWAuditService
from matrix_raid_bot.services.scheduler import SchedulerService

from matrix_raid_bot.commands.signup import SignupCommand
from matrix_raid_bot.commands.roster import RosterCommand
from matrix_raid_bot.commands.attendance import AttendanceCommand

import os


def main() -> None:
    db = Database("data/raidbot.sqlite")
    wcl = WCLService(api_key=os.getenv("WCL_API_KEY", ""))
    audit = WoWAuditService(api_key=os.getenv("WOWAUDIT_API_KEY", ""))
    scheduler = SchedulerService()

    signup_cmd = SignupCommand(db=db, audit=audit)
    roster_cmd = RosterCommand(audit=audit)
    attendance_cmd = AttendanceCommand(db=db, wcl=wcl)

    # Future: pass these into bot/client for Matrix event handling
    print("Bot initialized with modular services and commands.")


if __name__ == "__main__":
    main()