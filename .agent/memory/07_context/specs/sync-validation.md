# 📝 Spec: Sync Script Validation
> Date: 2026-02-27
> Origin: /anchor_plan

## 🎯 Objective
Add a validation layer to `generate_system_prompts.py` to ensure that synchronization completes correctly, preserves user data, and maintains consistency across all IDE rule files.

## 🏗️ Architecture & Context
- **Main File**: `.agent/scripts/generate_system_prompts.py`
- **Output Files**: `.cursorrules`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.github/prompts/*.prompt.md`
- **Logic**: The script extracts data from `.agent/memory/` and writes to IDE-specific files.

## 🛠️ Proposed Changes

### 1. Integrity Check (Pre-run)
Add a function `validate_memory_availability(project_dir: Path)`:
- Check if `.agent/memory/13_preferences/code_style.md` exists.
- Check if `.agent/memory/13_preferences/language.md` or `language_local.md` contains valid settings.

### 2. Custom Rules Preservation Safeguard
Update `main()` to verify `custom_rules` extraction:
- If a system prompt file existed but `extract_custom_rules()` returned an empty string while the original file *had* a CUSTOM RULES section (detected via regex), trigger a warning or abort to prevent data loss.

### 3. Post-Sync Report & Verification
Implement `verify_sync_results(project_dir: Path)`:
- Verify that 4 main prompt files were updated today.
- Verify that the number of files in `.github/prompts/` matches the number of files in `.agent/workflows/`.
- Print a summary table of the sync health.

### 4. Integration with `main()`
- Call `validate_memory_availability` at start.
- Call `verify_sync_results` at end.
- Use exit codes: `0` for success, `1` for critical errors (e.g., missing memory), `2` for warnings (e.g., mismatch in Copilot prompts).

## ✅ Verification & Tests
- [ ] Run `py -3 .agent/scripts/generate_system_prompts.py` and check the health table output.
- [ ] Manually delete a workflow file and verify that the sync script detects the orphaned `.prompt.md` file (or reports the count mismatch).
- [ ] Verify that adding a custom rule in `.cursorrules` is properly reported as "Preserved" in the summary.
