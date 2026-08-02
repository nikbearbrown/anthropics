#!/usr/bin/env python3
"""build_batch.py — unattended batch build for anthropics/youtube/ reels.

Builds every reel that lacks a master mp4 (>0.5MB).
Pipeline per reel (all FREE, local — no spend):
  1. Generate Kokoro audio (--no-gate, voice=am_onyx)
  2. Render Remotion beats (shot.remotion.pattern → media/<BID>.mp4)
  3. Render pending Manim beats (if scenes_std.py / scenes.py exists)
  4. Compile → clean master at 4K (compile.py --height 2160 --allow-slates)
  5. Run type_check.py → TYPECHECK.md  (FAIL → mark NEEDS-REVIEW, continue)
  6. Write FACTCHECK.md (basic provenance check)

Three nevers: never spend (Kokoro only), never publish, never stall on a gate.
Logs to BATCH-BUILD-LOG.md in this directory.

Usage:
  python3 build_batch.py [--dry-run] [--category behind-the-model] [--limit 20]
"""
import argparse, glob, json, os, re, subprocess, sys, time
from datetime import datetime
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
HERE = Path(__file__).resolve().parent          # anthropics/youtube/
BOOKS = HERE.parent.parent                       # books/
ART_HOME = BOOKS / "brutalist-art"
SCRIPTS = ART_HOME / "runtime" / "scripts"
REMOTION_PROJECT = ART_HOME / "runtime" / "remotion"

CATEGORIES = [
    'behind-the-model', 'claude-agent-skills', 'claude-basics', 'claude-code',
    'claude-cowork', 'claude-for-education', 'claude-mcp-connectors', 'claude-news',
    'claude-plugins', 'claude-prompting', 'claude-research', 'claude-skills', 'claude-youtube',
]

SKIP_NAMES = {
    '_batch_qc', '_to_delete', '_ai_explainer_scaffold_manifest.md',
    '_copied_reels_manifest.md', '_COPY-REPORT.md', 'BATCH-STATUS.md',
    'LENS-NOTES.md', 'OVERNIGHT-SLATE-BUILD.md', 'video-ideas.md',
    'video-ideas.md.bak-2026-07-24', 'README.md',
}

LOG_PATH = HERE / "BATCH-BUILD-LOG.md"


# ── Helpers ───────────────────────────────────────────────────────────────────
def log(msg: str, also_print=True):
    if also_print:
        print(msg)
    with open(LOG_PATH, "a") as f:
        f.write(msg + "\n")


def run_cmd(cmd, cwd=None, timeout=600, env=None) -> tuple[int, str, str]:
    """Run a command, return (rc, stdout, stderr)."""
    e = os.environ.copy()
    if env:
        e.update(env)
    try:
        r = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True,
            timeout=timeout, env=e
        )
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "TIMEOUT"
    except Exception as ex:
        return 1, "", str(ex)


def has_master(reel: Path) -> bool:
    """True if a real master mp4 (>0.5MB) exists for this reel."""
    slug = reel.name
    for pat in [
        reel / "mp4" / f"{slug}-cut.mp4",
        reel / f"{slug}-cut.mp4",
        reel / "mp4" / f"{slug}.mp4",
        reel / f"{slug}.mp4",
    ]:
        # Follow symlinks to real file
        real = pat.resolve() if pat.exists() else pat
        if real.exists() and real.stat().st_size > 500_000:
            return True
    return False


def has_audio(reel: Path) -> bool:
    return bool(list(reel.glob("mp3/beat-*.mp3")))


def get_beats(reel: Path) -> list:
    bs = reel / "beat_sheet.json"
    if not bs.exists():
        return []
    try:
        return json.loads(bs.read_text()).get("beats", [])
    except Exception:
        return []


def has_manim_pending(reel: Path) -> bool:
    beats = get_beats(reel)
    for b in beats:
        bid = b.get("beat_id", "")
        manim = b.get("shot", {}).get("manim") or b.get("manim", {})
        if manim and not (reel / "media" / f"{bid}.mp4").exists():
            if not (reel / "manim" / f"{bid}.mp4").exists():
                return True
    return False


def has_remotion_pending(reel: Path) -> bool:
    beats = get_beats(reel)
    for b in beats:
        bid = b.get("beat_id", "")
        pattern = (b.get("shot", {}).get("remotion") or {}).get("pattern")
        if pattern and not (reel / "media" / f"{bid}.mp4").exists():
            return True
    return False


