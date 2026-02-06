# 🏗️ Architecture Overview

> **Created**: 2026-02-06  
> **Last Updated**: 2026-02-06  

---

## 📊 Layered Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                     │
│  /wakeup  /sleep  /remember  /recall  /anchor_briefing     │
│                                                             │
│  User interacts via slash commands in AI IDE chat          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW LAYER                           │
│  .agent/workflows/*.md — Command definitions                │
│                                                             │
│  Each command is a markdown file with execution steps       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SKILL LAYER                              │
│  .agent/skills/MEMORY_SKILL.md — AI instructions            │
│                                                             │
│  Defines HOW AI should work with memory                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    STORAGE LAYER                            │
│  .agent/memory/01-13 — Categorized knowledge                │
│                                                             │
│  13 folders with markdown files for each knowledge type     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    INDEX LAYER                              │
│  .agent/MEMORY_INDEX.md — Central navigation                │
│                                                             │
│  Single entry point that maps to all categories             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 Component Relationships

| Component | Depends On | Used By |
|-----------|------------|---------|
| Commands | Workflows | User |
| Workflows | Skills | Commands |
| Skills | Memory, Index | Workflows |
| Memory | File System | Skills, Scripts |
| Index | Memory | Skills |
| Scripts | Memory | User (optional) |

---

## 📊 Layer Responsibilities

| Layer | Read | Write | Validate |
|-------|------|-------|----------|
| User Interface | ❌ | ❌ | ❌ |
| Workflow | ✅ | ✅ | ❌ |
| Skill | ✅ | ✅ | ✅ |
| Storage | ✅ | ✅ | ❌ |
| Index | ✅ | ✅ | ❌ |
