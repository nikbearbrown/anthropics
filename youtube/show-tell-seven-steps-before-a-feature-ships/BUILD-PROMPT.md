# BUILD-PROMPT — show-tell-seven-steps-before-a-feature-ships

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-seven-steps-before-a-feature-ships/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-seven-steps-before-a-feature-ships
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Ciao" comes out clean in Kokoro (whisper-check BIDEA anyway); "/feature-dev" is written "slash feature dev" in the narration
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-seven-steps-before-a-feature-ships --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-seven-steps-before-a-feature-ships --height 2160 --out anthropics/youtube/show-tell-seven-steps-before-a-feature-ships/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-read the plugin's raw files (`anthropics/claude-plugins-official/plugins/feature-dev/`, especially `commands/feature-dev.md`, which is what runs) and diff them against `sources/live_*`. The reviewer floor is the agent file's "≥ 80", not the README's "75-100" output line (SOURCES.md).

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
