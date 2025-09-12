indForge v0.5 — только папки
MindForge/
├── deploy/                      # 🚀 Деплой и инфраструктура
│   ├── docker/                  # Docker-окружение
│   └── k8s/                     # Kubernetes-манифесты
│
├── docs/                        # 📖 Документация
│   └── adr/                     # Архитектурные решения (ADR)
│
├── installer/                   # 🛠 Скрипты установки структуры
│
├── mf_core/                     # 🧠 Основной Python-пакет
│   ├── __main__.py              # CLI: запуск как `python -m mf_core`
│   │
│   ├── agents/                  # 🤖 Агенты (все собраны здесь)
│   │   ├── assets_audit/            # 💼 IT-активы и материальные ценности
│   │   ├── governance/              # ⚖️ Нормативка и документы
│   │   ├── info_security/           # 🔐 Информационная безопасность
│   │   │     ├──   response_agent.py      # связка кейсов с инцидентами
│   │   │     ├──   risks_agent.py         # учёт каналов утечек в матрице
│   │   ├── osint/                   # 🔍 Внешняя разведка
│   │   │     ├── osint_agent.py         # сбор/обогащение/скоры
│   │   │     ├──       enricher_xxx.py        # WHOIS, DNS, leaks, paste, соцсети
│   │   │     ├──     exporters.py           # выгрузка отчётов/артефактов
│   │   │     ├──      ioc_feed.py            # агрегатор индикаторов
│   │   │  
│   │   └── physical_security/       # 🛡️ Физическая охрана
│   │
│   ├── api/                     # 🌐 REST API (FastAPI)
│   │   ├── audit/               # API для выгрузок и проверок (ФСТЭК/ФСБ/РКН)
│   │   ├──dashboard/            # API для веб-дашборда (статусы, графики)
│   │   ├── v1/                   # /osint/observations, /cases, /reports 
│   │   └──  v1/                   # обмен с 1С (карточки, статусы)
│   │
│   ├── common/                  # 🔧 Общие модули
│   ├── db/                      # 💾 Работа с базой данных
│   │   └── migrations/          # Миграции (Alembic)
│   ├── embeddings/              # 🔤 Эмбеддинги
│   │   └── providers/           # Провайдеры эмбеддингов
│   ├── graph_eval/              # 📊 Анализ графа (документы ↔ процессы ↔ риски)
│   ├── llm/                     # 🤖 LLM-ядро
│   │   └── providers/           # Провайдеры LLM
│   ├── rag/                     # 🔍 Retrieval-Augmented Generation
│   ├── telemetry/               # 📈 Логирование и метрики
│   ├── vector_store/            # 🧠 Векторные БД (FAISS/Qdrant)
│   └── workers/                 # ⚙️ Фоновые задачи (Celery)
│
├── project_notes/               # 📒 Рабочие заметки
│   ├── research/                # Исследования
│   └── decisions/               # Принятые решения
│
├── scripts/                     # 🛠 Скрипты (инициализация, миграции)
│
└── tests/                       # 🧪 Тесты
    ├── unit/                    # Модульные
    └── integration/             # Интеграционные