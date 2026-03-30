---
name: serena
description: Use when navigating or editing a codebase by symbol — finding functions/classes,
             tracing call chains, replacing symbol bodies, or renaming across the entire project.
             Prefer over Grep/Read/Edit when Serena MCP is configured. Not useful for small
             projects, new files with no existing symbols, or non-code files.
---

# Serena — LSP Code Navigation

## Hard Constraints

<hard_constraint never_override>
- Never call memory tools (write_memory, read_memory, list_memories, etc.) — docs/ handles all memory.
- Never call onboarding or prepare_for_new_conversation — STATE.md handles session context.
- Always call activate_project before any navigation tool if project is not yet active.
</hard_constraint>

---

## Session Start

```
1. activate_project(project_path="<absolute path>")
2. Proceed with task — no onboarding needed, docs/ has the context
```

---

## Tool Routing

### Prefer Serena over native tools

| Task | Serena tool | Instead of |
|---|---|---|
| Find a function / class / variable | `find_symbol` | Grep |
| Who calls this function? | `find_referencing_symbols` | Grep |
| What's defined in this file? | `get_symbols_overview` | Read (full file) |
| Replace entire function/class body | `replace_symbol_body` | Edit |
| Rename symbol + all references | `rename_symbol` | Grep + Edit (manual) |
| Add code after a function | `insert_after_symbol` | Edit |
| Add code before a function | `insert_before_symbol` | Edit |
| Search text / regex in project | `search_for_pattern` | Grep |
| Find file by name/path | `find_file` | Glob |
| Browse directory tree | `list_dir` | Glob |

### Use native tools (Read, Edit, Write, Bash) for

- Reading non-code files (config, JSON, docs, templates)
- Creating new files from scratch
- Edits not bounded by a symbol (e.g., file header, import block)
- Running tests, build commands, shell operations

---

## Editing Decision

```
Does the change target a named symbol (function, class, method)?
  YES → replace_symbol_body / insert_after_symbol / insert_before_symbol
  NO  → replace_content / replace_lines / Edit (native)

Is this a rename across the whole codebase?
  YES → rename_symbol (LSP refactor — safe, handles all references)
  NO  → Edit / replace_content
```

---

## When Serena Provides Little Value

- Project has < 5 files — just Read/Edit directly
- Greenfield code — no symbols to navigate yet
- Dynamic language with no type annotations — LSP accuracy degrades
- Config/docs files — no symbol structure

---

## Troubleshooting

LSP returning unexpected results after external edits → `restart_language_server()`
Unsure what tools/modes are active → `get_current_config()`

---

## References

- `modes/workflow-mode.yml` [PERMANENT] — active tool set for this plugin
- `references/setup.md` [PERMANENT] — MCP configuration and language server setup
