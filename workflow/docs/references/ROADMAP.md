# ROADMAP.md Reference

## Purpose

Phases and success criteria for the current version. **Lifespan: VERSION (version-scoped) — DELETE ON VERSION RELEASE.**

## Lifecycle

```
Created by:
  └── initialize

Updated by:
  └── doc-sync (mark phases complete)

Deleted by:
  └── Version Release Event (→ archived to versions/v{x}.md)
```

## Structure

```markdown
# [Project Name] — Roadmap

**Lifespan: VERSION — DELETE ON VERSION RELEASE**

## Milestone: v1

| # | Phase | Goal | Requirements | Criteria |
|---|-------|------|--------------|----------|
| 1 | Auth | Login/logout | REQ-01 | 3 |
| 2 | User Profile | Profile CRUD | REQ-02 | 2 |
| 3 | Dashboard | Main UI | REQ-03, REQ-04 | 4 |

## Phase Details

### Phase 1: [Name]

**Goal:** [What this phase delivers]

**Requirements:** REQ-01, REQ-02

**Success Criteria:**
1. [Observable behavior 1]
2. [Observable behavior 2]
3. [Observable behavior 3]

### Phase 2: [Name]
...
```

## Phase Success Criteria

Good criteria are:
- **Observable** — user can verify (not internal implementation)
- **Specific** — not vague ("response < 200ms" not "fast")
- **Complete** — covers main outcomes

## Update Rules

- **initialize**: Create phases from requirements
- **doc-sync**: Mark completed phases with ✓
- **Rarely updated after creation**

## ⚠️ Version Release Policy

When user commits "Release V1.0":

```
1. Read ROADMAP.md → Summarize all phases
2. Create: docs/versions/v1.0.md with summary content
3. CLEAR docs/ROADMAP.md
4. Delete all docs/worker-reports/
5. System ready for next version
```

## ⚠️ KEEP vs DELETE After Version Release

```
KEEP:
  docs/features/*              ← Specs are permanent
  docs/standards/*             ← Standards are permanent
  docs/research/*              ← Research is permanent
  docs/concerns/*              ← Concerns are permanent
  docs/PROJECT.md              ← Project vision is permanent

DELETE:
  docs/ROADMAP.md             ← Reset for next version
  docs/worker-reports/*        ← No longer valuable after code goes to prod
```
