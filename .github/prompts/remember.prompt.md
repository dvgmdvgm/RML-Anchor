---
agent: agent
description: "Save information to project memory system (RLM-Anchor)"
---

# /remember — Save to Memory

You are executing the **RLM-Anchor /remember** workflow.

The user wants to save information to the project's persistent memory system.

## Step 0: Check Language Setting

Read `.agent/memory/13_preferences/language_local.md` (if exists, use it).
Otherwise read `.agent/memory/13_preferences/language.md`.
All saved entries must be written in this language!

## Step 1: Determine Category

Based on the user's message context, determine the appropriate category:

| Context | Category |
|---------|----------|
| Architecture decision, tech choice | `03_decisions` |
| Solved bug, workaround | `06_problems` |
| New component, function, class | `05_code` |
| External API, integration | `09_external` |
| Plan, idea, TODO | `12_roadmap` |
| User preference | `13_preferences` |
| Other | Ask user |

## Step 2: Read Category Index

Read `.agent/memory/[category]/_index.md` to understand existing entries.

## Step 3: Determine File

- If information relates to an existing file → update it
- If new topic → create new file

## Step 4: Create/Update Entry

Use template from `_template.md` if available, or standard format:

```markdown
# [Title - in configured language]

- **Date**: YYYY-MM-DD
- **Tags**: tag1, tag2

---

## Content

[Information - in configured language]
```

**IMPORTANT: Write content in the configured language!**

## Step 5: Update Category Index

Add new file to `_index.md` table.

## Step 6: Confirm to User

Output in configured language:

```
✅ Saved to memory/[category]/[file].md
```
