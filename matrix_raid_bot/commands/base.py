
from dataclasses import dataclass
from typing import Awaitable, Callable, Dict, Protocol
from matrix_raid_bot.client import ServiceContainer


@dataclass
class CommandContext:
    room_id: str
    sender: str
    body: str
    args: list[str]
    services: ServiceContainer


class CommandHandler(Protocol):
    def __call__(self, ctx: CommandContext) -> Awaitable[None]: ...


COMMANDS: Dict[str, CommandHandler] = {}


def command(name: str):
    def decorator(func: CommandHandler):
        COMMANDS[name] = func
        return func
    return decorator