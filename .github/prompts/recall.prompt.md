---
agent: agent
description: "Search and recall information from project memory (RLM-Anchor)"
---

# /recall — Search Memory

You are executing the **RLM-Anchor /recall** workflow.

The user wants to find information in the project's persistent memory system.

## Step 0: Check Language Setting

Read `.agent/memory/13_preferences/language_local.md` (if exists, use it).
Otherwise read `.agent/memory/13_preferences/language.md`.
Respond in this language!

## Step 1: Analyze Query

Understand what the user is looking for. Determine relevant categories based on keywords:

| Keywords | Categories to search |
|----------|---------------------|
| decision, why, chose, alternative | `03_decisions` |
| bug, error, fix, workaround | `06_problems` |
| architecture, design, pattern, flow | `02_architecture` |
| business logic, rule, workflow | `04_domain` |
| code, function, class, API, model | `05_code` |
| previous session, discussed, last time | `07_context` |
| deploy, server, environment | `11_deployment` |
| test, QA, edge case | `10_testing` |
| plan, future, tech debt, TODO | `12_roadmap` |
| preference, style, language | `13_preferences` |
| everything, all, general | All categories |

## Step 2: Search Memory

1. Read `_index.md` of each relevant category
2. Review file descriptions in the index
3. Read files that may contain the answer
4. Also check `.agent/memory/07_context/session_history/` for recent sessions

## Step 3: Present Results

Format found information clearly:

```
🔍 Memory search results:

📂 Category: [category name]
📄 File: [filename]

[Content summary or full content]

---

Found in N file(s) across M category(ies).
```

If nothing found:
```
🔍 Nothing found in memory for "[query]".

💡 Suggestion: Try /remember to save relevant information for next time.
```

## Step 4: Offer Follow-up

After presenting results, ask:
- "Want me to search more broadly?"
- "Want me to update this information?"
- "Want me to save something new related to this?"
