#!/usr/bin/env python3
"""build_batch2.py — Build all 117 remaining tier-1 prepped reels.

Resumes from where build_tier1.sh left off. Runs art run on each prepped
reel, runs Gate T, updates OVERNIGHT-WORKLIST.json status, logs to OVERNIGHT-RUN-LOG.md.

Run from: /Users/bear/Documents/CoWork/bear-textbooks/books/
"""

import json
import subprocess
import os
import sys
import time
from pathlib import Path

BOOKS = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
ROOT = BOOKS / "anthropics"
ART = BOOKS / "brutalist-art/art"
LOG_PATH = BOOKS / "anthropics/youtube/OVERNIGHT-RUN-LOG.md"
WORKLIST_PATH = BOOKS / "anthropics/youtube/OVERNIGHT-WORKLIST.json"

STOP_ON_CONSECUTIVE_FAILURES = 3


def load_worklist():
    with open(WORKLIST_PATH) as f:
        return json.load(f)


def save_worklist(data):
    with open(WORKLIST_PATH, "w") as f:
        json.dump(data, f, indent=2)


def log(msg):
    print(msg, flush=True)
    with open(LOG_PATH, "a") as f:
        f.write(msg + "\n")


def run_art(reel_dir: Path):
    """Run art run on reel_dir. Returns (returncode, duration_s, stdout)."""
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
    """Run Gate T (type_check --skip-pixels). Returns 'PASS', 'FAIL', or 'ERROR'."""
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
    else:
        return "FAIL"


def has_compiled_output(reel_dir: Path) -> bool:
    """Check if art run produced a slate or final mp4."""
    slug = reel_dir.name
    slate = reel_dir / f"{slug}-slate.mp4"
    final = reel_dir / f"{slug}.mp4"
    for f in [slate, final]:
        if f.exists() and f.stat().st_size > 500_000:
            return True
    return False


def main():
    data = load_worklist()
    items = data["items"]
    tier1_prepped = [r for r in items if r.get("tier") == 1 and r.get("status") == "prepped"]

    log(f"\n## BATCH 2 START — {len(tier1_prepped)} reels to build")
    log(f"Started: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")

    consecutive_failures = 0
    last_fail_gate = None
    built = 0
    failed = 0
    skipped = 0

    for item in tier1_prepped:
        slug = item["dir"].rsplit("/", 1)[-1]
        reel_dir = ROOT / item["dir"]

        if not reel_dir.exists():
            log(f"\n### {slug}\nSKIP — directory not found: {reel_dir}\n")
            skipped += 1
            continue

        log(f"\n### {slug}")

        # Run art run
        try:
            rc, elapsed, output = run_art(reel_dir)
        except subprocess.TimeoutExpired:
            log(f"FAIL — art run timed out after 600s")
            item["status"] = "failed"
            item["note"] = "art run timeout"
            consecutive_failures += 1
            failed += 1
            last_fail_gate = "art run timeout"
            save_worklist(data)
            if consecutive_failures >= STOP_ON_CONSECUTIVE_FAILURES:
                log(f"\n## STOP — {STOP_ON_CONSECUTIVE_FAILURES} consecutive failures (gate: {last_fail_gate})")
                log("See OVERNIGHT-BLOCKED.md")
                break
            continue
        except Exception as e:
            log(f"FAIL — art run exception: {e}")
            item["status"] = "failed"
            item["note"] = str(e)[:80]
            consecutive_failures += 1
            failed += 1
            last_fail_gate = "art run exception"
            save_worklist(data)
            if consecutive_failures >= STOP_ON_CONSECUTIVE_FAILURES:
                log(f"\n## STOP — {STOP_ON_CONSECUTIVE_FAILURES} consecutive failures")
                break
            continue

        # Check if output was produced
        if not has_compiled_output(reel_dir):
            log(f"FAIL — no compiled mp4 after art run (rc={rc}, {elapsed}s)")
            # Log snippet of output for diagnosis
            output_tail = output[-500:] if len(output) > 500 else output
            log(f"Output tail:\n{output_tail}")
            item["status"] = "failed"
            item["note"] = f"no mp4 output rc={rc}"
            consecutive_failures += 1
            failed += 1
            last_fail_gate = "no mp4"
            save_worklist(data)
            if consecutive_failures >= STOP_ON_CONSECUTIVE_FAILURES:
                log(f"\n## STOP — {STOP_ON_CONSECUTIVE_FAILURES} consecutive failures (gate: no mp4)")
                break
            continue

        # Reset consecutive failure counter on successful build
        consecutive_failures = 0

        # Gate T
        gate_t = run_gate_t(reel_dir)

        # Determine final mp4 name
        slate = reel_dir / f"{slug}-slate.mp4"
        final = reel_dir / f"{slug}.mp4"
        mp4_name = final.name if final.exists() else slate.name if slate.exists() else "unknown"
        mp4_size = 0
        mp4_path = final if final.exists() else slate
        if mp4_path.exists():
            mp4_size = mp4_path.stat().st_size // 1024

        log(f"OK — {mp4_name} ({mp4_size}K) | Gate T: {gate_t} | {elapsed}s")

        item["status"] = "done"
        item["note"] = f"built {mp4_name} Gate-T={gate_t}"
        item["attempts"] = item.get("attempts", 0) + 1
        built += 1
        save_worklist(data)

    log(f"\n## BATCH 2 COMPLETE")
    log(f"Built: {built} | Failed: {failed} | Skipped: {skipped}")
    log(f"Finished: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")


if __name__ == "__main__":
    main()
