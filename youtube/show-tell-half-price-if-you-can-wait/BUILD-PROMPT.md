# BUILD-PROMPT — show-tell-half-price-if-you-can-wait

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-half-price-if-you-can-wait/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-half-price-if-you-can-wait
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# "Bonjour" comes out clean in Kokoro (whisper-check BIDEA anyway). small.en whisper hears "errored" as "erred";
# medium.en hears it correctly, so check with medium.en before re-voicing.
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-half-price-if-you-can-wait --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-half-price-if-you-can-wait --height 2160 --out anthropics/youtube/show-tell-half-price-if-you-can-wait/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any version-sensitive fact (time limits, the 50%, retention), re-fetch the raw live page (`curl -sL https://platform.claude.com/docs/en/build-with-claude/batch-processing.md`): the live docs win over `anthropics/claude-cookbooks/misc/batch_processing.ipynb`, whose SDK path and model are already out of date. Name no model and no SDK path; use no per-model prices.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
