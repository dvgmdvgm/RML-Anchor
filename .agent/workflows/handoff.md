---
description: Create context handoff summary for switching between AI models
---

# /handoff — Model Handoff

## Usage

```
/handoff
```

---

## Purpose

Creates a compact context summary when switching between AI models (Claude → Gemini → GPT, etc.) to ensure continuity.

---

## Execution Steps

// turbo-all

### 1. Check Language Setting

```
Read .agent/memory/13_preferences/language.md
Output must be in configured language!
```

### 2. Gather Current Context

Read the following files:
- `.agent/memory/07_context/current_session.md`
- `.agent/memory/07_context/pending_tasks.md`
- Recent entries in `.agent/memory/03_decisions/`
- Recent entries in `.agent/memory/06_problems/`

### 3. Generate Handoff Summary

Create a compact summary following this format:

```markdown
# 🔄 Model Handoff Summary

> Generated: [DATE TIME]
> Language: [CONFIGURED LANGUAGE]

---

## 📍 Current State

**Project**: [Project name from 01_project if available]
**Working on**: [Current task/feature]
**Last action**: [What was just completed]
**Next step**: [Immediate next action]

---

## 📁 Key Files in Focus

| File | Context |
|------|---------|
| `file1.py` | [What was being done] |
| `file2.html` | [What was being done] |

---

## ⚖️ Recent Decisions (Last 3)

1. [Decision 1] — [Brief reason]
2. [Decision 2] — [Brief reason]
3. [Decision 3] — [Brief reason]

---

## ⚠️ Critical Notes

- [Important thing to remember]
- [Watch out for this]
- [User preference to follow]

---

## 📋 Pending Tasks

- [ ] [Task 1 - priority]
- [ ] [Task 2 - priority]

---

## 🎨 Style Reminders

- **Code**: See `.agent/memory/13_preferences/coding_style.md`
- **Communication**: See `.agent/memory/13_preferences/communication.md`
- **Language**: [CONFIGURED LANGUAGE] — ALL responses in this language!

---

## 🚀 Ready to Continue

The next AI model should:
1. Read this handoff summary
2. Review referenced preference files
3. Continue from [specific next step]
```

### 4. Save Handoff (Optional)

If user wants to save:
```
Write to .agent/memory/07_context/handoff_YYYY-MM-DD_HHMM.md
```

### 5. Display to User

Show the complete handoff summary so it can be:
- Copied to new session
- Referenced by new model
- Saved for later

---

## Example (Russian)

```
USER: /handoff

AI: # 🔄 Сводка для передачи контекста
    
    > Дата: 2026-02-05 15:30
    > Язык: Русский (ru)
    
    ---
    
    ## 📍 Текущее состояние
    
    **Проект**: AnchorGravity Memory System
    **Работаем над**: Системой передачи контекста между моделями
    **Последнее действие**: Создали файлы стиля кода
    **Следующий шаг**: Создать workflow для walkthrough
    
    ---
    
    ## 📁 Ключевые файлы
    
    | Файл | Контекст |
    |------|----------|
    | `coding_style.md` | Только что создан |
    | `communication.md` | Только что создан |
    
    ---
    
    ## ⚖️ Недавние решения
    
    1. AUTO_SAVE=ask — для качества данных RLM
    2. Мультиязычность — через language.md
    3. Команды /wakeup, /sleep вместо старых
    
    ---
    
    ## 🚀 Следующей модели:
    
    1. Прочитай эту сводку
    2. Проверь language.md (язык: ru)
    3. Продолжи создание /walkthrough workflow
```

---

## Notes

- Handoff should be **compact** — fits in one screen
- Always include **language reminder** — critical for consistency
- Reference **preference files** — new model should read them
