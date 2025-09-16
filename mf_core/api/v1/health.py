#mf_core/api/v1/health.py

from fastapi import APIRouter

# 1. Название: Health Check
# 2. Путь: mf_core/api/v1/health.py
# 3. Описание: Проверка состояния API

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/health", tags=["health"])

@router.get("")
def health_check():
    return {"status": "ok"}
