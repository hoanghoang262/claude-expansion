# Concern Resolution

How concerns are created, tracked, and resolved.

---

## What is a concern

A concern is an issue discovered during work that is **not blocking** but **should not be forgotten**. It lives in `docs/concerns/CONCERN-{id}.md` [PERMANENT].

Concerns are internal — agent-to-agent communication. User only sees Tier 3 escalations.

---

## Concern lifecycle

```
Discovered → Created (status: open) → Resolved (status: resolved) → ADR created
```

### Creating a concern (Tier 2 escalation)

Use template `templates/concern-template.md`. Required fields:

```
ID: CONCERN-{N}
Discovered by: {agent-name} | {date}
Severity: High | Medium | Low
Status: open

Description: {what is the issue}
Location: {file:line or module}
Why it matters: {impact}
Options: {A vs B with pros/cons}
Recommended: {which option and why}
```

### Resolving a concern

When user provides a decision, or PM resolves it:

1. **Create ADR** — `docs/decisions/YYYY-MM-DD-{slug}.md` [PERMANENT]
   - Use template `templates/decision-template.md`
   - Context: what prompted this (link to concern)
   - Decision: what was decided
   - Consequences: what this enables/constrains

2. **Update concern file** — don't delete, update the `## Resolution` section:
   ```markdown
   ## Resolution

   **Status:** resolved
   **Resolved:** {YYYY-MM-DD}
   **Decision:** see `docs/decisions/{slug}.md`
   ```

3. **If decision requires implementation** → return to `clarify` for a new feature. Never implement without a spec.

---

## When to create vs not

| Situation | Create concern? |
|-----------|----------------|
| Code smell found during execute | No — Tier 1, fix in place |
| Technical debt that affects future work | Yes — Tier 2 |
| Spec gap discovered mid-ACT | Yes — Tier 2 (spec is frozen) |
| Can't proceed at all | No — Tier 3 only after Tier 1 exhausted. Ask user directly |
| Design choice with non-obvious trade-offs | Yes — Tier 2, then resolve via ADR |

---

## Review cadence

PM checks `docs/concerns/` (status: open) at:
- Every `clarify` action (session start)
- Before phase transitions (UNDERSTAND → ACT)
- Before version release (all open concerns reviewed)
