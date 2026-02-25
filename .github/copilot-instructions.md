# RLM-Anchor — System Rules for GitHub Copilot Chat

> **This file is auto-read by VS Code Copilot Chat on EVERY request.**
> It contains routing logic for the RLM-Anchor memory system.
> Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (always active)

- **Language**: ALWAYS respond in **Russian (ru)**. Source: `.agent/memory/13_preferences/language_local.md`
- **OS**: Windows — NEVER use Unix commands (`du`, `wc`, `find`, `grep`, `sed`, `awk`). Use PowerShell or built-in tools
- **Session logging**: After completing ANY code/UI/architecture task, you MUST append what was done to `.agent/memory/07_context/current_session.md` (Topics Discussed section). If a design decision was made → also save to `03_decisions/`. Report in footer: `💾 Сохранено: [what] → [where]`. See Step 6 for details.

---

## 🧠 MEMORY-AWARE ROUTING ENGINE

**BEFORE generating any response that involves creating, editing, or reviewing code/content, you MUST follow this routing process.**

### Step 1: Classify the request

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

**This step is MANDATORY.** Based on the classification, read the corresponding files from the workspace:

| Type | MUST read before responding |
|------|---------------------------|
| **CODE** | `.agent/memory/05_code/_index.md` → then relevant files. Also `.agent/memory/13_preferences/coding_style.md` (relevant language section only) |
| **UI** | `.agent/memory/05_code/conventions.md` + `.agent/memory/13_preferences/coding_style.md` (HTML/CSS section). Check CUSTOM PROJECT RULES below |
| **ARCHITECTURE** | `.agent/memory/02_architecture/_index.md` → relevant files. Also `.agent/memory/03_decisions/_index.md` for existing ADRs |
| **DOMAIN** | `.agent/memory/04_domain/_index.md` → relevant files |
| **DEBUG** | `.agent/memory/06_problems/_index.md` → check `bugs/` and `workarounds/` |
| **DEPLOY** | `.agent/memory/11_deployment/_index.md` → relevant files |
| **TEST** | `.agent/memory/10_testing/_index.md` → relevant files |
| **GENERAL** | No memory reading required — respond directly |

> **KEY RULE**: Read the `_index.md` first. It tells you which specific files exist. Then read only the relevant ones.

### Step 3: Apply rules and generate

1. **Apply all rules** from those files
2. **Check CUSTOM PROJECT RULES** below
3. **If files contradict** — the more specific file wins
4. **Generate the response**

### Step 4: Self-check (for CODE/UI only)

Before finalizing code output, verify:
- [ ] Follows conventions from `05_code/conventions.md`?
- [ ] Follows `coding_style.md` rules?
- [ ] Avoids patterns from `06_problems/`?
- [ ] Complies with CUSTOM PROJECT RULES?

### Step 5: Memory transparency footer (EVERY response)

At the end of EVERY response, append:

When memory was consulted:
```
---
📎 **Память:** `conventions.md`, `coding_style.md` (HTML/CSS) → тёмная тема, без белых фонов, BEM-именование
```

When no memory was needed:
```
---
📎 **Память:** обращение к файлам памяти не требовалось
```

Rules: 1-3 lines max, file names only, brief summary after →, use Russian.

### Step 6: Post-action analysis (after EVERY completed task)

**6a.** Is this a significant change? (design decision, bug fix, convention change, business logic)

**6b.** If YES → update `current_session.md` (Topics Discussed + Key Decisions sections)

**6c.** If FUNDAMENTAL (affects multiple files, changes convention) → save to appropriate memory category:
- Architecture → `03_decisions/`
- Bug fix → `06_problems/bugs/`
- Convention → `05_code/conventions.md`
- Business rule → `04_domain/`

Report: `💾 Сохранено: [what] → [category]`

**6d.** If NOT significant → do nothing.

---

## 🟢 MEMORY SYSTEM

This project uses **RLM-Anchor** persistent memory.
- Memory location: `.agent/memory/` (13 categories)
- Main index: `.agent/MEMORY_INDEX.md`

**Commands** (type `/command` in Copilot Chat — these use `.github/prompts/` prompt files):

| Command | Action |
|---------|--------|
| `/wakeup` | Start session → load project context |
| `/sleep` | End session → summarize and archive |
| `/remember` | Save to memory |
| `/recall` | Search memory |
| `/anchor-sync` | Regenerate system prompt files |

---

## ⚙️ ENVIRONMENT

- **OS**: Windows — NEVER use Unix commands
- Use PowerShell or built-in agent tools
- See: `.agent/memory/13_preferences/tools.md`

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
