from dataclasses import dataclass
from typing import Optional

from .database.sqlite import Database
from .services.wowaudit import WoWAuditClient
from .util.matrix_helpers import MatrixService


@dataclass
class ServiceContainer:
    matrix: MatrixService
    db: Database
    wowaudit: Optional[WoWAuditClient]
    default_room_id: str