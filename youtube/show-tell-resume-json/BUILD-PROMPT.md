# BUILD-PROMPT — show-tell-resume-json

**What this is.** How to build this film from the planning package. Run everything from `books/`.

**GATE P is open.** Nothing below has been run. Audio costs nothing on Kokoro but the render is expensive, and the narration is about Bear's own record — he clears the gate.

```bash
python3 anthropics/youtube/show-tell-resume-json/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py anthropics/youtube/show-tell-resume-json
# pad BOUT with 1.0 s of silence, then write ffprobe durations back to actual_duration_s
./brutalist.art/art run   anthropics/youtube/show-tell-resume-json --height 2160
./brutalist.art/art final anthropics/youtube/show-tell-resume-json --height 2160 \
    --out anthropics/youtube/show-tell-resume-json/exports/landscape
```

Then STOP. Staging (`art post`) and publishing happen only on Bear's word.

## Before writing scenes.py

Paste `brutalist.art/skills/make/show-tell/templates/iso_kit.py` at the top of `scenes.py` — **do not import it**, Gate A copies only `scenes.py`. Write every class literally as `class B00_OneDocument(Scene):`; `run.sh` finds scenes by that exact text and silently compiles a placeholder otherwise.

## Traps this film will hit

- **B01 and B02 depend on the inserted line looking identical to the real ones.** That fights GATE T, which samples the midpoint: a line still fading in at the midpoint reads as a fused text blob. Land it fully opaque before the midpoint and let the *position* carry the meaning.
- **B02's magnifier must not stop.** The claim is that nothing catches the line. If the animation pauses on it, the film argues the opposite of what it says.
- **B04's checks are terracotta; the row labels are ink.** Never terracotta text.
- **B08's grey rows must stay grey through the midpoint** — that is the whole beat. And the postings stack must have no cable; an accidental leader line touching it inverts the finding.
- **B03 and B06/B07/B08 share one card.** Continuity law: the card that appears in B03 is the same object through to B08, and each beat must still *add* a shape (Gate A reads an unchanged shape set as a repeated animation).
- Numerals in B06 (679) and B07 (700) are ink, never terracotta.

## If the film is cut for length

183 s estimated is at the style's ceiling. The first beats to merge are **B04 into B03** (the record and attesting it) and **B05** (generation), which is the most familiar idea in the film. Do not cut B08: the ending is the finding.
