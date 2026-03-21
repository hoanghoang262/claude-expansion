# discuss — Requirements Gathering

## Orchestrator asks the user in exactly 2 scenarios:

1. **Entering discuss:** gather or clarify requirements
2. **During any action:** a trade-off decision arises that AI cannot resolve alone

## Step 1: Read existing context (in parallel)

```
docs/PROJECT.md
docs/ROADMAP.md
docs/features/           ← check existing features
docs/standards/TESTING.md
```

## Step 2: Analyze user intent

```
User describes a COMPLETELY NEW feature?
  → YES → New feature → Step 3

Feature already in features/?
  → Yes, spec exists? → spec (skip discuss)
  → Yes, spec absent? → read requirement.md → spec
  → No → New feature → Step 3
```

## Step 3: Gather information

```
Description CLEAR?
  → YES → Step 4a

Description VAGUE?
  → YES → Step 4b (max 5 questions, ask all at once)
```

**5 questions (ask all at once):**

1. "What is the end goal? (What does the user achieve?)"
2. "Who is the user? (Frontend dev? End user? Admin?)"
3. "When is the feature DONE?" — criteria must be OBSERVABLE
4. "Any special technical constraints?"
5. "Any API/service you want to integrate?"

## Step 4a: Enough information

```
1. Create: docs/features/{id}-{name}/requirement.md
   Use: templates/requirement-template.md
2. Update: docs/ROADMAP.md (add feature to milestone)
3. → spec
```

## Step 4b: Need clarification

```
Ask 5 questions (see above).
After user answers → Step 4a.
```
