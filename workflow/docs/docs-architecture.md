# Memory Architecture

Two zones with clear separation. Never mix them.

---

## Long-Term Memory — `docs/`

Project knowledge that persists across all sessions and contributors. Updated continuously as the system evolves.

```
docs/
├── PROJECT.md                    # project identity, stack, goals, constraints
├── overview.md                   # what the system does and how
├── specs/<slug>/
│   └── spec.md                   # locked contract (status: draft → approved)
├── features/<name>.md            # feature behavior docs
├── use-cases/<name>.md           # user-facing behavior
└── adr/<date>-<name>.md          # architecture decisions (immutable, global)
```

**Rules:**
- Content must be accurate at time of writing
- Updated as part of any delivery that changes what is documented
- No speculation presented as fact
- A change is not done until docs reflect it

---

## Short-Term Memory — `.workflow/`

Thinking in progress. Not project knowledge — working space for the current session or delivery.

```
.workflow/
├── brainstorm/
│   └── <N>-<topic>.md            # numbered, kept until feature ships
└── log/
    ├── task-N.md                 # implementer output: SHA, what built
    └── review-N.md               # reviewer output: ✅/❌ + issues
```

**Rules:**
- Created freely — no ceremony
- Never treated as source of truth
- Not linked from long-term docs
- Cleaned up after feature ships (`phase: done`)

---

## Promotion Rule

Short-term content moves to `docs/` only when distilled — rough notes stripped, only decisions and behavior kept.

Promote if:
1. Has long-term value (needed in future sessions or by future contributors)
2. Affects how the system is understood
3. Reflects a committed requirement, spec, or design decision
4. Is a traceable architectural decision

If none of these → discard.

---

## Traceability

`spec.md` is the connection hub. It carries `related:` frontmatter linking to every `docs/` file this delivery touches:

```yaml
---
status: approved
related:
  feature: docs/features/<name>.md
  use-cases: docs/use-cases/<name>.md
  adr: docs/adr/YYYY-MM-DD-<decision>.md   # only if architectural decision made
---
```

`doc-syncer` reads `related:` → knows exactly which files to update. No guessing, no scanning.

**Rules:**
- Only include docs that exist or will be created in this delivery
- Update `related:` if a linked file is renamed or moved
- `adr:` only when a new architectural decision was locked

---

## Spec Lifecycle

One file. Evolves in-place.

```
Status: draft    → being written, gaps marked [GAP: ...]
Status: approved → locked contract, changes only via amendment process
```

Amendment = edit `spec.md` directly + commit with descriptive message:
```
spec(<slug>): amend <section> — <what changed and why>
```

Git is the audit trail. No amendment log in the file itself.

---

## ADR Convention

```
docs/adr/<date>-<slug>.md
```

ADRs are global and immutable. Superseded by a new ADR, never edited.

```markdown
# ADR: <title>

Date: YYYY-MM-DD
Status: accepted | superseded by docs/adr/<date>-<slug>.md

## Context
<why this decision was needed>

## Decision
<what was decided>

## Consequences
<what this enables, what it constrains>
```

---

## Doc Sync Is Part of Done

Every delivery that changes behavior, architecture, or constraints MUST update affected `docs/` files before being marked done. `doc-syncer` runs last, reads `related:` from `spec.md`, makes the updates.
