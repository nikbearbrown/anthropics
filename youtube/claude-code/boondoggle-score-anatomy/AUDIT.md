# AUDIT.md — boondoggle-score-anatomy

Filmloop pass 2026-08-31. Narration LOCKED per rebuild contract; only envelope,
patterns, verdict, sparks touched.

## Phase 0 — rebuild contract

- `beat_sheet.pre-rebuild.json` written (byte-exact of prior sheet).
- Narration on every beat preserved verbatim. No datable-claim edits required —
  no model versions, no prices, no "as of" phrases in body.
- VOICE-LOCK: dropped stale metadata (`build`, `design_version`→v2, redundant
  `voice_kokoro` at metadata level kept). All beats: `engine: kokoro`,
  `voice: am_onyx`, `voice_kokoro: am_onyx`.
- Non-claude channel skins: N/A (this is `claude-liam`).

## Phase 1 checks

1. **Stale renders — PASS.** No `<slug>.mp4` or `<slug>-slate.mp4` on disk. No
   media/ directory. Nothing to delete.

2. **Bookends — FIXED.** Prior sheet had duplicated tail: B04 (VERDICT), B05
   (HANDOFF), B06 (OUTRO) *and* placeholder BVDT/BHTF/BOUT. The body beats
   carry the locked narration and measured mp3s; the placeholders had empty
   narration, no audio, template-default verdict lines, and a bracketed
   `[Take what you learned from …]` in BHTF. Merged: dropped BVDT/BHTF/BOUT,
   promoted B04 to `ClaudeVerdictArtifact` (was `motion: stagger`, no pattern),
   B05 to `ClaudeComposerAsk` with a real 4-word segment, B06 already
   `ClaudeTitleOutro`. Canonical: B00 ClaudeComposerAsk / B04
   ClaudeVerdictArtifact / B05 ClaudeComposerAsk / B06 ClaudeTitleOutro.

3. **Spark lines — FIXED.** B00 `shot.remotion.props.greeting` was the string
   `"Liam"` alone (the top-level greeting `"Sawadee, Liam"` never reached the
   render prop). Set to `"Sawadee, Liam"`. Sawadee (Thai) checked against
   adjacent reels in the batch — not repeated. B05 greeting `"Your turn."`
   already present. All inner ClaudeComposerAsk composers now carry a legit
   greeting; no other inner composer beats exist.

4. **Verdict — AUTHORED.** Prior BVDT was placeholder (`Key finding one/two/
   three`) with empty narration. Body B04 is 76 words, five sentences — meets
   the 180-word / 5-beat AUTHOR threshold when combined with the B01–B03 body.
   Authored four artifactLines from B04's own claims:
   - "The Score is not a capability judgment — it is a prompt for yours."
   - "It forces the who-decides question before any code runs."
   - "Two human-only rows, three Claude-only rows: honest build."
   - "Zero human-only rows: probably not."
   B04 narration unchanged; the verdict card is what the narration was already
   saying, rendered on-frame.

5. **Card text — FIXED.** Prior B01 FormBCard items had prose-fragment labels
   ("The Score table has five", "The who column has three", "Claude-only means
   the step is") and `sub` values equal to full narration clauses — mid-word
   truncation risk plus subs that duplicate the label. Reauthored B01, added
   B02/B03 (they had no `shot.remotion` at all — punt), all with 1–3 word
   category labels and short `sub` lines under 60 chars:
   - B01: Claude-only / Human-only / Claude-with-review (three lanes for the
     who column, one icon each — matches nopunt "short list of named things").
   - B02: Accidental / Essential (Brooks 1986 two-up).
   - B03: Vague handoff / Specific handoff (the Popper test the narration names).
   `sub` lines are all real content from the narration, no "TBD" / "see
   narration" placeholders.

5b. **Chart text — N/A** (routed away from Manim). `scenes_std.py` on disk
   used `Text(narration[:60])` slices as pipeline-box labels — the exact
   enterprise-search failure mode. No longer referenced from any beat; file
   left as-is (not deleted, may resurface if a future pass wants to route
   back to Manim after rewriting the labels).

5c. **Your-Turn placeholder — FIXED.** Prior BHTF carried the template default
   `"Take what you learned from [The Boondoggle Score: Label Who Does Each
   Step] and apply it to your own work."` — bracket placeholder. Dropped
   BHTF; B05 already carries a real exercise: paste the walk-me-through-each-
   column prompt, look for red flags per column and what a >8 total means.

6. **Punt sweep — PASS.** Every remaining beat renders from `shot.remotion.
   pattern`. Zero unfilled `PIPELINE → fill_slates` needs. Zero DoodleScene /
   DoodleChart / gen-AI / STILL archive slots.

7. **Card-only reel — N/A.** B01/B02/B03 are FormBCards (drawn figures with
   iconography), B00/B04/B05 are ClaudeComposerAsk / ClaudeVerdictArtifact
   (drawn UI), B06 is ClaudeTitleOutro. All beats draw something.

8. **Lens audit — PASS.** Two skeptical moves earned:
   - **Popper (state failure in measurable terms):** B03 states the
     falsifiability test as content — "'Claude decides' is not a handoff
     condition; 'Classification threshold verified against baseline dataset'
     is." Vague handoff condition = the failure signal, stated in advance.
   - **Plato (artifact / world / relationship):** B02 and B04 hold the Score
     (artifact) apart from the actual build (world). B02: "When you write
     Claude-only for a step that requires domain judgment, you have handed
     over the essential work and kept the accidental" — the artifact says
     one thing, the world requires another. B04: the Score is a prompt for
     your judgment, not a report on Claude's capability.

9. **Brand fields — PASS.** `folderLabel: @NikBearBrown` (channel handle).
   Engine `kokoro`, voice `am_onyx`, brand `claude-liam`, register `Teardown`
   — all internally consistent. Narration self-identifies "This is Liam, in
   for Bear" / "Liam, in for Bear" — matches Kokoro `am_onyx`.

10. **Pacing — LOG.** Word rate against measured audio:
    - B00: 88 w / 24.30s = 3.6 wps (0.2 over the 3.4 ceiling; measured Kokoro
      output, no retime available — LOGGED)
    - B01: 62 w / 20.89s = 3.0 wps ✓
    - B02: 63 w / 22.78s = 2.8 wps ✓
    - B03: 64 w / 20.46s = 3.1 wps ✓
    - B04: 76 w / 18.60s = 4.1 wps (0.7 over — LOGGED, dense verdict)
    - B05: 46 w / 12.86s = 3.6 wps (0.2 over — LOGGED)
    - B06: 16 w / 6.14s = 2.6 wps ✓
    Two beats over the ceiling; both are bookend density (verdict + your-turn
    with a full paste-me prompt read aloud). No retime — audio is the clock.

11. **type_check.py — PASS.** GATE T: PASS (see TYPECHECK.md). One §8.10
    advisory on B04 (verdict narration overlaps verdict card — intrinsic to
    verdict beats; advisory, does not block).

## Result

All Phase 1 checks resolved or logged. Cut compiled + Gate V passed after one
mid-build fix (B04 pagination overflow, see FILMLOOP-LOG entry).
