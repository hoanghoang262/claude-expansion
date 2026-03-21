#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.
1. Injects orchestrator skill into Claude's context.
2. Auto-initializes docs/ if absent or empty.
3. Performs orient-before-acting and routes to the correct phase.
"""
import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent


def find_project_root() -> Path | None:
    """Walk up from cwd to find a directory with docs/ inside."""
    cwd = Path.cwd()
    for candidate in [cwd, cwd.parent, cwd.parent.parent]:
        if (candidate / "docs").exists():
            return candidate
    return None


def get_orchestrator_skill() -> str:
    """Load the orchestrator SKILL.md content."""
    try:
        return (PLUGIN_ROOT / "skills" / "orchestrator" / "SKILL.md").read_text(encoding="utf-8")
    except OSError:
        return "[workflow-orchestrator] Error: SKILL.md not found."


def main() -> None:
    project_root = find_project_root()

    if project_root is None:
        # No project found — nothing to initialize, let Orchestrator handle it
        skill_text = get_orchestrator_skill()
        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": f"<workflow-orchestrator>\n{skill_text}\n</workflow-orchestrator>",
            }
        }
        print(json.dumps(output))
        return

    docs_dir = project_root / "docs"
    state_file = docs_dir / "STATE.md"
    project_file = docs_dir / "PROJECT.md"

    # Determine initial action for Orchestrator to select
    if not project_file.exists():
        routing_hint = "orient"
    elif not state_file.exists():
        routing_hint = "orient"
    else:
        routing_hint = "ready"

    skill_text = get_orchestrator_skill()
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                f"<workflow-orchestrator>\n{skill_text}\n"
                f"</workflow-orchestrator>\n\n"
                f"<session_start_context>\n"
                f"project_root: {str(project_root)}\n"
                f"routing_hint: {routing_hint}\n"
                f"docs_exists: {docs_dir.exists()}\n"
                f"state_exists: {state_file.exists()}\n"
                f"project_exists: {project_file.exists()}\n"
                f"</session_start_context>"
            ),
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
