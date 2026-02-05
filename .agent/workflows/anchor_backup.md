---
description: Creates a manual backup of the entire RLM-Anchor system.
---

# /anchor_backup — Manual Backup

## Usage

```
/anchor_backup
/anchor_backup [custom_name]
```

## Purpose

Create a complete backup of the RLM-Anchor system for:
- Transferring to another PC
- Migrating to another IDE
- Safety before major changes
- Version snapshots

---

## Execution Steps

### Step 1: Prepare Backup

```markdown
📦 **Creating Backup...**

Scanning .agent/ folder...
```

### Step 2: Create Backup Directory

```bash
mkdir -p .agent/backups
```

### Step 3: Generate Backup Filename

If custom name provided:
```
anchor_backup_{custom_name}_{date}.zip
```

Otherwise:
```
anchor_backup_{date}_{time}.zip
```

### Step 4: Create ZIP Archive

```bash
cd .agent && zip -r "backups/anchor_backup_2026-02-05_19-30-00.zip" \
  memory/ \
  workflows/ \
  scripts/ \
  skills/ \
  docs/ \
  MEMORY_INDEX.md \
  README.md \
  -x "backups/*"
```

### Step 5: Report Success

```markdown
✅ **Backup Created Successfully**

📦 File: `.agent/backups/anchor_backup_2026-02-05_19-30-00.zip`
📊 Size: 2.3 MB
📁 Files: 47
🧠 Memory entries: 23

---

## How to Use This Backup

### Restore on same PC:
```
/anchor_restore .agent/backups/anchor_backup_2026-02-05_19-30-00.zip
```

### Transfer to another PC:
1. Copy the ZIP file to the new PC
2. Place it in your project root
3. Run: `/anchor_restore ./anchor_backup_2026-02-05_19-30-00.zip`

### Manual restore:
```bash
unzip anchor_backup_2026-02-05_19-30-00.zip -d .agent/
```
```

---

## Backup Contents

The backup includes:

| Folder | Description |
|--------|-------------|
| `memory/` | All 13 memory categories |
| `workflows/` | All command definitions |
| `scripts/` | Python utilities |
| `skills/` | AI instructions |
| `docs/` | Documentation |
| `MEMORY_INDEX.md` | Main index |
| `README.md` | System readme |

**Excluded**: Previous backups (to prevent nesting)

---

## Auto-Cleanup

By default, only the last 5 backups are kept.

To change this, edit `.agent/memory/13_preferences/cleanup_settings.md`:
```yaml
BACKUP:
  MAX_BACKUPS: 5
  AUTO_DELETE_OLD: true
```

---

## Example Session

```
User: /anchor_backup

AI: 📦 Creating backup...
    
    ✅ Backup created!
    📦 File: .agent/backups/anchor_backup_2026-02-05_19-30-00.zip
    📊 Size: 2.3 MB
    📁 Files: 47

User: /anchor_backup before-refactor

AI: 📦 Creating backup...
    
    ✅ Backup created!
    📦 File: .agent/backups/anchor_backup_before-refactor_2026-02-05.zip
    📊 Size: 2.3 MB
```
