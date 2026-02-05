# ADR-001: RLM-like Memory System Creation

- **Date**: 2026-02-05
- **Status**: Accepted
- **Authors**: User, AI Assistant
- **Tags**: memory, RLM, context, architecture

---

## 📋 Context

When working on projects with AI assistant, the following problems arise:
1. LLM context window is limited (~200K tokens)
2. All context is lost between sessions
3. Important decisions and information are forgotten
4. Need to repeat the same things

**Question**: How to provide persistent project memory for AI assistant?

---

## 🎯 Decision

**We decided**: Create a memory system based on RLM (Recursive Language Models) principles using structured Markdown files.

The system includes:
- 13 categories for different types of information
- Hierarchical structure with indexes
- RLM-like search algorithm (Examine → Decompose → Recurse → Aggregate)
- Workflows for memory management (/remember, /recall, /wakeup, /sleep)
- Python utilities for search and statistics
- Multi-language support via preference file

---

## 💡 Rationale

1. **Markdown files** — simple, readable, version-controllable via Git
2. **Hierarchical structure** — allows AI to quickly find needed information
3. **Category indexes** — enable precise search without scanning all files
4. **RLM principles** — proven effective in MIT research
5. **Multi-language** — supports international users

---

## 🔄 Considered Alternatives

### Alternative 1: Vector Database (RAG)

**Description**: Use ChromaDB/Pinecone for semantic search

**Pros**:
- Semantic search
- Automatic indexing

**Cons**:
- Requires additional infrastructure
- Harder to debug
- Not as transparent

**Why rejected**: Excessive complexity for current tasks

### Alternative 2: Simple Text File

**Description**: One large README with notes

**Pros**:
- Maximum simplicity

**Cons**:
- Not structured
- Hard to search
- Quickly becomes chaotic

**Why rejected**: Doesn't scale

---

## 📊 Consequences

### Positive:
- Persistent memory between sessions
- Structured knowledge storage
- Transparency (files readable manually)
- Version control via Git
- Portability between projects
- International support

### Negative:
- Requires discipline to update memory
- AI might forget to access memory
- Manual index management

### Neutral:
- Context window doesn't physically increase
- This isn't "magic" — requires explicit use

---

## 🔗 Related Files

- `.agent/MEMORY_INDEX.md` — main index
- `.agent/skills/MEMORY_SKILL.md` — AI instructions
- `.agent/workflows/` — management commands
- `.agent/memory/13_preferences/language.md` — language settings

---

## 📚 Sources

- [RLM Paper (MIT)](https://arxiv.org/abs/2512.24601) — Recursive Language Models
- YouTube: "MIT Researchers DESTROY the Context Window Limit"

---

## 📝 Change History

| Date | Change |
|------|--------|
| 2026-02-05 | Created and implemented |
| 2026-02-05 | Added multi-language support |
