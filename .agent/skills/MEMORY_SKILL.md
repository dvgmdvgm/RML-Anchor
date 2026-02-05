---
name: Project Memory System
description: Long-term project memory system based on RLM (Recursive Language Models) principles. Provides persistent storage and retrieval of project knowledge with multi-language support.
---

# 🧠 MEMORY SKILL — Complete Memory System Instructions

> **CRITICAL**: You MUST follow these instructions when working with this project.

---

# ⚠️⚠️⚠️ MANDATORY FIRST STEP — READ BEFORE ANYTHING ELSE ⚠️⚠️⚠️

## 🌍 LANGUAGE CHECK — DO THIS FIRST!

**BEFORE responding to ANY user message, you MUST:**

```
1. READ file: .agent/memory/13_preferences/language.md
2. EXTRACT the LANGUAGE= value (e.g., LANGUAGE=ru)
3. USE ONLY that language for your ENTIRE response
```

### STRICT RULES:

| Rule | Description |
|------|-------------|
| ❌ **NEVER** | Respond in a different language than configured |
| ❌ **NEVER** | Switch languages mid-conversation |
| ❌ **NEVER** | Match user's message language if different from config |
| ✅ **ALWAYS** | Check language file at session start |
| ✅ **ALWAYS** | Write memory entries in configured language |
| ✅ **ALWAYS** | Create logs/summaries in configured language |

### If user writes in different language:

- Still respond in CONFIGURED language
- You may acknowledge their language but respond in configured one
- Example: User writes in Spanish, config is Russian → Respond in Russian

---

### Before ANY interaction:

1. **READ** `.agent/memory/13_preferences/language.md`
2. **EXTRACT** the `LANGUAGE=` value
3. **USE ONLY** that language for:
   - All responses to user
   - All memory entries
   - All summaries and logs
   - All roadmaps and plans
   - All error messages

### STRICT ENFORCEMENT:

```
❌ NEVER respond in a different language than specified
❌ NEVER write memory entries in a different language
❌ NEVER create logs/summaries in a different language
✅ ALWAYS check language setting at session start
✅ ALWAYS use the specified language consistently
```

---

## 🎯 Operating Principle (RLM-like)

```
REQUEST → EXAMINE → DECOMPOSE → RECURSE → AGGREGATE → RESPONSE
            ↓          ↓           ↓           ↓
         Read       Identify    Dive into   Combine
         index     categories    details   information
```

---

## 📋 MANDATORY ACTIONS

### 🔵 At SESSION START (first user message)

1. **Read** `.agent/memory/13_preferences/language.md` — get language setting
2. **Read** `.agent/MEMORY_INDEX.md`
3. **Read** `.agent/memory/07_context/current_session.md` (if exists)
4. **Read** `.agent/memory/07_context/pending_tasks.md` (if exists)
5. **Inform** user about pending tasks (if any)
6. **Respond** in the configured language

### 🟢 At EVERY user message

1. **Analyze** message for trigger words (see below)
2. **If triggers found** — access corresponding memory category
3. **Use** found information in response
4. **Reference** source: "According to `memory/03_decisions/...`"
5. **Always respond** in configured language

### 🟡 At SIGNIFICANT events

Automatically **write to memory** when:

### 🟡 At SIGNIFICANT events (Decisions, Solutions, Changes)

**Algorithm:**

1. **Check setting**: Read `.agent/memory/13_preferences/memory_settings.md`
2. **If `AUTO_SAVE=auto`**:
   - Write to memory immediately
   - Notify user (if `NOTIFY_ON_SAVE=true`)
3. **If `AUTO_SAVE=ask` (Default)**:
   - **DO NOT** write immediately
   - **Ask user**: "Should I save this [decision/fix] to memory?" / "Записать это [решение/фикс] в память?"
   - Write ONLY if user confirms

**Where to potentialy save:**

| Event | Category |
|-------|----------|
| Architecture decision made | `03_decisions/` |
| Complex problem solved | `06_problems/` |
| Important component created | `05_code/` |
| Tech stack changed | `01_project/tech_stack.md` |
| Integration added | `09_external/` |

**Important**: Write entries in the language specified in `language.md`!

### 🔴 At SESSION END (on `/sleep` command)

1. **Summarize** key session discussions
2. **Write** to `memory/07_context/session_history/YYYY-MM-DD.md`
3. **Update** `memory/07_context/pending_tasks.md`
4. **Update** relevant `_index.md` files
5. **All in** the configured language

---

## 🔍 TRIGGER WORDS

### Read from Memory (RETRIEVE)

When detecting these words — **MUST check memory**:

| Trigger | Where to Search |
|---------|-----------------|
| "why did we...", "how did we decide..." | `03_decisions/` |
| "last time", "previously discussed" | `07_context/` |
| "what architecture", "how is it structured" | `02_architecture/` |
| "there was a problem", "how did we fix" | `06_problems/` |
| "what stack", "what technologies" | `01_project/` |
| "what does it mean", "term", "definition" | `04_domain/glossary.md` |
| "how does function/class work" | `05_code/` |
| "plans", "what's next", "roadmap" | `12_roadmap/` |
| "how to deploy", "where is server" | `11_deployment/` |
| "remind me", "recall" | All relevant categories |

### Write to Memory (STORE)

