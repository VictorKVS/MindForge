# tests/unit/test_health_unit.py
# ✅ Юнит-тест эндпоинта health_check (без клиента)

from mf_core.api.v1.health import health_check

def test_health_unit():
    result = health_check()
    assert result == {"status": "ok"}