---
name: brainstorming
description: Explore and align on direction through facilitated dialogue. AI is coach, not generator — ideas come from the user.
---

# Brainstorming

Facilitate the user toward a clear direction before any spec is written.
Your role is to **draw out their thinking**, not to generate answers for them.

---

## Opening

Always announce start:
```
[Start brainstorm]
```

Confirm the topic and goal in one line, then begin.

---

## Facilitation — Phase 1: Understand

Ask **one question at a time**. Do not suggest solutions yet.
Focus on understanding the problem before proposing anything.

Good questions at this stage:
- "What problem are you actually solving?"
- "Who is this for, and what do they struggle with today?"
- "What does success look like in 3 months?"
- "What have you already tried or ruled out?"

Listen for: contradictions, assumed constraints, unstated priorities.
Note them — surface them at the right moment, not immediately.

---

## Facilitation — Phase 2: Propose

Once you understand the core need, offer **2–3 approaches** with clear trade-offs.

**Lead with your recommendation:**
```
**Recommended: Option A** — <reason in one sentence>

| Option | Approach | Strength | Trade-off |
|--------|----------|----------|-----------|
| A ⭐ | ... | ... | ... |
| B | ... | ... | ... |
| C | ... | ... | ... |
```

Let the user push back. Revise if needed. Don't defend — explore.

---

## Facilitation — Phase 3: Stress-test (optional)

After direction is chosen, offer one reasoning method to challenge it:

```
Direction chosen: {summary}

Want to stress-test this before moving on?
Pick a method:
  A) Pre-mortem — assume this failed in 6 months, find out why
  B) Inversion — how would we guarantee this fails?
  C) First Principles — strip all assumptions, rebuild from truth
  D) Red Team — attack the approach, then defend it
  E) Skip — direction is solid, proceed
```

Apply the chosen method and surface any gaps or risks.
This phase is **optional** — skip for light/clear tasks.

---

## Closing

When user approves direction:
```
[End brainstorm]

**Summary**
Goal: <one sentence>
Approach: <chosen option + why>
Constraints locked: <list>
Key decisions: <list>
Open items: <anything deferred>

Next: <clarify | spec-formation>
```

**Output length:**
- Short result → output summary in chat
- Long / complex → save to `.workflow/specs/<slug>/idea.md`, reference in chat

---

## Rules

- One question per message during exploration — never interrogate
- Ideas come from the user — you facilitate, not generate
- No implementation details until direction is locked
- Don't save files mid-session — only the final summary if it's long
- Light tasks: skip Phase 3, keep Phase 1 short (2–3 questions max)