def build_complexity(reel: Path) -> int:
    """0=trivial(just compile), 1=needs remotion, 2=needs audio+remotion, 3=full"""
    audio_ok = has_audio(reel)
    remotion_ok = not has_remotion_pending(reel)
    if audio_ok and remotion_ok:
        return 0
    if audio_ok:
        return 1
    if remotion_ok:
        return 2
    return 3


def discover_reels(only_category=None) -> list[Path]:
    reels = []
    cats = [only_category] if only_category else CATEGORIES
    for cat in cats:
        cat_path = HERE / cat
        if not cat_path.is_dir():
            continue
        for slug_path in sorted(cat_path.iterdir()):
            if slug_path.name in SKIP_NAMES or slug_path.name.startswith('_'):
                continue
            if not slug_path.is_dir():
                continue
            if not (slug_path / "beat_sheet.json").exists():
                continue
            if has_master(slug_path):
                continue
            reels.append(slug_path)
    # Sort by complexity: cheapest first
    reels.sort(key=lambda r: (build_complexity(r), r.name))
    return reels


# ── Step 1: Generate Kokoro audio ─────────────────────────────────────────────
def step_audio(reel: Path, dry_run: bool) -> bool:
    if has_audio(reel):
        log(f"  [audio] already exists — skip")
        return True
    beats = get_beats(reel)
    has_narration = any(b.get("narration_text", "").strip() for b in beats)
    if not has_narration:
        log(f"  [audio] no narration text — skip")
        return True
    if dry_run:
        log(f"  [audio] DRY-RUN: would run generate_audio_kokoro.py")
        return True

    cmd = [sys.executable, str(SCRIPTS / "generate_audio_kokoro.py"),
           str(reel), "--no-gate"]
    log(f"  [audio] generating Kokoro audio (am_onyx, free)…")
    rc, out, err = run_cmd(cmd, cwd=ART_HOME, timeout=600,
                           env={"ART_HOME": str(ART_HOME)})
    if rc != 0:
        log(f"  [audio] FAIL (rc={rc}): {err[-400:]}")
        return False
    log(f"  [audio] OK")
    return True


# ── Step 2: Render Remotion beats ─────────────────────────────────────────────
def step_remotion(reel: Path, dry_run: bool) -> bool:
    beats = get_beats(reel)
    candidates = [b for b in beats
                  if (b.get("shot", {}).get("remotion") or {}).get("pattern")
                  and not (reel / "media" / f"{b['beat_id']}.mp4").exists()]
    if not candidates:
        log(f"  [remotion] no pending Remotion beats — skip")
        return True
    log(f"  [remotion] {len(candidates)} pending: {[b['beat_id'] for b in candidates]}")
    if dry_run:
        log(f"  [remotion] DRY-RUN: would run remotion_scenes.py")
        return True

    cmd = [sys.executable, str(SCRIPTS / "remotion_scenes.py"), str(reel)]
    rc, out, err = run_cmd(cmd, cwd=ART_HOME, timeout=900,
                           env={"ART_HOME": str(ART_HOME)})
    if rc != 0:
        log(f"  [remotion] FAIL (rc={rc}): {err[-400:]}")
        return False
    log(f"  [remotion] OK")
    return True


