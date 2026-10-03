# REBUILD-LOG.md — nbb-lnp-endosomal-escape

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.
Pattern mirrors sibling `nbb-nanoparticle-characterization` (Liam Claude wrapper of a Nik Bear Brown source reel), 2026-08-28.

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-28 before any edit (22,539 B).

## LOCKED (unchanged)

- Body B01–B08 `narration_text` — verbatim from pre-rebuild sheet.
- Body B02 (`NikBearBrownTerminalAsk` claude command), B03 (`NikBearBrownCodeBlock` code), B04 (Manim intent), B05 (`NikBearBrownTerminalAsk` claude command) — verbatim.
- Wrapper narration verbatim: `NBB00→B00` (84 words, Liam cold-open ask), `NBB01→BVDT` recap prose (128 words, "Let's recap with Claude…" + B07+B08 body content verbatim), `NBB03→BOUT` (title only, silent).
- Metadata identity: title, slug, topic, register, palette, source pointer.

## REBUILT (regenerated)

1. **Voice envelope** — `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx` stamped on metadata + every beat.
2. **Bookend surgery** (matches nano-char rebuild §2):
   - `NBB00` → `B00` (Liam ClaudeComposerAsk cold open).
   - `NBB01` → `BVDT` (Liam ClaudeVerdictArtifact).
   - `NBB02` → `BHTF` (Liam ClaudeComposerAsk your-turn).
   - `NBB03` → `BOUT` (Liam ClaudeTitleOutro).
   - Dropped the empty placeholder `BVDT/BHTF/BOUT` scaffolds at the tail (they had `narration_text: ""` and placeholder `Key finding one/two/three` verdict lines).
   - Dropped source `B00` (`NikBearBrownOpen`; "Nik Bear Brown. One to two percent. The mRNA medicine bottleneck.") — the Liam ClaudeComposerAsk cold open now plays the opening role, per nano-char / abraxane pattern.
3. **Mp3 renames on disk**: `beat-NBB00.mp3` regenerated (see §5), `beat-NBB01.mp3 → beat-BVDT.mp3`, `beat-NBB02.mp3 → beat-BHTF.mp3`, `beat-NBB03.mp3 → beat-BOUT.mp3` — then all 12 beats regenerated fresh to be safe.
4. **Body FormBCard authoring** — the pre-rebuild sheet had `source: null` slate holes at B06/B07/B08 and a placeholder FormBCard at B01 with `Key point one/two/three` labels and empty `sub` strings. Authored real FormBCards from each beat's own narration (nouns, numbers):
   - B01 "The 1–2% Escape Floor" — three items (escape, degradation, bottleneck).
   - B06 "Three Ways to Move the Floor" — ionizable-lipid library (5–10×), fusogenic peptides (GALA), endosome-disruptive polymers.
   - B07 "The Cell's Pathogen Defense" — endolysosomes as defense, partial pH exploit, vaccines OK / cancer gene therapy needs more.
   - B08 "Your Move" — check pKa (6.2–6.5), verify PEG shedding, Onpattro reference.
