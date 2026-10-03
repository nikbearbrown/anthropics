# REBUILD-LOG — claude-liam-nanomedicine-translation-gap

Timestamp: 2026-08-27

## Locked (no changes)
- Narration for B01, B02, B03, B04, B05, B06, B07, B08, B09.
- Beat order and act labels.
- Metadata identity: title, slug, topic, source.

## Envelope rebuild
- Dropped `metadata.voice_id: TyW6NH39JcFb5M3xdIIk` (ElevenLabs dead field).
- Normalized `metadata.voice` from `nbbhuman` → `am_onyx` (matches kokoro engine, which is authoritative per VOICE-LOCK; the reel's audio is Kokoro am_onyx).
- Kept `folderLabel: "@NikBearBrown"` on BHTF (channel handle, correct).

## Skin swap — B00
- Old pattern: `NikBearBrownOpen` with `topic` + `lines[]` props.
- New pattern: `ClaudeComposerAsk` per canonical bookend rule.
- New spark line: `Jambo, Liam.` (Swahili hello; 2 words; rotates fresh).
- New props: greeting/topic/segment/command/runningText/folderLabel populated from the intro concept (compile the honest ledger).
- Narration_text unchanged.

## Narration additions (NOT rewrites)
- **BVDT** was empty (`""`). Body is 8 beats / ~420 words → qualifies for a real verdict. Authored:
  - narration_text: "The verdict: thirty years, thousands of formulations, fewer than twenty approvals. Not one succeeded primarily by passive EPR. Doxil reduced cardiotoxicity. Abraxane rode the albumin pathway. ADCs and radioligands actively target. The translation gap is a measurement problem: the loop measures at every step; the line assumes and hopes."
  - Old artifactLines were `["Key finding one","Key finding two","Key finding three"]` — replaced with:
    - "Fewer than twenty nanomedicine approvals in thirty years."
    - "Not one succeeded primarily via passive EPR: real drivers were cardiotoxicity, albumin-SPARC, active targeting, radioligand loops."
    - "The gap is measurement — nanoparticles lack quantifiable imaging, biodistribution confirmation, and target-confirmed kill."

## Card fills (props only; no narration change)
- **B01** (FormBCard) — three empty `sub` fields authored from the beat's own narration:
  - `label: "30 years, 4 approvals"`, `sub: "Doxil 1995 → Abraxane 2005 → ADCs 2013 → radioligands 2022."`
  - `label: "Thousands developed, <20 approved"`, `sub: "Lower success rate than small-molecule drugs."`
  - `label: "Good at making, less good at working"`, `sub: "The gap is not the chemistry — it is patients."`

## Spark line polish (props only)
- **B02** NikBearBrownTerminalAsk greeting: `The ask,` → `Compile the ledger.` (3 words, beat-specific)
- **B05** NikBearBrownTerminalAsk greeting: `The ask,` → `Iterate the loop.` (3 words, beat-specific)

## Datable-claim pass
- Dates in narration (Doxil 1995, Abraxane 2005, ADCs 2013, Pluvicto/radioligands 2022) are historical anchors — no rot.
- No model names / prices / "as of" claims to update.
- No changes.

## Template misses
- None. All patterns used (`ClaudeComposerAsk`, `FormBCard`, `NikBearBrownTerminalAsk`, `NikBearBrownCodeBlock`, `NikBearBrownOutro`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) exist in `runtime/remotion/src/scenes/`.
