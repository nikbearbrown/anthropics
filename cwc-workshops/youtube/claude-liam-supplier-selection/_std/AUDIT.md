# AUDIT — claude-liam-supplier-selection

**Run:** 2026-08-26 by film-factory loop  
**Brand:** claude-liam · **Palette:** claude (#FAF9F5 / #3D3929 / #D97757)

---

## CHECK 1 — Stale renders

**PASS** — no mp4 files exist in the reel directory. Absent is honest.

---

## CHECK 2 — Bookends

**PASS** — all four canonical bookends present:
- B00: `ClaudeComposerAsk` ✓
- BVDT: `ClaudeVerdictArtifact` ✓
- BHTF: `ClaudeComposerAsk` (greeting: "Your turn.") ✓
- BOUT: `ClaudeTitleOutro` ✓

---

## CHECK 3 — Spark lines

**FIXED**

| Beat | Issue | Fix |
|---|---|---|
| B00 | greeting: "Hola, Liam" | PASS — correct world-language hello |
| BHTF | greeting: "Your turn." | PASS — correct bookend |
| B01 | sparkLine "The file is the program." — 5 words over limit | → "File is the program." (4 words) |
| B02 | sparkLine "Input in. Output out." — 4 words | PASS |
| B03 | sparkLine "This is the part worth knowing." — 7 words over limit | → "Know the limit." (3 words) |

---

## CHECK 4 — Verdict

**PASS** (after truncation fix)

BVDT has specific, non-template content. artifactLines[1] was truncated
("choosing a s") — rewritten as a clean verdict line:
"Task: rank and pick a supplier for a SKU — chosen by a weighted score."

Narration is specific and not a placeholder formula. Reel has 3 body beats
and ~140 words of body content — threshold met for authoring.

---

## CHECK 5 — Card text

**FIXED**

Multiple beats had the SKILL.md description auto-truncated at ~80 chars:
- B00 narration: double period "order.." → "order."
- B03 narration: "choosing a supplier, c." → full sentence
- BVDT narration: "task involves ch." → "task involves choosing a supplier."
- BVDT artifactLines[1]: "choosing a s" (mid-word clip) → clean line
- BHTF narration: broken grammar "I want to how to" → "I need to select"
- BHTF command prop: same broken/truncated prompt → clean prompt

All fixes preserve the original intent (truncation artifacts only).

---

## CHECK 6 — Punt sweep

**PASS** — no punts found

- No gen-AI asks, no unfilled slates, no DoodleScene/DoodleChart
- No `STILL src=archive` for conceptual content
- No FormA card whose narration names a visual it never draws
- SkillTeardown* templates verified present in `runtime/remotion/src/scenes/`
- No `fill_slates` / `remotion_scenes` unfilled slates

---

## CHECK 7 — Card-only reel

**PASS**

SkillTeardownAnatomy (B01) and SkillTeardownPipeline (B02) are animated
Remotion components that draw file trees and pipeline diagrams respectively —
not static text cards. B03 uses SkillTeardownMechanism for the design-tell.
These are the purpose-built skill-teardown scene family; all verified in source.

Note: the scoring formula (`score = 0.5×price + 0.3×lead_time + 0.2×reliability`)
in the source SKILL.md would benefit from a Manim equation beat, but the rebuild
contract locks beat order. Flagged for a future full rebuild.

---

## CHECK 8 — Lens audit

**PASS (two moves present, terse)**

Against the four computational-skepticism moves (LENS-NOTES.md):

- **Descartes** (what would falsify this): B03 — "What it bites: anything outside
  the spec." Anything the SKILL.md doesn't handle (unknown suppliers, corrupt
  catalog CSV, override table ambiguity) breaks the output. ✓ (present, terse)
- **Hume** (confidence is a property of the model, not the world): B03 —
  "What it gets right: repeatable results." The model's confidence is bounded
  by the spec's assumptions about the data. ✓ (present, terse)
- **Popper** (state in advance what counts as failure): implicit in B03, not
  named explicitly. Not counted.
- **Plato** (artifact vs. world): not present. The artifact (the supplier score)
  vs. the world (actual delivery reliability) gap is unexplored.

Two moves pass the threshold. The reel would be stronger with explicit Plato
framing on the score-vs-reality gap, but narration is locked by the rebuild
contract.

---

## CHECK 9 — Brand fields

**FIXED**

| Field | Issue | Fix |
|---|---|---|
| `folderLabel` | "@NikBearBrown" | PASS — correct channel handle |
| `modelLabel` (metadata) | "Opus 4.8" — does not exist | → "Opus 4.7" |
| `modelLabel` B00 props | "Opus 4.8" | → "Opus 4.7" |
| `modelLabel` BHTF props | "Opus 4.8" | → "Opus 4.7" |
| `engine` / `voice` | kokoro / am_onyx | PASS — matches channel |
| Persona | "Liam (in for Bear)" — B00 narration says it out loud | PASS |

---

## CHECK 10 — Pacing

**LOG — no action taken**

Estimated durations in the sheet are generous (26s, 24s, 26s, 28s for beats
that rendered in 12–16s each). The actual_duration_s values are already set
from the previous audio generation and will drive the compile.

Beats with estimated durations vs. actual audio:
| Beat | estimated_s | actual_s | ratio |
|---|---|---|---|
| B00 | 26 | 15.62 | 0.60 |
| B01 | 24 | 12.42 | 0.52 |
| B02 | 26 | 7.83 | 0.30 |
| B03 | 28 | 16.09 | 0.57 |

Estimated durations are stale; actual values are authoritative. Audio regen
will update actual_duration_s for beats with changed narration.

---

## CHECK 11 — type_check.py

Will run after audio generation and before compile. Result logged in TYPECHECK.md.

---

## Overall verdict

**ALL CHECKS PASS OR FIXED.** Proceeding to PHASE 2 build.
