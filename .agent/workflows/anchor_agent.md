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

### 1. Check Current Language Setting

```
Read .agent/memory/13_preferences/language.md
All output must be in this language!
```

### 2. Detect IDE Rules Files

> [!IMPORTANT]
> Before integration, check for existing IDE configuration files that contain 
> project rules, preferences, and instructions. These should be imported into 
> the RLM memory system.

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

If any file is found, proceed to Step 3 (Import). Otherwise, skip to Step 4.

### 3. Import IDE Rules Data

For each detected rules file:

1. **Read the file content**
2. **Parse and categorize the data**:
   
   | Content Type | Destination |
   |-------------|-------------|
   | Coding style preferences | `13_preferences/coding_style.md` |
   | Tech stack info | `01_project/techstack.md` |
   | Project guidelines | `01_project/guidelines.md` |
   | Communication style | `13_preferences/communication.md` |
   | Business rules | `04_domain/business_rules.md` |
   | Architecture decisions | `02_architecture/patterns.md` |
   
3. **Add source reference**: Include note about imported data origin

```markdown
<!-- Imported from GEMINI.md on 2026-02-05 -->
```

### 4. Scan for Existing .agent/ Structure

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

### 5. Report Conflicts

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

### 6. Offer Options

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

### 7. Execute Chosen Option

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

### 8. Post-Integration Verification

```
Run validation:
- Check all required files exist
- Verify index structure
- Test language file
```

### 9. Report Success (with IDE Rules Import)

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
