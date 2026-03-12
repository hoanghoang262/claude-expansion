# Workflow Plugin — Smart Autonomy Redesign

Date: 2026-03-12
Status: approved

## Goal

Rebuild the workflow plugin so AI operates autonomously by default — planning before acting, surfacing only decisions with long-term or irreversible impact, and making its internal state visible to the user at all times.

## Core Problems Being Fixed

| Problem | Root Cause |
|---------|------------|
| AI asks too many questions | No clear rule for when to ask vs. assume |
| AI confirms/restates user intent | Skills have "restate before proceeding" steps |
| User can't tell what AI is doing | No announce protocol across skills |
| Brainstorm blocks clear tasks | Brainstorm is mandatory gate instead of optional branch |
| Spec clarify phase is implicit | No clear boundary between "exploring requirement" and "writing contract" |

---

## Design Decisions

### 1. Smart Autonomy Protocol

Every skill follows this decision rule — no exceptions:

| Situation | Action |
|-----------|--------|
| Implementation detail, test choice, refactor | Proceed |
| Missing info, reasonable default exists | Assume + note in brief |
| Info missing, no reasonable default | 1 targeted question |
| Irreversible: data deletion, public API change, force push | Ask |
| Strategic: new dependency, scope expansion, architecture change >3 files | Ask |

**Never:** restate user intent, ask permission to start, confirm obvious decisions.

### 2. Task Brief — required before every task

Before any task begins, AI outputs:

```
[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk = ask first. LOW/NONE = proceed immediately after brief.

### 3. AI Visibility — announce protocol

Every skill announces at each phase transition. Built into skill language, no hooks needed.

Format:
```
[workflow:<skill>] <Phase> — <detail>
```

Examples:
```
[workflow:spec-formation] Drafting: export-invoice-pdf
[workflow:execute] Task 3/7 — Add PDF renderer | track: standard
[workflow:execute] ⏸ spec-reviewer subagent running...
[workflow:doc-sync] Updated: docs/overview.md
```

### 4. Slash Commands — shortcuts only

AI uses skills automatically based on context. Commands let user bypass AI judgment and assign directly.

```
/brainstorm [topic]   → force brainstorming
/spec [topic]         → force spec-formation
/tasks                → force task-breakdown on current approved.md
/execute              → force execute
/status               → show STATE.md summary
/amend <change>       → force spec-amendment
```

### 5. Brainstorm — optional branch, not mainline

**Trigger:** Only when user has strategic ambiguity — doesn't know which direction to take.

**Not triggered:** When user knows what they want but lacks details. Those go straight to spec-formation.

**Routing rule — 3 diagnostic questions:**
1. Does user know the direction? → No → brainstorm
2. Is ambiguity strategic (which approach?) or requirement-level (what exactly?)? → Strategic → brainstorm
3. Would different answers lead to fundamentally different specs? → Yes → brainstorm

### 6. Spec-Formation — 2 explicit phases

**Phase 1: Clarify**
- AI drafts working.md immediately from user intent
- Marks gaps inline: `[GAP: <specific question>]`
- Triages gaps: ask now / assume / defer
- Asks only blocking gaps (answer changes FR, scope, entity shape)
- **Never asks to confirm understanding of the prompt** — drafts first, user corrects draft

**Phase 2: Lock**
- All blocking gaps resolved
- FR: WHAT not HOW, testable
- SC: measurable, no adjectives without numbers
- AI self-validates before presenting
- Light: compact summary for approval
- Standard/Heavy: full spec for explicit approval
- On approval: working.md → approved.md, STATE.md updated

**Rule:** If prompt is unclear → draft with assumptions. Only ask if prompt is so vague that no FR can be written.

### 7. Docs — sync and condense

| Action | Files |
|--------|-------|
| Merge | `philosophy.md` + `responsibility.md` → `principles.md` |
| Rewrite shorter | `orchestration.md`, `review-model.md` |
| Keep | `spec-lifecycle.md`, `task-model.md`, `docs-architecture.md` |
| Update after skills done | `overview.md` |

---

## Skills Rewrite Scope

| Skill | Changes |
|-------|---------|
| `orchestrator` | New routing logic (brainstorm gate), autonomy rules, announce format |
| `brainstorming` | Rewrite trigger condition, token-optimize language |
| `spec-formation` | Explicit Phase 1/2 split, remove restate pattern, draft-first rule |
| `task-breakdown` | Add Task Brief format, announce protocol |
| `execute` | Add Task Brief before each task, announce at each step |
| `doc-sync` | Add announce protocol, condense language |
| `spec-amendment` | Minor: add announce, remove verbose prose |

## Slash Commands (new)

Add `workflow/commands/` directory with one `.md` per command.

---

## File Structure After

```
workflow/
  skills/
    orchestrator/SKILL.md       ← routing + autonomy rules
    brainstorming/SKILL.md      ← optional branch, token-optimized
    spec-formation/SKILL.md     ← 2-phase: clarify → lock
    task-breakdown/SKILL.md     ← task brief format
    execute/SKILL.md            ← task brief + announce
    doc-sync/SKILL.md           ← announce + condensed
    spec-amendment/SKILL.md     ← announce + condensed
  commands/
    brainstorm.md
    spec.md
    tasks.md
    execute.md
    status.md
    amend.md
  docs/
    principles.md               ← merged philosophy + responsibility
    spec-lifecycle.md
    task-model.md
    orchestration.md            ← rewritten shorter
    review-model.md             ← rewritten shorter
    docs-architecture.md
    overview.md                 ← updated last
```
