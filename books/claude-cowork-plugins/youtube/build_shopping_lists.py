#!/usr/bin/env python3
"""
build_shopping_lists.py — Generate Gate D2 SHOPPING.md for all 14 reels.
Run AFTER audio lock (measured durations available in beat mp3s).
Reads actual beat durations via ffprobe or falls back to estimated_duration_s.
"""
import json, subprocess, shutil
from pathlib import Path

BASE = Path(__file__).parent
FFPROBE = shutil.which("ffprobe") or "ffprobe"

REELS = [
    "claude-liam-what-plugins-are",
    "claude-liam-installing-plugins",
    "claude-liam-productivity",
    "claude-liam-marketing",
    "claude-liam-sales",
    "claude-liam-research",
    "claude-liam-data",
    "claude-liam-enterprise-search",
    "claude-liam-product",
    "claude-liam-support",
    "claude-liam-legal-finance",
    "claude-liam-building-plugins",
    "claude-liam-combining-plugins",
    "claude-liam-troubleshooting",
]


def probe_dur(path: Path) -> float | None:
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True
    )
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def get_beat_dur(reel_dir: Path, bid: str, est: float) -> float:
    mp3 = reel_dir / "mp3" / f"beat-{bid}.mp3"
    if not mp3.exists():
        mp3 = reel_dir / "audio" / f"{bid}.mp3"
    if mp3.exists():
        d = probe_dur(mp3)
        if d:
            return round(d, 2)
    return round(est, 2)


def make_shopping_md(slug: str) -> int:
    reel_dir = BASE / slug
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        return 0

    bs = json.loads(bs_path.read_text())
    meta = bs["metadata"]
    title = meta.get("title", slug)
    beats = bs["beats"]

    # Collect VOX beats needing stills
    vox_beats = [b for b in beats if b.get("lane") == "VOX"]
    if not vox_beats:
        return 0

    lines = [
        f"# SHOPPING LIST — {title}",
        f"Slug: `{slug}`",
        f"Gate D2 — pantry stills, duration-locked, Tier 1 illustrative only",
        "",
        "All stills in this series are **Tier 1 illustrative** — no real people, no real",
        "events, no specific objects requiring rights clearance. Generate via AI (GPT Image 2,",
        "Midjourney, or similar) or source stock. Credit: illustrative only, no sidecar needed.",
        "",
        "Drop the finished still at `pantry/<BID>.png`, then rerun `./art run <slug>`.",
        "The compiler will intake, treat (desaturate 80%, contrast 1.15, film grain, cream stage),",
        "and animate per `shot.motion`.",
        "",
        "## Stills needed",
        "",
    ]

    for b in vox_beats:
        bid = b["beat_id"]
        est = b.get("estimated_duration_s", 6.0)
        dur = get_beat_dur(reel_dir, bid, est)
        pantry_note = b.get("pantry_note", "")
        narr = b.get("narration_text", "").strip()
        motion = (b.get("shot") or {}).get("motion", "kenburns")
        focus = (b.get("shot") or {}).get("focus", [0.5, 0.5])
        spark = b.get("spark_line", "")

        # Check if pantry file already exists
        pantry_file = reel_dir / "pantry" / f"{bid}.png"
        status = "[ ]" if not pantry_file.exists() else "[x]"

        lines.append(f"### {status} {bid} — {spark} ({dur:.1f}s)")
        lines.append(f"**Motion:** {motion}, focus {focus}")
        if pantry_note:
            lines.append(f"**Brief:** {pantry_note}")
        else:
            lines.append(f"**Brief (from narration):** {narr[:200]}")
        lines.append(f"**Min duration:** {dur + 2:.0f}s (request ≥ {dur + 3:.0f}s so conform trims)")
        lines.append(f"**Drop at:** `pantry/{bid}.png`")
        lines.append("")

    n = len(vox_beats)
    lines.append("---")
    lines.append(f"Total: {n} still(s) needed | All Tier 1 (AI-generate or stock)")
    lines.append("")

    (reel_dir / "SHOPPING.md").write_text("\n".join(lines))
    return n


def main():
    print("=== Gate D2 — Shopping Lists ===\n")
    total = 0
    for slug in REELS:
        n = make_shopping_md(slug)
        print(f"  {slug}: {n} still(s) needed")
        total += n
    print(f"\nTotal across batch: {total} pantry stills needed")
    print("Drop stills at pantry/<BID>.png, then run ./art run <slug>")


if __name__ == "__main__":
    main()
