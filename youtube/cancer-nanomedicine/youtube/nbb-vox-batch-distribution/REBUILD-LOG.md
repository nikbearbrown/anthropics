# REBUILD-LOG.md — nbb-vox-batch-distribution

Date: 2026-08-28. Snapshot: `beat_sheet.pre-rebuild.json` (byte-exact copy of the
pre-rebuild sheet, made FIRST per the rebuild contract).

## Bookend consolidation — envelope, not narration

Pre-rebuild sheet carried TWO bookend sets: canonical stubs `B00 / BVDT / BHTF /
BOUT` with EMPTY narration, plus filled `NBB00 / NBB01 / NBB02 / NBB03`
duplicates. Sibling nbb-vox-* reels (doxil-heart, abraxane-solvent) use only
the canonical set. The NBB* payload was promoted into the canonical slots and
the duplicate stubs dropped. Body beats B01–B12 were untouched.

| Was            | Now      | What moved                                             |
|----------------|----------|--------------------------------------------------------|
| NBB00 → dropped | B00     | 90-word cold-open narration + ClaudeComposerAsk props  |
| NBB01 → dropped | BVDT    | verdict slot (narration rewritten — see below)         |
| NBB02 → dropped | BHTF    | your-turn narration + ClaudeComposerAsk props          |
| NBB03 → dropped | BOUT    | outro title narration + ClaudeTitleOutro props         |
| B00  (empty)    | dropped | duplicate stub, no narration                            |
| BVDT (empty)    | dropped | placeholder "Key finding one/two/three"                 |
| BHTF (empty)    | dropped | duplicate stub, no narration                            |
| BOUT (empty)    | dropped | duplicate stub, no narration                            |

MP3 renames: `beat-NBB00 → beat-B00`, `beat-NBB01 → beat-BVDT`, `beat-NBB02 →
beat-BHTF`, `beat-NBB03 → beat-BOUT`.

## Verdict authored — REPLACED, not carried

The pre-rebuild `BVDT` was the template default (`"Key finding one/two/three"`
+ heading "Key findings"). The NBB01 verdict lines were recycled body-narration
fragments, not authored findings. Both are `verdict_audit.py` violations. A
real verdict was authored from the body's own nouns and numbers.

- **Old narration (NBB01):** "Let's recap with Claude. Here's what the body just
  demonstrated. Those three populations have different pharmacokinetics… [400+
  words of recycled body narration]"
- **New narration (BVDT):** "The verdict. Two liposomal batches with a
  98-nanometer mean can behave as different products: one circulates six hours,
  the other clears in forty-five minutes. The polydispersity index is what
  separates them — above roughly zero-point-two, a wide distribution hides
  three pharmacokinetic populations inside one label: small particles that
  clear in minutes, mid-size that behave as designed, and large that go
  straight to liver and spleen. The mean is only the center of that spread.
  Matching the distribution — not the mean — is what proves the product."
- **New artifactLines** (authored from body B02, B07, B08, B10):
  - "Two batches at 98 nm mean cleared at 45 min and 6 h."
  - "PDI above 0.2 hides three pharmacokinetic populations."
  - "Small clears fast, mid delivers, large goes to liver/spleen."
  - "Match the distribution, not the mean — that proves the product."
- **New heading:** "same 98 nm mean, forty-five minutes vs six hours in circulation"

Source: pre-rebuild body beats B02 (45 min vs 6 h), B07 (PDI 0.2 threshold),
B08 (three populations), B10 (mean vs distribution).

## Spark line — B00 greeting

- Was: `"greeting": "Liam"` (on the empty B00 stub) / `"greeting": "Your turn."`
  on NBB00 (wrong — that's the BHTF spark line).
- Now: `"greeting": "Namaste, Liam"` — Hindi hello, not used by any adjacent
  nbb-vox-* reel in this cancer-nanomedicine batch (surveyed abraxane-solvent,
  bystander-effect, endosomal-escape, protein-corona, doxil-heart, epr-gap,
  trial-failure-tree, delivery-funnel, light-ceiling — none use Hindi).

## Card props cleaned to match locked source-clip render

Two body beats had FormB/FormA remotion props with placeholder subs that would
fail GATE T. The source clip in `../vox-batch-distribution/clips/` is the
authoritative render (locked); the sheet's shot props were legacy scaffolding.
Reshaped to the CARD/STILL shape used by the source render.

- **B01:** was `FormBCard` with `Key point one/two/three` + empty subs → now
  `CARD kind:title` with copy `"Same Average Size, Different Product"` and
  sub `"Why Batches Can't Be Proved Identical Like Pills"` (matches the
  actual pre-rendered title card).
- **B02:** dropped the `FormACard` mirror of narration (which triggered §8.10
  "narration recites the card"); kept the `STILL` shape used by the source
  render.

## Datable claims

Body narration was scanned for datable claims (model names, versions, prices,
"as of" phrasing) — none found. All B01–B12 narration is generic mechanism
(PDI numbers, clearance times, tumor delivery percentages) — no rot risk.

## Bookend audio

All four bookend mp3s were re-generated fresh with Kokoro `am_onyx` at
2026-08-28 so `actual_duration_s` reflects the current narration (the pre-
rebuild NBB00 audio was 5.03s for 85 words — 16.9 wps, impossibly fast — a
truncated old take that would have desynced the composer overlay). Post-
regen: 33.3s / 29.7s / 7.8s / 2.8s for B00 / BVDT / BHTF / BOUT.

## Staging — body clips symlinked

The pre-rebuild sheet points at `../vox-batch-distribution/clips/BXX.mp4` via
`source_clip` (locked). `vox_compile.py`'s `resolve_slot` only reads
`media/<bid>.mp4`; the source_clip pointer is documentation-only. Staged the
twelve body clips as symlinks into `media/B01.mp4 … media/B12.mp4` so the
compiler picks them up as VIDEO instead of falling to SLATE.
