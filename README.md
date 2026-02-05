# 🧠 AI Memory System

> **RLM-inspired Long-term Memory for AI Assistants**

A persistent memory system for AI-powered development environments based on [Recursive Language Models](https://arxiv.org/abs/2512.24601) principles.

---

## 🌟 Features

- **📁 13 Organized Categories** — structured storage for all project knowledge
- **🔍 RLM-like Search** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multi-language Support** — respond and record in any language
- **⚡ Simple Commands** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **📝 Markdown-based** — human-readable, Git-friendly
- **🔄 Session Persistence** — context preserved between sessions

---

## 📦 Quick Start

1. **Import `.agent/` folder** to your project using Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Set your language** in `.agent/memory/13_preferences/language.md`
3. **Start working** with `/wakeup`

---

## 🌍 Language Configuration

Edit `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=en    # English
LANGUAGE=ru    # Russian  
LANGUAGE=es    # Spanish
LANGUAGE=de    # German
...
```

All AI responses, memory entries, and logs will use the configured language.

---

## ⚡ Commands

| Command | Description |
|---------|-------------|
| `/wakeup` | Start session, load context |
| `/sleep` | End session, summarize work |
| `/remember` | Save information to memory |
| `/recall` | Find information in memory |
| `/handoff` | **NEW!** Create context summary for model switching |
| `/walkthrough` | **NEW!** Generate feature documentation |
| `/agent` | Safely integrate into existing project |
| `/memory-stats` | Show memory statistics |

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
    ├── 01_project/           # Project info
    ├── 02_architecture/      # System architecture
    ├── 03_decisions/         # Architecture decisions (ADR)
    ├── 04_domain/            # Business domain
    ├── 05_code/              # Code documentation
    ├── 06_problems/          # Problems & solutions
    ├── 07_context/           # Session context
    ├── 08_people/            # People & roles
    ├── 09_external/          # External dependencies
    ├── 10_testing/           # Testing info
    ├── 11_deployment/        # Deployment info
    ├── 12_roadmap/           # Plans & future
    └── 13_preferences/       # User preferences & LANGUAGE
```

---

## 🔄 How It Works

### RLM-like Process

```
User Query
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Read memory index      │
│ 2. DECOMPOSE — Identify categories  │
│ 3. RECURSE — Search relevant files  │
│ 4. AGGREGATE — Combine information  │
└─────────────────────────────────────┘
    ↓
Contextual Response (in configured language)
```

---

## 📝 Usage Examples

### Start a Session
```
User: /wakeup
AI: 🚀 Loading project context...
    ✅ Session started!
    📌 Pending tasks: 2
```

### Remember a Decision
```
User: /remember We chose PostgreSQL for ACID transactions
AI: ✅ Saved to memory/03_decisions/ADR-002-database.md
```

### Recall Information
```
User: /recall Why did we choose PostgreSQL?
AI: 📁 Found in memory:
    Source: memory/03_decisions/ADR-002-database.md
    We chose PostgreSQL for ACID transaction support...
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

MIT License — feel free to fork and improve!

---

## 🙏 Credits

Inspired by [MIT RLM Research](https://arxiv.org/abs/2512.24601) on Recursive Language Models.

---

## 🤝 Contributing

Contributions welcome! Please read the structure and follow the patterns.
