---
name: brainstorming
description: Optional branch for strategic ambiguity. Use when user doesn't know which direction to take — not for requirement gaps.
---

# Brainstorming

**Trigger:** Strategic ambiguity only — user unsure which direction, not just missing details.
**Not triggered:** User knows what they want but lacks specifics → use spec-formation directly.

---

## On Entry

```
[workflow:brainstorming] Starting — Topic: <topic>
```

Check `.workflow/specs/` for existing `idea.md`:
- Found → "Previous brainstorm on `<topic>` exists. Continue or start fresh?"
- Not found → proceed to Phase 1

---

## Phase 1 — Understand

One question per message. No proposals yet.
Note tensions, contradictions, unstated priorities — surface only when you have enough context.

Useful probes:
- "What problem are you actually solving?"
- "What does success look like in 3 months — concretely?"
- "What have you already tried or ruled out, and why?"
- "What's the riskiest assumption in this direction?"
- "What would make you abandon this approach entirely?"

Checkpoint every 3–4 exchanges:
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

Save to `.workflow/specs/<slug>/idea.md` only if session was long or decisions are complex.

---

## Rules

- One question per message in Phase 1
- No implementation details before direction is locked
- Checkpoint every 3–4 exchanges
- Light tasks: max 3 questions in Phase 1, skip Phase 3
