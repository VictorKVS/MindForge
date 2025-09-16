# mf_core/api/v1/law.py
# Эндпоинт для нормативки/законов (заглушка)
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/law", tags=["law"])

@router.get("/ping")
def ping():
    return {"agent": "law"}