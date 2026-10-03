# REBUILD-LOG.md — claude-liam-software-design-document

Date: 2026-08-31  |  Contract: `skills/make/rebuild/SKILL.md`  |  Auditor: filmloop unattended

## Backup

- `beat_sheet.pre-rebuild.json` — byte-exact copy of the pre-rebuild sheet (18,081 B, mtime 2026-08-01).

## Envelope normalization (VOICE-LOCK, dropped fields)

Dropped from `metadata`:
- `_variant_todo` (dead — the reel is post-variant).
- `build` block (`at`, `cut`, `filled`, `of`, `slates`, `skin_warnings`) — stale build receipt from 2026-07-16 that pre-dated the current schema. The warnings it recorded ("B00 palette=claude but the cold open is 'NikBearBrownOpen'") are resolved by this rebuild.

Dropped from every beat: legacy `build` receipts (status/src/filled_by/at/needs). The pipeline writes fresh receipts on compile.

Added / normalized on metadata:
- `folderLabel: "@NikBearBrown"` (channel handle; was scattered across beats only).
- `voice_kokoro: "am_onyx"` (VOICE-LOCK canonical field).
- `ground: "#FAF9F5"` (Claude cream — was `#FFFFFF` which is not the Claude palette).
- `total_estimated_duration_seconds: 155.0` (recalculated from beat sums; was 118).

No ElevenLabs-era fields present in the old sheet to drop.

## Narration edits — LOCKED except where noted

Per rebuild contract, narration is LOCKED. The only permitted changes are datable-claim fixes (none needed here — no model versions, prices, or "as of" language) and the two empty-bookend authoring cases below.

| Beat | Old narration | New narration | Reason |
|---|---|---|---|
| B00 | Three hours of drift because a local-only editor became a multi-user backend. One eleven-minute SDD prevents it. | *(unchanged, verbatim)* | LOCKED |
| B01 | The SDD is the decision that prevents you from making the same decision twice under deadline pressure. The Principle Collision Test is what separates a real principle from a tagline. | *(unchanged)* | LOCKED |
| B02 | We give Claude a v0 sentence and ask it to generate a complete five-section SDD, then run the Principle Collision Test on all three architecture principles. | *(unchanged)* | LOCKED |
| B03 | Claude generates the five sections. The Collision Test flags a conflict between local-only and any future sync requirement. The non-component list explicitly names: no backend, no database, no login. | *(unchanged)* | LOCKED |
| B04 | Five sections: Problem Statement names one user and one done-condition. Architecture Principles survive the Collision Test. User Needs are stopwatch-measurable. Component List names no backend as an explicit non-component. | *(unchanged)* | LOCKED |
| B05 | We add multi-user sync to scope and re-run. Claude flags the immediate conflict with the local-only principle rather than silently resolving it. | *(unchanged)* | LOCKED |
| B06 | The Collision Test fires immediately: local-only versus sync is an irreconcilable conflict at the principle level. Claude flags it and asks for a scope decision rather than inventing a workaround. The SDD caught the drift before the first line of code. | *(unchanged)* | LOCKED |
| YOURTURN | *(long — kept verbatim)* | *(unchanged)* | LOCKED |
| B07 | The SDD is not documentation after the fact — it is the decision itself, made once, in writing, before any code is written. The Collision Test is what keeps principles from being taglines. | *(unchanged)* | LOCKED |
| B08 | Next: score a build plan using the Boondoggle Score. | *(unchanged)* | LOCKED |
| BVDT | *(empty)* | Five sections and one test. Problem Statement, Architecture Principles, User Needs, Component List, Open Questions. The Principle Collision Test flags conflicts between principles before code is written. When scope adds sync, local-only fails the test immediately. The SDD caught the drift before the first keystroke. | Authored (empty→real) — per rebuild contract, closing-block narration is NEW writing derived from the sheet's own body content. Source: B01/B04/B06 nouns. |
| BHTF | *(empty)* | Your turn. Pick your next side project. Before any code, write a five-section SDD: Problem Statement with one user and one done-condition, Architecture Principles each run through the Collision Test, User Needs measured with a stopwatch, a Component List that names its explicit non-components, and the Open Questions you have not answered yet. Then flag the principle that survives the fewest realistic conflicts — that is the one that would have drifted first. | Authored (empty→real) — turns the seeded template BHTF into a real scaffolded exercise (nopunt whole-sheet checklist §"SCAFFOLDED viewer task"). |
| BOUT | *(empty)* | *(unchanged — outro title card, no narration by design)* | LOCKED |

## Shot / form rebuild (SHOT-FORM-SYSTEM derived from locked patterns)

