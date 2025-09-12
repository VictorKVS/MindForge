# __main__.py
# mf_core/__main__.py
# [WIP] CLI entrypoint (в разработке)
import uvicorn
# MindForge Core — CLI Entrypoint
# Path: mf_core/__main__.py
# 🚀 Запуск FastAPI-приложения через Uvicorn (PoC v0.6, в разработке)

import uvicorn
from mf_core.api.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)