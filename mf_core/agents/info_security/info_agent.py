from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/info", tags=["info_security"])

@router.get("/ping")
def ping():
    return {"agent": "info_security", "status": "ok"}

@router.get("/search")
def search(query: str = Query(..., description="Поиск по угрозам/рискам")):
    return {
        "agent": "info_security",
        "query": query,
        "results": [
            {"threat": f"Threat related to {query}", "risk": "medium"},
            {"threat": f"Another threat for {query}", "risk": "high"}
        ]
    }