---
description: Safely removes RLM-Anchor from the project with backup and confirmation.
---

# /anchor_remove — Safe System Removal

## Usage

```
/anchor_remove
```

## Purpose

Safely remove the entire RLM-Anchor system from the project with:
- Two-factor confirmation (random code)
- Automatic backup before deletion
- Clear restore instructions

---

## Execution Steps

### Step 1: Display Warning

```markdown
⚠️ **WARNING: COMPLETE SYSTEM REMOVAL**

You are about to remove the entire RLM-Anchor memory system!

🛡️ **YOUR PROJECT FILES ARE SAFE!**
Only the `.agent/` folder will be deleted. Your source code, configs, and all other project files will NOT be affected.

This will delete:
- 📁 .agent/ folder and ALL its contents
- 🧠 All memory entries (13 categories)
- ⚙️ All workflows and scripts
- 📝 All preferences and settings

**Total files to be deleted**: [COUNT]
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

# Create timestamped ZIP backup
zip -r ".agent/backups/anchor_backup_FINAL_$(date +%Y-%m-%d_%H-%M-%S).zip" .agent/

# Move backup outside .agent before deletion
mv .agent/backups/anchor_backup_FINAL_*.zip ./
```

Report backup creation:

```markdown
📦 **Backup Created**

✅ Backup saved to: `./anchor_backup_FINAL_2026-02-05_19-30-00.zip`
📊 Size: 2.3 MB
📁 Files archived: 47

Backup location is OUTSIDE .agent folder for safety.
```

### Step 6: Remove System

```bash
# Remove the .agent folder
rm -rf .agent/
```

### Step 7: Confirm Removal

```markdown
✅ **RLM-Anchor Removed Successfully**

The memory system has been completely removed from this project.

---

## 🔄 To Restore

If you want to restore the system, run:

```
/anchor_restore ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
```

Or manually:
```bash
unzip anchor_backup_FINAL_2026-02-05_19-30-00.zip -d .
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
Please manually remove .agent/ folder if needed.
```

---

## Security Notes

1. **Random code** prevents accidental removal (typos, auto-complete)
2. **Backup first** ensures no data loss
3. **Backup outside .agent** survives the deletion
4. **Clear restore path** makes recovery easy
5. **3 attempt limit** prevents brute-force (though not really needed)

---

## Example Session

```
User: /anchor_remove

AI: ⚠️ WARNING: COMPLETE SYSTEM REMOVAL

    You are about to remove the entire RLM-Anchor memory system!
    
    This will delete:
    - 📁 .agent/ folder and ALL contents
    - 🧠 All memory entries (47 files)
    - ⚙️ All workflows (8 files)
    
    🔐 To confirm, type this exact code: a7x9K2mQ
    
User: a7x9K2mQ

AI: 📦 Creating backup...
    ✅ Backup saved: ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
    
    🗑️ Removing .agent folder...
    ✅ RLM-Anchor removed successfully!
    
    To restore: /anchor_restore ./anchor_backup_FINAL_2026-02-05_19-30-00.zip
```
