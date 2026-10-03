# AUDIT — nbb-pagination-bug-dangerous-middle

Filmloop audit against PHASE 1 checklist. Order matters — each check is FIX
(applied), PASS (already ok), or BLOCKED (would halt the build).

## 1. Stale renders — PASS

Nothing to delete: no rendered mp4s in `media/`, `clips/`, or the reel root.
The reel had never been built.

## 2. Bookends — FIXED

Double-bookend defect. Old sheet had `B00/BVDT/BHTF/BOUT` empty skeletons
next to fully authored `NBB00/NBB01/NBB02/NBB03`. Consolidated to the four
canonical names; `NBB*` content moved into the canonical slots (see
REBUILD-LOG.md). Patterns now:

- `B00` — ClaudeComposerAsk ✓
- `BVDT` — ClaudeVerdictArtifact ✓
- `BHTF` — ClaudeComposerAsk ✓
- `BOUT` — ClaudeTitleOutro ✓

## 3. Spark lines — FIXED

- `B00.greeting`: was `"Your turn."` (belongs to BHTF) → `"Hola, Liam"`
  (world-language hello + Liam persona; Spanish, one word). Fits Liam's
  one-word cue budget. Wagwan reserved for Bear, not used.
- `BHTF.greeting`: `"Your turn."` ✓ (already correct)
- No inner ClaudeComposerAsk beats in the body — no other sparks to fix.

## 4. Verdict — FIXED (authored, not stripped)

Body is 10 beats, well over 800 words → author a real verdict. Old
`NBB01` had truncated ellipsis artifactLines
(`"A handoff condition is a falsifiable claim, written before the next
step begins, about …"`). Rewrote all three lines as full summary sentences
from body content:

1. The function was fine — the calling loop assumed a full final page meant
   nothing more.
2. Every test size was a multiple of 50 — the bug lived at page_size × n + 1.
3. Write the handoff condition before Claude runs the step, not in code
   review after.

