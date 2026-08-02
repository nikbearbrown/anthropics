# BUILD — blank SVG plates (stills)

Point Claude Code at this file to (re)build the blank Okabe-Ito **SVG stills** for a
plate set. Run from the book's `illustrae/` folder (e.g. `cancer-biology/illustrae/`).

## What you're building
One blank, unannotated vector diagram per cajal prompt — Okabe-Ito palette, white ground,
**no baked text** (the previz/reel layer owns every label). Plus PNGs and a stills contact
sheet. These are the "what it looks like" reference; motion is built separately
(see `BUILD-PLATES-MANIM.md`).

## Inputs (in this folder)
- `plates_gen.py` — the geometry engine. Primitives return backend-agnostic shape records;
  the SVG backend renders them. This is the single source of truth for plate geometry.
- `CAJAL-FIGURE-CANDIDATES.md` — the cajal `ILLUSTRAE PASTE BLOCK` prompts (the specs each
  plate renders). Section NN ↔ plate NN.

## Build
```bash
# from <book>/illustrae/
PLATES_OUT="$PWD/plates" python3 plates_gen.py
```
Outputs: `plates/NN-slug.svg` (always), `plates/NN-slug.png` (if `cairosvg` is installed),
`plates/contact-sheet.html`. SVG generation needs only Python — no dependencies.

## Add or change a plate
1. In `plates_gen.py`, write `def pNN(): ... return W, H, b` where `b` is a list of shape
   records built from the primitives: `node/rect/circ/dot/ln(arrow)/poly/cluster/vstack/…`.
   Coordinates are pixel-space, y-down; keep to **6–8 components** (cajal cap).
2. Register it in `PLATES` (num, slug, fn) and add a `META[num]` entry (title, pattern, priority).
3. Re-run the build. The still, PNG, and contact-sheet update automatically.

## Rules (do not violate)
- **Blank only** — never bake text, numbers, or labels into a plate.
- Okabe-Ito palette, white background, single-headed arrows, no red/green pairing, no 3D.
- Grayscale test: the diagram must read with color removed.

## QC
Open `plates/contact-sheet.html`, or view a few `plates/NN-slug.svg`. Confirm each is blank,
on-palette, and structurally matches its cajal section. Never publish.
