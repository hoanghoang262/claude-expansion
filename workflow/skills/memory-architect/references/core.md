# Memory Core

BASE structure and per-file lifecycle. Always apply regardless of project type.

---

## BASE Structure

Always create exactly this — no more, no less:

```
docs/
├── project.md          [LTM] — project truth, always exists
└── .pa/
    ├── state.md        [STM] — reset each session
    ├── learnings/      [LTM] — patterns PA accumulates
    ├── concerns/       [LTM] — open issues
    └── worker-reports/ [STM] — agent outputs, clear at CLOSE
```

Organic layer (`decisions/`, `setup.md`, `architecture/`, etc.) — created only when real content exists.

---

## Per-File Rules

### project.md

Template: `templates/project.md`

Sections:
- **Overview** — what, for whom, type, tech stack (core only), key features
- **User Context** — role, working style, communication preferences
- **Goals** — Current milestone (next few sessions) + Direction (long-term)
- **Constraints** — non-negotiables

Update `Current milestone` when a milestone is reached. Never pre-fill with guesses.

---

### state.md

Template: `templates/state.md`

Fields:
- **Phase** — UNDERSTAND | BUILD | VERIFY | CLOSE
- **Session Goal** — what this session set out to accomplish
- **Current Work** — specific task in progress right now
- **Progress** — `[x]` done, `[ ]` pending
- **Blockers** — active blockers; `- none` if clear
- **Open Questions** — unresolved unknowns; `- none` if clear

Reset completely at CLOSE. Never accumulate history here.

---

### concerns/CONCERN-{topic}.md

Template: `templates/concern.md`

Fields:
- **Status** — `open` → `investigating` → `resolved`
- **Tier** — always 2
- **Discovered** — session context or date
- **Affects** — which phase or component
- **Escalate if** — condition that would make this Tier 3

Naming: `CONCERN-{topic}` — topic-based, not numbered. Never delete — mark resolved, keep.

---

### learnings/{topic}.md

Template: `templates/learning.md`

Fields:
- **Confidence** — `high` | `medium` | `uncertain`
- **Applies when** — triggering context PA reads to decide relevance

Write at CLOSE when a pattern emerged that will affect future sessions. Never delete.

---

### worker-reports/{task}.md

Template: `templates/worker-report.md`

Fields:
- **Agent** — which agent produced this
- **Status** — `complete` | `partial` | `failed` | `blocked`
- **Output** — summary of results
- **Artifacts** — files created/modified
- **Concerns Logged** — links to any CONCERN-{topic}.md created

One file per delegated task. Clear entire folder at CLOSE.