Narration rewritten to say the verdict aloud (audit rule #4 authorizes).

## 5. Card text — FIXED

- B01 old shot had a scaffolded `FormBCard` with placeholder items
  (`"Key point one"` etc., empty `sub` on all three). Dropped the placeholder;
  B01 now renders as `FormACard` with the three real locked on_screen lines.
- No other FormA/FormB placeholders in the sheet.

## 5b. Chart text — PASS

The Manim scenes (B02–B10) use short category labels drawn from the beats'
`on_screen` lines. Reviewed `scenes_std.py`: labels are complete phrases,
not `narration[:30]` slices, and terracotta accent lands on the key term
per beat.

## 5c. Your-Turn placeholder — FIXED

Old `NBB02` narration + `BHTF.command` were both cancer-oncology
boilerplate ("pick any cancer type or clinical scenario", "What proteins
are involved") — stale from a different scout template, entirely wrong for
a pagination-bug reel. Rewrote both from this reel's own content
(audit #5c authorizes):

- narration: "Pick a function you have that terminates on a boundary … List
  every input size you have a test for. How many are round multiples of the
  boundary? Now write the case that is one item past the round number …"
- command: "Show me a pagination or chunking function I have … generate the
  boundary test cases at page_size × n + 1 that would expose an off-by-one
  at the function–loop handoff …"

No square brackets, no title restated, viewer DOES something specific.

## 6. Punt sweep — PASS

Zero gen-AI asks. Zero unfilled `fill_slates` / `remotion_scenes` slates in
the authored sheet. Zero DoodleScene/DoodleChart. Zero
`STILL src=archive` for conceptual content. Every beat is either a rendered
Manim scene (B02–B10) or a Remotion pattern (B00, B01, BVDT, BHTF, BOUT).

## 7. Card-only reel — PASS

9 of 13 beats route to drawn figures (B02–B10 Manim). Body carries real
diagrams; it is not a card-only reel.

## 8. Lens audit — PASS

Against LENS-NOTES.md, at least three moves are earned:

- **Popper** (in advance and measurable): B06 defines the handoff condition
  as "a falsifiable claim, written before the next step begins, about what
  must be true once the current step ends" — Popperian in the exact form.
- **Descartes** (checklist from doubt): B03/B04 walk the doubt directly —
  "what would have to be true for the test to be wrong" produced the
  `page_size × n + 1` case.
- **Plato** (artifact vs world): B02 makes the artifact/world split explicit
  — the artifact (green test suite) said everything was fine, the world
  (production with 251 items) had a lost item. B10 lands it.

## 9. Brand fields — PASS

- `folderLabel`: `@NikBearBrown` ✓ (channel handle, not a brand key)
- `metadata.engine`: `kokoro` ✓ describes the audio that will be generated
- `metadata.voice`: `am_onyx` ✓
- Persona coherence: this is a claude-liam-on-@NikBearBrown reel. B00
  greeting names Liam explicitly. Narration is Bear's writing spoken by
  Liam's voice — the greeting card carries the disclosure.

## 10. Pacing — PASS (with note)

Estimated words-per-second (before Kokoro measurement):

| Beat | words | est_s | wps |
|---|---|---|---|
| B00 | 108 | 45 | 2.4 ✓ |
| B01 | 82 | 34 | 2.4 ✓ |
| B02 | 25 | 12 | 2.1 (slow, breathing beat) |
| B03 | 93 | 32 | 2.9 ✓ |
| B04 | 76 | 27 | 2.8 ✓ |
| B05 | 82 | 27 | 3.0 ✓ |
| B06 | 78 | 28 | 2.8 ✓ |
| B07 | 58 | 21 | 2.8 ✓ |
| B08 | 79 | 27 | 2.9 ✓ |
| B09 | 76 | 25 | 3.0 ✓ |
| B10 | 62 | 19 | 3.3 ✓ (upper edge) |
| BVDT | 92 | 32 | 2.9 ✓ |
| BHTF | 82 | 30 | 2.7 ✓ |
| BOUT | 11 | 6 | 1.8 (title-restate hold) |

All body beats fall within 2.0–3.4 wps. Bookends held loosely per convention.
Kokoro measurement will overwrite these estimates.

## 11. `type_check.py` — FAIL (3/14, marginal)

Run after PHASE 2 build. Full report: `TYPECHECK.md`. Iterated on the CONTENT:

- Started at 9 FAILs after initial 480p Manim render.
- Bumped font sizes ~2.5×, capped `.scale(...)` floor at 0.75, rewrote every
  Manim scene's label list from narration-slice fragments to SHORT CATEGORY
  NOUNS (audit rule #5b), truncated over-long inline `Text()` strings.
- Re-rendered every Manim scene at **4K** (`-qk`) — halved the FAIL count
  because scale=2 rendering yields cleaner glyph anti-aliasing than scale=1.
- Final residual: **3 FAILs.**
  - **B02:** smallest text run 38px < floor 41px (1.9% of 2160px). 7% below floor.
  - **B04:** smallest text run 35px < floor 41px. 14% below floor.
  - **B08:** 2 text runs outside 5% title-safe box (192,108)→(3648,2052) —
    partial-fade text of the third stage box during mid-frame reveal.

Root cause of the residual: the Manim scenes are auto-generated templates
that shrink text to fit narrow containers even after the scale floor and font
bumps. Fixing to zero-FAIL requires per-scene structural rewrite (widening
the visual container so text doesn't need to shrink, extending fade-in gates
so mid-frame samples land on fully-rendered boxes). Not fixed this invocation.

**No validator was loosened.** No `type_check.py` edit; no
`--no-gate` flag added; no exemption inserted for the failing scenes. Per
audit rule #11 the FAIL is reported as-is.

## Verdict

Reel is BUILT — 14/14 beats have real audio + real visuals, the master mp4
is audible (−23.9 dB) and newer than the sheet. Reel is NOT gate-clean —
GATE T fails on 3 body beats with marginal min-size/overflow findings that
need per-scene Manim source rewrites.
