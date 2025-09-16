#tests/integration/test_files_preview.py
from pathlib import Path
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)


def test_text_file_preview(tmp_path):
    # СЃРѕР·РґР°С‘Рј РІСЂРµРјРµРЅРЅС‹Р№ .txt С„Р°Р№Р»
    test_file = tmp_path / "test_preview.txt"
    test_file.write_text("РР‘ С‚РµСЃС‚РѕРІС‹Р№ С„Р°Р№Р» РґР»СЏ preview")

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_preview.txt", f, "text/plain")},
        )

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "uploaded"
    assert data["filename"] == "test_preview.txt"
    assert "РР‘ С‚РµСЃС‚РѕРІС‹Р№ С„Р°Р№Р»" in data["preview"]  # РїСЂРѕРІРµСЂСЏРµРј preview


def test_binary_file_no_preview(tmp_path):
    # СЃРѕР·РґР°С‘Рј РІСЂРµРјРµРЅРЅС‹Р№ Р±РёРЅР°СЂРЅС‹Р№ .jpg С„Р°Р№Р»
    test_file = tmp_path / "test_image.jpg"
    test_file.write_bytes(b"\xFF\xD8\xFF\xE0\x00\x10JFIF")  # РјРёРЅРёРјР°Р»СЊРЅС‹Р№ JPEG-Р·Р°РіРѕР»РѕРІРѕРє

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_image.jpg", f, "image/jpeg")},
        )

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "uploaded"
    assert data["filename"] == "test_image.jpg"
    assert data["preview"] is None  # Сѓ Р±РёРЅР°СЂРЅС‹С… С„Р°Р№Р»РѕРІ preview РЅРµ РґРѕР»Р¶РЅРѕ Р±С‹С‚СЊ