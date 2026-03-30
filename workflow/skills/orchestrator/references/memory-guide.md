# Memory Guide

How to structure and grow `docs/` per project.

---

## Structure

```
docs/                        ← Project scope (PA writes, humans read)
├── project.md               [BASE · LTM] always exists
└── [organic]                created when real content exists
    decisions/               when important choices are made (ADR)
    setup.md                 non-trivial install/run
    usage/                   interface layer (API, CLI, UI flows)
    architecture/            system design, schema, data flow
    specs/                   active feature specs [VERSION — delete on release]
    [detail layer]/          mirrors project natural structure

docs/.pa/                    ← PA internal scope
├── state.md                 [BASE · STM] always exists — reset each cycle
├── learnings/               [BASE · LTM] always exists — patterns PA accumulates
├── concerns/                [BASE · LTM] always exists — issues PA tracks
└── worker-reports/          [BASE · STM] always exists — agent outputs, clear at CLOSE
```

---

## docs/ organic layer — what to create when

| Content type | Create |
|---|---|
| Non-trivial install or run steps | `setup.md` |
| Public interface (API, CLI, UI flows) | `usage/` or `api.md` or `commands.md` |
| System design, DB schema, data pipeline | `architecture/` |
| Active feature spec requiring approval | `specs/{feature}.md` |
| Feature-oriented project | `features/{name}/` |
| Component-oriented project | `components/{name}.md` |
| AI/ML project | `models/`, `pipelines/` |
| Research project | `findings/`, `sources/` |
| Script/automation | `tasks/`, `flows/` |

PA derives structure from the actual project — names above are guidance, not prescription.

---

## project.md — what to capture

```
## Overview
- What is this? Problem it solves? For whom?
- Project type
- Tech stack (core only)
- Key features

## User Context
- Role, background, working style
- What matters most: quality / speed / learning / shipping

## Goals
- Current milestone
- Longer-term direction

## Constraints
- Non-negotiables, known limitations
```

---

## Sync rule — CLOSE phase

When work changes anything user-facing or structural, update before clearing STM:

| Work done | Update |
|---|---|
| Feature added / changed | `project.md` Features + `usage/` |
| Setup / dependencies changed | `setup.md` |
| Architecture changed | `architecture/` |
| Important choice made | `decisions/{date}-{topic}.md` |
| Pattern discovered | `docs/.pa/learnings/{topic}.md` |
| Issue surfaced | `docs/.pa/concerns/CONCERN-{topic}.md` |

PA does not close a session without asking: *What in docs/ is now stale?*

---

## STM vs LTM

| Ask | Answer |
|-----|--------|
| Will I need this next session? | YES → LTM |
| Only relevant to current task? | YES → STM or skip |
| Important choice with lasting impact? | YES → `decisions/` |
| Pattern worth remembering? | YES → `.pa/learnings/` |
| Issue that may affect future work? | YES → `.pa/concerns/` |
| Working data, agent outputs? | YES → `.pa/worker-reports/` |
