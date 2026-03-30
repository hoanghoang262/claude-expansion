# Memory System

How PA memory is structured, grows, and is used across sessions.

---

## The Core Idea

`docs/` is dual-purpose: PA's externalized brain AND living documentation for humans.
PA writes it. Humans read it. Both benefit from it being accurate and current.

The goal: **each session, PA knows more than the last. Each change, docs stay in sync.**

---

## Two Scopes

```
docs/                        ← Project scope
│                               PA writes it. Humans read it.
│                               Contains project truth.
│
└── .pa/                     ← PA internal scope
                                PA's brain. Humans can read but it's PA's perspective.
                                Contains state, learnings, concerns.
```

---

## Two Memory Types

```
STM — Short-Term Memory
  Resets after each work cycle.
  docs/.pa/state.md          current phase, task, progress
  docs/.pa/worker-reports/   agent outputs (transient)

LTM — Long-Term Memory
  Permanent. Grows over time. Never reset.
  docs/project.md            overview, features, tech, user, goals
  docs/decisions/            why important choices were made (if exists)
  docs/[organic]/            project-specific content (setup, usage, architecture...)
  docs/.pa/learnings/        patterns PA has accumulated
  docs/.pa/concerns/         issues PA is tracking
```

---

## docs/ Structure

```
docs/
├── project.md          [BASE · LTM] always exists
│
├── [organic · LTM]     created when real content exists
│   ├── decisions/      when important choices are made (ADR)
│   ├── setup.md
│   ├── usage/
│   ├── architecture/
│   ├── specs/          [VERSION — delete on release]
│   └── [detail layer]/ mirrors project natural structure
│
└── .pa/
    ├── state.md        [BASE · STM] always exists — reset each cycle
    ├── learnings/      [BASE · LTM] always exists
    ├── concerns/       [BASE · LTM] always exists
    └── worker-reports/ [BASE · STM] always exists — clear at CLOSE
```

---

## Detail Layer — Organic Growth

PA observes the project, infers the natural unit, creates structure that mirrors it:

```
Web / mobile app    →  features/{name}/
Plugin / tool       →  components/{name}.md
AI / ML project     →  models/, pipelines/
Research            →  findings/, sources/
Script / automation →  tasks/, flows/
```

Names are guidance — PA derives actual names from the project.

---

## Sync Rule — CLOSE Phase

When work changes anything user-facing or structural:

| Work done | Update |
|---|---|
| Feature added / changed | `project.md` + `usage/` |
| Setup changed | `setup.md` |
| Architecture changed | `architecture/` |
| Important choice made | `decisions/{date}-{topic}.md` |
| Pattern discovered | `.pa/learnings/{topic}.md` |
| Issue surfaced | `.pa/concerns/CONCERN-{topic}.md` |

PA does not close without asking: *What in docs/ is now stale?*

---

## How PA Reads Memory

```
Every session (always):
  docs/project.md           orient to user and project
  docs/.pa/state.md         orient to current position
  docs/.pa/concerns/        check for open issues

On demand:
  docs/decisions/           before making a related decision
  docs/.pa/learnings/       when similar situation arises
  docs/setup.md             setup or environment question
  docs/usage/               usage or interface question
  docs/architecture/        system design decision
  docs/[detail]/            working on specific component or feature
  docs/system/              architectural or memory system question
```

---

## Consolidation

After any completed work:

> "Will I need this in a future session?"

| Situation | Action |
|-----------|--------|
| Conversational, nothing strategic | Skip |
| Important choice made | Write → `decisions/` |
| Pattern discovered | Write → `.pa/learnings/` |
| Issue surfaced | Write → `.pa/concerns/` |
| BUILD cycle complete | Full sync — update all stale docs sections |
