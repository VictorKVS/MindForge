# tests/integration/test_files_upload.py
# 1. Название: Тест загрузки файла
# 2. Путь: tests/integration/test_files_upload.py
# 3. Описание: Проверяет загрузку текстового файла в /uploads/

from pathlib import Path
from mf_core.api.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_file_upload(tmp_path):
    # создаём временный файл для теста
    test_file = tmp_path / "test_ib.txt"
    test_file.write_text("ИБ тестовый файл", encoding="utf-8")

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_ib.txt", f, "text/plain")},
        )

    # проверяем код ответа
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "uploaded"
    assert data["filename"] == "test_ib.txt"

    # проверяем, что файл действительно появился в uploads/
    uploaded_path = Path("uploads") / "test_ib.txt"
    assert uploaded_path.exists()

    # читаем с учётом кодировок
    try:
        content = uploaded_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = uploaded_path.read_text(encoding="cp1251")

    assert "ИБ тестовый файл" in content