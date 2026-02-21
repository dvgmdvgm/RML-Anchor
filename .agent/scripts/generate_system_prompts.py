"""
generate_system_prompts.py — Generate .cursorrules, CLAUDE.md, GEMINI.md from RLM-Anchor memory.

Usage:
    python .agent/scripts/generate_system_prompts.py [--project-dir .]

This script reads memory files and generates compact system prompt files
that IDEs inject into every AI request automatically.
"""

import argparse
import re
from pathlib import Path


def read_file_safe(path: Path) -> str:
    """Read file contents or return empty string if not found."""
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, PermissionError):
        return ""


def extract_language(project_dir: Path) -> str:
    """Extract language setting from memory files."""
    local_lang = read_file_safe(
        project_dir / ".agent" / "memory" / "13_preferences" / "language_local.md"
    )
    if local_lang:
        match = re.search(r"LANGUAGE\s*=\s*(\w+)", local_lang)
        if match:
            return match.group(1)

    default_lang = read_file_safe(
        project_dir / ".agent" / "memory" / "13_preferences" / "language.md"
    )
    match = re.search(r"LANGUAGE\s*=\s*(\w+)", default_lang)
    return match.group(1) if match else "en"


def extract_custom_rules(content: str, file_format: str) -> str:
    """Extract CUSTOM PROJECT RULES section from existing system prompt file."""
    if file_format == "comment":
        # .cursorrules format (# comments)
        pattern = r"(# 🎯 CUSTOM PROJECT RULES\n# ═+\n)(.*?)(\n# ═)"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            rules_block = match.group(2).strip()
            # Filter out example/placeholder lines
            lines = rules_block.split("\n")
            custom_lines = [
                line for line in lines
                if line.strip()
                and not line.strip().startswith("# Add your")
                and not line.strip().startswith("# Examples:")
                and not line.strip().startswith("#   -")
                and not line.strip().startswith("# These rules")
            ]
            return "\n".join(custom_lines)
    else:
        # Markdown format (CLAUDE.md, GEMINI.md)
        pattern = r"(## 🎯 CUSTOM PROJECT RULES\n)(.*?)(\n---|\n## )"
        match = re.search(pattern, content, re.DOTALL)
        if match:
            rules_block = match.group(2).strip()
            lines = rules_block.split("\n")
            custom_lines = [
                line for line in lines
                if line.strip()
                and not line.strip().startswith("Add your")
                and not line.strip().startswith("<!-- Example")
                and not line.strip().startswith("-->")
                and not line.strip().startswith("- Never use white")
                and not line.strip().startswith("- Always use dark")
                and not line.strip().startswith("- API responses")
            ]
            return "\n".join(custom_lines)
    return ""


def detect_os() -> str:
    """Detect OS from tools.md or system."""
    import platform
    return "Windows" if platform.system() == "Windows" else platform.system()


def extract_code_style_summary(project_dir: Path) -> str:
    """Extract compact code style summary from coding_style.md."""
    content = read_file_safe(
        project_dir / ".agent" / "memory" / "13_preferences" / "coding_style.md"
    )
    if not content:
        return "# No coding style found. Run /remember to add."

    # Extract key formatting rules per language
    summary_lines = []
    # Python
    if "INDENTATION=4 spaces" in content and "Python" in content:
        summary_lines.append(
            'Python: 4 spaces, "double quotes", type hints, Google docstrings'
        )
    # JS/TS
    if "INDENTATION=2 spaces" in content and "JavaScript" in content:
        summary_lines.append(
            "JS/TS: 2 spaces, 'single quotes', semicolons, ES modules"
        )
    # HTML/CSS
    if "HTML" in content:
        summary_lines.append("HTML/CSS: 2 spaces, BEM, semantic HTML")
    # Django
    if "Django" in content:
        summary_lines.append(
            "Django Templates: spaces around ==, tags on single line"
        )

    return "\n".join(summary_lines) if summary_lines else "See coding_style.md for details"


def extract_project_summary(project_dir: Path) -> str:
    """Extract one-line project summary from overview.md."""
    content = read_file_safe(
        project_dir / ".agent" / "memory" / "01_project" / "overview.md"
    )
    if not content:
        return ""
    # Find the first meaningful description line
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("**") and "—" in line:
            return line
    return ""


