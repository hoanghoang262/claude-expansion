# Spec Form Phase

Create new specification from user intent. Spec-Driven Development.

## Inputs Needed

1. **User intent** - What user wants to build
2. **Context** - `docs/PROJECT.md`, relevant specs
3. **Existing codebase** - Related components

## Process

### Phase 1: Assess Intent

Classify what user provides:

| Type | Action |
|------|--------|
| Clear goal + full context | Draft spec immediately |
| Clear goal + brief | Draft with assumptions, ask 1 focused question |
| Vague ("make it better") | Ask ONE clarifying question first |
| Has existing plan | Verify quality, don't recreate |

### Phase 2: Draft Spec

Create `docs/specs/<slug>/spec.md`:

```markdown
---
status: draft
track: <light|standard|heavy>
created: YYYY-MM-DD
---

# Spec: <slug>

## Goal
One sentence. What this builds and why.

## Scope
In scope: ...
Out of scope: ...

## User Stories          ← standard/heavy only
### Story 1 — <title> (P1)
<who does what and why>
Acceptance:
- Given <state>, when <action>, then <outcome>

## Functional Requirements
- FR-001: System MUST <testable behavior>
- FR-002: ...

## Key Entities          ← when data involved
- <Entity>: <attributes, relationships>

## Assumptions
- A-001: <assumed true> — if wrong, impacts: FR-N

## Non-Functional        ← heavy only
- Performance: <measurable target>
- Security: <specific constraint>

## Edge Cases            ← standard/heavy only
- What happens when <boundary condition>?

## Success Criteria
- SC-001 (covers FR-001): <measurable outcome>
- SC-002 (covers FR-002): <measurable outcome>

## Open Items
- <deferred to planning/implementation>
```

### Phase 3: Clarify

If intent not clear → ask ONE question:

```
**Clarifying:** <question>

Context: <why this matters>
```

### Phase 4: Self-Validate

Check:
- [ ] Track stated
- [ ] Every FR: MUST + testable, no HOW
- [ ] Every SC: measurable — numbers not adjectives
- [ ] Every FR maps to at least one SC
- [ ] Scope: in AND out explicit

### Phase 5: Present for Approval

**Light:**
```
**Spec: <slug>** (light)
Goal: <one sentence>
Will do: <2-3 bullet FRs>
Won't do: <scope boundary>

Looks right? Reply "yes" or give me the next task.
```

**Standard/Heavy:**
```
Spec ready. Gaps: <list>. Deferred: <list>.
Approve to lock, or tell me what to change.
```

### Phase 6: Lock

On approval:
1. Set `status: approved`
2. Update `related:` in frontmatter

## Track Classification

| Track | Criteria |
|-------|----------|
| Light | All safe, no new behavior |
| Standard | Medium risk, no critical |
| Heavy | High risk, critical path |

### Track Reasoning (required)

When classifying track, state reasoning clearly:

```
Track: STANDARD
Reasoning:
  - reversibility: ✅ code only, revert safe
  - blast_radius:  ⚠️ affects 2 modules
  - coordination:  ✅ none
  - testability:   ✅ unit test sufficient
```

Don't classify silently — reasoning must be visible for user to audit if needed.

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| New spec | `docs/specs/<slug>/spec.md` |
| Related feature | `docs/features/<name>.md` (if new) |
| Architecture change | `docs/architecture/` + ADR if needed |

## Output

- Approved spec in `docs/specs/<slug>/spec.md`
- Track determined
- Next phase: `plan.md`

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Spec approved | `plan.md` |
| Need clarification | Ask user |
| Intent unclear | Back to understand.md |
