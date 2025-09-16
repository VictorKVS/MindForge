# mf_core/api/v1/files.py
from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter(prefix="/api/v1/files", tags=["files"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    content = await file.read()

    # СЃРѕС…СЂР°РЅСЏРµРј С„Р°Р№Р»
    with open(file_path, "wb") as f:
        f.write(content)

    # СЃРѕР·РґР°С‘Рј preview
    preview = None
    try:
        # РїСЂРѕР±СѓРµРј РїСЂРѕС‡РёС‚Р°С‚СЊ РєР°Рє С‚РµРєСЃС‚ UTF-8
        text = content.decode("utf-8")
        preview = text[:100]  # РїРµСЂРІС‹Рµ 100 СЃРёРјРІРѕР»РѕРІ
    except UnicodeDecodeError:
        # Р±РёРЅР°СЂРЅС‹Рµ С„Р°Р№Р»С‹ в†’ preview РЅРµ РґРµР»Р°РµРј
        preview = None

    return {
        "status": "uploaded",
        "filename": file.filename,
        "preview": preview,
    }