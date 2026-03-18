# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Claude Code plugin marketplace** called `claude-expansion` — a curated collection of plugins that extend Claude Code functionality. It is managed via `.claude-plugin/marketplace.json`.

## Plugins

| Plugin           | Status     | Description                                                                                                          |
| ---------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| `playwright-cli` | Mature     | Browser automation via Playwright (screenshots, form filling, scraping, test generation)                             |
| `workflow`       | Scaffolded | Workflow automation (in development)                                                                                 |
| `memory`         | Scaffolded | Persistent memory/context management (in development)                                                                |
| `superpowers`    | Reference  | Skills library from [obra/superpowers](https://github.com/obra/superpowers) — TDD, debugging, collaboration patterns |

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
  superpowers/                     # Skills library plugin (reference for building new plugins)
    .claude-plugin/plugin.json
    skills/                        # 16 reusable skills (brainstorming, TDD, debugging, etc.)
  backup/                         # Development principles (workflow, code, docs)
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

## Key Concepts

This repository uses Claude Code's extension system. Key terms:

- **Skill** — A specialized capability triggered by the Skill tool. Defined in `SKILL.md` with `name:` and `description:` frontmatter. Example: `superpowers:brainstorming`
- **Agent** — A specialized subagent type launched via the Agent tool with specific capabilities. Defined in `agents/` directory.
- **Command** — Custom slash commands (e.g., `/playwright-cli`). Defined in `commands/`.
- **Hook** — Event hooks that run on specific events. Defined in `hooks/`.

Reference: See `resource/superpowers/skills/` for examples of well-documented skills.

## Development Principles

From `resource/backup/`:

**Workflow:** Context → implement → validate. Parallel by default; sequential only when outputs feed inputs. Feature branches only; diff before commit. Commit format: `type(scope): message`.

**Code:** No TODOs in core logic. No new dependencies without approval. Comment the "why" using prefixes: `WHY:`, `WARN:`, `NOTE:`, `HACK:`, `FIXME:`.

**Docs:** `docs/` is shared memory. New project → create `docs/overview.md`. Architecture decisions → create an ADR in `docs/adr/`. High-level design in `docs/`, low-level reasoning in code comments.

## Superpowers Skills Library

`resource/superpowers/skills/` contains 16 reusable skills for agent-driven development workflows. Key skills:

- `superpowers:brainstorming` — Socratic design refinement before implementation (MUST use before any creative work)
- `superpowers:subagent-driven-development` — Execute plans with fresh subagent per task + two-stage review
- `superpowers:test-driven-development` — RED-GREEN-REFACTOR cycle
- `superpowers:systematic-debugging` — 4-phase root cause analysis
- `superpowers:writing-plans` — Break work into 2–5 minute tasks
- `superpowers:finishing-a-development-branch` — Merge/PR decision workflow
- `superpowers:dispatching-parallel-agents` — Concurrent subagent workflows
- `superpowers:verification-before-completion` — Validate before marking done
- `superpowers:executing-plans` — Execute plans in parallel session
- `superpowers:requesting-code-review` — Code review templates
- `superpowers:receiving-code-review` — Handle review feedback
- `superpowers:using-git-worktrees` — Isolated workspace setup
- `superpowers:writing-skills` — How to write good skills

These are reference implementations for building new plugins and skills. Study `brainstorming/SKILL.md` and `subagent-driven-development/SKILL.md` to understand skill structure.

- alway wright by englash
- if have claude code knowlge as subagent skill term, use claude-code-guild subagent to search first
