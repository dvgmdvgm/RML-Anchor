---
description: Find and recall information from project memory
---

# /recall — Enhanced Memory Search

## Usage

```
/recall [query]              # Smart search (3 levels)
/recall --global [query]     # Search across linked projects too
```

---

## Execution Steps

// turbo-all

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language.md
All output must be in this language!
```

### 1. Parse Query

From the user's query, extract:
- **Keywords** (nouns, technical terms)
- **Intent** (looking for decision? bug fix? how-to? definition?)
- **Synonyms** (e.g., "auth" → also search "authentication", "login", "JWT")

> [!NOTE]
> The AI should think broadly about what the user might mean.
> "cors" → also consider "cross-origin", "preflight", "access-control"
> "db" → also consider "database", "PostgreSQL", "MySQL", "migration"

---

### 2. Level 1 — Index Search (fast, ~20 KB)

```
Read ALL 13 _index.md files simultaneously:
- .agent/memory/01_project/_index.md
- .agent/memory/02_architecture/_index.md
- .agent/memory/03_decisions/_index.md
- .agent/memory/04_domain/_index.md
- .agent/memory/05_code/_index.md
- .agent/memory/06_problems/_index.md
- .agent/memory/07_context/_index.md
- .agent/memory/08_people/_index.md
- .agent/memory/09_external/_index.md
- .agent/memory/10_testing/_index.md
- .agent/memory/11_deployment/_index.md
- .agent/memory/12_roadmap/_index.md
- .agent/memory/13_preferences/_index.md
```

**Search the file tables** in each _index.md for matches by:
- File name similarity
- Description similarity
- Synonym matching

**If matches found:**
→ Read the matched files
→ Extract relevant sections
→ Go to Step 5 (Format Response)

**If NO matches found:**
→ Continue to Level 2

---

### 3. Level 2 — Content Search (medium, grep)

> [!NOTE]
> Only runs if Level 1 found nothing.
> Uses grep/ripgrep to search inside file contents.

**3.1. Run grep across all memory files:**

```
Search for query keywords in ALL .md files inside .agent/memory/
Use case-insensitive search
Include file path, line number, and context line
```

**3.2. AI ranks grep results by relevance:**

For each grep hit, evaluate:
- Is this an exact match or partial?
- Is the surrounding context relevant to the query?
- Which category does the file belong to?

**3.3. Read top 3-5 most relevant files**

**If matches found:**
→ Extract relevant sections
→ Go to Step 5 (Format Response)

**If NO matches found:**
→ Continue to Level 3

---

### 4. Level 3 — Archive Search (slow, last resort)

> [!NOTE]
> Only runs if Levels 1 and 2 found nothing.
> Checks if the knowledge existed but was archived.

**4.1. Check Archived Entries tables:**

```
Search for "📦 Archived Entries" sections in all _index.md files
Look for matches in the archived file names and summaries
```

**4.2. If archived match found:**

→ Tell the user what was found and where it was archived
→ Offer to restore from archive:

```
📦 This knowledge was archived:

| Original File | Summary | Archived |
|---------------|---------|----------|
| PROB-002-memory-leak.md | WebSocket memory leak, fixed in v1.3 | 2026-03-01 |

Archive location: .agent/memory/archive/expired/2026-03/
Restore this file? [y/N]
```

**4.3. If nothing found anywhere:**

→ Go to Step 5 with "not found" result

---

### 4G. Global Search (only with --global flag)

> [!NOTE]
> Only runs when user explicitly uses `/recall --global [query]`
> Searches across linked projects defined in linked_projects.md

**4G.1. Read linked projects config:**

```
Read .agent/memory/13_preferences/linked_projects.md
Get list of project paths
```

**4G.2. For each linked project:**

```
Read ONLY their _index.md files (Level 1 search only!)
Do NOT grep their file contents (privacy)
Do NOT modify anything in their memory
```

**4G.3. If matches found in linked projects:**

→ Read the specific matched files from the linked project
→ Include in results with project label

---

### 5. Format Response

**If results found — show with source and match level:**

```
🔍 Search: "[query]"

Found N matches:

| # | File | Category | Level | Context |
|---|------|----------|-------|---------|
| 1 | ADR-004-jwt-auth.md | 03_decisions | 🟢 Index | JWT chosen for auth |
| 2 | api-design.md | 02_architecture | 🟡 Content | "...auth middleware..." |
| 3 | digest_2026-01.md | 07_context | 🟡 Content | "...discussed auth flow..." |

