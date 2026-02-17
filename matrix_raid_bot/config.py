from pydantic import BaseModel
import os


class Settings(BaseModel):
    matrix_homeserver: str = ""
    matrix_user: str = ""
    matrix_password: str = ""
    matrix_device_name: str = "matrix-raid-bot"

    wcl_api_key: str | None = None
    wowaudit_api_key: str | None = None
    wowaudit_guild_id: str | None = None

    database_path: str = "raidbot.db"
    log_level: str = "INFO"
    scheduler_interval_seconds: int = 60

    class Config:
        extra = "ignore"


def load_settings() -> Settings:
    return Settings(
        matrix_homeserver=os.getenv("MATRIX_HOMESERVER", ""),
        matrix_user=os.getenv("MATRIX_USER", ""),
        matrix_password=os.getenv("MATRIX_PASSWORD", ""),
        matrix_device_name=os.getenv("MATRIX_DEVICE_NAME", "matrix-raid-bot"),
        wcl_api_key=os.getenv("WCL_API_KEY"),
        wowaudit_api_key=os.getenv("WOWAUDIT_API_KEY"),
        wowaudit_guild_id=os.getenv("WOWAUDIT_GUILD_ID"),
        database_path=os.getenv("DATABASE_PATH", "raidbot.db"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        scheduler_interval_seconds=int(os.getenv("SCHEDULER_INTERVAL_SECONDS", "60")),
    )