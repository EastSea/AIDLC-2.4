from dataclasses import dataclass, asdict
from typing import Any, Optional


@dataclass
class ToolResponse:
    success: bool
    data: Optional[Any]
    error: Optional[str]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class CustomerContext:
    session_id: str
    store_code: str
    table_number: int
    token: str
    table_id: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class AdminContext:
    session_id: str
    username: str
    token: str
    store_id: int

    def to_dict(self) -> dict:
        return asdict(self)
