---
name: spec-amendment
description: Change an approved spec. Requires explicit user approval. Guards against silent scope creep.
---

# Spec Amendment

The only way to change a locked spec.
Never edit `approved.md` directly. Never proceed without user approval.

---

## When to invoke

- Implementation reveals a requirement is wrong or missing
- User explicitly asks to change the spec
- A dependency or constraint was discovered that invalidates part of the spec

Do NOT invoke for:
- Implementation details (those are AI's domain)
- Minor wording clarifications that don't change behavior
- Adding tests or improving code quality

---

## Process

### Step 1 — State the change

Present clearly:
```
[Spec Amendment Request]

What needs to change: <specific section and current text>
Proposed change: <new text>
Reason: <why — discovery, user request, constraint>
Blast radius:
  - FRs affected: <list or "none">
  - SCs affected: <list or "none">
  - Tasks affected: <list or "none">
  - Entities changed: <list or "none">
  - Assumptions invalidated: <list or "none">
  - Integrations impacted: <list or "none">
```

### Step 2 — Get approval

```
Approve this amendment to continue, or reject to proceed with the current spec.
```

Do not proceed until explicit approval. "Ok" or "yes" counts as approval.

### Step 3 — Apply

On approval:
1. Edit `approved.md` — update the relevant section
2. Add an amendment record at the bottom:

```markdown
---
## Amendments

### Amendment 1 — YYYY-MM-DD
**Changed:** <section>
**From:** <original text>
**To:** <new text>
**Reason:** <why>
**Approved by user:** yes
```

3. Assess impact on `tasks.md`:
   - Affected tasks → update or add tasks
   - Completed tasks that are now wrong → flag for re-implementation

4. Update STATE.md:
```
next-action: Resume execute with amended spec
```

5. Announce:
```
[Spec amended] approved.md updated.
Tasks affected: <list or "none">
Resuming: <next action>
```

---

## Hard rules

- Never edit `approved.md` without going through this process
- Never self-approve — user must confirm
- One amendment at a time — if multiple changes needed, handle sequentially
- If amendment invalidates completed work, surface that explicitly before proceeding
