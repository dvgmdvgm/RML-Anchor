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
- **Strict selective deletion** (preserves your custom configs)

> [!IMPORTANT]
> This command removes ONLY RLM-Anchor files. Other files in `.agent/` 
> (like custom IDE configurations) will NOT be touched.

---

## RLM-Anchor Files to Remove

The following paths are part of RLM-Anchor and will be removed:

```yaml
RLM_PATHS_TO_DELETE:
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

### Step 1: Display Warning

```markdown
⚠️ **WARNING: RLM-ANCHOR SYSTEM REMOVAL**

You are about to remove the RLM-Anchor memory system!

🛡️ **YOUR IDE CONFIGS ARE SAFE!**
Only RLM-Anchor files will be deleted. Other files in `.agent/` 
(custom IDE configurations, rules, etc.) will NOT be affected.
```

### Step 2: Confirmation (Code)

```markdown
🔐 To confirm, type this code: [GENERATED_CODE]
```

### Step 3: Create Backup

Before any deletion, create a complete backup of the strict file list.

```bash
# ... (Backup logic same as /anchor_backup) ...
```

### Step 4: Remove RLM Files (Strict)

Delete specific files and subfolders:

```bash
# 1. Remove Memory Categories
rm -rf .agent/memory/01_project
rm -rf .agent/memory/02_architecture
rm -rf .agent/memory/03_decisions
rm -rf .agent/memory/04_domain
rm -rf .agent/memory/05_code
rm -rf .agent/memory/06_problems
rm -rf .agent/memory/07_context
rm -rf .agent/memory/08_people
rm -rf .agent/memory/09_external
rm -rf .agent/memory/10_testing
rm -rf .agent/memory/11_deployment
rm -rf .agent/memory/12_roadmap
rm -rf .agent/memory/13_preferences

# 2. Remove Scripts
rm -f .agent/scripts/memory_search.py
rm -f .agent/scripts/memory_stats.py
rm -f .agent/scripts/memory_validate.py

# 3. Remove Skills
rm -f .agent/skills/MEMORY_SKILL.md

# 4. Remove Workflows
rm -f .agent/workflows/anchor_agent.md
rm -f .agent/workflows/anchor_backup.md
rm -f .agent/workflows/anchor_cleanup.md
rm -f .agent/workflows/anchor_remove.md
rm -f .agent/workflows/anchor_restore.md
rm -f .agent/workflows/handoff.md
rm -f .agent/workflows/memory-stats.md
rm -f .agent/workflows/recall.md
rm -f .agent/workflows/remember.md
rm -f .agent/workflows/sleep.md
rm -f .agent/workflows/wakeup.md
rm -f .agent/workflows/walkthrough.md

# 5. Remove Index
rm -f .agent/MEMORY_INDEX.md
```

### Step 5: Conditional Folder Cleanup

Attempt to remove parent folders ONLY if they are empty.
(Using `rmdir` which fails safely if folder is not empty).

```bash
# Order MUST be strict:

# 1. Clean memory/
rmdir .agent/memory 2>/dev/null || true

# 2. Clean scripts/
rmdir .agent/scripts 2>/dev/null || true

# 3. Clean skills/
rmdir .agent/skills 2>/dev/null || true

# 4. Clean workflows/
rmdir .agent/workflows 2>/dev/null || true

# 5. Finally, clean .agent/ root
rmdir .agent 2>/dev/null || true
```

### Step 6: Confirm Removal

```markdown
✅ **RLM-Anchor Removed Successfully**

🛡️ Your custom IDE configs in `.agent/` were preserved (if any existed).
```
