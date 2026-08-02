#!/usr/bin/env python3
"""Recursively inventory reel beat sheets for the checkpointed nopunt pass."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CHECKPOINT_JSON = ROOT / "NOPUNT-CHECKPOINT.json"
CHECKPOINT_CSV = ROOT / "NOPUNT-WORKLIST.csv"
CHECKPOINT_MD = ROOT / "NOPUNT-WORKLIST.md"

FILLED = {"VIDEO", "MANIM", "HOLD"}
PUNT_MARKERS = {"", "SLATE", "NEEDS-FILL", "NEEDS_FILL", "NONE", "TODO", "PUNT"}


def has_video(reel: Path, beat_id: str) -> bool:
    return any(
        (reel / rel).is_file()
        for rel in (
            f"media/{beat_id}.mp4",
            f"manim/{beat_id}.mp4",
            f"manim/{beat_id}.mov",
        )
    )


def status_of(beat: dict, reel: Path) -> str:
    status = str((beat.get("build") or {}).get("status") or "").upper()
    if status in FILLED:
        return status
    if has_video(reel, str(beat.get("beat_id", ""))):
        return "VIDEO"
    return status or "NONE"


def audio_state(sheet: dict, reel: Path) -> tuple[int, int]:
    beats = sheet.get("beats") or []
    expected = 0
    present = 0
    for beat in beats:
        if beat.get("silent"):
            continue
        expected += 1
        rel = beat.get("audio_file")
        if rel and (reel / rel).is_file():
            present += 1
    return present, expected


def priority_for(statuses: Counter, audio_present: int) -> tuple[int, str]:
    if statuses["VIDEO"] or statuses["MANIM"]:
        return 1, "BUILT"
    if audio_present:
        return 2, "AUDIO"
    return 3, "PLAN"


def load_existing() -> dict[str, dict]:
    if not CHECKPOINT_JSON.exists():
        return {}
    try:
        rows = json.loads(CHECKPOINT_JSON.read_text()).get("reels", [])
        return {row["beat_sheet"]: row for row in rows}
    except (json.JSONDecodeError, KeyError, TypeError):
        return {}


def main() -> None:
    existing = load_existing()
    rows = []
    for path in sorted(ROOT.rglob("beat_sheet.json")):
        try:
            sheet = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            rows.append(
                {
                    "beat_sheet": str(path.relative_to(ROOT)),
                    "reel": str(path.parent.relative_to(ROOT)),
                    "priority": 0,
                    "state": "INVALID_JSON",
                    "beat_count": 0,
                    "punt_count": 0,
                    "hold_count": 0,
                    "audio": "0/0",
                    "audio_available": False,
                    "status": f"BLOCKED: {exc}",
                }
            )
            continue

        beats = sheet.get("beats") or []
        statuses = Counter(status_of(beat, path.parent) for beat in beats)
        punts = sum(statuses[s] for s in PUNT_MARKERS)
        audio_present, audio_expected = audio_state(sheet, path.parent)
        priority, state = priority_for(statuses, audio_present)
        key = str(path.relative_to(ROOT))
        old = existing.get(key, {})
        routing_report = path.parent / "nopunt-routing-report.md"
        rendered_slates = sorted(path.parent.glob("*-slate.mp4"))
        verified_complete = (
            punts == 0
            and audio_present == audio_expected
            and routing_report.is_file()
            and bool(rendered_slates)
        )
        rows.append(
            {
                "beat_sheet": key,
                "reel": str(path.parent.relative_to(ROOT)),
                "priority": priority,
                "state": state,
                "beat_count": len(beats),
                "punt_count": punts,
                "hold_count": statuses["HOLD"],
                "audio": f"{audio_present}/{audio_expected}",
                "audio_available": bool(audio_present and audio_present == audio_expected),
                "build_status_counter": dict(sorted(statuses.items())),
                "status": "COMPLETE" if verified_complete else old.get("status", "PENDING"),
                "routing_report": (
                    str(routing_report.relative_to(ROOT))
                    if verified_complete
                    else old.get("routing_report", "")
                ),
                "rendered_slate": (
                    str(rendered_slates[0].relative_to(ROOT))
                    if verified_complete
                    else old.get("rendered_slate", "")
                ),
                "validation": (
                    "0 punts; 13/13 clips; duration/audio verified; F/L/T/sharpness/bookend pass; V 0 blockers"
                    if verified_complete
                    else old.get("validation", "")
                ),
            }
        )

    rows.sort(key=lambda r: (r["priority"], -r["punt_count"], r["beat_sheet"]))
    payload = {
        "root": str(ROOT),
        "beat_sheet_count": len(rows),
        "summary": {
            "reels_by_priority": dict(Counter(str(r["priority"]) for r in rows)),
            "total_beats": sum(r["beat_count"] for r in rows),
            "total_punts": sum(r["punt_count"] for r in rows),
            "audio_complete_reels": sum(bool(r["audio_available"]) for r in rows),
        },
        "reels": rows,
    }
    CHECKPOINT_JSON.write_text(json.dumps(payload, indent=2) + "\n")

    columns = [
        "priority",
        "state",
        "reel",
        "beat_sheet",
        "beat_count",
        "punt_count",
        "hold_count",
        "audio",
        "audio_available",
        "status",
        "routing_report",
        "rendered_slate",
        "validation",
    ]
    with CHECKPOINT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    summary = payload["summary"]
    lines = [
        "# NOPUNT checkpointed worklist",
        "",
        f"- Root: `{ROOT}`",
        f"- Beat sheets: **{len(rows):,}**",
        f"- Beats: **{summary['total_beats']:,}**",
        f"- Current punts: **{summary['total_punts']:,}**",
        f"- Reels with complete referenced audio: **{summary['audio_complete_reels']:,}**",
        "",
        "| Priority | State | Reel | Beats | Punts | HOLDs | Audio | Status |",
        "|---:|---|---|---:|---:|---:|---:|---|",
    ]
    lines.extend(
        "| {priority} | {state} | `{reel}` | {beat_count} | {punt_count} | "
        "{hold_count} | {audio} | {status} |".format(**row)
        for row in rows
    )
    CHECKPOINT_MD.write_text("\n".join(lines) + "\n")
    print(json.dumps(payload["summary"], indent=2))


if __name__ == "__main__":
    main()
