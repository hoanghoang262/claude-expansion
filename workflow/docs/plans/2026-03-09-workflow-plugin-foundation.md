# Workflow Plugin Foundation — Implementation Plan

> **For Claude:** Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Build the foundational layer of the workflow plugin: session-start hook (Python) + orchestrator skill that routes AI to the right skill at the start of every session.

**Architecture:** A Python session-start hook reads the orchestrator SKILL.md and optionally reads `.workflow/STATE.md` from the project root, then injects both into Claude's context as `additionalContext`. The orchestrator skill is a routing guide that tells Claude when to use which skill and how to classify task complexity.

**Tech Stack:** Python 3.8+ (stdlib only: json, pathlib, sys), Markdown for skills.

---

## Task 1: Directory scaffold + hooks.json

**Files:**
- Create: `workflow/hooks/hooks.json`
- Create: `workflow/skills/orchestrator/SKILL.md` (empty placeholder)
- Delete: `workflow/skills/.gitkeep`
- Delete: `workflow/hooks/.gitkeep`

**Step 1: Create hooks.json**

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '${CLAUDE_PLUGIN_ROOT}/hooks/session_start.py'",
            "async": false
          }
        ]
      }
    ]
  }
}
```

Save to `workflow/hooks/hooks.json`.

**Step 2: Create placeholder orchestrator skill**

```markdown
# Orchestrator

(placeholder — will be filled in Task 3)
```

Save to `workflow/skills/orchestrator/SKILL.md`.

**Step 3: Remove .gitkeep files**

```bash
rm workflow/skills/.gitkeep workflow/hooks/.gitkeep
```

**Step 4: Commit**

```bash
git add workflow/hooks/hooks.json workflow/skills/orchestrator/SKILL.md
git rm workflow/skills/.gitkeep workflow/hooks/.gitkeep
git commit -m "feat(workflow): scaffold hooks and skills directories"
```

---

## Task 2: Session-start hook (Python)

**Files:**
- Create: `workflow/hooks/session_start.py`
- Create: `workflow/hooks/tests/test_session_start.py`

**Step 1: Write the failing test**

```python
# workflow/hooks/tests/test_session_start.py
import json
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).parent.parent / "session_start.py"


def run_hook(cwd=None, env=None):
    """Run session_start.py and return parsed JSON output."""
    import os
    e = {**os.environ, **(env or {})}
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        capture_output=True, text=True, cwd=cwd or Path.cwd(), env=e
    )
    assert result.returncode == 0, f"Hook failed: {result.stderr}"
    return json.loads(result.stdout)


def test_output_has_required_keys(tmp_path):
    out = run_hook(cwd=tmp_path)
    assert "hookSpecificOutput" in out
    assert out["hookSpecificOutput"]["hookEventName"] == "SessionStart"
    assert "additionalContext" in out["hookSpecificOutput"]


def test_context_contains_orchestrator(tmp_path):
    out = run_hook(cwd=tmp_path)
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "<workflow-orchestrator>" in ctx


def test_context_without_state_file(tmp_path):
    """When .workflow/STATE.md doesn't exist, no state block injected."""
    out = run_hook(cwd=tmp_path)
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "<workflow-state>" not in ctx


def test_context_with_state_file(tmp_path):
    """When .workflow/STATE.md exists, its content is injected."""
    state_dir = tmp_path / ".workflow"
    state_dir.mkdir()
    (state_dir / "STATE.md").write_text("phase: execute\nactive-spec: auth-feature")

    out = run_hook(cwd=tmp_path)
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "<workflow-state>" in ctx
    assert "phase: execute" in ctx


def test_context_with_missing_orchestrator_skill(tmp_path, monkeypatch):
    """If orchestrator SKILL.md is missing, hook still outputs valid JSON with error note."""
    import os
    # Point PLUGIN_ROOT to a dir with no skills
    out = run_hook(cwd=tmp_path)
    # Just check it doesn't crash — orchestrator content may say "Error reading"
    assert "hookSpecificOutput" in out
```

**Step 2: Run test to verify it fails**

```bash
cd /home/hoanghoang262/Documents/code/claude-code-plugin
python3 -m pytest workflow/hooks/tests/test_session_start.py -v
```

Expected: FAIL — `session_start.py` doesn't exist yet.

**Step 3: Write minimal implementation**

```python
#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.

