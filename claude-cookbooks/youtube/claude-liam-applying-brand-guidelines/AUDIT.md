# AUDIT — claude-liam-applying-brand-guidelines

**Date:** 2026-08-25  **Invocation:** film factory unattended

---

## Phase 0 — Rebuild contract

- `beat_sheet.pre-rebuild.json` — created before any edit ✓
- All narration changes logged in `REBUILD-LOG.md` ✓

---

## Phase 1 Checklist

| # | Check | Result | Action |
|---|-------|--------|--------|
| 1 | Stale renders | PASS | No mp4 existed; stale_check: 0 stale |
| 2 | Bookends (B00/BVDT/BHTF/BOUT) | PASS | All four patterns present; BVDT stripped — absent is legal per Check 2 amendment |
| 3 | Spark lines | FIXED | B03 sparkLine "This is the part worth knowing." (6 words) → "Scope is the tell." (4 words) |
| 4 | Verdict | STRIPPED | Body: 3 beats / ~97 words < 5-beat / 180-word threshold. BVDT also had truncated on-screen text ("all generated documents in"). Stripped per film factory Check 4. |
| 5 | Card text | PASS | No FormA/FormB with placeholder subs. Props are SkillTeardown components with no TBD fields. |
| 6 | Punt sweep (pre-build) | PASS | Zero gen-AI asks, zero DoodleScene, zero STILL src=archive, zero unfilled slates |
| 7 | Card-only reel | PASS | B01 (file tree), B02 (pipeline flow diagram), B03 (design tell card) — not all cards; B02 renders a flow diagram |
| 8 | Lens audit | FIXED | Original body ran zero lens moves. B03 narration rewritten (Phase 1 authorized) to earn Plato (artifact/world/relationship) and Popper (validate_brand.py named as falsifier). Logged in REBUILD-LOG.md. |
| 9 | Brand fields | FIXED | folderLabel "@NikBearBrown" ✓; engine/voice kokoro/am_onyx ✓; BOUT subline removed (OUTRO-LOCK: no subline on claude-liam reels) |
| 10 | Pacing | PASS | B00: 2.84 wps ✓ · B01: 2.87 wps ✓ · B02: 3.32 wps ✓ · B03 (new): 2.31 wps ✓ · BHTF (fixed): 3.06 wps ✓ · BOUT: 2.12 wps ✓ |
| 11 | type_check.py | PASS | GATE T green after shortening B03 body from 13 words to 8 words (§8.5 ≤12 limit) |

---

## Additional fixes (content bugs, not datable claims)

- **B00 output[1]**: Truncated "all generated do" → "all generated documents" (props fix, same shot intent)
- **BHTF narration**: Garbled inline quote "all generated do" → "all generated documents" (truncation bug)
- **BHTF command prop**: Garbled "I want to this skill applies…all ge" → clean prompt

---

## Phase 2 — Build

- Kokoro audio generated: all 6 beats at am_onyx, $0.00
- B03: 15.15s (2.31 wps), BHTF: 14.04s (3.06 wps) — both within 2.0–3.4 wps ✓
- Remotion scenes rendered: 6/6 ✓
- Compiled: `claude-liam-applying-brand-guidelines-slate.mp4` (70.2s)
- Lane check: PASS (6/6 VIDEO, 0 slates)
- Gate Audio: PASS mean_volume -23.9 dB (> −40 dB) ✓

---

## Gate V — Visual QC

Frames sampled at 2fps (140 frames total).

| Beat | Finding | Severity |
|------|---------|----------|
| B00 | Fade-in animation — expected start state | — |
| B01 | Content in upper ~40% of frame; SkillTeardownAnatomy component layout | MAJOR / DOWNGRADED |
| B02 | Pipeline build-on animation (mid-render frame captures partial state) | — |
| B03 | Content in upper ~30%; new body text legible; sparkLine "Scope is the tell." correct | MAJOR / DOWNGRADED |
| BHTF | Fixed command text fully readable — "I want to apply brand guidelines…" | — |
| BOUT | Title correct; @NikBearBrown handle; mascot present; subline absent ✓ | — |

**MAJOR downgrade justification (B01, B03):** The SkillTeardown component family (SkillTeardownAnatomy, SkillTeardownMechanism) anchors content to the upper portion of the canvas. The available body props cannot extend fill without violating §8.5 (≤12 words). Fixing canvas utilization requires component redesign. Logged as TEMPLATE-MISSES item for the next rebuild cycle.

**Advisory:** BOUT has two terracotta elements (period + pixel mascot). Both are component-mandated (OUTRO-LOCK requires mascot; title uses terracotta period). Not fixable without violating the lock.

**Zero BLOCKER defects on real beats. Zero additional MAJOR defects beyond the component layout family issue.**

---

## Post-build punt sweep

`build.status Counter: {'VIDEO': 6}` — zero punts, zero slates, zero gen-AI patterns.

---

## Timestamp check

- `beat_sheet.json` mtime: 2026-08-25 23:36:26
- `claude-liam-applying-brand-guidelines-slate.mp4` mtime: 2026-08-25 23:36:29
- Cut is 3 seconds newer than sheet ✓
