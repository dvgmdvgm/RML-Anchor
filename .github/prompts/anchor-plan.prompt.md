---
agent: agent
description: "Anchor plan (RLM-Anchor)"
---

# /anchor_plan — Anchor Orchestra: Planning Phase

## Usage

```
/anchor_plan [task description]
```

---

## Purpose

The **Planning Phase** is the mandatory first step before any major code implementation. It ensures:
1. The AI understands the project structure and architecture.
2. The context remains clean by isolating research from coding.
3. The user approves the technical design before work begins.

---

## Execution Steps

### 1. Identify Task Scope
- Analyze the user's request.
- Use `/recall` to find related decisions (categories `02`, `03`) and code patterns (category `05`).
- List files in relevant directories to understand the structure.

### 2. Research Phase
- Read headers/skeletons of relevant files (use line ranges to save tokens).
- Identify dependencies and potential side effects.
- **NEVER** edit files during this phase.

### 3. Generate Specification File (The "Bridge")
Create a new file in `.agent/memory/07_context/specs/[TASK-NAME].md`.

**Spec File Template:**
```markdown
# 📝 Spec: [Task Name]
> Date: YYYY-MM-DD
> Origin: /anchor_plan

## 🎯 Objective
[Brief description of what we are achieving]

## 🏗️ Architecture & Context
- **Root Directory**: ...
- **Main Files Involved**: ...
- **Relevant ADRs**: [Links to category 03 entries]

## 🛠️ Proposed Changes
[Detailed step-by-step technical instructions for the coding agent]
- [ ] Create file X...
- [ ] Implement function Y in file Z...
- [ ] Update imports...

## ✅ Verification & Tests
- [ ] Run command `npm test`
- [ ] Verify endpoint `/api/v1/...`
```

### 4. Update Current Session
Log the creation of the spec file in `.agent/memory/07_context/current_session.md`.

### 5. Present to User for Approval
Output the summary of the plan in the user's configured language.

```markdown
✅ **Plan Created: [Task Name]**

I have analyzed the project and prepared a technical specification:
- **Spec Path**: `.agent/memory/07_context/specs/[NAME].md`
- **Estimated Changes**: [Small / Medium / Large]

Please review the spec file. Once approved, we will proceed to implementation using a fresh subagent or a clean session.

**Next step**: `/anchor_implement [NAME]` (or manual approval)
```

---

## Orchestration Rule
> [!IMPORTANT]
> If a task is complex (requires more than 2 files or 20 lines of code), the AI **MUST** suggest `/anchor_plan` first. **NEVER** bloat the main conversation context with research data and implementation code simultaneously.