# Action: Init

Triggered when: no `docs/project.md` exists.

---

## Step 1 — Gather project info

**New project (no codebase):**
Ask user 3 questions max:
- What is this project?
- What do you want to achieve?
- Any constraints or preferences I should know?

**Existing project (has codebase):**
1. Spawn codebase-surveyor → scan project structure
2. Form hypotheses: project type, tech stack, current state
3. Ask 1-2 targeted questions to fill gaps

---

## Step 2 — Create base docs/

Always create this minimal structure — no exceptions:

```
docs/
├── project.md            ← from gathered info
└── .pa/
    ├── state.md          ← phase: UNDERSTAND
    ├── learnings/
    ├── concerns/
    └── worker-reports/
```

Organic layers (`setup.md`, `usage/`, `architecture/`, `decisions/`) are created only when real content exists — never pre-created empty.

---

## Step 3 — Detect project type

Classify into one of: `web-app` · `ai-ml` · `cli-tool` · `plugin` · `research` · `learning`

Load `project-types/{type}.md` — use it as guide for:
- What the natural unit folder is called (`features/`, `experiments/`, `topics/`...)
- What sections to fill in `docs/` for this project type

Do NOT pre-create natural unit folders — create them when first content exists.

---

## Step 4 — Return to UNDERSTAND

State: phase = UNDERSTAND, current work = initial orientation.
