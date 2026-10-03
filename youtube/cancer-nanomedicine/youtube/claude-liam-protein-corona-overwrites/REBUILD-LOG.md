# REBUILD-LOG.md — claude-liam-protein-corona-overwrites

Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy of the 2026-08-19 sheet).

## Narration edits (locked-script contract)

Body B00, B01, B02, B03, B04, B05, B06, B07, B08, B09: **unchanged** (byte-exact).

BVDT: authored (previous `narration_text = ""`).
- **new →** "The verdict. Within thirty seconds of injection the protein corona buries your targeting ligands, so cell-culture uptake tells you almost nothing about what reaches a tumor. Zwitterionic surfaces cut adsorption by half in vivo — none has cleared a phase two trial. The more honest strategy now is designing with the corona: apolipoprotein A-I pre-coating routes particles to hepatocytes, and the corona-coated particle is the product."
- **source →** body beats B01 (30 s overwrite), B04 (Vroman + MPS), B06 (zwitterionic ~50% in vivo, no phase 2), B07 (corona is the product).

BHTF: authored (previous `narration_text = ""`).
- **new →** "Your turn. Take the corona test protocol into your own lab. Run your nanoparticle in fifty percent human serum, measure the DLS shift and the zeta change, and decide whether to fight the corona or recruit one. Paste the prompt into Claude and run it on your own work."
- **source →** body beat B08 (DLS + zeta protocol) + B06 (fight vs recruit strategy).

BOUT: kept silent (title outro card).

## Structural edits (non-narration)

- metadata: dropped `voice_id` (ElevenLabs cruft), `_variant_todo`, `build` stub (compile.py restamps), skin_warnings stub. Kept `engine: kokoro`, `voice_kokoro: am_onyx`, added `derived_from: beat_sheet.pre-rebuild.json`.
- B01: replaced `Key point one / two / three` FormBCard items with three real items compressed from the B01 narration.
- B04: converted from Manim SLATE (`B04_ProteinCorona` scene never authored) to FormBCard with four items naming the four narration moments (Ligands / Soft corona / Hard corona / What the macrophage sees). The Manim scene remains open for a future full-render pass.
- B06, B07, B08: converted from pure slate (`shot.source = null`) to FormBCards with real items from each beat's own narration.
- Removed the erroneous `"lane": "BOOKEND"` from B01 (B01 is a body beat, not a bookend — legacy paste from the July skeleton).
- BVDT `artifactHeading`: `"Key findings"` → `"The verdict"` (matches sibling and the authored narration).
- BVDT `artifactLines`: 3 placeholder → 3 real lines from body. Line 1 rewritten a second time after Gate V caught `stripLeadNum` regex chopping the leading `30-`: `"30-second corona buries…"` → `"Within 30 s the corona buries your targeting ligands…"`.
- BHTF `command`: replaced bracketed-title placeholder `Take what you learned from [Research the Protein Corona: How the Body…]` with a real, actionable prompt referencing the DLS + zeta protocol.
- BHTF `segment`: `"Research the Protein Corona: How the Body…"` (title stub) → `"Protein corona — your work"`.
- All beats: normalized voice envelope — every beat now carries `voice: am_onyx`, `engine: kokoro`, `voice_kokoro: am_onyx`.

## Datable-claim audit

No datable claims required updates. Reel cites Wilhelm 2016 (n=117) once (in Chapter 4's context) but this reel doesn't restate the year; references to zwitterionic in-vivo reductions and phase-2 status are treated as current stable claims. No model names, prices, or "as of" phrasing appear.
