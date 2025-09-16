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

    # сохраняем файл
    with open(file_path, "wb") as f:
        f.write(content)

    # создаём preview
    preview = None
    try:
        # пробуем прочитать как текст UTF-8
        text = content.decode("utf-8")
        preview = text[:100]  # первые 100 символов
    except UnicodeDecodeError:
        # бинарные файлы → preview не делаем
        preview = None

    return {
        "status": "uploaded",
        "filename": file.filename,
        "preview": preview,
    }