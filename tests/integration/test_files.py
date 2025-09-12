# tests/integration/test_files.py
# [WIP] integration test for /api/v1/files
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_files_upload_endpoint_exists():
    """Проверяем, что эндпоинт /api/v1/files отвечает хотя бы 200/400."""
    resp = client.post("/api/v1/files", files={"file": ("test.txt", b"hello")})
    assert resp.status_code in [200, 400]  # зависит от текущей реализации