#!/bin/bash
# ═══════════════════════════════════════════════════
# RLM-Anchor: Git skip-worktree setup
# ═══════════════════════════════════════════════════
#
# This script marks _index.md files with skip-worktree flag.
# Git will keep the clean template in the repo, but your
# local modifications (user entries) will be invisible to git.
#
# Run ONCE after cloning or setting up the project.
#
# To UNDO (if you need to commit template changes):
#   bash .agent/scripts/skip_worktree_undo.sh
# ═══════════════════════════════════════════════════

echo "🔧 Setting skip-worktree on _index.md files..."
echo ""

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

count=0
for f in "${FILES[@]}"; do
    if [ -f "$f" ]; then
        git update-index --skip-worktree "$f"
        echo "  ✅ $f"
        ((count++))
    else
        echo "  ⚠️ SKIP (not found): $f"
    fi
done

echo ""
echo "✅ Done! $count files marked with skip-worktree."
echo ""
echo "Your local changes to these files will NOT appear in git status/diff."
echo "Git will always push the clean template versions."
echo ""
echo "To undo: bash .agent/scripts/skip_worktree_undo.sh"
