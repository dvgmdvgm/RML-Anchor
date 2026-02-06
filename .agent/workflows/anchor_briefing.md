---
description: Full project briefing with all memory categories
---

# /anchor_briefing — Complete Project Overview

## Usage

```
/anchor_briefing
```

---

## Purpose

Generate a **comprehensive briefing** that covers ALL aspects of the project stored in the 13 memory categories. This is the most complete overview available.

---

## Execution Steps

### 1. Read Language Settings

```
Read .agent/memory/13_preferences/language.md
All output must be in this language!
```

### 2. Scan All Memory Categories

Read `_index.md` from each category:

```
.agent/memory/01_project/_index.md
.agent/memory/02_architecture/_index.md
.agent/memory/03_decisions/_index.md
.agent/memory/04_domain/_index.md
.agent/memory/05_code/_index.md
.agent/memory/06_problems/_index.md
.agent/memory/07_context/_index.md
.agent/memory/08_people/_index.md
.agent/memory/09_external/_index.md
.agent/memory/10_testing/_index.md
.agent/memory/11_deployment/_index.md
.agent/memory/12_roadmap/_index.md
.agent/memory/13_preferences/_index.md
```

For each category with content, read the relevant entries.

### 3. Generate Comprehensive Report

Output format:

```markdown
# 📊 PROJECT BRIEFING: [Project Name]

> Generated: YYYY-MM-DD HH:MM
> Language: [Language]
> Memory Entries: N total

---

## 📁 01. Project Overview

| Property | Value |
|----------|-------|
| Name | ... |
| Type | ... |
| Tech Stack | ... |
| Status | ... |

**Description**: ...

---

## 🏗️ 02. Architecture

| Component | Technology | Notes |
|-----------|------------|-------|
| Backend | ... | ... |
| Frontend | ... | ... |
| Database | ... | ... |

**Patterns Used**: ...
**Data Flow**: ...

---

## ⚖️ 03. Decisions (ADRs)

| ID | Decision | Date | Status |
|----|----------|------|--------|
| ADR-001 | ... | YYYY-MM-DD | ✅ Active |

---

## 📚 04. Domain / Business Logic

| Entity | Description | Rules |
|--------|-------------|-------|
| User | ... | ... |

**Key Business Rules**:
- Rule 1
- Rule 2

---

## 💻 05. Code Guidelines

| Aspect | Standard |
|--------|----------|
| Language | ... |
| Style | ... |
| Naming | ... |

---

## 🐛 06. Known Issues

### Active Bugs:
| ID | Description | Priority |
|----|-------------|----------|
| BUG-001 | ... | 🔴 High |

### Workarounds:
| Issue | Workaround |
|-------|------------|
| ... | ... |

---

## 📅 07. Current Context

**Current Session**: Started YYYY-MM-DD
**Pending Tasks**:
| Priority | Task |
|----------|------|
| 🔴 | ... |

**Recent Sessions**: N sessions in history

---

## 👥 08. Team / Stakeholders

| Role | Person | Contact |
|------|--------|---------|
| Owner | ... | ... |

---

## 🔌 09. External Integrations

| Service | Purpose | Status |
|---------|---------|--------|
| ... | ... | ✅ Active |

**API Keys Location**: ...

---

## 🧪 10. Testing

| Type | Coverage | Notes |
|------|----------|-------|
| Unit | ...% | ... |
| E2E | ...% | ... |

**Testing Strategy**: ...

---

## 🚀 11. Deployment

| Environment | URL | Status |
|-------------|-----|--------|
| Production | ... | ✅ |
| Staging | ... | ✅ |

**CI/CD**: ...
**Hosting**: ...

---

## 🗺️ 12. Roadmap

### Upcoming Milestones:
| Milestone | Date | Status |
|-----------|------|--------|
| v1.0 Release | ... | 🔄 In Progress |

### Planned Features:
- Feature 1
- Feature 2

---

## ⚙️ 13. Preferences

| Setting | Value |
|---------|-------|
| Language | ... |
| Response Style | Tables preferred (~65%) |
| Code Style | PEP8 / ESLint |

---

## 📊 Memory Statistics

| Category | Entries | Last Updated |
|----------|---------|--------------|
| 01_project | N | YYYY-MM-DD |
| 02_architecture | N | YYYY-MM-DD |
| ... | ... | ... |
| **Total** | **N** | — |
```

---

## Example (Russian)

```
USER: /anchor_briefing

AI: 📊 ПОЛНЫЙ БРИФИНГ ПРОЕКТА: AnchorGravity

    > Сгенерировано: 2026-02-06 03:20
    > Язык: Русский
    > Записей в памяти: 47

    ---

    ## 📁 01. О проекте
    
    | Параметр | Значение |
    |----------|----------|
    | Название | AnchorGravity |
    | Тип | RLM Memory System |
    | Tech Stack | Markdown, Python |
    | Статус | ✅ Production Ready |
    
    ---
    
    ## ⚖️ 03. Решения (ADR)
    
    | ID | Решение | Дата | Статус |
    |----|---------|------|--------|
    | ADR-001 | Строгий список файлов | 2026-02-05 | ✅ |
    | ADR-002 | Архивация сессий | 2026-02-06 | ✅ |
    
    ... [все 13 категорий] ...
    
    ---
    
    📊 Всего записей: 47
```

---

## Notes

- This is the **most comprehensive** command in the system
- Use it when onboarding to a project or after a long break
- Output can be long — that's expected for a full briefing
- AI should summarize empty categories briefly ("No entries")
