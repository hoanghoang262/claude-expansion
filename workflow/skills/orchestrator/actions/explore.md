# explore

**Phase:** CLARIFY — Session start, new project, or unclear context

## Purpose

Understand the project completely before deciding what to do next.

## Iron Law

`SYNTHESIZE ENOUGH CONTEXT BEFORE DECIDING. Never jump to solutions.`

---

## Steps

### Step 1 — Find project root

Walk up from cwd looking for `docs/`:
- Found → go to Step 2
- Not found → go to **Init Memory** below

### Step 2 — Read project state

Read in order:
1. `docs/project.md` — vision, goals, tech stack
2. `docs/state.md` — current phase, wave progress, blockers
3. `docs/rules/` — all rule files (git-workflow, coding-standards, testing-strategy, constitution)
4. `docs/concerns/` — open concerns (CONCERN-*.md with status: open)
5. `docs/features/` — active features and their spec/plan status

### Step 3 — Analyze

Answer these before proceeding:
- What is the user's actual request? (surface vs underlying need)
- What phase are we in? (CLARIFY or IMPLEMENT)
- What is the next logical action?
- Are there open concerns that affect this work?
- Are there [NEEDS CLARIFICATION] markers in current spec?

Label every finding: `[fact]` / `[infer]` / `[assume]`

### Step 4 — Route

| Context                                         | Route to  |
|-------------------------------------------------|-----------|
| No project.md                                   | Init Memory |
| User provides resolution for an open concern    | **Concern Resolution** below |
| New feature request, no spec                    | `discuss` |
| Spec exists but has [NEEDS CLARIFICATION]       | `spec`    |
| Spec approved, no PLAN.md                       | `plan`    |
| PLAN.md exists, work incomplete                 | `execute` |
| Work done, verify missing                       | `verify`  |
| User confirms all done                          | Summarize + ask about next feature |

---

## Concern Resolution

When the user provides a product decision that resolves an open concern:

1. **Create `docs/decisions/YYYY-MM-DD-{slug}.md` [PERMANENT]** first:

```markdown
# Decision: {title}

Date: YYYY-MM-DD
Status: accepted
Prompted by: docs/concerns/{CONCERN-file}.md

## Context
{Why this decision was needed — the gap or ambiguity that surfaced it}

## Decision
{What was decided — specific, unambiguous}

## Consequences
{What this enables, what it constrains, any follow-on work needed}
```

2. **Update `docs/concerns/{CONCERN-file}.md`** — set `Status: resolved`, add:
```
Resolved: YYYY-MM-DD
Resolution: see docs/decisions/{slug}.md
```

3. **Do NOT delete the concern file** — it is `[PERMANENT]`. It serves as the audit trail of what was discovered and when.

4. If the decision requires implementation (e.g., "build retry flow"), offer to open a `discuss` action for the new feature. Do not implement without a spec.

---

## Init Memory

When no `docs/` found. Ask user (one wave of questions):

```
I don't see a docs/ folder. Let me set up project memory.

1. What type of project is this? (web app / CLI tool / library / data pipeline / other)
2. What is the main goal? (one sentence)
3. Any existing tech stack constraints?
4. Any team conventions I should know? (git workflow, testing approach)
```

After user responds, create:
```
docs/
├── project.md          ← fill from answers
├── state.md            ← Phase: CLARIFY, Action: discuss
└── rules/
    ├── constitution.md ← copy from template
    ├── git-workflow.md ← default or from user answers
    └── coding-standards.md ← default or from user answers
```

Use templates from `skills/orchestrator/templates/`.
