# Database Schema

## Overview
- **Database:** {PostgreSQL | MySQL | MongoDB | ...}
- **ORM:** {Prisma | TypeORM | Sequelize | none}
- **Migration tool:** {prisma migrate | knex | manual}

## Entities

| Entity | Description | Key fields |
|--------|------------|------------|
| {Model} | {what it represents} | {important columns + types} |

## Relationships

```
{entity relationship diagram — ASCII}

Example:
  User 1──* Post
  User 1──* Comment
  Post 1──* Comment
  Post *──* Tag
```

## Indexes

| Table | Index | Purpose |
|-------|-------|---------|
| {table} | {columns} | {why — performance, uniqueness} |

## Enums / Constants

| Name | Values | Used by |
|------|--------|---------|
| {enum} | {value1, value2, ...} | {which models} |
