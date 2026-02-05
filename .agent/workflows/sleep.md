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

Create a brief session summary:
- Main discussion topics
- Decisions made
- Files created/modified
- Important notes

**Write in configured language!**

### 2. Save to Session History

```
Create file .agent/memory/07_context/session_history/YYYY-MM-DD.md
```

Format:

```markdown
# Session: YYYY-MM-DD

## 📋 Discussion Topics

1. Topic 1
2. Topic 2

## ⚖️ Decisions Made

| Decision | Description |
|----------|-------------|
| ... | ... |

## 📁 Modified Files

- `file1.py` — what changed
- `file2.html` — what changed

## 📝 Notes

- Note 1
- Note 2

## ⏳ Pending

- Task 1
- Task 2
```

### 3. Update pending_tasks.md

```
Update .agent/memory/07_context/pending_tasks.md
```

- Add new pending tasks
- Mark completed ones

### 4. Clear current_session.md

```
Update .agent/memory/07_context/current_session.md
```

Prepare for next session.

### 5. Update Relevant Indexes

If new entries were created in other categories — update their `_index.md`.

### 6. Confirm to User

Output in configured language:

```
✅ Session ended!

📊 Session Statistics:
- Duration: ~X hours
- Decisions recorded: N
- Problems documented: M

📁 Saved:
- memory/07_context/session_history/2026-02-05.md

📌 For next time:
- Task 1
- Task 2

👋 See you later!
```

---

## Example (Language: Russian)

```
USER: /sleep

AI: 📝 Суммаризирую сессию...

    ✅ Сессия завершена!
    
    📊 Сегодня мы:
    - Обсудили Context Window в LLM
    - Изучили RLM (Recursive Language Models)  
    - Создали систему памяти проекта
    
    📁 Сохранено:
    - memory/07_context/session_history/2026-02-05.md
    - 20+ файлов системы памяти
    
    ⚖️ Записано решение:
    - ADR-001: Создание RLM-подобной системы памяти
    
    📌 На следующий раз:
    - Протестировать систему памяти
    - Добавить Python скрипты
    
    👋 До встречи!
```

## Example (Language: Spanish)

```
USER: /sleep

AI: 📝 Resumiendo la sesión...

    ✅ ¡Sesión terminada!
    
    📊 Hoy hemos:
    - Discutido Context Window en LLM
    - Estudiado RLM (Recursive Language Models)  
    - Creado el sistema de memoria del proyecto
    
    📁 Guardado:
    - memory/07_context/session_history/2026-02-05.md
    
    📌 Para la próxima vez:
    - Probar el sistema de memoria
    
    👋 ¡Hasta luego!
```
