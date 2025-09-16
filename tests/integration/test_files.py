# tests/integration/test_files.py

from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_files_upload_endpoint_exists():
    """РџСЂРѕРІРµСЂСЏРµРј, С‡С‚Рѕ /api/v1/files СЃРѕС…СЂР°РЅСЏРµС‚ С„Р°Р№Р»"""
    resp = client.post("/api/v1/files", files={"file": ("test.txt", b"hello")})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "saved"
    assert data["filename"] == "test.txt"