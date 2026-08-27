# CC-COWORK-AUDIT — Visual Audit, 22-Reel Simulator Conversion Batch

Generated: 2026-08-10 | Auditor: agent session (fully autonomous per task spec)

## Audit scope

22 reels — 12 Cowork block (`claude-cowork/`) and 10 CC block (`claude-code/`).

**Lane rule (binary, body beats only):**
- **LANE A** — Product-fidelity kit: Cowork* scenes on CW reels; CC* scenes on CC reels. Family tokens only. Chrome strings verbatim product strings. Content fills SAFE area.
- **LANE B** — Real diagram from existing primitives: FlowDiagram, LayerStack, SourceFlow, ChipGrid, PredictCard, Manim fragment, or C2 deck pattern.
- **BOOKEND** — Standard Claude scenes: ClaudeComposerAsk, ClaudeVerdictArtifact, ClaudeComposerAsk ("Your turn."), ClaudeTitleOutro. Exempt from lane rule.
- Anything else = **FAIL**.

**Structural requirements (all reels):**
- Closing block exactly: BVDT (ClaudeVerdictArtifact) → BHTF (ClaudeComposerAsk, greeting "Your turn.") → BOUT (ClaudeTitleOutro)
- No duplicate Your Turn beats
- No dark/inert handoff beats before BHTF
- BVDT `artifactLines` must be real content (not placeholder "Key finding one/two/three")
- At least one LANE B diagram beat per reel

---

## REEL 1 — cowork-access-ladder

