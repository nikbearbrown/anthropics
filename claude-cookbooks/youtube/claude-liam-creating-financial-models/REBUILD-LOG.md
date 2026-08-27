# REBUILD-LOG — claude-liam-creating-financial-models

Rebuild run: 2026-08-25
Pre-rebuild backup: beat_sheet.pre-rebuild.json (byte-exact)

---

## LOCKED (carried verbatim)

- B00, B01, B02, BOUT narration_text — unchanged
- Beat order and act labels — unchanged
- B03 act, shot patterns, props (except sparkLine fix below)
- Metadata identity: title, slug, topic, source pointer, register, channel

---

## REBUILT / FIXED

### 1. B03 sparkLine — PHASE 1 Check 3 (spark line too long)

- **Old:** `"This is the part worth knowing."` (6 words — violates ≤4 word limit)
- **New:** `"Spec is the limit."` (4 words — compressed from the beat's own "What it bites: anything outside the spec.")
- Reason: SPARK-LINE LAW, inner beats ≤4 words

### 2. B03 narration_text — corrupted generation artifact (text truncation)

- **Old fragment:** `"...sensitivity testing, Mon. What it gets right..."` — "Mon" is a corrupted truncation of "Monte Carlo simulations"
- **New fragment:** `"...sensitivity testing, Monte Carlo simulations. What it gets right..."` — complete sentence
- Source: The skill description is "...DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions" (verified against source_skill SKILL.md)
- Not a datable claim; a generation error (auto-generator hit a character limit, yielded garbled text). Logged here per rebuild contract.

### 3. BVDT beat — STRIPPED (Phase 1 Check 4: thin body)

- Body beats: B01 + B02 + B03 = 3 beats, ~119 words
- Threshold: 5+ beats AND 180+ words required for a verdict
- Verdict was thin AND contained two generic lines true of any skill teardown:
  - `"Same input → same output, every run"` — true of any skill
  - `"Limit: only what the SKILL.md specifies"` — true of any skill
  - Line 2 was also a truncated sentence ("sensitivity te...")
- Action: BVDT beat removed from beats array; metadata.build.filled/of updated to 6/6
- Rule: "A placeholder verdict is worse than no verdict." BVDT absent is legal per Phase 1 Check 2.

### 4. BHTF narration_text and command prop — CLOSING BLOCK REWRITE

The original BHTF was corrupted (broken command text, truncated narration):
- **Old command prop:** `"I want to this skill provides an advanced financial modeling suite with dcf anal. Read the creating-financial-models skill and walk me through what you will do before you do it."` — broken grammar, truncated
- **Old narration fragment:** `"'I want to this skill provides an advanced financial modeling suite with dcf analysis, sens."` — incoherent

The closing block is rewritable per rebuild contract ("new close narration from sheet content").
- **New command:** `"I want to stress-test a five-year revenue projection. Read the creating-financial-models skill and walk me through what you will build before you touch a number."`
- **New narration:** Reads the command aloud verbatim, then discusses the key clause ("before you touch a number") and why it surfaces the planning assumptions. The "walk me through first" pattern was the locked original intent — preserved, expressed coherently.
- Logged here. Audio regeneration required for this beat.

### 5. B03 body prop — GATE T de-wordify (§8.5 no-wordy-card)

- **Old:** `"This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions"` (22 words — fails §8.5 pull-quote limit ≤12)
- **New:** `"DCF analysis · sensitivity testing · Monte Carlo · scenario planning"` (10 words — passes §8.5)
- Reason: SkillTeardownMechanism renders `body` at fontSize 38; a 22-word sentence fills the frame with prose instead of a scannable capability list. The de-wordified version names the same four capabilities as structured items, not a sentence.

---

## Audio to regenerate

- B03: narration changed (truncation fix → longer by ~6 words)
- BHTF: narration completely rewritten (closing block rewrite)
- All other beats: existing mp3s valid, no regeneration needed

---

## Fields dropped (dead ElevenLabs era)

None found — the original sheet had no voice_id, voice_env, or ElevenLabs clock prose.

---

## Pacing flags (logged, not silently retimed)

- B02: ~29 words / 7.83s = 3.71 wps — over 3.4 ceiling. Beat is short. Audio not changed.
- BOUT: ~8 words / 4.12s = 1.94 wps — just under 2.0 floor. Outro, near-boundary. Audio not changed.
