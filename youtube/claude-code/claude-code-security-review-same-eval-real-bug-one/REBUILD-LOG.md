# REBUILD-LOG — claude-code-security-review-same-eval-real-bug-one

Rebuild run: 2026-08-31 (film-loop invocation).
Backup: `beat_sheet.pre-rebuild.json` (byte-exact copy of pre-rebuild sheet).

## LOCKED (verbatim)
- All body narration in B00–B05 preserved word-for-word.
- Beat order for the body (B00 → B05).
- Metadata identity: slug, title, topic, source pointer, register, channel.

## REBUILT
- **Envelope:** dropped dead ElevenLabs-era `metadata.clock` prose field
  ("narration (Kokoro am_onyx) — master clock; conform each beat to measured
  audio"). Kokoro `am_onyx` is fixed by VOICE-LOCK; the prose was residue.
- **`shot.form` derived per beat**
  (COMPOSER_ASK / FORM_B_CARD / FORM_A_CARD / CODE_BEAT / TITLE_OUTRO).
- **B00 greeting:** `"Liam"` → `"Konnichiwa, Liam"` — pulled from
  `metadata.greeting`, fixes empty spark-line lone-asterisk defect.
- **B00 output:** empty `[]` → two lines from the reel's own hook
  ("Because the token is not the vulnerability." / "Reachability is.") so the
  composer answers instead of hanging on `runningText`.
- **B01 items:** replaced placeholder subs
  ("Key point one/two/three", empty `sub`) with content drawn from body:
  "Same token" / "One is reachable" / "The other is sealed", each with a real
  one-line sub.
- **B02 shot:** none → `FormBCard` two-up naming the 100 vs 5 comparison the
  narration states.
- **B03 shot:** none → `FormBCard` four-up naming the four context inputs the
  narration lists (data flow, entry point, architectural intent, reachability).
- **B04 shot:** none → `ClaudeCodeBeat` showing the two eval() call-sites
  side by side (public web handler → REPORTED, sandboxed math test → EXCLUDED),
  matching the app-SKIN rule for code beats.
- **B05 shot:** none → `FormACard` recap card
  ("The token isn't the bug. / Reachability is.").
- **BVDT (verdict) — STRIPPED.** Placeholder verdict lines
  ("Key finding one/two/three") with empty narration. Body word-count = 138
  across 6 beats; below the 180-word / 5-beat threshold in the film-loop
  contract → strip. Amendment: BVDT legitimately absent when a previous pass
  stripped a placeholder verdict (spec, Phase 1 §2).
- **YOURTURN — REMOVED as pre-canonical duplicate.** The v1-era "your turn"
  beat was superseded by canonical `BHTF`. Its authored narration (a real
  paste-this prompt) was folded into `BHTF` so nothing is lost.
- **OUTRO — REMOVED as pre-canonical duplicate.** The v1-era outro title
  card was superseded by canonical `BOUT` (`ClaudeTitleOutro`). Keeping both
  would title-restate twice.
- **BHTF narration:** authored from body content — a real "trace one flagged
  line" exercise using the four checks (origin, path, entry-point, sink) the
  video teaches. No more "Take what you learned from [X]" placeholder.
- **BOUT narration:** added "Liam, in for Bear." sign-off (IN-FOR-BEAR LAW).

## Datable-claim edits
- None. No model version, price, or "as of" claim in the locked narration.

## Gates
- GATE T (type_check.py): PASS.
- Verdict-strip: applied by removing BVDT (verdict_strip.py's `--only` glob
  pattern misses this reel's `youtube/claude-code/<slug>/` layout; strip
  reproduced by hand).
