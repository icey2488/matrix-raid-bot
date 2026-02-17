import asyncio
from datetime import datetime, timedelta
from typing import Callable


class SchedulerService:
    def __init__(self) -> None:
        self._tasks = []

    def schedule(self, run_at: datetime, callback: Callable[[], None]) -> None:
        delay = (run_at - datetime.now()).total_seconds()
        task = asyncio.create_task(self._delayed_run(delay, callback))
        self._tasks.append(task)

    async def _delayed_run(self, delay: float, callback: Callable[[], None]) -> None:
        await asyncio.sleep(max(0, delay))
        callback()

    def cancel_all(self) -> None:
        for task in self._tasks:
            task.cancel()
        self._tasks.clear()