# ── Step 3: Render Manim beats ────────────────────────────────────────────────
def step_manim(reel: Path, dry_run: bool) -> bool:
    beats = get_beats(reel)
    # Find beats that need Manim and which scene file to use
    scenes_file = None
    for candidate in ["scenes.py", "scenes_std.py", "scenes_std.py"]:
        if (reel / candidate).exists():
            scenes_file = reel / candidate
            break
    if not scenes_file:
        log(f"  [manim] no scenes.py — skip Manim (beats will be slates)")
        return True

    pending = []
    for b in beats:
        bid = b.get("beat_id", "")
        # Check if beat has manim field
        manim_info = b.get("shot", {}).get("manim") or b.get("manim")
        if not manim_info:
            continue
        # Skip if already rendered
        if (reel / "media" / f"{bid}.mp4").exists():
            continue
        if (reel / "manim" / f"{bid}.mp4").exists():
            continue
        scene_class = manim_info.get("scene_class") if isinstance(manim_info, dict) else None
        if scene_class:
            pending.append((bid, scene_class))

    if not pending:
        log(f"  [manim] all Manim beats filled — skip")
        return True

    log(f"  [manim] {len(pending)} pending Manim beats: {[bid for bid, _ in pending]}")
    if dry_run:
        log(f"  [manim] DRY-RUN: would run manim for {[sc for _, sc in pending]}")
        return True

    (reel / "manim").mkdir(exist_ok=True)
    (reel / "media").mkdir(exist_ok=True)

    for bid, scene_class in pending:
        log(f"  [manim] rendering {scene_class}…")
        # Check aspect ratio
        bs_data = {}
        try:
            bs_data = json.loads((reel / "beat_sheet.json").read_text())
        except Exception:
            pass
        is_portrait = bs_data.get("metadata", {}).get("aspect_ratio", "") == "9:16"
        resolution = "2160,3840" if is_portrait else "3840,2160"

        cmd = ["manim", "-qk", "--fps", "24", "-r", resolution,
               str(scenes_file.name), scene_class]
        rc, out, err = run_cmd(cmd, cwd=str(reel), timeout=300)
        if rc != 0:
            log(f"  [manim] FAIL {scene_class}: {err[-300:]}")
            continue

        # Find the output
        found = False
        for search_root in [reel / "media", reel / "manim", reel]:
            for mp4 in search_root.rglob("*.mp4"):
                if scene_class in str(mp4):
                    dest = reel / "manim" / f"{bid}.mp4"
                    import shutil
                    shutil.copy2(str(mp4), str(dest))
                    log(f"  [manim] slotted {scene_class} → manim/{bid}.mp4")
                    found = True
                    break
            if found:
                break
        if not found:
            # Check the standard manim output path
            for mp4 in (reel / "media" / "videos").rglob("*.mp4"):
                if scene_class in str(mp4):
                    dest = reel / "manim" / f"{bid}.mp4"
                    import shutil
                    shutil.copy2(str(mp4), str(dest))
                    log(f"  [manim] slotted from videos/ → manim/{bid}.mp4")
                    found = True
                    break

    return True


# ── Step 4: Compile ────────────────────────────────────────────────────────────
def step_compile(reel: Path, dry_run: bool) -> tuple[bool, str]:
    """Returns (success, output_path_or_error)."""
    if dry_run:
        log(f"  [compile] DRY-RUN: would run compile.py --height 2160")
        return True, "dry-run"

    cmd = [sys.executable, str(SCRIPTS / "compile.py"),
           str(reel), "--height", "2160"]
    log(f"  [compile] compiling clean master…")
    rc, out, err = run_cmd(cmd, cwd=ART_HOME, timeout=600,
                           env={"ART_HOME": str(ART_HOME)})
    def find_master(r: Path) -> Path | None:
        slug = r.name
        for cand in [r / f"{slug}-cut.mp4", r / f"{slug}.mp4",
                     r / "mp4" / f"{slug}-cut.mp4", r / "mp4" / f"{slug}.mp4"]:
            real = cand.resolve() if cand.exists() else cand
            if real.exists() and real.stat().st_size > 500_000:
                return cand
        return None

    if rc == 0:
        mp4 = find_master(reel)
        if mp4:
            log(f"  [compile] OK → {mp4.relative_to(reel)}")
            return True, str(mp4)
        log(f"  [compile] compile rc=0 but no master mp4 found — trying --allow-slates")

    # Try with --allow-slates
    log(f"  [compile] retrying with --allow-slates (rc={rc})")
    cmd2 = [sys.executable, str(SCRIPTS / "compile.py"),
            str(reel), "--height", "2160", "--allow-slates"]
    rc2, out2, err2 = run_cmd(cmd2, cwd=ART_HOME, timeout=600,
                              env={"ART_HOME": str(ART_HOME)})
    if rc2 == 0:
        mp4 = find_master(reel)
        if mp4:
            log(f"  [compile] OK (with slates) → {mp4.relative_to(reel)} — NEEDS-REVIEW")
            return True, str(mp4) + " [SLATES]"
        log(f"  [compile] FAIL: no master mp4 produced even with --allow-slates")
        return False, f"compile failed: no mp4 produced"

    return False, f"compile failed (rc={rc2}): {err2[-300:]}"


# ── Step 5: Type check ────────────────────────────────────────────────────────
def step_typecheck(reel: Path, dry_run: bool) -> bool:
    tc_script = SCRIPTS / "type_check.py"
    if not tc_script.exists():
        log(f"  [typecheck] type_check.py not found — skip")
        return True
    if dry_run:
        log(f"  [typecheck] DRY-RUN")
        return True
    cmd = [sys.executable, str(tc_script), str(reel)]
    rc, out, err = run_cmd(cmd, cwd=ART_HOME, timeout=120,
                           env={"ART_HOME": str(ART_HOME)})
    if rc == 0:
        log(f"  [typecheck] GATE T PASS")
        return True
    elif rc == 3:
        log(f"  [typecheck] GATE T skipped (missing deps)")
        return True
    else:
        log(f"  [typecheck] GATE T FAIL — marked NEEDS-REVIEW, continuing")
        return False  # non-fatal for unattended run


