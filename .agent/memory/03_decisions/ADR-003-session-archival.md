# ADR-003: Session Archival

> **Status**: ✅ Active  
> **Date**: 2026-02-06  
> **Decision Makers**: dvgmdvgm

---

## 📋 Context

We need a strategy for preserving session context:
- Sessions should be recoverable
- History should be searchable
- Old sessions shouldn't clutter current context

---

## 🤔 Options Considered

| Option | Pros | Cons |
|--------|------|------|
| **Archive to history/** | Searchable, preserved | More files |
| Overwrite current | Simple | Loses history |
| Keep all in one file | Single file | Gets huge |
| Delete old | Saves space | Loses context |

---

## ✅ Decision

**Archive each session to `session_history/`** with timestamp:

```
session_history/
├── session_2026-02-05_14-30.md
├── session_2026-02-06_09-15.md
└── session_2026-02-06_18-00.md
```

---

## 📊 Consequences

### Positive
- Full history available
- Can search past sessions
- Can summarize periodically

### Negative
- Many files accumulate (solved by `/anchor_cleanup`)

---

## 📝 Implementation

- `/sleep` creates archive file
- Filename: `session_YYYY-MM-DD_HH-MM.md`
- `/wakeup` loads recent sessions
- `/anchor_cleanup` summarizes old sessions
