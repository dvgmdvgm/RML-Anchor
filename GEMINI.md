# RLM-Anchor — System Rules for Gemini

> **This file is auto-read by Gemini CLI / Antigravity on EVERY request.**
> Keep it compact (<80 lines). Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (never violate)

**Language**: ALWAYS respond in the language specified in:
- `.agent/memory/13_preferences/language_local.md` (if exists, priority)
- `.agent/memory/13_preferences/language.md` (fallback)

---

## 🟡 PROJECT RULES

**Before generating UI/CSS:**
- Read `.agent/memory/13_preferences/coding_style.md`
- Read `.agent/memory/05_code/conventions.md`
- Apply project design rules (colors, spacing, typography)

**Before making architecture decisions:**
- Read `.agent/memory/03_decisions/` for existing ADRs
- Don't repeat solved problems → check `.agent/memory/06_problems/`

---

## 🟢 MEMORY SYSTEM

This project uses **RLM-Anchor** persistent memory.
- Memory: `.agent/memory/` (13 categories)
- Index: `.agent/MEMORY_INDEX.md`

**Commands** (user says `/command`):
| Command | Action |
|---------|--------|
| `/wakeup` | Start session → `.agent/workflows/wakeup.md` |
| `/sleep` | End session → `.agent/workflows/sleep.md` |
| `/remember` | Save to memory → `.agent/workflows/remember.md` |
| `/recall` | Search memory → `.agent/workflows/recall.md` |

---

## 📐 CODE STYLE (quick reference)

Full: `.agent/memory/13_preferences/coding_style.md`
- **Python**: 4 spaces, `"double quotes"`, type hints, Google docstrings
- **JS/TS**: 2 spaces, `'single quotes'`, semicolons, ES modules
- **HTML/CSS**: 2 spaces, BEM, semantic HTML

---

## ⚙️ ENVIRONMENT

- **OS**: Windows — NEVER use Unix commands (`du`, `wc`, `find`, `grep`)
- Use PowerShell or built-in tools
- See: `.agent/memory/13_preferences/tools.md`

---

## 🎯 CUSTOM PROJECT RULES

Add your project-specific rules below:
<!-- Example:
- Never use white backgrounds for buttons
- Always use dark theme
- API responses must include error codes
-->

---

## 📖 FULL CONTEXT

| Category | Path |
|----------|------|
| Project | `.agent/memory/01_project/overview.md` |
| Architecture | `.agent/memory/02_architecture/patterns.md` |
| Decisions | `.agent/memory/03_decisions/` |
| Problems | `.agent/memory/06_problems/` |
| Preferences | `.agent/memory/13_preferences/` |