def generate_cursorrules(
    language: str,
    code_style: str,
    os_name: str,
    custom_rules: str,
    project_summary: str,
) -> str:
    """Generate .cursorrules content."""
    custom_section = custom_rules if custom_rules else (
        "# Add your project-specific rules below this line.\n"
        "# These rules are enforced on EVERY AI request.\n"
        "# Examples:\n"
        "#   - Never use white backgrounds for buttons\n"
        "#   - Always use dark theme colors\n"
        "#   - API responses must include error codes"
    )

    return f"""# RLM-Anchor — System Rules
# This file is auto-read by Cursor AI on EVERY request.
# Generated by /anchor_sync. Manual edits to CUSTOM RULES are preserved.

# ═══════════════════════════════════════
# 🔴 CRITICAL RULES (never violate)
# ═══════════════════════════════════════

# Language: ALWAYS respond in: {language}
# Source: .agent/memory/13_preferences/language_local.md

# ═══════════════════════════════════════
# 🟡 PROJECT RULES
# ═══════════════════════════════════════

# Before generating UI/CSS:
# - Read .agent/memory/13_preferences/coding_style.md
# - Read .agent/memory/05_code/conventions.md
# Before making architecture decisions:
# - Read .agent/memory/03_decisions/ for existing ADRs
# - Don't repeat solved problems → check .agent/memory/06_problems/

# ═══════════════════════════════════════
# 🟢 MEMORY SYSTEM
# ═══════════════════════════════════════

# This project uses RLM-Anchor persistent memory.
# Memory: .agent/memory/ (13 categories)
# Index: .agent/MEMORY_INDEX.md
# Commands: /wakeup, /sleep, /remember, /recall

# ═══════════════════════════════════════
# 📐 CODE STYLE (quick reference)
# ═══════════════════════════════════════

# Full: .agent/memory/13_preferences/coding_style.md
# {code_style.replace(chr(10), chr(10) + "# ")}

# ═══════════════════════════════════════
# ⚙️ ENVIRONMENT
# ═══════════════════════════════════════

# OS: {os_name} — NEVER use Unix commands (du, wc, find, grep, sed, awk)
# Use PowerShell or built-in agent tools.
# See: .agent/memory/13_preferences/tools.md

# ═══════════════════════════════════════
# 🎯 CUSTOM PROJECT RULES
# ═══════════════════════════════════════

{custom_section}

# ═══════════════════════════════════════
# 📖 FULL CONTEXT
# ═══════════════════════════════════════
# Project: .agent/memory/01_project/overview.md
# Architecture: .agent/memory/02_architecture/patterns.md
# Decisions: .agent/memory/03_decisions/
# Problems: .agent/memory/06_problems/
# Preferences: .agent/memory/13_preferences/
"""


