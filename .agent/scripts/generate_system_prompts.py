"""
generate_system_prompts.py — Generate .cursorrules, CLAUDE.md, GEMINI.md from RLM-Anchor memory.

Usage:
    python .agent/scripts/generate_system_prompts.py [--project-dir .]

This script reads memory files and generates compact system prompt files
that IDEs inject into every AI request automatically.
"""

import argparse
import re
import sys
from datetime import datetime
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


def validate_memory_availability(project_dir: Path) -> bool:
    """Check if critical memory files are present before running."""
    critical_files = [
        project_dir / ".agent" / "memory" / "13_preferences" / "coding_style.md",
        project_dir / ".agent" / "memory" / "13_preferences" / "language.md",
    ]
    missing = [str(f) for f in critical_files if not f.exists()]
    if missing:
        print(f"[ERROR] Critical memory missing: {', '.join(missing)}")
        return False
    return True


def verify_sync_results(project_dir: Path, workflow_count: int):
    """Update health summary and correlate workflows with copilot prompts."""
    prompt_files = [
        project_dir / ".cursorrules",
        project_dir / "CLAUDE.md",
        project_dir / "GEMINI.md",
        project_dir / ".github" / "copilot-instructions.md"
    ]
    
    today = datetime.now().date()
    updated_today = 0
    for pf in prompt_files:
        if pf.exists() and datetime.fromtimestamp(pf.stat().st_mtime).date() == today:
            updated_today += 1

    prompts_dir = project_dir / ".github" / "prompts"
    actual_prompts = len(list(prompts_dir.glob("*.prompt.md"))) if prompts_dir.exists() else 0
    
    print("\n[V] Sync Health Summary:")
    print(f"  - Core Prompt Files Updated: {updated_today}/{len(prompt_files)}")
    print(f"  - Workflow/Copilot Sync: {actual_prompts}/{workflow_count} tasks")
    
    if updated_today < len(prompt_files):
        print("  [!] Warning: Some core prompt files were not updated.")
    if actual_prompts != workflow_count:
        print(f"  [!] Warning: Mismatch detected between .agent/workflows/ ({workflow_count}) and .github/prompts/ ({actual_prompts})")


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

# Session logging: After ANY work, append to .agent/memory/07_context/current_session.md
# Auto-compression: IF "Topics Discussed" > 50 items -> summarize to 20 key points.
# Context7 MCP: Always use Context7 MCP for library/API documentation, code generation, setup or configuration.

