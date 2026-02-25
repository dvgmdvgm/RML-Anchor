---
description: Update RLM-Anchor to the latest version from GitHub without losing user data.
---

# /anchor_update — Update RLM-Anchor

## Usage

```
/anchor_update             # Interactive update
/anchor_update --check     # Check only (no changes)
```

> [!CAUTION]
> **Recommended order: `/sleep` → `/anchor_update` → (new chat) → `/wakeup`**
> Running during an active session is NOT recommended — AI has old instructions in context.

---

## File Classification

> [!IMPORTANT]
> Only files present in the new version are candidates for update.
> Custom user files (not in new version) are NEVER touched.

### 🟢 OVERWRITE — Replace entirely

```yaml
OVERWRITE:
  - .agent/workflows/*.md
  - .agent/scripts/*.py
  - .agent/MEMORY_INDEX.md
  - .agent/VERSION
  - .agent/memory/03_decisions/_template.md
  - .agent/memory/06_problems/_template.md
  - .agent/memory/06_problems/bugs/README.md
  - .agent/memory/06_problems/workarounds/README.md
  - .github/prompts/*.prompt.md            # Copilot Chat prompt files
  # Files in project's workflows/ NOT in new version → SKIP (custom)
```

### 🟡 SMART_MERGE — Update structure, keep user data

```yaml
SMART_MERGE:
  - .agent/memory/*/_index.md          # all 13 category indexes
  - .agent/memory/13_preferences/*.md  # preference files (keep user values)
  - .cursorrules                       # keep CUSTOM PROJECT RULES section
  - CLAUDE.md                          # keep CUSTOM PROJECT RULES section
  - GEMINI.md                          # keep CUSTOM PROJECT RULES section
  - .github/copilot-instructions.md    # keep CUSTOM PROJECT RULES section
```

### 🔴 NEVER_TOUCH — User data

```yaml
NEVER_TOUCH:
  - .agent/memory/13_preferences/language.md
  - .agent/memory/13_preferences/language_local.md
  - .agent/memory/13_preferences/linked_projects.md
  - .agent/memory/07_context/session_history/*
  - .agent/memory/07_context/memory_stats_log.md
  - .agent/memory/07_context/current_session.md
  - .agent/memory/07_context/pending_tasks.md
  - User-created .md files in categories 01-12
  - Custom workflows not in new version
```

---

## Execution Steps

### 1. Check Version

```
Read .agent/VERSION (if missing → assume 1.0.0)
```

### 2. Download Latest

```
Clone: git clone --depth 1 https://github.com/dvgmdvgm/RML-Anchor.git /tmp/anchor_update/
Read /tmp/anchor_update/.agent/VERSION → compare
If same version → "✅ Already up to date" → stop
If --check → "📦 Update available: X → Y" → stop
```

### 3. Read Language

```
Read language_local.md (or language.md) → LANGUAGE value
```

### 4. Create Backup

```
Copy .agent/ → .agent/backups/pre_update_vX.Y.Z_YYYY-MM-DD/
```

### 5. Apply OVERWRITE

Replace each OVERWRITE file from new version. New files not in project → create. Custom files not in new version → skip.

### 6. Apply SMART_MERGE

**For _index.md files:**
1. Extract user data rows from OLD file tables
2. Take NEW template structure
3. Insert user data back → write merged result

**For preference files:**
1. Keep all user's existing values
2. Add any NEW settings with defaults

**For .cursorrules / CLAUDE.md / GEMINI.md / .github/copilot-instructions.md:**
1. Extract CUSTOM PROJECT RULES section from OLD file
2. Take NEW routing engine
3. Insert user's CUSTOM RULES back → write merged result

### 7. Translate (if needed)

If LANGUAGE ≠ "en": translate all user-facing .md files (indexes, templates, preferences). Keep structure, emoji, paths, YAML keys unchanged. Do NOT translate workflow files or user data.

### 8. Update Version & Cleanup

```
Write new version → .agent/VERSION
Delete /tmp/anchor_update/
```

### 9. Report

```
✅ UPDATE COMPLETE: vX.Y.Z → vA.B.C

| Action | Files |
|--------|-------|
| 🟢 Overwritten | N |
| 🟡 Merged | N |
| 🆕 Added | N |
| 🔒 Custom (untouched) | N |
| 🌐 Translated | N |

💾 Backup: .agent/backups/pre_update_vX.Y.Z_YYYY-MM-DD/
⚠️ Restore: /anchor_restore [backup_path]
```

---

## Safety Rules

1. **ALWAYS** backup before update
2. **NEVER** overwrite user data (NEVER_TOUCH list)
3. **NEVER** touch custom workflows not in new version
4. User entries in `_index.md` tables are **sacred** — merge, not replace
5. User preference values are **sacred** — add new settings, keep existing
6. CUSTOM PROJECT RULES in system prompts are **sacred** — preserve on merge
7. Translate after update if language ≠ en
8. Include backup path in report