Path: `claude-cowork/claude-liam-cowork-access-ladder/`
Kit: Cowork. GATE T: PASS (11 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines: ["Key finding one", "Key finding two", "Key finding three"]` — placeholder shipped |
| YOURTURN | —           | FAIL      | Duplicate Your Turn — `YOURTURN` beat + `BHTF` beat both present; closing block has 4 beats instead of 3 |
| BHTF     | BOOKEND     | FAIL      | Second Your Turn (kept — canonical); dark/inert beat before BHTF needs removal |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Critical: mandatory 4-rung access-ladder diagram (LANE B) required by task spec — not present in current beat sheet.**
**Summary: 4 FAIL — BVDT placeholder, YOURTURN duplicate, B01 mislabeled, mandatory access-ladder diagram missing.**

---

## REEL 2 — claude-for-excel

Path: `claude-cowork/claude-liam-claude-for-excel/`
Kit: Cowork. GATE T: PASS (12 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | ClaudeComposerAsk body variant — acceptable opener |
| B02      | LANE A      | PASS      | CoworkComposer — correct |
| B03      | LANE A      | PASS      | CoworkComposer — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| B07      | LANE A      | PASS      | CoworkComposer — correct |
| B08      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder — "Key finding one/two/three" |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B diagram beat. Every body beat is LANE A (Cowork product kit). Spec requires at least one LANE B per reel.**
**Summary: 2 FAIL — BVDT placeholder, missing LANE B beat.**

---

## REEL 3 — stop-prompting-claude

Path: `claude-cowork/claude-liam-stop-prompting-claude/`
Kit: Cowork. GATE T: PASS (13 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | ClaudeComposerAsk body variant — acceptable |
| B02      | LANE A      | PASS      | CoworkComposer — correct |
| B03      | LANE A      | PASS      | CoworkSideRail — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| B07      | LANE A      | PASS      | CoworkTaskView — correct |
| B08      | LANE A      | PASS      | CoworkComposer — correct |
| B09      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B diagram beat. All body beats are LANE A.**
**Summary: 2 FAIL — BVDT placeholder, missing LANE B beat.**

---

## REEL 4 — seven-field-brief

Path: `claude-cowork/claude-liam-seven-field-brief/`
Kit: Cowork. GATE T: PASS (11 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE B      | PASS      | Manim scene — correct |
| B05      | LANE A      | PASS      | CoworkTaskView — correct |
| B06      | LANE A      | PASS      | CoworkComposer — correct |
| B07      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 2 FAIL — BVDT placeholder, B01 mislabeled BOOKEND.**

---

## REEL 5 — nondelegation-checklist

Path: `claude-cowork/claude-liam-nondelegation-checklist/`
Kit: Cowork. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 2 FAIL — BVDT placeholder, B01 mislabeled BOOKEND.**

---

## REEL 6 — plan-review-checklist

Path: `claude-cowork/claude-liam-plan-review-checklist/`
Kit: Cowork. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | FAIL      | CoworkTaskView used with invalid props `title` and `tasks` — CoworkTaskView schema requires `blocks[]` and `cues[]`; `title`/`tasks` are not valid props; beat likely renders incorrectly |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 3 FAIL — BVDT placeholder, B01 mislabeled BOOKEND, B06 invalid CoworkTaskView props.**

---

## REEL 7 — synthesis-vs-deciding

Path: `claude-cowork/claude-liam-synthesis-vs-deciding/`
Kit: Cowork. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | FAIL      | ClaudeTitleOutro missing `handle` prop — only `title` and `slug` present; mascotSeed derivation may fail or default incorrectly |

**Summary: 3 FAIL — BVDT placeholder, B01 mislabeled BOOKEND, BOUT missing `handle` prop.**

---

## REEL 8 — claude-connectors

Path: `claude-cowork/claude-liam-claude-connectors/`
Kit: Cowork. GATE T: PASS (13 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | ClaudeComposerAsk body — acceptable |
| B02      | LANE A      | PASS      | CoworkTaskView — correct |
| B03      | LANE A      | PASS      | CoworkTaskView — correct |
| B04      | LANE A      | PASS      | CoworkComposer — correct |
| B05      | LANE A      | PASS      | CoworkTaskView — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| B07      | LANE A      | PASS      | CoworkComposer — correct |
| B08      | LANE A      | PASS      | CoworkComposer — correct |
| B09      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B diagram beat. All body beats are LANE A.**
**Summary: 2 FAIL — BVDT placeholder, missing LANE B beat.**

---

## REEL 9 — be-good-at-claude

Path: `claude-cowork/claude-liam-be-good-at-claude/`
Kit: Cowork. GATE T: PASS (13 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | ClaudeComposerAsk body — acceptable |
| B02      | LANE A      | PASS      | CoworkComposer — correct |
| B03      | LANE A      | PASS      | CoworkComposer — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkSettings — correct product fidelity |
| B06      | LANE A      | PASS      | CoworkSettings — correct |
| B07      | LANE A      | PASS      | CoworkTaskView — correct |
| B08      | LANE A      | PASS      | CoworkComposer — correct |
| B09      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B diagram beat. All body beats are LANE A.**
**Summary: 2 FAIL — BVDT placeholder, missing LANE B beat.**

---

## REEL 10 — privacy-classification-scanner

Path: `claude-cowork/claude-liam-privacy-classification-scanner/`
Kit: CC (CLI video — subject is a Claude Code scanning workflow). GATE T: PASS (12 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct (no `lane` set — implicit BOOKEND) |
| B01      | LANE A      | FAIL      | CoworkTaskView on a CC-kit video — wrong product family; should be CCSession |
| B02      | LANE A      | PASS      | CCSession — correct for CC-kit |
| B03      | LANE A      | PASS      | CCSession — correct |
| B04      | LANE A      | FAIL      | CoworkTaskView on CC-kit video — wrong family |
| B05      | LANE A      | PASS      | CCSession — correct |
| B06      | LANE A      | FAIL      | CoworkTaskView on CC-kit video — wrong family |
| B07      | LANE A      | FAIL      | CoworkTaskView on CC-kit video — wrong family |
| B08      | LANE A      | FAIL      | CoworkTaskView on CC-kit video — wrong family |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Mixed kit: 5 body beats use Cowork* scenes on what is clearly a CC/CLI video. No LANE B beat.**
**Summary: 7 FAIL — BVDT placeholder, B01/B04/B06/B07/B08 wrong kit, missing LANE B.**

---

## REEL 11 — cowork-task-packet

Path: `claude-cowork/claude-liam-cowork-task-packet/`
Kit: Cowork. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 2 FAIL — BVDT placeholder, B01 mislabeled BOOKEND.**

---

## REEL 12 — extraction-schema-first

Path: `claude-cowork/claude-liam-extraction-schema-first/`
Kit: Cowork. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CoworkTaskView body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CoworkTaskView — correct |
| B05      | LANE A      | PASS      | CoworkComposer — correct |
| B06      | LANE A      | PASS      | CoworkTaskView — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 2 FAIL — BVDT placeholder, B01 mislabeled BOOKEND.**

---

## REEL 13 — command-development

Path: `claude-code/claude-liam-command-development/`
Kit: CC. GATE T: PASS (7 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct (no lane tag, implicit BOOKEND) |
| B01      | LANE A      | PASS      | CCSession — correct |
| B02      | LANE A      | PASS      | CCPlanCard — correct |
| B05      | LANE A      | PASS      | CCSession teardown — correct |
| BVDT     | BOOKEND     | PASS      | Real content, 5 lines — PASS |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B beat. All body beats LANE A (CC kit). Teardown-format reel — LANE B advisory (not hard failure for teardown format).**
**Summary: 0 FAIL — clean. Advisory: no LANE B diagram beat.**

---

## REEL 14 — hook-development

Path: `claude-code/claude-liam-hook-development/`
Kit: CC. GATE T: PASS (7 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | CCSession — correct |
| B02      | LANE A      | PASS      | CCPlanCard — correct |
| B05      | LANE A      | PASS      | CCSession — correct |
| BVDT     | BOOKEND     | PASS      | Real content, 6 lines — PASS |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 0 FAIL — clean. Advisory: no LANE B diagram beat (teardown format).**

---

## REEL 15 — writer-reviewer-pattern

Path: `claude-code/claude-liam-writer-reviewer-pattern/`
Kit: CC. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CCSession body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE A      | FAIL      | ClaudeComposerAsk used as body handoff — should be a content beat (LANE A or LANE B), not a bookend pattern mid-reel |
| B06      | LANE A      | FAIL      | CCSession used as outro text — closing block should be BVDT→BHTF→BOUT; this outro beat disrupts the standard closing block |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**B05 ClaudeComposerAsk body + B06 CCSession outro both interrupt the standard closing block flow.**
**Summary: 4 FAIL — BVDT placeholder, B01 mislabeled BOOKEND, B05 wrong pattern mid-body, B06 outro disrupts closing block.**

---

## REEL 16 — plan-mode-interruption

Path: `claude-code/claude-liam-plan-mode-interruption/`
Kit: CC. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CCSession body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim scene — correct |
| B03      | LANE B      | PASS      | Manim scene — correct |
| B04      | LANE A      | PASS      | CCPlanCard — correct |
| B05      | LANE A      | FAIL      | ClaudeComposerAsk mid-body — missing `rendered` block inside `shot.remotion`; also wrong pattern for content beat |
| B06      | LANE A      | FAIL      | CCSession used as outro — disrupts closing block |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 4 FAIL — BVDT placeholder, B01 mislabeled, B05 missing `rendered` block, B06 outro disrupts closing block.**

---

## REEL 17 — vox-subagent-context

Path: `claude-code/claude-liam-vox-subagent-context/`
Kit: CC. GATE T: PASS (13 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | CCSession — correct |
| B02      | LANE B      | PASS      | Manim — correct |
| B03      | LANE A      | PASS      | CCSession — correct |
| B04      | LANE B      | PASS      | Manim — correct |
| B05      | LANE B      | PASS      | Manim — correct |
| B06      | LANE B      | PASS      | Manim — correct |
| B07      | LANE A      | PASS      | CCSession — correct |
| B08      | LANE B      | PASS      | Manim — correct |
| B09      | LANE A      | PASS      | CCSession — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 1 FAIL — BVDT placeholder only. Strongest body structure in the batch.**

---

## REEL 18 — slash-context-window-check

Path: `claude-code/claude-liam-slash-context-window-check/`
Kit: CC. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CCSession body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim — correct |
| B03      | LANE B      | PASS      | Manim — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE A      | FAIL      | ClaudeComposerAsk mid-body — missing `rendered` block; wrong pattern for content beat |
| B06      | LANE A      | FAIL      | CCSession used as outro — disrupts closing block |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 4 FAIL — BVDT placeholder, B01 mislabeled, B05 missing `rendered`, B06 outro disrupts closing block.**

---

## REEL 19 — engineering-partner-loop

Path: `claude-code/claude-liam-engineering-partner-loop/`
Kit: CC. GATE T: PASS (12 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct (no lane tag) |
| B01      | LANE A      | PASS      | CCSession — correct |
| B02      | LANE A      | PASS      | CCSession (plan block) — correct |
| B03      | LANE A      | PASS      | CCSession (diff block) — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE A      | PASS      | CCSession — correct |
| B06      | LANE A      | PASS      | CCSession — correct |
| B07      | LANE A      | PASS      | CCSession — correct |
| B08      | LANE A      | PASS      | CCSession — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B beat. All body beats LANE A. Appropriate for a live-session-demo reel but noted.**
**Summary: 1 FAIL — BVDT placeholder. Advisory: no LANE B diagram beat.**

---

## REEL 20 — hook-advisory-vs-deterministic

Path: `claude-code/claude-liam-hook-advisory-vs-deterministic/`
Kit: CC. GATE T: PASS (10 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CCSession body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim — correct |
| B03      | LANE B      | PASS      | Manim — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE A      | FAIL      | ClaudeComposerAsk mid-body — missing `rendered` block; wrong pattern for content beat |
| B06      | LANE A      | FAIL      | CCSession used as outro — disrupts closing block |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**Summary: 4 FAIL — BVDT placeholder, B01 mislabeled, B05 missing `rendered`, B06 outro disrupts closing block.**

---

## REEL 21 — tests-pass-user-fails

Path: `claude-code/claude-liam-tests-pass-user-fails/`
Kit: CC. GATE T: PASS (13 beats).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk — correct |
| B01      | LANE A      | PASS      | CCSession — correct |
| B02      | LANE A      | PASS      | CCSession — correct |
| B03      | LANE A      | PASS      | CCSession — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE A      | PASS      | CCSession — correct |
| B06      | LANE A      | PASS      | CCSession — correct |
| B07      | LANE A      | PASS      | CCSession — correct |
| B08      | LANE A      | PASS      | CCSession — correct |
| B09      | LANE A      | PASS      | CCSession — correct |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder |
| BHTF     | BOOKEND     | PASS      | ClaudeComposerAsk "Your turn." — correct |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct |

**No LANE B beat. All body beats LANE A — appropriate for session-demo reel.**
**Summary: 1 FAIL — BVDT placeholder. Advisory: no LANE B diagram beat.**

---

## REEL 22 — nbb-vox-agentic-loop

Path: `claude-code/nbb-vox-agentic-loop/`
Kit: CC (source body) + NBB wrapper bookends. GATE T: **FAIL** (3 failures: B06, B07, B09).

| beat_id  | lane/bookend | pass/fail | issues |
|----------|-------------|-----------|--------|
| B00      | BOOKEND     | PASS      | ClaudeComposerAsk cold open — correct |
| NBB00    | BOOKEND     | PASS      | ClaudeComposerAsk Liam cold open — correct |
| B01      | LANE A      | FAIL      | Tagged `lane: BOOKEND` but is CCSession body beat — mislabeled |
| B02      | LANE B      | PASS      | Manim — correct |
| B03      | LANE B      | PASS      | Manim — correct |
| B04      | LANE A      | PASS      | CCSession — correct |
| B05      | LANE B      | PASS      | Manim — correct |
| B06      | LANE B      | FAIL      | Manim GATE T FAIL §8.1 — font_size=20px (pipeline labels) and 24px (act label) below 35px floor |
| B07      | LANE B      | FAIL      | Manim GATE T FAIL §8.1 — font_size=18px (node labels) below 35px floor |
| B08      | LANE B      | PASS      | Manim — correct |
| B09      | LANE B      | FAIL      | Manim GATE T FAIL §8.1 — font_size=18px (node labels) below 35px floor |
| B10      | LANE B      | PASS      | Manim — correct |
| B11      | LANE B      | PASS      | Manim — correct |
| B12      | LANE B      | PASS      | Manim — correct |
| NBB01    | BOOKEND     | PASS      | ClaudeVerdictArtifact — real content (3 lines) — PASS |
| NBB02    | BOOKEND     | FAIL      | ClaudeComposerAsk "Your turn." — command references "[cancer type or clinical case]" — topic mismatch, content error |
| NBB03    | BOOKEND     | FAIL      | CCSession used as outro — should be ClaudeTitleOutro; narration text is the title (correct) but pattern is wrong |
| BVDT     | BOOKEND     | FAIL      | `artifactLines` placeholder — "Key finding one/two/three" (NBB01 has real content but BVDT still has placeholder) |
| BHTF     | BOOKEND     | FAIL      | ClaudeComposerAsk "Your turn." — command is generic "[topic] and apply it to your own work" — thin handoff |
| BOUT     | BOOKEND     | PASS      | ClaudeTitleOutro — correct, has `handle` prop |

**Critical: GATE T FAIL (B06/B07/B09 font below floor). NBB02 has wrong domain command (cancer reference — wrong video). NBB03 uses CCSession instead of ClaudeTitleOutro. BVDT still placeholder despite NBB01 having real content.**
**Summary: 7 FAIL — B06/B07/B09 GATE T font floor, B01 mislabeled, NBB02 wrong command, NBB03 wrong pattern, BVDT placeholder.**

---

## Cross-reel summary

| # | Slug | GATE T | BVDT | LANE B | Kit | Duplicate YT | Mislabeled | Other FAIL | Total FAIL |
|---|------|--------|------|--------|-----|-------------|-----------|------------|------------|
| 1  | cowork-access-ladder | PASS | FAIL | YES (B02-B03) | CW | YOURTURN dup | B01 | Mandatory ladder missing | 4 |
| 2  | claude-for-excel | PASS | FAIL | NO | CW | — | — | Missing LANE B | 2 |
| 3  | stop-prompting-claude | PASS | FAIL | NO | CW | — | — | Missing LANE B | 2 |
| 4  | seven-field-brief | PASS | FAIL | YES (B02-B04) | CW | — | B01 | — | 2 |
| 5  | nondelegation-checklist | PASS | FAIL | YES (B02-B03) | CW | — | B01 | — | 2 |
| 6  | plan-review-checklist | PASS | FAIL | YES (B02-B03) | CW | — | B01 | B06 invalid props | 3 |
| 7  | synthesis-vs-deciding | PASS | FAIL | YES (B02-B03) | CW | — | B01 | BOUT missing `handle` | 3 |
| 8  | claude-connectors | PASS | FAIL | NO | CW | — | — | Missing LANE B | 2 |
| 9  | be-good-at-claude | PASS | FAIL | NO | CW | — | — | Missing LANE B | 2 |
| 10 | privacy-classification-scanner | PASS | FAIL | NO | CC | — | — | Mixed kit (5 beats), missing LANE B | 7 |
| 11 | cowork-task-packet | PASS | FAIL | YES (B02-B03) | CW | — | B01 | — | 2 |
| 12 | extraction-schema-first | PASS | FAIL | YES (B02-B03) | CW | — | B01 | — | 2 |
| 13 | command-development | PASS | PASS | NO (advisory) | CC | — | — | — | 0 |
| 14 | hook-development | PASS | PASS | NO (advisory) | CC | — | — | — | 0 |
| 15 | writer-reviewer-pattern | PASS | FAIL | YES (B02-B03) | CC | — | B01 | B05 wrong pattern, B06 outro | 4 |
| 16 | plan-mode-interruption | PASS | FAIL | YES (B02-B03) | CC | — | B01 | B05 missing rendered, B06 outro | 4 |
| 17 | vox-subagent-context | PASS | FAIL | YES (B02,B04-B06,B08) | CC | — | — | — | 1 |
| 18 | slash-context-window-check | PASS | FAIL | YES (B02-B03) | CC | — | B01 | B05 missing rendered, B06 outro | 4 |
| 19 | engineering-partner-loop | PASS | FAIL | NO (advisory) | CC | — | — | — | 1 |
| 20 | hook-advisory-vs-deterministic | PASS | FAIL | YES (B02-B03) | CC | — | B01 | B05 missing rendered, B06 outro | 4 |
| 21 | tests-pass-user-fails | PASS | FAIL | NO (advisory) | CC | — | — | — | 1 |
| 22 | nbb-vox-agentic-loop | FAIL | FAIL | YES | CC | — | B01 | GATE T B06/B07/B09, NBB02 wrong cmd, NBB03 wrong pattern | 7 |

**Universal FAIL: BVDT placeholder across 20/22 reels (command-development and hook-development are the two clean ones).**
**GATE T FAIL: nbb-vox-agentic-loop only (B06/B07/B09 — font_size 16–18px below 35px floor).**

---

## Fix priority order

**P0 — GATE T unblocking (before any other renders):**
1. `nbb-vox-agentic-loop` scenes_std.py: raise all `font_size` values below 35px to 36px minimum; re-render B06/B07/B09; rerun GATE T.

**P1 — BVDT content fill (all 20 placeholder reels):**
Fill `artifactLines` from each reel's narration. No audio change.

**P2 — Structural fixes (beat_sheet.json edits):**
- Remove `YOURTURN` beat from cowork-access-ladder (closing block dedupe)
- Fix `BOUT` missing `handle` in synthesis-vs-deciding
- Fix B06 invalid props in plan-review-checklist (CoworkTaskView: replace `title`+`tasks` with `blocks`+`cues`)
- Fix B05/B06 pattern issues in writer-reviewer-pattern, plan-mode-interruption, slash-context-window-check, hook-advisory-vs-deterministic (B05 is mid-body ClaudeComposerAsk — needs `rendered` block; B06 CCSession outro should be removed or converted to content beat with the outro role absorbed by BOUT)
- Fix NBB02 wrong command in nbb-vox-agentic-loop
- Fix NBB03 CCSession → ClaudeTitleOutro in nbb-vox-agentic-loop
- Fix `lane` labels on mislabeled B01 beats (12 reels)

**P3 — Missing LANE B (reels with no diagram beat):**
- claude-for-excel: add LANE B FlowDiagram or Manim beat (e.g. B01.5 showing Excel→Claude→Result flow)
- stop-prompting-claude: add LANE B (e.g. spec-prompt flow diagram)
- claude-connectors: add LANE B (connector types tier diagram)
- be-good-at-claude: add LANE B (skill progression / capability map)
- privacy-classification-scanner: fix kit first (Cowork→CC), then add LANE B

**P4 — Mandatory access-ladder diagram:**
- cowork-access-ladder: add 4-rung vertical LANE B diagram (Uploaded files → Connector → Browser → Computer use) with terracotta marker on lowest sufficient rung. Add as new beat B04-access or replace B04 if that beat is weak.

**P5 — privacy-classification-scanner kit fix:**
- B01, B04, B06, B07, B08: convert CoworkTaskView → CCSession with appropriate block content.
