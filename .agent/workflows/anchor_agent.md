---
description: Safely integrates the Antigravity Agent Template into the current project.
---

# /anchor_agent — Safe Integration of RLM-Anchor

## Usage

```
/anchor_agent
/anchor_agent [scan instruction]
```

---

## Description

This workflow safely integrates the AI Memory System into an existing project without overwriting existing files.

---

## Execution Steps

### 1. Language Detection & Template Localization

> [!IMPORTANT]
> This step MUST be completed BEFORE all other steps.
> The memory system must be fully translated to the user's language
> before any project scanning or data import begins.

**1.1. Read language setting:**

```
Read .agent/memory/13_preferences/language.md
Extract the value of LANGUAGE= (e.g., "en", "ru", "es", "de", etc.)
```

**1.2. If language is NOT "en" — translate these files (exactly 25):**

```yaml
# ── Category indexes (13 files) ──
- .agent/memory/01_project/_index.md
- .agent/memory/02_architecture/_index.md
- .agent/memory/03_decisions/_index.md
- .agent/memory/04_domain/_index.md
- .agent/memory/05_code/_index.md
- .agent/memory/06_problems/_index.md
- .agent/memory/07_context/_index.md
- .agent/memory/08_people/_index.md
- .agent/memory/09_external/_index.md
- .agent/memory/10_testing/_index.md
- .agent/memory/11_deployment/_index.md
- .agent/memory/12_roadmap/_index.md
- .agent/memory/13_preferences/_index.md

# ── Templates (2 files) ──
- .agent/memory/03_decisions/_template.md
- .agent/memory/06_problems/_template.md

# ── Context files (2 files) ──
- .agent/memory/07_context/current_session.md
- .agent/memory/07_context/pending_tasks.md

# ── Subfolder READMEs (2 files) ──
- .agent/memory/06_problems/bugs/README.md
- .agent/memory/06_problems/workarounds/README.md

# ── Preferences / Settings (6 files) ──
- .agent/memory/13_preferences/auto_save_rules.md
- .agent/memory/13_preferences/cleanup_settings.md
- .agent/memory/13_preferences/coding_style.md
- .agent/memory/13_preferences/communication.md
- .agent/memory/13_preferences/memory_settings.md
- .agent/memory/13_preferences/response_templates.md
```

> [!CAUTION]
> **DO NOT translate** `.agent/memory/13_preferences/language.md` — 
> it is a configuration file and must stay as-is.

**Translation rules** — for EACH file:
1. Read its current content
2. Translate ALL English text to the target language (headings, descriptions, table headers, hints, comments)
3. **Keep unchanged**: structure, formatting, emoji, markdown syntax, code blocks
4. **Keep unchanged**: category codes (`01_project`, `02_architecture`, etc.)
5. **Keep unchanged**: YAML keys (`TRIGGERS`, `CONFIDENCE`, `TTL`, `AUTO_SAVE`, etc.)
6. **Keep unchanged**: file paths and filenames inside the content
7. Write the translated content back to the file

**1.3. After translation, confirm:**

```
All output from this point on must be in the user's chosen language!
```

### 2. Project Scanning & Analysis

> [!IMPORTANT]
> Before importing any rules or creating memory entries, the AI must 
> understand what the project actually IS — its purpose, structure, 
> technologies, and how it works.

**2.1. Scan project structure:**

```
List the top-level files and directories of the project.
Identify the project type (web app, library, CLI tool, API, mobile, etc.)
```

**2.2. Read key project files (if they exist):**

```yaml
KEY_FILES:
  # Documentation
  - README.md (or README.*)
  - CONTRIBUTING.md
  - CHANGELOG.md
  - docs/

  # Package/dependency files
  - package.json          # Node.js
  - requirements.txt      # Python
  - Pipfile               # Python
  - pyproject.toml        # Python
  - Cargo.toml            # Rust
  - go.mod                # Go
  - pom.xml               # Java/Maven
  - build.gradle          # Java/Gradle
  - Gemfile               # Ruby
  - composer.json         # PHP

  # Configuration
  - .env.example
  - docker-compose.yml
  - Dockerfile
  - Makefile
  - tsconfig.json
  - webpack.config.*
  - vite.config.*

  # Entry points
  - main.* / index.* / app.* / manage.py / server.*
```

