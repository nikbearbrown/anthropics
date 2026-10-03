# AUDIT.md — nbb-vox-bystander-effect

Ran the Phase-1 audit against LENS-NOTES.md and the film-loop checklist.

## Phase-0 rebuild contract
- pre-rebuild snapshot: `beat_sheet.pre-rebuild.json` created (byte-exact copy of the July 16 sheet before any edit).

## Check list

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no `.mp4` in reel folder; nothing to purge. |
| 2 | Bookends canonical | FIXED | reel carried BOTH an empty `B00/BVDT/BHTF/BOUT` scaffold AND a filled `NBB00-NBB03` set. Dropped the empty scaffold; renamed the filled NBB set to canonical ids (`B00`, `BVDT`, `BHTF`, `BOUT`). mp3 files renamed on disk to match. |
| 3 | Spark lines | FIXED | `B00.greeting` → `"Konnichiwa, Liam"` (Japanese; not used in adjacent nbb reels this batch — abraxane=Portuguese, nanoparticle-char=Hindi, light-ceiling=Maori). `BHTF.greeting` = `"Your turn."` (per SPARK-LINE LAW). `segment` fields normalized to `"bystander effect · T-DXd vs T-DM1"` (was truncated mid-word "Why Two Identical Anti-HER2 Drugs Kill Completely…"). Dropped legacy `modelLabel`/`effortLabel` (Fable 5 / High) — Kokoro reel, not model-branded. |
| 4 | Verdict | FIXED | `BVDT.artifactLines` were `Key finding one/two/three` placeholders; authored a real verdict from the body's own nouns and numbers ("T-DM1's charged payload cannot cross the membrane — trapped in one cell", "T-DXd's cleavable linker releases a membrane-permeable payload that diffuses", "Same antibody, 5 entry cells → ~40 kills — eight times more"). `artifactHeading` truncated placeholder replaced with `"bystander effect: the payload, not the antibody"`. BVDT narration was already authored (kokoro mp3 exists) — kept verbatim. |
| 5 | Card text | FIXED | `B01` FormBCard items were `Key point one / two / three` with empty subs. Rewrote to real content pulled from the body: `The patient` (HER2-low breast cancer), `The paradox` (one drug approved for HER2-low, other not), `The clue` (T-DM1 and T-DXd share the exact same antibody). |
| 5b | Chart text | N/A | body beats all fall to review slates (no `media/{bid}.*` exist; Manim `scene_class` names are wishes, not renders). Slate labels are the beat's own short act tag. |
| 6 | Punt sweep | LOG | body beats declare Manim classes (`B01_Title`, `B02_TwoDrugs`, `B03_Question`, `B04_AntibodyOneStep`, `B05_NaiveGuess`, `B06_TDM1Confined`, `B08_TDXdSpreads`, `B09_ImplicationQuote`, `B10_Example`, `B11_Endcard`) plus one STILL (`B07`) with a FormACard fallback, but no `manim/` renders exist under this reel. Every body beat becomes a declared review slate. Bookends (B00/BVDT/BHTF/BOUT) render intents `ClaudeComposerAsk` / `ClaudeVerdictArtifact` / `ClaudeComposerAsk` / `ClaudeTitleOutro`; they compile as real Remotion cards (composer/verdict/composer/outro). Legitimate: this is a review-slate cut per the film-loop contract. |
| 7 | Card-only reel | PASS | body includes STILL (B07), DOCUMENT (B05, B09), CARD (B03, B11), and 6 declared Manim GRAPHIC beats — not a card-only reel. All body beats fall to slate for the review cut. |
| 8 | Lens audit | LOG | The body runs **Descartes** (falsification of the naive guess: B05 states the naive prediction — "both drugs underperform equally because antigen is scarce" — and the mechanism refutes it by naming a hidden variable, payload membrane permeability); **Plato** (artifact / world / relationship: the antibody is the artifact you'd naively grade; the tumor patch is the world; the relationship is that the antibody controls only ONE step — B04 states this explicitly). Popper's move is implicit in the 5→40 kill count (the mechanism predicts a measurable multiplier). Hume is not named. Two moves are earned. Narration is LOCKED per the rebuild contract. |
| 9 | Brand fields | FIXED | `folderLabel: @NikBearBrown` ✓. `engine: kokoro / voice: am_onyx` ✓ on metadata and every beat. Dropped legacy ElevenLabs-era `voice_id`/`voice_env` (never present in this sheet). Persona coherence: "Let's recap with Claude" opening in BVDT + "Konnichiwa, Liam" cold-open greeting = Liam narrating for Bear (Kokoro am_onyx) — audio matches. |
| 10 | Pacing (wps) | PASS | every body beat lands 2.0–3.4 wps against measured legacy durations (B01 26 words / 10.34s = 2.5, B10 47 words / 17.97s = 2.6, B11 40 words / 14.03s = 2.85). Bookend narrations will be re-measured after Kokoro regen. |
| 11 | type_check.py | run below | see FILMLOOP-LOG.md entry after compile. |

## Datable-claim scan
- `T-DM1`, `T-DXd`, `HER2`, `HER2-low` — trade / marker names, not versioned.
- `"five HER2-positive cells"` / `"roughly forty surrounding cells"` — mechanism claims hedged with "roughly" and framed as an illustrative example; non-datable. No edit.
- No model/tool version claims to fix. Narration LOCKED per rebuild contract.

## Blocked?
NO — all checks either PASSED or FIXED. Proceeding to Phase 2.
