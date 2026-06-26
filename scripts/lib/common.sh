#!/usr/bin/env sh
# Shared helpers for scripts/. POSIX sh. No required runtime for the basic path.
set -eu

# Repo root = parent of scripts/
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
export ROOT

# Colors only when stdout is a tty
if [ -t 1 ]; then RED='\033[31m'; YEL='\033[33m'; GRN='\033[32m'; Z='\033[0m';
else RED=''; YEL=''; GRN=''; Z=''; fi

info()  { printf '%s\n' "$*"; }
warn()  { printf "${YEL}WARN ${Z}%s\n" "$*"; }
err()   { printf "${RED}FAIL ${Z}%s\n" "$*" >&2; }
ok()    { printf "${GRN}%s${Z}\n" "$*"; }

# Locate a WORKING Python (for the optional validation/index adapter).
# Probes candidates by actually running one — skips broken shims (e.g. the
# Windows Store python alias) that exist on PATH but don't execute.
find_python() {
  for c in python3 python py; do
    if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys' >/dev/null 2>&1; then
      command -v "$c"; return 0
    fi
  done
  return 1
}

# Artifact spec dirs (skills are nested one level deeper)
ARTIFACT_GLOBS="skills/*/* agents/* workflows/* teams/* playbooks/*"

# List artifact directories that contain a metadata.yaml
list_artifacts() {
  for g in $ARTIFACT_GLOBS; do
    for d in "$ROOT"/$g; do
      [ -f "$d/metadata.yaml" ] && printf '%s\n' "$d"
    done
  done
}