**2.3. Analyze and identify:**

From the scanned files, determine:
- **Project name and purpose** (from README, package.json, etc.)
- **Technology stack** (languages, frameworks, databases)
- **Project structure** (main directories and their purpose)
- **Entry points** (where the app starts)
- **Dependencies** (key libraries used)
- **Build/run commands** (how to start, test, deploy)

**2.4. Save findings to memory:**

Create the following memory entries based on analysis:

| File | Content |
|------|---------|
| `01_project/overview.md` | Project name, purpose, description |
| `01_project/techstack.md` | Languages, frameworks, databases, key dependencies |
| `01_project/structure.md` | Directory layout and purpose of each folder |
| `02_architecture/patterns.md` | Architecture patterns identified (MVC, microservices, etc.) |
| `05_code/conventions.md` | Code style patterns observed (naming, structure) |

> [!NOTE]
> This scan is intentionally SURFACE-LEVEL. 
> It reads key files and directory structure, NOT every source file.
> Deep understanding builds over time through /wakeup sessions.

### 3. Detect IDE Rules Files

> [!NOTE]
> Now that the project is understood, check for IDE configuration files.
> Having project context helps categorize imported rules more accurately.

Check for these files in project root:

```yaml
IDE_RULES_FILES:
  - GEMINI.md              # Antigravity / Gemini CLI
  - .cursorrules           # Cursor IDE
  - .windsurfrules         # Windsurf IDE
  - .github/copilot-instructions.md  # GitHub Copilot
  - .aider.conf.yml        # Aider
  - claude_rules.md        # Claude
  - .clinerules            # Cline VSCode extension
  - CLAUDE.md              # Claude Projects
  - rules.md               # Generic rules file
```

If any file is found, proceed to Step 4 (Import). Otherwise, skip to Step 5.

### 4. Import IDE Rules Data

For each detected rules file:

1. **Read the file content**
2. **Parse and categorize the data** (using project context from Step 2):
   
   | Content Type | Destination |
   |-------------|-------------|
   | Coding style preferences | `13_preferences/coding_style.md` |
   | Tech stack info | `01_project/techstack.md` (merge with existing) |
   | Project guidelines | `01_project/guidelines.md` |
   | Communication style | `13_preferences/communication.md` |
   | Business rules | `04_domain/business_rules.md` |
   | Architecture decisions | `02_architecture/patterns.md` (merge with existing) |
   
3. **Add source reference**: Include note about imported data origin

```markdown
<!-- Imported from GEMINI.md on 2026-02-05 -->
```

### 5. Scan for Existing .agent/ Structure

Check if these files/folders already exist:

```
Check existence of:
- .agent/MEMORY_INDEX.md
- .agent/memory/
- .agent/workflows/remember.md
- .agent/workflows/recall.md
- .agent/workflows/wakeup.md
- .agent/workflows/sleep.md
- .agent/skills/MEMORY_SKILL.md
```

### 6. Report Conflicts

Output conflict report:

```
📋 INTEGRATION ANALYSIS / АНАЛИЗ ИНТЕГРАЦИИ
═══════════════════════════════════════════

✅ Safe to add (no conflicts):
- .agent/memory/ (new folder)
- .agent/MEMORY_INDEX.md
- ...

⚠️ Potential conflicts:
- .agent/workflows/remember.md (already exists!)
- ...

❌ Cannot overwrite (backup needed):
- ...
```

### 7. Offer Options

Present options to user:

```
🔧 OPTIONS / ВАРИАНТЫ:

1. [SAFE] Add only non-conflicting files
   - Creates memory/ folder
   - Adds new workflows with different names
   
2. [MERGE] Merge with existing files
   - Adds memory instructions to existing SKILL files
   - Extends existing workflows
   
3. [FULL] Full installation (backup existing)
   - Creates backup of existing .agent/
   - Installs complete memory system
   
4. [CANCEL] Cancel integration
```

### 8. Execute Chosen Option

Based on user choice, perform the integration:

