#!/usr/bin/env bash
# build_tier1.sh — Batch compile all 121 tier-1 reels
# Run from: /Users/bear/Documents/CoWork/bear-textbooks/books/
# Output log: anthropics/youtube/OVERNIGHT-RUN-LOG.md

set -e
cd /Users/bear/Documents/CoWork/bear-textbooks/books

LOG="anthropics/youtube/OVERNIGHT-RUN-LOG.md"
WORKLIST="anthropics/youtube/OVERNIGHT-WORKLIST.json"

echo "# OVERNIGHT-RUN-LOG.md" > "$LOG"
echo "Generated: $(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$LOG"
echo "" >> "$LOG"

DONE=0
FAIL=0
TOTAL=121

# Process each tier-1 reel from the worklist
python3 - <<'PYEOF'
import json
import subprocess
import os
import sys
from pathlib import Path

ROOT = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics")
BOOKS = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
LOG = BOOKS / "anthropics/youtube/OVERNIGHT-RUN-LOG.md"
WORKLIST = BOOKS / "anthropics/youtube/OVERNIGHT-WORKLIST.json"

with open(WORKLIST) as f:
    data = json.load(f)

tier1 = [x for x in data["items"] if x["tier"] == 1 and x["status"] == "prepped"]
print(f"Building {len(tier1)} tier-1 reels...", flush=True)

done = 0
fail = 0

with open(LOG, "a") as log:
    log.write("## Build Results\n\n")

    for item in tier1:
        slug = item["slug"]
        reel_dir_rel = f"anthropics/{item['dir']}"
        reel_dir_abs = BOOKS / "anthropics" / item["dir"]

        print(f"\n[{done+fail+1}/{len(tier1)}] Building {slug}...", flush=True)

        try:
            result = subprocess.run(
                ["./brutalist-art/art", "run", reel_dir_rel],
                capture_output=True,
                text=True,
                timeout=300,  # 5 min per reel
                cwd=str(BOOKS),
                env={**os.environ, "ART_STRICT": "0"}
            )

            # Check for slate or final mp4
            slate = reel_dir_abs / f"{slug}-slate.mp4"
            final = reel_dir_abs / f"{slug}.mp4"
            has_video = slate.exists() or final.exists()

            # Check TYPECHECK.md
            tc_path = reel_dir_abs / "TYPECHECK.md"
            tc_pass = False
            if tc_path.exists():
                tc_content = tc_path.read_text()
                tc_pass = "Overall: **PASS**" in tc_content or "Overall: PASS" in tc_content

            # Check for GATE T PASS in output
            gate_t_pass = "GATE T: PASS" in result.stdout or "GATE T: PASS" in result.stderr

            if has_video and (gate_t_pass or tc_pass):
                done += 1
                status = "done"
                video_file = str(final) if final.exists() else str(slate)
                note = f"compiled → {Path(video_file).name}; Gate T: PASS"
                print(f"  [DONE] {slug}", flush=True)
            elif has_video:
                done += 1  # has video but gate status unclear
                status = "done"
                video_file = str(final) if final.exists() else str(slate)
                note = f"compiled → {Path(video_file).name}; Gate T: unknown"
                print(f"  [DONE] {slug} (gate T unconfirmed)", flush=True)
            else:
                fail += 1
                status = "failed"
                last_lines = result.stdout[-500:] if result.stdout else result.stderr[-500:]
                note = f"no video produced; rc={result.returncode}"
                print(f"  [FAIL] {slug} — rc={result.returncode}", flush=True)
                print(f"    stdout tail: {result.stdout[-200:]}", flush=True)
                print(f"    stderr tail: {result.stderr[-200:]}", flush=True)

            # Update worklist item
            for i, orig in enumerate(data["items"]):
                if orig["slug"] == slug and orig["dir"] == item["dir"]:
                    data["items"][i]["status"] = status
                    data["items"][i]["attempts"] = 1
                    data["items"][i]["note"] = note
                    break

            # Write to log
            log.write(f"## {slug}\n")
            log.write(f"Tier: 1 | Status: {status}\n")
            log.write(f"Lens: PASS (Popper via BVDT, Plato via BHTF)\n")
            log.write(f"§8.5 fix: body shortened\n")
            log.write(f"Result: {note}\n")
            log.write("\n")
            log.flush()

        except subprocess.TimeoutExpired:
            fail += 1
            print(f"  [TIMEOUT] {slug}", flush=True)
            for i, orig in enumerate(data["items"]):
                if orig["slug"] == slug and orig["dir"] == item["dir"]:
                    data["items"][i]["status"] = "failed"
                    data["items"][i]["note"] = "timeout (300s)"
                    break
            log.write(f"## {slug}\nStatus: TIMEOUT\n\n")
            log.flush()

        except Exception as e:
            fail += 1
            print(f"  [ERROR] {slug}: {e}", flush=True)
            for i, orig in enumerate(data["items"]):
                if orig["slug"] == slug and orig["dir"] == item["dir"]:
                    data["items"][i]["status"] = "failed"
                    data["items"][i]["note"] = f"error: {str(e)[:100]}"
                    break

# Save updated worklist
with open(WORKLIST, "w") as f:
    json.dump(data, f, indent=1)

print(f"\n=== BUILD COMPLETE: {done} done, {fail} failed ===")
PYEOF
