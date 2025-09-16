# tests/integration/test_summary.py
# [WIP] integration test for /api/v1/summary
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_summary_endpoint_exists():
    """РџСЂРѕРІРµСЂСЏРµРј РґРѕСЃС‚СѓРїРЅРѕСЃС‚СЊ /api/v1/summary"""
    resp = client.post("/api/v1/summary", json={"text": "MindForge С‚РµСЃС‚"})
    assert resp.status_code in [200, 400]