# test_health.py
#tests/integration/test_health.py
# [WIP] integration test (в разработке)
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_health():
    r = client.get("/api/v1/health")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"