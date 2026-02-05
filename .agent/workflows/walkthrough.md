---
description: Generate walkthrough documentation after implementing features
---

# /walkthrough — Feature Documentation

## Usage

```
/walkthrough [feature_name]
```

or after completing work:

```
/walkthrough
```

---

## Purpose

Generates comprehensive documentation after implementing a feature, fixing a bug, or completing significant work. Creates a user-friendly guide showing what was done and how to use it.

---

## Execution Steps

// turbo-all

### 0. Check Language Setting — CRITICAL!

```
Read .agent/memory/13_preferences/language.md
ENTIRE walkthrough must be in configured language!
```

### 1. Gather Implementation Context

Collect information about:
- Files created/modified
- Features implemented
- Problems solved
- Code patterns used

### 2. Generate Walkthrough Document

Create documentation following this format:

```markdown
# 📖 Walkthrough: [Feature Name]

> **Date**: YYYY-MM-DD
> **Status**: ✅ Completed
> **Language**: [Configured Language]

---

## 🎯 Overview

[2-3 sentences describing what was built and why]

---

## 📁 Files Changed

| File | Action | Description |
|------|--------|-------------|
| `file1.py` | Created | [What it does] |
| `file2.html` | Modified | [What changed] |
| `file3.css` | Modified | [What changed] |

---

## 🔧 How It Works

### [Component 1]
[Explanation with code snippets]

```python
# Example code
def example():
    pass
```

### [Component 2]
[Explanation]

---

## 📝 Usage Examples

### Example 1: [Use Case]
```
[Code or command example]
```

### Example 2: [Use Case]
```
[Code or command example]
```

---

## ⚙️ Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| `OPTION_1` | `value` | What it controls |

---

## ⚠️ Known Limitations

- [Limitation 1]
- [Limitation 2]

---

## 🔗 Related Files

- `related_file.md` — [Why related]
- `another_file.py` — [Why related]

---

## 📚 Next Steps

- [ ] [Suggested improvement 1]
- [ ] [Suggested improvement 2]
```

### 3. Save Walkthrough

Save to appropriate location:

**Option A**: Project artifacts folder
```
.agent/brain/walkthrough_[feature].md
```

**Option B**: Memory context
```
.agent/memory/07_context/walkthroughs/YYYY-MM-DD_[feature].md
```

### 4. Update Memory Index

If saving to memory, update relevant `_index.md` files.

### 5. Confirm to User

Output in configured language:
```
✅ Walkthrough created!

📁 Saved to: [path]

[Display summary or full walkthrough]
```

---

## Example (Russian)

```
USER: /walkthrough Система памяти

AI: # 📖 Walkthrough: Система памяти RLM
    
    > **Дата**: 2026-02-05
    > **Статус**: ✅ Завершено
    
    ---
    
    ## 🎯 Обзор
    
    Создана персистентная система памяти для AI-ассистента на 
    основе принципов RLM. Позволяет сохранять знания между 
    сессиями и обеспечивает контекст для работы.
    
    ---
    
    ## 📁 Созданные файлы
    
    | Файл | Описание |
    |------|----------|
    | `MEMORY_INDEX.md` | Главный индекс памяти |
    | `MEMORY_SKILL.md` | Инструкции для AI |
    | `language.md` | Настройки языка |
    | `/wakeup`, `/sleep` | Workflows |
    
    ---
    
    ## 🔧 Как это работает
    
    ### Принцип RLM
    ```
    Запрос → Examine → Decompose → Recurse → Aggregate → Ответ
    ```
    
    ---
    
    ## 📝 Использование
    
    ### Начать сессию
    ```
    /wakeup
    ```
    
    ### Запомнить информацию
    ```
    /remember мы выбрали PostgreSQL
    ```
    
    ---
    
    ✅ Walkthrough сохранён в memory/07_context/walkthroughs/
```

---

## Example (English)

```
USER: /walkthrough Memory System

AI: # 📖 Walkthrough: RLM Memory System
    
    > **Date**: 2026-02-05
    > **Status**: ✅ Completed
    
    ---
    
    ## 🎯 Overview
    
    Created a persistent memory system for AI assistant based 
    on RLM principles. Enables knowledge preservation between
    sessions and provides context for work.
    
    [... rest in English ...]
```

---

## Auto-Trigger

AI should **offer** to generate walkthrough when:
- Major feature completed
- Bug fixed with significant changes
- User explicitly asks "what did we do?"
- Session ends with substantial work done

**Prompt**:
```
Would you like me to generate a walkthrough for this implementation?
Хочешь, чтобы я создал walkthrough для этой реализации?
```

---

## Notes

- **Always** check language first
- Keep explanations **clear** for future reference  
- Include **code examples** where relevant
- Link to **related files** for context
