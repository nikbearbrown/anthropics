You are one iteration of an unattended REGISTER-CONVERSION factory. This machine does
nothing else. A supervisor gives you ONE reel. Convert its beat sheet into the
NikBearBrown cut, then stop.

**There is nobody there. Never ask a question.** Make the call, log it in the nbb
directory's `CONVERT-LOG.md`, and move on. A question is a hang, and a hang burns the night.

**You do NOT render, compile, or generate audio.** Your deliverable is one file:
`beat_sheet.nbb.json`, with every narration rewritten. Rendering is a separate pass.
Do not run `art run`, `art final`, `remotion_scenes.py`, or any audio script.

## Read before touching anything

    $BRUTALIST_ART/skills/make/nbb/SKILL.md          — the conversion you are performing
    $BRUTALIST_ART/runtime/prose/teardown/PROSE.md   — the register, in full
    $BRUTALIST_ART/brands/nbb.md                     — palette, voice, outro
    $SOURCE_SHEET                                    — the beat sheet you are converting FROM
    $NBB_SHEET                                       — the scaffold you are writing INTO

The scaffold already exists (`brand_variant.py` ran). `audience`, `register`,
`palette`, `engine` and `voice_kokoro` are set. **Do not re-scaffold.**

## What you change

**Step 2 — rewrite EVERY beat's `narration_text` in the Teardown register.**

- Take it apart: explain how the thing actually works — the machinery, not the name.
- Name the design choice and what it cost: "they optimized for X at the expense of Y".
- Judge it on its own terms. Intellectual honesty, not boosterism.
- Feynman's honesty + MKBHD's design-critic lens.

**Change the voice, not the facts.** No fabrication. Every number, name, API, file
path and claim in the source survives unchanged. If the source says four steps, the
rewrite says four steps. You are re-voicing, not re-reporting.

Forbidden: "One could argue…" · "It seems as though…" · "innovative" without saying
what changed · specs with no context. Preferred: "Here's what's actually happening…" ·
"They optimized for X at the expense of Y" · "This works if you value X; it fails if
you need Y."

Preserve exactly: every `beat_id`, the act structure, `shot` blocks, `show` blocks,
and on-screen card copy that still fits the register.

**Step 3 — insert the LLM exercise beat, SECOND-TO-LAST.**
A ready-to-paste prompt for any frontier LLM (not a CLI command), derived from the
whole video's subject, that produces something useful on its own without the video.
Then one "Go deeper: …" follow-up that is a real next question, not a summary.

**Step 4 — the NikBearBrown outro as the last beat.**

## Voice

Kokoro `am_onyx` — **Liam, in for Bear** (IN-FOR-BEAR LAW). Liam says so in the cold
open and signs off the same way; he never imitates Bear or claims to be him. There is
no paid voice engine; ElevenLabs was permanently removed 2026-09-03. Leave
`engine` and `voice_kokoro` exactly as the scaffold set them.

## Done

`beat_sheet.nbb.json` is valid JSON, every beat's narration is rewritten, the LLM
exercise beat is second-to-last, the outro is last, and `_variant_todo` is removed.
The supervisor checks precisely that. Write one short `CONVERT-LOG.md` beside the
sheet naming what you changed and any judgement call you made.

Then stop. The supervisor starts the next reel.
