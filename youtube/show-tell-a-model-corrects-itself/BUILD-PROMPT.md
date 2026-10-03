# BUILD-PROMPT — show-tell-a-model-corrects-itself

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-a-model-corrects-itself/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-a-model-corrects-itself
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# "Hallo" comes out clean. "In Claude, paste this" was heard as "paced", so BHTF says "Paste this into Claude";
# "that score is the reward" was heard as "that scores the reward", so B10 says "that score is used as the reward".
# The DRAFT / CRITIQUE / REVISION labels are spoken in lower case (Kokoro spells out capitals).
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-a-model-corrects-itself --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-a-model-corrects-itself --height 2160 --out anthropics/youtube/show-tell-a-model-corrects-itself/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first (a stale Manim cache pushes re-renders past their audio). Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Every claim comes from the paper PDF (`anthropics/claude-cookbooks/misc/data/Constitutional AI.pdf`, text in `sources/`) and the two prompt files in `anthropics/ConstitutionalHarmlessnessPaper/prompts/`. Keep the three quotes verbatim (B02 `harmful0`, B03/B04 the §3.1 wifi example, B08 the §4.1 principle), keep "a model is fine-tuned" (the paper names different models in the abstract and §3), keep the human helpfulness labels in B09, and keep B12's line that this is the 2022 method, not a claim about how any model is trained today. The feedback model's faces are darker than the kit's DARK_* on purpose (GATE T ink tolerance), and the RL arc in B10 is grey, not ink (a long ink arc reads as one frame-wide text run).

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
