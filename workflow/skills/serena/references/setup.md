# Serena MCP Setup

## Prerequisites

Install `uv` (first time only):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Configure MCP in Claude Code

Add to your project's `.claude/settings.json` (or global `~/.claude/settings.json`):

```json
{
  "mcpServers": {
    "serena": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/oraios/serena",
        "serena", "start-mcp-server",
        "--context", "ide-assistant",
        "--mode", "/absolute/path/to/workflow/skills/serena/modes/workflow-mode.yml"
      ]
    }
  }
}
```

Replace `/absolute/path/to/workflow/...` with the real path to `workflow-mode.yml` in this repo.

Restart Claude Code to load the MCP server.

---

## Per-Project Activation

Each project must be activated once before Serena can navigate its code:

```
activate_project(project_path="/absolute/path/to/your/project")
```

Run this at the start of any session before using navigation tools.

---

## Verify Setup

```
get_current_config()
```

Should show `serena` in active MCP servers and `workflow-mode` in active modes.

---

## Language Server Notes

Serena auto-detects language servers. For best results:

| Language | Required LSP |
|---|---|
| Python | `pylsp` or `pyright` (`pip install python-lsp-server`) |
| TypeScript/JS | `typescript-language-server` (`npm i -g typescript-language-server typescript`) |
| Go | `gopls` (`go install golang.org/x/tools/gopls@latest`) |
| Rust | `rust-analyzer` (via rustup) |

If LSP acts up after external edits: `restart_language_server()`
