#!/usr/bin/env bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books
until grep -q "=== ARROWS ALL DONE ===" anthropics/claude-code-101/.cc101loop/fix-arrows.log; do sleep 30; done
for R in anthropics/claude-code-101/01-context-and-memory/cc-claude-md anthropics/claude-code-101/01-context-and-memory/cc-claude-md-length; do
  python3 - "$R" <<'PY'
import json, os, sys
R=sys.argv[1]; d=json.load(open(f"{R}/beat_sheet.json")); changed=[]
for b in d["beats"]:
    r=b["shot"]["remotion"]
    if r["pattern"]=="CCSession":
        for blk in r["props"]["blocks"]:
            if blk.get("type")=="status" and blk.get("tokens","").startswith("↓ "): blk["tokens"]=blk["tokens"][2:]; changed.append(b["beat_id"])
for b in d["beats"]:
    if b["beat_id"] in changed:
        b["shot"]["remotion"]["rendered"]={"out":"","at":""}; b.pop("build",None); m=f"{R}/media/{b['beat_id']}.mp4"; os.path.exists(m) and os.remove(m)
json.dump(d,open(f"{R}/beat_sheet.json","w"),indent=2,ensure_ascii=False)
p=f"{R}/author_sheet.py"; s=open(p).read().replace('"tokens": "↓ ','"tokens": "').replace('"tokens":"↓ ','"tokens":"'); open(p,'w').write(s); print(R, changed)
PY
  slug=$(basename "$R"); rm -f "$R/$slug.mp4" "$R/$slug-slate.mp4" "$R/.render.lock"
  ./brutalist-art/art run "$R" && echo "=== RUN DONE $slug ===" && ./brutalist-art/art final "$R" && echo "=== FINAL DONE $slug ==="
done
echo "=== ARROWS2 DONE ==="
