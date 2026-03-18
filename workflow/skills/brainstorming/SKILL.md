---
name: brainstorming
description: |
  Use when: User has vague idea, needs to explore options, or needs help clarifying vision.
  NOT for: clear intent, simple tasks.
---

# Brainstorming

Explore and expand user's ideas. Help clarify vision through structured discussion.

## When to Use

- User says: "brainstorm", "suy nghĩ", "ý tưởng", "chưa biết làm gì"
- Vague intent: "make it better", "improve something"
- User stuck, needs options
- Orchestrator detects unclear direction → suggests brainstorm

## Process

### 1. Explore

Ask questions to understand:
- What problem are you solving?
- Who is this for?
- What does success look like?
- Any constraints?

### 2. Generate Options

Present 3-5 options:
- Option A: description + pros + cons
- Option B: description + pros + cons
- ...

### 3. Guide Decision

Help user pick direction:
- Ask which resonates
- Highlight trade-offs
- Don't force decision

### 4. Document

Save to `.workflow/brainstorm/<topic>.md`:

```markdown
# Brainstorm: <topic>

## Context
<what user shared>

## Options Explored
| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A | ... | ... | ... |

## Decision
<what user chose or deferred>
```

## Output

- Clear direction or
- List of options with trade-offs
- Next step identified

## Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Direction clear → spec | `spec-form.md` |
| Need more thinking | Stay in brainstorm |
| User wants to proceed | spec-form.md |
