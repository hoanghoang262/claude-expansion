# {Feature} — Technical Design

**Status:** Draft | Approved
**Created:** {date}
**Covers:** {FR-xxx list from requirements}

## Architecture

```
{file tree — what files are involved}

{component diagram — how they connect}
```

## Data Model

| Entity | Fields | Relationships |
|--------|--------|--------------|
| {Model} | {key fields with types} | {belongs to X, has many Y} |

## API / Interface Contracts

| Method | Endpoint | Request | Response | Auth |
|--------|----------|---------|----------|------|
| {GET/POST/...} | {/api/...} | {body/params} | {response shape} | {role required} |

## Logic / Rules

- {business logic that code implements}
- {validation rules}
- {state transitions}

## Error Handling

| Error case | Response | User sees |
|-----------|----------|-----------|
| {scenario} | {HTTP code + body} | {message} |

## Security

- {auth: who can access what}
- {input validation: what's sanitized}
- {data protection: what's encrypted/hashed}

## Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| {what} | {picked option} | {rationale} |

## Dependencies

- **Requires:** {other features/modules this depends on}
- **Required by:** {features that depend on this}
