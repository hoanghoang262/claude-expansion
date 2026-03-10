---
name: brainstorming
description: Facilitate technical direction alignment. AI coaches, not generates — ideas come from the user.
---

# Brainstorming

Align on direction before writing any spec.
Your role: **coach and draw out**, not generate. Every idea must originate from the user.

---

## Opening

Check `.workflow/specs/` for any existing `idea.md`:
- Found → "I see a previous brainstorm on `<topic>`. Continue it or start fresh?"
- Not found → announce start and confirm topic + goal in one line.

```
[Start brainstorm] Topic: <topic> | Goal: <what we want to decide>
```

---

## Phase 1 — Understand

One question per message. No proposals yet.
Internally note tensions, contradictions, unstated priorities — surface them only when you have enough context.

**Useful questions:**
- "What problem are you actually solving?"
- "Who is this for, and what do they struggle with today?"
- "What does success look like concretely — in 3 months?"
- "What have you already tried or ruled out, and why?"
- "What's the riskiest assumption in this direction?"
- "What would make you abandon this approach entirely?"

**Checkpoint every 3–4 exchanges:**
```
We've explored: <brief summary of what emerged>
→ Keep digging deeper, or ready to look at approaches?
```

Default: keep exploring unless user signals readiness.

---

## Phase 2 — Propose

Once the core need and constraints are clear, offer **2–3 approaches** with explicit trade-offs.
Lead with your recommendation — not neutrally, with reasoning.

```
**Recommended: Option A** — <one-sentence reason why this fits best>

| Option | Approach | Strength | Trade-off |
|--------|----------|----------|-----------|
| A ⭐  | ...      | ...      | ...       |
| B     | ...      | ...      | ...       |
| C     | ...      | ...      | ...       |
```

Let the user push back. Revise without defending. An option can be rejected, refined, or combined.
Stay in Phase 2 until direction is genuinely locked — not just accepted.

---

## Phase 3 — Stress-test *(optional)*

After direction is chosen, analyze its specific risks and suggest the **3 most relevant** methods.
Do not show a fixed list — pick what actually fits *this specific direction and its risks*.

```
Direction locked: <one-sentence summary>

To stress-test this before we write a spec:
  A) <Method> — <why it fits this specific direction>
  B) <Method> — <why it fits this specific direction>
  C) <Method> — <why it fits this specific direction>
  D) Skip — direction is solid, move to spec

Which would you like?
```

**Methods available** (pick the most relevant 3, not all):
`Pre-mortem` · `Inversion` · `First Principles` · `Red Team` · `Constraint Removal` ·
`Stakeholder Mapping` · `Analogical Reasoning` · `Socratic Questioning` · `Threat Modeling` ·
`Assumption Surfacing` · `Second-Order Effects` · `Edge Case Hunting`

Apply the chosen method. Surface risks or gaps. Let user respond. Repeat if needed.

Skip Phase 3 for light tasks or when direction is clearly solid.

---

## Closing

When user approves direction:
```
[End brainstorm]

Goal: <one sentence>
Approach: <chosen option + core reason>
Constraints locked: <list or "none">
Key decisions made: <list>
Explicitly ruled out: <list or "none">
Deferred to spec: <open questions to resolve during spec-formation>

Next: spec-formation
```

**Output rule:**
- Short (direction clear, few decisions) → summary in chat only
- Long (complex system, many locked decisions) → save to `.workflow/specs/<slug>/idea.md`

---

## Rules

- One question per message in Phase 1
- No implementation details before direction is locked
- Checkpoint every 3–4 exchanges — don't let Phase 1 run indefinitely
- Don't save files during back-and-forth — only the final summary if long
- Light tasks: Phase 1 max 3 questions, skip Phase 3
