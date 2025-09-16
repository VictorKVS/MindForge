# tests/unit/test_agents.py
# [WIP] unit test for agents logic
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

def test_health_check():
    resp = client.get("/api/v1/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}