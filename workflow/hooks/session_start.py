#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.
1. Injects orchestrator SKILL.md into Claude's context.
2. Reads project state and provides routing_hint to orchestrator.
3. When docs/ absent or incomplete: routing_hint=explore.
   When docs/ present with state.md: no routing_hint (orchestrator reads state.md).
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
    skill_text = get_orchestrator_skill()

    if project_root is None:
        # No docs/ found anywhere — orchestrator will run explore to init memory
        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": (
                    f"<workflow-orchestrator>\n{skill_text}\n</workflow-orchestrator>\n\n"
                    f"<session_start_context>\n"
                    f"routing_hint: explore\n"
                    f"docs_exists: false\n"
                    f"</session_start_context>"
                ),
            }
        }
        print(json.dumps(output))
        return

    docs_dir = project_root / "docs"
    state_file = docs_dir / "state.md"
    project_file = docs_dir / "project.md"

    # docs/ found but project not initialized yet
    if not project_file.exists() or not state_file.exists():
        routing_hint_line = "routing_hint: explore\n"
    else:
        # docs/ and state.md both exist — orchestrator reads state.md to determine next action
        routing_hint_line = ""

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                f"<workflow-orchestrator>\n{skill_text}\n</workflow-orchestrator>\n\n"
                f"<session_start_context>\n"
                f"project_root: {str(project_root)}\n"
                f"{routing_hint_line}"
                f"docs_exists: {str(docs_dir.exists()).lower()}\n"
                f"state_exists: {str(state_file.exists()).lower()}\n"
                f"project_exists: {str(project_file.exists()).lower()}\n"
                f"</session_start_context>"
            ),
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