def generate_markdown_prompt(
    language: str,
    code_style: str,
    os_name: str,
    custom_rules: str,
    project_summary: str,
    target_ide: str,
) -> str:
    """Generate CLAUDE.md or GEMINI.md content."""
    ide_names = {
        "claude": "Claude Code",
        "gemini": "Gemini CLI / Antigravity",
    }
    ide_label = ide_names.get(target_ide, target_ide)

    custom_section = custom_rules if custom_rules else (
        "Add your project-specific rules below:\n"
        "<!-- Example:\n"
        "- Never use white backgrounds for buttons\n"
        "- Always use dark theme\n"
        "- API responses must include error codes\n"
        "-->"
    )

    code_style_lines = "\n".join(
        f"- **{line.split(':')[0].strip()}**: {':'.join(line.split(':')[1:]).strip()}"
        for line in code_style.split("\n")
        if line.strip()
    )

    return f"""# RLM-Anchor — System Rules for {ide_label}

> **This file is auto-read by {ide_label} on EVERY request.**
> Keep it compact (<80 lines). Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (never violate)

**Language**: ALWAYS respond in: **{language}**

---

## 🟡 PROJECT RULES

**Before generating UI/CSS:**
- Read `.agent/memory/13_preferences/coding_style.md`
- Read `.agent/memory/05_code/conventions.md`
- Apply project design rules (colors, spacing, typography)

**Before making architecture decisions:**
- Read `.agent/memory/03_decisions/` for existing ADRs
- Don't repeat solved problems → check `.agent/memory/06_problems/`

---

## 🟢 MEMORY SYSTEM

This project uses **RLM-Anchor** persistent memory.
- Memory: `.agent/memory/` (13 categories)
- Index: `.agent/MEMORY_INDEX.md`

**Commands** (user says `/command`):
| Command | Action |
|---------|--------|
| `/wakeup` | Start session → `.agent/workflows/wakeup.md` |
| `/sleep` | End session → `.agent/workflows/sleep.md` |
| `/remember` | Save to memory → `.agent/workflows/remember.md` |
| `/recall` | Search memory → `.agent/workflows/recall.md` |

---

## 📐 CODE STYLE (quick reference)

Full: `.agent/memory/13_preferences/coding_style.md`
{code_style_lines}

---

## ⚙️ ENVIRONMENT

- **OS**: {os_name} — NEVER use Unix commands (`du`, `wc`, `find`, `grep`)
- Use PowerShell or built-in tools
- See: `.agent/memory/13_preferences/tools.md`

---

## 🎯 CUSTOM PROJECT RULES

{custom_section}

---

## 📖 FULL CONTEXT

| Category | Path |
|----------|------|
| Project | `.agent/memory/01_project/overview.md` |
| Architecture | `.agent/memory/02_architecture/patterns.md` |
| Decisions | `.agent/memory/03_decisions/` |
| Problems | `.agent/memory/06_problems/` |
| Preferences | `.agent/memory/13_preferences/` |
"""


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate system prompt files from RLM-Anchor memory"
    )
    parser.add_argument(
        "--project-dir",
        default=".",
        help="Path to the project root (default: current directory)",
    )
    args = parser.parse_args()
    project_dir = Path(args.project_dir).resolve()

    print(f"🔄 Generating system prompts for: {project_dir}")

    # Extract data from memory
    language = extract_language(project_dir)
    code_style = extract_code_style_summary(project_dir)
    os_name = detect_os()
    project_summary = extract_project_summary(project_dir)

    print(f"  Language: {language}")
    print(f"  OS: {os_name}")
    print(f"  Code style: {len(code_style.split(chr(10)))} rules")

    # Read existing custom rules
    cursorrules_path = project_dir / ".cursorrules"
    claude_path = project_dir / "CLAUDE.md"
    gemini_path = project_dir / "GEMINI.md"

    custom_cursorrules = extract_custom_rules(
        read_file_safe(cursorrules_path), "comment"
    )
    custom_claude = extract_custom_rules(
        read_file_safe(claude_path), "markdown"
    )
    custom_gemini = extract_custom_rules(
        read_file_safe(gemini_path), "markdown"
    )

    # Generate .cursorrules
    cursorrules_content = generate_cursorrules(
        language, code_style, os_name, custom_cursorrules, project_summary
    )
    cursorrules_path.write_text(cursorrules_content, encoding="utf-8")
    lines_cr = len(cursorrules_content.split("\n"))
    print(f"  ✅ .cursorrules: {lines_cr} lines")

    # Generate CLAUDE.md
    claude_content = generate_markdown_prompt(
        language, code_style, os_name, custom_claude, project_summary, "claude"
    )
    claude_path.write_text(claude_content, encoding="utf-8")
    lines_cl = len(claude_content.split("\n"))
    print(f"  ✅ CLAUDE.md: {lines_cl} lines")

    # Generate GEMINI.md
    gemini_content = generate_markdown_prompt(
        language, code_style, os_name, custom_gemini, project_summary, "gemini"
    )
    gemini_path.write_text(gemini_content, encoding="utf-8")
    lines_gm = len(gemini_content.split("\n"))
    print(f"  ✅ GEMINI.md: {lines_gm} lines")

    print("\n✅ System prompts synced!")
    print(f"  Custom rules preserved: cursorrules={bool(custom_cursorrules)}, "
          f"claude={bool(custom_claude)}, gemini={bool(custom_gemini)}")


if __name__ == "__main__":
    main()
