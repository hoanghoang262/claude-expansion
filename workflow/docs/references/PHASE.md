# Phase Docs Reference

## Purpose

Track work for each phase.

## Lifecycle Labels

See `references/memory-lifecycle.md` for full lifespan explanation of each file.

## File Naming

```
docs/features/{id}-{name}/
├── requirement.md    # discuss-phase output (PERMANENT)
├── spec.md          # discuss-phase output (PERMANENT)
├── PLAN.md         # plan-phase output (PERMANENT)
├── UAT.md          # verify-work output (PERMANENT)
└── SUMMARY.md      # execute-phase output (PERMANENT)

docs/worker-reports/{feature-id}/
└── {task}.json     # execute-phase output (VERSION - delete on release)
```

## Created By

| File | Created by | Lifespan |
|------|-----------|----------|
| requirement.md | discuss-phase | PERMANENT |
| spec.md | discuss-phase | PERMANENT |
| PLAN.md | plan-phase | PERMANENT |
| UAT.md | verify-work | PERMANENT |
| worker-reports/* | execute-phase | VERSION |

## Phase Flow

```
discuss-phase
  → Create requirement.md + spec.md
  → docs/features/{id}/

plan-phase
  → Create PLAN.md
  → docs/features/{id}/

execute-phase
  → Create worker-reports/
  → docs/worker-reports/{id}/

verify-work
  → Create UAT.md
  → docs/features/{id}/

doc-sync
  → Update all → reset STATE.md
```
