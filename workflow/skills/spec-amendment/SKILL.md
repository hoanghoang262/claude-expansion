---
name: spec-amendment
description: The only way to change a locked spec. Requires explicit user approval.
---

# Spec Amendment

```
[workflow:spec-amendment] Amendment requested
```

Never edit `approved.md` directly. Never proceed without user approval.

---

## When to invoke

- Implementation reveals requirement is wrong or missing
- User explicitly asks to change spec
- New constraint invalidates part of spec

**Not for:** implementation details, minor wording that doesn't change behavior, adding tests.

---

## Process

### Step 1 — State the change

```
[Spec Amendment Request]

Change: <specific section + current text>
Proposed: <new text>
Reason: <discovery | user request | new constraint>
Blast radius:
  FRs affected: <list or "none">
  SCs affected: <list or "none">
  Tasks affected: <list or "none">
  Entities changed: <list or "none">
  Assumptions invalidated: <list or "none">
```

### Step 2 — Get approval

```
Approve to continue, or reject to proceed with current spec.
```

"Ok" or "yes" counts as approval. Do not proceed until explicit approval.

### Step 3 — Apply

1. Edit `approved.md` — update relevant section
2. Add amendment record at bottom:

```markdown
## Amendments

### Amendment {N} — YYYY-MM-DD
**Changed:** <section>
**From:** <original>
**To:** <new>
**Reason:** <why>
**Approved:** yes
```

3. Assess `tasks.md` impact — update or add tasks. Flag completed tasks now wrong.
4. Update STATE.md: `next-action: Resume execute with amended spec`
5. Announce:

```
[workflow:spec-amendment] approved.md updated
Tasks affected: <list or "none">
Resuming: <next action>
```

---

## Hard rules

- Never edit `approved.md` without this process
- Never self-approve
- One amendment at a time
- If amendment invalidates completed work → surface explicitly before proceeding
