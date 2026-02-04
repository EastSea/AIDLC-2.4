import httpx
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from typing import Any, Optional, List

TIMEOUT = 0.8  # 800ms
RETRYABLE = (httpx.TimeoutException, httpx.ConnectError)


class TableOrderClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _headers(self, token: Optional[str] = None) -> dict:
        h = {"Content-Type": "application/json"}
        if token:
            h["Authorization"] = f"Bearer {token}"
        return h

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.1, max=1), retry=retry_if_exception_type(RETRYABLE))
    async def _get(self, path: str, token: Optional[str] = None, params: Optional[dict] = None) -> Any:
        async with httpx.AsyncClient(timeout=TIMEOUT) as c:
            r = await c.get(f"{self.base_url}{path}", headers=self._headers(token), params=params)
            r.raise_for_status()
            return r.json()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.1, max=1), retry=retry_if_exception_type(RETRYABLE))
    async def _post(self, path: str, data: dict, token: Optional[str] = None) -> Any:
        async with httpx.AsyncClient(timeout=TIMEOUT) as c:
            r = await c.post(f"{self.base_url}{path}", headers=self._headers(token), json=data)
            r.raise_for_status()
            return r.json()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.1, max=1), retry=retry_if_exception_type(RETRYABLE))
    async def _patch(self, path: str, data: dict, token: Optional[str] = None) -> Any:
        async with httpx.AsyncClient(timeout=TIMEOUT) as c:
            r = await c.patch(f"{self.base_url}{path}", headers=self._headers(token), json=data)
            r.raise_for_status()
            return r.json()

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.1, max=1), retry=retry_if_exception_type(RETRYABLE))
    async def _delete(self, path: str, token: Optional[str] = None) -> Any:
        async with httpx.AsyncClient(timeout=TIMEOUT) as c:
            r = await c.delete(f"{self.base_url}{path}", headers=self._headers(token))
            r.raise_for_status()
            return r.json()

    # Customer APIs
    async def login(self, store_code: str, table_number: int, password: str) -> dict:
        return await self._post("/customer/auth/login", {"store_code": store_code, "table_number": table_number, "password": password})

    async def get_categories(self, token: str) -> List[dict]:
        return await self._get("/customer/categories", token)

    async def get_menus(self, token: str, category_id: Optional[str] = None) -> List[dict]:
        params = {"category_id": category_id} if category_id else None
        return await self._get("/customer/menus", token, params)

    async def get_cart(self, token: str, session_id: str) -> dict:
        return await self._get("/customer/cart", token, {"session_id": session_id})

    async def add_to_cart(self, token: str, session_id: str, menu_id: str, quantity: int, options: Optional[str] = None) -> dict:
        data = {"session_id": session_id, "menu_id": menu_id, "quantity": quantity}
        if options:
            data["options"] = options
        return await self._post("/customer/cart", data, token)

    async def create_order(self, token: str, session_id: str, items: List[dict]) -> dict:
        return await self._post("/customer/orders", {"session_id": session_id, "items": items}, token)

    async def get_orders(self, token: str, session_id: str) -> List[dict]:
        return await self._get("/customer/orders", token, {"session_id": session_id})

    async def call_staff(self, token: str, table_id: str) -> dict:
        return await self._post("/customer/staff-call", {"table_id": table_id}, token)

    # Admin APIs
    async def admin_login(self, store_code: str, username: str, password: str) -> dict:
        return await self._post("/admin/auth/login", {"store_code": store_code, "username": username, "password": password})

    async def get_all_orders(self, token: str, table_id: Optional[str] = None) -> List[dict]:
        params = {"table_id": table_id} if table_id else None
        return await self._get("/admin/orders", token, params)

    async def update_order_status(self, token: str, order_id: str, status: str) -> dict:
        return await self._patch(f"/admin/orders/{order_id}/status", {"status": status}, token)

    async def complete_table(self, token: str, table_id: str) -> dict:
        return await self._post(f"/admin/tables/{table_id}/complete", {}, token)

    async def get_menus_admin(self, token: str) -> List[dict]:
        return await self._get("/admin/menus", token)

    async def update_menu(self, token: str, menu_id: str, data: dict) -> dict:
        return await self._patch(f"/admin/menus/{menu_id}", data, token)
