---
description: Phase 2 of the Anchor Orchestra system - Execute changes based on a Spec file.
---

# /anchor_implement — Anchor Orchestra: Implementation Phase

## Usage

```
/anchor_implement [spec-name]
```

---

## Purpose

The **Implementation Phase** is where the actual coding happens. It is designed to be run in a clean context to ensure high precision and minimal token waste.

---

## Execution Steps

### 1. Load the Specification
- Read the file located at `.agent/memory/07_context/specs/[spec-name].md`.
- **IMMEDIATE RULE**: Do not waste time researching the whole project. Trust the Spec file.

### 2. Prepare Environment
- Locate the files mentioned in the "Main Files Involved" section of the Spec.
- Check if they exist.

### 3. Implementation Loop
For each item in the "Proposed Changes" list:
1. Read the target code block.
2. Apply the change using `replace_file_content` or `multi_replace_file_content`.
3. Verify syntax/lint if possible.

### 4. Verification
- Run the commands specified in the "Verification & Tests" section of the Spec.
- If errors occur, attempt to fix them within the scope of the Spec.

### 5. Cleanup & Reporting
- If successful, notify the user.
- **NEVER** archive the spec file automatically (user may want to review it).

---

## Orchestration Note
> [!TIP]
> This command is best used in a **New Chat** to provide the AI with a fresh context window of 128k specifically for the coding task.
