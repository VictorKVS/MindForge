# 1. РќР°Р·РІР°РЅРёРµ: Status API
# 2. РџСѓС‚СЊ: mf_core/api/v1/status.py
# 3. РћРїРёСЃР°РЅРёРµ: Р—Р°РіР»СѓС€РєР° РїСЂРѕРІРµСЂРєРё СЃС‚Р°С‚СѓСЃР° Р·Р°РґР°С‡Рё
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/status", tags=["status"])

@router.get("/{task_id}")
async def get_status(task_id: str):
    """
    Р—Р°РіР»СѓС€РєР° РїСЂРѕРІРµСЂРєРё СЃС‚Р°С‚СѓСЃР° РїРѕ task_id.
    """
    return {"task_id": task_id, "status": "in progress (stub)"}