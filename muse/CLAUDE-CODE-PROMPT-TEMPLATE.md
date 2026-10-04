# CLAUDE-CODE-PROMPT-TEMPLATE.md

Template for the paste-ready Claude Code prompt that ships in every film
folder as `CLAUDE-CODE-PROMPT.md`. When building a film, copy everything from
the title line below into the film folder's `CLAUDE-CODE-PROMPT.md` and fill in
the `{{PLACEHOLDERS}}`.

Placeholders:
- `{{TITLE}}` — the film's title, e.g. `What Muse Is`
- `{{REEL_SLUG}}` — e.g. `muse-film-01-what-muse-is`
- `{{BEAT_COUNT}}` — e.g. `16`
- `{{TOTAL_S}}` — total runtime in seconds, e.g. `286`
- `{{TOTAL_M_S}}` — human runtime, e.g. `4m46s`
- `{{SCENE_COUNT}}` — number of Manim scene classes, e.g. `14`
- `{{SCENE_RANGE}}` — e.g. `M01–M14`
- `{{FILM_DIR}}` — the FULL local path on Bear's Mac, WITH trailing slash, e.g.
  `/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/muse/film-01-what-muse-is/`

# CLAUDE-CODE-PROMPT.md — paste-ready prompt for Claude Code (Bear's Mac)

Copy everything below the line into Claude Code, running inside this film folder:
`{{FILM_DIR}}`

---

You are finishing a lecture film for the @NikBearBrown YouTube channel.
Persona: Liam, in for Bear. Everything except narration audio and rendered
video is already done and in this folder. Your job: render the audio and the
video. Do not publish anything.

## The film
- Title: {{TITLE}}
- Reel slug: {{REEL_SLUG}}
- Beats: {{BEAT_COUNT}} (see beat_sheet.json), total runtime {{TOTAL_S}}s ({{TOTAL_M_S}})
- You are in the film folder: {{FILM_DIR}}

## Files you have
- `beat_sheet.json` — the script. Each beat: id, scene, dur_s, act, voice,
  line (the exact narration), screen (what the viewer sees).
- `scenes.py` — the Manim visuals ({{SCENE_COUNT}} classes, {{SCENE_RANGE}}).
- `ACTS.md` / `SHOTLIST.md` / `FACTCHECK.md` / `SOURCES.md` — context. Read
  `SHOTLIST.md` if any visual confuses you.
- `CLAUDE-CODE-RENDER.md` — the detailed render instructions. Follow them.

## Step 1 — narration audio (Kokoro, voice am_onyx)
For EVERY beat in `beat_sheet.json`, synthesize the beat's `line` field
EXACTLY as written using Kokoro TTS voice `am_onyx`, and save to
`audio/<BEAT_ID>.mp3` (e.g. `audio/BIDEA.mp3`, `audio/B01.mp3`, …
`audio/BOUT.mp3`) — {{BEAT_COUNT}} files total.
- Numbers in the lines are already written as spoken words — do not "fix"
  them back to digits.
- Liam persona, Teardown register: read it straight, no added intro/outro.
- Create `audio/` if it doesn't exist.
- When done, verify: one MP3 per beat id, {{BEAT_COUNT}} files total, each
  non-empty and playable.

## Step 2 — review cut
From the brutalist.art toolkit directory on this Mac:

```
./art run --reel {{REEL_SLUG}} --beats {{FILM_DIR}}beat_sheet.json --scenes {{FILM_DIR}}scenes.py --audio {{FILM_DIR}}audio/
```

Watch the review cut (or spot-check act by act). If a scene visibly breaks,
stop and report which scene and what you see — do not redesign the film.

## Step 3 — final 4K master

```
./art final --reel {{REEL_SLUG}}
```

Verify the master: 3840×2160, runtime ≈ {{TOTAL_S}}s (the sum of the audio),
silent tail present at the end.

## Hard rules
- NEVER commit or push any MP3, MP4, or WAV. Audio and renders stay on this Mac.
- NEVER publish, upload, or stage anything for publishing.
- When finished, report: beat count, audio files created, review-cut result,
  master resolution, runtime, and file location.
