---
description: Runs intelligent cleanup of memory with TTL, importance scoring, and summarization.
---

# /anchor_cleanup — Intelligent Memory Cleanup

## Usage

```
/anchor_cleanup              # Full interactive cleanup (all 3 phases)
/anchor_cleanup sessions     # Phase 1 only — Session Merge
/anchor_cleanup topics       # Phase 2 only — Topic Compress
/anchor_cleanup --dry-run    # Show what would happen without doing it
```

## Purpose

Maintain a clean, efficient memory by:
- **Phase 1**: Merging old session files into monthly digests
- **Phase 2**: Compressing multiple files on the same topic into one
- **Phase 3**: Creating archive summaries before any deletion

---

## Execution Steps

### Step 1: Load Settings & Assess Health

```
Read .agent/memory/13_preferences/language_local.md (if exists, use it)
Otherwise read .agent/memory/13_preferences/language.md → use this language for output
Read .agent/memory/13_preferences/cleanup_settings.md → load TTL, thresholds
```

**Count and report:**

```
Count files in .agent/memory/07_context/session_history/
Count total .md files across categories 01-12
Count files in .agent/memory/archive/ (if exists)
```

Output health report:

```
🧹 MEMORY HEALTH ASSESSMENT
═══════════════════════════════

| Metric           | Value | Status |
|------------------|-------|--------|
| Session files    | N     | 🟢/🟡/🔴 |
| Total entries    | N     | 🟢/🟡/🔴 |
| Archive size     | N     | — |
| Memory age       | N days| — |

Phases to run:
  ✅ Phase 1: Session Merge (N session files found)
  ✅ Phase 2: Topic Compress (scanning...)
  ✅ Phase 3: Archive Summary (automatic)
```

---

### Step 2: Phase 1 — Session Merge

> [!NOTE]
> Triggers when session_history/ has > 30 files.
> If ≤ 30 files — skip this phase.

**2.1. Group sessions by month:**

```
List all files in .agent/memory/07_context/session_history/
Group by month: session_YYYY-MM-DD.md → group YYYY-MM
Ignore months with only 1-3 files (too few to merge)
```

**2.2. For each month with > 3 files:**

1. Read ALL session files for that month
2. Extract from each session:
   - Key decisions made
   - Main topics discussed
   - Problems found/solved
   - Tasks created/completed
3. Generate a monthly digest file

**Digest format:**

```markdown
# 📋 Digest: [Month Year]

> Auto-generated from N session files

## 🎯 Key Decisions
- [Decision 1]
- [Decision 2]

## 💬 Main Topics
- [Topic 1] (N sessions)
- [Topic 2] (N sessions)

## 🐛 Problems Solved
- [Problem 1] — [how solved]

## ⏳ Carried Over
- [Unfinished task 1]

## 📊 Statistics
| Metric | Value |
|--------|-------|
| Sessions | N |
| Decisions | N |
| Bugs fixed | N |

---
*Original files archived to: .agent/memory/archive/sessions/YYYY-MM/*
```

**2.3. Save and archive:**

1. Save digest as `session_history/digest_YYYY-MM.md`
2. Create folder `.agent/memory/archive/sessions/YYYY-MM/`
3. Move original session files to that archive folder
4. Add entry to `07_context/_index.md` → Archived Entries table

**2.4. Report:**

```
✅ Phase 1: Session Merge
| Month | Files merged | Before | After | Saved |
|-------|-------------|--------|-------|-------|
| Jan 2026 | 30 → 1 | 90 KB | 5 KB | 94% |
| Dec 2025 | 28 → 1 | 75 KB | 4 KB | 95% |
```

---

### Step 3: Phase 2 — Topic Compress

> [!NOTE]
> This phase is INTERACTIVE — always asks the user before merging.

**3.1. Scan for topic clusters:**

```
Read titles and tags of all files in categories:
  03_decisions/
  06_problems/
  06_problems/bugs/
  06_problems/workarounds/

Identify clusters: ≥ 3 files that share the same topic/keyword
```

**3.2. Present clusters to user:**

```
🔍 Topic Compress: found N clusters

1. [Topic Name] (N files, ~XX KB → ~X KB)
   - file1.md
   - file2.md
   - file3.md
   
2. [Topic Name] (N files, ~XX KB → ~X KB)
   - file1.md
   - file2.md
   - file3.md

Merge cluster #1? [y/N/all/skip]
  y    — merge this cluster
  N    — skip this cluster
  all  — merge all clusters
  skip — skip Phase 2 entirely
```

**3.3. For each approved cluster:**

1. Read all files in the cluster
2. Generate one comprehensive file with full chronology:
   - Initial problem/decision
   - Evolution over time
   - Current status
   - All related files referenced
3. Save merged file in the appropriate category
4. Move originals to `.agent/memory/archive/merged/[topic]/`
5. Update `_index.md` of the category

**3.4. Report:**

```
✅ Phase 2: Topic Compress
| Cluster | Files merged | Before | After | Saved |
|---------|-------------|--------|-------|-------|
| CORS issues | 3 → 1 | 25 KB | 8 KB | 68% |
```

---

### Step 4: Phase 3 — Archive Summary

> [!NOTE]
> This phase runs AUTOMATICALLY whenever any file is archived or deleted
> (during Phase 1, Phase 2, or manual deletion).

