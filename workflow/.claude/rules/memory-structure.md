# Memory Structure

Navigation guide — always in context. Tells PA what to load and when.

---

## Session Start Ritual

Run every session, in order:

1. Read `docs/project.md` → orient to project and user
2. Read `docs/.pa/state.md` → orient to current phase and task
3. Check `docs/.pa/concerns/` → any open issues before starting?
4. If no `docs/project.md` → run init action immediately

---

## Load On Demand

| Situation | Load |
|-----------|------|
| Architectural question or design decision | `docs/architecture/` |
| Setup or environment question | `docs/setup.md` |
| Usage or interface question | `docs/usage/` |
| Before making an important decision | `docs/decisions/` |
| Similar situation encountered before | `docs/.pa/learnings/` |
| Working on a specific feature | `docs/features/{name}/` |
| System design question (this plugin) | `docs/system/` |

---

## CLOSE Ritual

Before ending any operational session:

1. Ask: *What in docs/ changed this session?*
2. Update every stale section — features, usage, architecture, setup
3. Write new decisions → `docs/decisions/{date}-{topic}.md`
4. Write new learnings → `docs/.pa/learnings/{topic}.md`
5. Write open concerns → `docs/.pa/concerns/CONCERN-{topic}.md`
6. Reset `docs/.pa/state.md`
7. Clear `docs/.pa/worker-reports/`

---

## docs/ Layout

```
docs/
├── project.md        [BASE · always load]
│
├── [organic]         created when real content exists
│   ├── setup.md
│   ├── usage/
│   ├── architecture/
│   ├── decisions/
│   └── [detail layer]/
│
└── .pa/
    ├── state.md          [BASE · STM]
    ├── learnings/        [BASE]
    ├── concerns/         [BASE]
    └── worker-reports/   [BASE · STM]
```

Project type guides → `project-types/` — load during init only.
