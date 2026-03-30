#!/bin/bash
# Verify init output for an existing project.
# Usage: bash verify-init.sh /path/to/project
#
# Checks skeleton + cross-references docs-map.md vs filesystem.
# Run AFTER init completes.

PROJECT_ROOT="${1:-.}"
PASS=0; FAIL=0; WARN=0

check() {
  if [ -e "$PROJECT_ROOT/$1" ]; then
    echo "  PASS $2"; ((PASS++))
  else
    echo "  FAIL $2 — missing: $1"; ((FAIL++))
  fi
}

check_not_empty() {
  if [ -s "$PROJECT_ROOT/$1" ]; then
    echo "  PASS $2"; ((PASS++))
  elif [ -e "$PROJECT_ROOT/$1" ]; then
    echo "  WARN $2 — exists but empty"; ((WARN++))
  else
    echo "  FAIL $2 — missing: $1"; ((FAIL++))
  fi
}

check_state_format() {
  local path="$PROJECT_ROOT/docs/state.md"
  [ ! -f "$path" ] && echo "  FAIL state.md — missing" && ((FAIL++)) && return
  if grep -qi "ACTIVE DEVELOPMENT\|Last Known\|Backend:.*functional" "$path" 2>/dev/null; then
    echo "  FAIL state.md — contains project status (must be orchestrator tracking only)"; ((FAIL++))
  else
    echo "  PASS state.md — orchestrator tracking format"; ((PASS++))
  fi
}

check_docs_map() {
  local path="$PROJECT_ROOT/docs/docs-map.md"
  [ ! -f "$path" ] && echo "  FAIL docs-map.md — missing" && ((FAIL++)) && return
  if grep -q "To be written by Step 1 agent" "$path"; then
    echo "  FAIL docs-map.md — still placeholder (Step 1 agent did not run)"; ((FAIL++))
    return
  fi
  if grep -q '```yaml' "$path"; then
    echo "  PASS docs-map.md — has YAML block"; ((PASS++))
  else
    echo "  FAIL docs-map.md — no yaml block"; ((FAIL++))
  fi
}

cross_check_features() {
  local docs_map="$PROJECT_ROOT/docs/docs-map.md"
  [ ! -f "$docs_map" ] && echo "  SKIP cross-check — docs-map.md missing" && return
  grep -q "To be written" "$docs_map" && echo "  SKIP cross-check — docs-map.md not ready" && return

  local expected
  expected=$(awk '/```yaml/{f=1;next} /```/{f=0} f && /name:/{print}' "$docs_map" \
             | sed 's/.*name:[[:space:]]*//' | tr -d '"'"'" | xargs)

  if [ -z "$expected" ]; then
    echo "  PASS cross-check — no features (single-unit project)"; ((PASS++)); return
  fi

  for feature in $expected; do
    if [ -d "$PROJECT_ROOT/docs/features/$feature" ]; then
      echo "  PASS cross-check: features/$feature/"; ((PASS++))
    else
      echo "  FAIL cross-check: features/$feature/ — in docs-map but missing on disk"; ((FAIL++))
    fi
  done

  # Reverse: dirs on disk not in docs-map
  if [ -d "$PROJECT_ROOT/docs/features" ]; then
    for d in "$PROJECT_ROOT/docs/features"/*/; do
      [ -d "$d" ] || continue
      feat=$(basename "$d")
      if ! echo "$expected" | grep -qw "$feat"; then
        echo "  WARN cross-check: features/$feat/ — on disk but not in docs-map"; ((WARN++))
      fi
    done
  fi
}

# ---

echo ""
echo "Verifying: $PROJECT_ROOT"
echo ""

echo "--- Skeleton (Step 0) ---"
check "docs"             "docs/"
check "docs/project.md"  "project.md"
check "docs/state.md"    "state.md"
check "docs/docs-map.md" "docs-map.md"
check "docs/decisions"   "decisions/"
check "docs/concerns"    "concerns/"
check "docs/.tmp"        ".tmp/"

echo ""
echo "--- Content quality ---"
check_state_format
check_docs_map
check_not_empty "docs/project.md" "project.md has content"

echo ""
echo "--- Rules ---"
check           ".claude/rules"                    ".claude/rules/"
check_not_empty ".claude/rules/constitution.md"    "constitution.md"
check_not_empty ".claude/rules/memory-structure.md" "memory-structure.md"

echo ""
echo "--- Cross-check: docs-map.md vs filesystem ---"
cross_check_features

echo ""
echo "--- Foundations ---"
FOUND=0
for f in "$PROJECT_ROOT"/docs/foundations/*.md; do
  [ -f "$f" ] && ((FOUND++))
done
if [ $FOUND -gt 0 ]; then
  echo "  PASS $FOUND foundation file(s)"; ((PASS++))
else
  echo "  WARN No foundation docs (expected for most projects)"; ((WARN++))
fi

echo ""
echo "========================="
echo "Pass: $PASS  Fail: $FAIL  Warn: $WARN"
[ $FAIL -eq 0 ] && echo "All checks passed" || echo "$FAIL check(s) failed"
echo ""
