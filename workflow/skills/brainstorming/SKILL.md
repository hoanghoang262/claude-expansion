---
name: workflow:brainstorming
description: Use when the goal itself is vague or inconsistent — explore and align on direction before clarifying details
---

# Brainstorming

Explore and align on direction through Socratic dialogue.
Used when the goal is unclear, not just the details.

## When to Trigger

**Triggered by:**
- User runs `/brainstorm` explicitly
- Orchestrator detects inconsistency or uncertainty during clarify
- User says they don't know what they want yet

**Do NOT use when:**
- Goal is clear, only details need resolving → use `workflow:clarify`
- Already brainstormed and user approved direction → move on

---

## Process

### Start

Always announce:
```
[Start brainstorm]
```

### During

- Ask one question at a time — Socratic, not interrogation
- Understand the problem before proposing solutions
- Once you understand the core need, propose **2–3 approaches** with trade-offs
- Lead with your recommendation and reasoning
- Let user push back, refine, or choose

### End

When user approves a direction, announce:
```
[End brainstorm]
```

Then output a summary (see Output section below).

---

## Output

**Short result (fits in chat):** Output summary directly in chat.

**Long result (complex system, many decisions):** Save to `.workflow/specs/<slug>/idea.md` and reference it.

### Summary format

```
**Brainstorm Summary**

**Goal:** <one sentence>
**Approach chosen:** <name> — <why>
**Key constraints:** <list>
**Decisions locked:** <list>
**Open questions:** <anything deferred>

Next: <clarify | spec-formation>
```

---

## Rules

- Stay in exploration mode until direction is clear — don't jump to implementation
- One question per message during exploration
- Proposals come only after you understand the problem
- Summary must be concise — capture decisions, not the conversation
- Don't save files during the back-and-forth — only at the end if summary is long
