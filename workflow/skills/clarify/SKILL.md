---
name: workflow:clarify
description: Use when user submits a requirement that is unclear, ambiguous, or missing critical details — resolve before moving to spec-formation
---

# Clarify

Resolve ambiguity in user requirements through focused, efficient questioning.
One round of questions per message. Multiple independent questions can be asked
together in a single round. Prefer options over open-ended questions.

## When to Trigger

**Auto-triggered by orchestrator when:**
- Intent is present but details are missing (what, how, scope unclear)
- Multiple valid interpretations exist
- Constraints or success criteria are undefined

**Do NOT trigger when:**
- Requirements are clear enough to write a spec directly
- User just answered clarify questions (move to spec-formation)
- Task is `light` track (fix obvious, no ambiguity possible)

**Suggest brainstorming when (mid-clarify):**
- User's answers reveal internal inconsistencies
- The goal itself seems uncertain or conflicted
- User says "I'm not sure what I want"

---

## Format

Group all independent questions into **one message per round**.
Use a numbered list. For each question, offer labeled options when possible.

```
[Clarify] Tôi cần làm rõ một số điểm:

1. <Question needing options>
   a) <option>  b) <option>  c) <option>

2. <Question needing options>
   a) <option>  b) <option>

3. <Open-ended question when options can't capture it>
```

After user responds, either:
- Ask the next round if new gaps appeared from their answers
- Proceed to `workflow:spec-formation` when all critical gaps are resolved

---

## Rules

- **One round per message** — never split a single round across multiple messages
- **Options first** — if the answer space is bounded, list options
- **Only critical questions** — skip nice-to-know, ask what blocks spec-writing
- **Max 2 rounds** — if still unclear after 2 rounds, suggest `workflow:brainstorming`
- **Never re-ask** — don't repeat questions the user already answered

---

## Transition

After clarify resolves all gaps:

```
[Clarify complete] Requirements are clear. Moving to spec-formation.
```

If inconsistency detected mid-clarify:

```
[Clarify] Your answers suggest the goal itself may need more exploration.
Would you like to run a brainstorm session to align on direction first?
```
