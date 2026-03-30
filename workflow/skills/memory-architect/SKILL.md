---
name: memory-architect
description: Use when initializing project memory (op=init) or syncing memory at session end (op=close). Owns all memory file creation, update, and cleanup.
---

# Memory Architect

Full memory lifecycle manager. PA dispatches this skill at most twice per session: init and CLOSE.

<hard_constraint never_override>
1. Never pre-create empty organic dirs — BASE structure only.
2. Always read reference files before creating or updating anything.
3. .claude/rules/memory-structure.md must be tailored to project type — never generic.
</hard_constraint>

---

## Input

Received from PA in task description:

```
op: init | close
project_root: <absolute path to user's project>

# op=init only:
project_info: <what PA gathered — vision, goals, constraints, tech>
project_type: <web-app|ai-ml|cli-tool|plugin|research|learning|unknown>

# op=close only:
changes: <what changed this session — features, decisions, patterns, open issues>
```

---

## Thinking Model

```
op=init  → Step 1 → Step 2 (if unknown) → Step 3 → Step 4 → Step 5
op=close → Step 1 → Step 6 → Step 7
```

---

## Step 1 — Read references (always first)

Read:
- `references/core.md`
- `references/organic.md`

If project_type is known, also read:
- `project-types/{project_type}.md`

---

## Step 2 — Detect project type (op=init, project_type=unknown only)

1. `ls {project_root}` — top-level structure
2. Read key files: `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `README*`, `.claude-plugin/plugin.json`, `requirements.txt`
3. Check presence of: `src/`, `app/`, `experiments/`, `topics/`, `flows/`
4. Classify: `web-app` | `ai-ml` | `cli-tool` | `plugin` | `research` | `learning`
5. Read `project-types/{detected_type}.md`

---

## Step 3 — Create BASE docs/ structure (op=init)

Read templates: `templates/project.md`, `templates/state.md`

Create:
```
{project_root}/docs/
├── project.md       ← fill from project_info — no placeholders for known fields
└── .pa/
    ├── state.md     ← phase: UNDERSTAND, session goal: initial orientation
    ├── learnings/
    ├── concerns/
    └── worker-reports/
```

---

## Step 4 — Generate .claude/rules/memory-structure.md (op=init)

Create `{project_root}/.claude/rules/memory-structure.md`.

Read `references/organic.md` for the generation template.
Substitute type-specific Load On Demand rows for the detected project type.

---

## Step 5 — Write worker report (op=init)

Write `{project_root}/docs/.pa/worker-reports/memory-architect-init.md`:
- Project type detected (and how)
- What was created
- key_findings: anything notable PA should know

Return summary to PA:
`Memory initialized. Type: {type}. project.md + .pa/ + .claude/rules created.`
Include key_findings if non-trivial so PA can ask user targeted questions.

---

## Step 6 — Sync docs/ (op=close)

For each item in `changes`:

| Change type | Action |
|-------------|--------|
| Feature added/changed | Update `docs/project.md` Features + `docs/usage/` if public-facing |
| Architecture changed | Create/update `docs/architecture/` |
| Important decision made | Write `docs/decisions/{date}-{topic}.md` |
| Pattern discovered | Write `docs/.pa/learnings/{topic}.md` using `templates/learning.md` |
| Issue surfaced | Write `docs/.pa/concerns/CONCERN-{topic}.md` using `templates/concern.md` |
| Milestone reached | Update `docs/project.md` Current milestone |

Only update files where content actually changed.

---

## Step 7 — Reset STM (op=close)

1. Overwrite `docs/.pa/state.md` with blank from `templates/state.md`
2. Delete all files in `docs/.pa/worker-reports/` (keep dir)

Write worker report `docs/.pa/worker-reports/memory-architect-close.md` before clearing:
- What was synced, files updated

Return: `Memory synced. {N} docs updated. STM cleared.`
