# mf_core/api/v1/law.py
# Р­РЅРґРїРѕРёРЅС‚ РґР»СЏ РЅРѕСЂРјР°С‚РёРІРєРё/Р·Р°РєРѕРЅРѕРІ (Р·Р°РіР»СѓС€РєР°)
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/law", tags=["law"])

@router.get("/ping")
def ping():
    return {"agent": "law"}