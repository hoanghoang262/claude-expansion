# Memory Organic Layer

Rules for creating project-type-dependent docs/ structure.

---

## Rule

Never pre-create. Create only when real content exists.

PA derives structure from project type detected during init.
Full project type guides at: `project-types/{type}.md`

---

## Natural Unit by Project Type

| Type | Natural unit folder | Unit files |
|------|--------------------|----|
| `web-app` | `features/{name}/` | `requirements.md`, `spec.md` |
| `ai-ml` | `experiments/{name}/` | `hypothesis.md`, `results.md` |
| `cli-tool` | `flows/{name}/` | `spec.md` |
| `plugin` | `components/{name}/` | `requirements.md`, `spec.md` |
| `research` | `experiments/{name}/` | `findings.md`, `sources.md` |
| `learning` | `topics/{name}/` | `notes.md`, `progress.md` |

Create the natural unit folder when the first real feature/experiment/topic is defined — not before.

---

## Common Organic Sections

Create these when content warrants:

| Content | Create |
|---------|--------|
| Non-trivial install or run | `setup.md` |
| Public API, CLI, UI flows | `usage/` |
| System design, DB schema | `architecture/` |
| Important architectural choices | `decisions/{date}-{topic}.md` |

---

## .claude/rules/memory-structure.md Generation Template

Use this structure, substituting the type-specific rows:

```markdown
# Memory Structure

Navigation guide — always in context.

---

## Session Start Ritual

1. Read `docs/project.md` → orient to project and user
2. Read `docs/.pa/state.md` → orient to current phase and task
3. Scan `docs/.pa/concerns/` → any open issues?
4. No `docs/project.md` → run init immediately

---

## Load On Demand

| Situation | Load |
|-----------|------|
| Architectural question | `docs/architecture/` |
| Setup or environment | `docs/setup.md` |
| Important past decision | `docs/decisions/` |
| Similar problem before | `docs/.pa/learnings/` |
{TYPE_SPECIFIC_ROWS}

---

## CLOSE Ritual

Before ending any operational session:

1. Collect what changed this session (features, decisions, patterns, issues)
2. Dispatch memory-architect (op=close) with the changes
3. Memory-architect syncs docs/, writes learnings/decisions/concerns, resets STM
```

Type-specific rows by project type:

| Type | Rows to add |
|------|------------|
| `web-app` | `\| Working on a feature \| docs/features/{name}/ \|` + `\| API or UI flow \| docs/usage/ \|` |
| `ai-ml` | `\| Working on an experiment \| docs/experiments/{name}/ \|` + `\| Model info \| docs/models/ \|` |
| `cli-tool` | `\| Working on a command flow \| docs/flows/{name}/ \|` |
| `plugin` | `\| Working on a component \| docs/components/{name}/ \|` + `\| System design \| docs/system/ \|` |
| `research` | `\| Working on an experiment \| docs/experiments/{name}/ \|` + `\| Findings or sources \| docs/findings/, docs/sources/ \|` |
| `learning` | `\| Working on a topic \| docs/topics/{name}/ \|` |
