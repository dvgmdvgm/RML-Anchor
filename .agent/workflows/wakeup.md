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

### 3. Load Current Session Context

```
Read .agent/memory/07_context/current_session.md (if exists)
```

Output:
- Last session date
- Main topics
- Key decisions

### 4. Check Pending Tasks

```
Read .agent/memory/07_context/pending_tasks.md (if exists)
```

If there are pending tasks — display the list.

### 5. Load User Preferences

```
Read .agent/memory/13_preferences/_index.md
```

If there are entries — take them into account.

### 6. Report Readiness

Output in configured language:

```
✅ Session started!

📊 Memory Statistics:
- Categories: 13
- Entries: N
- Last updated: YYYY-MM-DD

📌 Pending Tasks:
- [ ] Task 1
- [ ] Task 2

💡 Ready to work!
```

---

## Automatic Execution

This procedure should run automatically on the first user message in a new session if:

1. `.agent/MEMORY_INDEX.md` exists
2. This is clearly a new session (not a continuation)

---

## Example (Language: Russian)

```
USER: Привет! Давай продолжим работу над проектом.

AI: 🚀 Загружаю контекст проекта...

    ✅ Сессия начата!
    
    📊 Память проекта:
    - 13 категорий
    - 5 записей
    - Последнее обновление: 2026-02-04
    
    📅 Прошлая сессия (2026-02-04):
    - Обсуждали архитектуру API
    - Решили использовать REST вместо GraphQL
    
    📌 Незавершённые задачи:
    - [ ] Доделать эндпоинт /users
    - [ ] Написать тесты для авторизации
    
    💡 Чем займёмся сегодня?
```

## Example (Language: English)

```
USER: Hi! Let's continue working on the project.

AI: 🚀 Loading project context...

    ✅ Session started!
    
    📊 Project memory:
    - 13 categories
    - 5 entries
    - Last updated: 2026-02-04
    
    📅 Previous session (2026-02-04):
    - Discussed API architecture
    - Decided to use REST instead of GraphQL
    
    📌 Pending tasks:
    - [ ] Complete /users endpoint
    - [ ] Write authorization tests
    
    💡 What shall we work on today?
```
