# Decision: docs/ Structure

Date: 2026-03-30

## Only one BASE file

**Decision:** `docs/project.md` is the only file that always exists. Everything else is organic — created when there is real content to write.

**Why:** Pre-creating empty directories is noise. Structure should grow from the project, not be imposed on it. If it doesn't have content, it doesn't exist.

---

## Two scopes inside docs/

**Decision:** `docs/` = project truth. `docs/.pa/` = PA's internal brain.

- `docs/` — dual-purpose: PA reads it, humans read it. Contains project-facing content.
- `docs/.pa/` — PA's cognitive state: state.md, learnings/, concerns/, worker-reports/.

**Why:** PA's working artifacts (what it's tracking, what it's learned, what it's worried about) are not project documentation. Mixing them confuses humans browsing docs and wastes context when PA loads memory. Dot-prefix signals internal — consistent with `.git/`, `.claude/`.

---

## PA brain is always BASE

**Decision:** `docs/.pa/state.md`, `docs/.pa/learnings/`, `docs/.pa/concerns/`, `docs/.pa/worker-reports/` are BASE — always exist for any project.

**Why:** These are PA's working memory. Without state.md, PA doesn't know where it is. Without learnings/ and concerns/, PA has nowhere to write what it accumulates. They are infrastructure, not content — they should always be there.

---

## decisions/ is organic

**Decision:** `docs/decisions/` is part of the organic layer — created only when important architectural choices are made.

**Why:** Not every project has decisions worth recording as ADR. Creating decisions/ upfront implies it must be filled. It should appear when the first real decision is made — not before.
