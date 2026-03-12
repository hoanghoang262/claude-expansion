# Workflow Plugin Smart Autonomy — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rebuild all workflow skills to maximize AI autonomy — plan before acting, surface only irreversible/strategic decisions, make AI state visible at all times.

**Architecture:** Rewrite 7 skills + create 6 slash commands + merge/condense 4 docs. No new infrastructure — all changes are in skill language and doc content. Skills are markdown files read by AI at runtime; quality = clarity + token efficiency + explicit decision rules.

**Tech Stack:** Markdown only. No code, no tests, no build step. Verification = self-review checklist per task.

---

## Verification Checklist (apply to every skill rewrite)

After writing each skill, verify:
- [ ] No "restate user intent" step
- [ ] No "ask permission to start" step
- [ ] Announce format present at every phase transition
- [ ] Autonomy rule present: explicit when-to-ask vs when-to-proceed
- [ ] Token-efficient: imperative sentences, no narrative prose, no meta-commentary
- [ ] Decision points use tables or conditionals, not paragraphs

---

## Task 1: Rewrite `orchestrator/SKILL.md`

**Files:**
- Modify: `workflow/skills/orchestrator/SKILL.md`

**Step 1: Write new content**

Replace entire file with:

```markdown
---
name: orchestrator
description: Loaded at every session start — routes to the right skill based on intent and complexity.
---

# Workflow Orchestrator

---

## On Session Start

**1. Check for `<workflow-state>` in context:**

| State present | Action |
|---------------|--------|
| Yes | Verify consistency (table below), then resume from `next-action` |
| No | Fresh session — read user's first message, classify, route |

**State consistency checks:**

| Phase | Check | If inconsistent |
|-------|-------|-----------------|
| `spec` | `.workflow/specs/<slug>/working.md` exists? | Restart spec-formation |
| `planning` | `approved.md` exists? | Surface inconsistency to user |
| `execute` | `tasks.md` exists? | Run task-breakdown first |
| `review` | All tasks in `tasks.md` done? | Yes → doc-sync. No → resume execute |

**2. Announce:**
```
[workflow:orchestrator] Session start — routing
```

**3. Classify → route.**

---

## Brainstorm Gate

Ask these 3 questions internally before routing:

1. Does user know the direction they want to take?
2. Is ambiguity strategic (which approach?) or requirement-level (what exactly?)?
3. Would different answers lead to fundamentally different specs?

**If ANY answer is "strategic ambiguity" → route to `workflow:brainstorming`**
**Otherwise → route to `workflow:spec-formation` directly**

Examples that go straight to spec (no brainstorm):
- "add export PDF for invoices"
- "add filter by date on orders page"
- "refactor auth module to separate guard/service/repository"

Examples that need brainstorm:
- "want to improve collaboration but unsure whether to do comments, mentions, or activity feed"
- "want better permissions but unsure role-based vs policy-based"
- "want to restructure for scale but unsure modular monolith vs microservices"

---

## Track Classification

| Track | Signals |
|-------|---------|
| `light` | Single file, obvious fix, no behavior change, no unknowns |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale concerns, breaking change |

Default: `standard` when uncertain.

---

## Skill Routing

| Situation | Route to |
|-----------|----------|
| Strategic ambiguity — user doesn't know direction | `workflow:brainstorming` |
| Intent clear (any track) | `workflow:spec-formation` |
| Approved spec exists → break into tasks | `workflow:task-breakdown` |
| Tasks ready → implement | `workflow:execute` |
| All tasks done → sync docs | `workflow:doc-sync` |
| Approved spec must change | `workflow:spec-amendment` |
| Bug or unexpected failure | `superpowers:systematic-debugging` |
| About to claim done | `superpowers:verification-before-completion` |
| All tasks done, ready to merge | `superpowers:finishing-a-development-branch` |

---

## Autonomy Rules

**Proceed without asking:**
- Implementation details within approved spec
- Test coverage, bug fixes within scope
- Refactors that don't change external behavior
- Gaps with reasonable defaults → assume + note

**Always ask before acting:**

| Situation | Reason |
|-----------|--------|
| Spec change needed | Locked contract — requires re-approval |
| New dependency | Affects maintainability long-term |
| Architecture change touching >3 files | Long-term consequence |
| Public API change | User must own this |
| Scope expansion | User hasn't committed to this |
| Data deletion, force push, irreversible ops | Cannot be undone |

**Never:** restate user intent, ask permission to start, confirm obvious decisions.

---

## Task Brief (required before every task)

```
[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → ask first. LOW/NONE → proceed immediately after brief.

---

## STATE.md Format

Update on every phase transition:

```
phase: <brainstorm|spec|planning|execute|review|done>
active-spec: <slug or "none">
track: <light|standard|heavy>
next-action: <one sentence>
blocked-by: <description or "none">
last-updated: YYYY-MM-DD
```

---

## Core Principle

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.
```

**Step 2: Self-review against checklist**

Verify all 6 checklist items pass. If any fail, fix before committing.

**Step 3: Commit**

```bash
git add workflow/skills/orchestrator/SKILL.md
git commit -m "refactor(orchestrator): smart autonomy routing + brainstorm gate + task brief protocol"
```

---

## Task 2: Rewrite `brainstorming/SKILL.md`

**Files:**
- Modify: `workflow/skills/brainstorming/SKILL.md`

**Step 1: Write new content**

Replace entire file with:

```markdown
---
name: brainstorming
description: Optional branch for strategic ambiguity. Use when user doesn't know which direction to take — not for requirement gaps.
---

# Brainstorming

**Trigger:** Strategic ambiguity only — user unsure which direction, not just missing details.
**Not triggered:** User knows what they want but lacks specifics → use spec-formation directly.

---

## On Entry

```
[workflow:brainstorming] Starting — Topic: <topic>
```

Check `.workflow/specs/` for existing `idea.md`:
- Found → "Previous brainstorm on `<topic>` exists. Continue or start fresh?"
- Not found → proceed to Phase 1

---

## Phase 1 — Understand

One question per message. No proposals yet.
Note tensions, contradictions, unstated priorities — surface only when you have enough context.

Useful probes:
- "What problem are you actually solving?"
- "What does success look like in 3 months — concretely?"
- "What have you already tried or ruled out, and why?"
- "What's the riskiest assumption in this direction?"
- "What would make you abandon this approach entirely?"

Checkpoint every 3–4 exchanges:
```
Explored so far: <brief summary>
→ Keep digging, or ready to look at approaches?
```

Default: keep exploring unless user signals readiness.

---

## Phase 2 — Propose

Once core need and constraints are clear, offer **2–3 approaches** with trade-offs.
Lead with recommendation — not neutrally, with reasoning.

```
**Recommended: Option A** — <one-sentence reason>

| Option | Approach | Strength | Trade-off |
|--------|----------|----------|-----------|
| A ⭐  | ...      | ...      | ...       |
| B     | ...      | ...      | ...       |
| C     | ...      | ...      | ...       |
```

Let user push back. Revise without defending.
Stay in Phase 2 until direction is genuinely locked — not just accepted.

---

## Phase 3 — Stress-test *(optional)*

After direction is chosen, pick **3 most relevant** methods for this specific direction:

```
Direction locked: <one-sentence summary>

Stress-test options:
  A) <Method> — <why it fits this direction>
  B) <Method> — <why it fits this direction>
  C) <Method> — <why it fits this direction>
  D) Skip — direction is solid

Which?
```

Available: `Pre-mortem` · `Inversion` · `Red Team` · `Assumption Surfacing` · `Threat Modeling` · `Second-Order Effects` · `Edge Case Hunting` · `First Principles`

Skip Phase 3 for light tasks or clearly solid directions.

---

## Closing

When user approves direction:

```
[workflow:brainstorming] Complete

Goal: <one sentence>
Approach: <chosen option + core reason>
Constraints locked: <list or "none">
Key decisions: <list>
Ruled out: <list or "none">
Deferred to spec: <open questions>

Next: spec-formation
```

Save to `.workflow/specs/<slug>/idea.md` only if session was long or decisions are complex.

---

## Rules

- One question per message in Phase 1
- No implementation details before direction is locked
- Checkpoint every 3–4 exchanges
- Light tasks: max 3 questions in Phase 1, skip Phase 3
```

**Step 2: Self-review against checklist**

**Step 3: Commit**

```bash
git add workflow/skills/brainstorming/SKILL.md
git commit -m "refactor(brainstorming): token-optimize, fix trigger condition, add announce protocol"
```

---

## Task 3: Rewrite `spec-formation/SKILL.md`

**Files:**
- Modify: `workflow/skills/spec-formation/SKILL.md`

**Step 1: Write new content**

Replace entire file with:

```markdown
---
name: spec-formation
description: Transform intent into approved spec. Draft immediately, clarify blocking gaps only, lock on approval.
---

# Spec Formation

**Two phases: Clarify → Lock.**
Draft first. Mark gaps inline. Ask only what blocks the contract.

---

## Step 0 — Classify track

| Track | Signals |
|-------|---------|
| `light` | Single behavior, obvious scope, no data model, no integration |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale/compliance |

State track before proceeding.

---

## Step 1 — Load context

1. `.workflow/specs/<slug>/idea.md` — brainstorm summary if exists
2. `.workflow/specs/<slug>/working.md` — previous draft if in progress
3. `.workflow/PROJECT.md` — constraints, tech stack, key decisions

---

## PHASE 1: CLARIFY

```
[workflow:spec-formation] Phase 1 — Clarifying: <slug>
```

### Draft immediately

Write `working.md` now. Do not ask questions before drafting.

**If prompt is unclear:** Draft with best interpretation. Mark your interpretation as assumption.
**Only exception:** Prompt so vague no FR can be written → ask 1 question minimum needed.

Where information is missing, write `[GAP: <specific question>]` inline.

### Spec structure

```markdown
# Spec: <slug>

Status: draft
Track: <light|standard|heavy>
Created: YYYY-MM-DD

## Goal
One sentence. What this builds and why.

## Scope
In scope:
- ...
Out of scope:
- ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<who does what and why>
Acceptance:
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>
- FR-002: Users MUST be able to <action>
[GAP: <question>]

## Key Entities          ← when data is involved
- <Entity>: <what it is, key attributes, relationships>

## Assumptions
- A-001: <assumed true> — if wrong, impacts: <FR-N>

## Non-Functional        ← heavy only or explicitly required
- Performance: <measurable target>
- Security: <specific constraint>

## Interaction & UX      ← when UI is involved
- <critical user journey>
- Error states: <what user sees when X fails>

## Integration           ← when external systems involved
- <System>: <what we depend on, failure mode>

## Edge Cases & Errors   ← standard/heavy only
- What happens when <boundary condition>?

## Success Criteria
- SC-001 (covers FR-001): <measurable outcome>

## Open Items
- <item deferred to planning/implementation>
```

**FR rule — WHAT not HOW:**
- ✅ `System MUST notify users when payment fails`
- ❌ `System MUST send Stripe webhook on payment failure`

### Triage gaps

For each `[GAP]`:

| Decision | When |
|----------|------|
| **Ask now** | Answer changes FR, SC, entity shape, or scope boundary |
| **Defer to Open Items** | Tech choices, implementation edge cases |
| **Assume + note** | Low stakes, reasonable default exists |

### Ask blocking gaps

Group independent questions in one message. Max 5 per session.

```
**Q1: <question>**
> Recommended: **<option>** — <one-sentence reason>

| Option | Description |
|--------|-------------|
| A | ... |
| B | ... |

Reply A/B, "yes" to accept recommendation, or custom answer.
```

After each answer: replace `[GAP]` with resolved detail, log in `## Clarifications`.

Run one more gap scan after answers — new answers can reveal new gaps. Max 3 rounds; remaining gaps → Open Items.

---

## PHASE 2: LOCK

```
[workflow:spec-formation] Phase 2 — Locking: <slug>
```

### Self-validate before presenting

```
[ ] Track stated
[ ] No [GAP] remain (or moved to Open Items with rationale)
[ ] Every FR: MUST + testable, no HOW details
[ ] Every SC: measurable — numbers not adjectives
[ ] Every FR maps to at least one SC
[ ] Scope: in AND out stated explicitly
[ ] Stories have Given/When/Then (standard/heavy)
[ ] PROJECT.md constraints respected
[ ] Light track: fits on one screen
```

### Present for approval

**Light track:**
```
**Spec: <slug>** (light)
Goal: <one sentence>
Will do: <2-3 bullet FRs>
Won't do: <scope boundary>
Done when: <SC-001>

Looks right? Reply "yes" or give me the next task.
```
Implicit approval: any affirmative reply counts.

**Standard/Heavy:**
```
Spec ready for review.
Resolved: {N} gaps. Deferred: {list}.

Approve to lock, or tell me what to change.
```
Requires explicit approval.

### Lock

On approval:
1. Copy `working.md` → `approved.md`, set `Status: approved`
2. Delete `working.md`
3. Update `.workflow/STATE.md`

**Light:**
```
phase: execute
active-spec: <slug>
track: light
next-action: Begin execute directly (skip task-breakdown)
```

**Standard/Heavy:**
```
phase: planning
active-spec: <slug>
track: <standard|heavy>
next-action: Run task-breakdown on approved.md
```

4. Announce:
```
[workflow:spec-formation] Locked → .workflow/specs/<slug>/approved.md
Gaps resolved: {N} | Deferred: {M}
Next: task-breakdown
```

---

## Memory

| File | Lifecycle |
|------|-----------|
| `idea.md` | Persistent — never delete |
| `working.md` | Temp — delete after `approved.md` created |
| `approved.md` | Permanent locked contract — change only via spec-amendment |
| `STATE.md` | Updated on every phase transition |

---

## Scale

| Track | Sections required | Clarification depth |
|-------|-------------------|---------------------|
| `light` | Goal + FRs + SC | 1–2 questions max |
| `standard` | + Scope + Stories + Entities + Edge Cases | Full triage, up to 5 questions |
| `heavy` | All sections | Full triage + NFR + Integration + 3 rounds |
```

**Step 2: Self-review against checklist**

**Step 3: Commit**

```bash
git add workflow/skills/spec-formation/SKILL.md
git commit -m "refactor(spec-formation): explicit clarify→lock phases, draft-first rule, remove restate pattern"
```

---

## Task 4: Rewrite `task-breakdown/SKILL.md`

**Files:**
- Modify: `workflow/skills/task-breakdown/SKILL.md`

**Step 1: Write new content**

Replace entire file with:

```markdown
---
name: task-breakdown
description: Decompose approved spec into independently verifiable tasks with parallelization map.
---

# Task Breakdown

```
[workflow:task-breakdown] Decomposing: <slug>
```

Turn `approved.md` into `tasks.md`. Each task = smallest unit that can be independently committed and verified.

---

## Step 0 — Read inputs

1. `approved.md` — locked contract
2. `PROJECT.md` — tech stack, conventions, constraints
3. Existing codebase state — understand before decomposing

---

## Step 1 — Decompose

Rules:
- One concern per task
- Each task independently testable
- Every task maps to specific FR or SC — no tasks without spec backing
- Order: infrastructure → features → integration

**Task format:**

```markdown
### Task {N} — {title}
**Spec ref:** FR-{N} / SC-{N}
**Parallel:** yes | no
**Depends on:** Task {N} | none

#### What to build
<one paragraph — behavior, not implementation>

#### Files
- Create: `path/to/file`
- Modify: `path/to/existing:L10-L50`
- Test: `path/to/test`

#### Acceptance
- [ ] <specific verifiable outcome>
- [ ] <specific verifiable outcome>

#### Steps (standard/heavy only)
1. Write failing test for <behavior>
2. Run → confirm FAIL
3. Implement minimal code
4. Run → confirm PASS
5. Commit: `type(scope): message`
```

**Heavy track extras:**
```markdown
#### Risk notes
- Risk: <what could go wrong>
- Mitigation: <how to handle>
```

---

## Step 2 — Parallelization map

```markdown
## Execution Order

Sequential:
- Task 1 → Task 2 (Task 2 needs Task 1's output)

Parallel group A (after Task 1):
- Task 3 [P]
- Task 4 [P]

Sequential:
- Task 5 (integrates A)
```

Heavy: add dependency graph after map.

---

## Step 3 — Save + update state

Save to `.workflow/specs/<slug>/tasks.md`.

Update STATE.md:
```
phase: execute
next-action: Begin Task 1
```

Announce:
```
[workflow:task-breakdown] {N} tasks across {M} parallel groups → tasks.md
Next: execute
```

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | 1–3 tasks, no steps section, no parallelization map |
| `standard` | Full format, steps section, parallelization map |
| `heavy` | Full format + dependency graph + risk notes |
```

**Step 2: Self-review against checklist**

**Step 3: Commit**

```bash
git add workflow/skills/task-breakdown/SKILL.md
git commit -m "refactor(task-breakdown): add announce protocol, token-optimize"
```

---

## Task 5: Rewrite `execute/SKILL.md`

**Files:**
- Modify: `workflow/skills/execute/SKILL.md`

**Step 1: Write new content**

Replace entire file with:

```markdown
---
name: execute
description: Implement tasks from tasks.md using fresh subagents. Task Brief before each task. Two-stage review for standard/heavy. Commit per task.
---

# Execute

```
[workflow:execute] Starting execution — <slug> | {N} tasks | track: <track>
```

---

## Step 0 — Load context (once)

Read once. Never make subagents read these files.

1. `approved.md` — what must be built
2. `tasks.md` — all tasks with full text
3. Current codebase — enough to give subagents accurate context

Cache everything. Subagents receive context as text, not file references.

---

## Step 1 — Task Brief (before every task)

Before dispatching any subagent, output:

```
[workflow:execute] Task {N}/{total} — <title>

[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → wait for user input before dispatching.
LOW/NONE → dispatch immediately after brief.

---

## Step 2 — Pick next task

From `tasks.md`, pick next unblocked task.
Parallel-safe tasks (`[P]` in same group) can be dispatched concurrently — never dispatch two tasks touching the same files.

---

## Step 3 — Dispatch implementer subagent

```
[workflow:execute] ⏳ Task {N} — dispatching implementer
```

Give subagent everything upfront:

```
You are implementing Task {N}: {title}

SPEC CONTEXT:
{relevant excerpt from approved.md}

TASK:
{full task text from tasks.md}

CODEBASE CONTEXT:
{relevant existing code, file structure, conventions}

Instructions:
- Follow task steps exactly
- Write tests first (standard/heavy)
- Self-review before reporting done
- Commit when complete: `type(scope): message`
- Ask questions BEFORE starting, not during
```

If subagent asks questions → answer completely, then redispatch.

---

## Step 4 — Review

**Light:** Self-review from subagent is sufficient.

**Standard/Heavy:** Two-stage review after each task.

### Stage 1 — Spec compliance

```
[workflow:execute] ⏳ Task {N} — spec compliance review
```

Dispatch fresh reviewer:
```
Review Task {N} for spec compliance.

SPEC: {approved.md excerpt}
TASK: {task definition}
Commits: {git SHAs}

Check:
- Every acceptance criterion met?
- Anything built NOT in spec?
- Any spec requirement missing?

Output: ✅ Compliant | ❌ Issues: [list]
```

Issues → implementer fixes → Stage 1 re-review. Never proceed to Stage 2 with open Stage 1 issues.

### Stage 2 — Code quality

```
[workflow:execute] ⏳ Task {N} — code quality review
```

Dispatch fresh reviewer:
```
Review Task {N} for code quality.

Commits: {git SHAs}
Conventions: {from PROJECT.md}

Check:
- Tests exist and meaningful
- No magic numbers, unclear names, dead code
- No unnecessary complexity
- Follows project conventions

Output: ✅ Approved | Issues: [Critical | Important | Minor]
```

Critical/Important → implementer fixes → re-review.
Minor → note, proceed.

---

## Step 5 — Mark complete + continue

After review passes:

```
[workflow:execute] ✅ Task {N}/{total} complete
```

Mark `[x] done` in `tasks.md`.

Update STATE.md:
```
next-action: Task {N+1} — {title}
```

Move to next task. Repeat until all done.

---

## Step 6 — Final review + handoff

```
[workflow:execute] All {N} tasks complete — final review
```

**Light:** Skip — per-task self-review sufficient.
**Standard:** Skip if tasks were low-risk and test coverage solid.
**Heavy:** Required.

Final review prompt:
```
Review complete implementation against approved spec.

approved.md: {full text}
All commits since task-breakdown: {SHAs}

Check: does full implementation deliver the spec?
Any integration issues between tasks?
```

Then:
```
[workflow:execute] Complete — {N} tasks done
Next: doc-sync → finishing-a-development-branch
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```
```

**Step 2: Self-review against checklist**

**Step 3: Commit**

```bash
git add workflow/skills/execute/SKILL.md
git commit -m "refactor(execute): task brief before each task, announce at every step, token-optimize"
```

---

## Task 6: Rewrite `doc-sync/SKILL.md` and `spec-amendment/SKILL.md`

**Files:**
- Modify: `workflow/skills/doc-sync/SKILL.md`
- Modify: `workflow/skills/spec-amendment/SKILL.md`

**Step 1: Write doc-sync new content**

Replace entire file with:

```markdown
---
name: doc-sync
description: Update project docs to reflect what was built. Runs after execute, before branch completion.
---

# Doc Sync

```
[workflow:doc-sync] Assessing changes: <slug>
```

Update only what changed. Don't create docs for their own sake.

---

## Step 1 — Assess

Compare built (approved.md + commits) against existing `docs/`.

Per changed area:
- Existing doc describes this behavior? → update it
- New architectural decision? → create ADR
- Project overview changed? → update overview
- API/interface changed? → update reference

Skip unaffected docs. Skip docs that restate code.

---

## Step 2 — Update

| Change type | Doc to update |
|-------------|---------------|
| New feature behavior | `docs/overview.md` if it changes big picture |
| Architecture decision | New ADR: `docs/adr/YYYY-MM-DD-<decision>.md` |
| API or interface change | Relevant reference doc |
| Bug fix | Nothing unless it reveals design correction |
| Refactor | Nothing unless it changes public behavior |

**ADR format:**
```markdown
# ADR: <decision title>

Date: YYYY-MM-DD
Status: accepted

## Context
<why this decision was needed>

## Decision
<what was decided>

## Consequences
<what this enables, what it constrains>
```

---

## Step 3 — Announce

```
[workflow:doc-sync] Complete
Updated: <list>
Created: <list>
Skipped: <what and why>
```

Update STATE.md:
```
phase: done
next-action: Run superpowers:finishing-a-development-branch
```

---

## Memory rule

| Content | Where |
|---------|-------|
| Long-term architectural knowledge | `docs/` |
| Current project state | `.workflow/STATE.md` |
| Spec details | `.workflow/specs/<slug>/approved.md` |
| Session working notes | Nowhere — discard after session |

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | Usually nothing. Skip unless public behavior changed. |
| `standard` | Update affected docs. Add ADR if architectural. |
| `heavy` | Full assessment — overview, ADRs, references as needed. |
```

**Step 2: Write spec-amendment new content**

Replace entire file with:

```markdown
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
```

**Step 3: Self-review both files against checklist**

**Step 4: Commit**

```bash
git add workflow/skills/doc-sync/SKILL.md workflow/skills/spec-amendment/SKILL.md
git commit -m "refactor(doc-sync,spec-amendment): add announce protocol, condense language"
```

---

## Task 7: Create slash commands

**Files:**
- Create: `workflow/commands/brainstorm.md`
- Create: `workflow/commands/spec.md`
- Create: `workflow/commands/tasks.md`
- Create: `workflow/commands/execute.md`
- Create: `workflow/commands/status.md`
- Create: `workflow/commands/amend.md`

**Step 1: Create `workflow/commands/brainstorm.md`**

```markdown
---
description: Force start brainstorming session
---

Invoke `workflow:brainstorming` skill now for this topic: $ARGUMENTS

Skip brainstorm gate check — user has explicitly requested brainstorming.
Announce: `[workflow:brainstorming] Starting (user-initiated)`
```

**Step 2: Create `workflow/commands/spec.md`**

```markdown
---
description: Force start spec-formation
---

Invoke `workflow:spec-formation` skill now for this topic: $ARGUMENTS

Skip orchestrator routing — go directly to spec-formation.
Announce: `[workflow:spec-formation] Starting (user-initiated)`
```

**Step 3: Create `workflow/commands/tasks.md`**

```markdown
---
description: Force task-breakdown on current approved spec
---

Invoke `workflow:task-breakdown` skill now.

Read `.workflow/STATE.md` for active-spec slug, then run task-breakdown on `.workflow/specs/<slug>/approved.md`.
Announce: `[workflow:task-breakdown] Starting (user-initiated)`
```

**Step 4: Create `workflow/commands/execute.md`**

```markdown
---
description: Force execute on current tasks
---

Invoke `workflow:execute` skill now.

Read `.workflow/STATE.md` for active-spec slug, then run execute on `.workflow/specs/<slug>/tasks.md`.
Announce: `[workflow:execute] Starting (user-initiated)`
```

**Step 5: Create `workflow/commands/status.md`**

```markdown
---
description: Show current workflow state
---

Read `.workflow/STATE.md` and display:

```
[workflow:status]
Phase: <phase>
Spec: <active-spec>
Track: <track>
Next: <next-action>
Blocked: <blocked-by>
Updated: <last-updated>
```

If no STATE.md found: "No active workflow. Start with /spec <topic> or describe what you want to build."
```

**Step 6: Create `workflow/commands/amend.md`**

```markdown
---
description: Force spec-amendment for a change
---

Invoke `workflow:spec-amendment` skill now for this change: $ARGUMENTS

Skip orchestrator routing — go directly to spec-amendment.
Announce: `[workflow:spec-amendment] Starting (user-initiated): $ARGUMENTS`
```

**Step 7: Commit**

```bash
git add workflow/commands/
git commit -m "feat(commands): add 6 slash commands as explicit workflow shortcuts"
```

---

## Task 8: Merge and rewrite docs

**Files:**
- Create: `workflow/docs/principles.md`
- Delete content of: `workflow/docs/philosophy.md` (replace with redirect)
- Delete content of: `workflow/docs/responsibility.md` (replace with redirect)
- Modify: `workflow/docs/orchestration.md`
- Modify: `workflow/docs/review-model.md`

**Step 1: Create `workflow/docs/principles.md`**

```markdown
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
```

**Step 2: Replace `philosophy.md` and `responsibility.md` with redirects**

`workflow/docs/philosophy.md`:
```markdown
# Core Philosophy

→ Merged into [principles.md](./principles.md)
```

`workflow/docs/responsibility.md`:
```markdown
# Responsibility Model

→ Merged into [principles.md](./principles.md)
```

**Step 3: Rewrite `orchestration.md`**

```markdown
# Orchestration Model

## Structure

Orchestrator (main Claude agent) + specialized subagents.

**Orchestrator:** holds full picture, routes skills, drives spec formation, assigns tasks to subagents, tracks state, escalates strategic decisions to user.

**Subagents:** receive a task + full context → implement → test → self-review → commit → return result. Never modify spec, never make strategic decisions.

## Flow

```
User → Orchestrator (reads orchestrator skill + STATE.md at session start)
  ├─ Strategic ambiguity? → brainstorming
  ├─ Intent clear → spec-formation
  ├─ Approved spec → task-breakdown → tasks.md
  ├─ Tasks ready → execute (subagents per task, two-stage review)
  ├─ All done → doc-sync
  └─ Ready to ship → finishing-a-development-branch
```

Track controls ceremony: `light` = fast + minimal review. `standard` = full spec + two-stage review. `heavy` = full spec + NFRs + ADRs + mandatory final review.

## Context Handoff

Orchestrator provides subagents: approved spec excerpt, task definition, project context, decisions already made.

Subagents do not read conversation history. Orchestrator must be thorough in handoffs.

## Natural Language First

Users speak naturally. Orchestrator infers phase from context and STATE.md. Slash commands exist for explicit overrides — not the default.
```

**Step 4: Rewrite `review-model.md`**

```markdown
# Review Model

Three layers. Issues caught at smallest scope = cheapest to fix.

## Layer 1 — Per Task

After each task. Checks: acceptance criteria met, spec compliant, edge cases handled, tests sufficient.

**Light:** subagent self-review only.
**Standard/Heavy:** separate spec-compliance reviewer, then code-quality reviewer.

## Layer 2 — Per Group

After a cluster of tasks that form a meaningful capability. Checks: tasks integrate correctly, behavior consistent end-to-end, no gaps between individually-passing tasks.

**Standard/Heavy only.**

## Layer 3 — Final Integration

After all tasks. Checks: full implementation delivers spec, no regressions, all docs updated.

**Light:** skip. **Standard:** optional. **Heavy:** required.

## Escalation

If review finds: spec scope change needed, design flaw, unexpected long-term risk, or decision requiring user judgment → escalate with:
1. What was found
2. Why it matters
3. Recommendation or options
4. Request for decision

Review does not expand scope, introduce new requirements, or block on style.
```

**Step 5: Commit**

```bash
git add workflow/docs/principles.md workflow/docs/philosophy.md workflow/docs/responsibility.md workflow/docs/orchestration.md workflow/docs/review-model.md
git commit -m "docs(workflow): merge philosophy+responsibility→principles, condense orchestration+review-model"
```

---

## Task 9: Update `overview.md`

**Files:**
- Modify: `workflow/docs/overview.md`

**Step 1: Write new content**

```markdown
# Workflow Plugin — Overview

A structured AI-driven development framework. Solves AI's primary failure: acting before understanding. Enforces intent clarity before execution, gives AI high autonomy within those bounds, keeps spec/code/docs in sync.

## Core Thesis

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.

## How It Works

Every session, the orchestrator skill is injected at start. It reads STATE.md (if present) and routes to the right skill based on current phase and intent.

```
User request
  ├─ Strategic ambiguity? → brainstorming → direction locked
  └─ Intent clear → spec-formation → approved spec
                         ↓
                   task-breakdown → tasks.md
                         ↓
                      execute → subagents implement + review
                         ↓
                     doc-sync → docs updated
                         ↓
              finishing-a-development-branch
```

## Skills

| Skill | Role |
|-------|------|
| `orchestrator` | Session router — injects at start, routes by intent + track |
| `brainstorming` | Optional — for strategic ambiguity only |
| `spec-formation` | Draft → clarify → lock. Two phases: clarify and lock |
| `task-breakdown` | Decompose approved spec into parallel-safe tasks |
| `execute` | Task Brief + subagent per task + two-stage review |
| `doc-sync` | Update only affected docs after delivery |
| `spec-amendment` | Guarded process for changing locked spec |

## Slash Commands

| Command | Action |
|---------|--------|
| `/brainstorm [topic]` | Force brainstorming |
| `/spec [topic]` | Force spec-formation |
| `/tasks` | Force task-breakdown |
| `/execute` | Force execute |
| `/status` | Show STATE.md |
| `/amend <change>` | Force spec-amendment |

Commands bypass orchestrator judgment. Use when you want to explicitly assign a phase.

## Smart Autonomy

AI outputs a **Task Brief** before every task:
```
[Task Brief]
Plan: <what + how>
Risk: NONE | LOW | HIGH
Action: proceeding | ⚠️ need input: <question>
```

HIGH risk = asks first. LOW/NONE = proceeds. AI only asks for irreversible or strategic decisions.

## Project State

`.workflow/` in user's project:
```
.workflow/
├── STATE.md              # current phase, active spec, next action
├── PROJECT.md            # identity, constraints, key decisions
└── specs/<slug>/
    ├── idea.md           # brainstorm output (persistent)
    ├── working.md        # spec in progress (temp)
    ├── approved.md       # locked contract
    └── tasks.md          # execution breakdown
```

## Docs

| Doc | Content |
|-----|---------|
| `principles.md` | Core beliefs + responsibility split |
| `spec-lifecycle.md` | Three layers: idea → working → approved |
| `task-model.md` | What a task is and how it's structured |
| `orchestration.md` | Orchestrator + subagent model |
| `review-model.md` | Three-layer review process |
| `docs-architecture.md` | Long-term vs temp docs, promote rules |
```

**Step 2: Commit**

```bash
git add workflow/docs/overview.md
git commit -m "docs(overview): update to reflect smart autonomy redesign, commands, task brief"
```

---

## Execution Handoff

Plan saved to `workflow/docs/plans/2026-03-12-workflow-smart-autonomy-implementation.md`.

**Two execution options:**

**1. Subagent-Driven (this session)** — dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** — open new session with executing-plans, batch execution with checkpoints

Which approach?
