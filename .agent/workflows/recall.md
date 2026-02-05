---
description: Find and recall information from project memory
---

# /recall — Recall from Memory

## Usage

```
/recall [query]
```

---

## Execution Steps

// turbo-all

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language.md
All output must be in this language!
```

### 1. Read Main Index

```
Read .agent/MEMORY_INDEX.md
```

### 2. Determine Relevant Categories

By query keywords, determine where to search:

| Keywords | Categories |
|----------|------------|
| decision, choice, why | `03_decisions` |
| bug, error, problem, fix | `06_problems` |
| architecture, structure, pattern | `02_architecture` |
| function, class, API | `05_code` |
| term, definition, glossary | `04_domain` |
| plan, roadmap, TODO | `12_roadmap` |
| discussed, last time | `07_context` |

### 3. Read Category Indexes

```
For each relevant category:
  Read .agent/memory/[category]/_index.md
```

### 4. Find Relevant Files

By descriptions in index, determine which specific files to read.

### 5. Extract Information

```
Read found files
Extract relevant sections
```

### 6. Form Response

Response should (in configured language):
- Contain found information
- Reference sources
- Indicate entry date (if available)

---

## Response Format

```
📁 Found in memory:

**Source**: `memory/03_decisions/ADR-001-database.md`
**Date**: 2026-01-15

> [Quote from file]

---

[Synthesized answer based on findings]
```

---

## Examples

### Example 1: Finding Decision (Russian)

```
USER: /recall почему выбрали PostgreSQL?

AI: 📁 Найдено в памяти:

    **Источник**: `memory/03_decisions/ADR-001-database-choice.md`
    **Дата**: 2026-01-15
    
    Мы выбрали PostgreSQL по следующим причинам:
    1. Нужны сложные JOIN запросы
    2. ACID транзакции для системы платежей
    3. Опыт команды с PostgreSQL
    
    Рассматривались также: MongoDB (отклонено из-за отсутствия транзакций)
```

### Example 2: Finding Problem Solution (English)

```
USER: /recall how did we fix Google authentication issue?

AI: 📁 Found in memory:

    **Source**: `memory/06_problems/PROB-005-google-auth.md`
    **Date**: 2026-01-20
    
    Problem: redirect_uri was using http instead of https
    Solution: Changed URI in Google Cloud Console
    Files: settings.py, config.py
```

### Example 3: Nothing Found (Spanish)

```
USER: /recall configuración de CI/CD

AI: 🔍 Buscando en memoria...
    
    ❌ No se encontró información sobre CI/CD en la memoria.
    
    Tal vez deberías:
    - Revisar `memory/11_deployment/` manualmente
    - Guardar esta información: /remember
```
