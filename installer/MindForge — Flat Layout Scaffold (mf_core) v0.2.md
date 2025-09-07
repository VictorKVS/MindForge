MindForge/
├── mf_core/
│ ├── __init__.py
│ ├── __main__.py # CLI: python -m mf_core
│ ├── api/
│ │ ├── __init__.py
│ │ ├── app.py # FastAPI приложение
│ │ └── v1/
│ │       ├── __init__.py
│ │       ├── health.py # /health
│ │       ├── files.py # /files
│ │       ├── search.py # /search
│ │       ├── summary.py # /summary
│ │       └── status.py # /status/{task_id}
│ ├── agents/
│ │         ├── __init__.py
│ │         ├── osint/
│ │         │     ├── __init__.py
│ │         │     └── agent.py
│ │         ├── project_analyzer/
│ │         │   ├── __init__.py
│ │         │   └── analyzer.py
│ │         └── training/
│ │                    ├── __init__.py
│ │                    └── trainer.py
│ ├── rag/
│ │      ├── __init__.py
│ │      ├── retriever.py
│ │      ├── semantic.py
│ │      ├── ner.py
│ │      └── graph.py
│ ├── embeddings/
│ │      ├── __init__.py
│ │      ├── base.py
│ │      └── providers/
│ │                 ├── __init__.py
│ │                 ├── openai.py
│ │                 └── local.py
│ ├── vector_store/
│ │     ├── __init__.py
│ │     ├── base.py
│ │     ├── qdrant_store.py
│ │     └── faiss_store.py
│ ├── llm/
│ │     ├── __init__.py
│ │     ├── base.py
│ │     ├── router.py
│ │     └── providers/
│ │           ├── __init__.py
│ │           ├── openai.py
│ │           ├── gigachat.py
│ │           └── mistral_local.py
│ ├── workers/
│ │    ├── __init__.py
│ │    └── celery_app.py
│ ├── telemetry/
│ │          ├── __init__.py
│ │          ├── logging.py
│ │          └── metrics.py
│ └── common/
│          ├── __init__.py
│          ├── paths.py # PROJECT_ROOT / PROJECT_NOTES_DIR
│          ├── config.py # Settings (pydantic)
│          └── schemas.py # Pydantic модели для API
├── docs/
│      ├── README.md
│      ├── architecture.md
│      └── adr/ADR-0001-structure.md
├── project_notes/
│      ├── roadmap.md
│      ├── design_notes.md
│      ├── research/
│      └── decisions/
├── tests/
│      ├── __init__.py
│      └── test_health.py
├── deploy/
│     ├── docker/
│     │       ├── Dockerfile.api
│     │       ├── Dockerfile.worker
│     │       └── docker-compose.yaml
│     └── k8s/
├── .gitignore
├── .env.example
├── pyproject.toml
├── Makefile
└── README.md





Предложения и дополнения к структуре
Вот модифицированная и дополненная структура дерева с комментариями.

