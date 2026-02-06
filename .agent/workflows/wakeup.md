---
description: Start a work session, load project context and memory
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
Read .agent/memory/13_preferences/language.md
Extract LANGUAGE= value
All subsequent output must be in this language!
```

### 2. Read Main Memory Index

```
Read .agent/MEMORY_INDEX.md
```

Output brief summary: how many categories, last update date.

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

### 5. Check Pending Tasks

```
Read .agent/memory/07_context/pending_tasks.md (if exists)
```

If there are pending tasks — display the list.

### 6. Load User Preferences

```
Read .agent/memory/13_preferences/_index.md
Read .agent/memory/13_preferences/communication.md
```

Apply response styling from preferences.

### 7. Initialize New Session

```
Update .agent/memory/07_context/current_session.md
```

Set:
- **Start Date**: current date/time
- **Status**: Active

### 8. Report Readiness

Output in configured language:

```
✅ Session started!

📊 Memory Statistics:
| Category | Status |
|----------|--------|
| Categories loaded | 13 |
| Memory entries | N |
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
