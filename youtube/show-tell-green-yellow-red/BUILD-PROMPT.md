# BUILD-PROMPT — show-tell-green-yellow-red

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-green-yellow-red/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-green-yellow-red
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Ciao" comes out clean in Kokoro (whisper-check BIDEA anyway). B02 reads the list as "the law, the market, and each
# team's risk tolerance all vary" (the first take merged it into "the law of the market"). "Claude dot M D" is heard as
# "clawed .md" (a homophone, left).
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-green-yellow-red --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-green-yellow-red --height 2160 --out anthropics/youtube/show-tell-green-yellow-red/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-read `anthropics/claude-for-legal/commercial-legal/skills/nda-review/SKILL.md`, `…/cold-start-interview/SKILL.md`, `commercial-legal/README.md` and `README.md` raw and `diff` them against `sources/live_*`. Keep the film's limits: the output is a draft for attorney review, not legal advice (the repo's words); no company names; generic example clauses only; no number the files don't state; tiers labelled in ink, never tinted green or red, never terracotta text.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
