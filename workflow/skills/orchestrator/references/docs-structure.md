# docs/ Folder Structure

All project memory lives here. Structure is the same regardless of project size.

```
docs/
├── [PERMANENT] PROJECT.md              Vision, goals, tech stack
├── [SESSION]   STATE.md                Current action/feature/wave (cleared after doc-sync)
├── [VERSION]   ROADMAP.md              Active milestones of this version
│
├── [PERMANENT] standards/
│   ├── GIT_FLOW.md                     Branch strategy
│   ├── STRUCTURE.md                    Folder/file conventions
│   ├── TESTING.md                      Test types, coverage
│   └── CONVENTIONS.md                  Naming, syntax rules
│
├── [PERMANENT] research/               Technology evaluations
├── [PERMANENT] concerns/               Technical debt log
├── [ARCHIVE]   versions/               Release reports
│
├── [VERSION]   worker-reports/         Machine-readable handover
│   └── {feature-id}/
│       └── TASK-{N}.json
│
└── [PERMANENT] features/
    └── {id}/
        ├── requirement.md              User stories, acceptance criteria
        ├── spec.md                     Technical design, data model, API
        ├── PLAN.md                     Micro-tasks with waves
        └── UAT.md                      Test checklist
```

## Lifespan Labels

| Label | Meaning |
|---|---|
| `[PERMANENT]` | Never delete. Accumulates across all versions. |
| `[VERSION]` | Delete on Version Release Event. |
| `[SESSION]` | Reset after every doc-sync. One session = one feature workflow. |
| `[ARCHIVE]` | Never delete. Historical records only. |
