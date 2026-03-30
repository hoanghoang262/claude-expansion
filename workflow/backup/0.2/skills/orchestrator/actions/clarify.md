# clarify

Entry point for every session. Two jobs: **detect** project state, **understand** user intent.

<hard_constraint never_override>
- Understand before acting. Never jump to solutions.
- Never create docs/ — that is `init`'s job.
- Do not accept vague answers — always drill down.
- Do NOT act before understanding what "done" looks like for this task.
</hard_constraint>

---

## Part 1 — Detect

**Always start by trying to read `docs/project.md`.**

| Result | Meaning | Next |
|--------|---------|------|
| Both `project.md` + `state.md` exist | Memory complete | Read both → go to Part 2 |
| `project.md` exists, `state.md` missing | Memory partial | Read project.md → reset state → go to Part 2 |
| `project.md` missing | No memory | Quick scan → determine new or existing project |

<hard_constraint never_override>
If docs/ exists but project.md is missing:
Memory is BROKEN. Other files (features/, specs) are orphaned — do not read or reuse them.
Treat as no memory → run init.
</hard_constraint>

### Quick scan (no memory)

PM does this directly — **no agents**, 3-4 tool calls max:

1. `ls` project root — folder structure overview
2. Check `.git/` exists?
3. Look for package manager files: `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`

```
Code found?
    ├── YES → EXISTING PROJECT → init (mode: existing)
    └── NO  → NEW PROJECT      → init (mode: new)
```

Present to user:
```
🔍 Quick scan
📁 {folder list or "empty project"}
➡️ Running init — setting up project memory
```

**STOP** → Read `actions/init.md` using Read tool → then follow it step by step.

---

## Gate — docs/ required

> Verify `docs/project.md` + `docs/state.md` exist before entering Part 2.
> If either missing → run `init` first. Do NOT answer the user's question before init completes.

---

## Part 2 — Understand

**First: understand what "done" looks like for THIS request.** Not every task needs a spec.

### Recognize Pattern

| Pattern | Signals | Entry |
|---------|---------|-------|
| **RESPOND** | "explain", "what is", "how does", "analyze this for me" — user needs insight, no persistent output | → Understand question → answer directly. Consolidate if strategic. |
| **DIRECT** | Small, clearly bounded, no design decision needed — "fix typo", "add this line", "rename X" | → Confirm scope (1 question max) → act immediately. |
| **BUILD** | "build", "create", "implement", "set up" — significant persistent output, design decisions involved | → Full requirements gathering → spec → ACT phase. |

**Recognition comes from understanding intent, not matching keywords.**
When pattern is ambiguous → go deeper (treat as BUILD) until clear.

---

### RESPOND

**Step 1 — Understand the question fully.**
What does the user actually want to know? What would make the answer useful?

**Step 2 — Answer directly.**
Use docs/, research, reasoning. If knowledge gap → spawn researcher with focused question.

**Step 3 — Consolidate (if valuable).**
Ask: "will this insight be useful in a future session?" → YES: save to `docs/learnings/` → NO: done.

---

### DIRECT

**Step 1 — Confirm scope** (if not 100% clear, ask one focused question).
**Step 2 — Act.** PM edits documentation directly. Code files → implementer agent.
**Step 3 — Consolidate** if decision has lasting implication.

---

### BUILD

**Step 1 — Ask open-ended questions.**
2-4 per round via AskUserQuestion. Round 1 = about the GOAL and USER, not tech.
Questions should help user discover what they actually need, not just extract requirements.

**Step 2 — Write docs** (after 1-2 rounds).
Create appropriate docs based on project type (see `references/memory-guide.md`).
For feature-based: `docs/features/{name}/requirements.md` + `user-stories.md`
Mark unknowns as `[GAP]`

**Step 3 — Loop until zero gaps.**
Read docs → find `[GAP]`s → ask → update → repeat.
Spawn `researcher` if topic needs deep technical knowledge.

**Step 4 — Confirm + exit to spec.**
Show summary of what will be built. User confirms → `spec`.

<hard_constraint never_override>
NOT ready to exit BUILD if:
- Any `[GAP]` markers remain in requirements docs
- Cannot describe primary user flows without blanks
- Accepted vague answers without drilling down
- Haven't gotten explicit user confirmation
</hard_constraint>

---

## Research (within any pattern)

Spawn `researcher` via Agent tool when PM hits a knowledge gap.

**When:** domain context needed, multiple approaches to compare, technical unknowns.
**How:** spawn in parallel, pass focused question + expected output format.
**Not for:** Part 1 detection (quick scan is enough).