───────────────────────────

📄 [#1] ADR-004-jwt-auth.md
Source: memory/03_decisions/ADR-004-jwt-auth.md
Date: 2026-01-15

> [Relevant quote or summary from the file]

───────────────────────────

[Synthesized answer combining all sources]
```

**If global results found — add project labels:**

```
📂 Current project:
| # | File | Category | Context |
|---|------|----------|---------|
| 1 | ADR-004-jwt-auth.md | 03_decisions | JWT auth decision |

📂 Linked: API-Gateway (/projects/gateway/):
| # | File | Category | Context |
|---|------|----------|---------|
| 2 | ADR-002-rate-limiting.md | 03_decisions | Rate limit strategy |
```

**If nothing found — suggest alternatives:**

```
🔍 Search: "[query]"

❌ Not found in memory (searched all 3 levels).

Suggestions:
  💡 Try different keywords: [suggest synonyms]
  💡 Save this knowledge: /remember [topic]
  💡 Search linked projects: /recall --global [query]
```

---

## Search Levels Summary

| Level | What | Speed | When |
|-------|------|-------|------|
| 🟢 Level 1 | Index tables in _index.md | Fast (~20 KB) | Always first |
| 🟡 Level 2 | Grep inside file contents | Medium | If Level 1 empty |
| 🔴 Level 3 | Archived entries tables | Slow | If Level 2 empty |
| 🌐 Global | Linked projects indexes | Slow | Only with --global |

---

## Examples

### Example 1: Found at Level 1 (Index)

```
USER: /recall why PostgreSQL?

AI: 🔍 Search: "PostgreSQL"

    Found in memory (Level 1 — Index):

    📄 ADR-001-database-choice.md
    Source: memory/03_decisions/ADR-001-database-choice.md

    We chose PostgreSQL because:
    1. Complex JOIN queries needed
    2. ACID transactions for payment system
    3. Team experience with PostgreSQL

    Also considered: MongoDB (rejected — no transactions)
```

### Example 2: Found at Level 2 (Content grep)

```
USER: /recall something about cors

AI: 🔍 Search: "cors"

    Not in indexes. Searching content...

    Found 2 matches (Level 2 — Content):

    | # | File | Line | Context |
    |---|------|------|---------|
    | 1 | PROB-001-cors.md | 3 | "CORS preflight request blocked" |
    | 2 | api-design.md | 45 | "Added CORS middleware for..." |

    📄 [#1] PROB-001-cors.md
    Source: memory/06_problems/PROB-001-cors.md

    Problem: CORS preflight requests blocked by nginx
    Solution: Added Access-Control-Allow-Origin headers
    Status: ✅ Resolved
```

### Example 3: Found at Level 3 (Archived)

```
USER: /recall memory leak in websocket

AI: 🔍 Search: "memory leak websocket"

    Not in indexes. Not in content.
    Checking archives...

    📦 Found in archived entries:

    | Original File | Summary | Archived |
    |---------------|---------|----------|
    | PROB-002-memory-leak.md | WebSocket memory leak, fixed in v1.3 | 2026-03-01 |

    Archive: .agent/memory/archive/expired/2026-03/PROB-002-memory-leak.md
    Restore this file? [y/N]
```

### Example 4: Global search

```
USER: /recall --global rate limiting

AI: 🔍 Global Search: "rate limiting"

    📂 Current project (MyAPI):
    ❌ Not found

    📂 Linked: API-Gateway:
    📄 ADR-002-rate-limiting.md
    Source: /projects/gateway/.agent/memory/03_decisions/ADR-002-rate-limiting.md

    Decision: Token bucket algorithm, 100 req/min per user
    Rationale: Simple, predictable, easy to configure

    📂 Linked: Frontend-App:
    ❌ Not found
```

### Example 5: Nothing found

```
USER: /recall kubernetes deployment

AI: 🔍 Search: "kubernetes deployment"

    ❌ Not found in memory (all 3 levels searched).

    Suggestions:
      💡 Try: "docker", "deploy", "CI/CD", "container"
      💡 Save this knowledge: /remember kubernetes setup
      💡 Search other projects: /recall --global kubernetes
```
