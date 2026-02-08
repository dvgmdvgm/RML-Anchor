# 🧠 AI Memory System (RLM-Anchor)

> **Long-term memory for AI assistants based on RLM**

A persistent memory system for AI development environments, based on the principles of [Recursive Language Models](https://arxiv.org/abs/2512.24601) (MIT research) (see [Video Guide](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Give your AI assistant a **persistent memory** that survives between chat sessions.

---

## 💡 The Problem

Every time you start a new chat with an AI, it forgets everything:
- Project architecture
- Past decisions and their reasons
- Known bugs and workarounds
- Your coding style preferences
- What you worked on yesterday

**RLM-Anchor solves this problem.** It gives AI structured long-term memory — as simple Markdown files right in your project.

---

---

## 🌟 Features

- **📁 13 organized categories** — structured storage of project knowledge
- **🔍 RLM-style search** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multilingual** — responses and entries in any language
- **⚡ Simple commands** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Context handoff** — seamless switching between AI models
- **📝 Markdown-based** — human-readable, Git-friendly
- **🔄 Session persistence** — context preserved between sessions

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANT**: Each project requires a SEPARATE RLM-Anchor installation! Using one memory for multiple projects will confuse AI due to conflicting context. Always install fresh for each new project.

1. **Import the `.agent/` folder** into your project via Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Set language** in `.agent/memory/13_preferences/language.md`
3. **Execute this prompt** (copy the entire block below):
   ```
   /anchor_agent scan current project directories for data that will help build context and configure memory correctly (technical data, business models, design rules and all other typical templates to find and preserve project context)
   ```
4. **Start working** with chat command `/wakeup`.
5. **Work in your IDE** (development, problem-solving, business decisions, do everything as usual).

*During work, at important stages you can use* `/remember` *to save important context.*

6. **When you finish work** in IDE, for example before sleep, execute `/sleep` command so RLM-Anchor saves context to memory.

*Now every time you return to work on the project — just wake up RLM-Anchor with* `/wakeup` *command and at the end of the session send it to sleep again* `/sleep` *so it remembers everything you did.*

---

## 🌍 Language Settings

Edit `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=en    # English
LANGUAGE=ru    # Russian  
LANGUAGE=uk    # Ukrainian
...
```

---

## ⚡ Commands

| Command | Description |
|---------|-------------|
| `/wakeup` | Start session, load context |
| `/sleep` | End session, archive to history |
| `/remember` | Save information to memory |
| `/recall` | Find information in memory |
| `/handoff` | Create summary for model switching |
| `/walkthrough` | Generate feature documentation |
| `/anchor_agent` | Safe project integration |
| `/anchor_briefing` | Full project briefing (all 13 categories) |
| `/anchor_backup` | Create manual backup (for transfer) |
| `/anchor_restore` | Restore from ZIP backup |
| `/anchor_remove` | Safe system removal (with backup) |
| `/anchor_cleanup` | Smart memory cleanup (TTL, scoring) |
| `/anchor_update` | Update to latest version from GitHub |
| `/anchor_validate` | Memory integrity check (5 checks) |
| `/memory-stats` | Show memory statistics with trends |

📖 **Full commands documentation**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Structure

```
.agent/
├── MEMORY_INDEX.md           # Main memory index
├── skills/
│   └── MEMORY_SKILL.md       # AI instructions
├── workflows/                 # Command definitions
├── scripts/                   # Python utilities
└── memory/
    ├── 01_project/           # Project information
    ├── 02_architecture/      # System architecture
    ├── 03_decisions/         # Architectural decisions (ADR)
    ├── 04_domain/            # Business domain
    ├── 05_code/              # Code documentation
    ├── 06_problems/          # Problems and solutions
    ├── 07_context/           # Session context
    ├── 08_people/            # People and roles
    ├── 09_external/          # External dependencies
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Deployment
    ├── 12_roadmap/           # Plans and future
    └── 13_preferences/       # Preferences and LANGUAGE
```

---

## 🔄 How It Works

### RLM-Style Process

```
User request
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Read memory index      │
│ 2. DECOMPOSE — Determine categories │
│ 3. RECURSE — Search in needed files │
│ 4. AGGREGATE — Combine data         │
└─────────────────────────────────────┘
    ↓
Contextual response (in configured language)
```

---

## 📝 Usage Examples

### 🚀 Initialization / Connection
```
User: /anchor_agent
AI: 📋 INTEGRATION ANALYSIS... [Scans and offers safe integration options]
```

### ☀️ Start Session
```
User: /wakeup
AI: 🚀 Loading project context...
    ✅ Session started!
    📌 Pending tasks: 2
```

### 📌 Saving Information
```
User: /remember We chose PostgreSQL for ACID transactions
AI: ✅ Saved to memory/03_decisions/ADR-002-database.md
```

### 🔍 Knowledge Search
```
User: /recall Why did we choose PostgreSQL?
AI: 📁 Found in memory:
    Source: memory/03_decisions/ADR-002-database.md
    We chose PostgreSQL for ACID transaction support...
```

### 🔄 Context Handoff
```
User: /handoff
AI: 🔄 Creating context handoff summary... [Generates summary for another model]
```

### 📖 Documentation Generation
```
User: /walkthrough New authorization
AI: 📖 Walkthrough created! Saved to memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Memory Statistics
```
User: /memory-stats
AI: 📊 Statistics: 42 files, 13 categories...
```

### 🌙 End Session
```
User: /sleep
AI: 📝 Summarizing session...
    ✅ History saved.
    👋 See you later!
```

---

## 🛠️ Customization

### Add New Categories
1. Create folder in `memory/`
2. Add `_index.md` 
3. Update `MEMORY_INDEX.md`

### Extend Workflows
Edit files in `workflows/` to customize commands.

---

## 📄 License
MIT License — fork and improve!

---

## 🙏 Acknowledgments
Inspired by [RLM research from MIT](https://arxiv.org/abs/2512.24601) on Recursive Language Models and [this video guide](https://www.youtube.com/watch?v=huszaaJPjU8).
