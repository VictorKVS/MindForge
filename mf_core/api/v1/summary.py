# 1. Название: Summary API
# 2. Путь: mf_core/api/v1/summary.py
# 3. Описание: Генерация краткого содержания текста
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/summary", tags=["summary"])

class SummaryRequest(BaseModel):
    text: str

# Утилита для генерации текста
async def generate_summary_text(text: str) -> str:
    return f"Краткое содержание: {text[:30]}..." if len(text) > 30 else f"Краткое содержание: {text}"

# Роутер POST /api/v1/summary
@router.post("")
async def generate_summary(request: SummaryRequest) -> dict:
    summary = await generate_summary_text(request.text)
    return {"summary": summary}