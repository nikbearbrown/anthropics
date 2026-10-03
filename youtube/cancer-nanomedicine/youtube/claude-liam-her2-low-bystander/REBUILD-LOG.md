# REBUILD-LOG — claude-liam-her2-low-bystander

Timestamp: 2026-08-27

## Locked (no changes)
- Narration for B01, B02, B03, B04, B05, B06, B07, B08, B09.
- Beat order and act labels.
- Metadata identity: title, slug, topic, register, source pointer.

## Envelope rebuild
- Dropped `metadata.voice_id: TyW6NH39JcFb5M3xdIIk` (ElevenLabs dead field).
- Normalized `metadata.voice` from `nbbhuman` → `am_onyx` (matches kokoro engine, authoritative per VOICE-LOCK; the reel's audio is Kokoro am_onyx).
- Dropped stale `metadata.build` block (will be re-stamped by compile.py).
- Kept `folderLabel: "@NikBearBrown"` on BHTF (channel handle, correct).

## Skin swap — B00
- Old pattern: `NikBearBrownOpen` with `topic` + `lines[]` props (skin_warning: COLD OPEN LAW wants ClaudeComposerAsk on palette=claude).
- New pattern: `ClaudeComposerAsk` per canonical bookend rule.
- New spark line: `Namaste, Liam.` (Hindi hello; 2 words; not used by adjacent sibling reels — nanomedicine-translation-gap used `Jambo, Liam.`).
- New props: greeting/topic/segment/command/runningText/folderLabel populated from the cleavable-linker cold-open concept.
- Narration_text unchanged.

## Narration additions (NOT rewrites)
- **BVDT** was empty (`""`). Body is 8 beats / ~450 words → qualifies for a real verdict. Authored:
  - narration_text: "The verdict. HER2-positive breast cancer was targetable from 1998; HER2-low was not, because T-DM1's non-cleavable linker could not bystander-kill low-expressing cells. T-DXd's cleavable linker released a diffusible payload — DESTINY-Breast04 confirmed the effect in patients. The chemistry choice created a new targetable population: fifty-five percent of all breast cancer."
  - Old artifactLines were `["Key finding one","Key finding two","Key finding three"]` — replaced with:
    - "The cleavable linker unlocked HER2-low breast cancer — 55% of all breast cancer."
    - "T-DM1 non-cleavable = HER2-high only. T-DXd cleavable = bystander kill of HER2-low neighbors."
    - "DESTINY-Breast04 (NEJM 2022) confirmed the mechanism: PFS 9.9 vs 5.1 months."

## Card fills (props only; no narration change)
- **B01** (FormBCard) — three placeholder items ("Key point one/two/three", empty subs) authored from the beat's own narration:
  - `label: "T-DM1 non-cleavable"`, `sub: "HER2-high only. No bystander kill."`
  - `label: "T-DXd cleavable"`, `sub: "HER2-low targetable. Bystander kill enabled."`
  - `label: "55% of breast cancer"`, `sub: "A new patient population, unlocked by chemistry."`

## Punt→SHOW conversions (props only; no narration change)
- **B04** was SLATE (Manim `B04_ADCMechanism` never authored — nopunt catalog says mechanism → Manim, but the scene doesn't exist). Converted to FormBCard SHOW:
  - `title: "T-DM1 vs T-DXd mechanism"`
  - `label: "T-DM1 (non-cleavable)"`, `sub: "Payload trapped in lysosome — kills only HER2-high cell."`
  - `label: "T-DXd (cleavable)"`, `sub: "DXd diffuses to neighbors — HER2-low bystander kill."`
  - `label: "DESTINY-Breast04"`, `sub: "Bystander kill confirmed in patients."`
- **B06** was SLATE (`YOU → gen-AI clip → pantry` punt costume). Converted to FormBCard SHOW:
  - `title: "The pattern generalizes"`
  - `label: "Sacituzumab (TROP2, TNBC)"`, `sub: "CL2A cleavable + SN-38 payload — approved 2020."`
  - `label: "T-DXd in HER2-low lung"`, `sub: "Same linker, same payload — DESTINY-Lung02 response."`
  - `label: "Cleavable generalizes"`, `sub: "Bystander unlocks previously untargetable tumors."`
- **B07** was SLATE (`YOU → gen-AI clip → pantry` punt costume). Converted to FormBCard SHOW:
  - `title: "The linker choice IS the strategy"`
  - `label: "Non-cleavable = single cell"`, `sub: "T-DM1: kill only what expresses the target."`
  - `label: "Cleavable = neighborhood"`, `sub: "T-DXd: kill heterogeneous HER2 tissue."`
  - `label: "+55% patient population"`, `sub: "Chemistry redefined the eligible population."`
- **B08** was SLATE (`YOU → gen-AI clip → pantry` punt costume). Converted to FormBCard SHOW:
  - `title: "Your move"`
  - `label: "Check DAR (2-8 range)"`, `sub: "Below 2: insufficient kill. Above 8: aggregation clears fast."`
  - `label: "Check linker cleavability"`, `sub: "Non-cleavable = zero bystander, regardless of payload."`
  - `label: "Match target to biology"`, `sub: "Heterogeneous expression → cleavable required."`

## Spark line polish (props only)
- **B02** NikBearBrownTerminalAsk greeting: `The ask,` → `Research the mechanism.` (3 words, beat-specific)
- **B05** NikBearBrownTerminalAsk greeting: `The ask,` → `Survey the field.` (3 words, beat-specific)

## Datable-claim pass
- HER2-positive 1998, Doxil 1995 analogs, EMILIA OS 29.9/25.9 mo, DESTINY-Breast04 NEJM 2022 PFS 9.9/5.1 mo, sacituzumab 2020 approval, DESTINY-Lung02, DAR 2–8 range — historical anchors, all still current, no rot.
- No model names / prices / "as of" claims to update.
- No narration changes.

## Template misses
- None. All patterns used (`ClaudeComposerAsk`, `FormBCard`, `NikBearBrownTerminalAsk`, `NikBearBrownCodeBlock`, `NikBearBrownOutro`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) exist in `runtime/remotion/src/scenes/`.
