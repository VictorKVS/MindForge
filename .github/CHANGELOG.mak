# Changelog
All notable changes to this project will be documented in this file.

Формат основан на [SemVer](https://semver.org) и Conventional Commits (feat/fix/docs/refactor/chore).

## [0.1.0] - 2025-09-08
### Added
- Базовая структура MindForge (api, agents, db, rag, llm, vector_store, telemetry)
- Интеграция 1С: эндпоинты `/onec` (webhook, create-task, get-document)
- Заготовка onec_service.py (HTTP-клиент)
- Docker Compose (api, worker, redis, postgres, qdrant)
- Pre-commit (black, ruff, mypy), CI (pytest)

### Changed
- README обновлён под версию v2.1 (светофор, роли, потоки)

### Fixed
- N/A

### Security
- Базовый .gitignore для секретов и артефактов сборки

[0.1.0]: https://github.com/VictorKVS/MindForge/releases/tag/v0.1.0