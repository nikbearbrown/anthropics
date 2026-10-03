#!/usr/bin/env bash
# overnight chain, started 2026-09-09: finish the two hand-built reels' compiles, then run the loop.
cd /Users/bear/Documents/CoWork/bear-textbooks/books
until grep -q "=== FINAL DONE ===\|FAILED\|ERROR\|Traceback" "/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/context-cost-build.log"; do sleep 20; done
echo "### context-cost finished: $(grep -c 'FINAL DONE' /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/context-cost-build.log)"
for r in cc-clear-vs-compact cc-context-check; do
  echo "##### $r $(date)"; ./brutalist-art/art run anthropics/claude-code-101/01-context-and-memory/$r && echo "=== RUN DONE $r ===" && ./brutalist-art/art final anthropics/claude-code-101/01-context-and-memory/$r && echo "=== FINAL DONE $r ==="
done
echo "##### starting cc101loop $(date)"
cd anthropics && ./cc101loop.sh
