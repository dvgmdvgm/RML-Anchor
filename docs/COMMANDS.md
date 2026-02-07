# 📖 RLM-Anchor — Complete Command Reference

> All commands available in the RLM-Anchor memory system.
> Each command is a chat prompt — just type it and AI will execute the workflow.

---

## 📋 Quick Reference

| Command | Purpose | When to Use |
|---------|---------|-------------|
| [`/wakeup`](#-wakeup) | Start session | Beginning of work |
| [`/sleep`](#-sleep) | End session | End of work |
| [`/remember`](#-remember) | Save to memory | Important moment |
| [`/recall`](#-recall) | Search memory | Need info |
| [`/handoff`](#-handoff) | Switch AI model | Changing model |
| [`/walkthrough`](#-walkthrough) | Document work | Feature done |
| [`/anchor_briefing`](#-anchor_briefing) | Full project overview | Onboarding / review |
| [`/memory-stats`](#-memory-stats) | Memory analytics | Check health |
| [`/anchor_agent`](#-anchor_agent) | Initialize system | First setup |
| [`/anchor_update`](#-anchor_update) | Update system | New version |
| [`/anchor_backup`](#-anchor_backup) | Create backup | Before changes |
| [`/anchor_restore`](#-anchor_restore) | Restore backup | Recovery |
| [`/anchor_cleanup`](#-anchor_cleanup) | Clean old data | Memory bloat |
| [`/anchor_validate`](#-anchor_validate) | Check integrity | Diagnosing issues |
| [`/anchor_remove`](#-anchor_remove) | Remove system | Uninstall |

---

## 🌅 Core Commands (Daily Use)

---

### ☀️ `/wakeup`

**Start a work session — load project context into AI memory.**

```
/wakeup
```

#### What it does

1. Reads your language setting
2. Loads the memory index (all 13 categories)
3. Checks for unfinished sessions
4. Loads pending tasks
5. Reads your coding style, preferences
6. Reports session status

#### When to use

- **Every time** you start a new chat or session
- After switching to a different AI model
- Returning to work after a break

#### What you get

AI instantly knows your project: architecture, past decisions, coding style, pending tasks, and everything saved in memory. No need to re-explain context.

#### Example

```
YOU: /wakeup

AI: 🚀 Загрузка контекста проекта...

    📊 Память: 13 категорий, 47 записей
    📅 Последняя сессия: 2026-02-07 (вчера)
    
    📌 Незавершённые задачи:
    • 🔴 Исправить баг с авторизацией
    • 🟡 Добавить пагинацию в каталог
    
    💻 Стек: Django 4.2, PostgreSQL, HTMX
    🎨 Стиль кода: PEP8, double quotes, 4 spaces
    
    ✅ Готов к работе!
```

---

### 🌙 `/sleep`

**End the session — save context and archive work history.**

```
/sleep
```

#### What it does

1. Summarizes everything done in this session
2. Archives the session to `session_history/`
3. Updates statistics log
4. Clears current session for next time
5. Reports what was saved

#### When to use

- **Before closing the chat** — always!
- Before switching AI models
- Before `/anchor_update`

#### Why it matters

Without `/sleep`, AI won't remember what you did. Session data is volatile — running `/sleep` commits it to persistent storage.

#### Example

```
YOU: /sleep

AI: 📝 Сохранение сессии...

    ## Работа за сессию:
    
    ✅ Исправлен баг с авторизацией (JWT timeout)
    ✅ Добавлена пагинация в каталог (20 items/page)
    ✅ Обновлены стили мобильной версии
    
    📁 Изменено файлов: 8
    ⏱️ Время работы: ~2 часа
    
    📦 Сессия архивирована: session_2026-02-07_22-30.md
    📊 Статистика обновлена
    
    👋 До встречи!
```

---

### 📌 `/remember`

**Save important information to long-term memory.**

```
/remember [what to save]
/remember [category] [what to save]
```

#### What it does

1. Analyzes the information you want to save
2. Automatically determines the best category (or uses specified)
3. Creates or updates the appropriate memory file
4. Updates the category index
5. Confirms what was saved and where

#### When to use

- Made an important architectural decision
- Found a bug workaround
- Changed business logic
- Set up an external integration
- Learned something critical about the project

#### Categories (auto-detected)

| Info Type | Saved To |
|-----------|----------|
| Architecture decision | `03_decisions/` |
| Bug or workaround | `06_problems/` |
| Business rule | `04_domain/` |
| API / external service | `09_external/` |
| Deployment config | `11_deployment/` |
| Team member info | `08_people/` |
| Code pattern / style | `05_code/` |
| Testing strategy | `10_testing/` |
| Future plan | `12_roadmap/` |

#### Example

```
YOU: /remember We chose PostgreSQL over MySQL because we need 
     JSONB fields for flexible user profiles and full-text search

AI: ✅ Сохранено в память

    📁 Файл: 03_decisions/ADR-003-postgresql.md
    📂 Категория: Архитектурные решения
    
    | Параметр | Значение |
    |----------|----------|
    | Решение | PostgreSQL вместо MySQL |
    | Причина | JSONB + полнотекстовый поиск |
    | Дата | 2026-02-07 |
    | Статус | ✅ Активно |
```

---

### 🔍 `/recall`

**Search through project memory using smart multi-level search.**

```
/recall [query]
/recall --global [query]    # search linked projects too
```

#### What it does

1. Parses your query (keywords, intent, synonyms)
2. **Level 1**: Searches all `_index.md` files for matches
3. **Level 2**: Opens matched files and searches content
4. **Level 3**: Deep search with synonym expansion
5. Presents results with source references

#### Search intelligence

The search doesn't just look for exact words. For example:
- `"auth"` → also searches `"authentication"`, `"login"`, `"JWT"`, `"OAuth"`
- `"db"` → also searches `"database"`, `"PostgreSQL"`, `"migration"`
- `"cors"` → also searches `"cross-origin"`, `"preflight"`, `"access-control"`

#### When to use

- "Why did we choose X?"
- "How did we solve the Y problem?"
- "What's our deployment process?"
- "What did we decide about Z?"

#### Example

```
YOU: /recall why postgresql

AI: 📁 Найдено в памяти:

    📄 03_decisions/ADR-003-postgresql.md
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Решение: PostgreSQL вместо MySQL
    Причина: JSONB поля для гибких профилей + 
             полнотекстовый поиск
    Дата: 2026-02-07
    
    📄 02_architecture/tech-stack.md
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Database: PostgreSQL 15
    ORM: Django ORM
    Migrations: django-migrations
```

---

## 🔄 Context & Documentation Commands

---

### 🔄 `/handoff`

**Create a compact context summary for switching between AI models.**

```
/handoff
```

#### What it does

1. Reads current session, pending tasks, recent decisions
2. Generates a compact handoff document with:
   - Current project state
   - Key files in focus
   - Recent decisions
   - Critical notes
   - Pending tasks
   - Style reminders
3. Optionally saves to memory

#### When to use

- Switching from Claude to Gemini (or any model)
- Starting a new chat with the same model
- Handing off work to a teammate

#### Advantage

Instead of re-explaining everything, you paste the handoff summary into the new chat. The new AI immediately has full context.

#### Example

```
YOU: /handoff

AI: # 🔄 Сводка для передачи контекста
    
    > Дата: 2026-02-07 22:30
    > Язык: Русский (ru)
    
    ## 📍 Текущее состояние
    
    Проект: E-commerce Platform
    Работаем над: Системой оплаты
    Последнее: Интегрировали Stripe API
    Следующий шаг: Добавить webhook обработчик
    
    ## ⚠️ Критические заметки
    
    - API ключ Stripe в .env, НЕ в коде
    - Используем PostgreSQL с JSONB
    - Стиль кода: PEP8, double quotes
    
    ## 📋 Нерешённые задачи
    
    - [ ] 🔴 Webhook для Stripe
    - [ ] 🟡 Пагинация каталога
```

---

### 📖 `/walkthrough`

**Generate comprehensive documentation for completed work.**

```
/walkthrough [feature name]
/walkthrough                    # auto-detect from recent work
```

#### What it does

1. Gathers all context about recent implementation
2. Creates a detailed document: overview, files changed, how it works, usage examples, limitations
3. Saves to walkthroughs folder in memory

#### When to use

- Just finished implementing a feature
- Fixed a complex bug
- Completed a significant refactoring
- Want to document what was done for future reference

#### What you get

A complete technical document that future-you (or a teammate) can read to understand exactly what was built and how to use it.

#### Example

```
YOU: /walkthrough Stripe Integration

AI: # 📖 Walkthrough: Интеграция Stripe
    
    > Дата: 2026-02-07
    > Статус: ✅ Завершено
    
    ## 🎯 Обзор
    
    Интегрирована платёжная система Stripe для 
    обработки подписок и разовых платежей.
    
    ## 📁 Изменённые файлы
    
    | Файл | Действие | Описание |
    |------|----------|----------|
    | payments/views.py | Создан | API endpoints |
    | payments/webhooks.py | Создан | Webhook handler |
    | settings.py | Изменён | Stripe API keys |
    
    ## 🔧 Как это работает
    [... подробное описание ...]
    
    ✅ Сохранено: walkthroughs/2026-02-07_stripe.md
```

---

### 📊 `/anchor_briefing`

**Generate a complete overview of the entire project from all 13 memory categories.**

```
/anchor_briefing
```

#### What it does

1. Reads ALL `_index.md` files across all 13 categories
2. For each category with content, reads the actual entries
3. Generates a comprehensive report: project info, architecture, decisions, domain logic, code style, known issues, context, team, integrations, testing, deployment, roadmap, preferences

#### When to use

- **Onboarding** to a project for the first time
- After a **long break** from the project
- When you need a **complete picture** of all project knowledge
- For **project reviews** or audits

#### What you get

The most comprehensive report in the system — covers everything stored in memory across all 13 categories.

#### Example

```
YOU: /anchor_briefing

AI: 📊 ПОЛНЫЙ БРИФИНГ: E-commerce Platform
    
    > Записей в памяти: 47
    > Категорий с данными: 11/13
    
    ## 📁 01. О проекте
    | Параметр | Значение |
    |----------|----------|
    | Стек | Django 4.2, PostgreSQL, HTMX |
    | Статус | 🔄 В разработке |
    
    ## 🏗️ 02. Архитектура
    Монолит + Django REST Framework + Celery
    
    ## ⚖️ 03. Решения (ADR)
    | ID | Решение |
    |----|---------|
    | ADR-001 | JWT авторизация |
    | ADR-002 | PostgreSQL + JSONB |
    | ADR-003 | Stripe для оплаты |
    
    ... [все 13 категорий] ...
```

---

### 📊 `/memory-stats`

**Show memory analytics dashboard with statistics and trends.**

```
/memory-stats                  # Full dashboard
/memory-stats --short          # Current state only
```

#### What it does

1. Counts files and entries per category
2. Calculates memory size and health
3. Analyzes session history trends
4. Provides optimization recommendations

#### When to use

- Check how much memory is used
- See which categories are most active
- After cleanup to verify results
- Periodic health check

#### Example

```
YOU: /memory-stats

AI: 📊 MEMORY ANALYTICS DASHBOARD
    
    ## Текущее состояние
    
    | Категория | Записей | Размер |
    |-----------|---------|--------|
    | 01_project | 3 | 4.2 KB |
    | 02_architecture | 5 | 12.1 KB |
    | 03_decisions | 7 | 18.4 KB |
    | ... | ... | ... |
    | Итого | 47 | 156 KB |
    
    ## Тренды
    📈 Сессии за неделю: 12
    📈 Новых записей: 8
    
    ## Рекомендации
    ⚠️ 07_context/session_history/ — 45 файлов
       Рекомендуется: /anchor_cleanup sessions
```

---

## 🛠️ System Management Commands

---

### 🚀 `/anchor_agent`

**Initialize RLM-Anchor in a new project — scan and configure memory.**

```
/anchor_agent
/anchor_agent [scan instruction]
```

#### What it does

1. Detects user language and translates all templates
2. Scans project directories for existing code, configs, documentation
3. Extracts technical data: stack, architecture, patterns, business rules
4. Populates memory categories with discovered information
5. Sets up preferences (coding style, communication)

#### When to use

- **First-time setup** after copying `.agent/` folder to your project
- One-time initialization command

#### Advantage

Instead of manually filling 13 memory categories, AI automatically discovers project context and populates memory with relevant data.

#### Example

```
YOU: /anchor_agent scan the project and configure memory

AI: 📋 ИНТЕГРАЦИЯ RLM-ANCHOR
    
    🔍 Сканирование проекта...
    
    ✅ Обнаружено:
    • Стек: Django 4.2, PostgreSQL, HTMX
    • Моделей: 12 (User, Product, Order...)
    • Шаблонов: 28 HTML файлов
    • API endpoints: 15
    • Тестов: 45
    
    📝 Заполнена память:
    • 01_project: основная информация
    • 02_architecture: структура проекта
    • 04_domain: бизнес-модели
    • 05_code: паттерны кода
    • 13_preferences: язык, стиль
    
    ✅ Инициализация завершена!
    Выполните /wakeup для начала работы.
```

---

### 🔄 `/anchor_update`

**Update RLM-Anchor to the latest version from GitHub without losing data.**

```
/anchor_update                  # Interactive update
/anchor_update --check          # Check only, no changes
```

#### What it does

1. Downloads latest version from GitHub
2. Compares versions
3. Creates automatic backup
4. Classifies files: OVERWRITE (safe to replace), SMART_MERGE (preserve user data), ADD_NEW (new files)
5. Applies updates preserving all user data
6. Translates new files to user's language
7. Reports changes

#### When to use

- When a new version is available
- To get new features or commands
- To fix bugs in workflows

#### Safety

- **Automatic backup** before any changes
- **User data never overwritten**: memory entries, session history, preferences
- **Custom workflows preserved**: your own workflow files are never touched

> ⚠️ **Recommended order**: `/sleep` → `/anchor_update` → `/wakeup`

#### Example

```
YOU: /anchor_update

AI: 🔄 ОБНОВЛЕНИЕ RLM-ANCHOR
    
    📌 Текущая версия: 1.4.0
    📌 Новая версия: 1.5.0
    
    📦 Бэкап создан: pre_update_1.4.0.zip
    
    📦 Изменения:
    | Действие | Файлов | Детали |
    |----------|--------|--------|
    | 🟢 Обновлено | 8 | workflows, scripts |
    | 🟡 Слияние | 2 | indexes (данные сохранены) |
    | 🆕 Добавлено | 1 | anchor_validate.md |
    
    ✅ Обновление завершено: v1.5.0
```

---

### 📦 `/anchor_backup`

**Create a complete backup of the RLM-Anchor system.**

```
/anchor_backup
/anchor_backup [custom_name]
```

#### What it does

1. Collects all RLM-Anchor files (memory, workflows, scripts, skills)
2. Creates a ZIP archive in `.agent/backups/`
3. Reports file count and size

#### When to use

- Before major refactoring
- Before running experimental commands
- To transfer RLM-Anchor to another PC or IDE
- As a periodic safety snapshot

#### What's backed up

All 13 memory categories, all workflows, scripts, skills, and the main index. Your custom IDE configs in `.agent/` are NOT included (they stay safe).

#### Example

```
YOU: /anchor_backup my_milestone

AI: ✅ Backup Created Successfully
    
    📦 File: .agent/backups/anchor_backup_my_milestone_2026-02-07.zip
    📊 Size: 2.3 MB
    📁 RLM Files: 47
    
    🛡️ Only RLM-Anchor files were backed up.
       Your custom IDE configs were NOT included.
```

---

### 📥 `/anchor_restore`

**Restore RLM-Anchor from a previously created backup.**

```
/anchor_restore [path_to_zip]
```

#### What it does

1. Validates the backup file
2. Offers choices: Overwrite / Merge / Cancel
3. Creates safety backup of current state
4. Extracts backup contents
5. Verifies restoration

#### When to use

- After accidental deletion
- When transferring from another PC
- To revert to a previous state
- After a failed update

#### Example

```
YOU: /anchor_restore ./anchor_backup_my_milestone_2026-02-07.zip

AI: 📦 Validating backup...
    ✅ Valid RLM-Anchor backup
    
    ⚠️ Existing .agent/ found!
    
    Choose:
    1. Overwrite (backup current first)
    2. Merge
    3. Cancel

YOU: 1

AI: ✅ Restore completed!
    📁 Files: 47
    🧠 Memory entries: 23
    
    Run /wakeup to start!
```

---

### 🧹 `/anchor_cleanup`

**Intelligent memory cleanup with session merging, topic compression, and archiving.**

```
/anchor_cleanup                  # Full cleanup (all 3 phases)
/anchor_cleanup sessions         # Phase 1 only — merge old sessions
/anchor_cleanup topics           # Phase 2 only — compress topics
/anchor_cleanup --dry-run        # Preview without changes
```

#### What it does

- **Phase 1** — Session Merge: Combines old session files into monthly digests (e.g., 30 daily sessions → 1 monthly summary)
- **Phase 2** — Topic Compress: Merges multiple files on the same topic into one (e.g., 3 files about CORS → 1 comprehensive file)
- **Phase 3** — Archive: Creates archive summaries before any deletion

#### When to use

- Memory has grown large (many session files)
- `/memory-stats` recommends cleanup
- Duplicate or similar entries exist
- Before transferring to a new PC (reduce size)

#### Advantage

Keeps memory efficient and fast without losing information. Old data is summarized, not deleted.

#### Example

```
YOU: /anchor_cleanup sessions

AI: 🧹 MEMORY CLEANUP — Phase 1
    
    📊 Scan Results:
    • Session files: 45
    • Older than 30 days: 32
    
    📦 Creating monthly digests:
    • December 2025: 12 sessions → 1 digest
    • January 2026: 20 sessions → 1 digest
    
    ✅ Cleanup complete:
    • Removed: 32 files
    • Created: 2 digest files
    • Saved: 340 KB
```

---

### 🔎 `/anchor_validate`

**Check memory structure integrity — find broken links, orphan files, naming issues.**

```
/anchor_validate                  # Full validation (5 checks)
/anchor_validate --fix            # Validate + auto-fix
/anchor_validate --quick          # Quick sync check only
```

#### What it does

5 validation checks:

1. **Category Structure** — Are all 13 folders and `_index.md` files present?
2. **Index ↔ Files Sync** — Do index entries match actual files? (ghost entries, orphan files)
3. **File Naming** — Do files follow naming conventions?
4. **Broken Links** — Do internal references point to existing files?
5. **Empty & Duplicates** — Any empty files or duplicate topics?

#### When to use

- Something feels off (missing data, broken references)
- After manual edits to memory files
- Periodic health check (monthly)
- After recovery from backup

#### Example

```
YOU: /anchor_validate

AI: 📋 VALIDATION REPORT
    
    | # | Check | Result | Issues |
    |---|-------|--------|--------|
    | 1 | Category Structure | ✅ OK | 0 |
    | 2 | Index ↔ Files Sync | ⚠️ | 2 |
    | 3 | File Naming | ✅ OK | 0 |
    | 4 | Broken Links | ⚠️ | 1 |
    | 5 | Empty & Duplicates | ✅ OK | 0 |
    
    Total: 3 issues found
    Auto-fixable: 2/3
    
    🔧 Run auto-fix? [y/N/review]
```

---

### 🗑️ `/anchor_remove`

**Safely remove RLM-Anchor from the project.**

```
/anchor_remove
```

#### What it does

1. Displays a warning about what will be removed
2. Requires confirmation code (safety)
3. Creates a full backup automatically
4. Removes ONLY RLM-Anchor files (your IDE configs are safe)
5. Cleans up empty folders

#### When to use

- You no longer need RLM-Anchor in this project
- You want to start fresh (remove → reinstall)
- Migrating to a different memory system

#### Safety

- **Two-factor confirmation** (you must type a random code)
- **Automatic backup** before deletion
- **Selective deletion** — only RLM-Anchor files, your custom configs in `.agent/` stay

#### Example

```
YOU: /anchor_remove

AI: ⚠️ WARNING: RLM-ANCHOR REMOVAL
    
    This will remove:
    • 13 memory categories
    • 15 workflow files
    • 3 scripts
    • MEMORY_INDEX.md
    
    🛡️ Your IDE configs in .agent/ are SAFE!
    
    🔐 To confirm, type: REMOVE-7X4K

YOU: REMOVE-7X4K

AI: 📦 Creating backup first...
    ✅ Backup: anchor_backup_pre_remove_2026-02-07.zip
    
    🗑️ Removing RLM-Anchor files...
    ✅ Removed successfully!
    
    Restore anytime: /anchor_restore [backup_path]
```

---

## 💡 Tips & Best Practices

### Daily Workflow

```
/wakeup → work → /remember (important stuff) → /sleep
```

### Before Switching AI Models

```
/handoff → copy summary → paste into new chat → /wakeup
```

### Before System Updates

```
/sleep → /anchor_update → /wakeup
```

### Monthly Maintenance

```
/memory-stats → /anchor_validate → /anchor_cleanup
```

### Before Major Changes

```
/anchor_backup → make changes → (if failed) /anchor_restore
```
