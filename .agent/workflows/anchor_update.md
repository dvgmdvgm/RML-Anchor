---
description: Update RLM-Anchor to the latest version from GitHub without losing user data.
---

# /anchor_update — Update RLM-Anchor

## Usage

```
/anchor_update                  # Interactive update
/anchor_update --check          # Check for updates only (no changes)
```

## Purpose

Safely update the RLM-Anchor system to the latest version from GitHub.
Preserves all user data, memory entries, session history, and language settings.

---

## File Classification

> [!IMPORTANT]
> The new version's file list acts as an implicit manifest.
> Only files that exist in the new version are subject to update.
> Custom user files (not in new version) are NEVER touched.

### 🟢 OVERWRITE — Safe to replace entirely

Product files that exist in **both** the new version AND the project:

```yaml
OVERWRITE:
  # Only files from the new version's .agent/ are candidates:
  - .agent/workflows/*.md                     # workflow files
  - .agent/scripts/*.py                       # scripts
  - .agent/MEMORY_INDEX.md                    # master index
  - .agent/VERSION                            # version file
  - .agent/memory/03_decisions/_template.md   # entry templates
  - .agent/memory/06_problems/_template.md
  - .agent/memory/06_problems/bugs/README.md
  - .agent/memory/06_problems/workarounds/README.md

  # RULE: If a file exists in the project's workflows/
  # but NOT in the new version → it's a custom user file → SKIP
```

### 🟡 SMART_MERGE — Update structure, keep user data

These files have both template structure AND user-created entries:

```yaml
SMART_MERGE:
  # Category indexes (user entries in file tables)
  - .agent/memory/01_project/_index.md
  - .agent/memory/02_architecture/_index.md
  - .agent/memory/03_decisions/_index.md
  - .agent/memory/04_domain/_index.md
  - .agent/memory/05_code/_index.md
  - .agent/memory/06_problems/_index.md
  - .agent/memory/07_context/_index.md
  - .agent/memory/08_people/_index.md
  - .agent/memory/09_external/_index.md
  - .agent/memory/10_testing/_index.md
  - .agent/memory/11_deployment/_index.md
  - .agent/memory/12_roadmap/_index.md
  - .agent/memory/13_preferences/_index.md

  # Preference files (user may have customized values)
  - .agent/memory/13_preferences/cleanup_settings.md
  - .agent/memory/13_preferences/auto_save_rules.md
  - .agent/memory/13_preferences/memory_settings.md
  - .agent/memory/13_preferences/communication.md
  - .agent/memory/13_preferences/coding_style.md
  - .agent/memory/13_preferences/response_templates.md
```

### 🔴 NEVER_TOUCH — User data, never overwrite

```yaml
NEVER_TOUCH:
  - .agent/memory/13_preferences/language.md        # user's language choice
  - .agent/memory/13_preferences/linked_projects.md  # user's project links
  - .agent/memory/07_context/session_history/*       # session history
  - .agent/memory/07_context/memory_stats_log.md     # stats log
  - .agent/memory/07_context/current_session.md      # current session
  - .agent/memory/07_context/pending_tasks.md        # pending tasks
  - .agent/memory/archive/*                          # archived files
  - Any user-created .md files in categories 01-12   # memory entries
  - Any file in project's workflows/ NOT in new version  # custom workflows
```

---

## Execution Steps

### Step 1: Check Current Version

```
Read .agent/VERSION
If file doesn't exist → assume version 1.0.0
Display current version
```

### Step 2: Download Latest Version

```
Create temp directory (e.g., /tmp/anchor_update/)
Clone the latest version:
  git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git /tmp/anchor_update/
Read /tmp/anchor_update/.agent/VERSION → latest version
```

**If current version = latest version:**
```
✅ Already up to date (version X.Y.Z)
```
→ Clean up temp dir and stop.

**If --check flag:**
```
📦 Update available: X.Y.Z → A.B.C
   Run /anchor_update to apply
```
→ Clean up temp dir and stop.

### Step 3: Read User's Language

```
Read .agent/memory/13_preferences/language.md
Extract LANGUAGE= value
All new files will be translated to this language after update
```

### Step 4: Create Backup

```
Create backup of current .agent/ folder:
  Copy .agent/ → .agent/backups/pre_update_vX.Y.Z_YYYY-MM-DD/
```

> [!CAUTION]
> ALWAYS backup before updating. If something goes wrong,
> user can restore from this backup.

### Step 5: Apply OVERWRITE Files

```
For each OVERWRITE-type file in the NEW version:
  If file also exists in the project → overwrite it
  If file does NOT exist in project → create it (ADD_NEW)
  
For each file in project's workflows/ NOT in the new version:
  → SKIP (this is a custom user workflow, do not touch)
```

Report:
```
🟢 Overwritten: N files
  - workflows/recall.md (updated)
  - workflows/anchor_validate.md (updated)
  - MEMORY_INDEX.md (updated)

🆕 New files: N
  - workflows/new_feature.md (added)

🔒 Custom (untouched): N
  - workflows/deploy.md (user's custom workflow)
```

### Step 6: Apply SMART_MERGE Files

**For each _index.md file:**

1. Read the OLD file (current project)
2. Read the NEW file (from update)
3. Extract user data from OLD file:
   - All rows in `## 📁 Files in This Category` table (except header/separator)
   - All rows in `## 📦 Archived Entries` table (except header/separator)
   - Any user-added sections
