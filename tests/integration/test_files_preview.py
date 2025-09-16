#tests/integration/test_files_preview.py
from pathlib import Path
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)


def test_text_file_preview(tmp_path):
    # создаём временный .txt файл
    test_file = tmp_path / "test_preview.txt"
    test_file.write_text("ИБ тестовый файл для preview")

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_preview.txt", f, "text/plain")},
        )

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "uploaded"
    assert data["filename"] == "test_preview.txt"
    assert "ИБ тестовый файл" in data["preview"]  # проверяем preview


def test_binary_file_no_preview(tmp_path):
    # создаём временный бинарный .jpg файл
    test_file = tmp_path / "test_image.jpg"
    test_file.write_bytes(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")  # минимальный JPEG-заголовок

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_image.jpg", f, "image/jpeg")},
        )

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "uploaded"
    assert data["filename"] == "test_image.jpg"
    assert data["preview"] is None  # у бинарных файлов preview не должно быть