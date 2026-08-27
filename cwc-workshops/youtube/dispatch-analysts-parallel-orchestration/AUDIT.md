# AUDIT — dispatch-analysts-parallel-orchestration

**Date:** 2026-08-26  
**Operator:** film-factory (unattended)  
**Reel:** cwc-workshops/youtube/dispatch-analysts-parallel-orchestration

---

## Check 1 — Stale renders

**PASS.** No `media/` folder exists; no mp4 files present. Nothing to delete.

---

## Check 2 — Bookends

| Bookend | Pattern | Status |
|---|---|---|
| B00 | ClaudeComposerAsk | PASS |
| BVDT | ClaudeVerdictArtifact | FIXED (template content replaced with real verdict — see Check 4) |
| BHTF | ClaudeComposerAsk | FIXED (folderLabel `@claude-liam` → `@NikBearBrown`; command genericness fixed) |
| BOUT | ClaudeTitleOutro | FIXED (added missing `handle` and `subline` props) |

---

## Check 3 — Spark lines

All Cwc* body beats carry a `sparkLine` prop. All five over-length spark lines **FIXED**:

| Beat | Old (words) | New (words) |
|---|---|---|
| B01 | "One head. Many analysts. No blocking." (6) | "One orchestrator, N sessions." (4) ✓ |
| B02 | "Tool call → server → sessions → results." (5) | "Custom tool. Server intercepts." (4) ✓ |
| B03 | "Fan out. Fan in." (4) | unchanged ✓ |
| B04 | "Server coordinates. Agent decides." (4) | unchanged ✓ |
| B05 | "Serial is a queue. Parallel is a wave." (8) | "Serial queues. Parallel waves." (3) ✓ |
| B06 | "Fan out collects everything. Fan in decides." (7) | "Deduplicate, rank, merge." (3) ✓ |
| B07 | "The contract is what makes parallelism safe." (7) | "Schema makes scale safe." (4) ✓ |

BHTF greeting: `"Your turn."` ✓  
B00 greeting: `"Bonjour, Liam"` ✓

---

## Check 4 — Verdict

**FIXED.** BVDT had template placeholder lines ("Key finding one/two/three") and generic heading "Key findings". Body has 7 beats and 550+ words — criterion for authoring a real verdict met.

Authored from body's own nouns and numbers (B05 timing data, B02/B03 mechanism, B07 schema contract). See REBUILD-LOG.md for old → new.

B08 (main-sequence verdict) already had real, specific content — PASS.

---

## Check 5 — Card text

**PASS.** No FormA/FormB beats in this reel. All ClaudeVerdictArtifact lines are now real (BVDT fixed above). No placeholder `sub` fields or overflowing labels found.

---

## Check 6 — Punt sweep

**PASS.** All Cwc* components confirmed registered in Root.tsx:
- `CwcOrchestrationQuestion` → alias for CwcConceptCard in CwcShared.tsx ✓
- `CwcFanOutConcept` → alias for CwcConceptCard in CwcShared.tsx ✓
- `CwcFanOutFlow` → standalone scene ✓
- `CwcSpreadMechanism` → alias for CwcConceptCard in CwcShared.tsx ✓
- `CwcFanOutSpeedGain` → standalone scene ✓
- `CwcResultAggregation` → standalone scene ✓
- `CwcOrchestrationContract` → standalone scene ✓

No gen-AI asks, no unfilled fill_slates, no DoodleScene/DoodleChart, no STILL src=archive for conceptual content found.

---

## Check 7 — Card-only reel

**PASS.** Multiple dedicated graphic beats (CwcFanOutFlow, CwcFanOutSpeedGain, CwcResultAggregation, CwcOrchestrationContract) render real diagrams. Not a card-only reel.

---

## Check 8 — Lens audit

**PASS — two moves identified:**

1. **Popper move** — B07 (orchestration-contract): "If an analyst returns something off-schema, the aggregator rejects it cleanly — one failed session does not corrupt the others." States what counts as failure in advance, in measurable terms (schema rejection).

2. **Popper / Descartes combined** — B09 (your-turn): "Watch what happens when one analyst fails: does the head get a partial result, or does it wait for a retry? Watch what happens when all three finish at different times: does the merge happen immediately, or does the server collect the slowest one?" Directed falsification checklist — the viewer is explicitly sent to test the failure modes.

Two distinct lens moves earned, Popper being the dominant one applied throughout.

---

## Check 9 — Brand fields

| Field | Status |
|---|---|
| B00 `folderLabel: "@NikBearBrown"` | PASS |
| B09 `folderLabel: "@NikBearBrown"` | PASS |
| BHTF `folderLabel` | FIXED (`@claude-liam` → `@NikBearBrown`) |
| BOUT `handle` | FIXED (added `@NikBearBrown`) |
| BOUT `subline` | FIXED (added "Liam, in for Bear.") |
| `engine: "kokoro"`, `voice: "am_onyx"` | PASS throughout |
| IN-FOR-BEAR LAW | PASS — B00: "This is Liam, in for Bear." B09/B10: "Liam, in for Bear." |
| `modelLabel: "Fable 5"` | FIXED → `"claude-sonnet-4-6"` (datable claim, logged in REBUILD-LOG.md) |

---

## Check 10 — Pacing

| Beat | Words | Duration (s) | WPS | Flag |
|---|---|---|---|---|
| B00 | 32 | 10.79 | 2.97 | PASS |
| B01 | 22 | 9.62 | 2.29 | PASS |
| B02 | 74 | 22.95 | 3.23 | PASS |
| B03 | 103 | 36.54 | 2.82 | PASS |
| B04 | 47 | 14.53 | 3.23 | PASS |
| B05 | 83 | 27.09 | 3.06 | PASS |
| B06 | 101 | 32.06 | 3.15 | PASS |
| B07 | 98 | 33.22 | 2.95 | PASS |
| B08 | 54 | 18.09 | 2.98 | PASS |
| **B09** | **120** | **34.58** | **3.47** | **LOG — over 3.4 ceiling; narration locked** |
| B10 | 12 | 4.63 | 2.59 | PASS |

**B09 is 0.07 WPS over ceiling.** Narration is locked (rebuild contract). Flagged for human review but does not block build.

---

## Check 11 — type_check.py

See TYPECHECK.md (run below).

---

## Executive summary note (informational)

B01 is Beat 2 in the sequence. It poses a question ("The question: how does a single agent coordinate...") rather than a full BLUF. EXECUTIVE-SUMMARY LAW strictly requires "states the WHOLE idea in one breath." The narration is locked; this cannot be changed in a rebuild. Flagged for future fresh build. Does not block this rebuild.
