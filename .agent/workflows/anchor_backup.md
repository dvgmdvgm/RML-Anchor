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
  - .agent/memory/01_project
  - .agent/memory/02_architecture
  - .agent/memory/03_decisions
  - .agent/memory/04_domain
  - .agent/memory/05_code
  - .agent/memory/06_problems
  - .agent/memory/07_context
  - .agent/memory/08_people
  - .agent/memory/09_external
  - .agent/memory/10_testing
  - .agent/memory/11_deployment
  - .agent/memory/12_roadmap
  - .agent/memory/13_preferences
  - .agent/scripts/memory_search.py
  - .agent/scripts/memory_stats.py
  - .agent/scripts/memory_validate.py
  - .agent/skills/MEMORY_SKILL.md
  - .agent/workflows/anchor_agent.md
  - .agent/workflows/anchor_backup.md
  - .agent/workflows/anchor_cleanup.md
  - .agent/workflows/anchor_remove.md
  - .agent/workflows/anchor_restore.md
  - .agent/workflows/handoff.md
  - .agent/workflows/memory-stats.md
  - .agent/workflows/recall.md
  - .agent/workflows/remember.md
  - .agent/workflows/sleep.md
  - .agent/workflows/wakeup.md
  - .agent/workflows/walkthrough.md
  - .agent/MEMORY_INDEX.md
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

### Step 4: Create ZIP Archive (Strict RLM Files Only)

```bash
cd .agent && zip -r "backups/anchor_backup_2026-02-05_19-30-00.zip" \
  memory/01_project \
  memory/02_architecture \
  memory/03_decisions \
  memory/04_domain \
  memory/05_code \
  memory/06_problems \
  memory/07_context \
  memory/08_people \
  memory/09_external \
  memory/10_testing \
  memory/11_deployment \
  memory/12_roadmap \
  memory/13_preferences \
  scripts/memory_search.py \
  scripts/memory_stats.py \
  scripts/memory_validate.py \
  skills/MEMORY_SKILL.md \
  workflows/anchor_agent.md \
  workflows/anchor_backup.md \
  workflows/anchor_cleanup.md \
  workflows/anchor_remove.md \
  workflows/anchor_restore.md \
  workflows/handoff.md \
  workflows/memory-stats.md \
  workflows/recall.md \
  workflows/remember.md \
  workflows/sleep.md \
  workflows/wakeup.md \
  workflows/walkthrough.md \
  MEMORY_INDEX.md \
  -x "backups/*"
```

### Step 5: Report Success

```markdown
✅ **Backup Created Successfully**

📦 File: `.agent/backups/anchor_backup_2026-02-05_19-30-00.zip`
📊 Size: 2.3 MB
📁 RLM Files: [COUNT]

🛡️ **Note**: Only RLM-Anchor files were backed up.
   Your custom IDE configs in `.agent/` were NOT included.
```

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

---

## Auto-Cleanup

By default, only the last 5 backups are kept.

To change this, edit `.agent/memory/13_preferences/cleanup_settings.md`:
```yaml
BACKUP:
  MAX_BACKUPS: 5
  AUTO_DELETE_OLD: true
```
