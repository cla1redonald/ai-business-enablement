#!/usr/bin/env bash
# Runs the whole toolchain against the synthetic Caldergate fixture and prints one
# line per step. Works from a clean clone. The fixture is copied to a temp directory,
# so nothing in the repo changes; the temp directory is removed on exit.
#
# Needs: python3 (3.10 or later) and openpyxl (pip install -r requirements.txt).
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURE="$REPO/fixtures/caldergate/workspace"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/abe-demo.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

# Run a step quietly; show its full output only if it fails. The last line of the
# tool's output, trimmed to its first sentence or clause, becomes the summary.
run() {
  local label="$1"; shift
  local out
  if ! out="$("$@" 2>&1)"; then
    printf '[FAIL] %s\n' "$label" >&2
    printf '%s\n' "$out" >&2
    exit 1
  fi
  LAST_OUT="$out"
}

summary() { printf '[ ok ] %-22s %s\n' "$1" "$2"; }

cd "$REPO"

run "self-test" python3 tools/check.py --self-test
rules="$(printf '%s\n' "$LAST_OUT" | grep -c '^  \[ok  \]')"
summary "self-test" "$rules rules and budgets each proved against a poison and a clean fixture"

run "observations" python3 tools/check.py --observations "$FIXTURE" \
  --config "$FIXTURE/check.config.json"
summary "observations check" "$(printf '%s\n' "$LAST_OUT" | tail -n 1 | sed 's/ Mechanical checks pass\..*/ Mechanical checks pass./')"

# Everything below writes into a throwaway copy of the workspace.
mkdir -p "$WORK/ws"
(cd "$FIXTURE" && tar --exclude=./packs -cf - .) | (cd "$WORK/ws" && tar -xf -)

run "facts" python3 tools/facts.py "$WORK/ws"
summary "facts" "$(printf '%s\n' "$LAST_OUT" | sed 's/ -> .*//')"

if cmp -s "$WORK/ws/facts.json" "$FIXTURE/facts.json"; then
  summary "facts vs committed" "regenerated facts.json is identical to the committed file"
else
  printf '[FAIL] facts vs committed: regenerated facts.json differs from %s\n' \
    "$FIXTURE/facts.json" >&2
  diff "$FIXTURE/facts.json" "$WORK/ws/facts.json" | head -20 >&2 || true
  exit 1
fi

run "workbook" python3 tools/workbook.py "$WORK/ws"
sheets="$(python3 - "$WORK/ws/artefacts/workbook.xlsx" <<'PY'
import sys
import openpyxl
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
print(f"{len(wb.sheetnames)} sheets")
PY
)"
summary "workbook" "workbook.xlsx built, $sheets"

run "check report" python3 tools/check.py "$WORK/ws/artefacts/report.md" \
  --config "$WORK/ws/check.config.json" --facts "$WORK/ws/facts.json"
summary "check report" "$(printf '%s\n' "$LAST_OUT" | tail -n 1 | sed 's/\. Warnings are judgement calls.*/./')"

run "pack" python3 tools/pack.py "$WORK/ws" --version 1
summary "pack" "baseline V1 built and audited clean, zipped (temp dir, removed on exit)"

printf '\nDemo complete: every step passed, repository untouched.\n'
