# CONVERT-LOG — nbb-healthcare--claude-liam-fhir-developer-skill

Converted from `../healthcare--claude-liam-fhir-developer-skill/beat_sheet.json`.

## Metadata

- Register: `Plain` → `Teardown`.
- Palette: `humanitarians` → `teardown`; `ground` `#F3EBDD` → `#FFFFFF`;
  `style_preset` `humanitarians` → `teardown`.
- Channel surface: `folderLabel` and `channel_title` `@HumanitariansAI` → `@NikBearBrown`.
- `purpose` rewritten to name the Teardown trade-off (interoperability at the
  expense of coverage — anything outside the FHIR spec's code vocabulary,
  the skill won't validate at all).
- `_variant_todo` removed.
- `audience`, `engine`, `voice_kokoro`, `outro_source`, `derived_from`, and
  `typography` untouched (scaffold-set by `brand_variant.py`).

## Palette swap in shot props

- B00 `BrutalistHesitantWriter` — `ink`/`accent`/`bg` retinted to teardown
  (`#2A1A0E` / `#C8102E` / `#FFFFFF`). `seed` renamed from
  `hai-fhir-developer-skill` → `nbb-fhir-developer-skill` so the RNG jitter
  differs from the HAI sibling. Trigger/replacement words unchanged
  (`pass-fail` → `the exact code`).
- NB01–NB03 Manim `production_viz.colors` retinted teardown
  (`#FFFFFF`, `#2A1A0E`, `#C8102E`). Chip labels, arrows, accent indices,
  captions, `manim` scene class names all preserved verbatim so the same
  `BKNB0*Scene` classes render in the new palette.
- BHTF `ClaudeComposerAsk.folderLabel` `@HumanitariansAI` → `@NikBearBrown`.

## Narration — every beat rewritten in Teardown

Same six existing beats plus a new second-to-last LLM-exercise beat and a
retooled outro. **Facts unchanged**: three-item folder (SKILL.md + references
+ scripts), three-step pipeline (read / execute / return), 422 for
invalid-enum, 412 for ETag mismatch on a conditional update, "same input, same
code, every run." Register only.

- **B00 (cold open)** — added the IN-FOR-BEAR LAW opening ("Liam here, in for
  Bear. Take this Claude skill apart."). The lead question now foregrounds the
  design contrast ("just tell you a FHIR request failed" vs. "name the exact
  code the spec already assigns for that class of problem") instead of the
  Plain-register "does Claude return the exact code" phrasing.
- **NB01 (folder)** — Teardown framing ("Here's what the skill actually is…
  Nothing hidden, nothing to reverse-engineer. The file is the program.").
  Explicitly names the design choice: no hidden logic.
- **NB02 (pipeline)** — Names the trade-off out loud: "That linearity is the
  design choice — deterministic and inspectable, at the expense of any clever
  runtime routing." Same three steps, same wording of the branching escape
  hatch.
- **NB03 (status code is the spec)** — Adds the design-critic lens ("it
  doesn't paraphrase the problem, it names the problem in the vocabulary the
  FHIR ecosystem already speaks") and the sacrifice ("They optimized for
  interoperability at the expense of coverage: anything outside that spec, it
  won't validate at all"). 422/412 examples preserved verbatim, including the
  "invalid enum value" and "ETag mismatch on a conditional update" specifics.
- **BCRY (carry-out)** — Kept the source carry-out claim intact and added the
  trade-off tag ("Interoperable to a fault, and silent on anything the spec
  doesn't cover.") so BCRY compresses both the win and the cost. `WantQuote`
  `sparkLine` "Not pass-fail. The exact code." preserved.
- **BHTF (now LLM EXERCISE)** — Recast the "your turn handoff" beat as the
  Teardown LLM-exercise slot required by nbb SKILL.md §Step 3. `act` field
  changed from `your turn handoff` → `LLM EXERCISE`. Added the required
  `llm_exercise` object with (a) a paste-ready `prompt` that instructs the
  LLM to write a short FHIR-DEVELOPER SKILL.md, draft three test resources
  (clean / bad-enum / stale-ETag on a conditional PUT), and run the skill —
  producing useful output on its own without the video — and (b) a
  `dig_deeper` that pushes the viewer to a genuine follow-up test
  (business-rule violation with no assigned status code — does the skill
  refuse or invent a code?). Narration ends with "Go deeper: …" as spec'd.
  `ClaudeComposerAsk.command` shortened to fit the composer card while
  preserving every 422/412/If-Match specific.
- **BOUT (outro)** — Swapped the `OutroSeries` pattern for `OutroCTA` to match
  the NikBearBrown sibling outros (`nbb-…-clinical-note-extract-skill`
  precedent). Content sourced from `../youtube/ai-1/AUTHOR.MD :: NikBearBrown`
  — handle `@NikBearBrown`. Signoff includes the IN-FOR-BEAR LAW line ("Liam,
  in for Bear."). Line was extended to fold in the design verdict ("in the
  vocabulary the FHIR spec already speaks. Interoperable to a fault.") so the
  outro doubles as the last recap of the trade-off. Estimated duration nudged
  6→10 s to fit the longer line.

## Judgement calls

- **Outro pattern swap (`OutroSeries` → `OutroCTA`).** The scaffold inherited
  the source's `OutroSeries` with `eyebrow`/`line`, but every rendered
  NBB-cut sibling in this book (verified against
  `nbb-healthcare--claude-liam-clinical-note-extract-skill/beat_sheet.nbb.json`)
  uses `OutroCTA` with `line`/`handle`. Followed the sibling for consistency
  in the NBB channel.
- **Estimated durations bumped** to match the longer Teardown narration on
  NB01 (17→21 s), NB02 (15→19 s), NB03 (20→32 s), BCRY (9→14 s), BHTF (24→40
  s), BOUT (6→10 s). These are estimates only — `generate_audio_kokoro.py`
  will write the real `actual_duration_s` on the next audio pass. `B00` bumped
  only 14→15 s to stay inside the BrutalistHesitantWriter TIMING LAW window.
- **B00 `seed`** deliberately renamed (`hai-…` → `nbb-…`) so the
  RNG-driven mistake/jitter timing is distinct from the HAI cut; would
  otherwise inherit an identical typing pattern rendered against a different
  palette, which reads as a bug.
- **Carry-out** kept the source sentence intact rather than rewriting from
  scratch — it was already the load-bearing claim of the reel and any
  Teardown flourish would weaken the compression. Added a second short
  sentence for the trade-off tag instead.
- **LLM exercise topic** stayed on FHIR validation (the reel's actual
  subject) rather than pivoting to a more general "status codes as spec"
  exercise; the paste-ready prompt has to produce something useful on its
  own, and a concrete FHIR validator is a sharper standalone artifact than
  an abstract discussion of HTTP status codes.

## Not done (per supervisor instructions)

No audio regenerated, no scenes rendered, no compile. The scaffold is ready
for `runtime/scripts/generate_audio_kokoro.py` → Manim/Remotion render →
`compile.py` on a later pass.
