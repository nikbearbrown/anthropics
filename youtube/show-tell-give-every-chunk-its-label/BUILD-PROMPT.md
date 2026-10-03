# BUILD-PROMPT — show-tell-give-every-chunk-its-label

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-give-every-chunk-its-label/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-give-every-chunk-its-label
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Hallo" comes out clean in Kokoro (whisper-check BIDEA anyway); "B M twenty-five" is written out so Kokoro says BM25
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-give-every-chunk-its-label --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-give-every-chunk-its-label --height 2160 --out anthropics/youtube/show-tell-give-every-chunk-its-label/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any number, re-read the raw notebook (`anthropics/claude-cookbooks/capabilities/contextual-embeddings/guide.ipynb`): the film uses only its 35% headline (with its exact framing) and the 90% cache-read discount. Its other figures disagree with each other (SOURCES.md).

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
