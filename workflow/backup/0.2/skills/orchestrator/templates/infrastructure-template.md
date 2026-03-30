# Infrastructure

## Services

| Service | Image/Tech | Port | Purpose |
|---------|-----------|------|---------|
| {name} | {image or tech} | {port} | {what it does} |

## Topology

```
{how services connect}

Example:
  frontend:5173 → backend:3000 → db:5432
                                → redis:6379
                                → s3 (external)
```

## Environment

| Variable | Service | Purpose |
|----------|---------|---------|
| {VAR_NAME} | {which service} | {what it configures} |

## How to run

```bash
# Development
{dev command}

# Production
{prod command}
```

## Volumes / Persistence
- {what data is persisted and where}
