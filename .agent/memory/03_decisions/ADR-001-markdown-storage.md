# ADR-001: Use Markdown for Storage

> **Status**: ✅ Active  
> **Date**: 2026-02-06  
> **Decision Makers**: dvgmdvgm

---

## 📋 Context

We need a storage format for the RLM-Anchor memory system that:
- Is human-readable without special tools
- Works well with version control (Git)
- Is understood natively by AI models
- Does not require runtime dependencies

---

## 🤔 Options Considered

| Option | Pros | Cons |
|--------|------|------|
| **Markdown** | Human-readable, Git-friendly, AI-native | No schema validation |
| SQLite | Queryable, structured | Not human-readable, needs tools |
| JSON | Structured, machine-readable | Hard to edit manually |
| YAML | Readable, structured | Less flexible for long content |
| XML | Well-defined | Too verbose |

---

## ✅ Decision

**Use Markdown (.md) files** for all storage.

---

## 📊 Consequences

### Positive
- Users can read/edit memory directly
- Perfect Git diffs
- No dependencies
- AI models understand natively

### Negative
- No schema enforcement
- No complex queries (solved by categories)

---

## 📝 Notes

This decision is foundational and unlikely to change.
