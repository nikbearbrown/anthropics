# BUILD — Manim viz (motion)

Point Claude Code at this file to (re)build the **Manim animation** for every plate. Run from
the book's `illustrae/` folder. The animation is built from the *same* geometry as the SVG
still (one source, so they can't drift).

## What you're building
One animated scene per plate — the blank diagram assembling in motion (shapes fade in, arrows
grow), Okabe-Ito, no text. Rendered to mp4 and shown beside the still in the contact sheet.
This is the baseline motion; **mechanism-tuned** choreography (the balance tipping, the dots
escaping, the gate pulsing) is the reel/`cli-explainer` job — see the exemplar below.

## Inputs (in this folder)
- `plates_gen.py` — records + the Manim backend (`make_construct`): turns a plate's shape
  records into an animated `Scene`. Same records the SVG uses.
- `manim_plates.py` — exposes one class per plate: `Plate01` … `Plate20`.
- `rb_scene.py` — a **hand-tuned** exemplar (plate 05, rb-convergence): the fan-in converging,
  the gate pulsing, the fire to output. Copy this pattern when a plate needs bespoke motion.

## Build
Use the house Manim (run under the `brutalist-art/` runtime so the toolkit's Manim is used).
```bash
# render all (also refreshes the contact sheet with animations):
PLATES_OUT="$PWD/plates" python3 plates_gen.py       # renders if `manim` is on PATH
# or render one scene directly:
manim -ql manim_plates.py Plate06
```
Outputs: `plates/manim/NN-slug.mp4`, and `plates/contact-sheet.html` (still + animation per plate).

## Hand-tune a plate's motion (when baseline isn't enough)
1. Copy `rb_scene.py` to a new scene; import the plate's records
   (`from plates_gen import p06`), build the mobjects, then choreograph: `Create`,
   `GrowArrow`, `Rotate` (a balance tipping), `MoveAlongPath` (dots escaping), `Flash`
   (a gate pulse), `Transform` (before→after states).
2. Keep it blank and Okabe-Ito. Render, QC by looking at a frame.

## Wire into a reel (cli-explainer OUTPUT beat)
Each `PlateNN` scene is the moving **OUTPUT** beat of a `cli-explainer` reel — the video
shows the Claude Code prompt, the actual Manim code (this scene), then this animation.
Follow `<book>/youtube/SERIES-BUILD-PROMPT-cli-explainer.md`.

## Rules
- Motion built from the plate's records — never hand-draw a scene that disagrees with the still.
- Blank, Okabe-Ito, no text. Never publish (leave at review cut).
