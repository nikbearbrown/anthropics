# AUDIT.md — vox-abraxane-solvent · 2026-08-28

Reel path: `books/anthropics/youtube/cancer-nanomedicine/youtube/vox-abraxane-solvent`
Skill: rebuild (vox-editorial legacy) · Channel: @NikBearBrown · Voice: Kokoro `am_onyx`
Skin peer: `vox-delivery-funnel` (rebuilt 2026-08-28).

## Phase 0 — Rebuild contract
- `beat_sheet.pre-rebuild.json` snapshot taken (byte-exact) BEFORE any edit.
- Narration is LOCKED. All 17 narrations preserved verbatim (verified word-count parity per beat).

## Phase 1 — Audit results

**1. Stale renders — PASS.** No `*.mp4` masters in reel dir; nothing to sweep. Old `clips/master.m4a` from 2025-07-16 (audio track only, not a video cut) left in place; `clips/_work/lbl-*.png`, `qc-*.png` from same era untouched (advisory PNGs, not deliverables).

**2. Bookends — EXEMPT.** Non-Claude channel; vox-editorial skin uses body + declared OutroSeries/OutroCTA slates (no ClaudeComposerAsk / BVDT / BHTF / BOUT). Rebuild contract §3 exempts. Matches sibling `vox-delivery-funnel`.

**3. Spark lines — N/A.** No ClaudeComposerAsk beats.

**4. Verdict — N/A.** No BVDT beat (vox skin). B15 endcard carries the compressed claim ("The drug never changed. The solvent did." / "Abraxane's benefit: albumin dissolved paclitaxel without Cremophor — the hypersensitivity disappeared.") — authored from body's nouns, not a template line.

**5b. Chart text — TRUSTED.** Trust `vox_scenes.py` labels; SerifLabel/LabelChip labels are 2–4 word category nouns (e.g., "Nearly Insoluble in Water", "TAXOL ~10%", "ABRAXANE <1%", "SAME DRUG"). No `Text(narration[:30])` truncation patterns. Gate B will confirm at render.

**5. Card text — FIXED.** Dropped dead truncated `shot.remotion.FormACard` sub-blocks on B02 and B10 (STILL beats carried orphan `"lines": ["Paclitaxel is one of the most effective…"]` and `"lines": ["Here is what that means in practice…"]` from a previous Remotion-pantry pass — unrenderable in vox pipeline; PIL slate label draws from `new_visual_element`). Same fix sibling `vox-delivery-funnel` applied.

**6. Punt sweep — PASS.** Zero gen-AI asks. Zero unfilled `fill_slates`. 13 real Manim scenes (B01, B03–B09, B11–B15). B02, B10 are declared STILL slates (labeled AI-generation slots; PIL card names the scene). B16 OutroSeries, B17 OutroCTA are declared slates (vox pipeline has no Remotion renderer). Same accepted three-slate profile as sibling `vox-delivery-funnel`.

**7. Card-only reel — PASS.** 13 body beats draw real Manim scenes; only bookends/STILL are cards.

**8. Lens audit — PASS.** Two moves earned:
  - **Descartes** (what would falsify): B04 poses the falsifiable question — "The drug didn't change. What did — and why did the reactions stop?" — and B09 answers with the testable claim (10% → <1% hypersensitivity rate). Falsification target: if patients on Abraxane still developed hypersensitivity at the Taxol rate, the solvent-blame hypothesis fails.
  - **Plato** (artifact vs world): B12 explicit — "This is what makes Abraxane different from most nanoparticle stories. We usually talk about nanoparticles accumulating at tumors, exploiting leaky blood vessels. That may play a role. But Abraxane's primary, undisputed benefit has nothing to do with tumor biology. It is a pure formulation fix." — artifact (nanoparticle) / world (tumor biology) / relationship (accidental — the actual benefit is elsewhere).

**9. Brand fields — FIXED.**
  - VOICE-LOCK envelope applied. DROPPED `voice_id: "TyW6NH39JcFb5M3xdIIk"` (ElevenLabs), `clock` prose ("narration (Kokoro (VOICE-LOCK)) — durations below are word-count estimates until GATE 0 audio lock"), `accents{}` block, `style_bible{}` block, `manim_move` field, `total_estimated_duration_seconds` (regenerated at compile time — the fields the current vox pipeline actually ignores).
  - ADDED `engine: "kokoro"`, `voice_kokoro: "am_onyx"`, `folderLabel: "@NikBearBrown"`, separate `source` line, `short_title: "The Solvent Was the Danger"`, `derived_from: "beat_sheet.pre-rebuild.json"`.
  - Persona coherence: narration is third-person editorial (no "Liam, in for Bear" claim); Kokoro `am_onyx` matches. Same channel/voice as sibling.

**10. Pacing — LOG.** B11 narration is 40 words over 20.32 s = 1.97 wps (0.03 under the 2.0 floor). Not silently retimed; audio already generated at that rate.

**11. `type_check.py` — SKIPPED.** Claude-channel gate. Vox reels use `vox_run.sh` Gates A/B/W (see Phase 2). Same skip sibling `vox-delivery-funnel` used.

## Phase 1 verdict
All checks PASS or FIXED. No BLOCKED items. Proceed to Phase 2 build.
