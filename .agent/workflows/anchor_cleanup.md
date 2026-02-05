---
description: Runs intelligent cleanup of memory with TTL, importance scoring, and summarization.
---

# /anchor_cleanup — Intelligent Memory Cleanup

## Usage

```
/anchor_cleanup           # Interactive cleanup
/anchor_cleanup --dry-run # Show what would happen without doing it
/anchor_cleanup --auto    # Auto-approve low-risk actions
```

## Purpose

Maintain a clean, efficient memory by:
- Removing expired entries (TTL)
- Archiving low-importance data
- Summarizing old session history
- Merging duplicates
- Deleting empty files

---

## Execution Steps

### Step 1: Load Settings

Read cleanup settings from:
`.agent/memory/13_preferences/cleanup_settings.md`

### Step 2: Scan Memory

```markdown
🔍 **Scanning Memory...**

Analyzing files in .agent/memory/...
```

Scan all files and collect metadata:
- Created date
- Last modified date
- Last accessed date (from metadata if available)
- File size
- Category
- Access count (from metadata)

### Step 3: Calculate Scores

For each file, calculate:

```
TTL_Status = (today - created_date) > category_ttl ? EXPIRED : OK

Importance = BASE_WEIGHT[category] 
           × RECENCY_FACTOR 
           × ACCESS_FACTOR 
           × EXPLICIT_BOOST

Where:
- RECENCY_FACTOR = 1 / (days_since_creation + 1)
- ACCESS_FACTOR = log(access_count + 1) / 10
- EXPLICIT_BOOST = 1.5 if marked important, else 1.0
```

### Step 4: Categorize Files

Sort files into action categories:

| Category | Criteria | Action |
|----------|----------|--------|
| 🟢 KEEP | Score > 0.7 OR TTL OK | Do nothing |
| 🟡 REVIEW | Score 0.4-0.7 AND TTL expired | Ask user |
| 🟠 SUMMARIZE | Multiple old sessions | Merge into summary |
| 🔴 ARCHIVE | Score 0.2-0.4 | Move to archive |
| ⚫ DELETE | Score < 0.2 OR empty | Delete (with backup) |

### Step 5: Show Report

```markdown
🧹 **CLEANUP ANALYSIS REPORT**

📊 Scanned: 47 files across 13 categories

---

## 🟢 KEEP (23 files) — No action needed

| File | Score | TTL Status |
|------|-------|------------|
| 03_decisions/ADR-001-database.md | 0.89 | ✅ 335 days left |
| 02_architecture/overview.md | 0.76 | ✅ Never expires |
| ... | | |

---

## 🟡 REVIEW (5 files) — Your decision needed

| File | Score | TTL Status | Suggestion |
|------|-------|------------|------------|
| 06_problems/old-auth-bug.md | 0.52 | ⚠️ Expired 10 days ago | Archive or extend? |
| 09_external/legacy-api.md | 0.45 | ⚠️ Expired 5 days ago | Still using this API? |

---

## 🟠 SUMMARIZE (8 files → 1 file)

Session history from January 2026:
- 07_context/session_history/2026-01-01.md
- 07_context/session_history/2026-01-02.md
- ... (6 more)

**Will create**: `07_context/session_history/2026-01_summary.md`

---

## 🔴 ARCHIVE (4 files)

Low importance, moving to `.agent/archive/`:
| File | Score | Reason |
|------|-------|--------|
| 07_context/session_history/2025-12-*.md | 0.15 | Very old |

---

## ⚫ DELETE (3 files)

| File | Reason |
|------|--------|
| 07_context/temp_notes.md | Empty file |
| 05_code/duplicate_snippet.md | Duplicate of snippet.md |
| 06_problems/test.md | Score 0.02, never accessed |

---

## 📊 Summary

| Action | Files | Space freed |
|--------|-------|-------------|
| Keep | 23 | - |
| Review | 5 | - |
| Summarize | 8 → 1 | ~45 KB |
| Archive | 4 | ~12 KB |
| Delete | 3 | ~3 KB |

**Total space to be freed**: ~60 KB

---

Proceed with cleanup? [y/N/review]
- **y** — Execute all actions
- **N** — Cancel
- **review** — Go through REVIEW items one by one
```

### Step 6: Execute Actions

Based on user choice:

#### For SUMMARIZE:
```python
# Combine multiple session files into one summary
summary = generate_session_summary(files)
write_file(summary_path, summary)
for file in files:
    move_to_archive(file)
```

#### For ARCHIVE:
```python
# Move to archive folder
archive_path = ".agent/archive/{date}/"
for file in archive_files:
    move(file, archive_path)
```

#### For DELETE:
```python
# Backup before delete
backup_deleted_files(delete_files)
for file in delete_files:
    delete(file)
```

### Step 7: Report Results

```markdown
✅ **Cleanup Completed**

| Action | Files | Status |
|--------|-------|--------|
| Summarized | 8 → 1 | ✅ |
| Archived | 4 | ✅ |
| Deleted | 3 | ✅ |

📦 Deleted files backed up to: `.agent/backups/cleanup_backup_2026-02-05.zip`

🧠 Memory is now cleaner and more efficient!
```

---

## Summarization Algorithm

When summarizing session history:

```markdown
# 📅 January 2026 — Session Summary

> Auto-generated from 8 session files

## 🎯 Key Topics Discussed

1. PostgreSQL setup and optimization
2. Auth module refactoring
3. API integration with Stripe

## 💡 Decisions Made

- ADR-005: JWT tokens for auth
- ADR-006: Redis for caching

## 🐛 Problems Solved

- Fixed session timeout bug
- Workaround for Safari CORS issue

## ⏳ Carried Over

- Query optimization (pending)
- Mobile responsive design (pending)

---

*Original files archived to: .agent/archive/2026-01/*
```

---

## Settings Reference

Edit `.agent/memory/13_preferences/cleanup_settings.md` to customize:

- TTL per category
- Importance score weights
- Action thresholds
- Summarization settings

---

## Example Session

```
User: /anchor_cleanup --dry-run

AI: 🔍 Scanning memory...
    
    📊 DRY RUN — No changes will be made
    
    Would summarize: 8 session files → 1 summary
    Would archive: 4 low-score files
    Would delete: 3 empty/duplicate files
    
    Run without --dry-run to execute.

User: /anchor_cleanup

AI: 🧹 CLEANUP ANALYSIS REPORT
    [... detailed report ...]
    
    Proceed? [y/N/review]
    
User: y

AI: ✅ Cleanup completed!
    Summarized: 8 → 1
    Archived: 4
    Deleted: 3
    
    Backup saved: cleanup_backup_2026-02-05.zip
```
