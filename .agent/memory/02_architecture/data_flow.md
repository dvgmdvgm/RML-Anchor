# 🔄 Data Flow

> **Created**: 2026-02-06  
> **Last Updated**: 2026-02-06  

---

## 📊 Main Data Flows

### 1. Session Start (`/wakeup`)

```
User: /wakeup
       │
       ▼
┌──────────────────┐
│ Read language.md │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Read MEMORY_INDEX│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Load session_history│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Load pending_tasks│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Report to User   │
└──────────────────┘
```

### 2. Memory Save (`/remember`)

```
User: /remember [info]
       │
       ▼
┌──────────────────┐
│ Analyze content  │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Select category  │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Create/Update file│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Update _index.md │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Confirm to User  │
└──────────────────┘
```

### 3. Session End (`/sleep`)

```
User: /sleep
       │
       ▼
┌──────────────────┐
│ Summarize session│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Archive to history│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Update pending_tasks│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Reset current_session│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Confirm to User  │
└──────────────────┘
```

---

## 📥 Read Operations

| Operation | Files Accessed |
|-----------|----------------|
| `/wakeup` | language.md, MEMORY_INDEX.md, session_history/, pending_tasks.md |
| `/recall` | Relevant category _index.md + matching files |
| `/anchor_briefing` | All 13 _index.md files |

---

## 📤 Write Operations

| Operation | Files Modified |
|-----------|----------------|
| `/remember` | Target category file + _index.md |
| `/sleep` | session_history/, pending_tasks.md, current_session.md |
| `/anchor_backup` | Creates ZIP in backups/ |
