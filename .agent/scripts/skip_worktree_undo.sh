#!/bin/bash
# Undo skip-worktree flags (when you need to commit template changes)

echo "🔓 Removing skip-worktree flags..."

FILES=(
    ".agent/memory/01_project/_index.md"
    ".agent/memory/02_architecture/_index.md"
    ".agent/memory/03_decisions/_index.md"
    ".agent/memory/04_domain/_index.md"
    ".agent/memory/05_code/_index.md"
    ".agent/memory/06_problems/_index.md"
    ".agent/memory/07_context/_index.md"
    ".agent/memory/08_people/_index.md"
    ".agent/memory/09_external/_index.md"
    ".agent/memory/10_testing/_index.md"
    ".agent/memory/11_deployment/_index.md"
    ".agent/memory/12_roadmap/_index.md"
    ".agent/memory/13_preferences/_index.md"
    ".agent/memory/07_context/current_session.md"
    ".agent/memory/07_context/pending_tasks.md"
)

for f in "${FILES[@]}"; do
    if [ -f "$f" ]; then
        git update-index --no-skip-worktree "$f"
        echo "  🔓 $f"
    fi
done

echo ""
echo "✅ Flags removed. Local changes to these files are now visible to git."
echo "⚠️  Don't forget to re-run skip_worktree_setup.sh after committing!"
