# tests/integration/test_summary.py
# [WIP] integration test for /api/v1/summary
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_summary_endpoint_exists():
    """Проверяем доступность /api/v1/summary"""
    resp = client.post("/api/v1/summary", json={"text": "MindForge тест"})
    assert resp.status_code in [200, 400]