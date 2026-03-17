---
name: orchestrator
description: |
  Use when: User wants to build, change, fix, refactor, brainstorm, research, review, plan, or understand a codebase. ALWAYS use this for any task that requires multiple steps, decision-making, or coordinating subagents. NOT for: simple one-off lookups like "read file X" or "what's in this folder."
---

# Workflow Orchestrator

Intent-driven workflow orchestrator. Classify user intent → jump to appropriate phase.

## Intent Router

**Step 1: Detect intent keywords**

| User says | Jump to | Example |
|-----------|---------|---------|
| "build", "implement", "thêm", "tạo" | `references/spec-form.md` | "build login feature" |
| "spec rồi", "có spec", "làm tiếp" | `references/plan.md` | "spec đã approve rồi" |
| "fix", "bug", "lỗi", "sửa" | → Step 2 | "fix cái bug login" |
| "brainstorm", "suy nghĩ", "ý tưởng" | `skills/brainstorming/SKILL.md` | "brainstorm về auth" |
| "research", "tìm hiểu" | `references/research.md` | "research về auth options" |
| "review", "kiểm tra" | `references/verify.md` | "review code này" |
| "docs", "tài liệu" | `references/doc-sync.md` | "update docs" |
| "cần biết", "giải thích" | `references/understand.md` | "project này dùng gì?" |
| "plan", "chia task" | `references/plan.md` | "chia task đi" |

**Step 2: For "fix" intents, assess scope**

- **Small fix** (typo, simple change, single file) → `references/execute.md` (do directly)
- **Complex fix** (bug in complex system, unclear root cause) → `references/understand.md`

**Step 3: For "refactor" intents**

- **Small refactor** (rename, extract function) → `references/execute.md`
- **Large refactor** (system-wide, multiple modules) → `references/understand.md` first (analyze scope), then `execute.md`

**Auto-suggest brainstorm** when:
- User has vague idea
- User says "not sure", "confused", "what if"
- Multiple options possible

## Phase References

| Phase | Reference | Purpose |
|-------|-----------|---------|
| Understand | `references/understand.md` | Analyze context, get clarification |
| Brainstorm | `skills/brainstorming/SKILL.md` | Explore ideas, generate options |
| Spec | `references/spec-form.md` | Create new spec |
| Spec Amend | `references/spec-amend.md` | Change existing spec |
| Plan | `references/plan.md` | Break into tasks |
| Execute | `references/execute.md` | Implement with subagent/team |
| Verify | `references/verify.md` | Test, review, validate |
| Research | `references/research.md` | Investigation |
| Doc Sync | `references/doc-sync.md` | Update documentation |

## Core: Docs is Xương Sống

**Every phase MUST update relevant docs:**

| Phase | Docs to update |
|-------|----------------|
| Understand | `docs/PROJECT.md` (if needed) |
| Brainstorm | `.workflow/brainstorm/` |
| Spec Form | `docs/specs/<slug>/spec.md` |
| Plan | `docs/specs/<slug>/plan.md` |
| Execute | Spec + code comments |
| Verify | `docs/specs/<slug>/spec.md` (SC results) |
| Research | `docs/architecture/` hoặc `docs/features/` |
| Doc Sync | All relevant docs |

## Task Scope

| Scope | Effort | Mode |
|-------|--------|------|
| Small | <30 min | Do yourself or single subagent |
| Medium | 30-120 min | 1-2 subagents |
| Large | >120 min | Agent team |

## Autonomy Rules

**Proceed without asking:**
- Implementation within spec
- Bug fixes (within understand → execute flow)
- Refactors that don't change behavior

**Always ask:**
- Spec changes (new/changed requirements)
- Scope expansion
- Irreversible operations
- Public API changes

**Never:**
- Ask permission to start
- Restate user's intent

## Announce

```
[workflow:<phase>] <Action> — <detail>
```

Example:
- `[workflow:understand] Analyzing: login bug`
- `[workflow:spec-form] Creating: auth-spec`
- `[workflow:execute] Dispatching implementer — Task 1/3`

## Commands

| Command | Action |
|---------|--------|
| `/brainstorm` | Start brainstorming |
| `/spec` | Start spec formation |
| `/execute` | Start execution |
| `/verify` | Start verification |
