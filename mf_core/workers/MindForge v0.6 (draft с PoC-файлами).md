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
│   ├── agents/
│   │   ├── assets_audit/         # 💼 Активы
│   │   │   └── __init__.py       📌 (заглушка)
│   │   ├── governance/           # ⚖️ Нормативка
│   │   │   └── __init__.py       📌 (заглушка)
│   │   ├── info_security/        # 🔐 ИБ
│   │   │   └── __init__.py       📌 (заглушка)
│   │   ├── osint/
│   │   │   ├── __init__.py       📌 (заглушка)
│   │   │   └── osint_agent.py    📌 (в разработке, PoC: заглушка «hello OSINT»)
│   │   └── physical_security/
│   │       └── __init__.py       📌 (заглушка)
│   │
│   ├── api/
│   │   ├── app.py                📌 (в разработке, FastAPI PoC)
│   │   └── v1/
│   │       ├── health.py         📌 (готово, /health)
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
└── tests/
    ├── unit/                     📌 (директория для тестов)
    └── integration/
        └── test_health.py        📌 (в разработке, тест /health)
