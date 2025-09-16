# tests/unit/test_health_unit.py
# вњ… Р®РЅРёС‚-С‚РµСЃС‚ СЌРЅРґРїРѕРёРЅС‚Р° health_check (Р±РµР· РєР»РёРµРЅС‚Р°)

from mf_core.api.v1.health import health_check

def test_health_unit():
    result = health_check()
    assert result == {"status": "ok"}