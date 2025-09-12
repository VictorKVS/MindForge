from fastapi import APIRouter
from pydantic import BaseModel

# 1. Название: Summary API
# 2. Путь: mf_core/api/v1/summary.py
# 3. Описание: Генерация краткого содержания текста

router = APIRouter()

class SummaryRequest(BaseModel):
    text: str

@router.post("/summary")
async def generate_summary(request: SummaryRequest):
    return {"summary": f"Краткое содержание: {request.text[:50]}..."}