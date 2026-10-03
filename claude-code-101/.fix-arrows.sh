#!/usr/bin/env bash
# fix the doubled ↓ on status lines: three published films + clear-vs-compact; serialized behind the running compiles
cd /Users/bear/Documents/CoWork/bear-textbooks/books
S=/private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad
until grep -q "=== FINAL DONE ===\|FAILED\|ERROR\|Traceback" "$S/context-cost-build2.log"; do sleep 20; done
fix(){ # <reel-rel-path>
  local R="$1"
  python3 - "$R" <<'PY'
import json, os, sys
R=sys.argv[1]; d=json.load(open(f"{R}/beat_sheet.json")); changed=[]
for b in d["beats"]:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        for blk in r["props"]["blocks"]:
            if blk.get("type")=="status" and blk.get("tokens","").startswith("↓ "):
                blk["tokens"]=blk["tokens"][2:]; changed.append(b["beat_id"])
for b in d["beats"]:
    if b["beat_id"] in changed:
        b["shot"]["remotion"]["rendered"]={"out":"","at":""}; b.pop("build",None)
        m=f"{R}/media/{b['beat_id']}.mp4"; os.path.exists(m) and os.remove(m)
json.dump(d,open(f"{R}/beat_sheet.json","w"),indent=2,ensure_ascii=False)
p=f"{R}/author_sheet.py"; s=open(p).read().replace('"tokens": "↓ ','"tokens": "').replace('"tokens":"↓ ','"tokens":"'); open(p,'w').write(s)
print(R, "arrows fixed on", changed)
PY
  local slug; slug=$(basename "$R"); rm -f "$R/$slug.mp4" "$R/$slug-slate.mp4" "$R/.render.lock"
  ./brutalist-art/art run "$R" && echo "=== RUN DONE $slug ===" && ./brutalist-art/art final "$R" && echo "=== FINAL DONE $slug ==="
}
for R in anthropics/claude-code-101/00-what-it-is/cc-vibecoders-welcome anthropics/claude-code-101/00-what-it-is/cc-agentic-harness anthropics/claude-code-101/00-what-it-is/cc-five-claudes-explained; do fix "$R"; done
until grep -q "FINAL DONE cc-clear-vs-compact\|##### starting cc101loop" anthropics/claude-code-101/.cc101loop/overnight.log; do sleep 20; done
fix anthropics/claude-code-101/01-context-and-memory/cc-clear-vs-compact
echo "=== ARROWS ALL DONE ==="
