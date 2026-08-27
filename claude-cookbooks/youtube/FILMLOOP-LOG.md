# FILMLOOP-LOG — anthropics/claude-cookbooks

---

## claude-liam-cookbook-audit · 2026-08-25

**Slug:** claude-liam-cookbook-audit  
**Duration:** 70.3s  
**Cut:** review slate (`claude-liam-cookbook-audit-slate.mp4`)  
**Beats:** 6 (B00, B01, B02, B03, BHTF, BOUT)

### Checks fixed
- Truncations (text repairs): B03 narration, BHTF narration, BHTF command prop — all ended mid-sentence; restored from skill description context
- Spark lines: B01 "The file is the program." (5w) → "File is the program." (4w); B03 "This is the part worth knowing." (6w) → "Spec defines the limit." (4w)
- Verdict STRIPPED: BVDT removed — body 3 beats / ~119 words below 5-beat / 180-word threshold; lines 3–4 generic-to-any-skill-teardown; line 2 truncated
- B01 ONE-TERRACOTTA: 3 × `accent: true` → only SKILL.md `accent: true`
- B03 canvas fill: added `verdictLabel: "REPEATABLE · SPEC-BOUND"`, `verdictPositive: false` to SkillTeardownMechanism
- B03 GATE T §8.5: body 18 words → 9 words ("Audit a Cookbook notebook against Anthropic's rubric.")
- Audio regenerated: B03 (truncation repaired), BHTF (truncation repaired)

### Punts authored
0

### Verdict
STRIPPED (thin-body rule: 3 beats / ~119 words)

### Gate V
PASS — B01 MINOR (right-half canvas fill; SkillTeardownAnatomy component layout constraint; logged in `_qc/REPORT.md`; not blocking)

### build.status Counter
Counter({'VIDEO': 6})

### mtime check
beat_sheet.json=1787714147 · slate.mp4=1787714149 · PASS (cut newer than sheet)

---

## claude-liam-applying-brand-guidelines — 2026-08-25

**Duration:** 70.2s · **Beats:** 6 (B00 B01 B02 B03 BHTF BOUT)

**Checks fixed:**
- B03 sparkLine 6-word → "Scope is the tell." (4 words)
- B03 narration rewritten: Plato + Popper lens moves added (artifact/world/validate_brand.py as falsifier)
- B03 body shortened 13 → 8 words to pass §8.5 (GATE T)
- BVDT stripped: 3-beat / 97-word body, below 5/180 threshold; also had truncated on-screen text
- BHTF narration + command: garbled truncation bug fixed ("all ge" / "all generated do")
- B00 output prop: truncated "all generated do" → "all generated documents"
- BOUT subline removed (OUTRO-LOCK: no subline on claude-liam reels)
- B03 and BHTF audio regenerated after narration changes

**Punts authored:** 0 (no punts found)

**Verdict:** STRIPPED (thin body — 3 beats / 97 words < 5/180 threshold)

**Gate V:** Zero BLOCKER, Zero MAJOR on content (SkillTeardown component canvas-fill downgraded — component layout constraint, not fixable via props without §8.5 violation). TEMPLATE-MISSES note logged for SkillTeardown family.

**Audio:** mean_volume -23.9 dB ✓

**Timestamp:** beat_sheet.json 23:36:26 < slate.mp4 23:36:29 ✓

**Output:** `claude-liam-applying-brand-guidelines-slate.mp4`
