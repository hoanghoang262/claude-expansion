# Orchestrator Docs — Overview

## Role

This is the **physical memory** of the project. Orchestrator reads and writes here instead of relying on conversation history.

## Three Memory Layers

```
PERMANENT  (never delete)
  PROJECT.md, features/*, standards/*, research/*, concerns/*

VERSION    (delete on Version Release)
  ROADMAP.md, worker-reports/*

SESSION    (reset after each phase)
  STATE.md
```

## Folder Structure

```
docs/
├── [PERMANENT]
│   ├── PROJECT.md                  ← Vision, goals
│   ├── features/                  ← One folder per feature
│   │   └── {id}-{name}/
│   │       ├── requirement.md     ← User stories, success criteria
│   │       ├── spec.md            ← Technical design
│   │       ├── PLAN.md           ← Micro-tasks + waves (after planning)
│   │       └── UAT.md            ← User acceptance test log
│   ├── standards/                   ← Supreme rule set
│   │   ├── CONVENTIONS.md        ← Coding style, naming
│   │   ├── STRUCTURE.md          ← Folder structure
│   │   ├── STACK.md             ← Tech stack
│   │   └── TESTING.md           ← Testing strategy
│   ├── research/                    ← Technology knowledge
│   └── concerns/                    ← Technical debt, risks
│
├── [VERSION]
│   ├── ROADMAP.md               ← Version phases (delete on release)
│   └── worker-reports/             ← Handover context (delete on release)
│       └── {feature-id}/
│           └── {task}.json
│
├── [SESSION]
│   └── STATE.md                  ← State (reset after phase)
│
└── [ARCHIVE]
    └── versions/
        └── v{x}.md             ← Release report
```

## Who Reads, Who Writes, When

| File | Created by | Updated by | Deleted by |
|------|------------|-----------|------------|
| PROJECT.md | initialize | doc-sync | Never |
| features/*/requirement.md | discuss-phase | - | Never |
| features/*/spec.md | discuss-phase | doc-sync | Never |
| features/*/PLAN.md | plan-phase | - | Never |
| features/*/UAT.md | verify-work | doc-sync | Never |
| standards/* | initialize + doc-sync | doc-sync | Never |
| research/* | plan-phase | - | Never |
| concerns/* | Orchestrator | Orchestrator | Never |
| ROADMAP.md | initialize | doc-sync | Version Release |
| worker-reports/* | execute-phase | - | Version Release |
| STATE.md | initialize + doc-sync | Orchestrator | doc-sync (reset) |
| versions/* | Version Release | - | Never |

## Templates

See `templates/` directory:

- `PROJECT-template.md` — Project.md template
- `REQUIREMENTS-template.md` — Requirement.md template
- `ROADMAP-template.md` — Roadmap.md template
- `STATE-template.md` — STATE.md template
- `PLAN-template.md` — PLAN.md template
- `CONCERNS-template.md` — Concerns.md template
- `STRUCTURE-template.md` — Structure standards template
- `CONVENTIONS-template.md` — Conventions standards template
- `TESTING-template.md` — Testing standards template
- `STACK-template.md` — Stack standards template

## How Orchestrator Works

```
1. Session Start
   → Read STATE.md → Know current position
   → Read PROJECT.md → Know project goals

2. Discuss Phase
   → Create features/{id}/requirement.md
   → Create features/{id}/spec.md

3. Plan Phase
   → Create features/{id}/PLAN.md
   → Research → docs/research/

4. Execute Phase
   → Spawn Executor subagents
   → Create worker-reports/

5. Verify Phase
   → Create features/{id}/UAT.md

6. Doc-Sync
   → Update all permanent docs
   → Reset STATE.md
   → Delete worker-reports/ (on Version Release)
```
