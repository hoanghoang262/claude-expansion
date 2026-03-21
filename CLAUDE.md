# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is a **Claude Code plugin marketplace** called `claude-expansion` — a curated collection of plugins that extend Claude Code functionality. It is managed via `.claude-plugin/marketplace.json`.

No build system or package manager is used. Plugins are self-contained directories with their own `.claude-plugin/plugin.json` descriptor.

---

## Plugins

| Plugin | Status | Description |
|---|---|---|
| `playwright-cli` | Mature | Browser automation via Playwright (screenshots, form filling, scraping, test generation) |
| `workflow` | Active | Multi-agent orchestration with memory lifecycle, wave execution, and version management |
| `memory` | Scaffolded | Persistent memory/context management (in development) |
| `superpowers` | Reference | Skills library from [obra/superpowers](https://github.com/obra/superpowers) — TDD, debugging, collaboration patterns |

---

## Repository Structure

```
.claude-plugin/marketplace.json      # Registry of all plugins
playwright-cli/                      # Mature plugin
  .claude-plugin/plugin.json
  skills/playwright-cli/
    SKILL.md
    references/                      # Explanatory guides
workflow/                            # Multi-agent orchestrator plugin
  .claude-plugin/plugin.json
  agents/                            # Subagent definitions (doc-syncer, implementer, etc.)
  commands/                          # Custom slash commands (e.g., /brainstorm)
  docs/                              # Project memory templates and guides
    templates/                       # Fillable doc templates (lifespan-labeled)
    guides/
    references/
  hooks/                             # Event hooks (session_start.py)
  skills/orchestrator/               # Core orchestrator skill
    SKILL.md
    templates/                       # Concrete file-format templates (JSON schemas, raw formats)
    references/                      # Phase guides (loaded on demand)
    evals/                           # Skill evaluation test cases
memory/                              # Scaffolded plugin
resource/
  superpowers/                       # Reference skills library (16 reusable skills)
    .claude-plugin/plugin.json
    skills/                          # Each skill has SKILL.md + optional references/
  backup/                            # Development principles (workflow, code, docs)
```

---

## Plugin Architecture

Each plugin follows this structure:

```
<plugin-name>/
  .claude-plugin/plugin.json      # Metadata: name, version, description, keywords
  skills/<skill-name>/
    SKILL.md                      # Main skill definition (always in English)
    templates/                     # Concrete formats: JSON schemas, raw skeletons (always in English)
    references/                    # Explanatory guides (loaded on demand, always in English)
  agents/                         # Agent definitions
  commands/                       # Custom slash commands
  hooks/                          # Event hooks
```

The marketplace registry at `.claude-plugin/marketplace.json` lists all plugins with their source path and version.

---

## Key Concepts

This repository uses Claude Code's extension system. Key terms:

- **Skill** — A specialized capability triggered by the Skill tool. Defined in `SKILL.md` with `name:` and `description:` frontmatter. Example: `superpowers:brainstorming`
- **Agent** — A specialized subagent type launched via the Agent tool with specific capabilities. Defined in `agents/` directory.
- **Command** — Custom slash commands (e.g., `/brainstorm`). Defined in `commands/`.
- **Hook** — Event hooks that run on specific events. Defined in `hooks/`.

Reference: See `resource/superpowers/skills/` for examples of well-documented skills.

---

## Skill Architecture

### Directory Layout

```
skills/<skill-name>/
├── SKILL.md           ← Entry point. Always loaded. English only. Max ~450 lines.
├── templates/         ← Pure format templates (no frontmatter, no prose)
│   └── *.json         # JSON schemas
│   └── *.md           # Markdown skeletons
├── references/        ← Explanatory guides (loaded on demand)
│   └── *.md           # How-to docs, policy, rationale
└── actions/           ← Action procedures (optional, at same level as SKILL.md)
    └── *.md           # Step-by-step procedures per action
```

### templates/ vs references/ vs actions/ — The Rule

| Directory | Contents | Rules |
|-----------|----------|-------|
| `templates/` | Pure format: JSON schemas, markdown skeletons. No frontmatter. No prose explanations. | Format only. |
| `references/` | Explanatory guides: when, why, policy. Point to templates for the actual format. | No duplication of template content. No `## When`. |
| `actions/` | Step-by-step procedures. Loaded by name from SKILL.md Action Registry. No `## When`. | SKILL.md defines when to load each action. |

### SKILL.md Standards

**Always in English.** Claude models parse English most reliably.

**Frontmatter (YAML):**
```
---
name: skill-name-with-hyphens   # Letters, numbers, hyphens only. No parentheses, no special chars.
description: Use when [specific triggering conditions — symptoms, situations, contexts]. Third person.
             NEVER summarize the skill's process or workflow here. Max ~1024 chars.
---
```

**Body structure (Progressive Disclosure):**
```
# Skill Name

## Persona                   (role statement + attribute table)
## Hard Constraints          (<do_not_act_before_instructions>, <assumed_interruption>)
## Thinking Model            (loop: understand → orient → select → run → loop)
## Decision Defaults         (<parallel_by_default>, <default_to_execute>)
## Action Registry           (YAML: actions + when + artifact + next)
## Stage Loop Behavior      (clarify ↔ implement loop, ask user only for trade-offs)
## Version Release Event     (if applicable)
## Reference Links           (load on demand)
```

**AML tags — what they are and when to use:**

AML tags define behavioral boundaries. They are NOT decoration.

| Tag | When to use | Never use for |
|---|---|---|
| `<do_not_act_before_instructions>` | Absolute prohibitions — things the agent must NEVER do | Workflow tips, preferences |
| `<assumed_interruption>` | Persistent policies that survive context resets | One-time instructions |
| `<parallel_by_default>` | Default behavior to override manual sequencing | Specific step ordering |
| `<default_to_execute>` | Common decision logic to shortcut explicit reasoning | Edge cases |
| `<blocking_thinking>` | Force structured reasoning before acting | Normal thought process |
| `<thought_process>` | Structured output format before phase/action transitions | Routine steps |
| `<examples>` | Structured few-shot output | Unstructured examples |
| `<stage>` | Group a mode of operation (e.g. CLARIFY vs IMPLEMENT) | Normal headings |

**Rule:** Wrap the CONTENT that needs the boundary, not surrounding structure. Never wrap table rows or list items.

**Lifespan labels** on every file path mentioned in the skill:
- `[PERMANENT]` — never delete
- `[VERSION]` — delete on Version Release Event
- `[SESSION]` — reset after each phase

---

## Development Principles

From `resource/backup/`:

**Workflow:** Context → implement → validate. Parallel by default; sequential only when outputs feed inputs. Feature branches only; diff before commit. Commit format: `type(scope): message`.

**Code:** No TODOs in core logic. No new dependencies without approval. Comment the "why" using prefixes: `WHY:`, `WARN:`, `NOTE:`, `HACK:`, `FIXME:`.

**Docs:** `docs/` is shared memory. New project → create `docs/overview.md`. Architecture decisions → create an ADR in `docs/adr/`. High-level design in `docs/`, low-level reasoning in code comments.

---

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

---

## Workflow Plugin — Key Conventions

### Three-Tier Memory Lifecycle

```
docs/
├── [PERMANENT]              ← NEVER delete. Project memory across all versions.
│   ├── PROJECT.md
│   ├── features/
│   ├── standards/
│   ├── research/
│   └── concerns/
├── [VERSION]                ← DELETE on Version Release Event
│   ├── ROADMAP.md
│   └── worker-reports/
├── [SESSION]               ← RESET after each phase
│   └── STATE.md
└── [ARCHIVE]
    └── versions/
        └── v{x}.md         ← Created by Version Release Event
```

### Version Release Event

```
1. Read ROADMAP.md → summarize all phases
2. Create docs/versions/v{x}.md
3. DELETE docs/worker-reports/
4. CLEAR ROADMAP.md entirely
5. KEEP docs/features/* unchanged
```

### Skill Writing Conventions

When creating or editing a skill in this repository, follow these rules:

**Language**
- All SKILL.md, templates/, and references/ files must be in English.

**Format — Hybrid Markdown + XML/AML**
Format for AI comprehension first, human readability second. Structure beats prose.

Priority order:
1. **Numbered/bullet lists** — for sequences, rules, checklists
2. **Tables** — for comparisons, file maps, metadata
3. **ASCII diagrams** — for workflows, phase chains, data flows
4. **Plain paragraphs** — only when lists/tables would be overkill
5. **XML/AML tags** — only for system toggles, blocking instructions, data boundaries, and few-shot examples. Never use XML to wrap normal prose.

**AML/XML tags — what they are and when to use them:**

AML tags define boundaries that Claude must respect. They are not decoration — they control behavior, constrain outputs, and isolate data.

Use AML/XML when you need Claude to:
- **Block actions** until a condition is met → `<do_not_act_before_instructions>`
- **Output structured reasoning** before acting → `<thought_process>`
- **Enforce a specific output format** → `<final_output>`, `<examples>`
- **Isolate background context** from instructions → `<context>`
- **Remind of persistent policies** → `<assumed_interruption>`
- **Group a stage or mode** of operation → `<stage>`, `<clarify>`, `<implement>`

**Format rule:**
- `<tag>` opens, `</tag>` closes. Always use both.
- Wrap the CONTENT that needs the boundary, not surrounding structure.
- Never wrap table rows, list items, or plain paragraph text.
- XML = boundary marker. Markdown (#) = document outline. Use both together.

```
## Two-Stage Mental Model

<stage name="CLARIFY">
- initialize → discuss-phase → plan-phase
- Your job: ask questions. Write docs. Do NOT spawn Executors.
</stage>

<stage name="IMPLEMENT">
- execute-phase → verify-work → doc-sync
- Your job: spawn agents. Check results. Do NOT ask requirement questions.
</stage>
```

**YAML frontmatter:**
```
name: skill-name-with-hyphens   # letters, numbers, hyphens only
description: Use when [specific triggering conditions — symptoms, situations,
             contexts]. Third person. Max ~1024 chars.
             NEVER summarize the workflow here.
```

**Structure — Progressive Disclosure (3 levels):**
```
Level 1 — SKILL.md frontmatter  (~100 tokens, always loaded)
Level 2 — SKILL.md body         (< 450 lines, loaded when skill triggers)
Level 3 — references/ + scripts/ (loaded on demand, no size limit)
```

**SKILL.md body — what goes where:**

| Content | Location |
|---|---|---|
| Reasoning logic, routing strategy, PM mindset | SKILL.md body |
| Step-by-step phase procedures | references/{phase}.md |
| Concrete formats, JSON schemas | templates/*.json |
| Executable helpers | scripts/*.py |

**Rules:**
- SKILL.md body < 450 lines. If approaching the limit, push detail to references/.
- Never nest references more than 1 level deep. From SKILL.md, link to references/. From references/, do not link further — inline the content.
- Never duplicate template content in references/.
- Every file path in SKILL.md must have a lifespan label: `[PERMANENT]`, `[VERSION]`, `[SESSION]`.
- Before deploying a new skill: use `superpowers:writing-skills` RED-GREEN-REFACTOR process. No skill without a failing test first.

**Self-ask patterns — use lists, not prose:**
```
Before spawning agents:
  - Is the plan approved by user? → No → Stop. Ask for approval.
  - Are there pending checkpoints? → Yes → Stop. Present to user.
```
Lists with arrow outcomes are readable by AI and easy to verify.

---

## Scripts

Automation helpers for the orchestrator skill live in `workflow/skills/orchestrator/scripts/`. Run from the project root:

```bash
python3 <path-to-orchestrator>/scripts/<script-name>.py [args]
```

Available scripts:

| Script | Purpose |
|--------|---------|
| `search_version.py` | Search `docs/versions/v*.md` for keywords, bug IDs, or feature names |
| `create_version_release.py` | Execute a Version Release Event: archive version, delete worker-reports, clear ROADMAP |

---

## Global Rules

- **Always write in English** in all skill files, templates, references, and scripts.
- If Claude Code concepts are involved (hooks, MCP servers, agent SDK), use the `claude-code-guide` subagent to search first.
- CLAUDE.md is the only file that may contain non-English notes or explanations (it is read by humans, not models).
