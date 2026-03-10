---
name: orchestrator
description: Loaded at every session start — routes AI to the right workflow skill based on task intent and complexity
---

# Workflow Orchestrator

You are operating inside the **workflow plugin**. This skill is your routing guide.
Read it at the start of every session, then act accordingly.

## Your First Action Every Session

1. Check if a `workflow-state` block was injected into your context.
   - If yes: read the current phase, active spec, and next action — resume from there.
   - If no: this is a fresh project or fresh task.
2. Read the user's first message to understand intent.
3. Classify and route (see below).

---

## Complexity Classification

Before choosing a flow, classify the task:

| Track | Signals | Ceremony |
|---|---|---|
| `light` | Single file, obvious fix, no behavior change, typo | Skip clarify + spec → execute directly |
| `standard` | New behavior, feature, multi-file change | clarify (if needed) → spec-formation → task-breakdown → execute → review → doc-sync |
| `heavy` | Architecture change, new system, risky migration, breaking change | Full standard flow + extra spec review gate before execute |

Classify based on **intent signals**, not file count alone. When in doubt, go `standard`.

---

## Skill Routing Rules

### When to use each skill:

| Situation | Skill |
|---|---|
| User has vague idea, doesn't know what to build | `workflow:brainstorming` |
| Task is clear but has ambiguous gaps | `workflow:clarify` |
| Ready to write spec (intent clear, no gaps) | `workflow:spec-formation` |
| Approved spec exists, need task breakdown | `workflow:task-breakdown` |
| Tasks ready, time to implement | `workflow:execute` (subagent) |
| Implementation done, need review | `workflow:review` (subagent) |
| Task complete, update docs | `workflow:doc-sync` (subagent) |
| Approved spec needs to change | `workflow:spec-amendment` |
| Bug or unexpected failure | `superpowers:systematic-debugging` |
| About to claim work is done | `superpowers:verification-before-completion` |
| All tasks done, ready to merge | `superpowers:finishing-a-development-branch` |

### Decision flow:

```
User message arrives
    |
    ├─ Resume? → read STATE.md → jump to current phase skill
    |
    └─ New task?
          |
          ├─ Intent too vague? → workflow:brainstorming
          ├─ Intent clear, gaps exist? → workflow:clarify
          └─ Intent clear, no gaps?
                |
                ├─ light track → execute directly
                └─ standard/heavy → workflow:spec-formation
```

---

## Autonomy Boundaries

**Act without asking:**
- Implementation details consistent with approved spec
- Test coverage improvements
- Bug fixes within current scope
- Refactors that don't change external behavior

**Always ask before acting:**
- Changing approved spec
- Architecture or dependency changes
- Expanding scope beyond what was approved
- Anything contradicting a previous user decision

---

## STATE.md Format

When you update `.workflow/STATE.md`, use this format:

```markdown
# Workflow State

phase: <clarify|spec|planning|execute|review|done>
active-spec: <spec slug or "none">
track: <light|standard|heavy>
next-action: <one sentence — what happens next>
blocked-by: <blocker description or "none">
last-updated: <YYYY-MM-DD>
```

Update STATE.md at every phase transition.

---

## Key Principle

> Standard flow always runs. Ceremony scales with complexity.
> You own execution. User owns intent and strategic decisions.
