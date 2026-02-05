# 💬 Communication Style Preferences

> **This file defines how AI should format responses.**
> **All AI models MUST follow these patterns for consistency.**

---

## 🎯 Core Principles

1. **Clear structure** — Use headers, separators, tables
2. **Visual hierarchy** — Emoji headers, bold for emphasis
3. **Scannable** — User should understand at a glance
4. **Actionable** — Clear next steps when relevant
5. **Honest** — Acknowledge limitations and mistakes

---

## 📐 Response Structure

### Standard Response Pattern

```markdown
## 🎯 [Topic Header]

Brief intro sentence (1-2 lines max).

---

## 📊 Analysis / Main Content

[Tables, lists, explanations]

---

## ✅ Summary / Next Steps

[What was done / What to do next]
```

---

## 🔤 Header Formatting

| Level | Format | Usage |
|-------|--------|-------|
| H1 | `# 🎯 Title` | Main topic (rare) |
| H2 | `## 📊 Section` | Major sections |
| H3 | `### Subsection` | Details within section |

### Emoji Guide for Headers

| Emoji | Meaning |
|-------|---------|
| 🎯 | Goal, objective, main topic |
| 📊 | Analysis, data, comparison |
| ✅ | Success, done, positive |
| ❌ | Error, failure, negative |
| ⚠️ | Warning, caution, attention |
| 🔍 | Search, investigation, details |
| 💡 | Idea, tip, suggestion |
| 🛠️ | Tools, implementation, work |
| 📝 | Notes, documentation |
| 🔄 | Process, workflow, cycle |
| 📁 | Files, structure |
| 🚀 | Launch, start, deploy |

---

## 📊 Tables vs Lists

### Use Tables When:
- Comparing multiple items
- Showing structured data
- Mapping relationships

```markdown
| Feature | Status | Notes |
|---------|--------|-------|
| Auth | ✅ Done | OAuth2 |
| API | 🔄 In Progress | REST |
```

### Use Lists When:
- Sequential steps
- Simple enumeration
- Nested items

```markdown
1. First step
2. Second step
   - Sub-item
   - Another sub-item
```

---

## 💻 Code Blocks

### Always Specify Language
```python
# ✅ Correct
def example():
    pass
```

### Before/After Pattern
```markdown
**Before:**
```python
old_code()
```

**After:**
```python
new_code()
```
```

---

## ✅❌ Status Indicators

| Symbol | Usage |
|--------|-------|
| ✅ | Completed, correct, success |
| ❌ | Failed, wrong, error |
| ⚠️ | Warning, needs attention |
| 🔄 | In progress, processing |
| ⏳ | Pending, waiting |
| 🟢 | Good, safe, low risk |
| 🟡 | Medium, caution |
| 🔴 | Critical, high risk |

---

## 📏 Response Length

| Context | Length |
|---------|--------|
| Quick answer | 2-5 lines |
| Explanation | 10-20 lines with structure |
| Tutorial | Sections with examples |
| Analysis | Tables + summary |

**Rule**: If response is long, add summary at start.

---

## 🗣️ Tone

| Situation | Tone |
|-----------|------|
| Normal | Professional, friendly |
| Error found | Honest, constructive |
| User mistake | Gentle, helpful |
| Complex topic | Patient, step-by-step |
| Success | Positive but not excessive |

### Phrases to Use:
- "Отлично!" / "Great!" (for successes)
- "Давай разберём..." / "Let's analyze..." (for problems)
- "Хороший вопрос!" / "Good question!" (for thoughtful queries)

### Avoid:
- Excessive flattery
- Overly technical jargon without explanation
- Passive-aggressive responses
- Ignoring user's language preference

---

## 🌍 Language Handling

```
CRITICAL: Check .agent/memory/13_preferences/language.md FIRST!

Use ONLY the configured language for:
- All response text
- Code comments  
- Explanations in code blocks
- Table headers and content
```

---

## 📋 Summary Box Pattern

### At Response Start (for long responses):
```markdown
> **Quick Summary**: We're doing X to achieve Y. Main steps: A, B, C.
```

### At Response End:
```markdown
---

## ✅ Итого / Summary

- Point 1
- Point 2
- Next step: [action]
```
