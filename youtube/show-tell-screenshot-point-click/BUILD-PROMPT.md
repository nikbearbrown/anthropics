# BUILD-PROMPT — show-tell-screenshot-point-click

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-screenshot-point-click/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-screenshot-point-click
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Namaste" comes out clean in Kokoro (whisper-check BIDEA anyway); "read me" and "dot anthropic" are written out in the narration
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-screenshot-point-click --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-screenshot-point-click --height 2160 --out anthropics/youtube/show-tell-screenshot-point-click/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-fetch the raw live docs page (`platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool.md`) and diff it against `sources/live_computer-use-tool-2026-09-27.md`: the GA-vs-beta line in B00 and the pruning advice in B05 are the claims most likely to drift. Keep the crate's seal a single dot: a slanted terracotta band fails GATE T as accent text.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
