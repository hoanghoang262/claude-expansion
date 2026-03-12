---
name: spec/amendment
description: The only way to change a locked spec. Requires explicit user approval. Edit directly, git is the audit trail.
---

# Spec Amendment

```
[workflow:spec-amendment] Amendment requested
```

Never change `spec.md` without this process. Never self-approve.

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

Section: <which section>
Current: <exact current text>
Proposed: <new text>
Reason: <discovery | user request | new constraint>

Blast radius:
  FRs affected: <list or none>
  SCs affected: <list or none>
  Tasks affected: <list or none>
  Assumptions invalidated: <list or none>
```

### Step 2 — Get approval

```
Approve to apply, or reject to proceed with current spec.
```

"Ok" or "yes" = approved. Do not proceed until explicit approval.

### Step 3 — Apply

1. Edit `docs/specs/<slug>/spec.md` directly — update the relevant section
2. Reassess tasks — update or add tasks as needed, flag completed tasks now wrong
3. Commit:
```
spec(<slug>): amend <section> — <what changed>

<one sentence why: discovery / user request / new constraint>
Blast radius: <FRs/SCs/tasks affected or "none">
```

4. Announce:
```
[workflow:spec-amendment] Applied
Tasks affected: <list or none>
Resuming: <next action>
```

---

## Hard rules

- One amendment at a time
- If amendment invalidates completed work → surface explicitly before proceeding
- Git diff is the amendment record — no need to log inside the file
