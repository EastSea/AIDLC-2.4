import json
from typing import Any, Optional

SESSION_TTL = 3600  # 1 hour
KEY_PREFIX = "mcp:"


class SessionManager:
    def __init__(self, redis):
        self.redis = redis

    def _key(self, session_id: str) -> str:
        return f"{KEY_PREFIX}{session_id}"

    async def save_context(self, session_id: str, context: dict) -> None:
        await self.redis.setex(self._key(session_id), SESSION_TTL, json.dumps(context))

    async def get_context(self, session_id: str) -> Optional[dict]:
        data = await self.redis.get(self._key(session_id))
        if data is None:
            return None
        return json.loads(data)

    async def delete_context(self, session_id: str) -> None:
        await self.redis.delete(self._key(session_id))

    async def is_valid(self, session_id: str) -> bool:
        return await self.redis.exists(self._key(session_id)) > 0
