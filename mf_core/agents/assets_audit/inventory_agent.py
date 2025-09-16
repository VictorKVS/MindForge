# Assets Inventory Agent
# mf_core/agents/assets_audit/inventory_agent.py
# рџ’ј Р—Р°РіР»СѓС€РєР° РґР»СЏ РёРЅРІРµРЅС‚Р°СЂРёР·Р°С†РёРё

from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/assets", tags=["assets"])

@router.get("/ping")
def ping():
    return {"agent": "assets_audit", "status": "ok"}

@router.get("/search")
def search(query: str = Query(..., description="РџРѕРёСЃРє РїРѕ Р°РєС‚РёРІР°Рј")):
    return {
        "agent": "assets_audit",
        "query": query,
        "results": [
            {"item": "Laptop Dell", "status": "found"},
            {"item": "Server HP", "status": "not found"}
        ]
    }