4. Take the NEW template structure (headings, descriptions, hints)
5. Insert user data back into the new structure
6. Write the merged result

**For each preferences file (cleanup_settings.md, etc.):**

1. Read the OLD file (user's customized values)
2. Read the NEW file (may have new settings added)
3. Keep all user's existing values
4. Add any NEW settings from update (with default values)
5. Write the merged result

Report:
```
🟡 Merged: N files
  - 06_problems/_index.md (kept 5 user entries, updated structure)
  - 13_preferences/cleanup_settings.md (added 2 new settings)
```

### Step 7: Apply ADD_NEW Files

```
For each file in new version that doesn't exist in project:
  Copy to project
  Mark for translation
```

Report:
```
🆕 New files: N
  - workflows/anchor_update.md
  - memory/13_preferences/linked_projects.md
```

### Step 8: Translate New/Updated Files

```
If LANGUAGE ≠ "en":
  For each OVERWRITE and ADD_NEW file that is in the translation list:
    Read its content
    Translate to user's language
    Write back
```

> [!NOTE]
> Uses the same translation rules as anchor_agent.md Step 1.
> Only translates files from the translation list (26 files).
> Workflow files are NOT translated (they are AI instructions, always English).

### Step 9: Update Version

```
Write new version to .agent/VERSION
```

### Step 10: Cleanup & Report

```
Delete temp directory (/tmp/anchor_update/)
```

**Final report:**

```
✅ ANCHOR UPDATE COMPLETE: vX.Y.Z → vA.B.C
═══════════════════════════════════════════

📦 Changes applied:
| Action | Files | Details |
|--------|-------|---------|
| 🟢 Overwritten | N | workflows, scripts, templates |
| 🟡 Merged | N | indexes (kept M user entries) |
| 🆕 Added | N | new files |
| 🔒 Custom | N | user workflows (untouched) |
| 🌐 Translated | N | to [language] |
| 🔴 Skipped | N | user data (untouched) |

💾 Backup: .agent/backups/pre_update_vX.Y.Z_YYYY-MM-DD/

📋 What's new in vA.B.C:
  - [AI reads CHANGELOG or commit messages and summarizes]

⚠️ If anything looks wrong, restore from backup:
   /anchor_restore .agent/backups/pre_update_vX.Y.Z_YYYY-MM-DD/
```

---

## Smart Merge Algorithm (detailed)

### For _index.md files:

```
OLD _index.md:                          NEW _index.md (from update):
┌──────────────────────┐                ┌──────────────────────┐
│ # PROBLEMS (old h1)  │  ← replace    │ # PROBLEMS (new h1)  │
│                      │               │                      │
│ ## Description       │  ← replace    │ ## Description (new) │
│ Old description...   │               │ Better description..│
│                      │               │                      │
│ ## Files             │  ← keep hdr   │ ## Files             │
│ | PROB-001 | cors |  │  ← KEEP!     │ | (empty template)   │
│ | PROB-002 | mem  |  │  ← KEEP!     │                      │
│                      │               │ ## 📦 Archived       │ ← NEW section!
│ ## When to Access    │  ← replace    │ (new in this version)│
│ Old hints...         │               │                      │
│                      │               │ ## When to Access    │
│                      │               │ New hints...         │
└──────────────────────┘                └──────────────────────┘

RESULT:
┌──────────────────────┐
│ # PROBLEMS (new h1)  │ ← from NEW
│                      │
│ ## Description (new) │ ← from NEW
│ Better description..│
│                      │
│ ## Files             │ ← header from NEW
│ | PROB-001 | cors |  │ ← DATA from OLD
│ | PROB-002 | mem  |  │ ← DATA from OLD
│                      │
│ ## 📦 Archived       │ ← NEW section (added!)
│ (empty)              │
│                      │
│ ## When to Access    │ ← from NEW
│ New hints...         │
└──────────────────────┘
```

### For preference files:

```
OLD cleanup_settings.md:                NEW cleanup_settings.md:
┌──────────────────────┐                ┌──────────────────────┐
│ TTL_DEFAULT: 90      │  ← user set   │ TTL_DEFAULT: 180     │ ← new default
│ MAX_FILES: 50        │  ← user set   │ MAX_FILES: 100       │ ← new default
│                      │               │ SESSION_MERGE: 30    │ ← NEW setting!
│                      │               │ TOPIC_THRESHOLD: 3   │ ← NEW setting!
└──────────────────────┘                └──────────────────────┘

RESULT:
┌──────────────────────┐
│ TTL_DEFAULT: 90      │ ← KEPT user's value
│ MAX_FILES: 50        │ ← KEPT user's value
│ SESSION_MERGE: 30    │ ← ADDED from new (default)
│ TOPIC_THRESHOLD: 3   │ ← ADDED from new (default)
└──────────────────────┘
```

---

## Safety Rules

1. **ALWAYS backup before update** — no exceptions
2. **NEVER overwrite user data files** — follow NEVER_TOUCH list exactly
3. **NEVER touch custom workflows** — files not in new version are user's own
4. **User entries in _index.md are sacred** — merge, not replace
5. **User preference values are sacred** — add new settings, keep existing values
6. **Translate after update** — ensure all user-facing text matches language
7. **Version check first** — don't update if already on latest
8. **Backup path in report** — so user knows where to restore from
