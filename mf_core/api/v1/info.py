# mf_core/api/v1/info.py
# Р—Р°РіР»СѓС€РєР° СЌРЅРґРїРѕРёРЅС‚Р° /info
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/info", tags=["info"])

@router.get("/ping")
def ping():
    return {"agent": "info_security"}