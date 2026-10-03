# BUILD-PROMPT — show-tell-two-mirror-prompts

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-two-mirror-prompts/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-two-mirror-prompts
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Hola" comes out clean in Kokoro (whisper-check BIDEA anyway). "the grader rates hedging" was heard as "the greater
# rate's hedging", so B08 says "Each answer gets a hedging score"; GPT-5 is written "G P T five".
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-two-mirror-prompts --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-two-mirror-prompts --height 2160 --out anthropics/youtube/show-tell-two-mirror-prompts/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-read `anthropics/political-neutrality-eval/README.md`, `eval_set.csv`, `topics.txt` and `prompts.py` raw and `cmp` them against `sources/live_*`. This is sensitive ground: describe the method only, take no position, use only non-partisan example pairs quoted word for word, and state no model result.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
