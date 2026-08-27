# BUILD LOG — claude-liam-enterprise-search

## Step 1 — Schema Reconcile

**Status:** DONE

Changes applied:
- `id` → `beat_id` for all beats
- `metadata.voice_kokoro: am_onyx` added (pipeline reads this, not `.voice`)
- `metadata.topic: CLAUDE · COWORK PLUGINS` added
- `shot` object added to all beats without one
- `estimated_duration_s` derived from word count (2.9 wps) for beats lacking it

**Remotion patterns used (VR* series — all use CLAUDE tokens natively):**

  C01 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  B01 (PredictCard) → VRPredictCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  C02 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  B05 (illustration/search-inside-document) → SlateCard (unregistered custom illustration — will render as slate in previz; needs Remotion component or pantry still before final cut).
  B06 (SourceFlow) → VRSourceFlow — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  C03 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  B09 (illustration/context-injection) → SlateCard (unregistered custom illustration — will render as slate in previz; needs Remotion component or pantry still before final cut).
  C04 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  B11 (ChipGrid) → VRChipGrid — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  C05 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  C06 (SegmentCard) → VRSegmentCard — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.
  B21 (ChipGrid) → VRChipGrid — already uses CLAUDE tokens (cream/ink/terracotta); no additional retint needed.

**Retint log:** VR* patterns (VRSegmentCard, VRChipGrid, VRPredictCard, VRSourceFlow, VRLayerStack) are from VercelRefactorIllu.tsx which imports `CLAUDE` tokens directly — cream #F2F0E9, ink #3D3929, accent/terracotta #D97757. No additional retinting required.

## Step 2 — Lane-Mix Lint

Pending audio lock.

## Step 3 — Gate P

**GATE P REQUIRED** — present full narration for sign-off before audio.


## 2026-08-26 — HUMAN FEEDBACK (Bear, is-done review): text issues + bunched boxes

Bear flagged the slate cut: bar-chart text colliding/truncated (B02, B09) and the
chip cards "bunched up in the upper left ... boxes bigger and in the middle" (B11/B21).

### Root causes and fixes
1. **VRChipGrid bunched upper-left — canvas mismatch, EVERY VR* structural beat.**
   `illustrations/structural.tsx` components are authored in a 1280×720 design space,
   but Root.tsx registers the VR* comps at 1920×1080 — absolute pixel math stranded
   every illustration in the top-left 2/3 of frame. FIX (shared, permanent):
   `IlluStage` (illustrations/kit.tsx) now scales its 1280×720 design space to the
   actual canvas via useVideoConfig, centered. ChipGrid additionally centers its grid
   block vertically and enlarges cards for ≤6 items. §9 verified: lint clean, tsc
   (2 pre-existing Root.tsx errors untouched), same-frame-twice pixel-identical,
   frames read. NOTE: other already-built reels with VR* beats have the old layout
   baked into media/*.mp4 — they need a re-render pass.
2. **B02/B09 bar charts — generated `Text(narration[:30])` labels** collided and
   truncated mid-word; captions were 60-char slices; bar heights contradicted the
   narration (the favored thing was shorter). Rewrote both scenes in scenes_std.py:
   short category labels ("by filename/by content", "generic/grounded answer"),
   complete captions, heights matching meaning. FILMLOOP-PROMPT.md gained rule 5b
   so the loop stops generating narration-fragment chart text.
3. **"ACTI" fused** — the known Pango space-collapse; "ACT  I"/"ACT  III" doubled.

### State
B02/B09/B11/B21 re-rendered; cut recompiled → `claude-liam-enterprise-search.mp4`
(master-named: no slate beats remain). All four fixed beats verified by eye in the
cut. Automated GATE V fails 34× `underfill` — the pre-existing 55%-fill-floor vs
airy-brand-style tension (every defect is underfill/low-contrast; none are the
flagged issues, none from this session's beats). That threshold question is open
at pipeline level, not per-reel.
