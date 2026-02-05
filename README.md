# 🧠 AI Memory System (RLM-Anchor)

> **RLM-inspired Long-term Memory for AI Assistants**

A persistent memory system for AI-powered development environments based on [Recursive Language Models](https://arxiv.org/abs/2512.24601) principles.

---

## 🌟 Features

- **📁 13 Organized Categories** — structured storage for all project knowledge
- **🔍 RLM-like Search** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multi-language Support** — respond and record in any language
- **⚡ Simple Commands** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Session Persistence** — context preserved between sessions
- **📝 Markdown-based** — human-readable, Git-friendly

---

## 📦 Quick Start & Usage

1. **Import `.agent/` folder** to your project using Git:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Set your language** in `.agent/memory/13_preferences/language.md` file.
3. **Run** ```/agent_anchor``` to implement RLM-Anchor safely into your current project.
4. **Start working** with ```/wakeup``` chat command.
5. **Work in your IDE** (develop, solve tasks, make business decisions, do everything as usual).

*In the process of work, at important stages you can use* ```/remember``` *to save important context.*

6. **When you finished working** in your IDE, for example, before you go to sleep, execute the command ```/sleep``` so that RLM-Anchor can save your context to memory.

*Now every time you return to work on your project, just wake up RLM-Anchor by running* ```/wakeup``` *and at the end of the session, send it back to sleep* ```/sleep``` *so it remembers everything you did.*

---

## 🌍 Language Configuration

Edit `.agent/memory/13_preferences/language.md`:

```
LANGUAGE=en    # English
LANGUAGE=ru    # Russian  
LANGUAGE=uk    # Ukrainian
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
| `/handoff` | Create context summary for model switching |
| `/walkthrough` | Generate feature documentation |
| `/agent_anchor` | Safely integrate into existing project |
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

### 🚀 Initialize / Connect
```
User: /agent_anchor
AI: 📋 INTEGRATION ANALYSIS... [Scans and suggests safe integration options]
```

### ☀️ Start a Session
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

### 🔍 Recalling Knowledge
```
User: /recall Why did we choose PostgreSQL?
AI: 📁 Found in memory:
    Source: memory/03_decisions/ADR-002-database.md
    We chose PostgreSQL for ACID transaction support...
```

### 🔄 Model Handoff
```
User: /handoff
AI: 🔄 Creating context handoff summary... [Generates summary for another model]
```

### 📖 Generate Documentation
```
User: /walkthrough New Auth Feature
AI: 📖 Walkthrough created! Saved to memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Check Statistics
```
User: /memory-stats
AI: 📊 Memory Stats: 42 files, 13 categories...
```

### 🌙 End Session
```
User: /sleep
AI: 📝 Summarizing session...
    ✅ Session history saved.
    👋 Goodbye!
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
Inspired by [MIT RLM Research](https://arxiv.org/abs/2512.24601) on Recursive Language Models and [this video guide](https://www.youtube.com/watch?v=huszaaJPjU8).
