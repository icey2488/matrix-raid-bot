import aiohttp
from typing import Optional


class WoWAuditService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://wowaudit.com/api"

    async def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.base_url}/{endpoint}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def get_roster(self, guild_id: str) -> dict:
        return await self._get(f"guilds/{guild_id}/roster")

    async def get_character(self, guild_id: str, character_name: str) -> dict:
        return await self._get(f"guilds/{guild_id}/characters/{character_name}")