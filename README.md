# 🧠 RLM-Anchor — AI Memory System

> Give your AI assistant a **persistent memory** that survives between chat sessions.

---

## 💡 The Problem

Every time you start a new chat with an AI assistant, it forgets everything:
- Your project architecture
- Past decisions and their reasons
- Known bugs and workarounds
- Your coding style preferences
- What you worked on yesterday

**RLM-Anchor solves this.** It gives AI a structured long-term memory — stored as simple Markdown files right in your project.

---

## 🚀 Quick Start (3 steps)

### 1. Install

```bash
git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
```

### 2. Set Language

Edit `.agent/memory/13_preferences/language.md`:
```
LANGUAGE=en
```

### 3. Initialize

Paste this into your AI chat:
```
/anchor_agent scan the current project directories for data that will help build context and configure memory correctly
```

**Done!** Now use `/wakeup` to start and `/sleep` to finish each session.

---

## ⚡ Daily Workflow

```
/wakeup          → AI loads your project context
  ... work ...   → develop, ask questions, make decisions
/remember ...    → save important info to memory
/sleep           → AI saves session, you can close the chat
```

Next time you open a new chat → `/wakeup` → AI remembers everything.

---

## 📋 Commands

| Command | What it does |
|---------|-------------|
| `/wakeup` | Start session — load project memory |
| `/sleep` | End session — save everything |
| `/remember` | Save a fact, decision, or note |
| `/recall` | Find something in memory |
| `/anchor_briefing` | Get full project overview |
| `/anchor_update` | Update RLM-Anchor to latest version |
| `/anchor_backup` | Create a backup |
| `/anchor_restore` | Restore from backup |
| `/handoff` | Create summary for switching AI models |
| `/memory-stats` | Show memory statistics |

---

## 🧩 How It Works

```
Your Project/
├── src/                    ← your code (unchanged)
├── .agent/                 ← AI memory lives here
│   ├── memory/
│   │   ├── 01_project/     ← project info
│   │   ├── 02_architecture/← system design
│   │   ├── 03_decisions/   ← why you chose X over Y
│   │   ├── 04_domain/      ← business logic
│   │   ├── 05_code/        ← code patterns & style
│   │   ├── 06_problems/    ← bugs & workarounds
│   │   ├── 07_context/     ← session history
│   │   ├── 08_people/      ← team & roles
│   │   ├── 09_external/    ← APIs & services
│   │   ├── 10_testing/     ← test strategies
│   │   ├── 11_deployment/  ← deployment info
│   │   ├── 12_roadmap/     ← future plans
│   │   └── 13_preferences/ ← your preferences
│   ├── workflows/          ← command definitions
│   └── MEMORY_INDEX.md     ← master index
```

**Key idea:** Everything is Markdown. You can read, edit, or version-control your AI's memory just like code.

---

## 🔍 The RLM Search Process

When you ask a question, AI doesn't read ALL memory files. Instead:

```
1. EXAMINE   → Read the master index (which categories exist?)
2. DECOMPOSE → Pick 2-3 relevant categories
3. RECURSE   → Search files in those categories
4. AGGREGATE → Combine findings into an answer
```

This keeps responses **fast** even with hundreds of memory files.

---

## ⚠️ Important Rules

- **One project = one RLM-Anchor** — never share `.agent/` between projects
- **Always `/sleep` before closing** — otherwise AI won't save the session
- **Don't edit `_index.md` manually** — AI manages these files
- **Memory is Git-friendly** — commit `.agent/` to your repo for team sharing

---

## 🔄 Updating

```
/anchor_update              # update to latest version
/anchor_update --check      # just check, don't update
```

Your data (memory entries, preferences, session history) is **never overwritten** during updates.

---

## 🌍 Supported Languages

RLM-Anchor works in any language. Set your preference in `language.md` and all AI responses, memory entries, and system messages will use that language.

---

## 📄 License

MIT License — free to use, fork, and improve.

---

## 🙏 Inspired By

[MIT RLM Research](https://arxiv.org/abs/2512.24601) on Recursive Language Models.

> 📚 Full technical documentation → [docs/archive/](docs/archive/)
