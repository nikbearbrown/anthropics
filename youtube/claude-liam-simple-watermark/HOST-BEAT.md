# HOST-BEAT — GATE H

**Test take for `simple`. One beat: B00.**

## Seed plate

**Primary:** `books/ask-claude/claude/claude-008.png`
Close-up, near-direct address, equipment rack with orange lamps behind. No spark
glyph, no wordmark. Best plate in the set for a talk-to-camera beat.

**Alternate:** `books/ask-claude/claude/claude-007.png` — three-quarter, slightly
wider. Use if 008's framing reads too tight at 16:9.

**Excluded:** `claude/006` (spark plaque on wall) and the entire `lab/` folder
(photoreal, wrong style, several carry the Anthropic wordmark).

## The line — 21 words

> "Someone asked what Claude's new watermark actually proves. Good question — most
> people guess wrong. Liam. Take them through it."

Voice: Kokoro `am_puck` (host). Liam is `am_onyx` and never appears on screen.
Estimated ~7s; the measured mp3 is the truth.

## Pipeline

Kokoro FIRST → mp3 is the clock and the lip-sync driver. Seedance SECOND, with that
mp3 as `audio_references` and `generate_audio: false`.

## Seedance call

| Field | Value |
|---|---|
| model | `seedance_2_0_mini` for the test, `seedance_2_0` for the keeper |
| start_image | `claude-008.png` |
| audio_references | `mp3/beat-B00.mp3` |
| generate_audio | `false` |
| duration | measured mp3 length, rounded up (4–15 window) |
| resolution | `720p` test / `1080p` keeper |
| aspect_ratio | `16:9` |
| genre | `auto` |

## Prompt

```
Stop-motion animation, articulated puppet, Laika-style handcrafted look. Hold the
seed image's character exactly: same face sculpt, same charcoal tweed suit and
patterned brown tie, same mid-century electronics lab with equipment racks and warm
orange indicator lamps behind him.

Action: the puppet speaks directly to camera, delivering the line with the measured,
unhurried cadence of someone who has explained this before. Mouth and jaw articulate
to the provided audio. Small natural head motion on stressed words; eyes stay on
lens. On the final clause he tilts his head very slightly toward frame right, as if
handing the floor to someone off-camera.

Camera: locked off, very slight handheld drift. Shallow depth of field, background
racks softly out of focus. No push, no zoom, no orbit.

Lighting: unchanged from the seed — warm practical light from the racks, soft key
from frame left, deep falloff.

Grade: warm desaturated, gentle film grain, subtle stop-motion micro-jitter between
frames. 24fps feel.

End on a held look to camera after the last word, room to cut.

Negative: no text on screen, no logos, no wall graphics, no subtitles, no modern
equipment, no photoreal human skin, no live-action footage, no camera moves, no
scene change, no second character.
```

## Take review

Three frames — first word, mid-line, final held look. Check: sculpt matches the seed,
mouth is on the words, nothing appeared on the walls, last frame is still enough to
cut from.

---
**GATE H — signed:** ______________________  (human)
