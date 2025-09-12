# config.py 
# mf_core/common/config.py (очень простой для PoC)

# [WIP] config (в разработке)
import os

APP_NAME = os.getenv("APP_NAME", "mindforge-core")
ENV = os.getenv("ENV", "dev")