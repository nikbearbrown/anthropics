# REBUILD-LOG — nbb-handoff-condition-protocol

Run: 2026-09-01 (autonomous film-factory sweep)

## Contract
- pre-rebuild backup: `beat_sheet.pre-rebuild.json` (byte-exact of the 2026-08-01 sheet).
- Older cleaner sibling copy kept: `beat_sheet.nbb.json` (2026-07-16).
- Channel: `@NikBearBrown` (non-Claude). Non-Claude channels keep their own open skin
  (NikBearBrownOpen); NBB00/NBB01/NBB02/NBB03 remain the canonical bookends for this reel
  and use the required Claude bookend patterns (ClaudeComposerAsk, ClaudeVerdictArtifact,
  ClaudeComposerAsk, ClaudeTitleOutro).

## Datable-claim edits
None. Narration contains no dated model / version / price claim.

## Narration edits (Phase 1 authorized)

### NBB00 — cold open (spark line + narration restored)
- Reason: current beat_sheet.json narration is a 110-word "ask" auto-substituted by a
  later pass while `actual_duration_s` still measured the prior ~9 s cold-open script
  (impossible for 110 words at Kokoro pace ≈ 40 s+). Older sibling `beat_sheet.nbb.json`
  (2026-07-16) preserves the true locked cold open. Restored from that sibling.
- Greeting was `"Your turn."` (belongs on the BHTF beat, not on a cold open). Rule 3
  requires `"<world-language hello>, Liam"`. Restored the sibling's `"Merhaba, Liam"`
  (Turkish — uncommon in this book's rotation).
- `command` prop shortened to match the restored ask.

### NBB01 — verdict
- Narration kept as authored (real recap of the body). No placeholder line, verdict
  passes `verdict_audit` (all three artifactLines are body-specific claims).

### NBB02 — your turn (5c PLACEHOLDER FIX)
- Old narration referenced a "cancer type or clinical scenario" — unrelated to the
  reel's topic (a Claude Code handoff validator). Command contained the
  `[Build and Test a Handoff Condition Protocol with Claude Code]` bracket placeholder
  and the same cancer prompt.
- Rewritten to a real handoff-condition exercise the viewer DOES (paste your own
  Claude Code step, write a shell handoff_condition, run the validator, see which step
  it names as blocking).

### B01 — FormBCard placeholder fix
- Items were `"Key point one/two/three"` with empty `sub`. Rewritten to the three
  fields a real handoff condition names — test file, case count, passing inputs —
  which is exactly what B00 announces and what the validator enforces.

## Envelope changes
- Dropped bookend beats BVDT / BHTF / BOUT: empty `narration_text` + placeholder
  `artifactLines`/`command` (all three present-and-empty). They duplicate the working
  NBB01/NBB02/NBB03 bookends already on this NBB-channel reel. Per Rule 4/PHASE 1
  bookend amendment, present-and-empty is illegal; NBB* satisfies the bookend contract.
- Cleared `source_clip` / `source_audio` / `audio_file` fields on B00-B08 that pointed
  at `../handoff-condition-protocol/{clips,mp3}/…` — those files never existed at that
  path. Kokoro will regenerate the mp3s locally and rewrite `audio_file`.
- Voice/engine envelope kept: kokoro / am_onyx per VOICE-LOCK, matches metadata.

## Not changed
- Metadata (slug, title, topic, audience, palette, register, engine, voice, body_beats).
- All body narration in B00-B08 (locked). Manim scene classes in scenes_std.py untouched.
- NikBearBrown open, terminal-ask, and code-block components — the non-Claude skin.
