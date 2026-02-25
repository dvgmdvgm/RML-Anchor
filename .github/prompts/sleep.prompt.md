---
agent: agent
description: "End session — save context and summarize the work done (RLM-Anchor)"
---

# /sleep — End Session

You are executing the **RLM-Anchor /sleep** workflow. Follow these steps precisely:

## Step 0: Check Language Setting

Read `.agent/memory/13_preferences/language_local.md` (if exists, use it).
Otherwise read `.agent/memory/13_preferences/language.md`.
All output and saved entries must be in this language!

## Step 1: Summarize Current Session

Analyze the conversation and create a session summary:
- Main discussion topics
- Decisions made
- Files created/modified
- Important notes

**Write in configured language!**

## Step 2: Archive Session to History

```
Generate filename: session_YYYY-MM-DD_HH-MM.md
Copy current_session.md content → .agent/memory/07_context/session_history/[filename]
```

**Session file format:**

```markdown
# Session: YYYY-MM-DD HH:MM

## 📋 Discussion Topics
1. Topic 1
2. Topic 2

## ⚖️ Decisions Made
| Decision | Description | Impact |
|----------|-------------|--------|
| ... | ... | ... |

## 📁 Modified Files
| File | Change |
|------|--------|
| `file1.py` | Added auth logic |

## 📝 Notes
- Note 1

## ⏳ Pending (Carried Over)
| Priority | Task |
|----------|------|
| 🔴 | Task 1 |
```

## Step 3: Update pending_tasks.md

Update `.agent/memory/07_context/pending_tasks.md`:
- Add new pending tasks from this session
- Move completed tasks to "Recently Completed"

## Step 4: Reset current_session.md

Overwrite `.agent/memory/07_context/current_session.md` with blank template:

```markdown
# 📍 Current Session

- **Start Date**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD

---

## 🎯 Main Session Topics
1. —
2. —

---

## 💡 Key Decisions
| Decision | Description |
|----------|-------------|
| — | — |

---

## 📌 Topics Discussed
- —

---

## ⏳ Current Status
**Status**: Ready to start

---

## 📝 Notes
- —
```

## Step 5: Update Relevant Indexes

If new entries were created in other categories — update their `_index.md`.

Verify: every content file created/modified during this session is listed in its category's `_index.md`. If any orphan found → add it now.

## Step 5.7: Update Stats Log

Append one row to `.agent/memory/07_context/memory_stats_log.md`:
- **Date**: today's date
- **Sessions**: count files in session_history/
- **Entries**: count total content .md files across categories 01-12
- **Size**: total size of .agent/memory/ folder
- **Decisions**: count files in 03_decisions/
- **Problems**: count files in 06_problems/

## Step 6: Confirm to User

Output in configured language:

```
✅ Session ended!

📊 Session Statistics:
| Metric | Value |
|--------|-------|
| Duration | ~X hours |
| Decisions recorded | N |
| Files modified | M |

📁 Archived to:
- `session_history/session_YYYY-MM-DD_HH-MM.md`

📌 Carried to next session:
| Priority | Task |
|----------|------|
| 🔴 | Task 1 |

👋 See you later!
```
