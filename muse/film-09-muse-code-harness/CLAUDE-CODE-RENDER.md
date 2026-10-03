# CLAUDE-CODE-RENDER.md — Film 9: "Muse Code, the Harness"

Render instructions for Claude Code on Bear's Mac. Claude Code renders; it
never publishes.

## 1. Get the files
Pull the repo (or download the folder) and `cd` into it:

```
cd muse/film-09-muse-code-harness
```

## 2. Narration audio (Kokoro, voice `am_onyx`)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written with Kokoro TTS voice `am_onyx` into `audio/<BEAT>.mp3`
(e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, … `audio/BOUT.mp3`).
- 15 beats total; numbers are already written as spoken words — do not
  convert them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Verify: 15 non-empty, playable MP3s, one per beat id.

## 3. Review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-09-muse-code-harness --beats muse/film-09-muse-code-harness/beat_sheet.json --scenes muse/film-09-muse-code-harness/scenes.py --audio muse/film-09-muse-code-harness/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## 4. Final 4K master

```
./art final --reel muse-film-09-muse-code-harness
```

Verify the master: 3840×2160, runtime ≈ 280s (the sum of the audio).

## 5. Publish
Only on Bear's explicit instruction. Never stage, upload, or publish
otherwise.

## Film facts
- Beats: 15 (10 body), total runtime 280s (4m40s).
- Manim scenes: 13 classes, all static-QC clean (0 warnings, 0 errors).
- `py_compile` clean. No MP3/MP4 committed — media lives on this Mac only.
