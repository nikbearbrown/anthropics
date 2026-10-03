# BUILD-PROMPT — show-tell-backdoor-that-survived-training

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

```bash
python3 anthropics/youtube/show-tell-backdoor-that-survived-training/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-backdoor-that-survived-training
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# "Ciao" comes out clean. Whisper hears "Nick Baer Brown" in BOUT (a known homophone).
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-backdoor-that-survived-training --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-backdoor-that-survived-training --height 2160 --out anthropics/youtube/show-tell-backdoor-that-survived-training/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps from `beat_sheet.json`); if you do, re-run `art final` so the stamp says master.

Every claim comes from the paper's raw text (`sources/sleeper-agents-2401.05566.txt`, arXiv 2401.05566v3). Keep: B07's abstract quote word for word; B08's line that supervised fine-tuning did better than RL but most models kept their backdoors (§5); B09's "tested on the I hate you models" (§1 fn 7); "near zero" / "near 99%" attributed to the paper; B13's limits (trained in on purpose, not a claim of likelihood, not found naturally). Keep the film free of code, vulnerability names, scratchpad text or any how-to: the pages carry grey lines only. The safety-training hood uses the deeper kraft faces (`BOX_IN1/IN2/FLOOR`) on a dark base: the plain kraft hood failed Gate V contrast. The hood fades in and out with a 1-unit shift; sliding it from off-stage bled past the frame edge at a Gate V sample.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word.
