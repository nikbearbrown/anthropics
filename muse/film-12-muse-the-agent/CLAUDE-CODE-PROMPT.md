# CLAUDE-CODE-PROMPT.md — paste-ready prompt for Claude Code (Bear's Mac)

Copy everything below the line into Claude Code, running inside this film folder:
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-12-muse-the-agent/`

---

You are finishing a lecture film for the @NikBearBrown YouTube channel.
Persona: Liam, in for Bear. Everything except narration audio and rendered
video is already done and in this folder. Your job: render the audio and the
video. Do not publish anything.

## The film
- Title: Muse the Agent: What It Does, Who Pays, and How to Survive It
- Reel slug: muse-film-12-muse-the-agent
- Beats: 17 (see beat_sheet.json), total runtime 386s
- You are in the film folder: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-12-muse-the-agent

## Files you have
- `beat_sheet.json` — the script. Each beat: id, scene, dur_s, act, voice,
  line (the exact narration), screen (what the viewer sees).
- `scenes.py` — the Manim visuals (classes M01…M15).
- `ACTS.md` / `SHOTLIST.md` / `FACTCHECK.md` / `SOURCES.md` — context. Read
  `SHOTLIST.md` if any visual confuses you.
- `CLAUDE-CODE-RENDER.md` — the detailed render instructions. Follow them.

## Step 1 — narration audio (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`) — 17 files total.
- Numbers in the lines are already written as spoken words — do not "fix"
  them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- When done, verify: one MP3 per beat id, 17 files total, each non-empty
  and playable.

## Step 2 — review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel muse-film-12-muse-the-agent --beats /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-12-muse-the-agent/beat_sheet.json --scenes /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-12-muse-the-agent/scenes.py --audio /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-12-muse-the-agent/audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## Step 3 — final 4K master

```
./art final --reel muse-film-12-muse-the-agent
```

Verify the master: 3840×2160, runtime ≈ 386s (the sum of the audio),
silent tail present at the end.

## Hard rules
- NEVER commit or push any MP3, MP4, or WAV. Audio and renders stay on this Mac.
- NEVER publish, upload, or stage anything for publishing.
- When finished, report: beat count, audio files created, review-cut result,
  master resolution, runtime, and file location.
