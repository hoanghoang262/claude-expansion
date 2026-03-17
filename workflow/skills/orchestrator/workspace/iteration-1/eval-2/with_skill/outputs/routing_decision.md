# Routing Decision

## Task
"build login feature"

## Route To
**`references/spec-form.md`** — Spec Form Phase

## Why

| Factor | Analysis |
|--------|----------|
| **Keyword match** | User says "build" — triggers `references/spec-form.md` |
| **Example match** | SKILL.md lists "build login feature" as exact example → perfect match |
| **Intent type** | New feature implementation — requires specification first |
| **Phase appropriateness** | Spec Form phase is designed for: "build", "implement", "thêm", "tạo" — create new feature spec |

## Reasoning

1. The Intent Router in SKILL.md explicitly maps "build", "implement", "thêm", "tạo" to `references/spec-form.md`
2. The provided example "build login feature" matches the user's input exactly — this is a direct example in the routing table
3. Building a new feature requires the Spec Form phase to:
   - Define requirements and acceptance criteria
   - Document the feature scope
   - Create a spec before planning and execution

## Next Step
After Spec Form phase completes, the workflow will:
- Proceed to `plan.md` to break the spec into tasks
- Then execute with `execute.md`
