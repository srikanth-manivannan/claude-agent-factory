#!/usr/bin/env sh
# Helper for the {{NAME}} skill.
# Portable POSIX shell per ARCHITECTURE §9. Declare any extra runtime in metadata.yaml.
#
# Usage: example-helper.sh <arg>
set -eu

if [ "$#" -lt 1 ]; then
  echo "usage: $(basename "$0") <arg>" >&2
  exit 64   # EX_USAGE
fi

ARG="$1"

# TODO: implement helper logic.
echo "{{NAME}} helper received: ${ARG}"
