---
name: spec-formation
description: Transform clear intent into an approved spec. Draft immediately, resolve gaps inline, lock on approval.
---

# Spec Formation

Own the full journey from intent to locked contract.
Draft first → mark gaps inline → triage and resolve → validate → approve → lock.

---

## Step 0 — Classify track

| Track | Signals |
|-------|---------|
| `light` | Single behavior, obvious scope, no data model, no integration |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale/compliance concerns |

State the track before proceeding. It controls which sections are required and how deep to go.

---

## Step 1 — Load context

1. `.workflow/specs/<slug>/idea.md` — brainstorm summary if exists
2. `.workflow/specs/<slug>/working.md` — previous draft if in progress
3. `.workflow/PROJECT.md` — project constraints, tech stack, key decisions

Note any PROJECT.md constraints that apply before writing.

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
In scope:
- ...
Out of scope:
- ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<plain language — who does what and why>
Acceptance scenarios:
- Given <state>, when <action>, then <outcome>
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>
- FR-002: Users MUST be able to <action>
[NEEDS CLARIFICATION: <question>]

## Key Entities          ← when data is involved
- <Entity>: <what it is, key attributes, relationships, state transitions>

## Non-Functional        ← heavy only, or when explicitly required
- Performance: <measurable target, e.g., p95 < 200ms>
- Security: <specific constraint>
- Scale: <volume/load assumption>
- Observability: <logging/metrics requirements>
- Compliance: <regulatory constraints if any>

## Interaction & UX      ← when UI is involved
- <critical user journey>
- Error states: <what user sees when X fails>
- Empty states: <what user sees with no data>

## Integration           ← when external systems involved
- <System>: <what we depend on, failure mode>

## Edge Cases & Errors   ← standard/heavy only
- What happens when <boundary condition>?
- How does system handle <failure scenario>?

## Success Criteria
- SC-001: <measurable outcome — no adjectives without numbers>
- SC-002: <measurable outcome>

## Open Items
- <item deferred to planning or implementation — note which phase>
```

**FR writing rule — WHAT not HOW:**
- ✅ `System MUST notify users when payment fails`
- ❌ `System MUST send Stripe webhook on payment failure`
- ✅ `Users MUST be able to recover access without contacting support`
- ❌ `Implement password reset via email token with 1hr expiry`

---

## Step 3 — Triage gaps

Collect all `[NEEDS CLARIFICATION]` markers. For each, decide:

| Decision | Criteria |
|----------|----------|
| **Ask now** | Answer would change FR, SC, entity shape, or scope boundary |
| **Defer to Open Items** | Better answered during planning (tech choices) or implementation (edge cases) |
| **Assume + note** | Low stakes, reasonable default exists — state assumption inline |

**Priority formula:** ask what has high impact on architecture, data modeling, test design, or acceptance criteria first.

---

## Step 4 — Ask

Group all independent questions into **one message per round**.
Dependent questions (B needs A's answer) come in separate rounds. Max **5 questions** per session.

**Format per question:**
```
**Q{N}: <question>**
> Recommended: **{option}** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
| C | ... |

Reply A/B/C, "yes" to accept recommendation, or a short custom answer.
```

After each answer:
1. Replace `[NEEDS CLARIFICATION]` with the clarified detail
2. Update the affected section
3. Log the resolution in `## Clarifications`:

```markdown
## Clarifications

### Session YYYY-MM-DD
- Q: <question> → A: <answer> — applied to: <section name>
```

If a clarification invalidates an earlier statement, replace it. Never duplicate.

After all questions encoded, **do one more gap scan** — new answers sometimes reveal new gaps.
If new gaps found: one more round (max 3 total). If still gaps after 3 rounds: move remaining to Open Items.

---

## Step 5 — Self-validate

Before presenting for approval:

```
[ ] Track stated
[ ] No [NEEDS CLARIFICATION] remain (or moved to Open Items with rationale)
[ ] Every FR: MUST + testable behavior, no HOW details, no vague verbs
[ ] Every SC: measurable — numbers, not adjectives ("fast" → "p95 < 500ms")
[ ] Scope: both in-scope AND out-of-scope stated explicitly
[ ] User stories have Given/When/Then (standard/heavy)
[ ] NFR and UX sections present if track requires
[ ] PROJECT.md constraints respected
[ ] Light track: fits on one screen
```

---

## Step 6 — Present & approve

**Light track** — show a compact summary, not the full spec:
```
**Spec: <slug>** (light)
Goal: <one sentence>
Will do: <2-3 bullet FRs>
Won't do: <scope boundary>
Done when: <SC-001>

Looks right? Reply "yes", "ok", or just give me the next task to proceed.
```
Implicit approval: any affirmative reply or a follow-on task message counts.

**Standard/Heavy track** — show the full spec:
```
Here's the spec for review.
Clarifications resolved: {N}. Deferred to Open Items: {list}.

Approve to lock, or tell me what to change.
```
Requires explicit approval. Revise until approved. Never lock without it.

---

## Step 7 — Lock

On approval:
1. Copy `working.md` → `approved.md`, set `Status: approved`
2. Delete `working.md`
3. Update `.workflow/STATE.md`:

```
phase: planning
active-spec: <slug>
track: <track>
next-action: Run task-breakdown on approved.md
blocked-by: none
last-updated: YYYY-MM-DD
```

4. Announce:
```
[Spec locked] .workflow/specs/<slug>/approved.md
Clarifications: {N} resolved, {M} deferred to Open Items
Next: task-breakdown
```

---

## Memory rule

| File | Lifecycle |
|------|-----------|
| `idea.md` | Persistent — never delete |
| `working.md` | Temporary — delete after `approved.md` created |
| `approved.md` | Permanent locked contract — change only via `spec-amendment` |
| `STATE.md` | Updated on every phase transition |

---

## Scale

| Track | Required sections | Clarification depth |
|-------|-------------------|---------------------|
| `light` | Goal + FRs + SC | 1–2 questions max, skip taxonomy |
| `standard` | + Scope + Stories + Entities + Edge Cases | Full triage, up to 5 questions |
| `heavy` | All sections | Full triage + NFR + Integration + 3 rounds if needed |

**Never pad a light spec to look like a heavy one.**
