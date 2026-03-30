# Announcements

Every action starts with an announcement. Never work silently.

---

## Format by level

**Action start** — one per action, always:
```
---
{icon} **{Action}** — {context}
---
```

**Substep** — for notable transitions within an action:
```
↳ *{substep}*: {detail}
```

**Completion** — when action fully done:
```
✓ **{Action} complete** — {summary}
```

**Concern / issue**:
```
⚠ **{issue}** — {what was tried} → {recommendation}
```

---

## Action registry

| Action  | Icon | Required context                                   |
|---------|------|----------------------------------------------------|
| clarify | 🔍   | `📁 {project}` · `💾 memory: OK \| missing`       |
| init    | 🏗️   | `mode: new \| existing`                            |
| spec    | 📐   | `feature: {name}`                                  |
| plan    | 📋   | `{N} tasks · {M} waves`                            |
| execute | 🚀   | `wave {W}/{T}` · `{N} tasks`                       |
| verify  | ✅   | `{N} acceptance criteria`                          |
| debug   | 🔧   | `trigger: verify \| execute` · `{symptom}`         |

---

## Rules

- Announce at the **very start** — before any tool call.
- Context must be specific. `feature: auth` not `feature: {name}`.
- Substeps only for transitions user would want to track.
- Never announce twice for the same action.
