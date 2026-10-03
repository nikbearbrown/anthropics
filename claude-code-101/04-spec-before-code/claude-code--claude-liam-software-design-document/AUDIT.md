# AUDIT.md — claude-liam-software-design-document

Auditor: filmloop unattended, 2026-08-31
Contract: `skills/make/rebuild/SKILL.md` (LOCKED script + shot list), Phase-1 audit list

## Phase-0

- [x] `beat_sheet.pre-rebuild.json` created byte-exact before any edit
      (`ls -la` shows both files at 18081 bytes, mtime 2026-08-01).

## Phase-1 check list

| # | Check | State | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No `.mp4` in reel dir; only `media/` empty; no stale to delete. |
| 2 | Bookends (B00/BVDT/BHTF/BOUT) | FIXED | B00 was `NikBearBrownOpen` → `ClaudeComposerAsk` (COLD OPEN LAW; palette=claude). BVDT/BHTF/BOUT canonical patterns confirmed. B07 was a duplicate `ClaudeTitleOutro` in body lane → converted to `FormACard` summary so the reel has ONE outro (BOUT). |
| 3 | Spark lines | FIXED | B00 greeting `Sawubona, Liam` (world hello, Liam persona, IN-FOR-BEAR LAW). B02 `Generate the SDD.` (≤4w, compressed from narration). B05 `Add sync, re-run.` (≤4w). YOURTURN/BHTF `Your turn.` (correct). All inner composers now have real spark lines from own narration, not arc-cue "The ask," placeholders. |
| 4 | Verdict (BVDT) | FIXED (authored) | Was 3 template lines ("Key finding one/two/three") and empty narration. Body has 8 beats and ~260 words → AUTHORED four verdict lines from body nouns (Problem Statement / Architecture Principles / User Needs / Component List / Open Questions / Collision Test / add sync → local-only fails), and authored a 58-word verdict narration. No template defaults, no boilerplate. |
| 5b | Chart text | N/A | No Manim charts in this reel. |
| 5c | Your-Turn placeholder (BHTF) | FIXED (authored) | Was the seeded template "Take what you learned from [Write a Five-Artifact...] and apply it to your own work." Replaced with a real exercise: pick your next side project, write the 5-section SDD with explicit Collision Test on each principle, flag the principle most likely to fail if scope grows. Narration authored (~75 words for the 24s window). `output` populated with two real prompt-response teasers. |
| 5 | Card text (FormA/FormB) | FIXED | B01/B04/B06/B08 all had `label == sub` (a duplicate narration line stuffed twice). Rewrote every label to a short category noun (1–4 words) and authored a distinct sub as the compressed narration. B04 promoted from 3-item card to 4-item card to include "Component List" (which the narration names). B06 title tightened from `THE COLLISION TEST FIRES` to `Collision fires`. |
| 6 | Punt sweep (bookends incl.) | FIXED | Old sheet was 5-slates-of-10. Every slate was a FormBCard or a ClaudeComposerAsk that had valid schema — the SLATE status came from the previous pipeline's PIPELINE→fill_slates path. Rebuilt with real filled props everywhere. Zero gen-AI asks, zero unfilled slates, zero DoodleScene, zero STILL src=archive, zero FormA that names a visual it never draws. Every beat is machine-buildable. |
| 7 | Card-only reel | PASS | B03 renders real code via `ClaudeCodeBeat`. Not card-only. |
| 8 | Lens audit (Descartes/Hume/Popper/Plato ≥2) | PASS | See lens audit below — the reel runs Popper (Collision Test as pre-declared failure mode) and Plato (SDD is the artifact; the software system is the world; the SDD holds the two apart before the code exists). |
| 9 | Brand fields | FIXED | `folderLabel` promoted to metadata + set to `@NikBearBrown` (channel handle, not brand key). `engine=kokoro` / `voice=am_onyx` match Liam voice (COLD OPEN says "in for Bear" — narration in B00 hook doesn't explicitly say it, but voice persona is Liam via Kokoro am_onyx, consistent with claude-liam channel). |
| 10 | Pacing (WPS) | ADVISORY | Estimated WPS: B00 18w/8s=2.25 ok; B01 32w/12s=2.67 ok; B02 30w/12s=2.5 ok; B03 35w/14s=2.5 ok; B04 34w/20s=1.7 SLOW (extra breathing space, acceptable for 4-item karaoke reveal); B05 27w/10s=2.7 ok; B06 45w/14s=3.2 ok; B07 34w/12s=2.83 ok; B08 10w/8s=1.25 SLOW (short beat, ok); BVDT 58w/20s=2.9 ok; BHTF 75w/24s=3.1 ok. No hard violations. |
| 11 | `type_check.py` | PASS | GATE T: PASS. 4 §8.10 redundancy advisories on FormBCard/FormACard beats (B01/B04/B07/B08) — advisory only, does not block cut. Redundancy is expected on compressed summary cards; the labels compress the narration into pointer nouns. |

## Lens audit (LENS-NOTES.md)

- **Descartes (falsification checklist):** partial — the Collision Test IS a Cartesian checklist ("what would have to be true for this principle to be wrong under a realistic requirement change"). Named implicitly in B01/B03/B05/B06, not stated as "Descartes" but the move is present.
- **Hume (confidence is a property of the model):** not present. This reel is about pre-writing the design, not about assessing model output confidence. Correct to omit.
- **Popper (falsifiability, pre-declared failure):** PRESENT. B02 asks Claude to "flag any principle that survives no realistic conflict" — a Popperian pre-declared failure spec. B05/B06 execute the test: local-only vs sync is the falsifying instance. Body pattern: "state in advance what would count as failing → go looking for exactly that."
- **Plato (artifact / world / relationship):** PRESENT. The SDD is the ARTIFACT; the software system (once built) is the WORLD; the Principle Collision Test interrogates the RELATIONSHIP before the world exists. B07 restates: "not documentation after the fact — it is the decision itself." The whole reel is the Cave move for pre-code design.

Two moves cleared (Popper + Plato) → LENS PASS.

## Sheet-level state after audit

- Every beat SHOW/HOLD/CARD classified: 13 SHOW, 0 HOLD, 0 CARD, 0 PUNT.
- Every FormBCard has ≥1 icon slot with real label + sub (no duplicates, no placeholders).
- Every ClaudeComposerAsk has a real greeting (spark), real command, real runningText, real folderLabel.
- BVDT: real title + 4 real findings, real narration.
- BHTF: real prompt exercise, real narration, non-empty `output`.
- BOUT: canonical `ClaudeTitleOutro` with correct title + slug.

## Verdict

Ready to build. Proceeding to PHASE 2 (audio + compile + Gate V).
