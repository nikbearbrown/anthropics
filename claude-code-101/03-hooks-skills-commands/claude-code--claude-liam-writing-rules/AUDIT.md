# AUDIT.md — claude-liam-writing-rules

**Audited:** 2026-08-21  
**Auditor:** film-factory (unattended)  
**Phase:** PHASE 1 + PHASE 2

---

## Check 1 — Stale renders

No `media/` directory exists. No stale mp4 files to delete.  
**STATUS: PASS**

---

## Check 2 — Bookends

| Beat | Pattern | Required |
|---|---|---|
| B00 | ClaudeComposerAsk | cold open ✓ |
| BVDT | ClaudeVerdictArtifact | verdict ✓ |
| BHTF | ClaudeComposerAsk | your-turn ✓ |
| BOUT | ClaudeTitleOutro | outro ✓ |

All four canonical bookends present.  
**STATUS: PASS**

---

## Check 3 — Spark lines

| Beat | Field | Found | Required | Fix |
|---|---|---|---|---|
| B00 | `props.greeting` | `"Ciao, Liam"` | `"<lang>, Liam"` | — |
| BHTF | `props.greeting` | `"Your Turn"` → `"Your turn."` | `"Your turn."` | FIXED |
| B01 inner | `props.sparkLine` | HookifyRuleAnatomy (custom pattern, ≤4 words after fix) | ≤4 words | FIXED (13→4 words) |

Inner beats B01, B02, B05 use custom HookifyXxx patterns (not ClaudeComposerAsk). No inner composer asks present.  
**STATUS: FIXED**

---

## Check 4 — Verdict

BVDT present with `ClaudeVerdictArtifact`.  
- `artifactHeading`: "Writing Hookify Rules" (specific to this reel)
- 6 `artifactLines`: all specific — file naming convention, 5 events, conditions format, action values, body guidance, gaps. No line would apply to a different video.
- Narration: real summary of the skill (87 words, specific findings).

Ran verdict_strip.py logic manually: 6 real lines, 0 placeholders. BVDT has real content.  
**STATUS: PASS**

---

## Check 5 — Card text

No FormA/FormB beats. B00 and BHTF output lines are specific and non-placeholder. BVDT artifactLines reviewed (Check 4). No subs or labels found empty or overflowing.  
**STATUS: PASS**

---

## Check 6 — Punt sweep

| Beat | Pattern | Status |
|---|---|---|
| B00 | ClaudeComposerAsk | registered, renders ✓ |
| B01 | HookifyRuleAnatomy | registered at `runtime/remotion/src/scenes/HookifyRuleAnatomy.tsx` ✓ |
| B02 | HookifyEventTypes | registered at `runtime/remotion/src/scenes/HookifyEventTypes.tsx` ✓ |
| B05 | HookifyTell | registered at `runtime/remotion/src/scenes/HookifyTell.tsx` ✓ |
| BVDT | ClaudeVerdictArtifact | registered ✓ |
| BHTF | ClaudeComposerAsk | registered ✓ |
| BOUT | ClaudeTitleOutro | registered ✓ |

Zero gen-AI asks, zero unfilled slates, zero DoodleScene/DoodleChart, zero STILL src=archive.  
**STATUS: PASS**

---

## Check 7 — Card-only reel

B01 (HookifyRuleAnatomy) renders "file location box, 5 frontmatter field rows, spark line" — structured animated content, not a text card. B02 (HookifyEventTypes) renders event rows and conditions callout. B05 (HookifyTell) renders 2-column teardown with callout and spark. These are custom teaching components that draw structure, not generic word cards.  
**STATUS: PASS**

---

## Check 8 — Lens audit (LENS-NOTES.md)

Reel type: skill teardown — evaluates the Writing Hookify Rules SKILL.md.

| Move | Where | Evidence |
|---|---|---|
| Descartes (what would falsify?) | B05 | "block action is described but never demonstrated — what does the user or Claude actually see when a rule blocks an operation?" and "conditions system for stop and prompt events does not document what fields are available" — asks what's missing to falsify completeness claim |
| Popper (failure criterion stated in advance) | BHTF | "If the rm rule uses action warn instead of block — it allows the command through, which is the opposite of what was asked. That is your gate." — pre-states the failure condition |

Two moves confirmed (Descartes + Popper). Minimum satisfied.  
**STATUS: PASS**

---

## Check 9 — Brand fields

| Field | Value | Check |
|---|---|---|
| `folderLabel` | `@NikBearBrown` | channel handle ✓ (not brand key) |
| `engine` | `kokoro` | matches audio that will be generated ✓ |
| `voice` | `am_onyx` | Kokoro am_onyx ✓ |
| `persona` | `Liam (in for Bear)` | narration says "this is Liam, in for Bear" ✓ |
| `modelLabel` B00 | `Opus 4.8` → `Opus 4.7` | FIXED — datable claim, logged in REBUILD-LOG.md |
| `modelLabel` BHTF | `Opus 4.8` → `Opus 4.7` | FIXED — datable claim |

**STATUS: FIXED**

---

## Check 10 — Pacing (2.0–3.4 wps)

| Beat | actual_duration_s | Words (est.) | wps |
|---|---|---|---|
| B00 | 37.8 | ~115 | ~3.04 |
| B01 | 58.18 | ~168 | ~2.89 |
| B02 | 58.69 | ~168 | ~2.86 |
| B05 | 68.95 | ~196 | ~2.84 |
| BVDT | 33.41 | ~87 | ~2.60 |
| BHTF | 51.73 | ~170 | ~3.29 |
| BOUT | 3.37 | ~7 | ~2.08 |

All beats within 2.0–3.4 wps range.  
**STATUS: PASS**

---

## Check 11 — type_check.py

First run: FAIL — B01 sparkLine "Name it. Event it. Pattern it. Message it. One markdown file, immediate effect." (13 words) > 12-word pull-quote limit (§8.5).  
Fix: shortened to "File. Fields. Pattern. Message." (4 words).  
Second run: **GATE T PASS** — 0 FAILs, all 3 middle beats pass no-wordy-card §8.5.

**STATUS: FIXED → PASS**

---

## Phase 1 Summary

| Check | Result |
|---|---|
| 1. Stale renders | PASS |
| 2. Bookends | PASS |
| 3. Spark lines | FIXED |
| 4. Verdict | PASS |
| 5. Card text | PASS |
| 6. Punt sweep | PASS |
| 7. Card-only | PASS |
| 8. Lens audit | PASS |
| 9. Brand fields | FIXED |
| 10. Pacing | PASS |
| 11. type_check | FIXED → PASS |

**No BLOCKED checks. Proceeding to Phase 2.**

---

## Phase 2 — Build

Audio: existing mp3s in `mp3/` (narration LOCKED, unchanged); all `actual_duration_s` already measured in beat_sheet.  
Remotion: rendering all 7 beats via `remotion_scenes.py`.  
Compile: `compile.py` assembling final cut.
