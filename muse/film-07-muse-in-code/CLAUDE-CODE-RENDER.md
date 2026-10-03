# CLAUDE-CODE-RENDER.md — Muse in Code (Film 7 of 12)

Render instructions for Bear's Mac. Persona: Liam, in for Bear
(@NikBearBrown). Voice: Kokoro `am_onyx`. Register: Teardown.

## 1. Title + purpose
"Muse in Code" — the viewer calls Muse from their own code three ways
(raw REST, OpenAI SDK, Anthropic SDK) and learns to debug via error
messages. Reel slug: `muse-film-07-muse-in-code`.

## 2. Get the files
Pull the repo (or download the film folder) and `cd` into it:

```
cd muse/film-07-muse-in-code
```

You need `beat_sheet.json` (13 beats) and `scenes.py` (11 scene classes,
M01–M11).

## 3. Narration
Kokoro TTS, voice `am_onyx`. For EVERY beat in `beat_sheet.json`,
synthesize the beat's `line` field EXACTLY as written and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`).
- Numbers are already written as spoken words — do not convert them back
  to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- Verify: 13 MP3s, one per beat id, each non-empty and playable.

## 4. Review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-07-muse-in-code --beats muse/film-07-muse-in-code/beat_sheet.json --scenes muse/film-07-muse-in-code/scenes.py --audio muse/film-07-muse-in-code/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## 5. Final 4K master

```
./art final --reel muse-film-07-muse-in-code
```

Verify the master: 3840×2160, runtime ≈ 282 s (the sum of the audio),
silent tail present at the end.

## 6. Publish
Only on Bear's explicit instruction. Never publish, upload, or stage
anything for publishing otherwise.

## 7. Film facts
- Beats: 13 (8 body), runtime 282 s (~4m42s).
- Scenes: 11 Manim classes, QC 11 clean · 0 warnings · 0 errors.
- No MP3/MP4/WAV committed. Audio and renders stay on this Mac.
