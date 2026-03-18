# Doc Sync Phase

Update documentation to reflect changes. Docs is xương sống — always sync.

## When to Enter

- After verify passed
- User says: "docs", "tài liệu", "update docs"
- Any significant change made

## Principle: Docs is Xương Sống

**Docs are NOT phase cuối — docs are xuyên suốt.**

Every phase should update relevant docs. This phase is for:
- Final sync
- Cross-reference updates
- Changelog

## Process

### 1. Identify Changed Areas

Based on what was done:
- New features → `docs/features/`
- Architecture changes → `docs/architecture/`
- API changes → Update relevant docs
- Bug fixes → Update if needed

### 2. Update Docs

**Feature Docs:**
```markdown
## Feature: <name>

### Overview
<what it does>

### Usage
<how to use>

### Related
- Spec: `docs/specs/<slug>/spec.md`
- Code: `<file paths>`
```

**Architecture Docs:**
```markdown
## <Component>

### Purpose
<why it exists>

### Structure
<key files>

### Dependencies
<what it depends on>
```

### 3. Update Changelog

If project uses changelog:
```markdown
## [Unreleased]

### Added
- <feature> — <description>

### Fixed
- <bug> — <description>
```

### 4. Cross-Reference

Ensure docs reference each other:
- Spec → Feature docs
- Feature docs → Spec
- Architecture → Related features

## Doc Structure Recommendation

```
docs/
├── PROJECT.md              ← Entry point
├── README.md               ← Overview
├── architecture/
│   ├── overview.md        ← System overview
│   └── components/         ← Component docs
├── features/
│   ├── feature-a.md
│   └── feature-b.md
├── specs/
│   └── <slug>/
│       └── spec.md
├── adr/                   ← Architecture decisions
└── changelog.md
```

## Docs Responsibility (this phase)

| Action | Docs to update |
|--------|----------------|
| Feature implemented | `docs/features/<name>.md` |
| Architecture changed | `docs/architecture/` |
| API changed | Relevant API docs |
| Bug fixed | If user-facing, update |
| General | `docs/changelog.md` |

## Output

- All relevant docs updated
- Cross-references intact
- Ready for merge

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Docs synced | Done — report to user |
| Missing info | Ask user |
| Need research | `research.md` |
