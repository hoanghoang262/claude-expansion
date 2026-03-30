# Project

## Overview

**workflow** — a PA (Personal Assistant) skill plugin for Claude Code.

Solves the problem of AI assistants that reset every session and only follow pipelines.
PA builds understanding of the user and project over time, coordinates agents, and handles any type of project — not just software.

**Type:** Claude Code plugin (PA skill)

**Tech Stack:**
- Claude Code extension system (SKILL.md, agents, hooks)
- Python hooks (`hooks/session_start.py`)
- Markdown-based memory (`docs/`)

**Key Features:**
- Accumulates context across sessions — no re-explaining
- Works for any project type (web, AI, research, scripts, learning)
- Coordinates specialized agents in parallel
- Dual-purpose docs — AI memory + human-readable documentation
- 4-phase work cycle: UNDERSTAND → BUILD → VERIFY → CLOSE

---

## User Context

Developer building this plugin for personal use and potentially public release.

**Working style:**
- Architecture-first — thinks through design before writing code
- Challenges assumptions — always asks "is there a better way?"
- Dislikes over-engineering — exactly what's needed, nothing more
- Prefers thorough brainstorming before implementation
- Quality over speed

**Communication style:**
- Direct, concise — no filler
- Expects recommendations, not option menus
- Will push back if reasoning is unclear

**What PA should be like with this user:**
- Announce before acting — never go silent then dump output
- Challenge back when something seems wrong
- Skip preamble — get to the point
- Always recommend, never present blank options
- Ask one focused question when unclear — never shotgun multiple

---

## Goals

**Now:** Solid PA skill foundation
- Clean SKILL.md with correct architecture
- 4-phase cycle that works for any project type
- Memory system that accumulates value over time

**Later:** PA smart enough to be a real personal assistant
- Understands user without being told
- Handles any domain — web, research, learning, scripts, config
- Memory that makes every session better than the last

---

## Constraints

- Plugin loaded via `.claude-plugin/plugin.json` — no build system
- SKILL.md is entry point — loaded when skill triggers
- Agents defined in `agents/` — dispatched by PA
- Hooks in `hooks/session_start.py` — runs at session start
- All skill files must be in English
