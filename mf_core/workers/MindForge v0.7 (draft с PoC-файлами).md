MindForge/
├── deploy/                      # 🚀 Деплой и инфраструктура
│   ├── docker/
│   │   ├── Dockerfile.api        📌 (в разработке)
│   │   ├── Dockerfile.worker     📌 (в разработке)
│   │   └── docker-compose.yaml   📌 (в разработке, PoC: API+Postgres+Redis)
│   └── k8s/
│       ├── api-deployment.yaml   📌 (в разработке)
│       ├── worker-deployment.yaml📌 (в разработке)
│       ├── redis-deployment.yaml 📌 (в разработке)
│       └── qdrant-deployment.yaml📌 (в разработке)
│
├── docs/
│   └── adr/
│       └── ADR-0001-structure.md 📌 (в разработке, описание v0.6)
│
├── installer/
│   └── mindforge_installer.py    📌 (готово, scaffold создаёт папки)
│
├── mf_core/
│   ├── __main__.py               📌 (в разработке, CLI `python -m mf_core`)
│   │
│   │
│   │
│   ├── assets_audit/           # 💼 Активы (заглушка)
│   │   ├── agents/                     # 🧩 Каркас агентов
│   │   │     ├── assets_audit/           # 💼 Активы 
│   │   │         ├──  __init__.py
│   │   │         └──inventory_agent.py
│   │   ├── governance/             # ⚖️ Нормативка (заглушка)
│   │        └── __init__.py
│   ├── info_security/          # 🔐 Инф. безопасность (заглушка)
│   │   └── __init__.py
│   ├── osint/                  # 🔍 OSINT
│   │   ├── __init__.py
│   │   └── osint_agent.py      # [PoC] hello OSINT
│   ├── physical_security/      # 🛡️ Физическая охрана (заглушка)
│   │   └── __init__.py
│   │
│   ├── cyberai/                # ⚡ CyberAI каркас
│   │   ├── __init__.py
│   │   ├── dev_agent.py        # CyberAI Dev – кодинг, API, логика
│   │   ├── ai_lab_agent.py     # CyberAI AI-Lab – ИИ атак/защиты
│   │   ├── ops_agent.py        # CyberAI Ops – CI/CD, DevOps
│   │   ├── game_agent.py       # CyberAI Game – сценарии, механики
│   │   ├── world_agent.py      # CyberAI World – графика, 3D
│   │   ├── npc_agent.py        # CyberAI NPC – персонажи
│   │   ├── blue_agent.py       # CyberAI Blue – защита, hunting
│   │   ├── logs_agent.py       # CyberAI Logs – анализ атак
│   │   ├── story_agent.py      # CyberAI Story – база знаний
│   │   ├── economy_agent.py    # CyberAI Economy – баланс, ресурсы
│   │   ├── test_agent.py       # CyberAI Test – тестирование
│   │   └── voice_agent.py      # CyberAI Voice – озвучка
│   │
│   ├── law/                    # ⚖️ Юридическая безопасность
│   │       ├── __init__.py
│   │       ├── health.py         📌 (готово, /health)
│   │       ├── health.py         📌 (готово, /health)
│   │       └── compliance_agent.py # Работа с регуляторами, НПА, юр. рис  ( существует)
│   ├── api/
│   │   ├── app.py                📌 (в разработке, FastAPI PoC)
│   │   └── v1/
│   │       ├──   assets.py                                              ( существует)
│   │       ├── health.py         📌 (готово, /health)
[text](../api/v1/law.py)
│   │       ├── files.py          📌 (в разработке, /files, заглушка)
│   │       ├── search.py         📌 (в разработке, /search, заглушка)
│   │       ├── status.py         📌 (в разработке, /status/{id}, заглушка)
│   │       └── summary.py        📌 (в разработке, /summary, заглушка)
│   │
│   ├── common/
│   │   ├── config.py             📌 (в разработке, pydantic.BaseSettings)
│   │   ├── paths.py              📌 (готово, PROJECT_ROOT)
│   │   └── schemas.py            📌 (в разработке, pydantic модели для API)
│   │
│   ├── db/
│   │   ├── models.py             📌 (в разработке, SQLAlchemy Base)
│   │   ├── storage.py            📌 (в разработке, session_local)
│   │   └── migrations/           📌 (директория Alembic, пока пусто)
│   │
│   ├── embeddings/
│   │   ├── base.py               📌 (заглушка)
│   │   └── providers/
│   │       ├── openai.py         📌 (в разработке, заглушка)
│   │       └── local.py          📌 (в разработке, заглушка)
│   │
│   ├── graph_eval/
│   │   └── __init__.py           📌 (пока пусто)
│   │
│   ├── llm/
│   │   ├── base.py               📌 (заглушка)
│   │   └── router.py             📌 (в разработке, PoC роутер)
│   │
│   ├── rag/
│   │   └── __init__.py           📌 (пока пусто)
│   │
│   ├── telemetry/
│   │   └── logging.py            📌 (в разработке, логгер JSON)
│   │
│   ├── vector_store/
│   │   └── base.py               📌 (в разработке, заглушка FAISS)
│   │
│   └── workers/
│       └── celery_app.py         📌 (в разработке, базовая конфигурация Celery)
│
├── project_notes/
│   ├── research/                 📌 (директория для заметок)
│   └── decisions/                📌 (директория для решений)
│
├── scripts/
│   └── prestart.sh               📌 (в разработке, Docker-entrypoint)
│
├── tests/
│   ├── unit/                     📌 (директория для тестов)
│   ├── docker/
│   └── integration/
│      ├── docker/
│            └── test_health.py        📌 (в разработке, тест /health)
│
├── .gitattributes (существует)
├── .gitignore     (существует)
├── NUL            (существует)
├── pyproject.toml (существует)
└── README.md      (существует)