# ADR-002: 13-Category Organization

> **Status**: ✅ Active  
> **Date**: 2026-02-06  
> **Decision Makers**: dvgmdvgm

---

## 📋 Context

We need to organize project knowledge in a way that:
- Covers all types of project information
- Is intuitive to navigate
- Supports partial access (AI reads only relevant parts)
- Is consistent across projects

---

## 🤔 Options Considered

| Option | Pros | Cons |
|--------|------|------|
| **13 Categories** | Comprehensive, balanced | May be too many |
| 5 Categories | Simple | Too broad, hard to find |
| Flat structure | Simple | Scales poorly |
| Dynamic categories | Flexible | Inconsistent |

---

## ✅ Decision

**Use 13 fixed categories** numbered 01-13:

| # | Category | Purpose |
|---|----------|---------|
| 01 | project | Project overview |
| 02 | architecture | System design |
| 03 | decisions | ADRs |
| 04 | domain | Business logic |
| 05 | code | Code documentation |
| 06 | problems | Bugs & fixes |
| 07 | context | Sessions |
| 08 | people | Team info |
| 09 | external | APIs |
| 10 | testing | Tests |
| 11 | deployment | DevOps |
| 12 | roadmap | Plans |
| 13 | preferences | Settings |

---

## 📊 Consequences

### Positive
- Every project has same structure
- Easy to port between projects
- AI knows where to look

### Negative
- Some projects may not use all categories
- Adding new category is a breaking change
