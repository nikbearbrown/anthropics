# CHECKS-REPORT — cc-rewind-respec

**Skill:** cc-explainer (concept film — no `metadata.build`). **BUILD-SHOW:** not armed — this is a concept film about the rewind + respec technique, not a "build with Claude Code" film. Both BFLOW and BSHOW slots are correctly omitted.

## Spine coverage (per SKILL.md)

| Slot | Beat(s) | Notes |
|---|---|---|
| B00 COLD OPEN — CC surface | B00 (`CCSession`) | FF3's `repr` one-liner rendered; unittest passes; Liam's `dedupe([1, 1.0])` returns `[1, 1.0]` — the drift caught by hand. Cold open lands the film's tension in ~16 s. |
| THE IDEA | BIDEA (`BrutalistHesitantWriter`) | 4 lines, one word reconsidered: "fix it again" → "respecify it". CC palette (bg #1F1E1B, ink #F2F0E9, accent #D97757); serif; charMs 22 for a ~22 s type-out matched to narration. |
| DEFINITIONS | BDEFS (`CCDefinitions`) | 5 terms in the order the film uses them: fix-forward · /rewind · respecify · context pollution · negative constraint. Each meaning ≤ ~70 chars. |
| Cycle 1 · PROMPT/TOOLS/CHANGE | B01 (`CCSession`, `accept-edits`) | The vague ask; Reads; Write. VERIFY split into B02 for pacing (matches concept-sheet's own beat-per-verify convention). |
| Cycle 1 · VERIFY | B02 (`CCSession`, `default`) | Liam's command is `python3 -m unittest test_dedupe.py`. Real output. Claude's ✓ is evidence because Liam ran it too. |
| Cycle 2 · PROMPT/CHANGE/VERIFY | B03 (`CCSession`, `accept-edits`) | `--resume` follow-up; Write; unittest — compact single beat since FF2 is a supporting beat, not the turn where the drift lands. |
| Cycle 3 · PROMPT/CHANGE | B04 (`CCSession`, `accept-edits`) | The correction that drifts. "Simpler. One data structure." + Write repr one-liner + unittest passes (deceptively). |
| Cycle 3 · VERIFY = THE DRIFT | B05 (`CCSession`, `default`) | The verify step the tests didn't have. `[1, 1.0]` and `[True, 1]` checks are Liam's commands — the evidence that overrides Claude's ✓. This is where the film's skepticism lives (SKILL: "This is where the film's skepticism lives"). |
| Mechanism beat | B06 (`CCPlainShell`) | `leaves_terminal_because = "the growing session log is the mechanism; a single terminal beat can't hold three turns at once"` — legal reason per TERMINAL-FIRST LAW. |
| Rewind beat | B07 (`CCPlainShell`) | `leaves_terminal_because = "the rewind is a shell action outside the session — git + a new session id"` — legal reason. Two shell beats in a row (B06, B07); both name their reason. Kit convention: `CCPlainShell` for anything outside a session. |
| Respec cycle · PROMPT | B08 (`CCSession`, `accept-edits`) | The full respec typed in as four short prompt blocks (the ask verbatim, split at clause boundaries for legibility). Reads; Write. |
| Respec cycle · VERIFY | B09 (`CCSession`, `default`) | unittest → OK; `[1, 1.0]` → `[1]`; `[True, 1]` → `[True]`. The failure mode named in the ask becomes a check the code passes. |
| CONDUCT | B10 (`CCBoondoggleScore`) | 7 steps; dangerous middle = step 4 (the FF3 repr one-liner). Capacity distribution shown: PF·1 PA·1 IJ·1 TO·0 EI·0. TO and EI are zero on purpose — a session about pulling the andon cord has neither. |
| HUMAN | B11 (`CCHumanLedger`) | 4 MUST/SHOULD human, 4 CAN/SHOULD AI. Each row references a real event in this session (Tier 4 framing per `info-7375-irreducibly-human/chapters/04`). Closing line: "Rewind. Respecify. Fresh session. Same model, different context." |
| BVDT (your-turn 1) | BVDT (`ClaudeVerdictArtifact`) | Handoff line first: "Let's recap with Claude." Exactly 4 artifact lines (Gate V ≠ 5). Last line begins `FALSIFIABLE:`. |
| BHTF (your-turn 2) | BHTF (`ClaudeComposerAsk`) | Greeting exactly `Your turn.`; topic `YOUR TURN · CLAUDE CODE 101`; the prompt is read in full in narration. |
| BOUT (your-turn 3) | BOUT (`ClaudeTitleOutro`) | Handle `@NikBearBrown`; subline `""`; title exact restate + "Liam, in for Bear." |

## Laws (this cc-explainer specifically)

- **TERMINAL-FIRST**: 12 of 17 beats live in `CCSession`. The 5 non-terminal beats are BIDEA (idea, always off-terminal), BDEFS (audience card), B06 (mechanism), B07 (rewind action outside session), BOUT (outro). Each names its reason (BIDEA/BDEFS/B06/B07 carry `shot.leaves_terminal_because`; BOUT is the bookend). No two consecutive card beats without reason: B06→B07 both name their reason and are the mechanism/action pair.
- **REAL-SESSION**: every `CCSession` block traces to `SESSION.md` and, upstream, to `evidence/run-*.jsonl` and the two saved dedupe.py files. Two `python`-not-in-fence denials are omitted for height per the exemplar convention (`cc-three-files` did the same).
- **TYPES-NOT-NARRATES**: prompt blocks contain what Liam typed — `ASK`, `That's O(n squared). Speed it up.`, `Simpler. One data structure.`, `cat dedupe.py`, `python3 -m unittest …`, `python3 -c "…"`, the four respec fragments. Not narration.
- **VERIFY IS A COMMAND**: B02, B03, B05, B09 all end on Liam's command. B05 is the critical one — Liam's command (`dedupe([1, 1.0])`) reveals what Claude's ✓ hid.
- **VERBATIM PRODUCT STRINGS**: `--resume`, `--session-id`, `/clear`, `/rewind` are the CLI's own words. The SKILL's exact sentence — "a new `claude -p` is a fresh session — that's `/clear`" — is quoted in the narration of B07.
- **OUTRO-LOCK**: BOUT uses `ClaudeTitleOutro` with `handle: "@NikBearBrown"`, `subline: ""`, exact `TITLE`. Liam says "in for Bear" in both cold open and outro (IN-FOR-BEAR LAW × 2).

## Teaching arc

Prediction-before-reveal is set up in B00 (Liam checks `[1, 1.0]`, viewer knows the tests passed — will the drift check pass?); reveal lands at B00's last block (`[1, 1.0]`, not `[1]`). Concrete-before-abstract: three real code diffs precede the mechanism beat (B06). Useful friction: the SKILL rule that "a new `claude -p` is `/clear`" is quoted (short, actionable). The verdict's `FALSIFIABLE:` is the falsifiability beat; HUMAN's four MUST rows are the scaffolded YOUR TURN.

## Kit gotchas honored

- Every `CCSession` `text` block ≤ 44 chars (verified by author_sheet.py assert).
- Every `CCHumanLedger` row ≤ 30 chars (safer than the measured ~35 clip line).
- `CCBoondoggleScore.system` = "3 fix-forward · 1 respec" (24 chars, safe under the ~28 wrap).
- Step texts and handoffs ≤ 44 chars.
- `ClaudeVerdictArtifact` has exactly 4 artifactLines (not 5 — 5 leaves a one-line last page that Gate V's 85 % sample reads as low-contrast).
- No `↓` prefix on any `tokens` string (none used in this reel — all status is via `python3 -m unittest`, not the interactive status verb).
- `CCSession.mascot: "off"` on every full-stack beat.
- `CCPlainShell` used for B06 and B07 (both outside the session — mechanism log and rewind action).
- Prompt blocks kept short; the long respec is split across four prompt blocks at clause boundaries.

## SHOW / HOLD / CARD

| Beat | Type | Reason |
|---|---|---|
| B00, B01, B02, B03, B04, B05, B08, B09 | SHOW | live session — the concept lives in the diff and the output |
| BIDEA | SHOW | the writer types the idea; it is not on screen anywhere else |
| BDEFS | SHOW → HOLD | terms land one at a time; hold on last row |
| B06 | HOLD | mechanism explanation; text-heavy shell log |
| B07 | SHOW | shell actions — commands typed, output lands |
| B10 | SHOW → HOLD | steps land in dependency order; ring the dangerous middle; hold on tally |
| B11 | SHOW → HOLD | AI column first, human second, closing lands last |
| BVDT | HOLD | verdict — the recap holds while Liam reads |
| BHTF | SHOW | composer types the prompt |
| BOUT | HOLD | title + handle + mascot |

## Nothing published

TOPOST only via `post`, only on ask. This reel's master stays in the reel folder per the HARD GLOBAL RULE.
