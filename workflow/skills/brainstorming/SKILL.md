---
name: brainstorming
description: Facilitate direction alignment through dialogue. AI draws out user thinking — ideas come from the user, not the AI.
---

# Brainstorming

Align on direction before writing any spec.
Your role: **facilitate**, not generate. Every idea must come from the user.

---

## Opening

```
[Start brainstorm]
```

State the topic and goal in one line. Begin Phase 1.

---

## Phase 1 — Understand

One question per message. No proposals yet.
Listen for: contradictions, assumed constraints, unstated priorities.

Useful questions:
- "What problem are you actually solving?"
- "Who is this for, and what do they struggle with today?"
- "What does success look like concretely?"
- "What have you ruled out, and why?"
- "What's the riskiest assumption here?"

Note tensions and contradictions silently. Surface them when you have enough context.

---

## Phase 2 — Propose

Once the core need is clear, offer **2–3 approaches** with trade-offs.

```
**Recommended: Option A** — <reason in one sentence>

| Option | Approach | Strength | Trade-off |
|--------|----------|----------|-----------|
| A ⭐ | ... | ... | ... |
| B    | ... | ... | ... |
| C    | ... | ... | ... |
```

Let the user push back. Revise without defending. Keep exploring until direction is locked.

---

## Phase 3 — Stress-test *(optional, skip for light tasks)*

After direction is chosen, analyze the specific content and suggest the **3 most relevant** reasoning methods for it.
Do not show a fixed menu — pick what actually fits this direction and its risks.

```
Direction: <summary>

Suggested stress-tests for this specific case:
  A) <Method name> — <why it fits this direction>
  B) <Method name> — <why it fits this direction>
  C) <Method name> — <why it fits this direction>
  D) Skip — direction is solid

Which would you like to run?
```

Available methods (choose the most relevant, not all):
Pre-mortem, Inversion, First Principles, Red Team, Constraint Removal,
Stakeholder Mapping, Analogical Reasoning, Socratic Questioning, Threat Modeling,
Assumption Surfacing, Edge Case Hunting, Second-Order Effects.

Apply the chosen method, surface gaps or risks, let user respond.

---

## Closing

```
[End brainstorm]

**Summary**
Goal: <one sentence>
Approach: <chosen option + why>
Constraints locked: <list or "none">
Key decisions: <list>
Deferred: <anything explicitly set aside>

Next: <clarify | spec-formation>
```

**Output rule:** Short summary → chat only. Long or complex → save to `.workflow/specs/<slug>/idea.md`.

---

## Rules

- One question per message during Phase 1
- No implementation details before direction is locked
- Do not save files mid-session — final summary only
- Light tasks: Phase 1 = 2–3 questions max, skip Phase 3
