# REBUILD-LOG.md — nbb-nanoparticle-characterization

Locked-script rebuild per `books/brutalist-art/skills/make/rebuild/SKILL.md`.
Pattern mirrors sibling `nbb-vox-abraxane-solvent` (Liam Claude wrapper of a Nik Bear Brown source reel).

## Snapshot

- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet, made 2026-08-27 before any edit (23,607 B).

## LOCKED (unchanged)

- Body B01–B08 `narration_text` — verbatim from pre-rebuild sheet (which itself carries the parent reel's Jul-16 script).
- Body B01–B08 shot patterns, props (FormBCard items, terminal-ask command strings, code block source) — verbatim from pre-rebuild sheet.
- Body B01–B08 clip and audio contents — inherited from the parent reel `../nanoparticle-characterization/` after that reel's own 2026-08-27 rebuild.
- Wrapper narration verbatim: `NBB00→B00` (84 words, Liam ask), `NBB01→BVDT` (120 words, "Let's recap with Claude…" recap of B07+B08), `NBB03→BOUT` (title-only outro).
- Metadata identity: title, slug, topic, register, palette, source pointer.

## REBUILT (regenerated)

1. **Voice envelope** — `engine: kokoro`, `voice: am_onyx`, `voice_kokoro: am_onyx` stamped on metadata + every beat.
2. **Bookend surgery** (matches abraxane rebuild §2):
   - `NBB00` → `B00` (Liam ClaudeComposerAsk cold open).
   - `NBB01` → `BVDT` (Liam ClaudeVerdictArtifact).
   - `NBB02` → `BHTF` (Liam ClaudeComposerAsk your-turn).
   - `NBB03` → `BOUT` (Liam ClaudeTitleOutro).
   - Dropped the empty placeholder `BVDT/BHTF/BOUT` scaffolds that duplicated the NBB set (they had `narration_text: ""` and placeholder verdict lines).
   - Dropped source `B00` (`NikBearBrownOpen` intro — "Nik Bear Brown. A nanoparticle is a distribution. Not a molecule.") — the Liam cold open now plays the opening role, per abraxane/doxil-heart pattern. Loses Bear's 5 s branded intro; brand preserved via `@NikBearBrown` `folderLabel` on every Claude card.
   - Dropped source `B09` (Bear's outro) — Liam's BOUT now plays that role.
3. **Mp3 renames on disk**: `beat-NBB00.mp3 → beat-B00.mp3`, `beat-NBB01.mp3 → beat-BVDT.mp3`, `beat-NBB02.mp3 → beat-BHTF.mp3`, `beat-NBB03.mp3 → beat-BOUT.mp3`.
4. **B00 audio regeneration** — pre-existing `beat-NBB00.mp3` was 4.8 s but the beat's `narration_text` is 84 words (17.5 wps — impossible; Jul-16 mp3 had been generated from a truncated text). Regenerated with Kokoro `am_onyx` → 32.81 s (2.56 wps). Re-rendered `media/B00.mp4` at the new duration. This is the ONE datable-adjacent narration fix; the `narration_text` string itself was never modified — only the mp3 was brought in sync with it.
5. **Spark line fix** — B00 `props.greeting` was `"Your turn."` (that belongs to BHTF, and B00 as a cold open needs a world-language hello). Set to `"Namaste, Liam."` — 4 words, not adjacent-reel duplicate (abraxane: "Olá", doxil-heart: "Salaam"). BHTF greeting `"Your turn."` retained.
6. **Verdict artifact lines (BVDT)** — placeholder truncated body-sentence ellipsis fragments (`"The three discordances: first, protein corona — the nanoparticle you characterized in b…"` etc.) REPLACED with four real verdict lines authored from body's own nouns/numbers:
   - "A nanoparticle is a distribution, not a molecule."
   - "Seven cascade measurements; each has its own artifact."
   - "Buffer characterization is not plasma behavior."
   - "Batch variability is the product, not impurity."
   `artifactHeading` `"Key findings"` → `"nanoparticle: a distribution, not a molecule"` (matches abraxane's `"abraxane: the solvent, not the drug"` pattern).
7. **BHTF (your-turn) command** — old command was the generic ask-Claude-about-your-case template. Replaced with a specific, rubric-bearing prompt drawn from B08's next-steps content (`Run your own nanoparticle formulation through the seven-measurement cascade, then re-run DLS in fifty-percent human serum…`) plus an evaluation rubric (all seven measurements as numbers, Δnm computed, one falsifiable prediction). Segment shortened; `folderLabel: "@NikBearBrown"` kept. Narration lightly rewritten (19 words) to match the more specific prompt — regenerated with Kokoro (6.38 s, 2.98 wps).
8. **BOUT subline** — the old `subline` was a mid-word snippet of a body sentence (`"the gap between those two numbers is your corona delta — and it predicts in vivo"`). Replaced with the verdict headline (`"A nanoparticle is a distribution, not a molecule."`).
9. **Fable-5 labels dropped** — `modelLabel: "Fable 5"` / `effortLabel: "High"` removed from ClaudeComposerAsk props on B00 and BHTF. Same rationale as abraxane rebuild §6: this is a Kokoro nbb reel, not a Claude model-branded cut.
10. **Body renders + audio** — body clips B01–B08 copied from parent `clips/BXX.mp4` into this reel's `media/BXX.mp4` (source clips are already audio-conformed to the same `am_onyx` voice used here). Body mp3s copied from parent `mp3/beat-BXX.mp3`.

## Datable-claim edits

None to narration text. All quantitative claims (PDI < 0.2, zeta > ±30 mV, EE > 70%, release > 80% in 24 h, endotoxin < 0.5 EU/mL, corona shift 15–40 nm) are FDA/USP baselines, not versioned — no dated tool names, model versions, or prices anywhere in the script.

## Dropped fields

- Metadata: `body_beats`, `old_outro_beats` (redundant with beats array); `body_duration_s` (stale).
- Every wrapper beat: legacy `modelLabel: "Fable 5"` / `effortLabel: "High"` from `ClaudeComposerAsk` props (nbb Kokoro reel, not Claude-branded).
- Old empty `BVDT/BHTF/BOUT` scaffolds (empty `narration_text`, placeholder `Key finding one/two/three` verdict lines).
- Source `B00` (NikBearBrownOpen) and source `B09` (NikBearBrownOutro) beat entries — replaced by Liam wrapper bookends per abraxane pattern.

## Reel-level notes

- Persona coherence: Liam narrates the wrapper (`am_onyx` speaking Claude cold-open/verdict/your-turn/outro cards); Bear's body clips carry his own `am_onyx` narration. Same voice engine on both, which is by design for the nbb-wrapper pattern — Liam and Bear read as different personas via card skin (ClaudeComposerAsk vs NikBearBrownTerminalAsk/CodeBlock/FormBCard) rather than voice timbre.
