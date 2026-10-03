# REBUILD-LOG — nbb-one-sentence-problem-statement

## Snapshot
- `beat_sheet.pre-rebuild.json` created byte-exact from pre-edit `beat_sheet.json` (2026-08-31).

## Envelope rebuilt
- Dropped duplicate NBB0X wrapper beats (NBB00/NBB01/NBB02/NBB03) that duplicated the B00/BVDT/BHTF/BOUT bookends.
- Consolidated bookends to canonical B00/BHTF/BOUT; BVDT stripped (see verdict).
- Metadata: added `channel`, normalized `palette: claude`, dropped `old_outro_beats`.

## LOCKED (unchanged)
- Body beats B01, B02, B03, B04 — `narration_text` locked verbatim per rebuild contract.
- Act structure and body order preserved.
- Manim scenes (Scene_B02/B03/B04) preserved as-is.

## Datable-claim edits
- None. The body is timeless — no model versions, prices, or "as of" claims.

## shot.form derived (per SHOT-FORM-SYSTEM)
- B00: composer_ask
- B01: formB_card
- B02–B04: manim_card
- BHTF: composer_ask
- BOUT: title_outro

## Bookend narration authored
- **B00**: `Merhaba. This is Liam, in for Bear. Why did it take fourteen minutes and two refusals to produce one valid sentence?` — combines Merhaba greeting with IN-FOR-BEAR law and the body's driving question. Source: NBB00 predecessor.
- **BHTF**: `Your turn. Write your current project as one sentence, then circle every and. If two remain, you are building two things. Pick one, name the user, name the done-condition, then ask Claude what the finished sentence forces you to commit to.` — real exercise built from the reel's own mechanism. Replaced template placeholder ("Take what you learned from […] and apply it to your own work").
- **BHTF command** (composer prompt): rewrote from a cancer/clinical-scenario placeholder (nonsense here) to a real ands-audit prompt.
- **BOUT**: `Why the One-Sentence Problem Statement Is the Most Expensive Thing You Write. Liam, in for Bear.` — title restate + Liam sign-off.

## Verdict decision
- BVDT stripped. Body has 4 beats (< 5 threshold) — placeholder verdict ("Key finding one/two/three") removed rather than authored. Absent BVDT is legal per audit rule 4.

## B01 FormB fix
- Was: 3 items "Key point one/two/three", empty subs — placeholder violation.
- Now: 4 items naming the four projects hidden in Seth's original sentence (audit / refactor / write tests / generate CLAUDE.md) — the "four projects dressed as one" the beat's narration describes.
