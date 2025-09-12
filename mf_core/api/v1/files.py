#mf_core/api/v1/files.py

from fastapi import APIRouter, UploadFile, File

# 1. Название: File Upload API
# 2. Путь: mf_core/api/v1/files.py
# 3. Описание: Загрузка и обработка файлов

router = APIRouter()

@router.post("/files")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}