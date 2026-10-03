# AUDIT — claude-liam-her2-low-bystander
_Generated 2026-08-27, filmloop unattended pass_

## Phase 1 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | No stale mp4s in folder; `clips/master.m4a` older than sheet but will be rebuilt by compile step (audio inputs re-concat, master regenerated) |
| 2 | Bookends present | FIXED | B00 swapped from `NikBearBrownOpen` → `ClaudeComposerAsk`. BVDT/BHTF/BOUT patterns already correct. |
| 3 | Spark lines | FIXED | B00 greeting `Namaste, Liam.` (Hindi, not adjacent-used). B02 greeting `The ask,` → `Research the mechanism.` B05 greeting `The ask,` → `Survey the field.` BHTF `Your turn.` already present. All ≤ 4 words. |
| 4 | Verdict authored | FIXED | BVDT had placeholder `Key finding one/two/three`; authored real verdict from body content (8 beats, ~450 words qualifies) + rewrote narration_text from empty to spoken verdict. |
| 5 | Card text | FIXED | B01 placeholder items (`Key point one/two/three`, empty subs) authored from beat narration. |
| 5b | Chart text | N/A | No Manim/D3 chart beats — B04 converted from stub Manim scene to FormBCard. |
| 6 | Punt sweep | FIXED | B04 (SLATE Manim scene never authored) → FormBCard. B06/B07/B08 (`YOU → gen-AI clip → pantry` costumes) → FormBCard × 3. Zero punts remain. |
| 7 | Card-only reel? | PASS | Reel has NikBearBrownCodeBlock (real code), NikBearBrownTerminalAsk × 2 (real command payloads), plus FormBCards. Not card-only. |
| 8 | Lens moves | PASS | POPPER: DESTINY-Breast04 as the trial designed to falsify/confirm — the mechanism was made testable in patients. PLATO: artifact (adc_comparison.py table) vs world (biology/tumor response) named explicitly. Reel earns ≥ 2 moves. |
| 9 | Brand fields | FIXED | Dropped `metadata.voice_id` (ElevenLabs dead field). `metadata.voice` normalized `nbbhuman` → `am_onyx` (kokoro is authoritative). `folderLabel: "@NikBearBrown"` channel handle preserved. Persona: narration says "Liam, in for Bear" and voice is Kokoro `am_onyx` — coherent. |
| 10 | Pacing | LOG | B02 narration ~30 words for 11.97s = 2.5 wps (in range). B05 ~35 words for 11.09s = 3.2 wps (in range). B01 66 words for 23.54s = 2.8 wps (in range). No outliers. |
| 11 | type_check.py | PENDING | Runs after build (needs rendered frames for §8.1 measurements). |

## Blockers

None. All content-level fixes are in the sheet; ready to build.

## Punts converted (nopunt log)

| Beat | Old status | Old form | New form | Rationale |
|---|---|---|---|---|
| B04 | SLATE | Manim `B04_ADCMechanism` (scene never authored) | FormBCard | Catalog: mechanism → Manim, but scene absent; converting to FormBCard delivers the mechanism as three named comparisons rather than an unfilled slate. |
| B06 | SLATE | `YOU → gen-AI clip → pantry` (punt costume) | FormBCard | Catalog: enumerated named things → FormB. Narration names three: sacituzumab TROP2 TNBC, T-DXd HER2-low lung, cleavable generalization. |
| B07 | SLATE | `YOU → gen-AI clip → pantry` (punt costume) | FormBCard | Catalog: enumerated named things → FormB. Narration compares single-cell vs neighborhood mechanism + patient shift. |
| B08 | SLATE | `YOU → gen-AI clip → pantry` (punt costume) | FormBCard | Catalog: enumerated actions → FormB. Narration names three viewer moves (DAR, cleavability, biology match). |
