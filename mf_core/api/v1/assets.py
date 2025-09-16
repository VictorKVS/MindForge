# mf_core/api/v1/assets.py
#from fastapi import APIRouter

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/assets", tags=["assets"])

@router.get("/ping")
def ping():
    return {"agent": "assets_audit"}