Injects:
1. Orchestrator skill content (always)
2. .workflow/STATE.md from project root (if exists)
"""
import json
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent
CWD = Path.cwd()


def read_file(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def build_context() -> str:
    parts = []

    # 1. Orchestrator skill
    orchestrator = read_file(PLUGIN_ROOT / "skills" / "orchestrator" / "SKILL.md")
    if orchestrator is None:
        orchestrator = "Error: orchestrator SKILL.md not found."
    parts.append(f"<workflow-orchestrator>\n{orchestrator}\n</workflow-orchestrator>")

    # 2. Project state (optional)
    state = read_file(CWD / ".workflow" / "STATE.md")
    if state is not None:
        parts.append(f"<workflow-state>\n{state}\n</workflow-state>")

    return "\n\n".join(parts)


def main() -> None:
    context = build_context()
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
```

Save to `workflow/hooks/session_start.py`.

**Step 4: Run tests to verify they pass**

```bash
python3 -m pytest workflow/hooks/tests/test_session_start.py -v
```

Expected: all 5 tests PASS.

**Step 5: Commit**

```bash
git add workflow/hooks/session_start.py workflow/hooks/tests/test_session_start.py
git commit -m "feat(workflow): add session-start hook in Python"
```

---

## Task 3: Orchestrator skill (SKILL.md)

**Files:**
- Modify: `workflow/skills/orchestrator/SKILL.md` (replace placeholder)

No tests — this is a Markdown skill file read by AI, not executable code.

**Step 1: Write orchestrator skill content**

```markdown
---
name: workflow:orchestrator
description: Loaded at every session start — routes AI to the right workflow skill based on task intent and complexity
---

# Workflow Orchestrator

You are operating inside the **workflow plugin**. This skill is your routing guide.
Read it at the start of every session, then act accordingly.

## Your First Action Every Session

1. Check if `<workflow-state>` was injected into your context.
   - If yes: read the current phase, active spec, and next action — resume from there.
   - If no: this is a fresh project or fresh task.
2. Read the user's first message to understand intent.
3. Classify and route (see below).

---

## Complexity Classification

Before choosing a flow, classify the task:

| Track | Signals | Ceremony |
|---|---|---|
| `light` | Single file, obvious fix, no behavior change, typo | Skip clarify + spec → execute directly |
| `standard` | New behavior, feature, multi-file change | clarify (if needed) → spec-formation → task-breakdown → execute → review → doc-sync |
| `heavy` | Architecture change, new system, risky migration, breaking change | Full standard flow + extra spec review gate before execute |

Classify based on **intent signals**, not file count alone. When in doubt, go `standard`.

---

## Skill Routing Rules

### When to use each skill:

| Situation | Skill |
|---|---|
| User has vague idea, doesn't know what to build | `workflow:brainstorming` |
| Task is clear but has ambiguous gaps | `workflow:clarify` |
| Ready to write spec (intent clear, no gaps) | `workflow:spec-formation` |
| Approved spec exists, need task breakdown | `workflow:task-breakdown` |
| Tasks ready, time to implement | `workflow:execute` (subagent) |
| Implementation done, need review | `workflow:review` (subagent) |
| Task complete, update docs | `workflow:doc-sync` (subagent) |
| Approved spec needs to change | `workflow:spec-amendment` |
| Bug or unexpected failure | `superpowers:systematic-debugging` |
| About to claim work is done | `superpowers:verification-before-completion` |
| All tasks done, ready to merge | `superpowers:finishing-a-development-branch` |

### Decision flow:

```
User message arrives
    |
    ├─ Resume? → read STATE.md → jump to current phase skill
    |
    └─ New task?
          |
          ├─ Intent too vague? → workflow:brainstorming
          ├─ Intent clear, gaps exist? → workflow:clarify
          └─ Intent clear, no gaps?
                |
                ├─ light track → execute directly
                └─ standard/heavy → workflow:spec-formation
```

---

## Autonomy Boundaries

**Act without asking:**
- Implementation details consistent with approved spec
- Test coverage improvements
- Bug fixes within current scope
- Refactors that don't change external behavior

**Always ask before acting:**
- Changing approved spec
- Architecture or dependency changes
- Expanding scope beyond what was approved
- Anything contradicting a previous user decision

---

## STATE.md Format

When you update `.workflow/STATE.md`, use this format:

```markdown
# Workflow State

phase: <clarify|spec|planning|execute|review|done>
active-spec: <spec slug or "none">
track: <light|standard|heavy>
next-action: <one sentence — what happens next>
blocked-by: <blocker description or "none">
last-updated: <YYYY-MM-DD>
```

Update STATE.md at every phase transition.

---

## Key Principle

> Standard flow always runs. Ceremony scales with complexity.
> You own execution. User owns intent and strategic decisions.
```

**Step 2: Commit**

```bash
git add workflow/skills/orchestrator/SKILL.md
git commit -m "feat(workflow): add orchestrator routing skill"
```

---

## Task 4: .workflow/ state templates

**Files:**
- Create: `workflow/scripts/init_workflow.py`

This script initializes `.workflow/` in a user's project (run once per project).

**Step 1: Write the script**

```python
#!/usr/bin/env python3
"""
Initialize .workflow/ directory in the current project.
Run: python3 <plugin-root>/scripts/init_workflow.py
"""
from pathlib import Path
from datetime import date

CWD = Path.cwd()
WORKFLOW_DIR = CWD / ".workflow"
SPECS_DIR = WORKFLOW_DIR / "specs"


STATE_TEMPLATE = f"""# Workflow State

