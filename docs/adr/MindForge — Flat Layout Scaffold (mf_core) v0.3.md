MindForge/
├── deploy/                      # 🚀 Деплой и инфраструктура
│   ├── docker/                  # Docker-окружение
│   │   ├── Dockerfile.api       # Образ для FastAPI-сервиса
│   │   ├── Dockerfile.worker    # Образ для Celery-воркера
│   │   └── docker-compose.yaml  # Локальная сборка (API, воркеры, БД, Redis, Qdrant)
│   └── k8s/                     # Манифесты Kubernetes
│       ├── api-deployment.yaml
│       ├── worker-deployment.yaml
│       ├── redis-deployment.yaml   # 📌 Брокер сообщений для Celery (Redis/RabbitMQ)
│       └── qdrant-deployment.yaml  # 📌 Деплой векторного хранилища Qdrant
│
├── docs/                        # 📖 Документация
│   ├── architecture.md          # Описание архитектуры
│   └── adr/                     # Архитектурные решения (ADR)
│       └── ADR-0001-structure.md
│
├── installer/
│   └── mindforge_installer.py   # 🛠 Скрипт создания структуры проекта
│
├── mf_core/                     # 🧠 Основной Python-пакет
│   ├── __main__.py              # CLI: запуск как `python -m mf_core`
│   │
│   ├── agents/                  # 🤖 Агенты-специалисты
│   │   ├── osint/               # Сбор информации (OSINT)
│   │   ├── project_analyzer/    # Анализ проектов и регламентов
│   │   └── training/            # Модуль обучения и симуляций
│   │
│   ├── api/                     # 🌐 REST API (FastAPI)
│   │   ├── app.py               # Основное приложение FastAPI
│   │   └── v1/                  # Версия API
│   │       ├── health.py        # /health — проверка состояния
│   │       ├── files.py         # /files — загрузка и обработка файлов
│   │       ├── search.py        # /search — семантический поиск
│   │       ├── summary.py       # /summary — генерация аннотаций
│   │       └── status.py        # /status/{task_id} — проверка фоновых задач
│   │
│   ├── common/                  # 🔧 Общие модули
│   │   ├── paths.py             # Пути проекта (PROJECT_ROOT и др.)
│   │   ├── config.py            # Настройки (pydantic)
│   │   └── schemas.py           # Pydantic-модели API
│   │
│   ├── db/                      # 💾 Работа с базой данных
│   │   ├── models.py            # ORM-модели (SQLAlchemy)
│   │   ├── storage.py           # Подключение к БД
│   │   └── migrations/          # Миграции (Alembic)
│   │
│   ├── embeddings/              # 🔤 Векторизация текста
│   │   ├── base.py
│   │   └── providers/           # Провайдеры эмбеддингов
│   │       ├── openai.py
│   │       └── local.py
│   │
│   ├── graph_eval/              # 📊 Метрики и анализ графа
│   │   ├── metrics.py           # Centrality, PageRank, Modularity
│   │   ├── clustering.py        # Кластеризация узлов
│   │   ├── visualization.py     # Экспорт в GraphML/GEXF, визуализация
│   │   └── evaluator.py         # Precision, Recall, nDCG
│   │
│   ├── llm/                     # 🤖 Работа с LLM
│   │   ├── base.py              # Базовый интерфейс
│   │   ├── router.py            # Роутер LLM-провайдеров
│   │   └── providers/           # Конкретные провайдеры (OpenAI, GigaChat, локальные)
│   │
│   ├── rag/                     # 🔍 Retrieval-Augmented Generation
│   │   ├── retriever.py         # Поиск по базе
│   │   ├── semantic.py          # Семантический поиск
│   │   ├── ner.py               # Извлечение сущностей
│   │   └── graph.py             # Построение графа знаний
│   │
│   ├── telemetry/               # 📈 Логирование и метрики
│   │   ├── logging.py           # Логирование (JSON)
│   │   └── metrics.py           # Метрики Prometheus
│   │
│   ├── vector_store/            # 🧠 Векторные БД
│   │   ├── base.py
│   │   ├── qdrant_store.py
│   │   └── faiss_store.py
│   │
│   └── workers/                 # ⚙️ Асинхронные фоновые задачи
│       ├── celery_app.py        # Настройка Celery
│       └── tasks.py             # Задачи для Celery
│
├── project_notes/               # 📒 Рабочие заметки
│   ├── roadmap.md               # Дорожная карта
│   ├── design_notes.md          # Проектные заметки
│   ├── research/                # Материалы исследований
│   └── decisions/               # Принятые решения
│
├── scripts/                     # 🛠 Полезные скрипты
│   └── prestart.sh              # Инициализация перед запуском (в Docker)
│
├── tests/                       # 🧪 Тесты
│   ├── unit/                    # Модульные тесты
│   ├── integration/             # Интеграционные тесты
│   └── test_health.py           # Проверка эндпоинта /health
│
├── .pre-commit-config.yaml      # Автоматические проверки кода (black, isort, ruff, mypy)
├── .env.example                 # Шаблон переменных окружения
├── .gitignore                   # Исключения Git
├── Makefile                     # Утилиты: сборка, тесты, линтеры
├── pyproject.toml               # Настройки пакета и зависимостей (src-layout)
└── README.md                    # Документация проекта