**For EVERY file moved to archive or deleted:**

1. Read the file content
2. Generate a one-line summary
3. Add a row to the `## 📦 Archived Entries` table in the corresponding `_index.md`

**Table format in _index.md:**

```markdown
## 📦 Archived Entries

| Original File | Summary | Archived |
|---------------|---------|----------|
| `PROB-002-memory-leak.md` | WebSocket memory leak, fixed in v1.3 | 2026-03-01 |
| `session_2026-01-*.md` | → `digest_2026-01.md` (30 sessions merged) | 2026-02-01 |
```

> [!IMPORTANT]
> This table is the "safety net" — even if the original file is gone,
> AI can see during /recall that knowledge existed and can restore
> from archive if needed.

---

### Step 5: TTL Expiration Check

```
For each file in categories 01-12:
  Calculate: days_since_created = today - file_creation_date
  Compare with: TTL from cleanup_settings.md for that category
```

**Categorize expired files:**

| Score | Action |
|-------|--------|
| TTL expired + still relevant | Extend TTL (ask user) |
| TTL expired + low relevance | Archive (with summary) |
| Empty file | Delete |
| Duplicate content | Merge with original |

**Present to user for confirmation:**

```
⏰ TTL Check: N files expired

| File | Category | Expired | Suggestion |
|------|----------|---------|------------|
| old-api-notes.md | 09_external | 15 days ago | Archive? |
| test-snippet.md | 05_code | 30 days ago | Delete (empty)? |

Action for each? [archive/delete/extend/skip]
```

---

### Step 5.5: Post-Cleanup Validation

> [!NOTE]
> Cleanup moves and archives files — this may desync _index.md.
> Quick validation ensures everything is still consistent.

```
Run quick sync validation (same as /anchor_validate --quick):
  Count content files on disk vs entries in _index.md
  If mismatch → auto-fix _index.md (remove ghost entries for archived files)
```

---

### Step 6: Final Report

```
✅ CLEANUP COMPLETE
═══════════════════════

📊 Results:
| Phase | Action | Files | Space saved |
|-------|--------|-------|-------------|
| Session Merge | 60 → 2 digests | 58 archived | ~170 KB |
| Topic Compress | 6 → 2 files | 4 archived | ~34 KB |
| TTL Expired | 3 archived, 1 deleted | 4 processed | ~8 KB |
| Archive Summary | 62 entries added to indexes | — | — |

Total space freed: ~212 KB
Archive location: .agent/memory/archive/

🧠 Memory is now clean and efficient!
```

---

## Archive Structure

```
.agent/memory/archive/
├── sessions/              ← Phase 1: merged sessions
│   ├── 2026-01/
│   │   ├── session_2026-01-01.md
│   │   ├── session_2026-01-02.md
│   │   └── ...
│   └── 2026-02/
├── merged/                ← Phase 2: topic-compressed files
│   └── cors-issues/
│       ├── PROB-001-cors.md
│       ├── PROB-004-cors-again.md
│       └── PROB-007-cors-preflight.md
└── expired/               ← Step 5: TTL-expired files
    └── 2026-03/
        └── old-api-notes.md
```

> [!NOTE]  
> The `archive/` folder is in `.gitignore` — never pushed to repo.
> Archives can be restored manually if needed.

---

## Safety Rules

1. **NEVER delete without backup** — all deleted files go to archive first
2. **NEVER auto-merge without asking** — Topic Compress always asks the user
3. **Session Merge is automatic** — but originals are preserved in archive
4. **Archive Summary is mandatory** — every archived file gets a one-line trace in _index.md
5. **Dry-run first** — when in doubt, use `--dry-run` flag

---

## Settings Reference

All thresholds and rules are configured in:
`.agent/memory/13_preferences/cleanup_settings.md`

Key settings:
- `TTL_BY_CATEGORY` — how long entries live per category
- `CLEANUP_TRIGGERS` — when to run checks (on_wakeup, on_sleep)
- `SUMMARIZATION` — digest format and merge rules
- `BACKUP` — backup location and retention

---

## Example Session

```
User: /anchor_cleanup

AI: 🧹 MEMORY HEALTH ASSESSMENT
    ═══════════════════════════
    
    | Metric        | Value | Status |
    |---------------|-------|--------|
    | Session files | 45    | 🟡     |
    | Total entries | 32    | 🟢     |
    
    Running Phase 1: Session Merge...
    Found 45 session files, grouping by month...
    
    ✅ Phase 1 complete:
    | Month    | Merged    | Saved |
    |----------|-----------|-------|
    | Jan 2026 | 30 → 1    | 94%   |
    | Dec 2025 | 15 → 1    | 91%   |
    
    Running Phase 2: Topic Compress...
    Found 1 cluster:
    
    1. CORS (3 files, ~25 KB → ~8 KB)
       - PROB-001-cors.md
       - PROB-004-cors-again.md
       - PROB-007-cors-preflight.md
    
    Merge? [y/N] 
    
User: y

AI: ✅ Merged into PROB-001-cors-complete.md
    
    Running Phase 3: Archive Summary...
    Added 48 entries to _index.md tables.
    
    ✅ CLEANUP COMPLETE
    Total space freed: ~204 KB
    🧠 Memory is clean!
```
