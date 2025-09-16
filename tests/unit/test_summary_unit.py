# tests/unit/test_summary_unit.py
# вњ… Р®РЅРёС‚-С‚РµСЃС‚ Р»РѕРіРёРєРё РіРµРЅРµСЂР°С†РёРё summary

from mf_core.api.v1.summary import generate_summary, SummaryRequest
import asyncio

def test_summary_unit():
    request = SummaryRequest(text="MindForge unit test for summary endpoint")
    result = asyncio.run(generate_summary(request))
    assert "РљСЂР°С‚РєРѕРµ СЃРѕРґРµСЂР¶Р°РЅРёРµ" in result["summary"]
    assert "MindForge" in result["summary"]