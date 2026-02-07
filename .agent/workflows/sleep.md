---
description: End session, save context and summarize the work done
---

# /sleep — End Session

## Usage

```
/sleep
```

---

## Execution Steps

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language.md
All output and saved entries must be in this language!
```

### 1. Summarize Current Session

Analyze the conversation and create a session summary:
- Main discussion topics
- Decisions made
- Files created/modified
- Important notes

**Write in configured language!**

### 2. Archive Session to History

```
Generate filename: session_YYYY-MM-DD_HH-MM.md
Copy current_session.md content → .agent/memory/07_context/session_history/[filename]
```

**Session file format:**

```markdown
# Session: YYYY-MM-DD HH:MM

## 📋 Discussion Topics

1. Topic 1
2. Topic 2

## ⚖️ Decisions Made

| Decision | Description | Impact |
|----------|-------------|--------|
| ... | ... | ... |

## 📁 Modified Files

| File | Change |
|------|--------|
| `file1.py` | Added auth logic |
| `file2.html` | Updated layout |

## 📝 Notes

- Note 1
- Note 2

## ⏳ Pending (Carried Over)

| Priority | Task |
|----------|------|
| 🔴 | Task 1 |
```

### 3. Update pending_tasks.md

```
Update .agent/memory/07_context/pending_tasks.md
```

- Add new pending tasks from this session
- Move completed tasks to "Recently Completed"

### 4. Reset current_session.md

```
Overwrite .agent/memory/07_context/current_session.md with blank template
```

Template:
```markdown
# 📍 Current Session

- **Start Date**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD

---

## 🎯 Main Session Topics

1. —
2. —

---

## 💡 Key Decisions

| Decision | Description |
|----------|-------------|
| — | — |

---

## 📌 Topics Discussed

- —

---

## ⏳ Current Status

**Status**: Ready to start

---

## 📝 Notes

- —
```

### 5. Update Relevant Indexes

If new entries were created in other categories — update their `_index.md`.

### 5.5. Quick Sync Validation

```
Verify: every content file created/modified during this session
        is listed in its category's _index.md
If any orphan found → add it to _index.md now (before session ends)
```

> [!NOTE]
> This catches files saved via /remember or manually that may have
> been missed in _index.md updates. Runs silently — only warns if issues found.

### 5.7. Update Stats Log

```
Append one row to .agent/memory/07_context/memory_stats_log.md
```

Collect:
- **Date**: today's date (YYYY-MM-DD)
- **Sessions**: count files in session_history/
- **Entries**: count total content .md files across categories 01-12
- **Size**: total size of .agent/memory/ folder
- **Decisions**: count files in 03_decisions/ (exclude _index.md, _template.md)
- **Problems**: count files in 06_problems/ (exclude _index.md, _template.md, subdirs)
- **Cleanup**: "cleanup" if /anchor_cleanup was run this session, "—" otherwise

Append as a new table row. **Never overwrite** existing rows.

### 6. Confirm to User

Output in configured language:

```
✅ Session ended!

📊 Session Statistics:
| Metric | Value |
|--------|-------|
| Duration | ~X hours |
| Decisions recorded | N |
| Files modified | M |

📁 Archived to:
- `session_history/session_2026-02-06_03-20.md`

📌 Carried to next session:
| Priority | Task |
|----------|------|
| 🔴 | Task 1 |

👋 See you later!
```

---

## Example (Language: Russian)

```
USER: /sleep

AI: 📝 Суммаризирую сессию...

    ✅ Сессия завершена!
    
    📊 Сегодня:
    | Показатель | Значение |
    |------------|----------|
    | Длительность | ~2 часа |
    | Решений записано | 3 |
    | Файлов изменено | 8 |
    
    📁 Архивировано:
    - `session_history/session_2026-02-06_03-20.md`
    
    ⚖️ Записанные решения:
    | Решение | Описание |
    |---------|----------|
    | ADR-002 | REST API вместо GraphQL |
    
    📌 На следующий раз:
    | Приоритет | Задача |
    |-----------|--------|
    | 🔴 | Доделать авторизацию |
    
    👋 До встречи!
```

## Example (Language: English)

```
USER: /sleep

AI: 📝 Summarizing session...

    ✅ Session ended!
    
    📊 Today:
    | Metric | Value |
    |--------|-------|
    | Duration | ~2 hours |
    | Decisions recorded | 3 |
    | Files modified | 8 |
    
    📁 Archived to:
    - `session_history/session_2026-02-06_03-20.md`
    
    ⚖️ Recorded decisions:
    | Decision | Description |
    |----------|-------------|
    | ADR-002 | REST API over GraphQL |
    
    📌 For next session:
    | Priority | Task |
    |----------|------|
    | 🔴 | Complete authentication |
    
    👋 See you later!
```
