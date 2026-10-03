# REBUILD-LOG — nbb-nanomedicine-translation-gap

Rebuild pass 2026-08-30 under the anthropics film-factory rebuild contract.

## Snapshot
- `beat_sheet.pre-rebuild.json` = byte-exact copy of the pre-rebuild sheet (23,349 bytes, 2026-07-16 build).

## What the pre-rebuild sheet was
A duplicate NBB channel variant of the source reel `../nanomedicine-translation-gap` (same @NikBearBrown channel, same locked body narration B00–B08 verbatim from source). The pre-rebuild wrapped the body with an obsolete legacy Liam envelope (NBB00/NBB01/NBB02/NBB03) AND stub current-doctrine bookends (BVDT/BHTF/BOUT with placeholder `Key finding one/two/three` lines and empty `narration_text`).

## What was REBUILT (rebuild contract permits)
- **Bookend closing block** — the rebuild contract explicitly names the closing block as the ONE place new narration is expected. Adopted the source reel's fully-authored BVDT/BHTF/BOUT (authored 2026-08-30 during the source reel's own rebuild pass). Content is derived from the sheet's own sparkLines and verdict material — not template stubs. See source `../nanomedicine-translation-gap/beat_sheet.json` beats BVDT/BHTF/BOUT.
- **Dropped legacy wrap** — NBB00, NBB01, NBB02, NBB03 removed. They were a pre-current-doctrine Liam-style envelope; their pedagogical role is now filled by the canonical bookends B00 (NikBearBrownOpen — non-Claude channel keeps its own open, per rebuild §Non-claude channels), BVDT, BHTF, BOUT.
- **Dropped stub BVDT/BHTF/BOUT** — replaced with authored versions listed above. Present-and-empty verdict was invalid per PHASE 1 check 2 amendment.
- **VOICE-LOCK envelope normalized** — engine=kokoro, voice=am_onyx across all beats; no ElevenLabs residue (never present in pre-rebuild); `voice_id`/`voice_env`/`clock` prose absent.
- **shot.form derivation** — every beat carries an explicit `shot.remotion.pattern` (NikBearBrownOpen, FormBCard, FormACard, NikBearBrownTerminalAsk, NikBearBrownCodeBlock, NikBearBrownOutro, ClaudeVerdictArtifact, ClaudeComposerAsk, ClaudeTitleOutro) — all templates exist in the runtime registry (verified via source reel's shipping build 2026-08-30).
- **B01/B04/B06/B08 FormBCard items filled** — pre-rebuild carried placeholder labels "Key point one/two/three" with empty subs. Replaced with source reel's authored ledger content (matches the narration's actual nouns/dates/mechanisms).

## What is LOCKED (verbatim from pre-rebuild / source)
- B00 narration: "Nik Bear Brown. Thirty years. Thousands of nanoparticles. Fewer than twenty approvals." — identical.
- B01–B08 narration: verbatim from pre-rebuild (which was verbatim from source). Not one word changed.
- B09 narration ("Nik Bear Brown. Build it with a CLI. Then take it apart. At Nik Bear Brown, nikbearbrown dot com.") — adopted from source; the pre-rebuild's version of the outro was carried under the NBB03 title-outro slot; the actual B09 sign-off narration is a channel bookend under the rebuild contract's "close narration is NEW writing" allowance.
- Metadata identity: title, topic, audience, register — unchanged.

## Datable-claim pass
No datable claims edited. Approval dates (Doxil 1995, Abraxane 2005, ADCs 2013–, radioligands 2022) and drug names (Doxil, Abraxane, T-DXd, Pluvicto) are correct per source reel's FACTCHECK.md.

## Slug change
Pre-rebuild `slug: "nanomedicine-translation-gap"` collided with the source reel's slug. Changed to `nbb-nanomedicine-translation-gap` (matches folder name) to prevent output-path collision. Metadata-only change; no narration impact.
