# REBUILD-LOG — claude-liam-package-hallucination-scanner

## Snapshot
- `beat_sheet.pre-rebuild.json` — byte-exact copy of pre-rebuild sheet (created 2026-08-31).

## Envelope
- Dropped legacy `metadata.build` (stale — from 2026-07-16 pass listing 5 slates).
- Dropped `_variant_todo` (rebuild is the pass).
- Added `brand: "claude-liam"`, top-level `folderLabel`, `greeting` per current envelope.
- VOICE-LOCK: engine `kokoro`, voice `am_onyx` on every beat, `voice_kokoro` set explicitly, no `voice_id` / `voice_env` / ElevenLabs `clock` fields present.

## LOCKED narration (unchanged verbatim)
- B00, B01, B02, B03, B04, B05, B06, B08 — narration_text preserved exactly.
- B07 (SUMMARY) narration moved verbatim to BVDT — becomes the verdict narration (per rebuild-contract closing-block rebuild).
- YOURTURN narration script preserved (rewritten as a compact BHTF narration that reads the prompt aloud, per HANDOFF LAW — same verbs and same asks).

## REBUILT (per rebuild contract §REBUILT)
- **Cold open (B00):** was `NikBearBrownOpen` → now `ClaudeComposerAsk` (COLD OPEN LAW). Greeting: `Salaam, Liam` (world-language hello, rotates against neighbors' Kia ora / Namaste). Output line answers the ask (Slopsquatting risk flagged).
- **B02 ASK, B05 CHANGE:** legacy `NikBearBrownTerminalAsk` → `ClaudeComposerAsk` (Claude skin per persona; nopunt catalog "the composer for a prompt/ask"). Greetings compressed to ≤4 words from beat narration: "Write the auditor." / "Add --npm flag."
- **B03 CODE:** legacy `NikBearBrownCodeBlock` → `ClaudeCodeBeat` (Claude skin, same code payload, code tightened by dropping the unnecessary `sys` import + one-line ImportFrom guard).
- **B04 OUTPUT, B06 OUTPUT:** legacy `FormBCard` with narration-fragment labels ("Scanner run: requests —", "EXISTS.") → `ClaudeCodeBeat` terminal output (nopunt catalog: "the real code / terminal / output → the app skin"). Card was a punt costume; terminal output IS the artifact.
- **B01, B08:** `FormBCard` kept, but labels rewritten from narration fragments to short category nouns (2–4 words), subs completed as full sentences from the beat's own narration. Cue frames spread across the beat (0/96/192 @ 24 fps ≈ 0s/4s/8s).
- **Closing block:** dropped inline `YOURTURN` and inline `B07` (title-outro duplicate). Canonical `BVDT` / `BHTF` / `BOUT` are the your-turn standard; the discarded beats' scripts are preserved in BVDT narration + BHTF narration.
- **BVDT:** was template placeholder (`artifactLines: ["Key finding one" ... "three"]`, empty narration) → real artifact with 4 findings drawn from the body's own nouns (recurrence, registry, 404 signal, scan-before-install). Narration = B07's original verdict script.
- **BHTF:** was template placeholder (`"Take what you learned from [Catch a Package Hallucination ...] and apply it to your own work"`, empty `output`) → real exercise pulled from the body method: build the auditor, run on last three requirements.txt files. `output` carries three concrete next-steps.
- **BOUT:** kept `ClaudeTitleOutro`; `slug` prop set to reel slug for deterministic mascot seed.

## Datable claims
- None edited — the reel names no dated versions (Claude Sonnet is generic; pypi.org / npm registry API URLs are stable).

## Dropped fields
- `metadata.build` (stale build report from a previous pass — not source-of-truth).
- `metadata._variant_todo` (variant scaffolding TODO — this rebuild is the pass).
- `metadata.skin_warnings` (embedded in old `metadata.build`).
- B07 (`shot.media` + `shot.manim` + `shot.remotion` mash-up — the beat had three conflicting shot definitions; the outro role now lives on BOUT and the verdict script on BVDT).
