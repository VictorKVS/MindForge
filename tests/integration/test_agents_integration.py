# Integration tests for agents
# tests/integration/test_agents.py
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

# список агентов, которые должны быть в OpenAPI
EXPECTED_AGENTS = [
    "osint",
    "assets",
    "info",
    "law",
]

def test_openapi_contains_agents():
    """Проверяем, что все роутеры агентов есть в OpenAPI схеме"""
    resp = client.get("/openapi.json")
    assert resp.status_code == 200

    data = resp.json()
    paths = data.get("paths", {})

    found_agents = []
    for path in paths.keys():
        for agent in EXPECTED_AGENTS:
            if path.startswith(f"/api/v1/{agent}"):
                found_agents.append(agent)

    missing = set(EXPECTED_AGENTS) - set(found_agents)
    assert not missing, f"Отсутствуют роутеры агентов: {missing}"



