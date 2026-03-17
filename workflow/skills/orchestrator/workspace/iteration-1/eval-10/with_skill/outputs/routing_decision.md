# Routing Decision

## Task
"Xem version hiện tại của app là gì?"

## Analysis

**Intent Classification:** Simple lookup question - asking for current app version

**Key Observations:**
- SKILL.md explicitly states: "NOT for: simple lookups or questions"
- This is a straightforward question requiring just reading version info
- No analysis, planning, building, fixing, or research needed

**Intent Router Match:**
| User says | Jump to | Match? |
|-----------|---------|--------|
| "cần biết", "giải thích" | `references/understand.md` | Partial |

The phrase "Xem version hiện tại" contains "cần biết" (need to know) which maps to understand.md, BUT this is a simple lookup, not an analysis task.

## Recommendation

**Phase: NONE (Skill should NOT be used)**

**Reason:** This is a simple lookup/question. The orchestrator skill is designed for:
- Building, implementing, creating
- Fixing bugs
- Brainstorming
- Researching
- Reviewing
- Planning

Asking for the current app version is a basic read operation that doesn't require the workflow orchestration overhead. Just answer the question directly.

**If forced to route:** `understand.md` (because it's the closest match for "cần biết")
- Would load project context
- Find version in package.json, pubspec.yaml, build.gradle, etc.
- Return version info

But ideally: **Don't use orchestrator skill for this query.**
