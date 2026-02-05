---
description: Show project memory system statistics
---

# /memory-stats — Memory Statistics

## Usage

```
/memory-stats
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

### 2. Collect Category Statistics

For each category:

```
Read .agent/memory/[category]/_index.md
Count number of entries
```

### 3. Output Report

In configured language:

```
📊 PROJECT MEMORY STATISTICS
═══════════════════════════════════════

📁 Categories:

| # | Category | Entries | Last Updated |
|---|----------|---------|--------------|
| 01 | PROJECT | N | YYYY-MM-DD |
| 02 | ARCHITECTURE | N | YYYY-MM-DD |
| ... | ... | ... | ... |

═══════════════════════════════════════

📈 Total Statistics:
- Total categories: 13
- Total entries: N
- First entry: YYYY-MM-DD
- Last updated: YYYY-MM-DD

💾 Memory size: ~X KB

═══════════════════════════════════════

📌 Recommendations:
- [If few entries] Try recording more decisions
- [If no context] Use /sleep to summarize
- [If no preferences] Tell about your preferences
```

---

## Example (English)

```
USER: /memory-stats

AI: 📊 PROJECT MEMORY STATISTICS
    ═══════════════════════════════════════
    
    📁 Categories:
    
    | # | Category | Entries | Updated |
    |---|----------|---------|---------|
    | 01 | PROJECT | 0 | — |
    | 02 | ARCHITECTURE | 0 | — |
    | 03 | DECISIONS | 2 | 2026-02-05 |
    | 04 | DOMAIN | 1 | 2026-02-04 |
    | 05 | CODE | 3 | 2026-02-05 |
    | 06 | PROBLEMS | 5 | 2026-02-05 |
    | 07 | CONTEXT | 3 | 2026-02-05 |
    | 08 | PEOPLE | 0 | — |
    | 09 | EXTERNAL | 1 | 2026-02-03 |
    | 10 | TESTING | 0 | — |
    | 11 | DEPLOYMENT | 0 | — |
    | 12 | ROADMAP | 2 | 2026-02-05 |
    | 13 | PREFERENCES | 1 | 2026-02-05 |
    
    ═══════════════════════════════════════
    
    📈 Total: 18 entries
    💾 Size: ~45 KB
    
    📌 Recommendations:
    - Add project information (01_project is empty)
    - Describe architecture (02_architecture is empty)
    - Set up deployment documentation
```

## Example (Russian)

```
USER: /memory-stats

AI: 📊 СТАТИСТИКА ПАМЯТИ ПРОЕКТА
    ═══════════════════════════════════════
    
    📁 Категории:
    
    | # | Категория | Записей | Обновлено |
    |---|-----------|---------|-----------|
    | 01 | PROJECT | 0 | — |
    ...
    
    📈 Итого: 18 записей
    💾 Размер: ~45 KB
    
    📌 Рекомендации:
    - Добавь информацию о проекте (01_project пуст)
```
