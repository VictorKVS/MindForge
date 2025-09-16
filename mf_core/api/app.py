# mf_core/api/app.py
from fastapi import FastAPI
from importlib import import_module
import pkgutil

app = FastAPI(title="MindForge API")

# Автоподключение роутеров из mf_core/api/v1
package = "mf_core.api.v1"
for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
    module = import_module(f"{package}.{module_name}")
    if hasattr(module, "router"):
        app.include_router(module.router)