# {Project Name}

## Identity
- **Type:** {web-app | api | cli | library | monorepo | other}
- **Purpose:** {1-2 sentences — what it does and for whom}
- **Path:** {project_root}

## Architecture

```
{high-level component diagram — how main parts connect}

Example:
  Client (React) → API (Express) → DB (PostgreSQL)
                                  → S3 (files)
```

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| {layer} | {tech} | {version} |

## Modules

| Module | Responsibility | Key files |
|--------|---------------|-----------|
| {name} | {what it does} | {entry point} |

## Data Flow

```
{how data moves through the system — request lifecycle}

Example:
  Request → Router → Middleware (auth, validation) → Controller → Service → Repository → DB
```

## Run

```bash
# Development
{command to start dev}

# Production
{command to build/deploy}
```

## Dependencies

- **External services:** {APIs, databases, storage, etc.}
- **Key libraries:** {the 5-10 most important dependencies}
