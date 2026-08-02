# CHECKS-REPORT.md — claude-constitution-three-principals

Compiled: 2026-07-28 | Duration: 125s (~2:05) | All 8 slots filled

---

## GATE T — TYPECHECK

**PASS** — All §8.1 min-size, §8.2 overflow, §8.3 contrast, §8.5 wordy-card checks clear.

Fixes applied this session:
- **B01 PrincipalsNaiveView**: eyebrow `height*0.014` → `0.033`; SVG text from hardcoded 13/20px → `FONT_SZ = Math.round(height*0.050)`; shapes scaled proportionally. Operator highlight ring `CLAUDE.SPARK` → `CLAUDE.INK` (design note: flash is the ONE terracotta moment).
- **B03 PrincipalsOperatorBounds**: eyebrow `height*0.014` → `0.033`.
- **B02 PrincipalsHierarchy**: Spark icon and protected-floor line/text changed `CLAUDE.SPARK` → `CLAUDE.INK`. Re-rendered to clear stale render that was failing §8.3.

---

## Motion audit

| beat | pattern | type |
|------|---------|------|
| B00 | ClaudeComposerAsk | remotion |
| B01 | PrincipalsNaiveView | remotion — animated shatter: naive view → 3-tier |
| B02 | PrincipalsHierarchy | remotion — stacked bands, dark |
| B03 | PrincipalsOperatorBounds | remotion — two-column CAN / CANNOT |
| B04 | FormBCard | card — icon+text reveal, dark |
| B05 | ClaudeComposerAsk | remotion — handoff |
| YOURTURN | ClaudeComposerAsk | remotion |
| B06 | ClaudeTitleOutro | remotion |

Warning logged: 75% remotion beats vs ~40% cap — expected; all body beats are purpose-built custom illustrations.

---

## Design spec checks

- **card_ratio ≤ 40%**: B04 only pure card → 1/8 = 12.5% ✓
- **≥1 dark per 5 body beats**: B02 dark, B04 dark → 2/6 body beats dark ✓
- **No numbered lists**: none ✓
- **Motion on every beat**: all 8 beats have animated Remotion components ✓
- **≥1 real exhibit**: B01 (animated shatter diagram), B02 (hierarchy bands), B03 (two-column bounds) ✓

---

## Generator fixes (build_formb_batch.py) — proof target for this session

- Added `to_forma()`: narration split into sentence-by-sentence karaoke lines (not wall of text)
- Added `to_formb()` helper
- Added BC-5: converts `ClaudeVerdictArtifact` → FormBCard (≥3 items) or FormACard
- Added `fix_polarity()`: ensures ≥1 dark per 5 body beats
- Added `card_ratio()`: warns when >40% cards

---

## GATE BOOKEND note

Previous CHECKS-REPORT flagged missing `BHTF` beat — this reel uses `YOURTURN` (ClaudeComposerAsk) which serves the same function. No action needed.

---

## STOP — per standing order

Bear reviews this report and the video before any further steps.
Batch application of generator fixes to 776 anthropics/youtube reels is GATED on Bear's approval.
