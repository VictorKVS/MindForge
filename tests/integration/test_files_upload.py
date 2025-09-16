# tests/integration/test_files_upload.py
# 1. РќР°Р·РІР°РЅРёРµ: РўРµСЃС‚ Р·Р°РіСЂСѓР·РєРё С„Р°Р№Р»Р°
# 2. РџСѓС‚СЊ: tests/integration/test_files_upload.py
# 3. РћРїРёСЃР°РЅРёРµ: РџСЂРѕРІРµСЂСЏРµС‚ Р·Р°РіСЂСѓР·РєСѓ С‚РµРєСЃС‚РѕРІРѕРіРѕ С„Р°Р№Р»Р° РІ /uploads/

from pathlib import Path
from mf_core.api.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_file_upload(tmp_path):
    # СЃРѕР·РґР°С‘Рј РІСЂРµРјРµРЅРЅС‹Р№ С„Р°Р№Р» РґР»СЏ С‚РµСЃС‚Р°
    test_file = tmp_path / "test_ib.txt"
    test_file.write_text("РР‘ С‚РµСЃС‚РѕРІС‹Р№ С„Р°Р№Р»", encoding="utf-8")

    with open(test_file, "rb") as f:
        response = client.post(
            "/api/v1/files/upload",
            files={"file": ("test_ib.txt", f, "text/plain")},
        )

    # РїСЂРѕРІРµСЂСЏРµРј РєРѕРґ РѕС‚РІРµС‚Р°
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "uploaded"
    assert data["filename"] == "test_ib.txt"

    # РїСЂРѕРІРµСЂСЏРµРј, С‡С‚Рѕ С„Р°Р№Р» РґРµР№СЃС‚РІРёС‚РµР»СЊРЅРѕ РїРѕСЏРІРёР»СЃСЏ РІ uploads/
    uploaded_path = Path("uploads") / "test_ib.txt"
    assert uploaded_path.exists()

    # С‡РёС‚Р°РµРј СЃ СѓС‡С‘С‚РѕРј РєРѕРґРёСЂРѕРІРѕРє
    try:
        content = uploaded_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = uploaded_path.read_text(encoding="cp1251")

    assert "РР‘ С‚РµСЃС‚РѕРІС‹Р№ С„Р°Р№Р»" in content