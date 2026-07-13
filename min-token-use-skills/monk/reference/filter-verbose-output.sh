#!/usr/bin/env bash
# Reference hook helper: shrink verbose command output to failure/error lines.
# Intended for a Claude Code PostToolUse hook that filters Bash tool output.
# Usage: <command-output> | ./filter-verbose-output.sh [max_lines]
# Prints lines matching failure/error patterns, capped at max_lines (default 100).
# If nothing matches, prints a single summary line so context still gets a signal.
set -euo pipefail
max_lines="${1:-100}"
matched="$(grep -E -i 'FAIL|ERROR|error:|Exception|Traceback|✗' || true)"
if [ -z "$matched" ]; then
  echo "[no failures/errors detected in output]"
else
  printf '%s\n' "$matched" | head -n "$max_lines"
fi