#### Option 1: SAFE
- Create `.agent/memory/` folder structure
- Add `MEMORY_INDEX.md`
- Add `MEMORY_SKILL.md` to skills/
- Add workflows with unique names if conflicts exist:
  - `remember.md` → `memory-remember.md`
  - `recall.md` → `memory-recall.md`

#### Option 2: MERGE
- Add memory folder structure
- Append MEMORY_SKILL content to existing skill files
- Merge workflow content

#### Option 3: FULL
- Create backup: `.agent.backup.YYYY-MM-DD/`
- Copy all files from template
- Overwrite existing files

### 9. Post-Integration Verification

```
Run validation:
- Check all required files exist
- Verify index structure
- Test language file
```

### 10. Report Success (with IDE Rules Import)

```
✅ INTEGRATION COMPLETE / ИНТЕГРАЦИЯ ЗАВЕРШЕНА
═══════════════════════════════════════════════

📁 Created:
- .agent/memory/ (13 categories)
- .agent/MEMORY_INDEX.md
- ...

📝 Available commands:
- /wakeup - Start session
- /sleep - End session
- /remember - Save to memory
- /recall - Find in memory

🌍 Language set to: [configured language]
```

**If IDE rules were imported, add this section:**

```
📥 IDE RULES IMPORTED / ПРАВИЛА IDE ИМПОРТИРОВАНЫ
═══════════════════════════════════════════════════

The following data was imported from your IDE rules file(s):

| Source File | Imported To | Items |
|-------------|-------------|-------|
| GEMINI.md | `coding_style.md` | 5 preferences |
| GEMINI.md | `guidelines.md` | 3 rules |

> [!TIP]
> It is recommended to DELETE the original rules file(s) to avoid 
> conflicts between IDE rules and RLM memory.
>
> The imported rules now live in:
> - `.agent/memory/13_preferences/coding_style.md`
> - `.agent/memory/01_project/guidelines.md`
>
> **File(s) to delete:**
> - `GEMINI.md`
```

```
💡 Run /wakeup to begin!
```

---

## Example

```
USER: /anchor_agent

AI: 📋 АНАЛИЗ ИНТЕГРАЦИИ
    ═══════════════════════════════════════════
    
    🔍 Обнаружен файл правил IDE: GEMINI.md
    
    Сканирую существующую структуру .agent/...
    
    ✅ Безопасно для добавления:
    - memory/ (новая папка)
    - MEMORY_INDEX.md
    - workflows/wakeup.md
    - workflows/sleep.md
    
    ⚠️ Потенциальные конфликты:
    - workflows/remember.md (уже существует!)
    
    🔧 ВАРИАНТЫ:
    
    1. [SAFE] Добавить только неконфликтующие файлы
    2. [MERGE] Слить с существующими файлами
    3. [FULL] Полная установка (с бэкапом)
    4. [CANCEL] Отменить
    
    Какой вариант выбираешь? (1/2/3/4)

USER: 1

AI: 📦 Выполняю безопасную интеграцию...
    
    ✅ Создано: memory/ (13 категорий)
    ✅ Создано: MEMORY_INDEX.md
    ✅ Создано: workflows/wakeup.md
    ✅ Создано: workflows/sleep.md
    ⚠️ Пропущено: workflows/remember.md (конфликт)
       → Создан: workflows/memory-remember.md
    
    📥 ИМПОРТИРОВАНЫ ПРАВИЛА IDE:
    
    | Источник | Категория | Записей |
    |----------|-----------|---------|
    | GEMINI.md | coding_style.md | 5 |
    | GEMINI.md | guidelines.md | 3 |
    
    💡 Рекомендуется удалить GEMINI.md чтобы избежать конфликтов.
       Правила теперь хранятся в .agent/memory/
    
    ✅ ИНТЕГРАЦИЯ ЗАВЕРШЕНА!
    
    💡 Выполни /wakeup чтобы начать!
```

---

## Important Notes

- Always create backup before FULL installation
- Language setting is preserved from existing project if found
- Existing memory entries are never deleted
- Conflicts are always reported before any action
- IDE rules files are imported automatically and user is notified
- Original IDE rules files should be deleted after import to avoid conflicts
