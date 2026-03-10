---
name: spec-formation
description: Transform clarified intent into an approved spec — the locked contract that drives all execution.
---

# Spec Formation

Turn clear intent into a locked spec (`approved.md`).
The spec is the contract. Once approved, it does not change without `spec-amendment`.

---

## Inputs

Before starting, check what exists in `.workflow/specs/<slug>/`:
- `idea.md` — brainstorm summary (if ran)
- `working.md` — clarify output with encoded answers (if ran)
- Neither → derive from the user's stated intent directly

---

## The Spec Structure

Scale each section to task complexity. Heavy tasks use all sections.
Light tasks may need only Goal + Acceptance Criteria.

```markdown
# Spec: <feature-name>

**Status:** draft | approved
**Track:** light | standard | heavy
**Created:** YYYY-MM-DD

## Goal
One sentence. What this builds and why.

## Scope
### In scope
- ...

### Out of scope
- ...

## User Stories *(standard/heavy only)*
### Story 1 — <title> (P1)
<plain language description>

**Acceptance scenarios:**
- Given <state>, when <action>, then <outcome>
- Given <state>, when <action>, then <outcome>

### Story 2 — <title> (P2)
...

## Functional Requirements
- **FR-001:** System MUST <specific, testable behavior>
- **FR-002:** System MUST <specific, testable behavior>

*Mark unresolved items:* `[NEEDS CLARIFICATION: <question>]`

## Key Entities *(if feature involves data)*
- **<Entity>:** <what it represents, key attributes, relationships>

## Non-Functional Requirements *(standard/heavy only)*
- **Performance:** <measurable target>
- **Security:** <specific constraint>
- **Scale:** <volume/load assumptions>

## Edge Cases & Error Handling *(standard/heavy only)*
- What happens when <boundary condition>?
- How does system handle <failure scenario>?

## Success Criteria
- **SC-001:** <measurable outcome — users can X in under Y>
- **SC-002:** <measurable outcome>

## Open Items *(deferred from clarify)*
- <item> → resolve during: <planning | implementation>
```

---

## Process

### 1. Draft

Write the spec in `working.md` using the structure above.
Scale sections to the track — do not add sections for their own sake.

As you write, if you find a gap:
- Small gap → make a reasonable assumption, note it inline
- Blocking gap → add `[NEEDS CLARIFICATION]`, flag to user before locking

### 2. Self-validate

Before presenting for approval, check:

```
[ ] No [NEEDS CLARIFICATION] markers remain (or all flagged to user)
[ ] Every FR is testable — no vague verbs ("handle", "support", "manage")
[ ] Every SC is measurable — no adjectives without numbers
[ ] Scope is explicit — in-scope AND out-of-scope stated
[ ] No implementation details in FRs (WHAT not HOW)
[ ] Light track: spec fits on one screen
[ ] Heavy track: all 8 sections present
```

### 3. Present & Approve

Show the spec to the user. Ask:
```
Does this spec capture what you want to build?
Approve to lock it, or tell me what to change.
```

Revise until approved. Do not lock without explicit approval.

### 4. Lock

On approval:
1. Copy `working.md` → `approved.md`
2. Update `Status: approved` in `approved.md`
3. Update `.workflow/STATE.md`:
   ```
   phase: planning
   active-spec: <slug>
   next-action: Run task-breakdown on approved.md
   ```
4. Announce:
   ```
   [Spec approved] → .workflow/specs/<slug>/approved.md
   Next: task-breakdown
   ```

---

## Scale

| Track | Sections required | Length |
|-------|-------------------|--------|
| `light` | Goal + FRs + Success Criteria | < 1 screen |
| `standard` | All except NFRs and Edge Cases | 1–2 pages |
| `heavy` | All sections | 2–4 pages |

**Never pad a light spec to look like a heavy one.**
A 3-line spec that captures a clear task is better than a 2-page spec with filler.
