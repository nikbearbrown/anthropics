#!/usr/bin/env python3
"""rebuild_fixup.py — Second-pass rebuild for reels fixed during batch2.

These reels were processed by batch1/batch2 with truncated or YAML-artifact
B00/BVDT content, then fixed. They need a clean rebuild.

Run AFTER build_batch2.py completes.
Run from: /Users/bear/Documents/CoWork/bear-textbooks/books/
"""

import json
import subprocess
import sys
import time
from pathlib import Path

BOOKS = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
ROOT = BOOKS / "anthropics"
ART = BOOKS / "brutalist-art/art"
LOG_PATH = BOOKS / "anthropics/youtube/OVERNIGHT-RUN-LOG.md"
WORKLIST_PATH = BOOKS / "anthropics/youtube/OVERNIGHT-WORKLIST.json"

# Reels that need targeted rebuild — read from REBUILD-LIST.txt
def _load_fixup_reels():
    p = BOOKS / "anthropics/youtube/REBUILD-LIST.txt"
    if not p.exists():
        return []
    reels = []
    for line in p.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            reels.append(line)
    return reels

FIXUP_REELS = _load_fixup_reels()


def log(msg):
    print(msg, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(msg + "\n")


def run_art(reel_dir: Path):
    t0 = time.time()
    result = subprocess.run(
        [str(ART), "run", str(reel_dir)],
        capture_output=True,
        text=True,
        cwd=str(BOOKS),
        timeout=600,
    )
    elapsed = int(time.time() - t0)
    return result.returncode, elapsed, result.stdout + result.stderr


def run_gate_t(reel_dir: Path):
    type_check = BOOKS / "brutalist-art/runtime/scripts/type_check.py"
    result = subprocess.run(
        [sys.executable, str(type_check), str(reel_dir), "--skip-pixels"],
        capture_output=True,
        text=True,
        cwd=str(BOOKS),
        timeout=120,
    )
    output = result.stdout + result.stderr
    if "Overall: PASS" in output or "Overall: **PASS**" in output:
        return "PASS"
    elif result.returncode == 0:
        return "PASS"
    return "FAIL"


def load_worklist():
    with open(WORKLIST_PATH) as f:
        return json.load(f)


def save_worklist(data):
    with open(WORKLIST_PATH, "w") as f:
        json.dump(data, f, indent=2)


def main():
    data = load_worklist()

    log(f"\n## FIXUP PASS — {len(FIXUP_REELS)} reels")
    log(f"Started: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")

    for reldir in FIXUP_REELS:
        reel_dir = ROOT / reldir
        slug = reel_dir.name

        if not reel_dir.exists():
            log(f"\n### {slug}\nSKIP — directory not found")
            continue

        # Clear any stale mp4s before rebuild
        for mp4 in reel_dir.glob("*.mp4"):
            mp4.unlink()

        log(f"\n### {slug} [fixup]")

        try:
            rc, elapsed, output = run_art(reel_dir)
        except subprocess.TimeoutExpired:
            log(f"FAIL — timeout after 600s")
            continue
        except Exception as e:
            log(f"FAIL — {e}")
            continue

        # Check output
        slug_mp4 = reel_dir / f"{slug}.mp4"
        slate_mp4 = reel_dir / f"{slug}-slate.mp4"
        mp4_path = slug_mp4 if slug_mp4.exists() else slate_mp4 if slate_mp4.exists() else None

        if not mp4_path or mp4_path.stat().st_size < 500_000:
            log(f"FAIL — no valid mp4 output (rc={rc}, {elapsed}s)")
            continue

        gate_t = run_gate_t(reel_dir)
        size = mp4_path.stat().st_size // 1024
        log(f"OK — {mp4_path.name} ({size}K) | Gate T: {gate_t} | {elapsed}s")

        # Update worklist
        for item in data["items"]:
            if item.get("dir") == reldir and item.get("tier") == 1:
                item["status"] = "done"
                item["note"] = f"fixup {mp4_path.name} Gate-T={gate_t}"
                break
        save_worklist(data)

    log(f"\n## FIXUP PASS COMPLETE")
    log(f"Finished: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")


if __name__ == "__main__":
    main()
