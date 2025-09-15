# mf_core/api/v1/status.py
# 1. Название: status.py
# 2. Полный путь: mf_core/api/v1/status.py
# 3. Краткое описание: эндпоинт проверки статуса фоновых задач

from fastapi import APIRouter

router = APIRouter()

@router.get("/status/{task_id}")
async def get_status(task_id: str):
    """
    [WIP] Проверка состояния фоновой задачи по её ID.
    Пока возвращает заглушку.
    """
    return {"task_id": task_id, "status": "in progress"}