# Token Efficiency: Your context window is limited (128k). To stay in one chat longer:
# 1. FAVOR RLM memory over global searches (@workspace).
# 2. **Anchor Orchestra**: For complex tasks, use /anchor_plan to create a Spec file in .agent/memory/07_context/specs/.
# 3. **Orchestration**: Act as the ORCHESTRATOR. Delegate coding to subagents via `runSubagent` or a new chat using the Spec file.
# 4. DO NOT read entire files if you only need a specific part; use line ranges.
# 5. MINIMIZE terminal output; show only errors or concise summaries.
# 6. IGNORE other AI system files: CLAUDE.md, GEMINI.md, .github/copilot-instructions.md.

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
    """Generate CLAUDE.md, GEMINI.md, or copilot-instructions.md content."""
    ide_names = {
        "claude": "Claude Code",
        "gemini": "Gemini CLI / Antigravity",
        "copilot": "GitHub Copilot Chat (VS Code)",
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

    exclusions = {
        "claude": ".cursorrules, GEMINI.md, .github/copilot-instructions.md",
        "gemini": ".cursorrules, CLAUDE.md, .github/copilot-instructions.md",
        "copilot": ".cursorrules, CLAUDE.md, GEMINI.md",
    }
    other_files = exclusions.get(target_ide, "")
    exclusion_rule = f"5. IGNORE other AI system files: {other_files}." if other_files else ""

    return f"""# RLM-Anchor — System Rules for {ide_label}

> **This file is auto-read by {ide_label} on EVERY request.**
> Keep it compact (<80 lines). Details → `.agent/memory/`

---

## 🔴 CRITICAL RULES (never violate)

**Auto-Context Load (MANDATORY)**: IF this is the FIRST message in a new chat → you MUST automatically read `.agent/memory/07_context/current_session.md` before doing anything else. In your VERY FIRST response, start with the exact line: `✅ Context loaded from current_session.md`. Failure to do this will confuse the user.

**Language**: ALWAYS respond in: **{language}**

**Session logging**: After ANY work, append it to `.agent/memory/07_context/current_session.md` (Topics Discussed).
**Auto-compression**: IF "Topics Discussed" > 50 items → summarize them into 20 key points immediately.
**Context7 MCP**: Always use Context7 MCP when I need library/API documentation, code generation, setup or configuration steps without me having to explicitly ask.

**Token Efficiency**: Your context window is limited (128k). To stay in one chat longer:
1. FAVOR RLM memory over global searches (`@workspace`).
2. **Anchor Orchestra**: For complex tasks, use `/anchor_plan` to create a Spec file in `.agent/memory/07_context/specs/`.
3. **Orchestration**: Act as the ORCHESTRATOR. Delegate coding to subagents via `runSubagent` or a new chat using the Spec file.
4. DO NOT read entire files if you only need a specific part; use line ranges.
5. MINIMIZE terminal output; show only errors or concise summaries.
{exclusion_rule}

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
| `/wakeup` | Start session |
| `/sleep` | End session |
| `/remember` | Save to memory |
| `/recall` | Search memory |

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


def sync_workflows_to_copilot(project_dir: Path):
    """Mirror .agent/workflows/*.md to .github/prompts/*.prompt.md."""
    workflows_dir = project_dir / ".agent" / "workflows"
    prompts_dir = project_dir / ".github" / "prompts"

    if not workflows_dir.exists():
        return

    prompts_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for wf_file in workflows_dir.glob("*.md"):
        # Map filenames: anchor_sync.md -> anchor-sync.prompt.md
        name = wf_file.stem.replace("_", "-")
        target_file = prompts_dir / f"{name}.prompt.md"
        
        content = wf_file.read_text(encoding="utf-8")
        
        # Extract title/description if possible, or use filename
        description = name.replace("-", " ").capitalize()
        
        # Prepare Copilot-style prompt header
        header = (
            "---\n"
            "agent: agent\n"
            f"description: \"{description} (RLM-Anchor)\"\n"
            "---\n\n"
        )
        
        # If the file already has frontmatter, we merge or replace
        if content.startswith("---"):
            # Strip existing frontmatter
            parts = content.split("---", 2)
            if len(parts) >= 3:
                content = parts[2].strip()
        
        final_content = header + content
        target_file.write_text(final_content, encoding="utf-8")
        count += 1
    
    print(f"  [OK] Copilot prompts: {count} commands synced")
    return count


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

    if not validate_memory_availability(project_dir):
        sys.exit(1)

    print(f"[*] Generating system prompts for: {project_dir}")

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
    copilot_dir = project_dir / ".github"
    copilot_path = copilot_dir / "copilot-instructions.md"

    # Pre-check for Custom Rules loss safeguard
    def safe_extract(path, fmt):
        content = read_file_safe(path)
        extracted = extract_custom_rules(content, fmt)
        if not extracted and "🎯 CUSTOM PROJECT RULES" in content:
            # Check if it actually had content beyond headers
            if len(content.split("🎯 CUSTOM PROJECT RULES")[1].strip()) > 50:
                 print(f"  [!] Safeguard: Custom rules found in {path.name} but extraction returned empty. Aborting to prevent overwrite.")
                 sys.exit(1)
        return extracted

    custom_cursorrules = safe_extract(cursorrules_path, "comment")
    custom_claude = safe_extract(claude_path, "markdown")
    custom_gemini = safe_extract(gemini_path, "markdown")
    custom_copilot = safe_extract(copilot_path, "markdown")

    # Generate .cursorrules
    cursorrules_content = generate_cursorrules(
        language, code_style, os_name, custom_cursorrules, project_summary
    )
    cursorrules_path.write_text(cursorrules_content, encoding="utf-8")
    lines_cr = len(cursorrules_content.split("\n"))
    print(f"  [OK] .cursorrules: {lines_cr} lines")

    # Generate CLAUDE.md
    claude_content = generate_markdown_prompt(
        language, code_style, os_name, custom_claude, project_summary, "claude"
    )
    claude_path.write_text(claude_content, encoding="utf-8")
    lines_cl = len(claude_content.split("\n"))
    print(f"  [OK] CLAUDE.md: {lines_cl} lines")

    # Generate GEMINI.md
    gemini_content = generate_markdown_prompt(
        language, code_style, os_name, custom_gemini, project_summary, "gemini"
    )
    gemini_path.write_text(gemini_content, encoding="utf-8")
    lines_gm = len(gemini_content.split("\n"))
    print(f"  [OK] GEMINI.md: {lines_gm} lines")

    # Generate .github/copilot-instructions.md
    copilot_dir.mkdir(parents=True, exist_ok=True)
    copilot_content = generate_markdown_prompt(
        language, code_style, os_name, custom_copilot, project_summary, "copilot"
    )
    copilot_path.write_text(copilot_content, encoding="utf-8")
    lines_cp = len(copilot_content.split("\n"))
    print(f"  [OK] .github/copilot-instructions.md: {lines_cp} lines")

    # Sync all workflows to Copilot commands
    workflow_count = sync_workflows_to_copilot(project_dir)

    print("\n[DONE] System prompts synced!")
    print(f"  Custom rules preserved: cursorrules={bool(custom_cursorrules)}, "
          f"claude={bool(custom_claude)}, gemini={bool(custom_gemini)}, "
          f"copilot={bool(custom_copilot)}")

    # Verification Phase
    verify_sync_results(project_dir, workflow_count)


if __name__ == "__main__":
    main()
