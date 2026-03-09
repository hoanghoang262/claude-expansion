import json
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).parent.parent / "session_start.py"


def run_hook(cwd=None):
    import os
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        capture_output=True, text=True, cwd=str(cwd or Path.cwd())
    )
    assert result.returncode == 0, f"Hook failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"
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


def test_no_state_block_without_state_file(tmp_path):
    out = run_hook(cwd=tmp_path)
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "<workflow-state>" not in ctx


def test_state_block_injected_when_file_exists(tmp_path):
    state_dir = tmp_path / ".workflow"
    state_dir.mkdir()
    (state_dir / "STATE.md").write_text("phase: execute\nactive-spec: auth-feature")
    out = run_hook(cwd=tmp_path)
    ctx = out["hookSpecificOutput"]["additionalContext"]
    assert "<workflow-state>" in ctx
    assert "phase: execute" in ctx


def test_output_is_valid_json(tmp_path):
    import subprocess
    result = subprocess.run(
        [sys.executable, str(HOOK)],
        capture_output=True, text=True, cwd=str(tmp_path)
    )
    assert result.returncode == 0
    # Should not raise
    parsed = json.loads(result.stdout)
    assert isinstance(parsed, dict)
