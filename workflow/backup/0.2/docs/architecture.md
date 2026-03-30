# Architecture — Workflow Plugin Orchestrator

> Mô tả thiết kế hệ thống hiện tại (v0.3).
> Cập nhật khi có thay đổi kiến trúc quan trọng.

---

## Tổng quan

```
┌─────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATOR                             │
│                                                                 │
│   ┌─────────────┐    ┌──────────────────┐    ┌─────────────┐   │
│   │   MEMORY    │───▶│       PM         │───▶│   AGENTS    │   │
│   │  (docs/)    │    │  (UNDERSTANDING  │    │  (workers)  │   │
│   │  STM + LTM  │◀───│    machine)      │    │  stateless  │   │
│   └─────────────┘    └──────────────────┘    └─────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**PM** là entity duy nhất nắm giữ toàn bộ context. Không code, không analyze code — chỉ hiểu, quyết định, điều phối.

**Agents** là stateless workers. Nhận đủ context từ PM, thực thi, trả kết quả. Không cần nhớ gì giữa các lần dispatch.

**Memory (docs/)** là external brain của PM. Tích lũy understanding qua thời gian. Không có docs/ → PM bắt đầu lại từ đầu mỗi session.

---

## Triết lý cốt lõi

### Understanding-first, không phải process-first

PM không follow pipeline. PM **hiểu user + project** → chọn process phù hợp.

```
Sai (v0.2):  mọi task → clarify → spec → plan → execute
Đúng (v0.3): understand fully → process emerges from understanding
```

### PM = UNDERSTANDING machine

PM hiểu ba thứ:
- **User**: goal thực sự, working style, expectations
- **Project**: type, constraints, what exists, history
- **Current state**: where are we, what was done, what remains

Từ ba thứ này → PM quyết định process nào phù hợp → delegate đúng agent.

---

## Hai Phase

```
UNDERSTAND → ACT
```

**UNDERSTAND:** PM + user. Mục tiêu: PM có đủ context để define "done."
**ACT:** PM điều phối agents. Mục tiêu: deliver đúng cái đã understand.

RESPOND và DIRECT thường resolve trong UNDERSTAND mà không cần sang ACT.

---

## Mode Patterns

PM nhận ra pattern từ understanding intent, không phải từ request text.

| Pattern | Khi nào | PM làm gì | Agents |
|---------|---------|-----------|--------|
| **RESPOND** | User cần insight, explanation, analysis — không cần persistent output | Think → respond. Consolidate nếu strategic. | Researcher nếu cần |
| **DIRECT** | Nhỏ, rõ ràng, không cần design decision | Confirm scope → act immediately | Có thể 1 agent |
| **BUILD** | Phức tạp, multi-step, output quan trọng và persistent | Full UNDERSTAND → ACT cycle | Full pipeline |

Patterns nest và transition: RESPOND context → carry vào BUILD nếu user quyết định implement.

**Research** là capability (spawn researcher agent), không phải pattern — dùng trong bất kỳ mode nào.

---

## Memory Model

Dựa trên human memory: STM + LTM + Consolidation.

### STM — Working memory (cleared after work cycle)

```
docs/state.md          ← phase hiện tại, action đang làm
docs/worker-reports/   ← task outputs (tạm thời)
```

### LTM — Accumulated understanding (permanent)

```
docs/project.md        ← identity: user, goals, project type
docs/decisions/        ← committed choices + rationale
docs/learnings/        ← patterns, insights verified
docs/concerns/         ← open issues đáng theo dõi
.claude/rules/         ← always-in-context knowledge
```

### Adaptive structure

docs/ không có một template cứng. Grows theo project type:

```
Feature-based  → docs/features/{name}/
Research       → docs/findings/, docs/sources/
Learning       → docs/goals.md, docs/progress/
Script/tool    → docs/scripts/, docs/usage.md
Config/system  → docs/current-state.md, docs/changes/
```

### Consolidation

Sau bất kỳ completed work loop nào — PM hỏi: "sẽ cần thứ này ở session sau không?"

- Không → move on (0 overhead, phổ biến với RESPOND/DIRECT nhỏ)
- Có → save vào LTM location phù hợp (1 Write call)
- BUILD cycle + session end → explicit review, 2–5 Write calls

---

## Action Flow

### Init — Bootstrap memory

```
New project (no code):          Existing project (has code):
PM leads conversation           PM scans codebase (3-4 tool calls)
  → Problem? For whom?            → Spawn codebase-surveyor
  → Success in 4 weeks?           → Form hypotheses
  → Constraints?                  → Ask targeted questions
  → Infer project type            → Confirm hypotheses
  ↓                               ↓
