---
agent: agent
description: "Wakeup (RLM-Anchor)"
---

# /wakeup — Start Session

## Usage

```
/wakeup
```

---

## Execution Steps

// turbo-all

### 1. Read Language Settings

```
Read .agent/memory/13_preferences/language_local.md (if exists, use it)
Otherwise read .agent/memory/13_preferences/language.md
Extract LANGUAGE= value
All subsequent output must be in this language!
```

### 2. Check for Handoff Snapshot (v2.5.2 Lean Entry)

```
Check if .agent/memory/07_context/handoff_snapshot.md exists.
```

If it exists:
- Read MUST be limited to this ONE file.
- Skip steps 3, 4, 5, and 6 (Index, History, Stats, Tasks). All that info is in the snapshot.

If NOT exists (cold start):
- Perform standard legacy steps (3-6).

### 3. Check for Unfinished Session

```
Read .agent/memory/07_context/current_session.md
```

**If not empty template** (contains actual data):
- Warn user: "Detected unfinished session from [date]. Data will be archived."
- Archive it first → `session_history/session_YYYY-MM-DD_orphan.md`
- Reset `current_session.md` to template

### 4. Load Session History

```
List files in .agent/memory/07_context/session_history/
Read last 2-3 sessions for context
```

Output:
- Last session summary
- Key decisions from recent sessions

### 5. Memory Health Check & Quick Validation

```
Count files in .agent/memory/07_context/session_history/
Count total .md files across all memory categories (01-12)
Read thresholds from .agent/memory/13_preferences/cleanup_settings.md
```

**Quick health evaluation:**

| Condition | Action |
|-----------|--------|
| Session files > 30 | ⚠️ Warn: "N session files detected. Consider running /anchor_cleanup" |
| Session files > 100 | 🔴 Warn: "Memory overload! Strongly recommend /anchor_cleanup" |
| Total memory files > 100 | ⚠️ Warn: "N memory entries. Topic compression may help" |

**Quick sync validation:**

```
Count content files on disk (exclude _index.md, _template.md, system files)
Count file entries across all _index.md tables
If counts don't match → ⚠️ "Index out of sync. Run /anchor_validate"
```

**Anomaly detection (from stats log):**

```
Read last 2 rows from .agent/memory/07_context/memory_stats_log.md
If log has ≥ 2 entries, compare last two rows:
  If entries grew > 10 since last session → ⚠️ "Rapid growth: +N new entries"
  If size grew > 50 KB since last session → ⚠️ "Large data increase: +X KB"
If log is empty or has 1 entry → skip (not enough data)
```

> [!NOTE]
> This is a QUICK check only — no files are modified.
> It only counts and warns. Full analytics via `/memory-stats`.

### 6. Check Pending Tasks

```
Read .agent/memory/07_context/pending_tasks.md (if exists)
```

If there are pending tasks — display the list.

### 7. Load User Preferences

```
Read .agent/memory/13_preferences/_index.md
Read .agent/memory/13_preferences/communication.md
```

Apply response styling from preferences.

### 7.5. Output Critical Rules Reminder

Do NOT read .cursorrules/CLAUDE.md/GEMINI.md files. 
The AI already has this information in its system prompt context. 
Extract the CUSTOM PROJECT RULES from your current memory and display them.

### 8. Initialize New Session

```
Update .agent/memory/07_context/current_session.md
```

Set:
- **Start Date**: current date/time
- **Status**: Active

### 9. Report Readiness

Output in configured language:

```
✅ Session started!

📊 Memory Statistics:
| Category | Status |
|----------|--------|
| Categories loaded | 13 |
| Memory entries | N |
| Session files | N |
| Last session | YYYY-MM-DD |

📅 Previous Session Summary:
| Topic | Decision |
|-------|----------|
| ... | ... |

📌 Pending Tasks:
| Priority | Task |
|----------|------|
| 🔴 High | Task 1 |
| 🟡 Medium | Task 2 |

⚠️ Memory Health: [OK / Warning / Critical]

💡 Ready to work! What shall we do today?
```

---

## Example (Language: Russian)

```
USER: Привет! Давай продолжим работу над проектом.

AI: 🚀 Загружаю контекст проекта...

    ✅ Сессия начата!
    
    📊 Память проекта:
    | Параметр | Значение |
    |----------|----------|
    | Категорий | 13 |
    | Записей | 5 |
    | Последняя сессия | 2026-02-05 |
    
    📅 Прошлая сессия (2026-02-05):
    | Тема | Решение |
    |------|---------|
    | Архитектура API | REST вместо GraphQL |
    | Авторизация | OAuth2 + JWT |
    
    📌 Незавершённые задачи:
    | Приоритет | Задача |
    |-----------|--------|
    | 🔴 | Доделать эндпоинт /users |
    | 🟡 | Написать тесты |
    
    💡 Чем займёмся сегодня?
```

## Example (Language: English)

```
USER: Hi! Let's continue working on the project.

AI: 🚀 Loading project context...

    ✅ Session started!
    
    📊 Project memory:
    | Parameter | Value |
    |-----------|-------|
    | Categories | 13 |
    | Entries | 5 |
    | Last session | 2026-02-05 |
    
    📅 Previous session (2026-02-05):
    | Topic | Decision |
    |-------|----------|
    | API Architecture | REST over GraphQL |
    | Authentication | OAuth2 + JWT |
    
    📌 Pending tasks:
    | Priority | Task |
    |----------|------|
    | 🔴 | Complete /users endpoint |
    | 🟡 | Write tests |
    
    💡 What shall we work on today?
```