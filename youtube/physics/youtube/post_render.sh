#!/usr/bin/env bash
# Run after rerender_4k.sh completes.
# Flow: type_check (writes TYPECHECK.md) → if PASS: art post → verify staged.json.
set -uo pipefail
BOOKS="/Users/bear/Documents/CoWork/bear-textbooks/books"
ART="$BOOKS/brutalist-art/art"
TC="$BOOKS/brutalist-art/runtime/scripts/type_check.py"
LOG="$BOOKS/physics/youtube/post_render.log"
: > "$LOG"

process_reel() {
    local reel="$1"
    local reel_dir="$BOOKS/$reel"
    local slug
    slug=$(basename "$reel")
    echo "" | tee -a "$LOG"
    echo "=== $slug ===" | tee -a "$LOG"
    cd "$BOOKS"

    echo "--- GATE T ---" | tee -a "$LOG"
    python3 "$TC" "$reel_dir" 2>&1 | tee -a "$LOG" | grep "Overall:"
    local gate
    gate=$(grep "Overall:" "$reel_dir/TYPECHECK.md" 2>/dev/null | head -1)
    echo "Result: $gate" | tee -a "$LOG"
    if echo "$gate" | grep -q "FAIL"; then
        echo "GATE T FAIL — see TYPECHECK.md; skipping art post" | tee -a "$LOG"
        # Show which beats failed
        grep "\*\*FAIL\*\*" "$reel_dir/TYPECHECK.md" | head -5 | tee -a "$LOG"
        return 1
    fi

    echo "--- art post ---" | tee -a "$LOG"
    "$ART" post "$reel" 2>&1 | tee -a "$LOG" | tail -10

    echo "--- staged entry ---" | tee -a "$LOG"
    python3 -c "
import json
from pathlib import Path
s = json.loads(Path('$BOOKS/youtube/TOPOST/staged.json').read_text())
for e in s.get('videos', []):
    if e.get('slug','') == '$slug':
        print(json.dumps(e, indent=2))
        break
else:
    print('not found in staged.json')
" 2>&1 | tee -a "$LOG"
}

process_reel physics/youtube/position-momentum-uncertainty
process_reel physics/youtube/one-atom-farther-cuts-current-tenfold
process_reel physics/youtube/wave-leaks-into-forbidden-wall
process_reel physics/youtube/two-spots-not-a-smear-bb

echo "" | tee -a "$LOG"
echo "=== POST-RENDER DONE ===" | tee -a "$LOG"
echo "Check $LOG for results."
