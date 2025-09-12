# mf_core/api/app.py

from fastapi import FastAPI
from mf_core.api.v1 import health, files, summary

# 1. Название: MindForge API
# 2. Путь: mf_core/api/app.py
# 3. Описание: Основная точка входа FastAPI, подключает все роутеры

app = FastAPI(title="MindForge API")

# Подключаем все роутеры
app.include_router(health.router, prefix="/api/v1")
app.include_router(files.router, prefix="/api/v1")
app.include_router(summary.router, prefix="/api/v1")