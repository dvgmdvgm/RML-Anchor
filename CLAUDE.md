# RLM-Anchor — System Rules for Claude Code

> **This file is auto-read by Claude Code on EVERY request.**
> It contains routing logic for the RLM-Anchor memory system.
> Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (always active)

- **Language**: ALWAYS respond in the language from `.agent/memory/13_preferences/language_local.md`. If missing → use `.agent/memory/13_preferences/language.md`
- **OS**: Windows — NEVER use Unix commands (`du`, `wc`, `find`, `grep`, `sed`, `awk`). Use PowerShell or built-in agent tools

---

## 🧠 MEMORY-AWARE ROUTING ENGINE

**BEFORE generating any response that involves creating, editing, or reviewing code/content, you MUST follow this routing process.**

### Step 1: Classify the request

Determine what the user is asking for. A request may match multiple types:

| Type | Trigger keywords/intent |
|------|------------------------|
| **CODE** | write code, create function, add method, refactor, edit file, implement |
| **UI** | page, button, layout, CSS, design, style, template, form, component |
| **ARCHITECTURE** | system design, API design, component structure, data flow, module |
| **DOMAIN** | business logic, business rule, workflow, process, entity, model |
| **DEBUG** | bug, error, not working, fix, broken, issue, crash |
| **DEPLOY** | deploy, server, config, production, environment, CI/CD |
| **TEST** | test, coverage, QA, edge case, test data |
| **GENERAL** | question, explanation, discussion, how does X work |

### Step 2: Read the required memory files

**This step is MANDATORY, not optional.** Based on the classification, read the corresponding files:

| Type | MUST read before responding |
|------|---------------------------|
| **CODE** | `.agent/memory/05_code/_index.md` → then relevant files listed there. Also read `.agent/memory/13_preferences/coding_style.md` (only the section for the relevant language) |
| **UI** | `.agent/memory/05_code/conventions.md` + `.agent/memory/13_preferences/coding_style.md` (HTML/CSS section). Check the CUSTOM PROJECT RULES below |
| **ARCHITECTURE** | `.agent/memory/02_architecture/_index.md` → relevant files. Also `.agent/memory/03_decisions/_index.md` to check existing ADRs |
| **DOMAIN** | `.agent/memory/04_domain/_index.md` → relevant files |
| **DEBUG** | `.agent/memory/06_problems/_index.md` → check if this problem was already solved in `bugs/` or `workarounds/` |
| **DEPLOY** | `.agent/memory/11_deployment/_index.md` → relevant files |
| **TEST** | `.agent/memory/10_testing/_index.md` → relevant files |
| **GENERAL** | No memory reading required — respond directly |

> **KEY RULE**: Read the `_index.md` first. It will tell you which specific files exist and what they contain. Then read only the files relevant to the current request. Do NOT read all files — only the ones that match the user's task.

### Step 3: Apply rules and generate

After reading the relevant memory files:
1. **Apply all rules** found in those files to your response
2. **Check CUSTOM PROJECT RULES** below for project-specific constraints
3. **If memory files contradict each other** — the more specific file wins (e.g., `conventions.md` wins over `coding_style.md`)
4. **Generate the response** with full compliance

### Step 4: Self-check (for CODE/UI only)

Before finalizing code output, verify:
- [ ] Does the code follow conventions from `05_code/conventions.md`?
- [ ] Does the styling follow `coding_style.md` rules?
- [ ] Does the code avoid patterns listed in `06_problems/`?
- [ ] Does the code comply with CUSTOM PROJECT RULES below?

---

## 🟢 MEMORY SYSTEM

This project uses **RLM-Anchor** persistent memory.
- Memory location: `.agent/memory/` (13 categories)
- Main index: `.agent/MEMORY_INDEX.md`

**Commands** (user says `/command`):
| Command | Action |
|---------|--------|
| `/wakeup` | Start session → `.agent/workflows/wakeup.md` |
| `/sleep` | End session → `.agent/workflows/sleep.md` |
| `/remember` | Save to memory → `.agent/workflows/remember.md` |
| `/recall` | Search memory → `.agent/workflows/recall.md` |
| `/anchor_sync` | Regenerate this file from memory → `.agent/workflows/anchor_sync.md` |

---

## 🎯 CUSTOM PROJECT RULES

<!-- ═══════════════════════════════════════ -->
<!-- ADD YOUR PROJECT-SPECIFIC RULES BELOW  -->
<!-- These are checked on EVERY request     -->
<!-- that involves CODE or UI generation.   -->
<!-- Keep rules short and specific.         -->
<!-- ═══════════════════════════════════════ -->

<!-- Example rules (replace with your own):
- NEVER use white or light backgrounds for buttons and interactive elements
- ALWAYS use CSS variables for colors: var(--btn-primary), var(--bg-main)
- ALWAYS use dark theme colors from the project palette
- Django templates: spaces around == in {% if %}, tags on single line
- API responses must include error codes and messages
- Database queries must use parameterized statements
-->

---

## 📖 MEMORY CATEGORIES REFERENCE

| # | Category | Path | When to check |
|---|----------|------|---------------|
| 01 | Project | `.agent/memory/01_project/` | Project overview, tech stack |
| 02 | Architecture | `.agent/memory/02_architecture/` | System design questions |
| 03 | Decisions | `.agent/memory/03_decisions/` | Before making architectural choices |
| 04 | Domain | `.agent/memory/04_domain/` | Business logic questions |
| 05 | Code | `.agent/memory/05_code/` | Before writing/editing code |
| 06 | Problems | `.agent/memory/06_problems/` | Before fixing bugs, to avoid repeating |
| 07 | Context | `.agent/memory/07_context/` | Session history and pending tasks |
| 08 | People | `.agent/memory/08_people/` | Team roles and responsibilities |
| 09 | External | `.agent/memory/09_external/` | External APIs and integrations |
| 10 | Testing | `.agent/memory/10_testing/` | Test strategies and data |
| 11 | Deployment | `.agent/memory/11_deployment/` | Deploy configs and environments |
| 12 | Roadmap | `.agent/memory/12_roadmap/` | Future plans and tech debt |
| 13 | Preferences | `.agent/memory/13_preferences/` | Code style, language, communication |
