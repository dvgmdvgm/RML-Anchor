# 🧠 Advanced Memory System — Design Document

> **Author**: dvgmdvgm  
> **Last update**: 2026-02-05  

---

## 📋 Table of Contents

1. [Problems We Solve](#-problems-we-solve)
2. [Automatic Saving by Patterns](#-automatic-saving-by-patterns)
3. [TTL (Time-to-Live)](#-ttl-time-to-live)
4. [Importance Score](#-importance-score)
5. [Periodic Cleanup](#-periodic-cleanup)
6. [Summarization](#-summarization)
7. [Safe Removal and Backup](#-safe-removal-and-backup)
8. [How It All Works Together](#-how-it-all-works-together)

---

## 🎯 Problems We Solve

### Problem 1: Garbage Accumulation
**Symptom**: Over time, memory fills up with outdated, duplicate, or irrelevant data.

**Real example**: You recorded "We use React 17", then upgraded to React 18, but the old entry remained. AI might give outdated advice.

**Solution**: TTL + Importance Score + Periodic Cleanup

---

### Problem 2: Too Much Manual Work
**Symptom**: User gets tired of manually saving every important fact.

**Real example**: You made an ADR (architecture decision), but forgot `/remember`. A week later, AI doesn't know about this decision.

**Solution**: Automatic saving by patterns

---

### Problem 3: Fear of Deletion
**Symptom**: User is afraid to clean up memory because they might lose something important.

**Real example**: You want to delete old sessions but are afraid to accidentally delete an important ADR.

**Solution**: Summarization before deletion + Safe Backup

---

### Problem 4: Accidental System Deletion
**Symptom**: User accidentally deletes the entire memory system with one command.

**Solution**: Two-factor confirmation + Automatic backup to ZIP

---

## 🤖 Automatic Saving by Patterns

### Concept

Not everything needs to be asked of the user. Some things are **objectively important** and should be saved automatically.

### What is saved AUTOMATICALLY (without asking):

| Category | Trigger | Where it's saved |
|----------|---------|------------------|
| **ADR (Decisions)** | Phrases: "we decided", "chose", "will use" | `03_decisions/` |
| **Bugs and fixes** | Phrases: "bug", "fixed", "workaround", "hack" | `06_problems/` |
| **External APIs** | Discussion of API keys, endpoints, integrations | `09_external/` |
| **Architecture** | Discussion of patterns, components, data flow | `02_architecture/` |

### What is ASKED of the user:

| Category | Why we ask |
|----------|-----------|
| **Business logic** | Too subjective, what's important varies |
| **Code snippets** | May be temporary |
| **Session context** | Lots of noise, needs filtering |
| **Preferences** | Personal settings |

---

## ⏳ TTL (Time-to-Live)

### Concept

Every entry in memory has an "expiration date". Not for auto-deletion, but for **marking for review**.

### TTL Categories:

| Category | TTL | Reason |
|----------|-----|--------|
| `07_context/current_session.md` | 1 day | Only relevant today |
| `07_context/session_history/` | 30 days | History becomes outdated |
| `06_problems/workarounds/` | 90 days | Workarounds should become fixes |
| `03_decisions/` | 365 days | Decisions may need revisiting |
| `02_architecture/` | ∞ | Architecture rarely changes |

---

## ⭐ Importance Score

### Concept

Not all entries are equally important. Importance Score helps with:
- Cleanup (remove low score)
- Search (high score has priority)
- Summarization (low score gets compressed first)

### Formula:

```
Importance = Base × Recency × Access × Explicit

Where:
- Base = base category weight (ADR=0.9, session=0.3)
- Recency = 1 / (days since creation + 1)
- Access = log(access_count + 1) / 10
- Explicit = 1.5 if user explicitly marked as important
```

### Thresholds:

| Score | Status | Action |
|-------|--------|--------|
| > 0.7 | 🟢 Critical | Never delete |
| 0.4-0.7 | 🟡 Important | Summarize on cleanup |
| 0.2-0.4 | 🟠 Medium | Archive after TTL |
| < 0.2 | 🔴 Low | Candidate for deletion |

---

## 🧹 Periodic Cleanup

### Concept

Automatic cleanup runs:
1. **On `/wakeup`** — quick check
2. **On `/sleep`** — full check
3. **Manually** — `/anchor_cleanup`

### Cleanup Algorithm:

```
1. SCAN — Scan all entries
      ↓
2. SCORE — Calculate Importance
      ↓
3. TTL CHECK — Check expiration
      ↓
4. CATEGORIZE — Divide into groups:
   • KEEP — Keep
   • SUMMARIZE — Compress
   • ARCHIVE — Archive
   • DELETE — Delete
      ↓
5. CONFIRM — Show plan
      ↓
6. EXECUTE — Execute (with backup!)
```

---

## 📝 Summarization

### Concept

Instead of completely deleting old data — **compress into a summary**.

### Types of summarization:

| Type | When applied | Result |
|------|--------------|--------|
| **Session Merge** | Multiple sessions over a period | 1 file with key points |
| **Topic Compress** | Many entries on one topic | 1 structured file |
| **Archive Summary** | Before archiving | Metadata + 1 paragraph |

---

## 🔐 Safe Removal and Backup

### `/anchor_backup` — Manual backup

```
User: /anchor_backup
AI: 📦 Backup created: .agent/backups/anchor_backup_2026-02-05.zip
```

### `/anchor_remove` — Safe removal

```
User: /anchor_remove
AI: ⚠️ WARNING: This will remove the RLM-Anchor system!
    🛡️ Your project files and IDE configs will NOT be affected!
    
    To confirm, type this code: [a7x9K2mQ]
```

### `/anchor_restore` — Restore

```
User: /anchor_restore ./backup.zip
AI: ✅ Restored successfully!
```

---

## 🔄 How It All Works Together

### Entry Lifecycle:

```
CREATION
  Auto-save by pattern or manual /remember
         ↓
      LIFE
  On each access: access_count++
  Score is recalculated
         ↓
     AGING
  TTL expired?
  ├── Score > 0.7 → Auto-extend
  ├── Score 0.4-0.7 → Ask user
  └── Score < 0.4 → Summarize + Archive
         ↓
      CLEANUP
  Periodic Cleanup finds:
  • Duplicates → Merge
  • Low Score → Delete (with backup)
  • Many files on topic → Summarize
```

---

## 📊 Real Benefits

| Problem | Without this system | With this system |
|---------|---------------------|------------------|
| Forgot to save ADR | AI doesn't know about decision | Auto-save caught it |
| 100+ files in memory | Slow search, noise | Periodic cleanup |
| Outdated data | Incorrect AI advice | TTL + notifications |
| Afraid to clean memory | Garbage accumulates | Backup before deletion |
| Accidentally deleted system | Lost everything | Restore from ZIP |
| Moving to another PC | Manual copying | `/anchor_backup` + restore |

---

## ✅ Summary

This system transforms "naive" memory into a **self-maintaining knowledge base**:

- 🤖 **Automation** — important things save themselves
- ⏳ **Time management** — old data is compressed, not forgotten
- 🧹 **Cleanliness** — garbage is removed, but with backup
- 🔐 **Safety** — nothing is lost forever
- 📦 **Portability** — easy to transfer to another PC
