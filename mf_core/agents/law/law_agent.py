from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/law", tags=["law"])

@router.get("/ping")
def ping():
    return {"agent": "law", "status": "ok"}

@router.get("/search")
def search(query: str = Query(..., description="РџРѕРёСЃРє РїРѕ Р·Р°РєРѕРЅРѕРґР°С‚РµР»СЊСЃС‚РІСѓ")):
    return {
        "agent": "law",
        "query": query,
        "results": [
            {"doc": f"Р¤Р—-152 СЃС‚Р°С‚СЊСЏ Рѕ {query}", "status": "Р°РєС‚СѓР°Р»РµРЅ"},
            {"doc": f"РџСЂРёРєР°Р· Р¤РЎРўР­Рљ в„–17, РєР°СЃР°СЋС‰РёР№СЃСЏ {query}", "status": "РІ СЂР°Р·СЂР°Р±РѕС‚РєРµ"}
        ]
    }