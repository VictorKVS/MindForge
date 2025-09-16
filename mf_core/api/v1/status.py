# 1. Название: Status API
# 2. Путь: mf_core/api/v1/status.py
# 3. Описание: Заглушка проверки статуса задачи
from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/status", tags=["status"])

@router.get("/{task_id}")
async def get_status(task_id: str):
    """
    Заглушка проверки статуса по task_id.
    """
    return {"task_id": task_id, "status": "in progress (stub)"}