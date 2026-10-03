# BUILD-PROMPT — show-tell-four-reviewers-and-a-sieve

**What this is.** How to rebuild this film ("Five Reviewers and a Sieve", card #31) from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-four-reviewers-and-a-sieve/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-four-reviewers-and-a-sieve
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards.
# "Hallo" comes out clean (whisper-check BIDEA anyway). B11 says "hands every scoring agent" (a first take,
# "gives every scorer", was heard "every score of"). "Claude dot M D" is heard "claw.md" by small.en (a homophone, left).
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-four-reviewers-and-a-sieve --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-four-reviewers-and-a-sieve --height 2160 --out anthropics/youtube/show-tell-four-reviewers-and-a-sieve/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Before re-stating any claim, re-read `anthropics/claude-plugins-official/plugins/code-review/commands/code-review.md` and `README.md` raw and `diff` them against `sources/live_*`. Keep the film's limits: follow the command file (five reviewers, "Filter out any issues with a score less than 80"), say the README's four only as the README's number, never say scores are averaged, and keep the slip scores as illustrations.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
