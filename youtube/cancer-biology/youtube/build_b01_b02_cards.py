#!/usr/bin/env python3
"""
Patch B01 and B02 in all 20 cancer-biology cli-explainer reels to use
ClaudeWindow artifact cards (Claude default skin: cream / terracotta).

Steps:
  1. Parse narration_text → ClaudeWindow props (title, heading, lines, sparkLine)
  2. Write remotion block into beat_sheet.json for B01 and B02
  3. Run remotion_scenes.py to render media/B01.mp4 + media/B02.mp4
  4. Run compile.py to produce final cut (no slates remain)
"""

import json, re, subprocess, sys, textwrap
from pathlib import Path
from datetime import datetime

BASE = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
ART  = BASE / "brutalist-art"
RUNTIME = ART / "runtime" / "scripts"

REELS = [
    "p53-circuit", "telomere-crisis", "rb-convergence", "restriction-point",
    "bypass-track", "spindle-checkpoint", "clonal-evolution", "synthetic-lethality",
    "apoptosis-momp", "bcl-selectivity", "differentiation-block",
    "mgmt-methylation-paradox", "mtap-passenger", "immune-starvation",
    "protein-level-loss", "hpylori-cancer", "mir-deletion", "hpv-dual-hit",
    "warburg-carbon", "venetoclax-priming",
]

def slug_to_title(slug: str) -> str:
    """e.g. 'p53-circuit' → 'p53 Circuit'"""
    parts = slug.split("-")
    return " ".join(p.upper() if p.upper() in {"P53","RB","BCL","HPV","MTAP","MGMT","MIR"} else p.capitalize()
                    for p in parts)

def sentences(text: str) -> list[str]:
    """Split narration into clean sentences."""
    raw = re.split(r'(?<=[.!?])\s+', text.strip())
    out = []
    for s in raw:
        s = s.strip().rstrip(".")
        if s:
            out.append(s)
    return out

def make_props(narration: str, beat: str, slug: str) -> dict:
    """Convert narration text into ClaudeWindow artifact props."""
    sents = sentences(narration)
    if not sents:
        sents = [narration[:120]]

    if beat == "B01":
        artifact_title = "The mechanism"
        artifact_heading = slug_to_title(slug)
    elif beat == "B02":
        artifact_title = "The stakes"
        artifact_heading = slug_to_title(slug)
    else:  # B08
        artifact_title = "The lesson"
        artifact_heading = slug_to_title(slug)

    # Lines: up to 4 sentences; sparkLine = last sentence
    if len(sents) == 1:
        lines = [sents[0]]
        spark = sents[0]
    elif len(sents) == 2:
        lines = [sents[0]]
        spark = sents[1]
    elif len(sents) == 3:
        lines = sents[:2]
        spark = sents[2]
    elif len(sents) == 4:
        lines = sents[:3]
        spark = sents[3]
    else:
        lines = sents[:4]
        spark = sents[-1]

    # Truncate lines to ~90 chars each for readability
    lines = [textwrap.shorten(l, 90, placeholder="…") for l in lines]
    spark  = textwrap.shorten(spark, 80, placeholder="…")

    return {
        "view": "artifact",
        "artifactTitle": artifact_title,
        "artifactHeading": artifact_heading,
        "artifactLines": lines,
        "sparkLine": spark,
    }

def patch_beat(beat_obj: dict, slug: str) -> bool:
    """Add remotion block to B01, B02, or B08. Return True if changed."""
    bid = beat_obj["beat_id"]
    if bid not in ("B01", "B02", "B08"):
        return False
    if (beat_obj.get("shot", {}).get("source") == "remotion"):
        return False  # already patched

    narration = beat_obj.get("narration_text", "")
    props = make_props(narration, bid, slug)

    beat_obj["shot"] = {
        "type": "GRAPHIC",
        "source": "remotion",
        "motion": "fade",
        "remotion": {
            "pattern": "ClaudeWindow",
            "props": props,
            "rendered": {"out": f"media/{bid}.mp4", "at": ""},
        },
    }
    beat_obj["build"] = {
        "status": "PENDING",
        "src": f"media/{bid}.mp4",
        "filled_by": "remotion",
        "at": datetime.now().isoformat(timespec="seconds"),
    }
    return True

def run(cmd, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    if r.returncode != 0:
        print("  STDERR:", r.stderr[-600:])
    return r

def main():
    dry = "--dry" in sys.argv

    for slug in REELS:
        reel_dir = BASE / "cancer-biology" / "youtube" / f"claude-liam-{slug}"
        bs_path  = reel_dir / "beat_sheet.json"

        if not bs_path.exists():
            print(f"[SKIP] {slug} — no beat_sheet.json")
            continue

        with open(bs_path) as f:
            d = json.load(f)

        changed = False
        for b in d["beats"]:
            if patch_beat(b, slug):
                changed = True
                print(f"[patch] {slug} {b['beat_id']} → ClaudeWindow")

        if not changed:
            print(f"[skip]  {slug} — B01/B02 already remotion")
            continue

        # Remove from slates list
        meta_build = d["metadata"].get("build", {})
        slates = meta_build.get("slates", [])
        slates = [s for s in slates if s not in ("B01", "B02", "B08")]
        meta_build["slates"] = slates
        meta_build["filled"] = 11 - len(slates)
        d["metadata"]["build"] = meta_build

        if dry:
            print(f"  [dry-run] would write beat_sheet.json")
            continue

        with open(bs_path, "w") as f:
            json.dump(d, f, indent=1)

        # Clear old slate placeholder mp4s so slate_resolves() sees them as empty
        for bid in ("B01", "B02", "B08"):
            old = reel_dir / "media" / f"{bid}.mp4"
            if old.exists():
                old.unlink()
                print(f"  [clear] removed old placeholder {bid}.mp4")

        # Render B01, B02, B08 via remotion_scenes.py
        print(f"  [remotion] rendering B01+B02+B08 for {slug}…")
        r = run([sys.executable, str(RUNTIME / "remotion_scenes.py"), str(reel_dir)],
                cwd=ART / "runtime" / "remotion")
        if r.returncode == 0:
            print(f"  [remotion] ok — {slug}")
        else:
            print(f"  [remotion] FAIL — {slug}")
            continue

        # Compile final cut
        print(f"  [compile] {slug}…")
        env_override = {"ART_FACTS": "0"}
        import os
        env = {**os.environ, **env_override}
        r = subprocess.run(
            [sys.executable, str(RUNTIME / "compile.py"), str(reel_dir)],
            capture_output=True, text=True, cwd=BASE, env=env
        )
        last = "\n".join((r.stdout + r.stderr).strip().splitlines()[-6:])
        print(f"  [compile] {last}")

    print("\ndone.")

if __name__ == "__main__":
    main()
