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

---

## Step 1 — Load context

1. `docs/PROJECT.md` — constraints, tech stack, key decisions
2. `docs/specs/<slug>/spec.md` — previous draft if exists
3. `.workflow/brainstorm/` — latest brainstorm file if relevant

If brainstorm session just completed → distill key decisions into spec, discard rough notes.

---

## PHASE 1: CLARIFY

```
[workflow:spec] Clarifying: <slug>
```

### Draft immediately

Create `docs/specs/<slug>/spec.md` with Status: draft. Do not ask questions before drafting.

**If prompt is unclear:** Draft with best interpretation, mark as assumption.
**Only exception:** Prompt so vague no FR can be written → ask 1 minimum question.

Mark missing information inline: `[GAP: <specific question>]`

### Spec format

```markdown
---
status: draft
track: <light|standard|heavy>
created: YYYY-MM-DD
related: {}
---

# Spec: <slug>

## Goal
One sentence. What this builds and why.

## Scope
In scope: ...
Out of scope: ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<who does what and why>
Acceptance:
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>
[GAP: <question>]

## Key Entities          ← when data is involved
- <Entity>: <attributes, relationships>

## Assumptions
- A-001: <assumed true> — if wrong, impacts: FR-N

## Non-Functional        ← heavy only
- Performance: <measurable target>
- Security: <specific constraint>

## Integration           ← when external systems involved
- <System>: <what we depend on, failure mode>

## Edge Cases            ← standard/heavy only
- What happens when <boundary condition>?

## Success Criteria
- SC-001 (covers FR-001): <measurable outcome>

## Open Items
- <deferred to planning/implementation>
```

**FR rule — WHAT not HOW:**
- ✅ `System MUST notify users when payment fails`
- ❌ `System MUST send Stripe webhook on payment failure`

### Triage gaps

| Decision | When |
|----------|------|
| **Ask now** | Answer changes FR, SC, entity shape, or scope boundary |
| **Defer to Open Items** | Tech choices, implementation edge cases |
| **Assume + note** | Low stakes, reasonable default exists |

Group independent questions. Max 5 per session. Format:

```
**Q1: <question>**
> Recommended: **<option>** — <reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
```

After answers: replace `[GAP]` inline. Max 3 rounds; remaining gaps → Open Items.

---

## PHASE 2: LOCK

```
[workflow:spec] Locking: <slug>
```

### Self-validate

```
[ ] Track stated
[ ] No [GAP] remain (or moved to Open Items)
[ ] Every FR: MUST + testable, no HOW
[ ] Every SC: measurable — numbers not adjectives
[ ] Every FR maps to at least one SC
[ ] Scope: in AND out explicit
[ ] Stories have Given/When/Then (standard/heavy)
[ ] PROJECT.md constraints respected
```

### Present for approval

**Light:**
```
**Spec: <slug>** (light)
Goal: <one sentence>
Will do: <2-3 bullet FRs>
Won't do: <scope boundary>
Done when: <SC-001>

Looks right? Reply "yes" or give me the next task.
```
Any affirmative reply = approved.

**Standard/Heavy:**
```
Spec ready. Resolved: {N} gaps. Deferred: {list}.
Approve to lock, or tell me what to change.
```
Requires explicit approval.

### Lock

On approval:
1. Set `status: approved` in frontmatter
2. Add `related:` — link to docs this spec will affect:

```yaml
related:
  feature: docs/features/<name>.md        # if adds/changes a feature
  use-cases: docs/use-cases/<name>.md     # if changes user-facing behavior
  adr: docs/adr/YYYY-MM-DD-<decision>.md  # only if architectural decision locked
```

Only include docs that exist or will be created. Omit irrelevant fields.

3. Announce:
```
[workflow:spec] Locked → docs/specs/<slug>/spec.md
Track: <track> | Gaps resolved: {N} | Deferred: {M}
```

---

## Scale

| Track | Sections required | Depth |
|-------|-------------------|-------|
| `light` | Goal + FRs + SC | 1–2 questions max |
| `standard` | + Scope + Stories + Entities + Edge Cases | Full triage, up to 5 questions |
| `heavy` | All sections | Full triage + NFR + Integration + 3 rounds |
