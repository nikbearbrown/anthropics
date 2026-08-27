#!/usr/bin/env python3
"""
verdict_strip.py — DELETE placeholder verdict beats. Do not rewrite them.

A verdict card that says "See the full argument above." is worse than no card: it
occupies the one slot a viewer screenshots and fills it with nothing, and the reel
would have been better without that beat at all.

So this removes the beat — from the sheet, from media/, from mp3/ — and deletes the
reel's stale renders so the next compile cannot ship the old cut.

ON GATE BOOKEND: the four-bookend law assumes BVDT carries a verdict. A placeholder
BVDT is not a bookend, it is a blank slot wearing a bookend's name. Stripping it
enforces the law's intent, but the VALIDATOR must be updated to match: BVDT is legal
either present-with-a-real-verdict or absent — never present-and-placeholder. Update
type_check.py accordingly or every stripped reel will fail the gate.

    python3 verdict_strip.py --root .                       # report
    python3 verdict_strip.py --root . --apply
    python3 verdict_strip.py --root . --apply --only slug-a,slug-b
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

PLACEHOLDER = [
    r"^key finding (one|two|three|\d+)\.?$",
    r"^see the full argument above\.?$",
    r"^test the claim in your own session\.?$",
    r"^the pattern holds at scale\.?$",
    r"^your turn to verify\.?$",
    r"^what the data shows$",
    r"^key findings$",
    r"^see narration\.?$",
    r"^see above\.?$",
    r"^like and subscribe.*$",
    r"^tbd\.?$",
    r"^placeholder",
    r"^[>|\-—•\s]*$",
]
EMPTY_NARRATION = [
    r"^here is what the evidence shows\.?$",
    r"^here are the key findings\.?$",
    r"^the verdict\.?$",
    r"^in summary\.?$",
]


def is_ph(s):
    s = (s or "").strip()
    return any(re.match(p, s, re.I) for p in PLACEHOLDER)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", default=None, help="comma-separated slugs")
    ap.add_argument("--min-real", type=int, default=1,
                    help="a verdict survives if it has at least this many non-placeholder lines")
    ap.add_argument("--thin-only", action="store_true",
                    help="strip ONLY reels whose body is too thin to support a verdict. A reel "
                         "with a real body earned a verdict and should have one AUTHORED, not "
                         "deleted — deleting it throws away the payload beat.")
    ap.add_argument("--thin-beats", type=int, default=5)
    ap.add_argument("--thin-words", type=int, default=180)
    a = ap.parse_args()

    only = set(s.strip() for s in a.only.split(",")) if a.only else None
    sheets = sorted(set(Path(a.root).glob("*/youtube/*/beat_sheet.json"))
                    | set(Path(a.root).glob("youtube/*/beat_sheet.json"))
                    | set(Path(a.root).glob("skills/youtube/*/beat_sheet.json")))
    if not sheets:
        sys.exit(f"no beat_sheet.json under {a.root}")

    stripped, kept, removed_files = [], 0, []

    for sheet in sheets:
        slug = sheet.parent.name
        if only and slug not in only:
            continue
        try:
            j = json.loads(sheet.read_text(encoding="utf-8"))
        except Exception:
            continue

        beats = j.get("beats", [])
        idx = None
        for i, b in enumerate(beats):
            rem = ((b.get("shot") or {}).get("remotion") or {})
            if rem.get("pattern") == "ClaudeVerdictArtifact":
                idx = i
                break
        if idx is None:
            continue

        beat = beats[idx]
        pr = ((beat.get("shot") or {}).get("remotion") or {}).get("props") or {}
        lines = [str(x) for x in (pr.get("artifactLines") or [])]
        real = [L for L in lines if not is_ph(L)]
        nar = (beat.get("narration_text") or "").strip()
        nar_empty = any(re.match(p, nar, re.I) for p in EMPTY_NARRATION)

        if len(real) >= a.min_real and not (is_ph(pr.get("artifactHeading", "")) and not real):
            kept += 1
            continue

        body = [(b.get("narration_text") or "").strip() for b in beats
                if b.get("beat_id") not in ("B00", "BVDT", "BHTF", "BOUT")]
        body = [t for t in body if t]
        words = sum(len(t.split()) for t in body)
        rich = len(body) >= a.thin_beats and words >= a.thin_words
        if a.thin_only and rich:
            kept += 1
            print(f"  SKIP (author, do not strip): {slug[:52]:52s} "
                  f"{len(body):2d} body beats, {words:4d} words")
            continue

        bid = beat.get("beat_id", "BVDT")
        why = []
        if not real:
            why.append(f"all {len(lines)} lines are placeholders")
        if is_ph(pr.get("artifactHeading", "")):
            why.append("placeholder heading")
        if nar_empty:
            why.append("contentless narration")
        stripped.append((slug, sheet, bid, "; ".join(why), lines))

        if not a.apply:
            continue

        bak = sheet.with_suffix(".json.pre-verdict-strip")
        if not bak.exists():
            shutil.copy2(sheet, bak)
        del beats[idx]
        j["beats"] = beats
        meta = j.setdefault("metadata", {})
        meta["verdict_stripped"] = (
            f"{bid} removed: {'; '.join(why)}. A placeholder verdict is worse than none."
        )
        bld = meta.get("build")
        if isinstance(bld, dict) and isinstance(bld.get("of"), int):
            bld["of"] = len(beats)
        sheet.write_text(json.dumps(j, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

        d = sheet.parent
        for p in [d / "media" / f"{bid}.mp4", d / "mp3" / f"beat-{bid}.mp3",
                  d / "manim" / f"{bid}.mp4", d / "clips" / f"{bid}.mp4"]:
            if p.exists():
                p.unlink()
                removed_files.append(str(p.relative_to(a.root)))
        # any render of the old cut is now a lie — the beat it contains no longer exists
        for p in list(d.glob(f"{slug}*.mp4")):
            p.unlink()
            removed_files.append(str(p.relative_to(a.root)))

    print(f"reels scanned          : {len(sheets)}")
    print(f"verdict kept (has real content): {kept}")
    print(f"verdict STRIPPED       : {len(stripped)}")
    for slug, _, bid, why, lines in stripped[:30]:
        print(f"\n  {slug}")
        print(f"    removing {bid} — {why}")
        for L in lines[:4]:
            print(f"      was: {L!r}")
    if len(stripped) > 30:
        print(f"\n  … and {len(stripped)-30} more")

    if a.apply:
        print(f"\ndeleted {len(removed_files)} artifact file(s) — beat media, audio, and every "
              f"stale render of the old cut.")
        print("Recompile the affected reels. Update type_check.py: BVDT must be either")
        print("present-with-a-real-verdict or absent, never present-and-placeholder.")
    else:
        print("\nDRY RUN — nothing deleted. Re-run with --apply (keeps .pre-verdict-strip backups).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
