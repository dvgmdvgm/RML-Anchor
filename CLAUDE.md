# RLM-Anchor — System Rules for Claude Code

> **This file is auto-read by Claude Code on EVERY request.**
> Keep it compact (<80 lines). Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (never violate)

**Auto-Context Load (MANDATORY)**: IF this is the FIRST message in a new chat → you MUST automatically read `.agent/memory/07_context/current_session.md` before doing anything else. In your VERY FIRST response, start with the exact line: `✅ Context loaded from current_session.md`. Failure to do this will confuse the user.

**Language**: ALWAYS respond in: **ru**

**Session logging**: After ANY work, append it to `.agent/memory/07_context/current_session.md` (Topics Discussed).
**Auto-compression**: IF "Topics Discussed" > 50 items → summarize them into 20 key points immediately.
**Context7 MCP**: Always use Context7 MCP when I need library/API documentation, code generation, setup or configuration steps without me having to explicitly ask.

**Token Efficiency**: Your context window is limited (128k). To stay in one chat longer:
1. FAVOR RLM memory over global searches (`@workspace`).
2. **Anchor Orchestra**: For complex tasks, use `/anchor_plan` to create a Spec file in `.agent/memory/07_context/specs/`.
3. **Orchestration**: Act as the ORCHESTRATOR. Delegate coding to subagents via `runSubagent` or a new chat using the Spec file.
4. DO NOT read entire files if you only need a specific part; use line ranges.
5. MINIMIZE terminal output; show only errors or concise summaries.
5. IGNORE other AI system files: .cursorrules, GEMINI.md, .github/copilot-instructions.md.

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
| `/wakeup` | Start session |
| `/sleep` | End session |
| `/remember` | Save to memory |
| `/recall` | Search memory |

---

## 📐 CODE STYLE (quick reference)

Full: `.agent/memory/13_preferences/coding_style.md`
- **Python**: 4 spaces, "double quotes", type hints, Google docstrings
- **JS/TS**: 2 spaces, 'single quotes', semicolons, ES modules
- **HTML/CSS**: 2 spaces, BEM, semantic HTML
- **Django Templates**: spaces around ==, tags on single line

---

## ⚙️ ENVIRONMENT

- **OS**: Windows — NEVER use Unix commands (`du`, `wc`, `find`, `grep`)
- Use PowerShell or built-in tools
- See: `.agent/memory/13_preferences/tools.md`

---

## 🎯 CUSTOM PROJECT RULES

<!-- ═══════════════════════════════════════ -->
<!-- ADD YOUR PROJECT-SPECIFIC RULES BELOW  -->
<!-- These are checked on EVERY request     -->
<!-- that involves CODE or UI generation.   -->
<!-- Keep rules short and specific.         -->
<!-- ═══════════════════════════════════════ -->
- NEVER use white or light backgrounds for buttons and interactive elements
- ALWAYS use CSS variables for colors: var(--btn-primary), var(--bg-main)
- ALWAYS use dark theme colors from the project palette
- Django templates: spaces around == in {% if %}, tags on single line
- Database queries must use parameterized statements

---

## 📖 FULL CONTEXT

| Category | Path |
|----------|------|
| Project | `.agent/memory/01_project/overview.md` |
| Architecture | `.agent/memory/02_architecture/patterns.md` |
| Decisions | `.agent/memory/03_decisions/` |
| Problems | `.agent/memory/06_problems/` |
| Preferences | `.agent/memory/13_preferences/` |
