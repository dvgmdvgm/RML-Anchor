---
description: Safely removes RLM-Anchor from the project with backup and confirmation.
---

# /anchor_remove — Safe System Removal

## Usage

```
/anchor_remove
```

## Purpose

Safely remove the RLM-Anchor memory system from the project with:
- Two-factor confirmation (random code)
- Automatic backup before deletion
- Clear restore instructions

> [!IMPORTANT]
> This command removes ONLY RLM-Anchor files. Other files in `.agent/` 
> (like custom IDE configurations) will NOT be touched.

---

## RLM-Anchor Files to Remove

The following paths are part of RLM-Anchor and will be removed:

```yaml
RLM_PATHS_TO_DELETE:
  - .agent/memory/              # All memory categories
  - .agent/workflows/           # RLM workflow files (see list below)
  - .agent/scripts/             # Python utilities
  - .agent/skills/MEMORY_SKILL.md  # Memory skill
  - .agent/docs/ADVANCED_MEMORY_SYSTEM*.md  # RLM documentation
  - .agent/backups/             # Backup folder
  - .agent/MEMORY_INDEX.md      # Main memory index

RLM_WORKFLOW_FILES:
  - remember.md
  - recall.md
  - wakeup.md
  - sleep.md
  - handoff.md
  - walkthrough.md
  - anchor_agent.md
  - anchor_backup.md
  - anchor_restore.md
  - anchor_remove.md
  - anchor_cleanup.md
  - memory-stats.md
```

---

## Execution Steps

### Step 1: Display Warning

```markdown
⚠️ **WARNING: RLM-ANCHOR SYSTEM REMOVAL**

You are about to remove the RLM-Anchor memory system!

🛡️ **YOUR IDE CONFIGS ARE SAFE!**
Only RLM-Anchor files will be deleted. Other files in `.agent/` 
(custom IDE configurations, rules, etc.) will NOT be affected.

This will delete:
- 📁 .agent/memory/ folder (all 13 categories)
- 📄 RLM workflow files (12 files)
- 📄 .agent/MEMORY_INDEX.md
- 📄 .agent/skills/MEMORY_SKILL.md
- 📁 .agent/docs/ADVANCED_MEMORY_SYSTEM*.md
- 📁 .agent/scripts/
- 📁 .agent/backups/

**Total RLM files to be deleted**: [COUNT]
**Total memory entries**: [COUNT]
```

### Step 2: Generate Confirmation Code

Generate a random 8-character alphanumeric code:

```python
import random
import string
code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
# Example: "a7x9K2mQ"
```

### Step 3: Request Confirmation

```markdown
🔐 **CONFIRMATION REQUIRED**

Before proceeding, a backup will be created automatically.

To confirm removal, type this exact code: **[GENERATED_CODE]**

Type the code or 'cancel' to abort:
```

### Step 4: Validate Code

- If code matches exactly → proceed to Step 5
- If code doesn't match → show error, allow retry (max 3 attempts)
- If 'cancel' or 3 failed attempts → abort

```markdown
❌ Code mismatch. Please try again. (Attempt 2/3)
```

### Step 5: Create Backup

Before any deletion, create a complete backup:

```bash
# Create backups directory if not exists
mkdir -p .agent/backups

# Create timestamped ZIP backup of RLM files only
cd .agent && zip -r "anchor_backup_FINAL_$(date +%Y-%m-%d_%H-%M-%S).zip" \
  memory/ \
  workflows/ \
  scripts/ \
  skills/MEMORY_SKILL.md \
  docs/ \
  MEMORY_INDEX.md \
  -x "backups/*"

# Move backup outside .agent before deletion
mv .agent/anchor_backup_FINAL_*.zip ./
```

Report backup creation:

```markdown
📦 **Backup Created**

✅ Backup saved to: `./anchor_backup_FINAL_2026-02-05_19-30-00.zip`
📊 Size: 2.3 MB
📁 RLM files archived: 47

Backup location is OUTSIDE .agent folder for safety.
```

### Step 6: Remove RLM Files Only

```bash
# Remove RLM-specific folders
rm -rf .agent/memory/
rm -rf .agent/scripts/
rm -rf .agent/backups/

# Remove RLM workflow files
rm -f .agent/workflows/remember.md
rm -f .agent/workflows/recall.md
rm -f .agent/workflows/wakeup.md
rm -f .agent/workflows/sleep.md
rm -f .agent/workflows/handoff.md
rm -f .agent/workflows/walkthrough.md
rm -f .agent/workflows/anchor_agent.md
rm -f .agent/workflows/anchor_backup.md
rm -f .agent/workflows/anchor_restore.md
rm -f .agent/workflows/anchor_remove.md
rm -f .agent/workflows/anchor_cleanup.md
rm -f .agent/workflows/memory-stats.md

# Remove RLM skill and index
rm -f .agent/skills/MEMORY_SKILL.md
rm -f .agent/MEMORY_INDEX.md

# Remove RLM documentation
rm -f .agent/docs/ADVANCED_MEMORY_SYSTEM*.md
```

### Step 7: Confirm Removal

```markdown
✅ **RLM-Anchor Removed Successfully**

The memory system has been removed from this project.

🛡️ Your custom IDE configs in `.agent/` were preserved.

---

## 🔄 To Restore

If you want to restore the system, run:

```
/anchor_restore ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
```

Or manually:
```bash
unzip anchor_backup_FINAL_2026-02-05_19-30-00.zip -d .agent/
```

---

## 🔄 To Reinstall Fresh

```bash
git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
```
```

---

## Error Handling

### Backup Failed
```markdown
❌ **Backup Failed**

Could not create backup. Removal aborted for safety.
Error: [ERROR_MESSAGE]

Please ensure you have write permissions and enough disk space.
```

### Removal Failed
```markdown
❌ **Removal Failed**

Backup was created successfully, but removal failed.
Error: [ERROR_MESSAGE]

Your backup is safe at: ./anchor_backup_FINAL_*.zip
Please manually remove RLM files if needed.
```

---

## Security Notes

1. **Random code** prevents accidental removal (typos, auto-complete)
2. **Backup first** ensures no data loss
3. **Backup outside .agent** survives the deletion
4. **Selective deletion** preserves custom IDE configs
5. **3 attempt limit** prevents brute-force (though not really needed)

---

## Example Session

```
User: /anchor_remove

AI: ⚠️ WARNING: RLM-ANCHOR SYSTEM REMOVAL

    You are about to remove the RLM-Anchor memory system!
    
    🛡️ YOUR IDE CONFIGS ARE SAFE!
    Only RLM-Anchor files will be deleted.
    
    This will delete:
    - 📁 .agent/memory/ (47 files)
    - 📄 RLM workflows (12 files)
    - 📄 MEMORY_INDEX.md, MEMORY_SKILL.md
    
    🔐 To confirm, type this exact code: a7x9K2mQ
    
User: a7x9K2mQ

AI: 📦 Creating backup...
    ✅ Backup saved: ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
    
    🗑️ Removing RLM files...
    ✅ RLM-Anchor removed successfully!
    
    🛡️ Your custom IDE configs were preserved.
    
    To restore: /anchor_restore ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
```
