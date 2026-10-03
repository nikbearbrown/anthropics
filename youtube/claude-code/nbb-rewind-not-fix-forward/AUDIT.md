# AUDIT — nbb-rewind-not-fix-forward

Run: 2026-08-31 (filmloop nopunt invocation)
Source of truth: `beat_sheet.pre-rebuild.json` (byte-exact copy of `beat_sheet.json` before edits).

## Structural context
This reel is an audience-preset variant of `../rewind-not-fix-forward` (which is
itself a Liam/kokoro NikBearBrown reel, freshly rebuilt at 2026-08-31 16:51). The
target's beat_sheet.json wrapped the source's body (B00–B05) with a Liam bookend
set (NBB00/NBB01/NBB02/NBB03) AND retained the legacy canonical bookends
(BVDT/BHTF/BOUT) as empty template stubs. The two closing sets are structurally
redundant.

## Check-by-check

**1. Stale renders — PASS.** No mp4 in reel folder; nothing to purge.

**2. Bookends — FIXED.** Reel had both NBB* (opener + verdict + your-turn + outro)
and BVDT/BHTF/BOUT canonical set. Per amendment ("BVDT may be legitimately ABSENT
if a previous pass stripped a placeholder verdict — absent is legal,
present-and-empty is not"), stripped the empty-narration BVDT/BHTF/BOUT since
NBB01/NBB02/NBB03 already fill their roles with real authored content. Kept
NBB00 (ClaudeComposerAsk cold open), NBB01 (ClaudeVerdictArtifact), NBB02
(ClaudeComposerAsk your-turn), NBB03 (ClaudeTitleOutro).

**3. Spark lines — FIXED.**
- NBB00 `props.greeting`: `"Your turn."` (bookend-close spark on a cold open — wrong)
  → `"Guten Tag, Liam"` (German; source used Zdravo/Croatian, avoid repeat).
- B00 `props.greeting`: `"Liam"` (bare — no world-hello) → `"Bonjour, Liam"` (French).
  B00's inner `remotion.props.greeting` was already "Zdravo, Liam"; unified.
- Body beats B01–B05 do not use ClaudeComposerAsk (FormBCard / manim / stagger / handoff),
  so the 4-word inner-composer spark rule does not apply.

**4. Verdict — FIXED.**
- NBB01 verdict body is 79+ words of authored, video-specific content
  (mutation bug, spec gap, andon-cord, respecify). Kept.
- NBB01 `artifactLines[1]` was truncated mid-word at "Cla…" — rewrote to a
  clean, complete line preserving the meaning.
- BVDT (empty narration + "Key finding one/two/three" template) → STRIPPED
  (NBB01 covers this role with authored content; per amendment, absent is legal).

**5c. Your-Turn placeholder — FIXED.**
- NBB02 narration was cancer/medical template
  ("pick any cancer type or clinical scenario…") — INVALID; nothing to do with
  rewind discipline. Rewritten to a real exercise from the video's own method
  (Esc-Esc + one-sentence respec on a viewer's actual failed session).
- NBB02 `props.command` was the cancer/proteins template — rewritten to a real
  prompt for the viewer to paste ("Open your last failed Claude Code session…").
- BHTF (template "Take what you learned from […]…") → STRIPPED (NBB02 covers it).

**5b. Chart text — N/A.** No Manim charts in this reel (Remotion cards +
ClaudeCompose bookends). The two Manim scene classes still in scenes_std.py
(Scene_B02_NbbRewindNot / Scene_B03_NbbRewindNot) with `Text([:50])` truncation
are unused after routing B02/B03 to the source reel's clean manim renders.

**5. Card text — FIXED.**
- B01 FormBCard had template items `Key point one/two/three` with empty subs.
  Authored real items from B01 narration (correction appends → conditioned on
  both → symptom moves). Mirrors the source reel's B01 items.

**6. Punt sweep — FIXED.** No gen-AI clip asks, no `fill_slates` slate,
no DoodleScene, no `STILL src=archive` for concepts. B02/B03 route to the
source reel's manim renders (both fresh; audit-passing). All bookends real.

**7. Card-only reel — PASS.** B02/B03 are Manim (drawn figures).

**8. Lens audit — PASS.**
- Popper: the reel names an in-advance failure signal ("two rewinds on the
  same row for the same failure") — a specific, measurable trigger, not a
  vague "if things feel wrong." That's the Popperian move (state what
  counts as failing before you go look for it).
- Plato: the reel separates artifact (Claude's output, which passed the
  tests), world (the array was mutated), and relationship (the handoff
  condition tested the wrong thing). The `deleteApplication` example holds
  the three apart.
Two moves earned. Not just a description of a keystroke.

**9. Brand fields — VERIFIED / FIXED.**
- `folderLabel: "@NikBearBrown"` (channel handle, not brand key). ✓
- `engine: "kokoro"`, `voice: "am_onyx"` — matches persona ("Liam, in for Bear"). ✓
- No dead ElevenLabs fields (`voice_id`, `voice_env`) present.

**10. Pacing — LOGGED.**
- NBB00: 137 words / 9s est → 15.2 wps; actual audio should measure larger.
  (NBB00 actual duration was 5.291s in an earlier measurement — inconsistent
  with the current locked-narration length. Will re-measure with Kokoro.)
- NBB02: 27 words / 8s est → 3.4 wps ✓
- Body B00–B05 measured against source-reel audio (all in 2.5–3.4 wps band). ✓

**11. type_check.py — pending after edits.**

## Not changed
- Body narration B00–B05 (LOCKED per rebuild contract).
- NBB01 verdict narration body (LOCKED; only the truncated artifactLine visual
  was fixed).
- Metadata title / slug / topic / audience.
