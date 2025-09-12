#mf_core/api/v1/health.py

from fastapi import APIRouter

# 1. Название: Health Check
# 2. Путь: mf_core/api/v1/health.py
# 3. Описание: Проверка состояния API

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}