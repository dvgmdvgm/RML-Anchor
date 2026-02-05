---
description: Safely integrates the Antigravity Agent Template into the current project.
---

# /agent — Safe Integration of Memory System

## Usage

```
/agent
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

### 2. Scan for Existing .agent/ Structure

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

### 3. Report Conflicts

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

### 4. Offer Options

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

### 5. Execute Chosen Option

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

### 6. Post-Integration Verification

```
Run validation:
- Check all required files exist
- Verify index structure
- Test language file
```

### 7. Report Success

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

💡 Run /wakeup to begin!
```

---

## Example

```
USER: /agent

AI: 📋 АНАЛИЗ ИНТЕГРАЦИИ
    ═══════════════════════════════════════════
    
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
    
    ✅ ИНТЕГРАЦИЯ ЗАВЕРШЕНА!
    
    💡 Выполни /wakeup чтобы начать!
```

---

## Important Notes

- Always create backup before FULL installation
- Language setting is preserved from existing project if found
- Existing memory entries are never deleted
- Conflicts are always reported before any action
