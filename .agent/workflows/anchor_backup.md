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

> [!IMPORTANT]
> This backup includes ONLY RLM-Anchor files. Other files in `.agent/` 
> (like custom IDE configurations) are NOT included to preserve your settings.

---

## RLM-Anchor Files to Backup

The following paths are part of RLM-Anchor and will be backed up:

```yaml
RLM_PATHS:
  - .agent/memory/              # All 13 memory categories
  - .agent/workflows/           # All workflow definitions
  - .agent/scripts/             # Python utilities
  - .agent/skills/MEMORY_SKILL.md  # Memory skill instructions
  - .agent/docs/                # Documentation
  - .agent/backups/             # Previous backups (optional)
  - .agent/MEMORY_INDEX.md      # Main memory index
```

---

## Execution Steps

### Step 1: Prepare Backup

```markdown
📦 **Creating Backup...**

Scanning RLM-Anchor files...
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

### Step 4: Create ZIP Archive (RLM Files Only)

```bash
cd .agent && zip -r "backups/anchor_backup_2026-02-05_19-30-00.zip" \
  memory/ \
  workflows/ \
  scripts/ \
  skills/MEMORY_SKILL.md \
  docs/ \
  MEMORY_INDEX.md \
  -x "backups/*"
```

### Step 5: Report Success

```markdown
✅ **Backup Created Successfully**

📦 File: `.agent/backups/anchor_backup_2026-02-05_19-30-00.zip`
📊 Size: 2.3 MB
📁 RLM Files: 47
🧠 Memory entries: 23

🛡️ **Note**: Only RLM-Anchor files were backed up.
   Your custom IDE configs in `.agent/` were NOT included.

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

| Folder/File | Description |
|-------------|-------------|
| `memory/` | All 13 memory categories |
| `workflows/` | All RLM command definitions |
| `scripts/` | Python utilities |
| `skills/MEMORY_SKILL.md` | AI memory instructions |
| `docs/` | Documentation |
| `MEMORY_INDEX.md` | Main index |

**Excluded**: 
- Previous backups (to prevent nesting)
- Custom IDE configs not part of RLM-Anchor

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
    📁 RLM Files: 47
    
    🛡️ Your custom IDE configs were preserved (not included in backup).

User: /anchor_backup before-refactor

AI: 📦 Creating backup...
    
    ✅ Backup created!
    📦 File: .agent/backups/anchor_backup_before-refactor_2026-02-05.zip
    📊 Size: 2.3 MB
```
