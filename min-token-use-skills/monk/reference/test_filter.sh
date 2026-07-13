#!/usr/bin/env bash
set -euo pipefail
dir="$(cd "$(dirname "$0")" && pwd)"
script="$dir/filter-verbose-output.sh"

pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; echo "got: [$2]"; exit 1; }

# Test 1: keeps only failure/error lines, drops PASS lines
out="$(printf 'PASS test_a\nFAIL test_b\nERROR: boom\nPASS test_c\n' | bash "$script")"
expected="$(printf 'FAIL test_b\nERROR: boom')"
[ "$out" = "$expected" ] || fail "drops PASS lines" "$out"
pass "drops PASS lines"

# Test 2: no matches -> single summary line
out="$(printf 'PASS test_a\nPASS test_b\n' | bash "$script")"
[ "$out" = "[no failures/errors detected in output]" ] || fail "no-match summary" "$out"
pass "no-match summary"

# Test 3: caps at max_lines
big="$(seq 1 50 | sed 's/^/ERROR line /')"
out="$(printf '%s\n' "$big" | bash "$script" 10 | wc -l)"
[ "$out" = "10" ] || fail "max_lines cap" "$out"
pass "max_lines cap"

echo "ALL HOOK TESTS PASSED"
