# REBUILD-LOG — claude-liam-applying-brand-guidelines

**Rebuild date:** 2026-08-25
**Film factory invocation:** unattended single-reel pass

---

## LOCKED (carried verbatim)

- B00, B01, B02 narration_text — unchanged
- Beat order (B00 → B01 → B02 → B03 → BHTF → BOUT)
- Act labels (cold open, anatomy, pipeline, design tell, handoff, outro)
- Shot intent per beat (patterns preserved: ClaudeComposerAsk, SkillTeardownAnatomy, SkillTeardownPipeline, SkillTeardownMechanism, ClaudeComposerAsk, ClaudeTitleOutro)

---

## REBUILT / CHANGED

### 1. B00 — output prop fix (content bug, not narration)

**Old:** `"This skill applies consistent corporate branding and styling to all generated do"`
**New:** `"This skill applies brand guidelines to all generated documents"`
**Reason:** Truncated text visible on screen ("all generated do"). Props may be re-shaped; shot intent preserved.

---

### 2. B03 — narration rewrite (Phase 1 authorized: lens audit fix)

**Old narration:** "Here is the design tell. These guidelines apply to all external communications. That is the interesting constraint in applying-brand-guidelines — a deliberate trade-off baked into the instruction set."

**New narration:** "Here is the design tell. Artifact: the branded document. World: actual brand consistency. SKILL.md bridges them. Scope is external communications only — that is the constraint. validate_brand.py is the falsifier: wrong colors, wrong fonts, wrong scope."

**Why:** Lens audit (Check 8) requires ≥2 moves from {Descartes, Hume, Popper, Plato}. The original ran zero. New narration adds:
- **Plato**: artifact (branded document) / world (brand consistency) / relationship (SKILL.md bridges them)
- **Popper**: validate_brand.py named as falsifier; failure modes enumerated

**Source:** SKILL.md for applying-brand-guidelines confirms validate_brand.py exists and checks colors, fonts, and scope.

### 3. B03 — sparkLine fix (Check 3: must be ≤4 words)

**Old:** `"This is the part worth knowing."` (6 words)
**New:** `"Scope is the tell."` (4 words)

### 4. B03 — props.body update (matches new narration content)

**Old:** `"These guidelines apply to all external communications"`
**New:** `"Artifact: document. World: brand. validate_brand.py is the falsifier."` (shortened to 8 words to pass §8.5 no-wordy-card limit of ≤12 words)

---

### 5. BVDT — stripped (Check 4: thin body)

Body: 3 beats / ~97 words (threshold: 5 beats / 180 words). Verdict beat stripped per film factory Check 4. The existing verdict also contained on-screen truncation bug: "This skill applies consistent corporate branding and styling to all generated documents in" (cut off mid-sentence). Absent BVDT is legal per Check 2 amendment.

---

### 6. BHTF — narration fix (content bug: truncated inline quote)

**Old narration:** "Your turn. Paste this into Claude: 'I want to this skill applies consistent corporate branding and styling to all generated do. Read the applying-brand-guidelines skill and walk me through what you will do before you do it.' That clause matters — explaining first surfaces the real constraint logic."

**New narration:** "Your turn. Paste this into Claude: 'I want to apply brand guidelines to my team's documents. Read the applying-brand-guidelines skill and walk me through what you will do before you do it.' That clause matters — explaining first surfaces the real constraint logic."

**Reason:** Original contained garbled/truncated text ("all generated do", "I want to this skill applies"). The handoff intent is preserved: ask Claude to apply the skill and explain before acting.

### 7. BHTF — command prop fix (content bug: same truncation)

**Old:** `"I want to this skill applies consistent corporate branding and styling to all ge. Read the applying-brand-guidelines skill and walk me through what you will do before you do it."`
**New:** `"I want to apply brand guidelines to my team's documents. Read the applying-brand-guidelines skill and walk me through what you will do before you do it."`

---

### 8. BOUT — subline removed (OUTRO-LOCK compliance)

**Old:** `"subline": "applying-brand-guidelines · Anthropic Skills"`
**New:** (field removed)
**Reason:** OUTRO-LOCK: claude-liam reels carry NO subline on the @NikBearBrown outro card.

---

## Audio regenerated

- `mp3/beat-B03.mp3` — deleted; regen required (narration changed)
- `mp3/beat-BHTF.mp3` — deleted; regen required (narration changed)
- `mp3/beat-BVDT.mp3` — deleted (beat stripped)
- All other beats: existing audio unchanged