phase: clarify
active-spec: none
track: none
next-action: Start by describing what you want to build.
blocked-by: none
last-updated: {date.today()}
"""

PROJECT_TEMPLATE = """# Project

## Identity
[Project name and one-sentence description]

## Goals
[What this project is trying to achieve]

## Constraints
[Technical constraints, non-negotiables, conventions]

## Key Decisions
[Architecture or design decisions already locked in]
"""


def init():
    if WORKFLOW_DIR.exists():
        print(f".workflow/ already exists at {WORKFLOW_DIR}")
        return

    SPECS_DIR.mkdir(parents=True)
    (WORKFLOW_DIR / "STATE.md").write_text(STATE_TEMPLATE)
    (WORKFLOW_DIR / "PROJECT.md").write_text(PROJECT_TEMPLATE)
    print(f"Initialized .workflow/ at {WORKFLOW_DIR}")
    print("Next: fill in .workflow/PROJECT.md with your project context.")


if __name__ == "__main__":
    init()
```

**Step 2: Write test**

```python
# workflow/scripts/tests/test_init_workflow.py
import subprocess, sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "init_workflow.py"


def test_creates_workflow_dir(tmp_path):
    subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, check=True)
    assert (tmp_path / ".workflow" / "STATE.md").exists()
    assert (tmp_path / ".workflow" / "PROJECT.md").exists()
    assert (tmp_path / ".workflow" / "specs").is_dir()


def test_state_md_has_required_keys(tmp_path):
    subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, check=True)
    content = (tmp_path / ".workflow" / "STATE.md").read_text()
    for key in ["phase:", "active-spec:", "track:", "next-action:", "blocked-by:"]:
        assert key in content


def test_idempotent(tmp_path):
    """Running twice should not crash or overwrite."""
    subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, check=True)
    result = subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 0
    assert "already exists" in result.stdout
```

**Step 3: Run tests**

```bash
python3 -m pytest workflow/scripts/tests/test_init_workflow.py -v
```

Expected: all 3 tests PASS.

**Step 4: Delete scripts/.gitkeep and commit**

```bash
git rm workflow/scripts/.gitkeep
git add workflow/scripts/init_workflow.py workflow/scripts/tests/test_init_workflow.py
git commit -m "feat(workflow): add init_workflow.py to scaffold .workflow/ in projects"
```

---

## Verification After All Tasks

```bash
# Run all tests
python3 -m pytest workflow/ -v

# Verify hook outputs valid JSON
python3 workflow/hooks/session_start.py | python3 -m json.tool

# Check file structure
find workflow/ -type f | grep -v __pycache__ | sort
```

Expected final structure:
```
workflow/
├── .claude-plugin/plugin.json
├── docs/
│   └── plans/2026-03-09-workflow-plugin-foundation.md
├── hooks/
│   ├── hooks.json
│   ├── session_start.py
│   └── tests/test_session_start.py
├── scripts/
│   ├── init_workflow.py
│   └── tests/test_init_workflow.py
└── skills/
    └── orchestrator/
        └── SKILL.md
```
