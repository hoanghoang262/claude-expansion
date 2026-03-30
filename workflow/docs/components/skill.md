# Component: PA Skill

The orchestrator skill — entry point for everything PA does.

---

## Entry Point

`skills/orchestrator/SKILL.md` — loaded at session start via plugin.

---

## Current SKILL.md Structure

### Persona
Single prose paragraph — captures character, not just role.

```
A trusted assistant, not a task executor. Invests in understanding
the user as a person... Runs work in background without going silent.
Direct, always has a recommendation. Quality over speed.
```

### Hard Constraints
5 rules that cannot be overridden:
1. No `docs/project.md` → run init action first
2. All questions → AskUserQuestion tool
3. Never ask for information already in docs/
4. Load action procedures before executing (Read `actions/{action}.md`)
5. Code changes → implementer agent (exception: clearly-bounded, no design decision)

### Cognitive Model
Orient (state.md + project.md) → Classify (Conversational vs Operational) → Act

### Phase Registry
4-phase cycle: UNDERSTAND → BUILD → VERIFY → CLOSE
Each phase described as prose with PA's job + activities + exit condition.

### Action Catalog
5 actions triggered by situation:
`init` / `research` / `spec` / `plan` / `debug`

### Reference Pointers
- `references/memory-guide.md` — docs/ structure
- `references/concern-resolution.md` — escalation tiers
- `references/announcements.md` — communication protocol

---

## Actions Directory

```
actions/
├── init.md       ← bootstrap project memory (new vs existing project)
├── research.md   ← fill information gaps in UNDERSTAND
├── spec.md       ← formal definition for complex tasks, requires approval
├── plan.md       ← task breakdown into parallel waves for BUILD
└── debug.md      ← failure diagnosis in VERIFY
```

---

## References Directory

```
references/
├── memory-guide.md        ← docs/ structure + sync rules
├── announcements.md       ← communication protocol
└── concern-resolution.md  ← Tier 1/2/3 escalation lifecycle
```
