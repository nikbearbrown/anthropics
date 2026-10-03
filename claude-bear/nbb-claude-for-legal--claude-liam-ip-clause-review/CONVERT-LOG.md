# CONVERT-LOG — nbb-claude-for-legal--claude-liam-ip-clause-review

Source: `../claude-for-legal--claude-liam-ip-clause-review/beat_sheet.json`
Converted: 2026-09-03

## What changed

- Rewrote all 5 body-beat narrations (B00, NB01, NB02, NB03, BCRY) in the
  Teardown register. Explained the machinery (Skill = folder + one plain-English
  file; Steps section = numbered list run top to bottom, no branching; ownership
  check = license vs. assignment). Named the design choice at each step (text
  you can read is text you can audit; repeatability comes from same-list-same-run;
  the check exists because warm English can hide the ownership gap).
- Facts unchanged: skill name (`ip-clause-review`), single-file design
  (`SKILL.md`), Steps-section semantics, the "all right, title, and interest,
  transferred" formulation, and the license-vs-assignment distinction all
  survive verbatim from source.
- Replaced BHTF from a CLI-style "paste this into Claude" prompt to a proper
  **LLM EXERCISE** beat (act renamed to `LLM EXERCISE`; `llm_exercise` block
  added with `prompt` + `dig_deeper`). The prompt is paste-ready for any
  frontier LLM (Claude / ChatGPT / Gemini) and produces useful output without
  the video: viewer pastes an actual IP clause, model walks through
  assignment-vs-license, practical ownership consequence, and any ambiguous
  phrase. Dig-deeper flips the exercise: ask the model to write three clauses
  that read like transfers but aren't, and name the tell.
- Replaced BOUT scene from `OutroSeries` to `OutroCTA` to match the
  completed-nbb reference pattern (`nbb-books--claude-liam-building-plugins`).
  New line: "Claude, Ip Clause Review — assignment, not license. Liam, in for
  Bear." Handle stays `@HumanitariansAI` (source-channel convention — matches
  the reference reels in this book).
- Removed `_variant_todo` from metadata.
- Bumped `estimated_duration_s` on the beats that grew (NB01 14→18, NB02 13→17,
  NB03 18→22, BCRY 9→11, BHTF 20→55, BOUT 6→7) — Kokoro will re-measure at
  audio time; these are hints only.

## Judgement calls

- **B00 word budget.** The BrutalistHesitantWriter TIMING LAW says 20–35 words.
  Source was 39; my rewrite is 30. Under-limit end preserves the "judging →
  checking a list" correction moment; the writer's `text`, `triggerWords`, and
  `replacementWords` props are untouched.
- **BCRY quote = narration.** The `WantQuote.quote` prop must match the spoken
  line exactly (matches the plugins-reference pattern), so I kept both to the
  same rewritten sentence rather than splitting them.
- **Handle stayed `@HumanitariansAI`** rather than switching to `@NikBearBrown`
  — matched the completed nbb reference in this book, which keeps the source
  channel on OutroCTA even after Teardown-register conversion. If the intent is
  a NikBearBrown channel post, the human can flip `handle` at post-time.
- **LLM prompt subject.** The source video's whole subject is the
  `ip-clause-review` skill and its assignment-vs-license check. I built the LLM
  exercise around that same check applied by any frontier LLM — no Skill file
  required — so the exercise stands on its own and reinforces the video's
  carry-out.

Done. Not rendered, not compiled, no audio generated. Next pass:
`generate_audio_kokoro.py` → compile.
