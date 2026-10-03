# REBUILD-LOG — claude-liam-ifp-pressure-barrier
_Rebuilt 2026-08-30 by nopunt/rebuild pass._

Pre-rebuild copy: `beat_sheet.pre-rebuild.json` (byte-exact copy of the previous
`beat_sheet.json`, taken before any edit).

## Narration — LOCKED

All beat `narration_text` values on B00–B09 are byte-identical to the pre-rebuild
sheet. No datable claims required correction (IFP ranges, mouse-window duration,
Jain lab / losartan / NCT status are unchanged).

New narration was authored ONLY for the Claude bookends that previously carried
placeholders or empty strings:

- **BVDT** — was `""`. Authored a real verdict speaking the finding: elevated
  IFP reverses convection, leaky vessels are the same cause on both sides of
  the paradox, mouse normalization window is 2–6 days but human window and
  survival benefit are undemonstrated. Sourced from the body narration
  (B01–B07).
- **BHTF** — was `""` with a template `command` (`"Take what you learned from
  [X] and apply it to your own work…"`). Authored a real Your Turn: pull IFP
  range for the viewer's tumor type; check whether their trusted delivery paper
  was orthotopic vs subcutaneous; check whether normalization pretreatment was
  used and reported. Sourced from B08. `output` slots populated with a real
  worksheet.

## Envelope rebuild (VOICE-LOCK + dead fields dropped)

Dropped from metadata:
- `voice_id: "TyW6NH39JcFb5M3xdIIk"`  — ElevenLabs-era field, dead under
  Kokoro; never carried forward.
- `derived_from`, `outro_source`, `_variant_todo` — completed brand-fork
  bookkeeping; the outro_source pointer was inconsistent with the current
  Claude bookend spine.
- `build` block (stale 2026-07-16 timestamps and skin_warnings).

Set / normalized in metadata:
- `engine: "kokoro"`, `voice: "am_onyx"`, `voice_kokoro: "am_onyx"` —
  consistent across metadata and every beat that carries voice fields.
- `ground: "#FAF9F5"` (Claude PAGE) — was `#FFFFFF`.
- `color_semantics` rewritten to the Claude teardown palette (INK #3D3929,
  TERRACOTTA #D97757, SLATE #545454).

Every beat with a `voice`/`engine`/`voice_kokoro` triple was checked; all are
Kokoro `am_onyx` (Liam). Narration says "This is Liam, in for Bear." Persona
coherence: PASS.

## Shot rebuild — punts authored, bookend law enforced

Per `nopunt` SKILL and audit rule 6 (zero gen-AI ask slates, zero unfilled
pipeline slates for animatable content).

| Beat | Was | Now | Reason |
|---|---|---|---|
| B00 | `NikBearBrownOpen` | `ClaudeComposerAsk` | Bookend law for a claude channel; ask now answers the segment. Narration locked. |
| B01 | FormBCard with empty `sub` fields ("Key point one/two/three") | FormBCard with real labels + real subs compressed from B01 narration | Audit rule 5 (card text). |
| B02 | `NikBearBrownTerminalAsk`, greeting `"The ask,"` | Same pattern, greeting `"Research the IFP problem."` | Audit rule 3 — inner-composer spark line, ≤4 words, compressed from beat narration. |
| B04 | Manim `B04_IFPGradient` (unrendered SLATE; scene file does not exist). First rebuild attempt used `BarChart` (Remotion); Gate V showed the BarChart component layout is broken at 3840×2160 (bars invisible, category+value labels crammed to the top edge of frame — reproduced across every timestamp of the raw B04.mp4). Component defect is out of scope for a single-reel rebuild. | `FormBCard` (Remotion) — three tissue panels: Normal (0–3 mmHg), Solid tumor (20–60), Pancreatic (up to 80). Icons: circle-check / shield-alert / circle-x for the escalating pressure regime. | Punt costume rejected; nopunt "Enumerated concepts → FormB". Body loses its one non-card figure — logged as a partial audit rule 7 concession (see AUDIT.md). |
| B05 | greeting `"The ask,"` | greeting `"The normalization window."` | Audit rule 3 — ≤4 words, compressed from B05 narration. |
| B06 | `null` shot / `YOU → gen-AI clip → pantry` | `FormBCard` — 3 panels (Mouse window / Losartan mechanism / Trial status) drawn from B06 narration | Punt costume rejected; nopunt "Enumerated concepts → FormB". |
| B07 | `null` shot / `YOU → gen-AI clip → pantry` | `FormBCard` — 2 panels (Enables EPR / Blocks delivery) drawing the contradiction | Punt costume rejected; enumerated contrast → FormB. |
| B08 | `null` shot / `YOU → gen-AI clip → pantry` | `FormBCard` — 3 panels (Tumor IFP / Model type / Combination) drawn from B08 narration | Punt costume rejected; enumerated actions → FormB. |
| B09 | `NikBearBrownOutro` | unchanged | Narration locked. Kept as channel signature; not one of the four canonical bookend positions (audit rule 2 lists B00/BVDT/BHTF/BOUT). |
| BVDT | placeholder `"Key finding one/two/three"` + empty narration | Real verdict lines + real narration | Audit rule 4. |
| BHTF | template `command` + empty `output` + empty narration | Real exercise + real worksheet lines + real narration | Audit rule 5c. |
| BOUT | `ClaudeTitleOutro` | unchanged | Canonical. |

## Lens (audit rule 8)

Two moves earn their place naturally from the source:

- **Popper (falsifiability, stated in advance)** — the Jain lab NCT trials
  "show improved drug delivery … but no survival benefit has been demonstrated
  yet." Delivery is the surrogate; survival is the falsifier stated in advance,
  still open.
- **Plato (artifact ≠ world)** — B08 explicitly separates the model (the
  subcutaneous mouse tumor with low IFP) from the world (the orthotopic /
  clinical tumor with high IFP). "The pressure barrier is not in the
  subcutaneous model. It is in the real tumor."

## FormB icon fixes (after first render pass)

First render pass failed on all four FormBCard beats with 404s from the icon
loader (`http://localhost:3000/public/form-b-icons/<name>.svg`). The library
holds only a fixed set of icon SVGs in
`runtime/remotion/public/form-b-icons/`; unknown names 404 and cancel the
render. Fixes:

| Beat | Icon(s) swapped | Replacement (from library) |
|---|---|---|
| B01 | `gauge` → `ruler` (Tumor IFP); `arrow-left` → `crosshair` (Reversed gradient) | ruler = measured range; crosshair = opposition of the gradient |
| B04 | initial `BarChart` fallback; then `circle-check` / `shield-alert` / `circle-x` for Normal / Solid tumor / Pancreatic | escalating from OK → warning → blocked |
| B06 | `clock` → `snowflake` (Mouse window); `flask-conical` → `clipboard-list` (Trial status) | snowflake = narrow frozen window; clipboard-list = trial results |
| B07 | `arrow-right` / `arrow-left` → `circle-check` / `circle-x` | polarity that reads at a glance |
| B08 | `gauge` → `ruler`; `flask-conical` → `frame` (Model type); `clock` → `list-checks` (Combination) | ruler = measured range; frame = which model frame; list-checks = the sequence to run |

## Not changed

- No datable claims were edited (all IFP ranges, mouse window, losartan
  mechanism, trial status are as in the pre-rebuild sheet; consistent with
  Jain lab literature).
- B03 code block is preserved verbatim (locked artifact).
