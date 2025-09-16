# 1. РќР°Р·РІР°РЅРёРµ: Summary API
# 2. РџСѓС‚СЊ: mf_core/api/v1/summary.py
# 3. РћРїРёСЃР°РЅРёРµ: Р“РµРЅРµСЂР°С†РёСЏ РєСЂР°С‚РєРѕРіРѕ СЃРѕРґРµСЂР¶Р°РЅРёСЏ С‚РµРєСЃС‚Р°
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/summary", tags=["summary"])

class SummaryRequest(BaseModel):
    text: str

# РЈС‚РёР»РёС‚Р° РґР»СЏ РіРµРЅРµСЂР°С†РёРё С‚РµРєСЃС‚Р°
async def generate_summary_text(text: str) -> str:
    return f"РљСЂР°С‚РєРѕРµ СЃРѕРґРµСЂР¶Р°РЅРёРµ: {text[:30]}..." if len(text) > 30 else f"РљСЂР°С‚РєРѕРµ СЃРѕРґРµСЂР¶Р°РЅРёРµ: {text}"

# Р РѕСѓС‚РµСЂ POST /api/v1/summary
@router.post("")
async def generate_summary(request: SummaryRequest) -> dict:
    summary = await generate_summary_text(request.text)
    return {"summary": summary}