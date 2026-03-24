# Docs Heuristics by Project Type

PM uses these when initializing docs/ or writing specs. Match project type to heuristics.

---

## Web Application

**project.md additions:** frontend framework, backend framework, DB, auth approach
**spec.md emphasis:** user flows (Given/When/Then), API contracts, data model, error states
**rules/ defaults:** git-flow (feature branches), REST conventions, test pyramid (unit + integration + e2e)
**constitution additions:** no direct DB queries in UI layer, auth checked at middleware

---

## CLI Tool

**project.md additions:** target OS, installation method, shell compatibility
**spec.md emphasis:** command syntax, flags, stdin/stdout behavior, exit codes
**rules/ defaults:** semver, man page conventions, backward compatibility policy
**constitution additions:** all output to stdout, errors to stderr, JSON output flag for scripting

---

## Library / SDK

**project.md additions:** target consumers, public API surface, versioning policy
**spec.md emphasis:** public API signatures, behavior contracts, error types
**rules/ defaults:** strict semver, changelog required, no breaking changes in minor versions
**constitution additions:** every public function documented, all errors typed not stringly-typed

---

## Data Pipeline

**project.md additions:** data sources, sinks, volume estimates, SLA
**spec.md emphasis:** schema in/out, transformation logic, idempotency, failure handling
**rules/ defaults:** idempotent by default, checkpoint every N records, no data loss on failure
**constitution additions:** always validate schema on input, log record counts at each stage

---

## General Rule

If project type is unclear, use Web Application defaults. PM updates rules/ once type is confirmed.
