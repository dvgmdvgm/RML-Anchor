# 🧠 MEMORY INDEX — Project Memory Main Index

> **Version**: 1.0.0  
> **Created**: 2026-02-05  
> **Last Updated**: 2026-02-05

---

# 🔴 STOP! CHECK LANGUAGE FIRST! 🔴

**Before doing ANYTHING, read:** `memory/13_preferences/language.md`

```
Current language file: .agent/memory/13_preferences/language.md
→ Extract LANGUAGE= value
→ Use ONLY that language for ALL responses
```

---

## 🎯 How to Use This Index

This file is the **entry point** to the project memory system. When accessing memory:

1. **Read this file** — understand the structure
2. **Identify relevant categories** — by query keywords
3. **Navigate to category** — read the category's `_index.md`
4. **Find specific files** — extract needed information

---

## 📁 Memory Categories Structure

| # | Category | Path | Description | Keywords |
|---|----------|------|-------------|----------|
| 01 | 🏗️ **PROJECT** | `memory/01_project/` | General project information | project, stack, tech, structure, dependencies |
| 02 | 🏛️ **ARCHITECTURE** | `memory/02_architecture/` | System architecture | architecture, patterns, components, diagrams, data flow |
| 03 | ⚖️ **DECISIONS** | `memory/03_decisions/` | Architecture Decision Records (ADR) | decision, why, choice, alternatives, ADR |
| 04 | 🎯 **DOMAIN** | `memory/04_domain/` | Business domain and logic | business, domain, terms, glossary, rules, entities |
| 05 | 💻 **CODE** | `memory/05_code/` | Important code aspects | code, functions, classes, API, models, endpoints |
| 06 | 🐛 **PROBLEMS** | `memory/06_problems/` | Problems and solutions | bug, error, problem, solution, workaround, fix |
| 07 | 💬 **CONTEXT** | `memory/07_context/` | Dialog context | session, discussed, last time, task, context |
| 08 | 👥 **PEOPLE** | `memory/08_people/` | People and roles | user, role, persona, team, stakeholder |
| 09 | 🔗 **EXTERNAL** | `memory/09_external/` | External dependencies | API, service, library, integration, external |
| 10 | 🧪 **TESTING** | `memory/10_testing/` | Testing | test, edge case, test data, QA |
| 11 | 🚀 **DEPLOYMENT** | `memory/11_deployment/` | Deployment | deploy, environment, config, server, production |
| 12 | 🗓️ **ROADMAP** | `memory/12_roadmap/` | Plans and future | plan, feature, idea, tech debt, TODO, future |
| 13 | ⚙️ **PREFERENCES** | `memory/13_preferences/` | User preferences | style, preference, setting, language |

---

## 🔍 Quick Search by Information Type

### Need to find a decision?
→ `memory/03_decisions/` or `memory/06_problems/`

### Need to understand architecture?
→ `memory/02_architecture/` or `memory/01_project/`

### Need to recall what was discussed?
→ `memory/07_context/`

### Need to understand business logic?
→ `memory/04_domain/`

### Need to find how something works in code?
→ `memory/05_code/`

---

## 📊 Memory Statistics

| Metric | Value |
|--------|-------|
| Total Categories | 13 |
| Total Entries | 0 |
| Last Updated | YYYY-MM-DD |

---

## ⚡ Commands for Working with Memory

| Command | Description |
|---------|-------------|
| `/remember` | Save information to memory |
| `/recall` | Find information in memory |
| `/wakeup` | Start session (load context) |
| `/sleep` | End session (summarize) |
| `/memory-stats` | Show memory statistics |

---

## 📖 Related Files

- **AI Instructions**: `.agent/skills/MEMORY_SKILL.md`
- **Workflows**: `.agent/workflows/remember.md`, `recall.md`, etc.
- **Scripts**: `.agent/scripts/memory_*.py`
- **Language Settings**: `.agent/memory/13_preferences/language.md`
