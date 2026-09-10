"""HTTP client for Diligent ESG (HighBond / Diligent One) API."""
from __future__ import annotations
import httpx
from typing import Any, Optional

DEFAULT_BASE = "https://apis.highbond.com/v1"

class DiligentESGClient:
    def __init__(self, api_key: str, base_url: str = ""):
        self.api_key = api_key.strip()
        self.base_url = (base_url.strip() if base_url else DEFAULT_BASE).rstrip("/")
        
        # Diligent HighBond HighBond-API uses Bearer token
        auth_val = f"Bearer {self.api_key}" if not self.api_key.startswith("Bearer ") else self.api_key
        self.headers = {
            "Authorization": auth_val,
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
            "User-Agent": "Imperal-DiligentESG-Connector/1.0.0"
        }
        self.timeout = httpx.Timeout(30.0, connect=10.0)

    async def verify_auth(self) -> dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                # HighBond API scopes under orgs/{org_id}/projects or global user endpoint
                resp = await client.get(f"{self.base_url}/orgs/0/projects", headers=self.headers)
                if resp.status_code in (200, 201, 204):
                    return {"status": "ok", "data": resp.json() if resp.content else {}}
                return {"status": "error", "error": f"HTTP {resp.status_code}: {resp.text}"}
            except Exception as e:
                return {"status": "error", "error": str(e)}

    async def list_emissions(self, limit: int = 20) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(f"{self.base_url}/orgs/0/projects", headers=self.headers, params={"page[size]": limit})
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, list): return data
                for k in ["data", "emissions", "items", "results"]:
                    if k in data and isinstance(data[k], list): return data[k]
                return []
            return []

    async def get_emissionrecord(self, emissionrecord_id: str) -> dict[str, Any]:
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(f"{self.base_url}/orgs/0/projects/{emissionrecord_id}", headers=self.headers)
            if resp.status_code == 200:
                return resp.json()
            raise ValueError(f"HTTP {resp.status_code}: {resp.text}")
