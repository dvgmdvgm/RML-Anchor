---
agent: agent
description: "Start a work session — load project context and memory (RLM-Anchor)"
---

# /wakeup — Start Session

You are executing the **RLM-Anchor /wakeup** workflow. Follow these steps precisely:

## Step 1: Read Language Settings

Read the file `.agent/memory/13_preferences/language_local.md` (if it exists, use it).
Otherwise read `.agent/memory/13_preferences/language.md`.
Extract the `LANGUAGE=` value. **All subsequent output must be in this language!**

## Step 2: Read Main Memory Index

Read `.agent/MEMORY_INDEX.md`.
Output brief summary: how many categories, last update date.

## Step 3: Check for Unfinished Session

Read `.agent/memory/07_context/current_session.md`.

**If it contains actual data** (not just the blank template):
- Warn user: "Detected unfinished session from [date]. Data will be archived."
- Copy its content to `.agent/memory/07_context/session_history/session_YYYY-MM-DD_orphan.md`
- Reset `current_session.md` to the blank template

## Step 4: Load Session History

List files in `.agent/memory/07_context/session_history/`.
Read the last 2-3 session files for context.
Output: last session summary, key decisions.

## Step 5: Memory Health Check

Count files in `.agent/memory/07_context/session_history/`.
Count total `.md` files across all memory categories (01-12).

| Condition | Action |
|-----------|--------|
| Session files > 30 | ⚠️ Warn: "N session files. Consider /anchor-sync" |
| Session files > 100 | 🔴 Warn: "Memory overload! Recommend cleanup" |
| Total memory files > 100 | ⚠️ Warn: "N memory entries. Compression may help" |

## Step 6: Check Pending Tasks

Read `.agent/memory/07_context/pending_tasks.md` (if exists).
If there are pending tasks — display the list.

## Step 7: Load User Preferences

Read `.agent/memory/13_preferences/_index.md`.
Read `.agent/memory/13_preferences/communication.md` (if exists).
Apply response styling from preferences.

## Step 7.5: Output Critical Rules Reminder

Read `.github/copilot-instructions.md`.
Extract the CUSTOM PROJECT RULES section.
Display as a compact reminder block:

```
🔴 **CRITICAL RULES (active this session):**
- Language: [configured language]
- [Custom rule 1]
- [Custom rule 2]
```

## Step 8: Initialize New Session

Update `.agent/memory/07_context/current_session.md`:
- **Start Date**: current date/time
- **Status**: Active

## Step 9: Report Readiness

Output in configured language:

```
✅ Session started!

📊 Memory Statistics:
| Category | Status |
|----------|--------|
| Categories loaded | 13 |
| Memory entries | N |
| Session files | N |
| Last session | YYYY-MM-DD |

📅 Previous Session Summary:
| Topic | Decision |
|-------|----------|
| ... | ... |

📌 Pending Tasks:
| Priority | Task |
|----------|------|
| 🔴 High | Task 1 |

⚠️ Memory Health: [OK / Warning / Critical]

💡 Ready to work! What shall we do today?
```
