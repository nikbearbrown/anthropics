# CONVERT-LOG — claude-plugins-official--claude-liam-skill-development

Source: `beat_sheet.json` (Plain register, hai-simple, 7 beats)
Output: `beat_sheet.nbb.json` (Teardown register, NikBearBrown, 7 beats)

## What changed

**Register rewrite (every beat, `narration_text` only):**
- **B00** — Reframed the cold-open premise in Teardown ("Wrong model. A Skill is a text file Claude reads and acts on. No compiler, no runtime beneath it."). Facts preserved; the on-screen BrutalistHesitantWriter text/trigger (`code` → `write`) unchanged.
- **NB01** — Explains the machinery ("A skill is a folder Claude reads before it works…"), then names the design choice ("the instructions and the executable are the same object"). All facts preserved verbatim: skill-development, SKILL.md, ~22 KB, references folder, plain English, no hidden runtime.
- **NB02** — Names the mechanism as legibility over compiled predicate: "the trigger is human-readable text, not a compiled predicate. You can audit exactly when the skill fires by reading English." Full list of applications (create/add-to-plugin/write-new/improve/organize/get-guidance) preserved verbatim; Steps-in-order rule preserved.
- **NB03** — Kept the repeatability-vs-no-fallback trade-off and added the design-critic line: "They optimized for auditability at the expense of graceful degradation."
- **BCRY** — Tightened the carry-out sentence; the `WantQuote` on-screen quote updated to match narration (was already Teardown-aligned; kept `sparkLine`: "The file is the program.").

**Structural changes (Steps 3–4 of nbb SKILL.md):**
- **BHTF** — Converted the source "your turn handoff" into the LLM EXERCISE beat (second-to-last). Added the `llm_exercise` block (`prompt` + `dig_deeper`), reworded narration to open with "Paste this into Claude, ChatGPT, or Gemini" and end with "Go deeper: …". Kept `ClaudeComposerAsk` as the render (per nbb Ask/intro scene rule), updated `command` + `runningText` to match the new paste-anywhere prompt. Prompt subject: writing your first Claude Skill for a real workflow (customer-support email replies) — designed to produce a useful `SKILL.md` draft on its own without the video. Dig-deeper pushes the viewer to find silent-failure phrasings without adding hidden fallback logic (echoes NB03's carry-out).
- **BOUT** — Swapped `OutroSeries` → `OutroCTA` (matches sibling nbb-* pattern in this book, e.g. `nbb-books--claude-liam-building-plugins`); handle `@HumanitariansAI` (per metadata `channel_title`), line: "The File Is the Program — the skill-development skill. Liam, in for Bear."

**Metadata:**
- Removed `_variant_todo`.
- Left `engine`, `voice_kokoro`, `palette`, `typography`, `audience`, `register`, `derived_from`, `outro_source` exactly as the scaffold set them (do-not-rescaffold rule).
- Updated `purpose` register tag from "Plain" → "Teardown".
- Left `style_preset: "humanitarians"` and `ground: "#F3EBDD"` untouched (scaffold-preserved legacy fields; palette is `teardown` and downstream reads from that).
- Updated each beat's `estimated_duration_s` to reflect new narration length (~2.5 words/sec Kokoro). Stripped `actual_duration_s` (stale — audio will regenerate). Left `audio_file` + `build` blocks intact (audio regen will overwrite).

## Judgement calls

1. **BHTF repurposed rather than inserted.** The source's B_HTF was already a paste-into-Claude handoff second-to-last; the sibling `nbb-books--claude-liam-building-plugins` reel repurposed the same slot into the LLM EXERCISE rather than inserting an extra beat. Same pattern here — keeps the ending sequence body → LLM exercise → outro and preserves the beat_id.

2. **On-screen quote (BCRY) updated to match narration.** SKILL.md says preserve on-screen card copy "that still fits the register". The quote and narration are the same sentence read aloud; letting them drift felt worse than tuning the on-screen quote to match. Preserved the `sparkLine` unchanged.

3. **Outro handle: `@HumanitariansAI`, not `@NikBearBrown`.** The metadata sets `channel_title: "@HumanitariansAI"` and the completed sibling reel in this book uses the same. Followed sibling.

4. **Ground / style_preset left alone.** These are scaffold-preserved legacy fields carried over from the source (`humanitarians`, `#F3EBDD`). The active palette is `teardown` and downstream renderers read from that; touching the legacy fields risked breaking the "do not re-scaffold" rule.

## Gate status

- JSON valid: yes
- Every beat narration rewritten: yes (7/7)
- LLM exercise second-to-last with `llm_exercise` block: yes (BHTF)
- NikBearBrown outro last: yes (BOUT, OutroCTA)
- `_variant_todo` removed: yes
- Not rendered (per invocation rules): correct — no audio, no compile, no render
