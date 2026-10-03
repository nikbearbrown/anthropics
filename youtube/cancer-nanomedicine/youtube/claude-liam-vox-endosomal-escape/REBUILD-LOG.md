# REBUILD-LOG — claude-liam-vox-endosomal-escape

Rebuilt 2026-08-27 under the locked-script rebuild contract (skills/make/rebuild/SKILL.md).

## Locked (unchanged)
- Every beat's narration_text (no datable-claim rewrites needed — no model names, versions, or prices).
- Beat order, act labels, shot INTENT per beat.
- Title, slug, topic, source, register, palette, channel.

## Envelope changes (VOICE-LOCK)
- DROPPED `metadata.voice_id` (ElevenLabs-era, dead field).
- REWROTE `metadata.clock` from ElevenLabs-era "…until GATE 0 audio lock" prose → "narration (Kokoro am_onyx, VOICE-LOCK); durations are measured after audio generation".
- DROPPED `metadata._variant_todo` — a legacy pre-rebuild TODO list; every item is already applied (Teardown register, Claude outro, kokoro voice).

## Authored spark line (B00) — SPARK-LINE LAW
- OLD: `props.greeting = "Liam"` (lone name, no world-language hello).
- NEW: `props.greeting = "Namaste, Liam."` — rotates against adjacent reels in this run (Salaam/Ciao/Konnichiwa already used by doxil-heart/emitter-range/epr-gap).

## Authored FormBCard items (B01) — no placeholder subs
- OLD items: "Key point one/two/three" with empty subs (template scaffolding).
- NEW items compressed from B01's own narration (siRNA works in a dish, fails in a mouse):
  - "Worked in a dish" / "90% silencing"
  - "Failed in a mouse" / "tumors kept growing"
  - "The paradox to solve" / "why?"

## Authored verdict (BVDT) — VERDICT-AUDIT
- OLD artifactLines: "Key finding one/two/three" (template placeholder). Narration empty.
- NEW artifactLines, authored from body's own nouns/numbers (11-beat body, ~500 words):
  - "Endosomal escape is the rate-limiting step — only 1–2% of cargo reaches the cytosol."
  - "The ionizable lipid's amine is neutral at blood pH 7.4, cationic at endosomal pH 5.5."
  - "That charge flip tears the endosomal bilayer and dumps the RNA into the cytosol."
  - "Same cargo, no switch: ~8% silencing. With switch: ~84%."
- NEW narration for BVDT (was empty): spoken restatement of the four artifact lines.
- estimated_duration_s bumped 20 → 22 to fit the narration.

## Bookend pattern audit
| Beat | Pattern | Verdict |
|------|---------|---------|
| B00  | ClaudeComposerAsk | present, greeting authored |
| BVDT | ClaudeVerdictArtifact | present, verdict authored |
| BHTF | ClaudeComposerAsk | present, greeting "Your turn." |
| BOUT | ClaudeTitleOutro | present |

## Punt sweep
- No `shot.type` set to a gen-AI ask; no DoodleScene/DoodleChart; no `STILL src=archive` for a concept.
- Legacy `build.needs` strings ("YOU → gen-AI clip → pantry") are stale build stamps from an earlier pipeline pass; they will be re-stamped by compile.py on this rebuild.
- The 6 Manim body beats (B04–B09) are declared SLATE for the review cut per PHASE-2 policy (heavy/uncertain slotted as honest slates); their real render is a later human-flagged pass.

## Lens audit
- **Plato** (artifact vs world) — earned by B01/B02: the DISH is the artifact, the MOUSE is the world; the RESULT reveal ("it never reached the cytosol") is the artifact-world discrepancy diagnosis.
- **Popper** (falsifiability) — earned by B09: swap experiment (LNP-A vs LNP-B, same cargo, only variable is the ionizable lipid) is a direct Popperian test — the ionizable-lipid-doesn't-matter null is falsified at 84% vs 8%.
- Two moves present; audit passes.

## Persona coherence
- Narration says "This is Liam, in for Bear" — voice is Kokoro `am_onyx` (Liam). Coherent.
- `folderLabel = @NikBearBrown` (channel handle). Correct.

## Pacing note (LOG only, per PHASE 1 §10)
- B01: 35 words / 9.26s ≈ 3.78 wps — above the 3.4 upper bound. Fast opener, ships as-is (audio already generated; retiming disallowed).
- B04: 48 words / 13.25s ≈ 3.62 wps — above upper bound. Fast, ships as-is.
- All other beats within 2.0–3.4 wps.
