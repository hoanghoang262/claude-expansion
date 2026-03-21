# REQUIREMENTS.md Reference

## Purpose

Lists all requirements with status. **Lifespan: PERMANENT — NEVER DELETE.**

## Lifecycle

```
Created by:
  └── initialize (initial requirements)

Updated by:
  └── doc-sync (mark completed requirements)

Never deleted.
```

## Structure

```markdown
# [Project Name] — Requirements

## v1 Requirements

### [Category]

- [ ] **REQ-{id}**: [Requirement description]

### [Category]

- [ ] **REQ-{id}**: [Requirement description]

## v2 Requirements (Deferred)

- [ ] **REQ-{id}**: [Requirement description]

## Out of Scope

- [Exclusion] — [why excluded]

## Traceability

| Requirement | Phase | Plan | Status |
|-------------|-------|------|--------|
| REQ-01 | 1 | 1 | [ ] |
| REQ-02 | 1 | 2 | [x] |
```

## REQ-ID Format

`[CATEGORY]-[NUMBER]`

Examples:
- AUTH-01, AUTH-02
- API-01, API-02, API-03
- UI-01, UI-02

## Good Requirements

| Good | Bad |
|------|-----|
| Specific and testable | Vague |
| User-centric ("User can X") | System-centric ("System does Y") |
| Atomic (one thing) | Multiple things |
| Independent (minimal deps) | Tightly coupled |

## Update Rules

- **doc-sync**: Mark completed requirements
- **plan-phase**: Map requirements to plans
- **verify-work**: Confirm requirements met

## ⚠️ Lifecycle Note

Requirements are **permanent** — never delete old requirements even if they change.
Keep the history to understand project evolution.
