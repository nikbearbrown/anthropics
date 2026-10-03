# BUILD-PROMPT — show-tell-inspector-says-no-first

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-inspector-says-no-first/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-inspector-says-no-first
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-inspector-says-no-first --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-inspector-says-no-first --height 2160 --out anthropics/youtube/show-tell-inspector-says-no-first/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio).

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
