---
description: Validate memory structure integrity, find broken links and orphan files.
---

# /anchor_validate — Memory Validation

## Usage

```
/anchor_validate              # Full validation (5 checks)
/anchor_validate --fix        # Validate + auto-fix with confirmation
/anchor_validate --quick      # Quick sync check only (same as wakeup check)
```

---

## Execution Steps

### 0. Check Language Setting

```
Read .agent/memory/13_preferences/language_local.md (if exists, use it)
Otherwise read .agent/memory/13_preferences/language.md
All output must be in this language!
```

---

### Check 1: Category Structure

**Verify all 13 categories exist with required files:**

```
For each category 01_project through 13_preferences:
  ✅ Directory exists?
  ✅ _index.md exists?

Additionally:
  ✅ 03_decisions/_template.md exists?
  ✅ 06_problems/_template.md exists?
  ✅ 06_problems/bugs/README.md exists?
  ✅ 06_problems/workarounds/README.md exists?
  ✅ 07_context/current_session.md exists?
  ✅ 07_context/pending_tasks.md exists?
```

**Output:**

```
Check 1: Category Structure
✅ 13/13 categories have _index.md
✅ All required system files present
```

OR:

```
Check 1: Category Structure
❌ 04_domain/ — missing _index.md!
⚠️ 06_problems/ — missing _template.md
```

**Auto-fix:** Restore missing system files from default template.

---

### Check 2: Index ↔ Files Synchronization

> [!IMPORTANT]
> This is the most critical check. Detects ghost entries and orphan files.

**2.1. Get list of ALL .md files on disk:**

```
List all .md files in .agent/memory/ (excluding system files):
  Exclude: _index.md, _template.md, README.md, current_session.md, pending_tasks.md
  Exclude: all files in 13_preferences/ (these are settings, not entries)
  Result: list of "content files"
```

**2.2. Get list of files referenced in _index.md tables:**

```
For each category 01-12:
  Read _index.md
  Parse the file table (| File | Description | ... |)
  Extract all filenames from the first column
  Result: list of "indexed files"
```

**2.3. Compare the two lists:**

```
GHOST ENTRIES = files in index but NOT on disk
ORPHAN FILES  = files on disk but NOT in index
MATCHED       = files in both
```

**Output:**

```
Check 2: Index ↔ Files Sync

⚠️ Ghost entries (in index, file missing):
  01_project/_index.md → `techstack.md` — FILE NOT FOUND

⚠️ Orphan files (on disk, not in index):
  03_decisions/ADR-004-jwt.md — NOT IN INDEX

✅ Matched: 15/17 files synced correctly
```

**Auto-fix:**
- Ghost entry → Remove row from _index.md table (with confirmation)
- Orphan file → Read file, generate description, add row to _index.md

---

### Check 3: File Naming Conventions

**Verify files follow naming patterns:**

```yaml
NAMING_RULES:
  03_decisions:  "ADR-NNN-*.md"          # ADR-001-database-choice.md
  06_problems:   "PROB-NNN-*.md"         # PROB-001-cors-bug.md
  session_history: "session_YYYY-MM-DD*.md" or "digest_YYYY-MM.md"
  all_others:    "kebab-case.md"         # tech-stack.md, api-design.md
```

**Check each file:**
- Lowercase only (except ADR, PROB prefixes)?
- No spaces in filenames?
- Follows category-specific pattern?

**Output:**

```
Check 3: File Naming Conventions

⚠️ 03_decisions/my decision.md
   → Should be: ADR-NNN-my-decision.md

⚠️ 01_project/TechStack.md
   → Should be: techstack.md (lowercase)

✅ 14/16 files follow conventions
```

**Auto-fix:** Rename file + update reference in _index.md.

---

### Check 4: Broken Links

**Scan all .md files for internal links:**

```
Search for these patterns in all .md files inside .agent/memory/:
  - Markdown links: [text](relative/path.md)
  - Backtick references: `filename.md`
  - "See also" references: "See ADR-001" or "See PROB-003"
  
For each found reference:
  Check if the target file actually exists
```

**Output:**

```
Check 4: Broken Links

⚠️ 02_architecture/patterns.md:15
   Link to `ADR-001-database.md` → FILE NOT FOUND

⚠️ 06_problems/PROB-003.md:8
   Reference "See PROB-001" → FILE NOT FOUND (archived?)

✅ 12/14 links valid
```

**Auto-fix:**
- If target exists in archive → update link to archive path
- If target doesn't exist at all → mark as `[BROKEN LINK]`

---

### Check 5: Empty Files & Possible Duplicates

**5.1. Find empty or template-only files:**

```
Check all content files (not system files):
  - Size 0 bytes → EMPTY
  - Contains only template placeholders ("—", "YYYY-MM-DD") → TEMPLATE-ONLY
```

**5.2. Find possible duplicates:**

```
For each pair of files in the same category:
  Compare titles (H1 headers)
  If titles are >80% similar → POSSIBLE DUPLICATE
```

> [!NOTE]
> Duplicate detection is title-based only (fast).
> Full content comparison is not done (too expensive).

**Output:**

```
Check 5: Empty & Duplicates

⚠️ Empty files:
  05_code/temp-notes.md (0 bytes)

⚠️ Template-only files:
  08_people/author.md (only placeholders)

⚠️ Possible duplicates (similar titles):
  06_problems/PROB-001-cors.md
  06_problems/PROB-004-cors-again.md
  → Consider merging with /anchor_cleanup topics

✅ 13/15 files have meaningful content
```

**Auto-fix:**
- Empty files → delete (with confirmation)
- Template-only → warn (no auto-fix, user may not have filled it yet)
- Duplicates → suggest `/anchor_cleanup topics` (no auto-merge)

---

### Final Report

```
📋 VALIDATION REPORT
═════════════════════

| # | Check | Result | Issues |
|---|-------|--------|--------|
| 1 | Category Structure | ✅ OK | 0 |
| 2 | Index ↔ Files Sync | ⚠️ | 2 |
| 3 | File Naming | ⚠️ | 1 |
| 4 | Broken Links | ✅ OK | 0 |
| 5 | Empty & Duplicates | ⚠️ | 1 |

Total: 4 issues found
Auto-fixable: 3/4

🔧 Run auto-fix? [y/N/review]
  y      — fix all with confirmation for each
  N      — report only, no changes
  review — go through each issue one by one
```

---

## Quick Validation Mode

When called with `--quick` or from `/wakeup`:

**Only runs Check 2 (Index ↔ Files Sync) in a simplified way:**

```
Count content files on disk: N
Count entries across all _index.md tables: M
If N ≠ M → ⚠️ "Index out of sync (N files, M entries). Run /anchor_validate"
If N = M → ✅ (no detailed check)
```

This takes ~2 seconds and catches 80% of issues.
