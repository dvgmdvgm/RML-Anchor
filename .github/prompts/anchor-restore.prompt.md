---
agent: agent
description: "Anchor restore (RLM-Anchor)"
---

# /anchor_restore — Restore from Backup

## Usage

```
/anchor_restore [path_to_zip]
```

## Examples

```
/anchor_restore ./anchor_backup_FINAL_2026-02-05.zip
/anchor_restore .agent/backups/anchor_backup_2026-02-01.zip
/anchor_restore C:\backups\my_project_anchor.zip
```

## Purpose

Restore the RLM-Anchor system from a previously created backup:
- After accidental deletion
- When transferring from another PC
- To revert to a previous state

---

## Execution Steps

### Step 1: Validate Input

Check if path is provided:
```markdown
❌ **Error: No backup file specified**

Usage: `/anchor_restore [path_to_zip]`

Example: `/anchor_restore ./anchor_backup_2026-02-05.zip`
```

### Step 2: Check File Exists

```bash
if [ ! -f "$BACKUP_PATH" ]; then
    echo "File not found: $BACKUP_PATH"
    exit 1
fi
```

```markdown
❌ **Error: Backup file not found**

File: `[PATH]`

Please check the path and try again.
Available backups in .agent/backups/:
- anchor_backup_2026-02-04.zip
- anchor_backup_2026-02-01.zip
```

### Step 3: Validate ZIP Contents

```bash
unzip -l "$BACKUP_PATH" | grep -E "(memory/|workflows/|MEMORY_INDEX.md)"
```

If not a valid RLM-Anchor backup:
```markdown
❌ **Error: Invalid backup file**

This doesn't appear to be a valid RLM-Anchor backup.
Expected contents: memory/, workflows/, MEMORY_INDEX.md

Please use a backup created by `/anchor_backup` or `/anchor_remove`.
```

### Step 4: Check for Existing Installation

If .agent/ exists:
```markdown
⚠️ **Existing Installation Detected**

An .agent/ folder already exists in this project.

Choose an action:
1. **Overwrite** — Replace current with backup (backup current first)
2. **Merge** — Add backup files, keep existing (may cause conflicts)
3. **Cancel** — Abort restore

Enter choice [1/2/3]:
```

### Step 5: Backup Current (if overwriting)

```bash
# Create safety backup of current state
zip -r ".agent/backups/pre_restore_backup_$(date +%Y-%m-%d_%H-%M-%S).zip" .agent/ -x "backups/*"
```

```markdown
📦 Current state backed up to: pre_restore_backup_2026-02-05_19-45-00.zip
```

### Step 6: Extract Backup

For overwrite:
```bash
rm -rf .agent/
unzip "$BACKUP_PATH" -d .
```

For merge:
```bash
unzip -o "$BACKUP_PATH" -d .
```

### Step 7: Verify Restoration

```bash
# Check key files exist
ls .agent/MEMORY_INDEX.md
ls .agent/memory/
ls .agent/workflows/
```

### Step 8: Report Success

```markdown
✅ **Restore Completed Successfully**

📦 Restored from: `anchor_backup_2026-02-05.zip`
📁 Files restored: 47
🧠 Memory categories: 13
⚙️ Workflows: 8

---

## Quick Start

1. Set your language: `.agent/memory/13_preferences/language.md`
2. Start session: `/wakeup`
3. Check memory: `/memory-stats`

---

## Previous State

Your previous installation was backed up to:
`.agent/backups/pre_restore_backup_2026-02-05_19-45-00.zip`
```

---

## Error Handling

### Extraction Failed
```markdown
❌ **Extraction Failed**

Could not extract backup file.
Error: [ERROR_MESSAGE]

Possible causes:
- Corrupted ZIP file
- Insufficient disk space
- Permission denied

Your original .agent/ folder was NOT modified.
```

### Partial Restore
```markdown
⚠️ **Partial Restore Warning**

Some files could not be restored:
- [LIST OF FAILED FILES]

The rest of the system was restored successfully.
You may need to manually copy these files from the ZIP.
```

---

## Example Session

```
User: /anchor_restore ./anchor_backup_FINAL_2026-02-05.zip

AI: 📦 Validating backup file...
    ✅ Valid RLM-Anchor backup detected
    
    ⚠️ Existing .agent/ folder found!
    
    Choose action:
    1. Overwrite (backup current first)
    2. Merge (may conflict)
    3. Cancel
    
User: 1

AI: 📦 Backing up current state...
    ✅ Saved: pre_restore_backup_2026-02-05_19-45.zip
    
    📦 Extracting backup...
    ✅ Restore completed!
    
    📁 Files: 47
    🧠 Memory entries: 23
    
    Run /wakeup to start!
```