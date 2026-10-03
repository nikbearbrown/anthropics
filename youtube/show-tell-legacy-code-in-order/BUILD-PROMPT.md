# BUILD-PROMPT — show-tell-legacy-code-in-order

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-legacy-code-in-order/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-legacy-code-in-order
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Bonjour" comes out clean in Kokoro (whisper-check BIDEA anyway). Kokoro says "preflight" as "per flight":
# the narration writes "pre-flight" (on-screen labels and the prompt keep the command name, preflight).
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-legacy-code-in-order --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-legacy-code-in-order --height 2160 --out anthropics/youtube/show-tell-legacy-code-in-order/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-fetch the plugin's files raw from GitHub main (`anthropics/claude-plugins-official/plugins/code-modernization/`) and diff them against `sources/live_2026-09-27_*`. The local copy in this tree is older (no `review`, no `verify`, bare `/modernize-*` names); the film follows the live version. If upstream has moved again, update the order, the names and FACTCHECK.md before re-voicing.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