When detecting these words — **suggest to save**:

| Trigger | Where to Write |
|---------|----------------|
| "decided to use...", "chose..." | `03_decisions/` |
| "remember this", "this is important" | By context |
| "fixed bug", "found solution" | `06_problems/` |
| "don't forget", "TODO" | `07_context/pending_tasks.md` |
| "I prefer...", "I like..." | `13_preferences/` |

---

## 📁 MEMORY FILE STRUCTURE

### Index Files (`_index.md`)

Each category has `_index.md` with:
- List of all files in category
- Brief description of each file
- Last update date

**Format**:
```markdown
# Category: [Name]

## Files in This Category

| File | Description | Updated |
|------|-------------|---------|
| `file1.md` | Description | 2026-02-05 |
```

### Entry Files

**Standard entry format**:
```markdown
# [Title]

- **Created**: YYYY-MM-DD
- **Last Updated**: YYYY-MM-DD
- **Status**: [Active/Deprecated/In Progress]
- **Tags**: tag1, tag2, tag3

---

## Content

[Main entry content - IN CONFIGURED LANGUAGE]

## Related Files

- `path/to/file.py`
- `another/file.html`

## Change History

- YYYY-MM-DD: Created
- YYYY-MM-DD: Updated [what changed]
```

---

## 🔄 MEMORY SEARCH ALGORITHM

```python
def search_memory(query):
    """
    RLM-like memory search algorithm
    """
    
    # 0. GET LANGUAGE
    language = read(".agent/memory/13_preferences/language.md")
    
    # 1. EXAMINE - Study index
    main_index = read(".agent/MEMORY_INDEX.md")
    
    # 2. DECOMPOSE - Identify relevant categories
    keywords = extract_keywords(query)
    categories = match_categories(keywords, main_index)
    
    # 3. RECURSE - Dive into categories
    results = []
    for category in categories:
        category_index = read(f".agent/memory/{category}/_index.md")
        relevant_files = find_relevant(query, category_index)
        
        for file in relevant_files:
            content = read(file)
            extracted = extract_relevant_sections(query, content)
            results.append(extracted)
    
    # 4. AGGREGATE - Combine results
    return synthesize_answer(query, results, language=language)
```

---

## ✍️ MEMORY WRITE ALGORITHM

```python
def write_to_memory(info, category):
    """
    Algorithm for writing information to memory
    """
    
    # 0. GET LANGUAGE
    language = read(".agent/memory/13_preferences/language.md")
    
    # 1. Determine file
    if is_new_topic(info):
        filename = generate_filename(info)  # new file
    else:
        filename = find_existing_file(info)  # update existing
    
    # 2. Format entry (IN CONFIGURED LANGUAGE!)
    formatted = format_entry(info, template=category.template, language=language)
    
    # 3. Write/update file
    write(f".agent/memory/{category}/{filename}", formatted)
    
    # 4. Update category index
    update_index(f".agent/memory/{category}/_index.md", filename, info.summary)
    
    # 5. Inform user (in configured language)
    notify(f"✅ Saved to memory/{category}/{filename}")
```

---

## 📊 FILE NAMING CONVENTIONS

| Category | Name Format | Example |
|----------|-------------|---------|
| decisions | `ADR-NNN-topic.md` | `ADR-001-database-choice.md` |
| problems | `PROB-NNN-topic.md` | `PROB-001-auth-google.md` |
| session_history | `YYYY-MM-DD.md` | `2026-02-05.md` |
| Others | `topic-name.md` | `tech-stack.md` |

---

## ⚠️ IMPORTANT RULES

### ✅ DO:

1. **Always read MEMORY_INDEX.md** at work start
2. **Always check language setting** before responding
3. **Reference sources** in responses
4. **Update _index.md** when creating new files
5. **Use standard templates** for entries
6. **Inform user** about memory writes
7. **Stay in configured language** throughout session

### ❌ DON'T:

1. **Don't record trivial things** — only significant information
2. **Don't duplicate information** — check existing files
3. **Don't forget to update indexes**
4. **Don't store secrets** — only descriptions, not values
5. **Don't ignore trigger words**
6. **Don't switch languages** — stay consistent

---

## 🛠️ UTILITIES

### Available Scripts:

| Script | Purpose |
|--------|---------|
| `scripts/memory_search.py` | Search memory |
| `scripts/memory_stats.py` | Memory statistics |
| `scripts/memory_validate.py` | Validate structure |

### Available Workflows:

| Workflow | Command | Purpose |
|----------|---------|---------|
| `remember.md` | `/remember` | Save to memory |
| `recall.md` | `/recall` | Find in memory |
| `wakeup.md` | `/wakeup` | Start session |
| `sleep.md` | `/sleep` | End session |
| `handoff.md` | `/handoff` | Context transfer between models |
| `walkthrough.md` | `/walkthrough` | Generate feature documentation |
| `agent.md` | `/agent` | Integrate into existing project |
| `memory-stats.md` | `/memory-stats` | Statistics |

---

## 📈 SUCCESS METRICS

Memory system works well if:

- [ ] Questions about past decisions get accurate answers with references
- [ ] Important decisions are recorded automatically
- [ ] Context is not lost between sessions
- [ ] User doesn't need to repeat information
- [ ] No contradictions between entries
- [ ] All interactions are in the configured language
