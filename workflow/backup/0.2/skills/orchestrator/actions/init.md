# init

Bootstrap project memory. Agents write docs directly as they work.

<hard_constraint never_override>
- Run ALL steps in order: Step 0 → Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6.
- Init is NOT complete until Step 6 (user confirms). Do not return to user's original request before Step 6.
- No skipping steps. "Enough info to answer" is NOT a valid reason to skip Step 3 or later.
- No user confirmation between steps — proceed automatically through all steps.
</hard_constraint>

---

## Mode: new (no code)

User doesn't have full clarity yet — PM leads the conversation to help user discover their own vision.

**Step 1 — PM-led discovery (AskUserQuestion, 2-3 rounds):**

Round 1 — about the PROBLEM, not the solution:
- "What problem are you trying to solve? Who experiences it?"
- "What do people do today without your solution?"

Round 2 — about success and scope:
- "What would success look like in 4 weeks?"
- "What's the one thing that must work on day one?"

Round 3 (if needed) — about constraints:
- "Any tech preferences or constraints I should know?"

**Step 2 — PM infers project type** from conversation signals:
- Feature-based (web/app/system) / Research / Learning / Script-tool / Config / Other

**Step 3 — Create minimal appropriate docs/ structure:**
```bash
python3 {scripts_dir}/create_docs_structure.py \
  --project-root "{project_root}" --project-name "{name}"
```
Then write directly:
- `docs/project.md` — using `templates/project-template.md`, filled with understanding from Step 1
- `.claude/rules/memory-structure.md` — using `templates/memory-structure-template.md`
- `.claude/rules/constitution.md` — using `templates/constitution-template.md`

**Step 4 — Present and confirm:**
```
🏗️ Init complete — mode: new

📄 docs/project.md — {project type} · goal: {one line}
📋 .claude/rules/  — memory map + conventions

Does this capture what you have in mind? Any corrections?
```

User confirms → clarify Part 2.

---

## Mode: existing (code found)

### Step 0 — Skeleton

```bash
python3 {scripts_dir}/create_docs_structure.py \
  --project-root "{project_root}" --project-name "{name}"
```

Creates: `project.md`, `state.md`, `docs-map.md` (placeholder), `decisions/`, `concerns/`

---

### Step 1 — General agent

**Announce:** `🏗️ **Init** — mode: existing · {N} features detected → writing project.md + docs-map + foundations`

Spawn **`codebase-surveyor`** agent (defined in `workflow/agents/codebase-surveyor.md`):

```
PROJECT_ROOT: {absolute path to project root}
TEMPLATES_DIR: {absolute path to this skill's templates/ directory}
```

PM writes directly (before dispatching feature agents):

- `.claude/rules/constitution.md` — from `templates/constitution-template.md`
- `.claude/rules/memory-structure.md` — from `templates/memory-structure-template.md`

> **Resolve before dispatching:** Replace `{templates_dir}` with the absolute path to this skill's `templates/` directory. Replace `{scripts_dir}` with the absolute path to this skill's `scripts/` directory.

---

### Step 2 — Create structure

```bash
python3 {scripts_dir}/create_docs_structure.py \
  --project-root "{project_root}" --docs-map "docs/docs-map.md"
```

Reads YAML block → creates feature directories + empty stub files.

---

### Step 3 — Feature agents

> **Checkpoint:** MANDATORY — do not skip regardless of task type or how much info was already gathered in Step 1. "Already have enough info" is NOT valid reason to skip.

PM reads `docs-map.md` → for each feature with `interface: user` or `developer`:

Spawn **`reverse-doc`** agent (defined in `workflow/agents/reverse-doc.md`):

```
FEATURE: {name}
INTERFACE: {user | developer | internal}
BACKEND: {backend path}
FRONTEND: {frontend path | none}
DOCS_TARGET: docs/features/{name}/
TEMPLATES_DIR: {absolute path to this skill's templates/ directory}
```

<hard_constraint never_override>
One agent per feature — do NOT group multiple features into one agent.
Run ALL feature agents in FOREGROUND. Do NOT use run_in_background.
No concurrency limit here — the "max 5 concurrent" rule is for execute phase only.
Wait for ALL to complete before Step 4.
</hard_constraint>

---

### Step 4 — Verify

Read `docs-map.md` → get expected feature list. Cross-check:

```bash
find docs -name "*.md" -not -path "*/.tmp/*" | sort
```

Every `features:` entry must have all its required docs.
Missing → spawn gap agent. **Do NOT report to user until 100% match.**

---

### Step 5 — Sync memory-structure.md

Read `docs-map.md` YAML block → update the **Project Structure** section of `.claude/rules/memory-structure.md` with the actual features and foundations discovered.

This makes `memory-structure.md` the always-in-context navigation guide. Model no longer needs to read `docs-map.md` for navigation — only tooling does.

---

### Step 6 — Report

Present via AskUserQuestion:

```
Init complete

docs/:
  project.md    — {type}, {stack}
  docs-map.md   — {N} features, {M} foundations
  features/     — {list}
  foundations/  — {list}

.claude/rules/: {list}

Review docs-map.md and correct anything wrong.
```

User confirms → clarify Part 2.
