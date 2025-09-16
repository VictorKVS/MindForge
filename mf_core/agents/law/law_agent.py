from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/law", tags=["law"])

@router.get("/ping")
def ping():
    return {"agent": "law", "status": "ok"}

@router.get("/search")
def search(query: str = Query(..., description="Поиск по законодательству")):
    return {
        "agent": "law",
        "query": query,
        "results": [
            {"doc": f"ФЗ-152 статья о {query}", "status": "актуален"},
            {"doc": f"Приказ ФСТЭК №17, касающийся {query}", "status": "в разработке"}
        ]
    }