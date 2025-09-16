#mf_core/api/v1/health.py

from fastapi import APIRouter

# 1. РќР°Р·РІР°РЅРёРµ: Health Check
# 2. РџСѓС‚СЊ: mf_core/api/v1/health.py
# 3. РћРїРёСЃР°РЅРёРµ: РџСЂРѕРІРµСЂРєР° СЃРѕСЃС‚РѕСЏРЅРёСЏ API

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/health", tags=["health"])

@router.get("")
def health_check():
    return {"status": "ok"}
