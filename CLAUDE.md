# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code plugin marketplace** called `claude-expansion` — a curated collection of plugins that extend Claude Code functionality. It is managed via `.claude-plugin/marketplace.json` and contains three plugins:

- **playwright-cli** — Browser automation via Playwright (screenshots, form filling, scraping, test generation)
- **workflow** — Workflow automation (scaffolded, in development)
- **memory** — Persistent memory/context management (scaffolded, in development)

No build system or package manager is used. Plugins are self-contained directories with their own `.claude-plugin/plugin.json` descriptor.

## Repository Structure

```
.claude-plugin/marketplace.json   # Registry of all plugins
playwright-cli/                   # Mature plugin with skills + references
  .claude-plugin/plugin.json
  skills/playwright-cli/
    SKILL.md                      # Command reference
    references/                   # 7 reference guides (tracing, video, mocking, etc.)
workflow/                         # Scaffolded plugin (empty)
memory/                           # Scaffolded plugin (empty)
resource/
  backup/                         # Development principles (workflow, code, docs)
  superpowers/                    # Full skills library from obra/superpowers
```

## Plugin Architecture

Each plugin follows this structure:
```
<plugin-name>/
  .claude-plugin/plugin.json      # Metadata: name, version, description, keywords
  skills/<skill-name>/
    SKILL.md                      # Main skill definition
    references/                   # Supporting reference docs
  agents/                         # Agent definitions
  commands/                       # Custom slash commands
  hooks/                          # Event hooks
  scripts/                        # Helper scripts
```

The marketplace registry at `.claude-plugin/marketplace.json` lists all plugins with their source path and version.

## Development Principles

From `resource/backup/`:

**Workflow:** Context → implement → validate. Parallel by default; sequential only when outputs feed inputs. Feature branches only; diff before commit. Commit format: `type(scope): message`.

**Code:** No TODOs in core logic. No new dependencies without approval. Comment the "why" using prefixes: `WHY:`, `WARN:`, `NOTE:`, `HACK:`, `FIXME:`.

**Docs:** `docs/` is shared memory. New project → create `docs/overview.md`. Architecture decisions → create an ADR in `docs/adr/`. High-level design in `docs/`, low-level reasoning in code comments.

## Superpowers Skills Library

`resource/superpowers/skills/` contains 16 reusable skills for agent-driven development workflows. Key skills:

- `brainstorming` — Socratic design refinement before implementation
- `writing-plans` — Break work into 2–5 minute tasks
- `subagent-driven-development` — Fast iteration with two-stage review
- `test-driven-development` — RED-GREEN-REFACTOR cycle
- `systematic-debugging` — 4-phase root cause analysis
- `dispatching-parallel-agents` — Concurrent subagent workflows
- `finishing-a-development-branch` — Merge/PR decision workflow

These are reference implementations for building new plugins and skills.