# ── Step 6: Write FACTCHECK.md ────────────────────────────────────────────────
def step_factcheck(reel: Path, dry_run: bool):
    fc_path = reel / "FACTCHECK.md"
    if fc_path.exists():
        log(f"  [factcheck] exists — skip")
        return
    if dry_run:
        log(f"  [factcheck] DRY-RUN")
        return
    beats = get_beats(reel)
    slug = reel.name
    lines = [f"# FACTCHECK — {slug}\n",
             f"\nGenerated: {datetime.now().isoformat()[:16]} (unattended batch)\n\n",
             "## Status\n",
             "PROVISIONAL — generated by build_batch.py. Human review required before publishing.\n\n",
             "## Beat narration inventory\n"]
    for b in beats:
        bid = b.get("beat_id", "?")
        narr = b.get("narration_text", "").strip()
        if narr:
            lines.append(f"\n**{bid}** — {narr[:200]}{'…' if len(narr) > 200 else ''}\n")
    lines.append("\n## VERDICT: PROVISIONAL\n")
    fc_path.write_text("".join(lines))
    log(f"  [factcheck] written (provisional)")


# ── Main loop ─────────────────────────────────────────────────────────────────
def build_reel(reel: Path, dry_run: bool) -> str:
    slug = reel.name
    cat = reel.parent.name
    log(f"\n### {cat}/{slug}")
    log(f"  complexity: {build_complexity(reel)} | audio={'YES' if has_audio(reel) else 'NO'}")

    # Step 1: Audio
    audio_ok = step_audio(reel, dry_run)
    if not audio_ok:
        (reel / "NEEDS-REVIEW.md").write_text(
            f"# NEEDS-REVIEW\nAudio generation failed. Re-run: "
            f"python3 runtime/scripts/generate_audio_kokoro.py {reel} --no-gate\n"
        )
        return "AUDIO-FAIL"

    # Step 2: Remotion
    remotion_ok = step_remotion(reel, dry_run)
    if not remotion_ok:
        log(f"  [remotion] soft-fail — will compile with slates")

    # Step 3: Manim (best-effort)
    step_manim(reel, dry_run)

    # Step 4: Compile
    compile_ok, result = step_compile(reel, dry_run)
    if not compile_ok:
        (reel / "NEEDS-REVIEW.md").write_text(
            f"# NEEDS-REVIEW\nCompile failed: {result}\n"
        )
        return "COMPILE-FAIL"

    # Step 5: Type check
    tc_ok = step_typecheck(reel, dry_run)
    if not tc_ok:
        (reel / "NEEDS-REVIEW.md").write_text(
            f"# NEEDS-REVIEW\nGATE T failed. See TYPECHECK.md.\n"
        )

    # Step 6: FACTCHECK.md
    step_factcheck(reel, dry_run)

    if "[SLATES]" in result:
        return "DONE-WITH-SLATES"
    if not tc_ok:
        return "DONE-NEEDS-TYPEFIX"
    return "DONE"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--category", default=None, help="only this category")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--skip-done-check", action="store_true")
    a = ap.parse_args()

    log(f"\n# Batch Build — {datetime.now().isoformat()[:16]}")
    log(f"DRY-RUN: {a.dry_run} | CATEGORY: {a.category or 'ALL'} | LIMIT: {a.limit}")
    log(f"ART_HOME: {ART_HOME}\n")

    reels = discover_reels(only_category=a.category)
    if a.limit:
        reels = reels[:a.limit]

    log(f"Reels to build: {len(reels)}\n")
    log("---\n")

    stats = {"DONE": 0, "DONE-WITH-SLATES": 0, "DONE-NEEDS-TYPEFIX": 0,
             "AUDIO-FAIL": 0, "COMPILE-FAIL": 0, "OTHER-FAIL": 0}

    for i, reel in enumerate(reels):
        t0 = time.time()
        log(f"\n## [{i+1}/{len(reels)}] {reel.parent.name}/{reel.name}")
        try:
            status = build_reel(reel, dry_run=a.dry_run)
        except Exception as ex:
            log(f"  EXCEPTION: {ex}")
            status = "OTHER-FAIL"
        elapsed = time.time() - t0
        stats[status] = stats.get(status, 0) + 1
        log(f"  → {status} in {elapsed:.1f}s")

    log(f"\n\n# Summary — {datetime.now().isoformat()[:16]}")
    for k, v in stats.items():
        log(f"  {k}: {v}")
    log(f"  TOTAL: {sum(stats.values())}")


if __name__ == "__main__":
    main()
