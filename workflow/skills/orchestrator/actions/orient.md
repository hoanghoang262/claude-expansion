# orient — Orientation & State Recovery

## Step 1: Find project root

```
Walk up from cwd to find docs/ directory.
If found → project_root = parent of docs/
If not found → no project yet → → discuss (new project)
```

## Step 2: Read existing docs (in parallel)

```
docs/PROJECT.md          ← exists? → project is initialized
docs/STATE.md           ← exists? → read current state
docs/ROADMAP.md         ← what's planned
docs/features/          ← what exists
docs/concerns/          ← open concerns
```

## Step 3: Classify situation

```
docs/PROJECT.md absent?
  → New project → scaffold docs/ (see Init Scaffold below)
  → Present to user: "New project initialized. What's the goal?"

STATE.md absent or corrupted?
  → Re-orient via ROADMAP.md + features/
  → Write clean STATE.md (see below)

docs/ exists, STATE.md says "ready"?
  → Read user request → SELECT next action
```

## Step 4: Write clean STATE.md

```markdown
# {Project Name} — State

## Project

Name: {name}
Path: {project_root}
Last Reset: {date}

## Session Continuity

Last session: {timestamp}
Status: ready
```

Use `templates/state-template.md`.

## Step 5: Select next action

Based on what exists in docs/:

| Situation                               | Next Action       |
| --------------------------------------- | ----------------- |
| No features in ROADMAP                  | `discuss`         |
| Features in ROADMAP, no requirement yet | `discuss`         |
| Requirement exists, no spec             | `spec`            |
| Spec exists, not approved               | `spec`            |
| Spec approved, no PLAN                  | `plan`            |
| PLAN exists, worker-reports incomplete  | `execute`         |
| Worker-reports complete, no UAT         | `verify`          |
| UAT all pass                            | `doc-sync`        |
| All features done                       | `version-release` |

## Init Scaffold

Create automatically when docs/PROJECT.md is absent. Do not ask the user first.

```
docs/
├── PROJECT.md           ← empty skeleton
├── ROADMAP.md          ← empty
├── STATE.md            ← orient result
├── standards/
│   ├── CONVENTIONS.md
│   ├── STRUCTURE.md
│   ├── TESTING.md
│   └── GIT_FLOW.md
├── research/           ← empty
├── concerns/           ← empty
├── versions/           ← empty
└── features/           ← empty
```
