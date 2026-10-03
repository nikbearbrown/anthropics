# CLAUDE-CODE-PROMPT.md — paste-ready prompt for Claude Code (Bear's Mac)

Copy everything below the line into Claude Code, running inside this film
folder (`muse/film-09-muse-code-harness/`).


---

You are finishing a lecture film for the @NikBearBrown YouTube channel.
Persona: Liam, in for Bear. Everything except narration audio and rendered
video is already done and in this folder. Your job: render the audio and the
video. Do not publish anything.

## The film
- Title: Muse Code, the Harness
- Reel slug: muse-film-09-muse-code-harness
- Beats: 15 (see beat_sheet.json), total runtime 280s
- You are in the film folder: muse/film-09-muse-code-harness

## Files you have
- `beat_sheet.json` — the script. Each beat: id, scene, dur_s, act, voice,
  line (the exact narration), screen (what the viewer sees).
- `scenes.py` — the Manim visuals (classes M01…).
- `ACTS.md` / `SHOTLIST.md` / `FACTCHECK.md` / `SOURCES.md` — context. Read
  `SHOTLIST.md` if any visual confuses you.
- `CLAUDE-CODE-RENDER.md` — the detailed render instructions. Follow them.

## Step 1 — narration audio (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`).
- Numbers in the lines are already written as spoken words — do not "fix"
  them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- When done, verify: one MP3 per beat id, 15 files total, each
  non-empty and playable.

## Step 2 — review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-09-muse-code-harness --beats muse/film-09-muse-code-harness/beat_sheet.json --scenes muse/film-09-muse-code-harness/scenes.py --audio muse/film-09-muse-code-harness/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## Step 3 — final 4K master

```
./art final --reel muse-film-09-muse-code-harness
```

Verify the master: 3840×2160, runtime ≈ 280s (the sum of the audio),
silent tail present at the end.

## Hard rules
- NEVER commit or push any MP3, MP4, or WAV. Audio and renders stay on this Mac.
- NEVER publish, upload, or stage anything for publishing.
- When finished, report: beat count, audio files created, review-cut result,
  master resolution, runtime, and file location.
