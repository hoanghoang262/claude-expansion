---
name: spec/formation
description: Transform intent into approved spec. Draft immediately, clarify blocking gaps only, lock on approval.
---

# Spec Formation

**Two phases: Clarify → Lock.**
Draft first. Mark gaps inline. Ask only what blocks the contract.

---

## Step 0 — Classify track

| Track | Signals |
|-------|---------|
| `light` | Single behavior, obvious scope, no data model, no integration |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale/compliance |

State track before proceeding.

---

## Step 1 — Load context

1. `.workflow/specs/<slug>/idea.md` — brainstorm summary if exists
2. `.workflow/specs/<slug>/working.md` — previous draft if in progress
3. `.workflow/PROJECT.md` — constraints, tech stack, key decisions

---

## PHASE 1: CLARIFY

```
[workflow:spec-formation] Phase 1 — Clarifying: <slug>
```

### Draft immediately

Write `working.md` now. Do not ask questions before drafting.

**If prompt is unclear:** Draft with best interpretation. Mark your interpretation as assumption.
**Only exception:** Prompt so vague no FR can be written → ask 1 question minimum needed.

Where information is missing, write `[GAP: <specific question>]` inline.

### Spec structure

```markdown
# Spec: <slug>

Status: draft
Track: <light|standard|heavy>
Created: YYYY-MM-DD

## Goal
One sentence. What this builds and why.

## Scope
In scope:
- ...
Out of scope:
- ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<who does what and why>
Acceptance:
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>
- FR-002: Users MUST be able to <action>
[GAP: <question>]

## Key Entities          ← when data is involved
- <Entity>: <what it is, key attributes, relationships>

## Assumptions
- A-001: <assumed true> — if wrong, impacts: <FR-N>

## Non-Functional        ← heavy only or explicitly required
- Performance: <measurable target>
- Security: <specific constraint>

## Interaction & UX      ← when UI is involved
- <critical user journey>
- Error states: <what user sees when X fails>

## Integration           ← when external systems involved
- <System>: <what we depend on, failure mode>

## Edge Cases & Errors   ← standard/heavy only
- What happens when <boundary condition>?

## Success Criteria
- SC-001 (covers FR-001): <measurable outcome>

## Open Items
- <item deferred to planning/implementation>
```

**FR rule — WHAT not HOW:**
- ✅ `System MUST notify users when payment fails`
- ❌ `System MUST send Stripe webhook on payment failure`

### Triage gaps

For each `[GAP]`:

| Decision | When |
|----------|------|
| **Ask now** | Answer changes FR, SC, entity shape, or scope boundary |
| **Defer to Open Items** | Tech choices, implementation edge cases |
| **Assume + note** | Low stakes, reasonable default exists |

### Ask blocking gaps

Group independent questions in one message. Max 5 per session.

```
**Q1: <question>**
> Recommended: **<option>** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |

Reply A/B, "yes" to accept recommendation, or custom answer.
```

After each answer: replace `[GAP]` with resolved detail, log in `## Clarifications`.

Run one more gap scan after answers — new answers can reveal new gaps. Max 3 rounds; remaining gaps → Open Items.

---

## PHASE 2: LOCK

```
[workflow:spec-formation] Phase 2 — Locking: <slug>
```

### Self-validate before presenting

```
[ ] Track stated
[ ] No [GAP] remain (or moved to Open Items with rationale)
[ ] Every FR: MUST + testable, no HOW details
[ ] Every SC: measurable — numbers not adjectives
[ ] Every FR maps to at least one SC
[ ] Scope: in AND out stated explicitly
[ ] Stories have Given/When/Then (standard/heavy)
[ ] PROJECT.md constraints respected
[ ] Light track: fits on one screen
```

### Present for approval

**Light track:**
```
**Spec: <slug>** (light)
Goal: <one sentence>
Will do: <2-3 bullet FRs>
Won't do: <scope boundary>
Done when: <SC-001>

Looks right? Reply "yes" or give me the next task.
```
Implicit approval: any affirmative reply counts.

**Standard/Heavy:**
```
Spec ready for review.
Resolved: {N} gaps. Deferred: {list}.

Approve to lock, or tell me what to change.
```
Requires explicit approval.

### Lock

On approval:
1. Copy `working.md` → `approved.md`, set `Status: approved`
2. Add `related:` frontmatter — link to docs this spec will affect:
```yaml
---
related:
  features: docs/features/<name>.md        # if this adds/changes a feature
  use-cases: docs/use-cases/<name>.md      # if this changes user-facing behavior
  architecture: docs/architecture.md       # only if architecture changes
  adr: docs/adr/YYYY-MM-DD-<decision>.md  # only if a new decision is locked
---
```
Only include docs that exist or will be created in this delivery. Omit irrelevant fields.
3. Delete `working.md`
3. Update `.workflow/STATE.md`

**Light:**
```
phase: execute
active-spec: <slug>
track: light
next-action: Begin execute directly (skip task-breakdown)
```

**Standard/Heavy:**
```
phase: planning
active-spec: <slug>
track: <standard|heavy>
next-action: Run task-breakdown on approved.md
```

4. Announce:
```
[workflow:spec-formation] Locked → .workflow/specs/<slug>/approved.md
Gaps resolved: {N} | Deferred: {M}
Next: task-breakdown
```

---

## Memory

| File | Lifecycle |
|------|-----------|
| `idea.md` | Persistent — never delete |
| `working.md` | Temp — delete after `approved.md` created |
| `approved.md` | Permanent locked contract — change only via spec-amendment |
| `STATE.md` | Updated on every phase transition |

---

## Scale

| Track | Sections required | Clarification depth |
|-------|-------------------|---------------------|
| `light` | Goal + FRs + SC | 1–2 questions max |
| `standard` | + Scope + Stories + Entities + Edge Cases | Full triage, up to 5 questions |
| `heavy` | All sections | Full triage + NFR + Integration + 3 rounds |
