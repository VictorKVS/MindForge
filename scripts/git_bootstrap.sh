#!/usr/bin/env bash
set -euo pipefail

# --- Config (edit if needed) ---
REPO_REMOTE_DEFAULT="${1:-}"
MAIN_BRANCH="main"
DEVELOP_BRANCH="develop"

# --- Ensure git repo ---
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "No git repo found. Initializing..."
  git init
fi

mkdir -p .github scripts

# --- Write CODEOWNERS ---
cat > .github/CODEOWNERS <<'EOF'
*                                   @VictorKVS
src/mf_core/api/**                  @backend-team
src/mf_core/agents/**               @ml-team
src/mf_core/agents/onec_adapter/**  @backend-team @ml-team
src/mf_core/agents/legislation/**   @ml-team
src/mf_core/agents/risks/**         @ml-team
src/mf_core/agents/control/**       @backend-team
src/mf_core/agents/documents/**     @ml-team
src/mf_core/rag/**                  @ml-team @backend-team
src/mf_core/llm/**                  @ml-team
src/mf_core/vector_store/**         @ml-team @backend-team
src/mf_core/db/**                   @backend-team
src/mf_core/telemetry/**            @backend-team @devops-team
deploy/**                           @devops-team
scripts/**                          @devops-team
tests/**                            @qa-team @backend-team @ml-team
EOF

# --- Write PR template ---
cat > .github/pull_request_template.md <<'EOF'
# 📝 Описание / Description
Кратко: что и зачем меняем? / Briefly: what & why?

- Тип / Type: feat / fix / refactor / docs / chore
- Область / Area: api / agents / db / rag / llm / vector_store / telemetry / infra / tests

Связанные задачи / Linked issues:
- Closes #ISSUE_ID
- Related #ISSUE_ID

## ✅ Чек-лист / Checklist
- [ ] Тесты добавлены/обновлены — Tests added/updated
- [ ] Линтеры/типы пройдены — Linters/typing pass (black, ruff, mypy)
- [ ] Миграции БД (если нужно) — DB migrations (if needed)
- [ ] Документация обновлена — Docs updated
- [ ] Нет секретов/ПДн в коде — No secrets/PII in code
- [ ] Нет регресса по производительности — No perf regress
- [ ] Совместимость API сохранена — API compatibility OK

## 🔄 План раскатки / Rollout
- [ ] Без даунтайма / No downtime
- [ ] Миграции безопасны / Safe migrations
- [ ] Обновлены инструкции деплоя / Deploy docs updated

## 📸 Скриншоты / Screens (opt.)
## 🧪 Как проверить / How to test
EOF

# --- Optional: .gitattributes for normalized EOL ---
if [ ! -f .gitattributes ]; then
cat > .gitattributes <<'EOF'
* text=auto eol=lf
*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.pdf binary
*.doc binary
*.docx binary
*.xls binary
*.xlsx binary
*.md  linguist-detectable=true
*.yml linguist-detectable=true
*.yaml linguist-detectable=true
*.json linguist-detectable=true
EOF
fi

# --- Commit ---
git add .github/CODEOWNERS .github/pull_request_template.md .gitattributes 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -m "chore(repo): add CODEOWNERS, PR template (RU+EN), .gitattributes"
else
  echo "Nothing to commit."
fi

# --- Branch setup & push (optional) ---
CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD || echo 'main')"
if [ "$CURRENT_BRANCH" != "$MAIN_BRANCH" ]; then
  git branch -M "$MAIN_BRANCH"
fi

if [ -n "$REPO_REMOTE_DEFAULT" ]; then
  if ! git remote | grep -q '^origin$'; then
    git remote add origin "$REPO_REMOTE_DEFAULT"
  fi
  git push -u origin "$MAIN_BRANCH"
  git checkout -B "$DEVELOP_BRANCH"
  git push -u origin "$DEVELOP_BRANCH"
fi

echo "✅ Done. CODEOWNERS & PR template installed."
