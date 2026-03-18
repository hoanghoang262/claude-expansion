# Clarify — Research

Phase 1b: Investigation, analysis, exploration.

> **Load only when needed.** Load `understand.md` first.

---

## When to Use

- User wants to compare options
- Need to investigate technical approaches, libraries, patterns
- Architecture decisions that need analysis
- User says: "what are the options?", "research", "compare", "investigate"

---

## Process

### 1. Define Questions
```
What needs to be answered:
1. <question 1>
2. <question 2>
```

### 2. Investigate
- Search codebase for existing patterns
- Read relevant docs
- Compare alternatives

### 3. Document

Template: [templates/research-findings.md](templates/research-findings.md)

---

## Depth

| Situation | Action |
|-----------|--------|
| Enough info to decide | Stop |
| 3+ sources confirm same | Stop |
| Results conflict | Dig deeper |
| Big impact (arch, security) | Dig deeper |
| User says "deep dive" | Dig deeper |

---

## Output Scale

| Context | Output |
|---------|--------|
| Quick | 1 paragraph + recommendation |
| Compare options | Trade-off table + recommendation |
| Deep dive | Full findings + sources |
