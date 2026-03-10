---
name: spec-formation
description: Transform clear intent into an approved spec. Draft immediately, clarify inline, lock on approval.
---

# Spec Formation

Own the full journey from intent to locked contract.
Draft first — clarify on the draft — approve — lock.

---

## Step 0 — Classify track

Before anything else, determine the track from the intent:

| Track | Signals |
|-------|---------|
| `light` | Single behavior, obvious scope, no data model, no integration |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale concerns, many unknowns |

State the track explicitly before proceeding. This controls which sections are required.

---

## Step 1 — Load context

Check in order:
1. `.workflow/specs/<slug>/idea.md` — brainstorm summary if it exists
2. `.workflow/specs/<slug>/working.md` — previous draft if in progress
3. `.workflow/PROJECT.md` — project constraints, key decisions, non-negotiables

If PROJECT.md exists, note any constraints that apply to this spec before writing.

---

## Step 2 — Draft

Write the spec immediately in `working.md`. Do not ask questions before drafting.
Where information is missing, write `[NEEDS CLARIFICATION: <specific question>]` inline.

**Spec structure — include sections required for the track:**

```markdown
# Spec: <slug>

Status: draft
Track: <light|standard|heavy>
Created: YYYY-MM-DD

## Goal
One sentence. What this builds and why.

## Scope
In scope: ...
Out of scope: ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<plain language>
Acceptance scenarios:
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>    ← WHAT, never HOW
- FR-002: Users MUST be able to <action>
[NEEDS CLARIFICATION: <question>]            ← mark gaps inline

## Key Entities          ← if data is involved
- <Entity>: <what it represents, attributes, relationships>

## Non-Functional        ← heavy only
- Performance: <measurable target>
- Security: <specific constraint>
- Scale: <volume assumption>

## Edge Cases            ← standard/heavy only
- What happens when <boundary>?
- How does system handle <failure>?

## Success Criteria
- SC-001: <measurable outcome>
- SC-002: <measurable outcome>

## Open Items
- <item deferred to planning/implementation>
```

**FR writing rules — WHAT not HOW:**
- ✅ `System MUST notify users when payment fails`
- ❌ `System MUST send a webhook to Stripe`
- ✅ `Users MUST be able to recover access without contacting support`
- ❌ `Implement password reset via email token with 1hr expiry`

---

## Step 3 — Resolve gaps

After drafting, collect all `[NEEDS CLARIFICATION]` markers.
Triage each:
- Blocks spec correctness → **ask now**
- Better answered during planning/implementation → **move to Open Items**

**Ask all independent questions in one message. Max 5 per session.**

Per question format:
```
**Q{N}: <question>**
> Recommended: **{option}** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |

Reply A/B/C or "yes" to accept, or a short custom answer.
```

After each answer:
- Replace the `[NEEDS CLARIFICATION]` with the clarified detail
- Update the affected section

Stop when: all blocking gaps resolved, user says "proceed", or 5 questions reached.

---

## Step 4 — Self-validate

Before presenting for approval, check every item:

```
[ ] Track is stated
[ ] No [NEEDS CLARIFICATION] markers remain (or moved to Open Items)
[ ] Every FR uses MUST + testable behavior, no HOW details
[ ] Every SC is measurable — numbers, not adjectives
[ ] Scope has both in-scope AND out-of-scope
[ ] User stories have Given/When/Then (standard/heavy)
[ ] PROJECT.md constraints are respected
[ ] Light track: fits on one screen
```

Fix any failures before presenting.

---

## Step 5 — Present & approve

Show the full spec. Ask:
```
Does this capture what you want to build?
Approve to lock it, or tell me what to change.
```

Revise until explicitly approved. Never lock without approval.

---

## Step 6 — Lock

On approval:
1. Copy `working.md` → `approved.md`, set `Status: approved`
2. Delete `working.md` (no longer needed)
3. Update `.workflow/STATE.md`:

```
phase: planning
active-spec: <slug>
track: <light|standard|heavy>
next-action: Run task-breakdown on approved.md
blocked-by: none
last-updated: <today>
```

4. Announce:
```
[Spec locked] → .workflow/specs/<slug>/approved.md
Next: task-breakdown
```

---

## Memory rule

| File | Lifecycle |
|------|-----------|
| `idea.md` | Persistent reference — never delete |
| `working.md` | Temporary — delete after `approved.md` is created |
| `approved.md` | Permanent locked contract — never overwrite, use `spec-amendment` |
| `STATE.md` | Always updated on phase transition |
