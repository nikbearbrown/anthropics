# BUILD-PROMPT — show-tell-one-lesson-three-tiers

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-one-lesson-three-tiers/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-one-lesson-three-tiers
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (1.0 s silent tail; unpadded copy to _superseded/),
# then write ffprobe durations back to actual_duration_s (and audio_file).
./brutalist.art/art run   anthropics/youtube/show-tell-one-lesson-three-tiers --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-one-lesson-three-tiers --height 2160 --out anthropics/youtube/show-tell-one-lesson-three-tiers/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Before re-stating any claim, re-fetch the live files (`https://raw.githubusercontent.com/anthropics/k12-teacher-skills/main/plugin/skills/k12-lesson-differentiation/SKILL.md`, `references/output.md`, `references/math.md`, `README.md`) and diff them against `sources/live_*`; the live files win over the local copy in `anthropics/k12-teacher-skills/`, which is older.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
