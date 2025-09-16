# mf_core/api/v1/files/router.py

from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter(prefix="/api/v1/files", tags=["files"])
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    # сохраняем файл
    with open(file_path, "wb") as f:
        f.write(await file.read())

    content_preview = None
    # если это текстовый файл — пытаемся декодировать
    if file.content_type.startswith("text") or file.filename.endswith(".txt"):
        try:
            content_preview = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content_preview = file_path.read_text(encoding="cp1251")
            except Exception:
                content_preview = None

    return {
        "status": "uploaded",
        "filename": file.filename,
        "preview": content_preview[:100] if content_preview else None,
    }
