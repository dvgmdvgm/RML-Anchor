---
description: Generate/update system prompt files (.cursorrules, CLAUDE.md, GEMINI.md) from RLM-Anchor memory
---

# /anchor_sync — Sync System Prompts

## Usage

```
/anchor_sync
```

---

## Purpose

Generates IDE system prompt files (`.cursorrules`, `CLAUDE.md`, `GEMINI.md`) from RLM-Anchor memory.
These files are automatically injected by the IDE into **every** AI request, providing enforcement of critical rules.

> [!IMPORTANT]
> System prompt files have **highest priority** for LLMs.
> Memory files (`.agent/memory/`) are read only when referenced.
> This command bridges the gap: rules from memory → system prompts.

---

## Execution Steps

// turbo-all

### 1. Read Source Data

```
Read .agent/memory/13_preferences/language_local.md (or language.md)
Read .agent/memory/13_preferences/coding_style.md (extract key rules only)
Read .agent/memory/05_code/conventions.md
Read .agent/memory/13_preferences/tools.md
Read .agent/memory/01_project/overview.md (extract project type and stack)
```

### 2. Check Existing Custom Rules

```
If .cursorrules exists → read CUSTOM PROJECT RULES section
If CLAUDE.md exists → read CUSTOM PROJECT RULES section
If GEMINI.md exists → read CUSTOM PROJECT RULES section
Preserve all custom rules during regeneration!
```

> [!CAUTION]
> NEVER overwrite the CUSTOM PROJECT RULES section. These are user-written rules that must be preserved during sync.

### 3. Generate System Prompt Content

Build a compact (50-80 lines) system prompt containing:

1. **Language rule** — from `language_local.md` or `language.md`
2. **Project info** — one-line summary from `overview.md`
3. **Code style** — key formatting rules per language (indent, quotes, etc.)
4. **Environment** — OS, tools restrictions from `tools.md`
5. **Memory pointers** — how to access the full memory system
6. **Custom rules** — preserved from existing files

### 4. Write Files

```
Write .cursorrules (# comment format for Cursor)
Write CLAUDE.md (Markdown format for Claude Code)
Write GEMINI.md (Markdown format for Gemini CLI)
```

### 5. Report

```
✅ System prompts synced!

| File | Status | Lines |
|------|--------|-------|
| .cursorrules | ✅ Updated | N |
| CLAUDE.md | ✅ Updated | N |
| GEMINI.md | ✅ Updated | N |

Custom rules preserved: N rules
Language: [language]
```

---

## When to Run

| Trigger | Action |
|---------|--------|
| After `/remember` with new rules | Run `/anchor_sync` to propagate |
| After changing language | Run `/anchor_sync` |
| After installing RLM-Anchor | Run `/anchor_sync` to generate initial files |
| After `/anchor_update` | System runs automatically |

---

## Example

```
USER: /anchor_sync

AI: 🔄 Синхронизирую системные промпты...

    Источники:
    - language_local.md → ru
    - coding_style.md → 11 languages
    - tools.md → Windows (no Unix)
    - 2 custom rules preserved

    ✅ Системные промпты обновлены!

    | Файл | Статус | Строк |
    |------|--------|-------|
    | .cursorrules | ✅ | 72 |
    | CLAUDE.md | ✅ | 68 |
    | GEMINI.md | ✅ | 68 |
```