| Beat | Old pattern | New pattern | Reason |
|---|---|---|---|
| B00 | `NikBearBrownOpen` | `ClaudeComposerAsk` | COLD OPEN LAW: palette=claude → cold open must be `ClaudeComposerAsk`. Added greeting `Sawubona, Liam` (world-language rotation; Liam persona per IN-FOR-BEAR LAW), command, output preview (ASK→RESULT begins at cold open), running text. |
| B01 | `FormBCard` (dup label/sub) | `FormBCard` (clean) | Same form; labels de-duplicated (were `label == sub == full narration line`), title tightened from `"THE SDD IS THE"` (truncated all-caps) to `"The SDD"` (Title Case per SPARK-LINE LAW). |
| B02 | `NikBearBrownTerminalAsk` | `ClaudeComposerAsk` | ILLUSTRATE / ASK→RESULT LAW: on the claude palette, ask beats render on the Claude composer, not the legacy dark terminal. Props preserved (command, topic, segment, runningText). Greeting swapped from arc-cue `"The ask,"` (Bear-only per SPARK-LINE LAW) to compressed 3-word spark `"Generate the SDD."` from own narration. Added `folderLabel`, `modelLabel`, `effortLabel` (Claude schema requirements). |
| B03 | `NikBearBrownCodeBlock` | `ClaudeCodeBeat` | Same idea (show real code); Claude skin per COLD OPEN LAW / ILLUSTRATE LAW consistency. Added `sparkLine: "Five sections, one collision."` (≤4 words compressed from narration). Code content preserved verbatim (trimmed for legibility to <15 lines). |
| B04 | `FormBCard` (dup label/sub, 3 items) | `FormBCard` (clean, 4 items) | Same form; labels de-duplicated. Promoted from 3 items to 4 items because narration names FOUR sections (Problem Statement / Architecture Principles / User Needs / Component List). Title tightened from `"FIVE SECTIONS: PROBLEM STATEMENT"` (all-caps, ran two headings together) to `"Five sections"`. |
| B05 | `NikBearBrownTerminalAsk` | `ClaudeComposerAsk` | Same reason as B02. Greeting `"Add sync, re-run."` (3 words, from own narration). |
| B06 | `FormBCard` (dup label/sub, 3 items) | `FormBCard` (clean, 3 items) | Labels de-duplicated. Title tightened from `"THE COLLISION TEST FIRES"` to `"Collision fires"`. |
| YOURTURN | `ClaudeComposerAsk` | *(unchanged)* | Already correct. Preserved. |
| B07 | `ClaudeTitleOutro` | `FormACard` | Old sheet had TWO `ClaudeTitleOutro` beats (B07 body-lane, BOUT bookend-lane) — a duplicate outro. Since narration is a SUMMARY (not a title restate), the beat is now a `FormACard` (serif summary lines). BOUT stays as the single canonical outro. |
| B08 | `FormBCard` (dup label/sub) | `FormBCard` (clean) | Labels de-duplicated; title from `"NEXT: SCORE A BUILD"` to `"Next"`. |
| BVDT | `ClaudeVerdictArtifact` (placeholder lines) | `ClaudeVerdictArtifact` (real content) | Same pattern; artifactLines authored from body content. artifactTitle tightened to `"Software Design Document"`. |
| BHTF | `ClaudeComposerAsk` (template command, empty output) | `ClaudeComposerAsk` (real command, real output) | Same pattern; command authored as a scaffolded exercise; output populated. Added `modelLabel`, `effortLabel`. |
| BOUT | `ClaudeTitleOutro` | *(unchanged)* | Canonical. Title updated to match metadata (`Five-Section`, not `Five-Artifact`). |

## Title consistency fix

Old metadata said `"Write a Five-Artifact Software Design Document"` but every body beat says `"five-section SDD"` and there is no artifact list — there are five *sections*. Corrected the title everywhere (metadata, BOUT prop) to `"Write a Five-Section Software Design Document with Claude Code"` for internal consistency. YOURTURN's own narration says "five-artifact structure" — LEFT VERBATIM per LOCKED rule (that language is Bear's from the original sheet, and the exercise deliberately probes both framings).

## Template misses

None. Every derived `shot.form` maps to a shipped Remotion component (`ClaudeComposerAsk`, `ClaudeCodeBeat`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`, `FormACard`, `FormBCard`). No `TEMPLATE-MISSES.md` row required.

## Gates run

- GATE T (type_check.py): **PASS** — 0 FAILs, 4 §8.10 advisory-only redundancy notes on summary cards (expected on compressed-noun summaries; not a blocker).
- verdict_audit hand-check: **PASS** — 4 non-placeholder lines, real narration.
- Punt sweep: **PASS** — 13/13 beats machine-buildable, 0 slates.
- Lens audit: **PASS** — Popper and Plato both cleanly present (see AUDIT.md).

## Next step

Audio (Kokoro `am_onyx`), fill-in, compile slate cut, Gate V (frame QC), append FILMLOOP-LOG.md entry.