5. **Kokoro audio regeneration** — all 12 mp3s regenerated fresh (see AUDIT.md §Pacing table). B00 was the required regen: old `beat-NBB00.mp3` was 5.78 s against 84 words (14.5 wps, impossible). New `beat-B00.mp3` = 32.98 s (2.55 wps).
6. **Spark line fix** — B00 `props.greeting` was `"Your turn."` (that slot belongs to BHTF; B00 cold-open needs a world-language hello). Set to `"Sawubona, Liam."` (Zulu, 2 words) — not adjacent-reel duplicate (adjacent nbb reels use "Namaste, Liam.", "Bonjour, Liam", "Olá, Liam", "Annyeong, Liam", "Vanakkam, Liam"). BHTF greeting `"Your turn."` retained.
7. **Verdict artifact lines (BVDT)** — placeholder truncated body-sentence ellipsis fragments (`"The three approaches: ionizable lipid library screening has pushed escape efficiency up…"` etc.) REPLACED with four real verdict lines authored from body nouns/numbers:
   - "The 1–2% escape floor is the mRNA-medicine bottleneck."
   - "Ionizable lipids flip cationic at pH 5.5 — the ALC-0315 trick."
   - "Best published lift: 5–10× via lipid-library screening."
   - "Optimal pKa 6.2–6.5; PEG must shed or escape collapses."
   `artifactHeading` `"Key findings"` → `"lnp escape: 1–2% is the floor, not the ceiling"` (matches nano-char's `"nanoparticle: a distribution, not a molecule"` pattern).
8. **BHTF (your-turn) command** — old command was the generic bracketed-title ask-Claude-about-your-case template (`Explain how [Research LNP Endosomal Escape: The Bottleneck That Limits mRNA Medicin] applies to a specific cancer type…`). Replaced with a specific rubric-bearing prompt drawn from B08's next-steps content (`Pick an mRNA formulation you're studying. Look up: (1) the ionizable lipid and its pKa; (2) the PEG-lipid and its shedding half-life; (3) any published endosomal-escape number…`) plus an evaluation rubric. Narration lightly rewritten (28 words) to match the more specific prompt — regenerated with Kokoro (10.84 s, 2.58 wps).
9. **BOUT subline** — the old `subline` was a mid-word snippet of a body sentence (`"then check whether the formulation uses peg-lipid shedding — if peg does not she"`, character-truncated mid-word). Replaced with the verdict headline: `"1–2% escape is the mRNA-medicine bottleneck."`
10. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from ClaudeComposerAsk props on B00 and BHTF. Same rationale as nano-char §9: this is a Kokoro nbb reel, not a Claude model-branded cut.
11. **B04 Manim rework** — inherited source `vox_scenes.py` had cream-background rectangles narrower than the text they backed, so an adjacent Slate/dark rectangle would clip a letter or two mid-word ("ENDOSOME" read as "NDOSOM", "LNP" as "NP", "ALC-0315" as "LC-0315"). Rewrote `_boxed()` helper that computes bg width from text width + padding. Repositioned LNP label to sit right of the circle instead of touching it; moved ALC-0315 label further from the endosome box. Also added `self.wait()` calls between animations so total scene = 24.2 s (compile slow-mo now 1.13×, was 3.9× extreme-slow warning). `manim` source-path import was rewritten to `from manim import *` — the original relied on a `vox_graphics` module at a path that does not exist in this tree.

## Datable-claim edits

None to narration text. All quantitative claims (1–2% escape, 98–99% degradation, ionizable-lipid pKa 6.2–6.5, ALC-0315 / SM-102 / ALC-0159 lipid names, Onpattro 2018 approval, 5–10× best published lift, GALA fusogenic peptide) are drawn from the source-reel FACTCHECK.md and remain valid.

## Dropped fields

- Metadata: `body_beats`, `old_outro_beats`, `body_duration_s` (redundant with beats array).
- Every wrapper beat: legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` from `ClaudeComposerAsk` props (nbb Kokoro reel, not Claude-branded).
- Old empty `BVDT/BHTF/BOUT` scaffolds at end of beats array (empty `narration_text`, placeholder `Key finding one/two/three` verdict lines).
- Source `B00` (NikBearBrownOpen) beat entry — replaced by Liam wrapper bookend per nano-char pattern.
- Body beat `source_clip` / `source_audio` pointers to `../lnp-endosomal-escape/clips/…` — parent reel has no built clips (Cohort B), so we built fresh renders and audio here rather than inherit.

## Reel-level notes

- Persona coherence: Liam narrates the wrapper (`am_onyx` speaking Claude cold-open / verdict / your-turn / outro cards); Bear's body narration is voiced by the same `am_onyx` engine here (his own recording never existed for this Cohort-B reel). Skin does the persona work — ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro for Liam, NikBearBrownTerminalAsk / NikBearBrownCodeBlock / FormBCard for Bear's body.
