# BLOCKED.md — anthropics/youtube

Reels that cannot be built under the current factory pass. Each entry names the reel,
the date, and the single load-bearing reason. Full detail lives in each reel's
`AUDIT.md`.

---

## medhavy-vox-tumor-pressure · 2026-08-27

**Path**: anthropics/youtube/cancer-nanomedicine/youtube/medhavy-vox-tumor-pressure

**Reason**: Pipeline mismatch + fundamental scaffolding gap. The factory prompt
targets Claude/Liam Brutalist bookend reels (`B00/BVDT/BHTF/BOUT`,
`runtime/scripts/compile.py`, `type_check.py`, etc.). This reel is a **Vox-style
medhavy audience variant** — different skin, different bookends (`OutroSeries` /
`OutroCTA`), different toolchain (`books/vox/scripts/vox_run.sh`). It has:

- **11 of 13 beats are the §6 gen-AI-clip punt costume** (`"YOU → 5–10s gen-AI
  clip → pantry"`) — a card-only reel per §7.
- **No `vox_scenes.py`** in the variant dir — `vox_run.sh` refuses (exit 2) without one.
- **No `FACTCHECK.md` / `SHOTLIST.md` / `PROMPTS.md`** — GATE F refuses without them.
- **No `media/` dir, no cut mp4 ever produced.** Parent `vox-tumor-pressure/` has not
  been compiled either.

Fix requires authoring 11 medhavy-palette Manim scenes, writing the paperwork set, and
running the Vox pipeline — outside a single unattended factory pass under the wrong
SKILL contract. Details: see the reel's `AUDIT.md`.

`beat_sheet.json` was NOT touched.

---

## medhavy-vox-batch-distribution · 2026-08-28

**Path**: anthropics/youtube/cancer-nanomedicine/youtube/medhavy-vox-batch-distribution

**Reason**: Same fingerprint as `medhavy-vox-tumor-pressure` above. Vox-style medhavy
audience variant, wrong pipeline for the factory prompt. 14 beats, 10 of which are
pipeline-owned (B02 FormACard, B04–B08/B10/B11 Manim graphics, B13/B14 OutroSeries/CTA)
and every one currently a slate. `runtime/manim/animated_graphics.py` contains **zero**
of the seven Manim scene classes this reel names (`B04_SmallMolecule`, `B05_NanoCloud`,
`B06_TwoHistograms`, `B07_PDIScale`, `B08_ThreePopulations`, `B10_MatchMeanVsDistribution`,
`B11_ExampleComparison`). `compile.py --review` would refuse via GATE LANE
(`PIPELINE-SLATE-IN-CUT`) — a gate `--allow-slates` cannot bypass. Rebuilding requires
authoring `vox_scenes.py` + paperwork + Remotion renders + Manim scene authoring — a
multi-hour job, not a single unattended pass.

`type_check.py` PASSED (one §8.10 ADVISORY only, non-blocking). `beat_sheet.json` NOT
edited (no `beat_sheet.pre-rebuild.json` created — no rebuild was attempted). No renders
deleted. No validator loosened. Details: reel's `AUDIT.md`.

---

## claude-liam-simple-delve/short · 2026-08-31

**Path**: anthropics/youtube/claude-liam-simple-delve/short

**Reason**: 16:9 Manim layout rendered at 9:16 — every S-beat cropped horizontally.
All 16 Manim scenes (`manim/S01.mp4`…`manim/S16.mp4`) are 1214×2160 but were composed
for a 1920×1080 stage: anchor text is chopped ("delve" → "ve" on S03 and the S13
payoff; two-column layouts on S12 cut both columns; act cards on S07 clip edge to
edge), and captions are narration fragments (Text(narration[:30])) that clip
mid-word ("like fifteen-fold in", "each word posit…", "have nudged it"). This is
Check 5b's exact defect (mid-word truncation of narration-as-caption) compounded by
a landscape-authored composition rendered vertical. The `short/` folder has no
`scenes.py` source to re-render; the metadata's `pantry/<bid>-916.*` remediation slot
is empty. Every other check passed (bookends legal for @NikBearBrown skin, verdict
authored, lens moves earned, no punts, no placeholder your-turn).

Fix requires a `rebuild` pass on the scenes source — reflow every S-scene for 9:16,
replace narration captions with short category labels, or hand-supply 16 `-916`
pantry overrides. Outside one unattended factory pass. `beat_sheet.json` was NOT
edited; `beat_sheet.pre-rebuild.json` was created as a byte-exact backup only. No
compile attempted. Details: reel's `AUDIT.md`.
