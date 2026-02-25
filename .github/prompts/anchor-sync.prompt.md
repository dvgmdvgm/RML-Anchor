---
agent: agent
description: "Regenerate system prompt files from RLM-Anchor memory"
---

# /anchor-sync — Sync System Prompts

You are executing the **RLM-Anchor /anchor_sync** workflow.

This regenerates IDE system prompt files from memory. These files are automatically injected by each IDE into every AI request.

## Step 1: Read Source Data

Read these files to gather current settings:

1. `.agent/memory/13_preferences/language_local.md` (or `language.md`)
2. `.agent/memory/13_preferences/coding_style.md` (extract key rules only)
3. `.agent/memory/05_code/conventions.md`
4. `.agent/memory/13_preferences/tools.md`
5. `.agent/memory/01_project/overview.md` (extract project type and stack)

## Step 2: Check Existing Custom Rules

Read existing system prompt files and **preserve CUSTOM PROJECT RULES** from each:
- `.cursorrules` → CUSTOM PROJECT RULES section
- `CLAUDE.md` → CUSTOM PROJECT RULES section
- `GEMINI.md` → CUSTOM PROJECT RULES section
- `.github/copilot-instructions.md` → CUSTOM PROJECT RULES section

> **CAUTION**: NEVER overwrite the CUSTOM PROJECT RULES section. These are user-written rules that must be preserved!

## Step 3: Run the Generation Script

Execute the Python script:
```
python .agent/scripts/generate_system_prompts.py --project-dir .
```

This generates `.cursorrules`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md`.

## Step 4: Verify Results

After the script runs, verify:
- All 4 files were generated
- Custom rules were preserved
- Language setting is correct

## Step 5: Report

```
✅ System prompts synced!

| File | Status | Lines |
|------|--------|-------|
| .cursorrules | ✅ Updated | N |
| CLAUDE.md | ✅ Updated | N |
| GEMINI.md | ✅ Updated | N |
| .github/copilot-instructions.md | ✅ Updated | N |

Custom rules preserved: N rules
Language: [language]
```
