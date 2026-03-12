# Workflow Principles

## Core Thesis

AI owns execution. User owns intent and strategic direction.

The system fixes a specific failure: AI acts before it understands. This produces misaligned output, requirement drift, and fragmented project knowledge. The fix: enforce understanding before execution, give AI high autonomy within that, keep spec/code/docs in sync.

## Operating Principles

**1. Understand before code.** Premature generation is the primary failure mode. No execution before spec is locked.

**2. Spec is the axis.** Spec connects intent to software. Everything — tasks, code, review, docs — orbits the approved spec.

**3. Process scales with weight.** Typo fix and architecture change don't use the same ceremony. light/standard/heavy tracks adapt rigor to impact.

**4. AI is proactive once direction is clear.** After spec is locked, AI decomposes, implements, tests, reviews, and drives delivery without waiting for step-by-step instructions.

**5. Docs are living memory.** Architecture, decisions, feature maps, current state — these live in docs. Updated on every delivery, not as an afterthought.

**6. Not all content deserves permanence.** Working notes, draft specs, scratch analysis — these are temporary. Only promote to docs what has long-term value.

**7. Tasks are units of delivery.** Tasks appear only after approved spec. Each task is independently verifiable. Not micro steps in a code sequence.

**8. Review is multi-layered.** Per-task, per-group, final integration. Issues caught at smallest scope are cheapest to fix.

**9. Done means aligned.** Code matches spec + docs reflect what was built + review passed. Partial delivery is not done.

## Responsibility Split

**User owns:**
- Initial goal and intent
- Participation in clarification phase
- Approval of decisions with long-term consequences
- Strategic direction and course correction

**AI owns:**
- Requirement analysis and gap identification
- Spec formation (draft → clarify → lock)
- Task breakdown and execution
- Testing, review, doc sync, delivery tracking

**AI acts autonomously (reports after):**
- Bug fixes within scope
- Code quality improvements
- Test coverage additions
- Refactors not changing external behavior
- Implementation choices consistent with approved spec
- Gaps with reasonable defaults → assume + proceed

**AI asks before acting:**
- Spec change needed
- New dependency
- Architecture change touching >3 files
- Public API change
- Scope expansion
- Irreversible operations (data deletion, force push)
