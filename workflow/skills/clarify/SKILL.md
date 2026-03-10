---
name: clarify
description: Resolve requirement gaps before spec-formation. Scan, ask, encode, report.
---

# Clarify

Turn ambiguous requirements into clear inputs for spec-formation.
Scan for gaps → ask targeted questions → encode answers → report coverage.

---

## Phase 1 — Scan

Before asking anything, scan the requirement against these categories.
Mark each: **Clear** / **Partial** / **Missing**.

| # | Category | What to check |
|---|----------|---------------|
| 1 | Functional scope | What it does, what's out of scope |
| 2 | Actors & roles | Who uses it, permission differences |
| 3 | Data & entities | Key objects, relationships, state transitions |
| 4 | Behavior & flows | Happy path, errors, edge cases |
| 5 | Non-functional | Performance, security, scale targets |
| 6 | Integration | External deps, APIs, failure modes |
| 7 | Definition of done | Acceptance criteria, measurable success |

As you scan, write `[NEEDS CLARIFICATION: <question>]` inline at the relevant spot in `working.md`.

**Triage questions:**
- Will this answer change implementation or acceptance criteria? → **Ask**
- Is this better resolved during spec-formation or planning? → **Defer**
- Is this a nice-to-know detail? → **Skip**

---

## Phase 2 — Ask

Present all independent questions in **one message**.
Sequential questions (answer B depends on answer A) must come in separate rounds.

**Per question format:**
```
**Q{N}: <question>**
> Recommended: **{option}** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
| C | ... |

Reply with A/B/C, "yes" to accept recommendation, or a short custom answer.
```

**Limits:**
- Max **5 questions** per session
- Stop early when all blocking gaps are resolved
- Respect "done" / "proceed" / "skip" signals

---

## Phase 3 — Encode

After each answer:
1. Remove the matching `[NEEDS CLARIFICATION]` from `working.md`
2. Update the relevant section with the clarified detail
3. Keep changes minimal and testable

---

## Phase 4 — Report

After all questions, output a coverage table:

```
[Clarify complete]

| Category | Status |
|----------|--------|
| Functional scope | ✅ Resolved |
| Actors & roles | ✅ Resolved |
| Data & entities | ⏩ Deferred → spec-formation |
| Behavior & flows | ✅ Resolved |
| Non-functional | ⚠️ Outstanding (low impact, safe to proceed) |
| Integration | ⏩ Deferred → planning |
| Definition of done | ✅ Resolved |

Next: spec-formation
```

Status key:
- ✅ Resolved — answered in this session
- ⏩ Deferred — better handled in next phase (note which phase)
- ⚠️ Outstanding — still unclear, flagged as low impact
- 🔴 Blocking — must resolve before proceeding

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | Skip scan. Ask 1–2 critical questions max. Brief report. |
| `standard` | Run full scan. Up to 5 questions. Full report. |
| `heavy` | Run full scan. Use all 5 slots. Explicitly flag all deferred/outstanding items. |
