#!/usr/bin/env sh
# Shared helpers for generators/. POSIX sh, no required runtime (pure scaffolding).
set -eu

GEN_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$GEN_DIR/../.." && pwd)
export ROOT

if [ -t 1 ]; then GRN='\033[32m'; YEL='\033[33m'; RED='\033[31m'; Z='\033[0m';
else GRN=''; YEL=''; RED=''; Z=''; fi
say()  { printf '%s\n' "$*"; }
ok()   { printf "${GRN}%s${Z}\n" "$*"; }
warn() { printf "${YEL}WARN ${Z}%s\n" "$*"; }
die()  { printf "${RED}ERROR ${Z}%s\n" "$*" >&2; exit 1; }

KEBAB='^[a-z0-9]+(-[a-z0-9]+)*$'
require_kebab() {
  printf '%s' "$1" | grep -Eq "$KEBAB" || die "'$1' must be kebab-case (a-z, 0-9, hyphens)."
}

today()        { date +%F; }
min_standard() { cat "$ROOT/standards/VERSION" 2>/dev/null || echo "0.1.0"; }
author()       { echo "${FACTORY_AUTHOR:-@your-handle}"; }

# kebab-case -> Title Case (portable, no GNU sed extensions)
titlecase() {
  printf '%s' "$1" | awk -F- '{for(i=1;i<=NF;i++)$i=toupper(substr($i,1,1)) substr($i,2)}1' OFS=' '
}

ensure_new_dir() { [ -e "$1" ] && die "$1 already exists."; mkdir -p "$1"; }
