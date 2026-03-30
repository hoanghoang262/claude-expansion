# Architecture

How the PA system works.

---

## Big Picture

```
                        ┌─────────────────────┐
                        │        USER         │
                        └──────┬──────────────┘
                               │ input
                               ▼
┌──────────────────────────────────────────────────────┐
│                          PA                          │
│                                                      │
│   ┌──────────────┐    ┌───────────────────────────┐  │
│   │    Memory    │───►│      Cognitive Model      │  │
│   │    docs/     │    │  Orient → Classify → Act  │  │
│   │              │◄───│                           │  │
│   └──────────────┘    └─────────────┬─────────────┘  │
│          ▲                          │ delegate        │
│          │ CLOSE                    │                 │
│          │ (consolidate + sync)     │                 │
└──────────┼──────────────────────────┼─────────────────┘
           │                          │
           │              ┌───────────┼───────────┐
           │              ▼           ▼           ▼
           │         [researcher] [implementer] [reviewer]
           │              └───────────┼───────────┘
           │                          │ output
           │                          ▼
           │                   PA verifies
           │                          │
           │              ┌───────────┴───────────┐
           │              │                       │
           │           PASS                     FAIL
           │              │                       │
           │              ▼                       │
           └──── update docs/          loop back to UNDERSTAND
                 clear STM                        │
                      │                           │
                      ▼                    ───────┘
               next session
               PA knows more
                      │
                      ▼
               ┌─────────────────────┐
               │   USER (session+1)  │  ← PA understands
               └─────────────────────┘    user better now
```

**The virtuous cycle:** every session PA learns → next session PA performs better → trust grows → user shares more context → PA learns more.

---

## Cognitive Model

Every input → PA does two things immediately:

```
1. Orient
   ┌─────────────────────────────────────┐
   │ Read state.md → where are we?       │
   │ Read project.md → who is the user?  │
   │ Check concerns/ → anything open?    │
   └─────────────────────────────────────┘

2. Classify
   Output needs to persist + be verifiable?
   ┌─── YES ──► Operational (4-phase cycle)
   └─── NO  ──► Conversational (respond directly)
```

### Conversational

```
User input → PA thinks → responds
                       → optionally asks 1 question to deepen context
Done in one response. No state change.
```

### Operational

```
User input → 4-phase cycle → persistent output
May span multiple sessions. Has state in docs/state.md.
```

---

## 4-Phase Cycle

```
  ┌──────────────────────────────────────────────────┐
  │                                                  │
  ▼                                                  │
UNDERSTAND ──► BUILD ──► VERIFY ──► CLOSE            │
  │                        │                         │
  │                        └── FAIL ─────────────────┘
  │                            (loop back)
  └── need more info ──► research action
```

| Phase | PA's job | Done when |
|---|---|---|
| UNDERSTAND | Know exactly what "done" looks like | Goal + constraints + done criteria clear |
| BUILD | Coordinate agents to produce output | All tasks claimed complete |
| VERIFY | Confirm output matches what was defined | Output verified, user informed |
| CLOSE | Leave project better than before | docs/ updated, STM clean |

**Depth adapts to complexity:**

```
Simple:  UNDERSTAND(5min) → BUILD(1 agent) → VERIFY(quick) → CLOSE(1 write)
Complex: UNDERSTAND(multi-session) → BUILD(parallel waves) → VERIFY(full QA) → CLOSE(full sync)
```

---

## Actions

Triggered by situation within a phase — not mandatory steps.

```
UNDERSTAND ──► init        (no project memory — runs first)
           ──► research    (need deeper info)
           ──► spec        (complex task needs formal definition + approval)

BUILD      ──► plan        (execution needs task breakdown into parallel waves)

VERIFY     ──► debug       (failure blocks progress)
```

---

## Agent Delegation

```
PA                          Agents
──                          ──────
Holds full context    ──►   researcher    (finds information)
Knows user deeply     ──►   implementer  (writes code)
Makes decisions       ──►   reviewer     (checks quality)
Verifies output       ──►   surveyor     (maps codebase)
Updates memory        ◄──   all agents return output + status
```

Rules:
- PA never writes code directly in BUILD phase
- Independent agents dispatched in parallel
- PA verifies all agent output before accepting

---

## Memory Overview

```
Session start          During work              Session end
─────────────          ────────────             ───────────
Load:                  Update realtime:         Consolidate + sync:
  project.md             state.md progress        decisions/
  state.md               concerns/ if issue       learnings/
  concerns/              worker-reports/          usage/, architecture/ if changed
                                                  Clear STM
```

See `docs/system/memory.md` for full memory system design.
