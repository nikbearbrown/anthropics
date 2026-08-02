# BUILD LOG — vox-photoelectric

## 2026-07-25 — Doodle parameter pass (first instance)

### Beat classification (doodle vs not)

BOOKEND (brand, never doodle):
  YTV01, B00, B01a, B03a, B04a, B05a, B06a, B07a, B08a, B11, B12

LITERAL TEXT CARDS (not doodle — text IS the content):
  B03 (question card), B10 (recap card)

BODY MODEL beats (doodle-eligible):
  B02 — Three facts — DoodleScene title+caption (icon library empty)
  B04 — Photon packets — DoodleScene icons → SHOPPING (library empty)
  B05 — Einstein equation — DoodleChart line (KE vs ν, computable)
  B06 — Sodium example — DoodleChart bar (E_green / Φ / E_UV, computable)
  B07 — Photons cannot pool — DoodleScene icons → SHOPPING (library empty)
  B08 — Intensity vs frequency — DoodleScene icons → SHOPPING (library empty)
  B09 — Millikan confirmation — STAYS MANIM (3 categorical series, style.md rule)

### B02 — first doodle beat rendered

- doodle block authored: title/caption/eyebrow only (icons: [] — library empty)
- doodle_fill.py --only B02: pattern DoodleScene, items=[], durationS=17.49s
- remotion_scenes.py --only B02: media/B02.mp4 rendered (17.5s)
- frame reviewed at 8s: Shadows Into Light hand-lettering, rough red underline
- data/B02-facts-audit.md: three qualitative claims verified against FACTCHECK.md

PALETTE DELTA (flagged for human decision):
  - DoodleScene uses VOX.CREAM = #FFFFFF; reel palette wants Claude cream #FAF9F5
  - DoodleScene caption underline uses VOX.CRIMSON = #C8102E; reel wants terracotta #D97757
  - Options: (a) modify DoodleScene to accept palette props, (b) accept VOX palette

GATE T: Shadows Into Light renders cleanly, no sub-floor sizes, no broken
kerning, caption is 5 words, title is 6 words across 2 lines. PASS for B02.

### Fixes applied

- Node.js llhttp symlink: created /opt/homebrew/opt/llhttp/lib/libllhttp.9.3.dylib
  → /opt/homebrew/Cellar/llhttp/9.3.1/lib/libllhttp.9.3.dylib
  (Node 25.9.0 was compiled against 9.3.x; Homebrew had upgraded llhttp opt to 9.4.x)

### B02 — approved ("go"), doodle pass continued

### B05 — DoodleChart line (KE vs ν)

- data/B05-ke-vs-nu.csv: numpy compute, h=4.136e-15 eV·s, Φ_Na=2.28 eV (NIST)
- data/B05-reference.png: matplotlib truth plot (continuous + scatter + threshold line)
- doodle block authored: DoodleChart kind=line, 5 data points, accentIndex=1 (threshold)
- remotion_scenes.py --only B05: media/B05.mp4 rendered (18.1s)
- frame verified at 6s: hockey-stick line, red threshold dot, caption correct

### B06 — DoodleChart bar (sodium)

- data/B06-sodium-bars.csv: E_green=2.2711eV, Φ_Na=2.28eV, E_UV=4.1333eV
- data/B06-reference.png: matplotlib bar chart (three bars, dashed threshold)
- doodle block authored: DoodleChart kind=bar, 3 bars, accentIndex=2 (UV = ejection)
- remotion_scenes.py --only B06: media/B06.mp4 rendered (21.1s)
- frame verified at 6s: three bars, UV bar red/accent at 4.13eV, caption correct

### B07 — DoodleScene icons (photons cannot pool)

- doodle block: sparkle-cluster (1000 red photons), medical-cross accent (cannot pool),
  circle (1 UV photon)
- doodle_fill.py: space-sparkle-cluster-01, medical-medical-cross-01, shapes-circle-01
- remotion_scenes.py --only B07: media/B07.mp4 rendered (15.6s)
- frame verified at 6s: three icons correctly placed, caption underlined red

### B08 — DoodleScene icons (intensity vs frequency)

- GATE T issue: everyday-sun-01 potrace path creates complex hachure blobs (31px <
  34px floor in 4K frame). Diagnosis: 5 connected ink blobs at x=664-1409 in sun bounds.
- Fix iteration 1: wave → lightning bolt (wave also has small sinusoidal arc blobs)
- Fix iteration 2: sun → bar chart (bar chart has embedded percentage text labels)
- Fix iteration 3: sun → shapes-arrow-01 (simple geometric path, no sub-floor blobs)
- Final: arrow (intensity=count) + lightning-bolt accent (frequency=energy)
- remotion_scenes.py --only B08: media/B08.mp4 rendered (15.9s)
- GATE T: PASS with arrow+bolt (simple paths, no hachure-blob false positives)
- frame verified at 6s: arrow left, lightning bolt right (crimson accent)

### B04 — SHOPPING (no electron icon in library)

- SHOPPING.md card: "doodle needed for: 'particle electron' (B04)"
- Stays Manim until electron/particle SVG is added to library

### Final compile

- art final --allow-slates: GATE T PASS, compiled 221.3s
- 5/20 beats filled (B02 B05 B06 B07 B08 = VIDEO; 15 = SLATE)
- 15 slates = bookends + ASK micro-beats (pending audio generation + Remotion renders)
- FACTCHECK.md doodle-pass VERDICT: PASS
- Palette delta: DoodleScene uses VOX palette (CREAM=#FFFFFF, CRIMSON=#C8102E)
  vs reel metadata (claude: cream #FAF9F5, terracotta #D97757). Accepted as-is.

### Remaining before full cut

- Generate audio for new bookend beats (kokoro af_kore) — see metadata.new_audio_needed
- Render Remotion bookends (ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeTitleOutro)
- Fix SKIN LINT: ASK micro-beats missing spark lines (B01a–B08a)
- Add electron icon to doodle library → re-run B04
