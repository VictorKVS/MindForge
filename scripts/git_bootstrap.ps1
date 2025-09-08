Param(
  [string]$RemoteUrl = ""
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
  Write-Host "No git repo found. Initializing..."
  git init | Out-Null
}

New-Item -ItemType Directory -Force -Path ".github" | Out-Null
New-Item -ItemType Directory -Force -Path "scripts" | Out-Null

@"
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
"@ | Out-File -Encoding utf8 ".github/CODEOWNERS"

@"
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
"@ | Out-File -Encoding utf8 ".github/pull_request_template.md"

if (-not (Test-Path ".gitattributes")) {
@"
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
"@ | Out-File -Encoding utf8 ".gitattributes"
}

git add .github/CODEOWNERS .github/pull_request_template.md .gitattributes | Out-Null
if (-not (git diff --cached --quiet)) {
  git commit -m "chore(repo): add CODEOWNERS, PR template (RU+EN), .gitattributes" | Out-Null
}

$main = "main"
$develop = "develop"
$current = (git rev-parse --abbrev-ref HEAD).Trim()
if ($current -ne $main) {
  git branch -M $main | Out-Null
}

if ($RemoteUrl -ne "") {
  if (-not (git remote | Select-String -Quiet "^origin$")) {
    git remote add origin $RemoteUrl | Out-Null
  }
  git push -u origin $main
  git checkout -B $develop
  git push -u origin $develop
}

Write-Host "✅ Done. Files created and committed."