bash
mindforge/
├── src/ # [!] Предлагается использовать src-layout
│   └── mf_core/ # основной Python‑пакет
│       ├── api/
│       │   ├── dependencies.py # [!] Ново: FastAPI Depends (БД, сервисы)
│       │   ├── errors.py # [!] Ново: кастомные обработчики ошибок
│       │   ├── middleware.py # [!] Ново: кастомное middleware (CORS, логирование)
│       │   ├── app.py
│       │   └── v1/
│       │       ├── __init__.py # [!] Важно: не забываем про __init__.py
│       │       ├── health.py
│       │       ├── files.py
│       │       ├── search.py
│       │       ├── summary.py
│       │       └── status.py
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── base.py # [!] Ново: базовый класс агента с общей логикой
│       │   ├── osint/
│       │   │   ├── __init__.py
│       │   │   └── agent.py
│       │   ├── project_analyzer/
│       │   │   ├── __init__.py
│       │   │   └── analyzer.py
│       │   └── training/
│       │       ├── __init__.py
│       │       └── trainer.py
│       ├── rag/
│       │   ├── __init__.py
│       │   ├── retriever.py
│       │   ├── semantic.py
│       │   ├── ner.py
│       │   └── graph.py
│       ├── embeddings/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── providers/
│       │       ├── __init__.py
│       │       ├── openai.py
│       │       └── local.py
│       ├── vector_store/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── qdrant_store.py
│       │   └── faiss_store.py
│       ├── llm/
│       │   ├── __init__.py
│       │   ├── base.py
│       │   ├── router.py
│       │   ├── caching.py # [!] Ново: кэширование ответов LLM (напр., Redis)
│       │   └── providers/
│       │       ├── __init__.py
│       │       ├── openai.py
│       │       ├── gigachat.py
│       │       └── mistral_local.py
│       ├── workers/
│       │   ├── __init__.py
│       │   ├── celery_app.py
│       │   └── tasks.py # [!] Ново: сами Celery-таски (импортируются в celery_app)
│       ├── telemetry/
│       │   ├── __init__.py
│       │   ├── logging.py
│       │   ├── metrics.py
│       │   └── tracing.py # [!] Ново: распределенная трассировка (OpenTelemetry)
│       ├── common/
│       │   ├── __init__.py
│       │   ├── paths.py
│       │   ├── config.py
│       │   └── schemas.py
│       └── services/ # [!] Ново: слой сервисов для бизнес-логики
│           ├── __init__.py
│           ├── file_service.py # Инкапсулирует работу с файлами (сохранение, валидация)
│           ├── summary_service.py # Инкапсулирует логику генерации резюме
│           └── search_service.py # Оркестрирует RAG, вектора, LLM для поиска
├── docs/
│   ├── architecture.md
│   └── adr/
│       └── ADR-0001-structure.md
├── project_notes/
│   ├── roadmap.md
│   ├── design_notes.md
│   ├── research/
│   └── decisions/
├── tests/ # [!] Предлагается структура mirrors src/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_health.py
│   │   └── ... # другие модульные тесты
│   ├── integration/
│   │   └── test_search_api.py # интеграционные тесты API
│   └── conftest.py # фикстуры pytest
├── deploy/
│   ├── docker/
│   │   ├── Dockerfile.api
│   │   ├── Dockerfile.worker
│   │   └── docker-compose.yaml
│   └── k8s/
│       ├── api-deployment.yaml
│       ├── worker-deployment.yaml
│       ├── redis-deployment.yaml # [!] Ново: Celery требует брокер (Redis/RabbitMQ)
│       └── qdrant-deployment.yaml # [!] Ново: если используем Qdrant в k8s
├── scripts/ # [!] Ново: полезные скрипты (напр., для миграций БД, seed данных)
│   └── prestart.sh # Скрипт, запускаемый перед стартом приложения в Docker
├── .gitignore
├── .env.example
├── .pre-commit-config.yaml # [!] Ново: настройка pre-commit хуков (линтеры, форматирование)
├── pyproject.toml # Сюда добавляем линтеры, pytest, pre-commit
├── Makefile
└── README.md
Пояснения к ключевым дополнениям:
src-layout: Современный стандарт для Python-проектов, избегает конфликтов импорта.

__init__.py: Не забывайте создавать эти файлы в каждой папке-пакете, чтобы Python корректно импортировал модули.

api/dependencies.py: Централизованное место для FastAPI.Depends (получение сессии БД, инициализация сервисов). Это делает app.py чище.

api/errors.py и api/middleware.py: Для централизованной обработки ошибок и добавления middleware (например, для аутентификации).

services/ слой: Важное дополнение. Агенты и API не должны напрямую работать с RAG, LLM и базами данных. Сервисы инкапсулируют сложную бизнес-логику, оставляя API и агентам роль оркестраторов. Это делает код более тестируемым и переиспользуемым.

llm/caching.py: Кэширование ответов LLM — критически важно для экономии денег и увеличения скорости.

workers/tasks.py: Логично вынести сами задачи Celery в отдельный файл.

telemetry/tracing.py: Распределенная трассировка (OpenTelemetry) — золотой стандарт для наблюдения за сложными распределенными системами.

Структура tests/: Зеркалирует структуру src/ для простоты навигации. Разделение на unit/integration.

deploy/k8s/redis-deployment.yaml: Celery требует брокер сообщений (Redis или RabbitMQ), его тоже нужно деплоить.

scripts/: Полезно для скриптов инициализации, миграций и т.д.

.pre-commit-config.yaml: Автоматизация проверки кода (black, isort, ruff, mypy) перед коммитом. Сильно повышает качество кода.

Дополнение к pyproject.toml (важно!)
Убедитесь, что в pyproject.toml настроена корректная упаковка для src-layout:

toml
[build-system]
requires = ["setuptools>=65.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
package-dir = {"" = "src"} # [!] Ключевая строка для поиска пакетов в src
packages = { find = { where = ["src"] } } # [!] Ищем пакеты в папке src

[project]
name = "mindforge-core"
version = "0.1.0"
# ... остальные настройки ...
Этот анализ и предложения должны помочь сделать структуру вашего проекта mindforge еще более robust, поддерживаемой и готовой к промышленной эксплуатации.