"""Extension declaration, capabilities, health check for Diligent ESG Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "diligent-esg-connector",
    version="0.1.0",
    display_name="Diligent ESG",
    icon="icon.svg",
    capabilities=["diligent_esg:manage"],
    description="Official Imperal connector for Diligent ESG (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("diligent_esg_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Diligent ESG connection(s) configured." if count else "Not connected yet."
    }
