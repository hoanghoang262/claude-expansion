---
name: orchestrator
description: |
  Use when: User wants to build, change, fix, refactor, brainstorm, research, review, plan, or understand a codebase. ALWAYS use this for multi-step tasks, decision-making, or coordinating subagents. NOT for: simple lookups like "read file X" or "what's in this folder."
---

# Workflow Orchestrator

Classify user intent → jump to appropriate phase.

## Intent Router

**Detect keywords and route:**

| User says | Jump to | Notes |
|-----------|---------|-------|
| "build", "implement", "add", "create" | `references/spec-form.md` | New feature |
| "spec ready", "approved", "continue" | `references/plan.md` | Has spec |
| "fix", "bug", "error" | → Assess scope | Small→execute, Complex→understand |
| "brainstorm", "not sure", "options" | `skills/brainstorming/SKILL.md` | Vague intent |
| "research", "find out" | `references/research.md` | Investigation |
| "review", "check" | `references/verify.md` | Validation |
| "docs", "documentation" | `references/doc-sync.md` | Doc updates |
| "what is", "explain" | `references/understand.md` | Comprehension |

**Scope rules:**
- Small fix (typo, single file) → execute directly
- Complex fix (unclear root cause) → understand first
- Small refactor (rename) → execute
- Large refactor (multi-module) → understand → execute

**Auto-suggest brainstorm** when: vague idea, "not sure", "what if", multiple options

## Phase References

| Phase | Reference | Purpose |
|-------|-----------|---------|
| Understand | `references/understand.md` | Analyze, clarify |
| Brainstorm | `skills/brainstorming/SKILL.md` | Explore options |
| Spec | `references/spec-form.md` | Create spec |
| Plan | `references/plan.md` | Break into tasks |
| Execute | `references/execute.md` | Implement |
| Verify | `references/verify.md` | Test, validate |
| Research | `references/research.md` | Investigation |
| Doc Sync | `references/doc-sync.md` | Update docs |

## Docs is Xương Sống

Every phase MUST update relevant docs:

| Phase | Docs to update |
|-------|----------------|
| Understand | `docs/PROJECT.md` |
| Brainstorm | `.workflow/brainstorm/` |
| Spec | `docs/specs/<slug>/spec.md` |
| Plan | `docs/specs/<slug>/plan.md` |
| Execute | Spec + code comments |
| Verify | `docs/specs/<slug>/spec.md` |
| Research | `docs/architecture/` |
| Doc Sync | All relevant docs |

## Task Scope

| Scope | Effort | Mode |
|-------|--------|------|
| Small | <30 min | Do yourself or subagent |
| Medium | 30-120 min | 1-2 subagents |
| Large | >120 min | Agent team |

## Autonomy Rules

**Proceed without asking:**
- Implementation within spec
- Bug fixes (understand → execute)
- Refactors (no behavior change)

**Always ask:**
- Spec changes
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
- `[workflow:spec-form] Creating: auth-spec`
- `[workflow:execute] Dispatching implementer — Task 1/3`

## Commands

| Command | Action |
|---------|--------|
| `/brainstorm` | Start brainstorming |
| `/spec` | Start spec formation |
| `/execute` | Start execution |
| `/verify` | Start verification |
