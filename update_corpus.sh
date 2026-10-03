#!/usr/bin/env bash
# update_corpus.sh — bring the 93 anthropics source snapshots up to upstream HEAD.
#
# Why: films are built from these sources, so they should be as current as
# Anthropic's repos (Bear, 2026-09-27). bootstrap.sh restores the PINNED
# snapshots; this script moves the pins forward.
#
# Per repo in repositories.json:
#   1. git ls-remote the default branch; if HEAD == pinned sha, skip.
#   2. shallow-clone HEAD into _update_tmp/<name> (one at a time: disk is tight).
#   3. files that exist locally but not upstream (outside youtube/) are MOVED to
#      _superseded-clones/<date>/<name>/, never deleted; our reels in <name>/youtube/
#      are never touched.
#   4. rsync the new tree over the snapshot (no .git, no youtube/).
#   5. record sha / prev_sha / updated_at in repositories.json.
# Old snapshots stay recoverable exactly: prev_sha + bootstrap.sh.
#
# Usage: ./update_corpus.sh [repo-name ...]   (no args = all repos)
set -uo pipefail
cd "$(dirname "$0")"
MANIFEST=repositories.json
TMP=_update_tmp
DAY=$(date +%F)
KEEP="_superseded-clones/$DAY"
mkdir -p "$TMP" "$KEEP"
LOG="update_corpus-$DAY.log"

only=("$@")
python3 - "$MANIFEST" ${only[@]+"${only[@]}"} > "$TMP/list.tsv" <<'EOF'
import json, sys
d = json.load(open(sys.argv[1])); only = set(sys.argv[2:])
for r in d["repositories"]:
    if only and r["name"] not in only: continue
    print("\t".join([r["name"], r["clone_url"], r.get("default_branch") or "main", r.get("sha") or ""]))
EOF

updated=0; same=0; failed=0
while IFS=$'\t' read -r name url branch pinned; do
  [ -d "$name" ] || { echo "[miss]  $name (no local folder)" | tee -a "$LOG"; continue; }
  head=$(git ls-remote "$url" "refs/heads/$branch" 2>/dev/null | cut -f1)
  if [ -z "$head" ]; then echo "[fail]  $name: ls-remote" | tee -a "$LOG"; failed=$((failed+1)); continue; fi
  if [ "$head" = "$pinned" ]; then echo "[same]  $name ${head:0:8}" | tee -a "$LOG"; same=$((same+1)); continue; fi
  rm -rf "${TMP:?}/$name"
  if ! git clone --quiet --depth 1 --branch "$branch" "$url" "$TMP/$name" 2>>"$LOG"; then
    echo "[fail]  $name: clone" | tee -a "$LOG"; failed=$((failed+1)); continue
  fi
  # local-only files (would be deleted by --delete): move them aside first
  rsync -a --delete --dry-run --itemize-changes --exclude='.git' --exclude='/youtube/' \
        "$TMP/$name/" "$name/" | awk '/^\*deleting /{sub(/^\*deleting +/,""); print}' > "$TMP/$name.gone"
  moved=0
  while IFS= read -r rel; do
    [ -z "$rel" ] && continue
    src="$name/$rel"; [ -e "$src" ] || continue
    [ -d "$src" ] && continue            # dirs empty out as their files move
    mkdir -p "$KEEP/$name/$(dirname "$rel")"
    mv "$src" "$KEEP/$name/$rel" && moved=$((moved+1))
  done < "$TMP/$name.gone"
  find "$name" -mindepth 1 -type d -empty -not -path "$name/youtube*" -delete 2>/dev/null
  rsync -a --exclude='.git' --exclude='/youtube/' "$TMP/$name/" "$name/"
  rm -rf "${TMP:?}/$name" "$TMP/$name.gone"
  python3 - "$MANIFEST" "$name" "$head" "$DAY" <<'EOF'
import json, sys
p, name, head, day = sys.argv[1:]
d = json.load(open(p))
for r in d["repositories"]:
    if r["name"] == name:
        r["prev_sha"] = r.get("sha"); r["sha"] = head; r["updated_at"] = day
json.dump(d, open(p, "w"), indent=2); open(p, "a").write("\n")
EOF
  echo "[upd]   $name ${pinned:0:8} -> ${head:0:8} (local-only files kept aside: $moved)" | tee -a "$LOG"
  updated=$((updated+1))
done < "$TMP/list.tsv"
echo "done: updated=$updated same=$same failed=$failed  (log: $LOG, set-aside: $KEEP)" | tee -a "$LOG"
