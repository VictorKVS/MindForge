# Integration tests for agents
# tests/integration/test_agents.py
from fastapi.testclient import TestClient
from mf_core.api.app import app

client = TestClient(app)

# СЃРїРёСЃРѕРє Р°РіРµРЅС‚РѕРІ, РєРѕС‚РѕСЂС‹Рµ РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ РІ OpenAPI
EXPECTED_AGENTS = [
    "osint",
    "assets",
    "info",
    "law",
]

def test_openapi_contains_agents():
    """РџСЂРѕРІРµСЂСЏРµРј, С‡С‚Рѕ РІСЃРµ СЂРѕСѓС‚РµСЂС‹ Р°РіРµРЅС‚РѕРІ РµСЃС‚СЊ РІ OpenAPI СЃС…РµРјРµ"""
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
    assert not missing, f"РћС‚СЃСѓС‚СЃС‚РІСѓСЋС‚ СЂРѕСѓС‚РµСЂС‹ Р°РіРµРЅС‚РѕРІ: {missing}"



