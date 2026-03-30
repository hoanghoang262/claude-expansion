# Action: Init

Triggered when: no `docs/project.md` exists.

Init is full project onboarding — understand the project deeply, help the user get started if needed, then capture that understanding in memory.

---

## Case A — No codebase (new project)

User has a vision but nothing built yet.

### Phase 1 — UNDERSTAND

PA asks user deeply. One question at a time. Never more than one at once.

Cover (not necessarily in this order — follow the conversation):
- What is this? What problem does it solve?
- Who is it for? What does success look like?
- Tech preferences? Stack, tools, constraints?
- Any timeline, team, or other constraints?

PA listens, follows up, until it genuinely understands the vision. 3–5 exchanges is normal.

### Phase 2 — BUILD foundation

Help the user get started with a concrete base. PA recommends — never presents blank options.

Depending on what was gathered:
- Software project → dispatch `implementer` to scaffold: git init, folder structure, config files, package manager setup, chosen stack
- Research/learning → propose structure, first topic/experiment skeleton
- Any type → make it concrete: something runnable or usable exists after this phase

### Phase 3 — CAPTURE

Dispatch agent with skill `memory-architect`:
```
Use skill memory-architect.
op: init
project_info: {everything PA gathered}
project_type: {detected from conversation}
project_root: {project_root from context}
```

---

## Case B — Codebase exists (existing project)

PA joins an in-progress project.

### Phase 1 — UNDERSTAND via memory-architect

Dispatch agent with skill `memory-architect`:
```
Use skill memory-architect.
op: init
project_type: unknown
project_root: {project_root from context}
```

memory-architect scans the codebase, creates docs/, and returns a worker-report with `key_findings`.

PA reads the worker-report. If key_findings reveal gaps PA cannot resolve from the codebase:
- Ask user 1–2 targeted questions only
- Update `docs/project.md` with answers

---

## After init

State: phase = UNDERSTAND, current work = initial orientation complete.

PA has context. Proceed to understand what the user wants to accomplish this session.
