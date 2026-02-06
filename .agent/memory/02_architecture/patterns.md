# 🎨 Design Patterns

> **Created**: 2026-02-06  
> **Last Updated**: 2026-02-06  

---

## 📋 Patterns Used

| Pattern | Where Applied | Why |
|---------|---------------|-----|
| **Category Pattern** | 13 memory folders | Logical organization |
| **Index Pattern** | _index.md in each folder | Navigation & discovery |
| **Template Pattern** | _template.md files | Consistency |
| **Command Pattern** | /slash commands | User interface |
| **Observer Pattern** | Session tracking | State capture |

---

## 📂 Category Pattern

Each knowledge type has its own folder:

```
memory/
├── 01_project/     # What the project is
├── 02_architecture/ # How it's built
├── 03_decisions/   # Why choices were made
...
└── 13_preferences/ # User settings
```

**Benefits**:
- Clear separation of concerns
- Easy to find relevant info
- Supports partial access

---

## 📑 Index Pattern

Every category has `_index.md`:

```markdown
# Category Name

## Files in This Category
| File | Description | Updated |
|------|-------------|---------|
| file1.md | ... | ... |

## When to Access
- "Question 1?"
- "Question 2?"
```

**Benefits**:
- AI knows what's available
- No need to scan all files
- Self-documenting

---

## 📝 Template Pattern

Standardized templates for entries:

```markdown
# Title

> **Created**: YYYY-MM-DD
> **Last Updated**: YYYY-MM-DD

## Content

...
```

**Benefits**:
- Consistent structure
- Easier parsing
- Professional look

---

## ⚡ Command Pattern

All user interactions via `/commands`:

| Command | Action |
|---------|--------|
| `/wakeup` | Initialize session |
| `/sleep` | End session |
| `/remember` | Store knowledge |
| `/recall` | Retrieve knowledge |

**Benefits**:
- Intuitive UX
- Easy to remember
- Extensible
