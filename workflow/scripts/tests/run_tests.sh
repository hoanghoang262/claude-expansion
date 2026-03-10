#!/usr/bin/env bash
set -e
REPO_ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
~/.local/bin/pytest "$REPO_ROOT/workflow/" --import-mode=importlib -v "$@"
