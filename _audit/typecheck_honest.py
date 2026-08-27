#!/usr/bin/env python3
"""typecheck_honest.py — GATE T §8.1 measured the way it was specified.

Differences from runtime/scripts/type_check.py, each a bug that made tiny type PASS:
  1. FLOOR: 3.2% of the PHYSICAL frame height (69px at 2160), not of a presumed
     1080 "logical" height (35px). The halving has no basis in the rendered file.
  2. GLYPH-SHAPED BLOBS COUNT: the old filter required width >= height*1.5, so an
     upright letter (taller than wide) was discarded as "not a text run" — which is
     exactly what small, loosely-tracked type looks like.
  3. NOISE FLOOR: old min_h = max(15, 0.7% of h) = 15px at 4K silently ate body text
     measured at 15-21px. Here the noise floor is 8px and anything above it is text.
  4. EMPTY RESULT = FAIL, not PASS. "No text blobs detected" means the check could
     not verify the frame, which is not the same as the frame being compliant.
  5. NO EXEMPTIONS. Reports what is there.

Usage: typecheck_honest.py <reel_dir> [more dirs...]
"""
import sys, os, subprocess, tempfile, json
import numpy as np
from PIL import Image

FLOOR_PCT = 3.2

def frames(mp4, n=6):
    out=[]
    with tempfile.TemporaryDirectory() as td:
        dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries",
             "format=duration","-of","csv=p=0",mp4]).decode().strip() or 0)
        for i in range(n):
            t=dur*(i+0.5)/n
            p=os.path.join(td,f"f{i}.png")
            subprocess.run(["ffmpeg","-v","error","-y","-ss",str(t),"-i",mp4,
                            "-frames:v","1",p],check=False)
            if os.path.exists(p): out.append(np.asarray(Image.open(p).convert("L"),dtype=np.uint8))
    return out

def label(mask):
    """4-connected component labelling, iterative (no scipy dependency)."""
    H,W=mask.shape; lab=np.zeros((H,W),np.int32); cur=0; boxes=[]
    for y in range(H):
        row=mask[y]
        xs=np.nonzero(row)[0]
        for x in xs:
            if lab[y,x]: continue
            cur+=1; stack=[(y,x)]; lab[y,x]=cur
            x0=x1=x; y0=y1=y
            while stack:
                cy,cx=stack.pop()
                if cx<x0:x0=cx
                if cx>x1:x1=cx
                if cy<y0:y0=cy
                if cy>y1:y1=cy
                for ny,nx in ((cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)):
                    if 0<=ny<H and 0<=nx<W and mask[ny,nx] and not lab[ny,nx]:
                        lab[ny,nx]=cur; stack.append((ny,nx))
            boxes.append((x0,y0,x1,y1))
    return boxes

def measure(img):
    H,W=img.shape
    floor=FLOOR_PCT*H/100.0
    # downscale 4x for tractable labelling, scale results back
    small=np.asarray(Image.fromarray(img).resize((W//4,H//4),Image.LANCZOS),dtype=np.uint8)
    dark = small < 140
    frac = dark.mean()
    if frac > 0.5: dark = small > 200      # dark-polarity frame
    boxes=label(dark)
    hs=[]
    for x0,y0,x1,y1 in boxes:
        h=(y1-y0+1)*4; w=(x1-x0+1)*4
        if h < 8: continue                       # true speck
        if h > H*0.5: continue                   # background fill
        if w > h*15: continue                    # horizontal rule
        hs.append(h)
    return floor, hs

def main():
    print(f"{'reel':52} {'floor':>6} {'minH':>6} {'#below':>7} {'#text':>6}  verdict")
    for d in sys.argv[1:]:
        mp4s=[f for f in os.listdir(d) if f.endswith('.mp4')]
        if not mp4s: continue
        m=os.path.join(d,max(mp4s,key=lambda f:os.path.getsize(os.path.join(d,f))))
        allh=[]; floor=0
        for img in frames(m):
            floor,hs=measure(img); allh+=hs
        if not allh:
            print(f"{os.path.basename(d)[:52]:52} {floor:6.0f} {'-':>6} {'-':>7} {0:6}  FAIL (no text measurable)")
            continue
        below=[h for h in allh if h<floor]
        v = "FAIL" if below else "PASS"
        print(f"{os.path.basename(d)[:52]:52} {floor:6.0f} {min(allh):6} {len(below):7} {len(allh):6}  {v}")

main()
