"""MCP Core - Shared service module for Table Order MCP Servers"""
import httpx
from typing import Optional

class TableOrderClient:
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url
        self.token: Optional[str] = None

    def set_token(self, token: str):
        self.token = token

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    async def get(self, path: str, params: dict = None):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.base_url}{path}", params=params, headers=self._headers())
            resp.raise_for_status()
            return resp.json()

    async def post(self, path: str, data: dict = None):
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"{self.base_url}{path}", json=data, headers=self._headers())
            resp.raise_for_status()
            return resp.json()

    async def patch(self, path: str, data: dict = None):
        async with httpx.AsyncClient() as client:
            resp = await client.patch(f"{self.base_url}{path}", json=data, headers=self._headers())
            resp.raise_for_status()
            return resp.json()

    async def delete(self, path: str):
        async with httpx.AsyncClient() as client:
            resp = await client.delete(f"{self.base_url}{path}", headers=self._headers())
            resp.raise_for_status()
            return resp.json()
