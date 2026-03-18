# Research Phase

Investigation, analysis, and exploration of options.

## Inputs Needed

1. **Research topic** - What to investigate
2. **Context** - Why this matters, constraints
3. **Existing knowledge** - What's already known

## Process

### 1. Define Research Questions

```
What needs to be answered:
1. <question 1>
2. <question 2>
```

### 2. Investigate

- Search codebase
- Read relevant docs
- Analyze patterns
- Compare options

### 3. Document Findings

Create `docs/research/<topic>.md`:

```markdown
# Research: <topic>

## Questions
1. <question 1>
2. <question 2>

## Findings

### <Finding 1>
<details>

### <Finding 2>
<details>

## Recommendations

Based on analysis:
- <Option A>: <pros/cons>
- <Option B>: <pros/cons>

## Next Steps
- Decision needed?
- Spec needed?
- Implementation?
```

## Depth

### When to stop research
- Already have enough info to answer original question
- 3+ sources confirm same conclusion
- User gave clear direction → no need for more options

### When to dig deeper
- Results conflict each other → need more sources
- Decision has big impact (architecture, security)
- User says "research thoroughly" or "deep dive"

### Output scale by context
- Quick question → 1 paragraph + recommendation
- Compare options → Trade-off table + recommendation
- Deep dive → Full findings + sources + multiple perspectives

## Docs Responsibility

| Output | Docs to update |
|--------|----------------|
| Technical findings | `docs/architecture/` |
| Feature research | `docs/features/` |
| Options analysis | `docs/specs/<slug>/research.md` |

## Output

- Research document with findings
- Recommendations with rationale
- Clear next action

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Decision made → implement | `spec-form.md` or `execute.md` |
| Need to plan | `plan.md` |
| More research needed | Stay in research |
