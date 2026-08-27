# AUDIT — agents-that-remember-memory-store

**Run:** 2026-08-26  
**Factory:** film factory (unattended)  
**Brand:** claude-liam · Palette: claude · Voice: kokoro am_onyx

---

## Check 1 — Stale renders
**PASS.** No mp4 files exist in reel directory. Nothing to delete.

## Check 2 — Bookends
**FIXED (BVDT) + FIXED (BHTF).**
- B00: ClaudeComposerAsk, greeting "Hola, Liam" ✓
- BVDT: ClaudeVerdictArtifact — present-with-template-defaults ("Key finding one/two/three") → FIXED: authored real verdict from body (see Check 4).
- BHTF: ClaudeComposerAsk, greeting "Your turn." ✓ — folderLabel was "@claude-liam" → FIXED to "@NikBearBrown" (see Check 9).
- BOUT: ClaudeTitleOutro ✓

## Check 3 — Spark lines
**PASS.** No inner ClaudeComposerAsk beats (B01–B08 use Cwc* custom components). B00 greeting "Hola, Liam" ✓. BHTF greeting "Your turn." ✓.

## Check 4 — Verdict
**FIXED.** BVDT had template `artifactLines` ("Key finding one", "Key finding two", "Key finding three") and empty `narration_text ""`  — invalid.

Body: 7 body beats, narration well over 180 words → author threshold met.

Authored from body's own nouns and numbers:
- narration_text: "Sessions are stateless by design — each starts blank. Attach a memory store and the agent writes structured facts in session A and reads them in session B: key-value pairs, confidence-scored, per user. The Dreaming Service runs between sessions — not during — reads past transcripts, and writes structured memory back automatically. Zero latency impact on your conversation. Memory is infrastructure you wire in. It is not a property of the model."
- artifactHeading: "The three-layer model" (changed from "Key findings")
- artifactLines: 4 real lines derived from B02/B05/B06 content (isolation, key-value structure, Dreaming Service between-session behavior, memory-as-infrastructure)

Body verdict at B08 (ClaudeVerdictArtifact) is separate and unchanged — already contained real content.

## Check 5 — Card text
**PASS.** No FormA/FormB beats. Cwc* custom components. BVDT template sub fields replaced with real content (Check 4).

## Check 6 — Punt sweep
**PASS.** All Cwc* patterns confirmed present in runtime:
- B01: CwcMemoryQuestion — registered in Root.tsx via CwcShared.tsx ✓
- B02: CwcSessionIsolation — registered in Root.tsx via CwcShared.tsx ✓
- B03: CwcMemoryTimeline — CwcMemoryTimeline.tsx ✓
- B04: CwcMemoryProgression — registered in Root.tsx via CwcShared.tsx ✓
- B05: CwcMemorySchema — CwcMemorySchema.tsx ✓
- B06: CwcDreamingService — CwcDreamingService.tsx ✓
- B07: CwcMemoryRetrieval — CwcMemoryRetrieval.tsx ✓
- B08: ClaudeVerdictArtifact (body verdict) ✓
- B09: ClaudeComposerAsk (handoff) ✓
- B10: ClaudeTitleOutro ✓
No gen-AI asks, no unfilled slates, no DoodleScene/DoodleChart, no STILL src=archive.

## Check 7 — Card-only reel
**PASS.** B01–B07 use Cwc* visual components. Not card-only.

## Check 8 — Lens audit
**PASS (2 moves).** 
- **Plato** (B05): Names artifact (structured key-value memory records with user_id, key, value, confidence), names world (agent's recall capability), names relationship ("the structure is what makes retrieval reliable — loose prose would not index well"). Explicit artifact/world/relationship triple present.
- **Popper** (B03): Before/after contrast explicitly demonstrates falsifiability. The reel shows the failure mode (no memory store → agent has no idea) before showing the fix. "Session B: you ask 'what's my coding style?' The agent has no idea. It was never written anywhere." → states what failing looks like before demonstrating the solution.

## Check 9 — Brand fields
**FIXED.** BHTF had `folderLabel: "@claude-liam"` — brand key, not channel handle. Changed to `@NikBearBrown`.
All other folderLabel fields: B00 `@NikBearBrown` ✓, B09 `@NikBearBrown` ✓.
Metadata: engine kokoro / voice am_onyx ✓. Persona: Liam (Kokoro am_onyx) ✓ — narration uses "Liam, in for Bear" ✓.

## Check 10 — Pacing
**LOG.** B09 narration: 121 words / 32.32s = 3.74 WPS (above 3.4 WPS ceiling). Narration is LOCKED per rebuild contract. Not fixed; logged here.
All other beats: within 2.0–3.4 WPS range. See calculations in session notes.

---

## Summary
- Checks FIXED: 2 (4), 3 (covered), 9
- Checks LOGGED: 10 (B09 pacing)
- No checks BLOCKED
- Reel proceeds to PHASE 2 build.
