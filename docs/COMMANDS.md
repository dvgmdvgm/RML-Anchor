# RLM-Anchor: Complete Command Reference

## Detailed Description of Each Command in the Persistent Memory System

*Author: dvgmdvgm*  
*Last update: February 2026*

---

## Table of Contents

| # | Command | Category | Purpose |
|---|---------|----------|---------|
| 1 | [`/wakeup`](#1-wakeup--awakening) | 🟢 Core | Start session |
| 2 | [`/sleep`](#2-sleep--session-end) | 🟢 Core | End session |
| 3 | [`/remember`](#3-remember--memorization) | 🟢 Core | Save to memory |
| 4 | [`/recall`](#4-recall--recollection) | 🟢 Core | Search in memory |
| 5 | [`/anchor_agent`](#5-anchor_agent--project-installation) | 🔧 System | Install in project |
| 6 | [`/anchor_briefing`](#6-anchor_briefing--full-briefing) | 📊 Analytics | Full project overview |
| 7 | [`/memory-stats`](#7-memory-stats--statistics) | 📊 Analytics | Memory statistics |
| 8 | [`/anchor_backup`](#8-anchor_backup--backup) | 🛡️ Maintenance | Create backup |
| 9 | [`/anchor_restore`](#9-anchor_restore--restoration) | 🛡️ Maintenance | Restore from backup |
| 10 | [`/anchor_cleanup`](#10-anchor_cleanup--smart-cleanup) | 🛡️ Maintenance | Memory cleanup |
| 11 | [`/anchor_update`](#11-anchor_update--system-update) | 🛡️ Maintenance | Update from GitHub |
| 12 | [`/anchor_validate`](#12-anchor_validate--memory-validation) | 🛡️ Maintenance | Integrity check |
| 13 | [`/anchor_remove`](#13-anchor_remove--system-removal) | 🛡️ Maintenance | Safe removal |
| 14 | [`/handoff`](#14-handoff--context-transfer) | 🔄 Context | Transfer between models |
| 15 | [`/walkthrough`](#15-walkthrough--feature-documentation) | 📝 Documentation | Work documentation |

---

## Core Commands

These four commands are the heart of the system. They cover the basic workflow cycle: start session → work → save knowledge → find knowledge → end session.

---

## 1. `/wakeup` — Awakening

### Why It Exists

Every AI assistant starts a session with a clean slate. It knows nothing about your project, past decisions, or current tasks. `/wakeup` solves this problem: it loads context, restores state, and brings the AI "up to speed."

It's like a morning briefing for a colleague who just returned from vacation. Instead of you explaining everything yourself — they read the journal and get back to work on their own.

### When to Call

- **At the beginning of each new session** with AI
- **When switching chats** (new dialog in IDE)
- **After a long break** from work

### How It Works Inside

```
Step 1: Read language settings
         │
         │  Reads .agent/memory/13_preferences/language.md
         │  Determines language: en, ru, es, de...
         │  ALL further work proceeds in this language
         ▼
Step 2: Load main index
         │
         │  Reads .agent/MEMORY_INDEX.md
         │  Gets map of all 13 categories
         │  Sees how many entries and when they were updated
         ▼
Step 3: Check for unfinished session
         │
         │  Reads .agent/memory/07_context/current_session.md
         │  If there's data (not template) — this means
         │  the previous session was NOT ended via /sleep
         │
         ├── Data exists? → Archives as "orphan" session
         │                   and warns user
         └── Empty? → Continues normally
         ▼
Step 4: Load session history
         │
         │  Reads last 2-3 files from
         │  .agent/memory/07_context/session_history/
         │  Extracts: topics, decisions, notes
         ▼
Step 5: Check pending tasks
         │
         │  Reads .agent/memory/07_context/pending_tasks.md
         │  Shows tasks with priorities
         ▼
Step 6: Load preferences
         │
         │  Reads coding style, communication preferences
         │  Applies to its behavior
         ▼
Step 7: Initialize new session
         │
         │  Updates current_session.md
         │  Sets status: Active
         ▼
Step 8: Report to user
         │
         └── Outputs: statistics, past decisions,
             pending tasks, readiness to work
```

### Why It Was Added

Without this command, every session starts "from zero." Users spend 15–20 minutes re-explaining context. `/wakeup` automates this process and reduces time to just a few seconds.

### Usage Example

```
User: /wakeup

AI: 🚀 Loading project context...

    ✅ Session started!
    
    📊 Project memory:
    | Parameter | Value |
    |-----------|-------|
    | Categories | 13 |
    | Entries | 15 |
    | Last session | 2026-02-06 |
    
    📅 Previous session (2026-02-06):
    | Topic | Decision |
    |-------|----------|
    | Architecture | 5-layer model |
    | Storage | Markdown files |
    
    📌 Pending tasks:
    | Priority | Task |
    |----------|------|
    | 🔴 | Fix CORS bug |
    
    💡 What shall we work on today?
```

---

## 2. `/sleep` — Session End

### Why It Exists

If `/wakeup` is loading context, then `/sleep` is saving it. Without this command, all work from the current session — discussions, decisions, discoveries — simply disappears. `/sleep` captures everything that happened and saves it to history.

It's like a work journal that's automatically filled out and put on the shelf — so tomorrow you can open it and remember where you left off.

### When to Call

- **At the end of a work session** (before closing the dialog)
- **Before a long break**
- **Before switching AI models** (before `/handoff`)
- **When you need to capture progress** intermittently

### How It Works Inside

```
Step 1: Read language settings
         │
         └── Determines language for archival
         ▼
Step 2: Session summarization
         │
         │  AI analyzes the entire current dialog and creates:
         │  - List of discussed topics
         │  - Decisions made
         │  - List of modified files
         │  - Important notes
         ▼
Step 3: Archive to history
         │
         │  Generates filename: session_YYYY-MM-DD_HH-MM.md
         │  Saves to .agent/memory/07_context/session_history/
         ▼
Step 4: Update pending_tasks.md
         │
         │  New incomplete tasks → adds
         │  Completed tasks → moves to "Recently Completed"
         ▼
Step 5: Reset current_session.md
         │
         │  Overwrites with empty template
         │  Next session will start clean
         ▼
Step 6: Update indices
         │
         │  If new entries were created in other categories
         │  → updates their _index.md files
         ▼
Step 7: Report to user
         │
         └── Shows statistics and tasks for next time
```

### Why It Was Added

Without session archival, every day starts from zero. With it — each subsequent `/wakeup` loads more and more context. Memory **accumulates**, rather than being lost.

### Usage Example

```
User: /sleep

AI: 📝 Summarizing session...

    ✅ Session complete!
    
    📊 Today:
    | Metric | Value |
    |--------|-------|
    | Duration | ~3 hours |
    | Decisions recorded | 2 |
    | Files modified | 8 |
    
    📁 Archived:
    session_history/session_2026-02-07_17-30.md
    
    📌 For next time:
    | Priority | Task |
    |----------|------|
    | 🔴 | Finish authorization |
    | 🟡 | Write tests |
    
    👋 See you later!
```

---

## 3. `/remember` — Memorization

### Why It Exists

During work, important knowledge is constantly generated: architecture decisions, found bugs and their solutions, business logic rules, API configurations. Without `/remember`, this knowledge exists only in the current chat window and disappears after closing.

`/remember` is the "write this down forever" command. It doesn't just copy text to a file — it **analyzes**, **categorizes**, and **structures** information, saving it to the correct memory category.

### When to Call

- **Made an important decision** (which database was chosen and why)
- **Found and fixed a bug** (so you don't waste time next time)
- **Discovered a nuance** of business logic (a rule that's easy to forget)
- **Configured an external API** (keys, endpoints, quirks)
- **Want to capture** any information for future sessions

### How It Works Inside

```
Step 1: Read language settings
         │
         └── Entry will be in user's language
         ▼
Step 2: Determine category
         │
         │  If user specified:
         │    /remember decisions we chose PostgreSQL
         │    → Category: 03_decisions
         │
         │  If not specified:
         │    /remember found CORS bug
         │    AI determines itself → 06_problems
         │
         │  Auto-detection table:
         │  ┌─────────────────────────────────────────┐
         │  │ Context             → Category          │
         │  │─────────────────────────────────────────│
         │  │ decision, choice    → 03_decisions      │
         │  │ bug, error, fix     → 06_problems       │
         │  │ function, class, API → 05_code          │
         │  │ external API        → 09_external       │
         │  │ plan, idea, TODO    → 12_roadmap        │
         │  │ preference          → 13_preferences    │
         │  └─────────────────────────────────────────┘
         ▼
Step 3: Read category index
         │
         │  Opens _index.md of selected category
         │  Checks: is there already an entry on this topic?
         ▼
Step 4: Create or update file
         │
         │  New topic → creates file from _template.md
         │  Existing → updates existing file
         ▼
Step 5: Update index
         │
         │  Adds new file to _index.md table
         ▼
Step 6: Confirmation
         │
         └── ✅ Saved to memory/03_decisions/ADR-004-postgresql.md
```

### Why It Was Added

Human memory is unreliable. AI memory — doesn't exist between sessions. `/remember` creates a **third memory** — external, persistent, categorized. This guarantees that no important decision will be lost.

### Usage Example

```
User: /remember We decided to use JWT for authorization
      because we need stateless architecture and horizontal
      scaling. Session-based was rejected due to problems
      with the load balancer.

AI: 📝 Analyzing content...
    → Category: 03_decisions (architectural decision)
    → Creating: ADR-004-jwt-auth.md
    
    ✅ Saved to memory/03_decisions/ADR-004-jwt-auth.md
    
    Contents:
    | Parameter | Value |
    |-----------|-------|
    | Decision | JWT for authorization |
    | Rationale | Stateless, scaling |
    | Rejected | Session-based (load balancer) |
```

---

## 4. `/recall` — Recollection

### Why It Exists

What's the point of memory if you can't quickly find what you need? `/recall` is the search command across all saved memory. It finds decisions, bugs, architectural notes, business rules — everything that was saved via `/remember` or recorded automatically.

It's like a search engine for your corporate knowledge base, but with context understanding and natural language.

### When to Call

- **"Why did we choose PostgreSQL?"** — will find ADR with justification
- **"How did we solve the CORS bug?"** — will find description and solution
- **"What are the Stripe API keys?"** — will find configuration
- **"What did we discuss last week?"** — will find session history
- Any question about past knowledge

### How It Works Inside

```
Step 1: Read language settings
         ▼
Step 2: Analyze query
         │
         │  Extracts keywords from user's question
         │  Determines which categories to search:
         │
         │  "why did we choose PostgreSQL?" → 03_decisions
         │  "authorization bug"              → 06_problems
         │  "Stripe API"                     → 09_external
         │  "what did we discuss yesterday?" → 07_context
         ▼
Step 3: Read category indices
         │
         │  For each relevant category reads _index.md
         │  Finds files matching by description
         ▼
Step 4: Extract information
         │
         │  Reads found files
         │  Extracts relevant sections
         ▼
Step 5: Form response
         │
         │  Synthesizes answer from found data
         │  Indicates sources (file path, date)
         │
         └── If nothing found → suggests saving
```

### Why It Was Added

Without memory search, users must manually open files, remember names, search in folders. `/recall` transforms memory from passive storage into an **active assistant** that instantly delivers needed information.

### Usage Example

```
User: /recall how did we solve the Google OAuth problem?

AI: 📁 Found in memory:

    Source: memory/06_problems/PROB-003-google-oauth.md
    Date: 2026-01-20
    
    > Problem: redirect_uri was using http instead of https.
    > Browser blocked redirect due to mixed content.
    >
    > Solution: Changed URI in Google Cloud Console to https://
    > and added protocol check in settings.py
    
    Affected files: settings.py, config.py
```

---

## System Commands

---

## 5. `/anchor_agent` — Project Installation

### Why It Exists

RLM-Anchor needs to be installed in every project where you want to use persistent memory. But your project might already have a `.agent/` folder with IDE configurations, other workflows, rules. `/anchor_agent` **safely** integrates the system without breaking the existing structure.

Additionally, many IDEs use their own rules files: `GEMINI.md`, `.cursorrules`, `.windsurfrules`. This command automatically **finds and imports** data from such files into the RLM memory structure, so everything is in one place.

### When to Call

- **Once during first installation** of RLM-Anchor in a new project
- **When migrating** between IDEs (data from IDE rules will be imported)
- **After cloning a project** with RLM-Anchor already installed

### How It Works Inside

```
Step 1: Read language settings
         ▼
Step 2: Search for IDE rules files
         │
         │  Scans project root for:
         │  GEMINI.md, .cursorrules, .windsurfrules,
         │  .github/copilot-instructions.md, CLAUDE.md...
         │
         │  If found → parses and prepares for import
         ▼
Step 3: Import IDE rules
         │
         │  Distributes data across categories:
         │  ┌──────────────────┬──────────────────────┐
         │  │ Coding style     → 13_preferences/      │
         │  │ Tech stack       → 01_project/          │
         │  │ Business rules   → 04_domain/           │
         │  │ Architecture     → 02_architecture/     │
         │  └──────────────────┴──────────────────────┘
         ▼
Step 4: Scan .agent/
         │
         │  Checks which files already exist
         │  Compiles conflict report
         ▼
Step 5: Offer options
         │
         │  1. SAFE — only non-conflicting files
         │  2. MERGE — merge with existing
         │  3. FULL — full installation (with backup)
         │  4. CANCEL — cancel
         ▼
Step 6: Execute chosen option
         │
         │  Creates structure:
         │  .agent/memory/ (13 categories)
         │  .agent/MEMORY_INDEX.md
         │  .agent/skills/MEMORY_SKILL.md
         │  .agent/workflows/ (all commands)
         ▼
Step 7: Validation
         │
         │  Checks: all files created?
         │  Indices correct? Language set?
         ▼
Step 8: Report (including IDE rules import)
         │
         └── Shows: what was created, what was imported,
             recommends removing original IDE rules files
```

### Why It Was Added

Users work in different IDEs with different configurations. You can't just "copy the folder" — it might break their settings. `/anchor_agent` is a **safe installer** that analyzes the situation, warns about conflicts, and offers choices.

IDE rules import — because information shouldn't be duplicated. If the user already has `GEMINI.md` with rules — why keep them separate from the memory system?

---

## Analytics Commands

---

## 6. `/anchor_briefing` — Full Briefing

### Why It Exists

Sometimes you need a **complete overview** of everything the system knows about the project. Not fragmentary (like `/recall`), but holistically — from project description to future plans. It's like an executive summary, but automatically generated from real memory data.

### When to Call

- **When onboarding** a new team member (or new AI model)
- **After a long break** from work (weeks/months)
- **For knowledge audit** — what does the system know, and what doesn't it
- **Before strategic decisions** — need the full picture

### How It Works Inside

```
Step 1: Read language settings
         ▼
Step 2: Sequential scanning of ALL 13 categories
         │
         │  For each category:
         │  1. Reads _index.md
         │  2. If there's content → reads key files
         │  3. If empty → marks "No entries"
         ▼
Step 3: Generate full report
         │
         │  Forms structured document with ALL
         │  13 sections: project, architecture, decisions, domain,
         │  code, problems, context, people, external integrations,
         │  testing, deployment, roadmap, preferences
         ▼
Step 4: Add statistics
         │
         └── Summary table: how many entries in each category
```

### Why It Was Added

This is the **heaviest** command in the system — it reads everything. But that's exactly why it's the most valuable for situations when you need the complete picture. Without it, users would have to manually open all 13 categories and read every file.

---

## 7. `/memory-stats` — Statistics

### Why It Exists

A quick way to check the state of the memory system without reading all files. How many entries? Which categories are filled? What's empty? When was data last updated?

### When to Call

- **For a quick check** of memory status
- **After a series of `/remember`** — to confirm everything was saved
- **To assess** completeness — which categories need attention

### How It Works Inside

Simple command: goes through all 13 categories, counts files (excluding `_index.md` and `_template.md`), collects last update dates and outputs a summary table with recommendations.

### Why It Was Added

Sometimes you don't need a full briefing — just numbers. "How many entries?", "What's empty?". `/memory-stats` answers in seconds.

### Usage Example

```
User: /memory-stats

AI: 📊 PROJECT MEMORY STATISTICS

    | # | Category | Entries | Updated |
    |---|----------|---------|---------|
    | 01 | PROJECT | 3 | 2026-02-06 |
    | 02 | ARCHITECTURE | 3 | 2026-02-06 |
    | 03 | DECISIONS | 3 | 2026-02-06 |
    | 04 | DOMAIN | 0 | — |
    | 05 | CODE | 0 | — |
    | 06 | PROBLEMS | 0 | — |
    | 07 | CONTEXT | 2 | 2026-02-07 |
    | 08 | PEOPLE | 0 | — |
    | 09 | EXTERNAL | 0 | — |
    | 10 | TESTING | 0 | — |
    | 11 | DEPLOYMENT | 0 | — |
    | 12 | ROADMAP | 3 | 2026-02-06 |
    | 13 | PREFERENCES | 8 | 2026-02-07 |
    
    📈 Total: 22 entries
    💾 Size: ~35 KB
    
    📌 Recommendations:
    - Add business logic (04_domain is empty)
    - Document problems (06_problems is empty)
```

---

## Maintenance Commands

---

## 8. `/anchor_backup` — Backup

### Why It Exists

Memory is valuable. Losing months of accumulated knowledge due to an accidental `rm -rf` or disk failure is unacceptable. `/anchor_backup` creates a complete ZIP archive of the entire memory system.

Important detail: the backup includes **only RLM-Anchor files** (strict list). Your own IDE configurations in `.agent/` are not touched and don't go into the archive. This protects privacy and reduces backup size.

### When to Call

- **Before major changes** to the project
- **Before cleanup** (`/anchor_cleanup`)
- **For transferring** the project to another computer
- **Periodically** for insurance (once a week)

### How It Works Inside

Creates a ZIP archive of strictly defined files (13 memory categories, scripts, skills, workflows, index) in `.agent/backups/` folder with name `anchor_backup_YYYY-MM-DD_HH-MM.zip`. Automatically deletes old backups if there are more than 5 (configurable).

### Why It Was Added

Any data storage system must have a backup mechanism. This is basic engineering discipline.

---

## 9. `/anchor_restore` — Restoration

### Why It Exists

The reverse operation: restore the system from backup. Works when transferring to another computer, rolling back to a previous state, or after a disaster.

### When to Call

- **When transferring** project to another computer
- **For rollback** to previous state
- **After accidental deletion** of files
- **When migrating** between IDEs

### How It Works Inside

```
Step 1: Validate ZIP file
         │
         │  Checks: exists? Correct structure?
         │  Contains memory/, workflows/, MEMORY_INDEX?
         ▼
Step 2: Check existing installation
         │
         │  If .agent/ already exists → offers:
         │  1. Overwrite (with backup of current)
         │  2. Merge
         │  3. Cancel
         ▼
Step 3: Create safety backup of current state
         │
         │  pre_restore_backup_YYYY-MM-DD_HH-MM.zip
         ▼
Step 4: Extract archive
         ▼
Step 5: Verify restoration
         │
         └── Checks key files → report
```

### Why It Was Added

`/anchor_backup` without `/anchor_restore` is useless. This is a paired command: backup creates a copy, restore recovers from it.

---

## 10. `/anchor_cleanup` — Smart Cleanup

### Why It Exists

Over time, memory grows. Old sessions accumulate, outdated problems take up space, duplicates appear. Without cleanup, the relevance coefficient (R) drops — AI spends more context reading irrelevant data.

`/anchor_cleanup` is not dumb deletion. This is **intelligent cleanup** with a scoring system, TTL, summarization, and safe backups.

### When to Call

- **Once a month** for maintenance
- **When `/memory-stats` shows** many entries
- **If AI becomes slower** loading context
- **Before an important project phase** (clear out the outdated)

### How It Works Inside

```
Step 1: Load cleanup settings
         │
         │  From .agent/memory/13_preferences/cleanup_settings.md
         │  TTL by category, scoring thresholds, actions
         ▼
Step 2: Scan all files
         │
         │  For each: creation date, size, category
         ▼
Step 3: Calculate importance score
         │
         │  Importance = BASE_WEIGHT[category]
         │             × RECENCY_FACTOR
         │             × ACCESS_FACTOR
         │             × EXPLICIT_BOOST
         │
         │  File categorization:
         │  🟢 KEEP     (Score > 0.7)   — don't touch
         │  🟡 REVIEW   (Score 0.4-0.7) — ask user
         │  🟠 SUMMARIZE (old sessions) — combine into digest
         │  🔴 ARCHIVE  (Score 0.2-0.4) — move to archive
         │  ⚫ DELETE   (Score < 0.2)   — delete (with backup)
         ▼
Step 4: Show report to user
         │
         │  Detailed table for each action
         │  User confirms or cancels
         ▼
Step 5: Execute
         │
         │  ✓ Summarization: 8 sessions → 1 digest
         │  ✓ Archival: move to .agent/archive/
         │  ✓ Deletion: with automatic backup
         ▼
Step 6: Results report
```

### Why It Was Added

A system without maintenance degrades. `/anchor_cleanup` is a **garbage collector** for memory. It ensures memory stays efficient and relevant, rather than turning into a dump of outdated data.

---

## 11. `/anchor_update` — System Update

### Why It Exists

RLM-Anchor is an evolving product. New commands appear, workflows improve, bugs are fixed. Without an update mechanism, users must manually download new versions, compare files, transfer data. `/anchor_update` automates this process, **guaranteeing preservation of all user data**.

It's like `apt upgrade` or `npm update`, but for a memory system — considering that this isn't just code, but a knowledge store.

### When to Call

- **Periodically** (once a week/month) to get improvements
- **When you learn about a new version** from changelog or notification
- **Before a big project** — ensure you're using the latest version
- **With `--check` flag** — only check if updates are available

### How It Works Inside

```
Step 1: Check current version
         │
         │  Reads .agent/VERSION
         │  Compares with latest on GitHub
         │
         ├── Versions equal? → ✅ Already up to date
         └── Newer exists? → Continue
         ▼
Step 2: Create backup
         │
         │  Backup current .agent/ to .agent/backups/pre_update_vX.Y.Z/
         │  This is insurance in case of problems
         ▼
Step 3: Download new version
         │
         │  git clone --depth 1 to temporary folder
         ▼
Step 4: Classify files
         │
         │  ┌──────────────────────────────────────────────┐
         │  │ 🟢 OVERWRITE — completely replace:           │
         │  │    workflows, scripts, MEMORY_INDEX.md       │
         │  │                                               │
         │  │ 🟡 SMART_MERGE — merge preserving data:      │
         │  │    _index.md files, preference settings      │
         │  │                                               │
         │  │ 🔴 NEVER_TOUCH — don't touch:                │
         │  │    language.md, session_history/,            │
         │  │    all user entries                          │
         │  └──────────────────────────────────────────────┘
         ▼
Step 5: Apply changes
         │
         │  For OVERWRITE: simple file replacement
         │  For SMART_MERGE: preserve user data
         │     in _index.md tables + update structure
         ▼
Step 6: Localization
         │
         │  If user language ≠ en:
         │    Translate all updated files to user language
         ▼
Step 7: Cleanup and report
         │
         │  Delete temporary files
         └── Show: what was updated, where backup is,
             what's new in this version
```

### Why It Was Added

A self-updating system is a sign of a mature product. Without it, users get stuck on old versions or are afraid to update due to risk of losing data. `/anchor_update` **removes this fear**: it guarantees updates are safe.

### Usage Example

```
User: /anchor_update --check

AI: 📦 Checking for updates...
    
    Current version: 2.0.3
    Latest version: 2.1.0
    
    ✨ Update available!
    Run /anchor_update to install.
```

```
User: /anchor_update

AI: 🔄 Updating RLM-Anchor...
    
    📦 Creating backup...
    ✅ Backup: .agent/backups/pre_update_v2.0.3_2026-02-07/
    
    📥 Downloading v2.1.0...
    
    📊 Changes:
    | Action | Files | Details |
    |--------|-------|---------|
    | 🟢 Replaced | 12 | workflows, scripts |
    | 🟡 Merged | 13 | indexes (preserved 45 entries) |
    | 🆕 Added | 2 | new files |
    | 🔴 Untouched | 8 | your data |
    | 🌐 Translated | 26 | to your language |
    
    ✅ UPDATE COMPLETE: v2.0.3 → v2.1.0
    
    📋 What's new:
    - Added /anchor_validate command
    - Improved Smart Merge algorithm
    - Fixed template localization
```

---

## 12. `/anchor_validate` — Memory Validation

### Why It Exists

Over time, inconsistencies can appear in the memory system: a file was deleted but the index entry remains; a file was created manually but not registered; a link points to a non-existent file. `/anchor_validate` is a **health check** for memory that finds all such problems.

It's like `fsck` for a filesystem or a linter for code — a tool that finds problems before they become critical.

### When to Call

- **After manual editing** of memory files
- **If something seems wrong** — `/recall` doesn't find what should be there
- **Periodically** for maintenance (once a month)
- **After restoring from backup** — to confirm everything is in place

### How It Works Inside

```
┌──────────────────────────────────────────────────────────────┐
│                          5 CHECKS                             │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ CHECK 1: Category Structure                                   │
│ ───────────────────────────                                  │
│   Do all 13 directories exist?                               │
│   Does each have _index.md?                                  │
│   Are system files in place (_template.md, current_session)? │
│                                                              │
│ CHECK 2: Index ↔ Files Synchronization                       │
│ ───────────────────────────────────                          │
│   GHOST ENTRIES = entries in index with no file on disk      │
│   ORPHAN FILES = files on disk with no entry in index        │
│                                                              │
│ CHECK 3: File Naming                                          │
│ ──────────────────────────                                   │
│   ADR-NNN-*.md for decisions?                                │
│   PROB-NNN-*.md for problems?                                │
│   kebab-case for others?                                     │
│                                                              │
│ CHECK 4: Broken Links                                         │
│ ─────────────────────                                        │
│   Do all Markdown links lead to existing files?              │
│   Do all "See ADR-001" reference real entries?               │
│                                                              │
│ CHECK 5: Empty and Duplicates                                 │
│ ──────────────────────────                                   │
│   Files with 0 bytes?                                        │
│   Files with only template placeholders?                     │
│   Similar titles (possible duplicates)?                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Why It Was Added

Any database requires an integrity checking mechanism. RLM-Anchor is a knowledge base, and `/anchor_validate` is its health maintenance tool. Without it, small problems accumulate and turn into a big mess.

### Usage Example

```
User: /anchor_validate

AI: 🔍 MEMORY VALIDATION
    ═══════════════════
    
    Check 1: Category Structure
    ✅ 13/13 categories have _index.md
    ✅ All system files in place
    
    Check 2: Index ↔ Files Synchronization
    ⚠️ Ghost entries (in index, no file):
       01_project/_index.md → `techstack.md` — FILE NOT FOUND
    
    ⚠️ Orphan files (on disk, not in index):
       03_decisions/ADR-004-jwt.md — NOT IN INDEX
    
    Check 3: File Naming
    ⚠️ 03_decisions/my decision.md
       → Should be: ADR-NNN-my-decision.md
    
    Check 4: Broken Links
    ✅ 12/12 links valid
    
    Check 5: Empty and Duplicates
    ✅ No empty files
    ⚠️ Possible duplicates:
       PROB-001-cors.md / PROB-004-cors-again.md
    
    ════════════════════════════════
    📋 SUMMARY
    
    | # | Check | Result | Issues |
    |---|-------|--------|--------|
    | 1 | Structure | ✅ OK | 0 |
    | 2 | Index ↔ Files | ⚠️ | 2 |
    | 3 | Naming | ⚠️ | 1 |
    | 4 | Links | ✅ OK | 0 |
    | 5 | Empty/Dupes | ⚠️ | 1 |
    
    Total issues: 4
    Auto-fixable: 3/4
    
    🔧 Run auto-fix? [y/N/review]
```

```
User: /anchor_validate --fix

AI: 🔧 Fixing...
    
    ✅ Removed ghost entry from 01_project/_index.md
    ✅ ADR-004-jwt.md added to 03_decisions/_index.md
    ✅ Renamed: my decision.md → ADR-005-my-decision.md
    ⚠️ Duplicates require manual review
    
    Fixed: 3/4 issues
```

---

## 13. `/anchor_remove` — System Removal

### Why It Exists

If the user decides RLM-Anchor is no longer needed, they should be able to **cleanly remove** the system. But removal must be safe: with confirmation, with backup, with preservation of unrelated files.

### When to Call

- **When deciding to abandon** the memory system
- **During full reinstallation** (remove → install again)
- **Very rarely** — this is a destructive command

### How It Works Inside

```
Step 1: Warning ⚠️
         │
         │  Shows what will be deleted
         │  Confirms: your IDE configs will NOT be touched
         ▼
Step 2: Two-factor confirmation
         │
         │  Generates random code (8 characters)
         │  User must enter it manually
         │  This protects against accidental invocation
         ▼
Step 3: Automatic backup
         │
         │  Creates anchor_backup_FINAL_YYYY-MM-DD.zip
         │  Before deleting any file
         ▼
Step 4: Delete strictly by list
         │
         │  Deletes ONLY RLM-Anchor files
         │  Your custom configs in .agent/ are preserved
         │
         │  After deletion: empty folders removed via rmdir
         │  (if not empty — not removed, your files stay)
         ▼
Step 5: Confirmation
         │
         └── Shows: what was deleted, where backup is
```

### Why It Was Added

**Ethics**: if the user installed the system, they should be able to completely remove it. **Safety**: deletion by strict list, not `rm -rf .agent/`, which could kill IDE configs. **Insurance**: double confirmation + mandatory backup.

---

## Context Commands

---

## 14. `/handoff` — Context Transfer

### Why It Exists

Developers often switch between AI models. In one IDE — Claude, in another — Gemini, in a third — GPT-4. Each switch is context loss. `/handoff` creates a **compact summary** of the current state that can be passed to another model.

It's like a shift handover: the departing specialist leaves a note for the next one.

### When to Call

- **Before switching** to another AI model
- **Before handing the project** to another developer
- **To capture** current state in compact form

### How It Works Inside

Collects from memory: current task, recent decisions, key files, preferences, language. Forms a **one-page summary** that the next model can read and instantly get up to speed.

### Why It Was Added

AI-agnosticism is one of the project's principles. If the system works with any model, it needs a mechanism for transferring context between models.

### Usage Example

```
User: /handoff

AI: # 🔄 Context Transfer Summary

    > Date: 2026-02-07 18:00
    > Language: English (en)

    ## 📍 Current State
    
    Project: AnchorGravity Memory System
    Working on: Command documentation
    Last action: Created COMMANDS.md
    Next step: Documentation review
    
    ## ⚖️ Recent Decisions
    
    1. JWT for authorization — stateless architecture
    2. PostgreSQL — need transactions
    
    ## ⚠️ Important Notes
    
    - DON'T do git commit/push without explicit request
    - Language: ALL responses in English
    
    ## 🚀 For the next model:
    1. Read this summary
    2. Check language.md (en)
    3. Continue reviewing COMMANDS.md
```

---

## 15. `/walkthrough` — Feature Documentation

### Why It Exists

After implementing a feature, fixing a bug, or completing significant work, it's useful to document: what was done, how it works, which files were changed. `/walkthrough` automatically generates such documentation.

It's like a work completion report, but written by AI based on real changes.

### When to Call

- **After completing** a major feature
- **After fixing** a complex bug
- **When you want to capture** how something works
- AI can **suggest creating** a walkthrough after significant work

### How It Works Inside

Analyzes the current session: which files were created/modified, which decisions were made, which patterns were used. Generates a structured document with description, code examples, and file links. Saves to `.agent/memory/07_context/walkthroughs/`.

### Why It Was Added

A week later, it's already hard to remember implementation details. A month later — practically impossible. `/walkthrough` creates **documentation while the trail is hot**, while AI still remembers all the details.

---

## Cheat Sheet: Which Command When to Use

```
STARTING WORK
│
├── /wakeup          ← Every time when starting
│
WORKING
│
├── /remember [info]  ← When you learned something important
├── /recall [query]   ← When you need to find something past
├── /memory-stats     ← Quick status check
├── /anchor_briefing  ← Need full overview
│
ENDING WORK
│
├── /sleep            ← Every time when finishing
├── /handoff          ← If changing AI model
├── /walkthrough      ← If completed a major feature
│
MAINTENANCE (rarely)
│
├── /anchor_cleanup   ← Once a month
├── /anchor_backup    ← Before important changes
├── /anchor_restore   ← If need to rollback
├── /anchor_update    ← New version? Update!
├── /anchor_validate  ← Memory integrity check
├── /anchor_remove    ← If decided to remove the system
│
FIRST INSTALLATION (once)
│
└── /anchor_agent     ← When installing in a new project
```

---

## Conclusion

15 commands cover the complete lifecycle of working with persistent memory:

| Stage | Commands | Purpose |
|-------|----------|---------|
| **Installation** | `/anchor_agent` | One time — project integration |
| **Daily work** | `/wakeup`, `/sleep`, `/remember`, `/recall` | Core cycle |
| **Analytics** | `/anchor_briefing`, `/memory-stats` | Overview and statistics |
| **Maintenance** | `/anchor_backup`, `/anchor_restore`, `/anchor_cleanup`, `/anchor_update`, `/anchor_validate`, `/anchor_remove` | Lifecycle |
| **Context** | `/handoff`, `/walkthrough` | Transfer and documentation |

Each command exists for a justified reason. None duplicate another. Remove any — and a functional gap appears in the system.

---

*RLM-Anchor is an open-source project. Source code available on [GitHub](https://github.com/dvgmdvgm/AnchorGravity).*

---

© 2026 dvgmdvgm | [MIT License](LICENSE)
