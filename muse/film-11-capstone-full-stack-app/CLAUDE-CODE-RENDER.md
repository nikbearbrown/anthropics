# CLAUDE-CODE-RENDER.md — Capstone: Ship a Full-Stack App (Film 11)

## Purpose
Finish Film 11: render narration audio and video from this folder's
`beat_sheet.json` and `scenes.py`. Do not publish anything.

## 1. Get the files
Clone or pull `nikbearbrown/anthropics`, then:

```
cd muse/film-11-capstone-full-stack-app/
```

## 2. Narration (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3` … `audio/BOUT.mp3`).
- Numbers are written as spoken words — do not "fix" them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist. 15 beats → 15 MP3s, each non-empty.

## 3. Review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-11-capstone-full-stack-app --beats muse/film-11-capstone-full-stack-app/beat_sheet.json --scenes muse/film-11-capstone-full-stack-app/scenes.py --audio muse/film-11-capstone-full-stack-app/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## 4. Final 4K master

```
./art final --reel muse-film-11-capstone-full-stack-app
```

Verify: 3840×2160, runtime ≈ 280s (the sum of the audio), silent tail present.

## 5. Publish
Only on Bear's explicit instruction. Never otherwise.

## Film facts
- Beats: 15 (10 body), runtime 280s (~4m40s).
- Scenes: 13 Manim classes (M01–M13), all QC-clean
  (13 clean · 0 warnings · 0 errors).
- No MP3/MP4/WAV committed — audio and renders stay on this Mac.
