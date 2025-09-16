# __main__.py
# mf_core/__main__.py
# [WIP] CLI entrypoint (РІ СЂР°Р·СЂР°Р±РѕС‚РєРµ)
import uvicorn
# MindForge Core вЂ” CLI Entrypoint
# Path: mf_core/__main__.py
# рџљЂ Р—Р°РїСѓСЃРє FastAPI-РїСЂРёР»РѕР¶РµРЅРёСЏ С‡РµСЂРµР· Uvicorn (PoC v0.6, РІ СЂР°Р·СЂР°Р±РѕС‚РєРµ)

import uvicorn
from mf_core.api.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)