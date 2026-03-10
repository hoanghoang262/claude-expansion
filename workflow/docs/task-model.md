# Task Model

A task is the unit of delivery — not the unit of thinking.

Tasks exist to hand work to an agent. They are created after the approved spec is clear, and they are scoped to be independently implementable and verifiable.

---

## What a Task Is Not

- A task is not a step in a coding sequence (too small)
- A task is not a feature (too large — a feature may need multiple tasks)
- A task is not a spec (spec comes before tasks)
- A task is not a note or a to-do item

---

## What a Good Task Contains

| Field | Purpose |
|---|---|
| Objective | What this task delivers in one or two sentences |
| Spec Reference | Which part of the approved spec this task fulfills |
| Scope Boundary | What is in and what is explicitly out |
| Verification Criteria | How to confirm the task is done correctly |
| Docs Impact | Which docs must be updated when this task is complete |
| Dependencies | Other tasks that must complete before this one can start (if any) |

A task that cannot be verified independently is not yet well-defined. Refine it before assigning it.

---

## Task Size

Tasks should be scoped to a **meaningful capability or behavior change** that can be:
- Implemented in one focused effort
- Tested and verified without external state from other in-progress tasks
- Reviewed as a coherent unit

**Too small:** "Add a null check to line 47" — this is an implementation detail, not a task.
**Too large:** "Implement the authentication system" — this likely needs to be broken into multiple tasks.
**Right size:** "Implement JWT token validation middleware with error handling" — scoped, verifiable, meaningful.

---

## Task Creation Rules

1. **Tasks come from approved spec only.** Do not create tasks from requirements, conversations, or working spec.
2. **Each task traces to a specific part of the spec.** If a task cannot be linked to a section of the approved spec, it should not exist.
3. **Tasks must be independently verifiable.** If verifying task B requires task A to be complete, then task B has a dependency on A — make that explicit.
4. **A task can spawn sub-tasks if complexity requires it,** but the parent task still owns the verification and the spec link.

---

## Task Lifecycle

```
Approved Spec
    |
    v
Task Breakdown  <-- AI decomposes spec into tasks
    |
    v
[READY]         <-- dependencies met, can be assigned
    |
    v
[IN PROGRESS]   <-- agent executing
    |
    v
[REVIEW]        <-- task-level review
    |
    v
[DONE]          <-- verified against spec, docs updated
```

A task is not DONE until:
- Implementation satisfies the verification criteria
- Relevant docs have been updated
- Task-level review has passed

---

## Parallel vs Sequential

Tasks with no dependencies should run in parallel. Tasks with dependencies must run sequentially in dependency order.

The orchestrator is responsible for understanding task dependencies and scheduling work accordingly. Agents do not need to know the full task graph — they receive their assigned task and execute it.
