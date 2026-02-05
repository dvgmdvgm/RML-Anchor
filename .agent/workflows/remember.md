---
description: Save information to project memory system
---

# /remember — Save to Memory

## Usage

```
/remember [category] [information]
```

or simply

```
/remember
```

(AI will determine category automatically)

---

## Execution Steps

// turbo-all

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language.md
All saved entries must be written in this language!
```

### 1. Determine Category

If category not specified, determine by context:

| Context | Category |
|---------|----------|
| Architecture decision, tech choice | `03_decisions` |
| Solved bug, workaround | `06_problems` |
| New component, function, class | `05_code` |
| External API, integration | `09_external` |
| Plan, idea, TODO | `12_roadmap` |
| User preference | `13_preferences` |
| Other | ask user |

### 2. Read Category Index

```
Read .agent/memory/[category]/_index.md
```

### 3. Determine File

- If information relates to existing file → update it
- If new topic → create new file

### 4. Create/Update Entry

Use template from `_template.md` if available, or standard format.

**IMPORTANT: Write content in the configured language!**

```markdown
# [Title - in configured language]

- **Date**: YYYY-MM-DD
- **Tags**: tag1, tag2

---

## Content

[Information - in configured language]
```

### 5. Update Category Index

Add new file to `_index.md` table.

### 6. Confirm to User

Output in configured language:

```
✅ Saved to memory/[category]/[file].md
```

---

## Examples

### Example 1: Explicit Category (Russian)

```
USER: /remember decisions мы выбрали PostgreSQL потому что нужны транзакции

AI: Создаю ADR-001-database-choice.md...
    ✅ Записано в memory/03_decisions/ADR-001-database-choice.md
```

### Example 2: Auto-detection (English)

```
USER: /remember fixed authentication bug, the problem was wrong redirect_uri

AI: Determining category... → problems
    Creating PROB-001-auth-redirect.md...
    ✅ Saved to memory/06_problems/PROB-001-auth-redirect.md
```

### Example 3: Without Parameters (Spanish)

```
USER: Decidimos usar Celery para tareas en segundo plano

AI: [notices important decision]
    ¿Quieres que guarde esta decisión en la memoria?
    
USER: sí

AI: ✅ Guardado en memory/03_decisions/ADR-002-celery.md
```
