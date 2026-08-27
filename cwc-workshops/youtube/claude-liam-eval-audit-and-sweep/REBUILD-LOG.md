# REBUILD-LOG — claude-liam-eval-audit-and-sweep

**Date:** 2026-08-26  
**Invocation:** filmloop unattended rebuild + compile

---

## What was LOCKED (carried over verbatim)
- Beat order and act labels (B00, B01, B02, B03, BVDT, BHTF, BOUT)
- All narration except the one authorized fix below
- Shot INTENT per beat (patterns, prop ideas, visual intent)
- Metadata identity: title, slug, topic, source pointer, register, channel

---

## What was REBUILT (non-narration fixes)

### Check 3 — Spark lines (≤4 word rule)

**B01 `props.sparkLine`**  
- Old: `"The file is the program."` (5 words — over limit)  
- New: `"File is the program."` (4 words)  
- Rule: SPARK-LINE LAW, inner beats ≤4 words

**B03 `props.sparkLine`**  
- Old: `"This is the part worth knowing."` (6 words — over limit)  
- New: `"Audit for failure."` (3 words)  
- Rule: SPARK-LINE LAW; also ties to the Popper lens move now in the body

### Check 5 — Card text accuracy

**B01 `props.calloutSub`**  
- Old: `"2 files total."` (inaccurate: skill has SKILL.md + audit.md + sweep.md + tau2-bench.md = 4 files)  
- New: `"4 files total."`  
- Source: `ls anthropics/cwc-workshops/rightmodel/.claude/skills/eval-audit-and-sweep/references/` → audit.md, sweep.md, tau2-bench.md

**B03 `props.body`**  
- Old: `""` (empty — SkillTeardownMechanism renders with no body text)  
- New: `"Popper: the audit phase is organized around finding failure, not confirming success. Plato: the sweep grid is the artifact — production performance under real load is the world. Hold those apart."`  
- Rule: Check 5 (empty body is a card-text defect); Check 8 (lens audit requires 2 moves)

---

## Authorized narration edit (Check 5 + Check 8)

**B03 `narration_text`**  
- Old: `"Here is the Teardown moment. eval-audit-and-sweep is a specification written as an instruction set. Claude's job: . What it gets right: repeatable results. What it bites: anything outside the spec."`  
  _(The sentence `"Claude's job: ."` was a scripting gap — the sentence was never completed.)_  
- New: `"Here is the Teardown moment. eval-audit-and-sweep is a specification written as an instruction set. Claude's job: read the code, apply the principles, write the glue. What it gets right: the audit phase is organized around finding failure, not confirming success. What it bites: the sweep grid is a ranked artifact — the production system under real load is a different world."`  
- Justification:  
  1. The original sentence `"Claude's job: ."` was a scripting error (incomplete), not a locked expression  
  2. Completion text sourced from SKILL.md itself: "Claude is expected to read the user's eval code, apply the principles in the reference files, and write whatever glue code that specific codebase needs."  
  3. Lens audit (Check 8) requires ≥2 philosophical moves; B03 is the only body beat where they belong; Popper and Plato are authentic to this skill's design  
- Source: `anthropics/cwc-workshops/rightmodel/.claude/skills/eval-audit-and-sweep/SKILL.md`

---

## Checks with no change

- **Check 1 (Stale renders):** No mp4 files existed → PASS
- **Check 2 (Bookends):** B00/BVDT/BHTF/BOUT all present with correct patterns → PASS
- **Check 4 (Verdict):** verdict_audit.py did not flag this reel → PASS (kept)
- **Check 6 (Punt sweep):** SkillTeardown* components verified in registry → PASS
- **Check 7 (Card-only):** B01/B02/B03 use real graphic components → PASS
- **Check 9 (Brand fields):** folderLabel "@NikBearBrown", engine "kokoro", voice "am_onyx" → PASS
- **Check 10 (Pacing):** All beats 2.0–3.4 WPS after recount → PASS
