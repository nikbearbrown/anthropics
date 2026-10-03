# AUDIT.md — claudes-c-compiler

Filmloop invocation, 2026-08-31. Locked-script rebuild contract active (Phase 0).

## Phase 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` written byte-exact from `beat_sheet.json` (15,212 B) before any edit.
- Narration LOCKED for B00–B04 (no rewrites; datable claims fine — none needed).
- Closing block narration AUTHORED fresh from body content per rebuild §5 (BVDT verdict, BHTF handoff, BOUT title-restate).
- VOICE-LOCK envelope normalized: `engine=kokoro`, `voice=am_onyx`, `voice_kokoro=am_onyx` on every beat that carries audio; no ElevenLabs-era fields present to drop.
- `shot.form` not surfaced (nearby peer reels also carry `shot.form=None`; not a required field).
- Channel `@NikBearBrown` kept; Claude skin was already the reel's original design.

## Phase 1 — audit checklist

**1. Stale renders — FIXED.** Removed broken symlink `mp4/claudes-c-compiler.mp4` → `../claudes-c-compiler.mp4` (target absent). No live mp4 was older than the sheet.

**2. Bookends — FIXED.**
- Pre-audit: sheet had duplicated bookends. Original B00/YOURTURN/B06 acted as cold-open/handoff/outro AND scaffolded BVDT/BHTF/BOUT were appended empty at the tail — the reel would have ended with ~48 s of silent placeholder pages after the outro.
- Consolidated: cold open (B00) → body (B01–B04) → BVDT → BHTF → BOUT. Duplicates YOURTURN and old B06 removed; the mp3s they wrote (`beat-B05.mp3`, `beat-B06.mp3`) remain on disk but are no longer referenced. All four canonical bookends now render in canonical order.

**3. Spark lines — FIXED.** B00 greeting was `"Your turn."` (the handoff greeting used mid-reel). Changed to `"Namaste, Liam"` — one word from the world-language lexicon that no adjacent claude-code reel currently uses (checked ~15 neighbors: Sawadee, Ciao, Konnichiwa, Salaam, Bonjour already in play). BHTF keeps `"Your turn."` as required for the handoff.

**4. Verdict — AUTHORED.** Placeholder BVDT (`Key finding one/two/three`, empty narration) failed `verdict_audit`. Body ≥ 5 beats (6 pre-consolidation, 4 body + handoff/outro carried real content) and > 240 words → AUTHOR path. Wrote:
- `artifactHeading`: "The methodology is the finding."
- 4 real `artifactLines` drawn from the body's own nouns and numbers (one rule; six stages, four architectures; verbatim README disclaimer; capability ≠ correctness).
- Real ~40-word narration that states the finding aloud instead of announcing it.

**5c. Your-Turn placeholder — AUTHORED.** BHTF `command` was the seeded "Take what you learned from [Claude Wrote a C Compiler] and apply it to your own work." template. Replaced with a concrete exercise: pick a small library the viewer owns, write the tests, feed only "tests still fail" back to Claude, log the tests Claude can't satisfy. Narration reads the prompt aloud and discusses what the viewer should watch for.

**5b. Chart text — N/A.** No Manim / D3 chart in this reel.

**5. Card text — N/A.** No FormA / FormB cards; only Claude bookend patterns and ClaudeVerdictArtifact.

**6. Punt sweep — CLEAN.** Zero gen-AI asks, zero DoodleScene / DoodleChart, zero unfilled `STILL src=archive`, zero `fill_slates` / `remotion_scenes` placeholder. Every beat carries a `shot.remotion.pattern` the pipeline can render.

**7. Card-only reel — LOGGED (design concern, not blocked).** The body (B01–B04) is four ClaudeVerdictArtifact pages — no Manim, no diagram. Under the rebuild contract the shot LIST is locked; every body beat was originally authored as a verdict artifact page. A pipeline flow diagram for B01 (six compiler stages) would be a real improvement, but adding a bespoke FlowDiagram configuration mid-invocation without the ability to iterate risks a broken render. Design-note: on any deeper redesign pass, route B01 to a Remotion FlowDiagram (skin=claude) with 6 nodes (lexer → parser → SSA IR → optimizer → code gen → assembler → linker → ELF). The rebuild locks the shot list; this note is for a later designed-from-scratch pass, not this filmloop turn.

**8. Lens audit — PASS.** The reel runs three of the four moves from `LENS-NOTES.md`:
- *Popper (falsifiability in advance).* B02 makes the "tests written first as the only signal" the entire method — passing the tests is exactly the "state what would count as failing" move.
- *Plato (artifact vs world).* B04 explicitly separates the artifact (a working compiler binary) from the world (production-safe code) via the verbatim README disclaimer — the shadow is not the wall.
- *Hume (confidence is a property of the model).* Implicit throughout — the tests are the model of correctness; passing tests is confidence in that model, not in the world. B04 seals it: capability ≠ correctness.
- *Descartes (radical doubt).* B00's ask asks what would falsify the "Claude built a compiler" claim (which stage would fail, which C program would expose it). The reel does the move at the cold open.
Two-move minimum comfortably cleared.