Create minimal docs/            Create adaptive docs/
Write project.md                Write project.md
```

Key difference: new project → user's vision is primary → PM asks open questions.
Existing project → evidence from code → PM asks targeted questions to verify.

### UNDERSTAND Phase

```
clarify (Part 1) → detect state
    ↓ no docs/
   init → bootstrap memory
    ↓ docs/ exists
clarify (Part 2) → recognize pattern → RESPOND/DIRECT/BUILD
    ↓ BUILD only
   spec → technical design → user approves
```

### ACT Phase (BUILD only)

```
plan → decompose spec → TaskCreate (2-5 min tasks, max 5 concurrent/wave)
  ↓
execute → for each task:
  implementer → spec-reviewer → quality-reviewer → complete
  (parallel within wave, sequential between waves)
  ↓
verify → test all acceptance criteria → evidence required
  ↓ fail
 debug → root cause → fix → return to verify
  ↓ pass
consolidate → promote learnings/decisions to LTM → clear STM
```

---

## Agents

| Agent | Role | Dispatch by |
|-------|------|-------------|
| `codebase-surveyor` | Analyze existing codebase → write project.md, docs-map | PM (init) |
| `reverse-doc` | Reverse-engineer one feature → requirements + spec | PM (init Step 3) |
| `researcher` | Research technical questions, compare options | PM (any pattern, on knowledge gap) |
| `implementer` | Write code + tests + worker-report | PM (execute) |
| `spec-reviewer` | Verify implementation matches spec | PM (execute, after implementer) |
| `quality-reviewer` | Check code quality, conventions, no regressions | PM (execute, after spec-reviewer) |
| `doc-syncer` | Update docs after features complete | PM (verify, after all pass) |

---

## Constraint Layering

**SKILL.md** — global invariants (apply everywhere):
- PM không dùng Edit/Write/Bash trên code files
- Mọi câu hỏi → AskUserQuestion tool
- Không có docs/project.md → init trước
- Đọc action file trước khi làm bất kỳ action nào
- Spec phải được user approve trước khi vào ACT

**Action files** — local constraints (chỉ apply trong action đó):
- Không duplicate lên SKILL.md

---

## Escalation

| Tier | Khi nào | Làm gì |
|------|---------|--------|
| 1 | Minor, fixable in context | Fix → log → continue |
| 2 | Non-blocking gap | Write docs/concerns/CONCERN-*.md → continue |
| 3 | Blocker thực sự | AskUserQuestion: issue + tried + options + recommendation |

Concerns là internal (agent-to-agent). User chỉ thấy Tier 3.

---

## File Map

```
workflow/
├── .claude-plugin/plugin.json    ← plugin manifest
├── skills/orchestrator/
│   ├── SKILL.md                  ← PM definition (always loaded)
│   ├── ARCHITECTURE-v0.3.md      ← design discussion doc
│   ├── actions/                  ← step-by-step procedures
│   │   ├── clarify.md
│   │   ├── init.md
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── execute.md
│   │   ├── verify.md
│   │   └── debug.md
│   ├── references/               ← load on demand
│   │   ├── memory-guide.md       ← adaptive structure guide
│   │   ├── thought-process.md    ← pre-action checklist
│   │   └── concern-resolution.md ← concern → ADR flow
│   ├── templates/                ← format templates
│   └── scripts/                  ← python utilities
├── agents/                       ← agent definitions
├── hooks/                        ← session_start hook
└── docs/                         ← project memory (this project)
    ├── project.md
    ├── architecture.md           ← this file
    ├── state.md
    ├── decisions/
    ├── learnings/
    └── concerns/
```
