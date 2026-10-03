# BUILD-PROMPT — show-tell-what-a-compiler-does

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-what-a-compiler-does/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-what-a-compiler-does
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Salaam" comes out clean in Kokoro (whisper-check BIDEA anyway). Chip names are written for the voice:
# "x eighty-six sixty-four", "i six eighty-six", "A. Arch sixty-four" (plain "A arch" loses the A), "risk five sixty-four".
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-what-a-compiler-does --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-what-a-compiler-does --height 2160 --out anthropics/youtube/show-tell-what-a-compiler-does/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-read `anthropics/claudes-c-compiler/DESIGN_DOC.md` and `README.md` raw and diff them against `sources/live_*`. Quote the README's caveat word for word; credit no person.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
