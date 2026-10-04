#!/bin/sh
set -eu
export PYTHONDONTWRITEBYTECODE=1
case "$0" in
  */*) tool_dir=${0%/*} ;;
  *) tool_dir=. ;;
esac
script_dir=$(CDPATH= cd -- "$tool_dir" && pwd)
if ! command -v nix >/dev/null 2>&1; then
  echo "skill-graph: Nix is required (flakes enabled); install it using your approved method." >&2
  exit 127
fi
if [ "${1-}" = "--help" ] || [ "${1-}" = "-h" ]; then
  exec nix develop --no-update-lock-file --no-write-lock-file "path:$script_dir" --command python "$script_dir/graph.py" --help
fi
exec nix develop --no-update-lock-file --no-write-lock-file "path:$script_dir" --command python "$script_dir/graph.py" "$@"
