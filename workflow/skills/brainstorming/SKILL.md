---
name: brainstorming
description: Align on direction before writing spec. AI coaches and draws out — ideas come from the user.
---

# Brainstorming


---

## On Entry

```
[workflow:brainstorming] Starting — Topic: <topic>
```

Proceed to Phase 1 immediately.

---

## Phase 1 — Understand

Goal: draw out the user's real problem, constraints, and mental model. No proposals yet.

**Questioning style:**
- Prioritize open questions — let user describe freely rather than answer yes/no
- Group related questions together (2–4 per message) — avoid one-at-a-time drip
- Skip trivial or obvious questions — ask only what genuinely changes understanding
- If research would expand the picture, do it inline and share findings as input to discussion
- Surface counter-arguments and opposing views with specific evidence — expand options, don't narrow them

Useful probes:
- "What problem are you actually solving — and for whom?"
- "What does success look like concretely in 3 months?"
- "What have you already tried or ruled out, and why?"
- "What's the riskiest assumption here?"
- "What would make you abandon this direction entirely?"

Checkpoint when enough context is gathered:
```
Explored so far: <brief summary>
→ Keep digging, or ready to look at approaches?
```

Default: keep exploring unless user signals readiness.

---

## Phase 2 — Propose

Once core need and constraints are clear, offer **2–3 approaches** with trade-offs.
Lead with recommendation — not neutrally, with reasoning.

```
**Recommended: Option A** — <one-sentence reason>

| Option | Approach | Strength | Trade-off |
|--------|----------|----------|-----------|
| A ⭐  | ...      | ...      | ...       |
| B     | ...      | ...      | ...       |
| C     | ...      | ...      | ...       |
```

Let user push back. Revise without defending.
Stay in Phase 2 until direction is genuinely locked — not just accepted.

---

## Phase 3 — Stress-test *(optional)*

After direction is chosen, pick **3 most relevant** methods for this specific direction:

```
Direction locked: <one-sentence summary>

Stress-test options:
  A) <Method> — <why it fits this direction>
  B) <Method> — <why it fits this direction>
  C) <Method> — <why it fits this direction>
  D) Skip — direction is solid

Which?
```

Available: `Pre-mortem` · `Inversion` · `Red Team` · `Assumption Surfacing` · `Threat Modeling` · `Second-Order Effects` · `Edge Case Hunting` · `First Principles`

Skip Phase 3 for light tasks or clearly solid directions.

---

## Closing

When user approves direction:

```
[workflow:brainstorming] Complete

Goal: <one sentence>
Approach: <chosen option + core reason>
Constraints locked: <list or "none">
Key decisions: <list>
Ruled out: <list or "none">
Deferred to spec: <open questions>

Next: spec-formation
```

Brainstorm summary lives in conversation only — no files needed.

---

## Rules

- No implementation details before direction is locked
- Counter-arguments must have specific evidence, not just "some people think X"
- No trivial questions — every question must change understanding if answered differently
- No implementation details before direction is locked
- Phase 3 optional — skip if direction is clearly solid
