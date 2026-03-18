# Spec Amend Phase

Amend existing spec when requirements change.

## When to Enter

- User says: "thay đổi", "update", "modify", "thêm requirement"
- Existing spec needs modification
- Scope expansion/contraction

## Inputs Needed

1. **Existing spec** - `docs/specs/<slug>/spec.md`
2. **Proposed changes** - What user wants to change
3. **Impact analysis** - How changes affect existing FRs/SCs

## Process

### 1. Load Existing Spec

```
Read: docs/specs/<slug>/spec.md
```

### 2. Analyze Changes

For each proposed change:
- Does it add/remove/modify FRs?
- Does it affect SCs?
- Does it change scope?

### 3. Draft Amendment

Update spec with changes:

```markdown
## Changes

### Change 1: <description>
- Before: <old>
- After: <new>
- Impact: <affected FRs/SCs>

### Change 2: <description>
...
```

### 4. Re-validate

Check:
- [ ] All FRs still have SCs
- [ ] New FRs have SCs
- [ ] Scope updated correctly
- [ ] Status: draft (need re-approval if major)

### 5. Present for Approval

```
**Spec Amendment: <slug>**

Changes:
- <change 1>
- <change 2>

Approve to lock, or tell me what to change.
```

## Types of Amendments

| Type | Action |
|------|--------|
| Minor (fix typo, clarify) | Update directly, note in spec |
| Medium (add FR, refine SC) | Update, re-validate |
| Major (change scope) | Set to draft, re-approve |

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| Spec amendment | `docs/specs/<slug>/spec.md` |
| Related features | `docs/features/<name>.md` |

## Output

- Updated spec with changes documented
- Re-approval if major changes

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Amendment approved | `plan.md` (nếu cần task mới) |
| Minor change | Continue to `execute.md` (nếu đang trong flow) |
| Need clarification | Ask user |
