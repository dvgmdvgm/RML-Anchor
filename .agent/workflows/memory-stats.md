---
description: Show project memory system statistics
---

# /memory-stats — Memory Analytics Dashboard

## Usage

```
/memory-stats              # Full dashboard (state + trends + recommendations)
/memory-stats --short      # Current state only (no trends)
```

---

## Execution Steps

// turbo-all

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language_local.md (if exists, use it)
Otherwise read .agent/memory/13_preferences/language.md
All output must be in this language!
```

---

### 1. Section 1 — Current State

**1.1. Count files per category:**

```
For each category 01-13:
  List .md files (exclude _index.md, _template.md, README.md)
  Count files
  Get last modified date
  Get total size
```

**1.2. Output current state:**

```
📊 MEMORY DASHBOARD
═══════════════════════════════════

📁 Current State:

| # | Category | Files | Size | Last Updated |
|---|----------|-------|------|-------------|
| 01 | PROJECT | N | X KB | YYYY-MM-DD |
| 02 | ARCHITECTURE | N | X KB | YYYY-MM-DD |
| 03 | DECISIONS | N | X KB | YYYY-MM-DD |
| 04 | DOMAIN | N | X KB | YYYY-MM-DD |
| 05 | CODE | N | X KB | YYYY-MM-DD |
| 06 | PROBLEMS | N | X KB | YYYY-MM-DD |
| 07 | CONTEXT | N | X KB | YYYY-MM-DD |
| 08 | PEOPLE | N | X KB | YYYY-MM-DD |
| 09 | EXTERNAL | N | X KB | YYYY-MM-DD |
| 10 | TESTING | N | X KB | YYYY-MM-DD |
| 11 | DEPLOYMENT | N | X KB | YYYY-MM-DD |
| 12 | ROADMAP | N | X KB | YYYY-MM-DD |
| 13 | PREFERENCES | N | X KB | YYYY-MM-DD |
|    | **TOTAL** | **N** | **X KB** | |

Session files: N (in session_history/)
Archive size: N files (in archive/)
```

> [!NOTE]
> If `--short` flag is used, stop here. Don't show trends or recommendations.

---

### 2. Section 2 — Trends (from stats log)

**2.1. Read the stats log:**

```
Read .agent/memory/07_context/memory_stats_log.md
```

**2.2. If log has < 2 entries:**

```
📈 Trends: Not enough data yet (need at least 2 sessions).
   Trends will appear after a few /sleep cycles.
```

→ Skip to Section 3.

**2.3. If log has ≥ 2 entries — calculate trends:**

Compare **first row** vs **last row** in the log:

```
📈 Trends (over N days):

| Metric | Then | Now | Change | Pace |
|--------|------|-----|--------|------|
| Total entries | X | Y | +Z | ~N/day |
| Session files | X | Y | +Z | status |
| Total size | X KB | Y KB | +Z KB | ~N KB/day |
| Decisions | X | Y | +Z | — |
| Problems | X | Y | +Z | — |
```

**Status indicators:**
- Pace < 1/day → 🟢 Stable
- Pace 1-3/day → 🟡 Active
- Pace > 3/day → 🔺 Fast growth
- Session files > 30 → ⚠️ Cleanup recommended

**2.4. Show hottest and coldest categories:**

```
🔥 Most active categories (this period):
  1. 07_context (+N files)
  2. 06_problems (+N files)
  3. 03_decisions (+N files)

❄️ Empty categories (0 entries):
  - 04_domain
  - 10_testing
```

---

### 3. Section 3 — Smart Recommendations

**AI analyzes the data and generates relevant recommendations:**

Based on patterns, recommend actions:

| Pattern | Recommendation |
|---------|---------------|
| Session files > 30 | 🧹 "Run /anchor_cleanup to merge sessions" |
| Session files > 100 | 🔴 "Critical: /anchor_cleanup urgently needed" |
| Empty categories (01, 02) | 📝 "Document your project basics" |
| Empty categories (10, 11) | 📋 "Consider documenting test/deploy strategy" |
| Problems growing fast | 🔍 "Many bugs tracked. Consider /anchor_cleanup topics" |
| No cleanup in log (30+ days) | 🧹 "No cleanup in N days. Consider /anchor_cleanup" |
| Size > 500 KB | ⚠️ "Memory is large. Summarization recommended" |
| Size > 1 MB | 🔴 "Critical size. Immediate cleanup needed" |
| Log has < 5 entries | 💡 "Keep using /sleep to build trend data" |

```
💡 Recommendations:

🧹 Session history has 45 files — run /anchor_cleanup
📝 01_project and 02_architecture are empty — document basics
🔍 06_problems grew by 7 files this month — topic compression may help
📅 Estimated next cleanup needed: ~5 days (at current growth rate)

Overall health: 🟡 Good, but cleanup recommended
```

---

## Example

```
USER: /memory-stats

AI: 📊 MEMORY DASHBOARD
    ═══════════════════════════════════

    📁 Current State:
    | # | Category | Files | Size | Updated |
    |---|----------|-------|------|---------| 
    | 01 | PROJECT | 2 | 8 KB | 2026-02-05 |
    | 02 | ARCHITECTURE | 1 | 4 KB | 2026-02-03 |
    | 03 | DECISIONS | 5 | 22 KB | 2026-02-07 |
    | 04 | DOMAIN | 0 | — | — |
    | 05 | CODE | 3 | 12 KB | 2026-02-06 |
    | 06 | PROBLEMS | 8 | 35 KB | 2026-02-07 |
    | 07 | CONTEXT | 3 | 9 KB | 2026-02-07 |
    | 08 | PEOPLE | 1 | 2 KB | 2026-02-01 |
    | 09 | EXTERNAL | 2 | 7 KB | 2026-02-04 |
    | 10 | TESTING | 0 | — | — |
    | 11 | DEPLOYMENT | 0 | — | — |
    | 12 | ROADMAP | 2 | 6 KB | 2026-02-05 |
    | 13 | PREFERENCES | 8 | 28 KB | 2026-02-07 |
    |    | TOTAL | 35 | 133 KB | |

    Sessions: 28 | Archive: 0

    ═══════════════════════════════════

    📈 Trends (14 days):
    | Metric | Feb 1 | Now | Change | Pace |
    |--------|-------|-----|--------|------|
    | Entries | 12 | 35 | +23 | ~1.6/day 🟡 |
    | Sessions | 5 | 28 | +23 | ⚠️ cleanup |
    | Size | 45 KB | 133 KB | +88 KB | ~6 KB/day |
    | Decisions | 2 | 5 | +3 | — |
    | Problems | 1 | 8 | +7 | 🔺 active |

    🔥 Most active: 06_problems (+7), 07_context (+3)
    ❄️ Empty: 04_domain, 10_testing, 11_deployment

    ═══════════════════════════════════

    💡 Recommendations:
    🧹 28 session files — approaching cleanup threshold (30)
    📝 04_domain is empty — consider adding domain terms
    🔍 06_problems grew fast (+7) — topic compression may help
    📅 Next cleanup: ~2 days at current pace

    Overall: 🟡 Healthy, cleanup soon
```
