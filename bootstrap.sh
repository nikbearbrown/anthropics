#!/usr/bin/env bash
# bootstrap.sh — re-clone the analysis corpus.
#
# This repo holds the ANALYSIS (beat sheets, scripts, notes) but not the code
# being analysed. The 93 anthropics repos are public and re-clonable; this
# script restores them to their original relative paths so every reel folder
# sits back inside its source repo and git-explainer's --verify (LOC == cloc,
# churn == git log, diff == git show) resolves exactly as it did originally.
#
# If repositories.json carries a pinned "sha", the clone is checked out at that
# commit — so the analysis is reproducible against the code it actually read,
# not against whatever upstream has become since.
set -uo pipefail

MANIFEST="${1:-repositories.json}"
[ -f "$MANIFEST" ] || { echo "manifest not found: $MANIFEST" >&2; exit 1; }

total=0; cloned=0; skipped=0; failed=0

while IFS=$'\t' read -r name url sha; do
  total=$((total+1))
  if [ -d "$name/.git" ]; then
    echo "[skip]  $name (already present)"
    skipped=$((skipped+1)); continue
  fi
  echo "[clone] $name"
  if git clone --quiet "$url" "$name" 2>/dev/null; then
    if [ -n "$sha" ] && [ "$sha" != "null" ]; then
      ( cd "$name" && git checkout --quiet "$sha" 2>/dev/null ) \
        && echo "        pinned at ${sha:0:8}" \
        || echo "        WARNING: could not check out $sha — left at default branch"
    fi
    cloned=$((cloned+1))
  else
    echo "        FAILED: $url" >&2
    failed=$((failed+1))
  fi
done < <(python3 -c "
import json,sys
d=json.load(open('$MANIFEST'))
for r in d['repositories']:
    print('\t'.join([r['name'], r.get('clone_url',''), str(r.get('sha') or '')]))
")

echo
echo "corpus: $total in manifest | $cloned cloned | $skipped already present | $failed failed"
[ "$failed" -eq 0 ] || exit 1
