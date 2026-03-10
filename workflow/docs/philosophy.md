# Core Philosophy

## What This System Is

This is a coordination framework for AI-assisted software development. It transforms working with AI from an unpredictable, hard-to-steer process into one that is reliable, explainable, and sustainable.

The system does not treat AI as a command-execution tool. It treats AI as an active delivery force — one that is given high autonomy in execution, but is held to strict standards around understanding intent, honoring strategic decisions, and maintaining a trustworthy record of the project.

The goal is not just to build software faster. It is to build software with AI in a way that is trustworthy, scalable, and does not trade away clarity of thinking.

---

## The Root Problem

The system was designed to address a specific failure pattern:

**AI acts too early, before it understands enough.**

This produces:
- Misaligned output that must be corrected repeatedly
- Requirement drift as AI fills gaps with its own interpretation
- Unpredictable results that undermine trust
- Docs that lag behind or disappear
- Project knowledge that fragments and degrades over time

The root cause is ambiguity, combined with insufficient control at the understanding phase and weak synchronization between intent, code, and docs.

---

## Core Beliefs

### 1. AI must not start with code

The biggest failure point is not slow code generation — it is premature code generation. A requirement that has not been properly understood is not a valid input to execution. The system enforces clarification before any delivery begins.

### 2. Spec is the axis between intent and software

Requirements are initial wishes. Code is the final artifact. What connects them reliably is spec.

Spec is not just a description of what to build. It locks the semantics of the goal, defines scope, captures constraints, establishes the definition of done, and records the design decisions that AI needs to execute without re-guessing the user's intent.

Everything else — tasks, code, tests, review, docs — orbits the spec.

### 3. The process must adapt to the weight of the task

A typo fix and an architecture change cannot go through the same process. A dangerous bug and a small refactor should not carry the same ceremony overhead.

The framework adapts: the higher the impact, the longer the horizon, or the deeper into the system a change reaches, the more rigorous the process. Small, clear, low-risk work moves fast and light.

### 4. AI must be proactive once direction is clear

Once intent has been clarified and key decisions have been locked, AI should not wait for step-by-step instructions. It must decompose work, implement, test, review, propose improvements, and drive delivery forward autonomously.

Proactive AI is a necessary condition for real-world efficiency. But that autonomy is only valid when paired with spec adherence, traceability, and respect for strategic checkpoints.

### 5. Users own direction; AI owns execution

Users do not need to micromanage implementation. Their role is to provide the initial goal, participate in the early clarity phase, and approve decisions with long-term consequences.

Users own: intent, goals, strategic decisions, and long-horizon direction.
AI owns: analysis, spec formation, task breakdown, implementation, testing, review, doc sync, and delivery operations.

### 6. Docs are the project's living memory

Code alone cannot carry the knowledge of a system. Architecture, use cases, feature maps, decision reasoning, constraints, current state, and the overall mental model of the project must live in docs.

Docs are not a polish step added after the fact. They are the central source of truth. They must be continuously updated to reflect the real system.

### 7. Not all generated content deserves permanence

AI needs space to think — to draft, explore options, sketch ideas, and leave working notes. But not everything produced in a session has lasting value.

The system maintains a clear distinction between:
- **Persistent knowledge** — what gets written into long-term docs
- **Temporary workspace** — what serves a session and is discarded after

Content only moves into permanent docs when it has long-term value, affects how the system is understood, or represents a decision that needs to be traceable.

### 8. Tasks are units of delivery, not units of thought

Work is not broken into tasks directly from requirements. Tasks appear only after the approved spec is sufficiently clear. A task represents a meaningful, independently verifiable unit of delivery — not a micro step in a code sequence.

### 9. Review is multi-layered

Review is not a single gate at the end. It is structured across three levels: per-task, per-group, and final integration. Each level checks for different things and catches different categories of issues.

### 10. Done means aligned

A change is complete only when code matches spec, docs reflect what was built, and necessary review has passed. Partial delivery — code without doc sync, or implementation without review — does not count as done.