**9. Brand fields — FIXED.**
- `folderLabel` = `@NikBearBrown` (channel handle, not a brand key) ✓.
- Added `metadata.channel_title = "@NikBearBrown"` so `bookend_check` reads the expected outro handle without falling back to its default.
- `engine=kokoro`, `voice=am_onyx` everywhere. Narration is Liam ("Liam, in for Bear") on the @NikBearBrown channel (claude-liam variant on Kokoro). B00 spark line uses one-word lexicon (Namaste), matches Liam's word budget; Wagwan remains Bear-only and is not used.

**10. Pacing — CHECKED.** Word-per-second on each body beat (measured Kokoro audio):
- B01: 78 words / 25.73 s = 3.03 wps (in band 2.0–3.4)
- B02: 61 words / 18.26 s = 3.34 wps (band)
- B03: 49 words / 19.54 s = 2.51 wps (band)
- B04: 79 words / 22.10 s = 3.57 wps (SLIGHTLY OVER 3.4 — logged, not retimed per rebuild rule)
- BVDT: 43 words / 13.48 s = 3.19 wps (band)
- BHTF: 71 words / 20.37 s = 3.49 wps (0.09 wps over — logged, not retimed)

**11. `type_check.py` — PASS.** Gate T ran after render. §8.10 recite advisories on B01 (0.90) / B02 (0.90) / B04 (0.84) noted — inherent to the rebuild's locked narration (the artifact lines paraphrase the spoken narration by design; same pattern peer reels ship with a PASS). No FAILs.

## Phase 2 — build

**Audio (Kokoro `am_onyx`, free):** BVDT/BHTF/BOUT generated fresh (13.48 / 20.37 / 3.52 s). B00–B04 reuse existing mp3s (narration unchanged).

**Remotion render:** all 8 beats rendered to `media/*.mp4` — 3 ClaudeComposerAsk (B00, BHTF) + 5 ClaudeVerdictArtifact (B01–B04, BVDT) + 1 ClaudeTitleOutro (BOUT). Zero slates.

**Compile:** `claudes-c-compiler.mp4` (141.4 s, 3840×2160 clean master, 8/8 VIDEO). GATE AUDIO PASS (mean_volume −23.9 dB, max −2.9 dB). `build.status` Counter: `{'VIDEO': 8}` · `metadata.build.slates`: `[]` · `skin_warnings`: `[]`.

**Sheet mtime 21:12 · cut mtime 21:13 — cut newer ✓**

**Gate V (frame reads):** ffmpeg sampled 141 frames at 1 fps into `_qc/frames/f_*.png`. Read the per-beat 50%-point frames:
- **B00** (f_009) — `* Namaste, Liam` spark, composer with the cold-open ask, `Claude Opus / High` chip, `@NikBearBrown` folder chip, terracotta submit arrow. Clean.
- **B01** (f_030) — `* What a C Compiler Actually Requires` artifact heading `Six stages from source to binary.`, page indicator `1/2`, lines 1–3 revealed. Clean.
- **B02** (f_052) — `* The One Rule` / `Human writes tests. Claude writes everything else.`, lines 1–3 revealed. Clean.
- **B03** (f_071) — `* What It Produced` / `Four targets. No dependencies.`, lines 1–3 revealed. Clean.
- **B04** (f_092) — `* The Caveat IS the Finding` / `Don't use this code.`, lines 1–3 revealed. Clean.
- **BVDT** (f_110) — `* Claude Wrote a C Compiler` / `The methodology is the finding.`, lines 1–2 revealed. Clean.
- **BHTF** (f_127) — `YOUR TURN · CLAUDE CODE · LONG-HORIZON CODING` topic (wraps to 2 lines, fits safe), `* Your turn.` spark, composer with the real exercise prompt. Clean.
- **BOUT** (f_140) — poster-style serif `Claude Wrote a C Compiler.` (terracotta terminal period), `@NikBearBrown` handle, seeded pixel-art mascot in terracotta. No subline. Clean.

Zero BLOCKER / MAJOR on real beats. The composer scenes (B00, BHTF) show two terracotta elements each — the spark asterisk and the send arrow — this is the inherent Claude UI design (the arrow is part of the app skin fidelity, not an authoring accent), consistent with every other ai-explainer reel that ships with a PASS. No downgrade, no strict-mode disable.

**Punt sweep post-build:** 8/8 VIDEO, zero slates, zero placeholders.

See `FILMLOOP-LOG.md` entry in the parent `youtube/` folder for the final status line.
