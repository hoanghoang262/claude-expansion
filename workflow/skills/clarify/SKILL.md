---
name: clarify
description: Resolve ambiguity in requirements before spec-formation. Scan for gaps, ask targeted questions, encode answers into working.md.
---

# Clarify

Identify and resolve the gaps that would block writing a solid spec.
Questions must be targeted, minimal, and immediately encoded back into the working spec.

---

## Step 1 — Scan for gaps

Before asking anything, scan the requirement against these categories.
For each, mark: **Clear** / **Partial** / **Missing**.

| Category | Examples |
|---|---|
| Functional scope | What it does, what's explicitly out of scope |
| Actors & roles | Who uses it, permission differences |
| Data & entities | Key objects, relationships, lifecycle |
| Behavior & flows | Happy path, error states, edge cases |
| Non-functional | Performance, security, scale constraints |
| Integration | External deps, APIs, failure modes |
| Definition of done | Acceptance criteria, measurable success |

Mark gaps with `[NEEDS CLARIFICATION: <question>]` inline in `working.md` as you scan.
Only ask about **Partial** or **Missing** categories that would change implementation.

---

## Step 2 — Ask

**Rules:**
- Max **5 questions** per clarify session
- Group all independent questions into **one message** per round
- For each question: lead with a **recommendation** + options table, not open-ended
- If a question depends on the answer to another, ask sequentially

**Format per question:**

```
**Q{N}: <question>**
Recommended: **{option}** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |
| C | ... |

Reply with A/B/C or "yes" to accept the recommendation.
```

**Stop early if:**
- All blocking gaps resolved (remaining questions become unnecessary)
- User says "done" / "proceed" / "good enough"
- 5 questions reached

---

## Step 3 — Encode

After each accepted answer:
1. Remove or replace the matching `[NEEDS CLARIFICATION]` marker in `working.md`
2. Update the relevant section with the clarified detail (requirement, constraint, entity, etc.)
3. Keep changes minimal and testable — no narrative drift

After all questions:
```
[Clarify complete] — {N} gaps resolved. Moving to spec-formation.
```

If inconsistency found mid-session (user answers reveal conflicting goals):
```
[Clarify] Your answers suggest the goal itself may need alignment.
Recommend running brainstorming to lock direction first.
```

---

## Flexibility

**Light tasks** (simple, few gaps): Ask 1–2 questions max, skip taxonomy scan, resolve inline.

**Heavy tasks** (complex, many unknowns): Run full taxonomy scan, use all 5 question slots, be explicit about deferred items.
