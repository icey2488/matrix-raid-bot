import aiohttp
from typing import Optional


class WCLService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://www.warcraftlogs.com/v1"

    async def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        url = f"{self.base_url}/{endpoint}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def get_report(self, report_id: str) -> dict:
        return await self._get(f"report/fights/{report_id}")

    async def get_character_logs(self, server: str, region: str, character: str) -> dict:
        return await self._get(
            f"character/{region}/{server}/{character}",
            params={"start": 0, "end": 9999999999},
        )