# CONVERT-LOG — nbb-claude-code--claude-liam-agent-development

Register conversion Plain → Teardown. Facts unchanged; voice, LLM-exercise beat, and outro placement adjusted per `skills/make/nbb/SKILL.md`.

## Beats rewritten (all narration_text)

- **B00** — Kept ~35 words to honor the NOTE's TIMING LAW (writer window ≥9s). Added the "Here's what's actually happening" framing implied by Teardown; unchanged fact chain (command fires once when typed → agent keeps going on its own → one file builds it).
- **B01** — Same five frontmatter fields, same "leave tools out → every tool" fact. Reframed the tools field as a **trade-off worth naming** (Teardown: "blast radius on purpose") instead of a neutral spec.
- **B02** — Same trigger pattern, same 4-part example shape, same "skip examples → nothing to match" outcome. Added the design-critic line that Claude "isn't reading your intent, it's matching against those examples" and named the concrete failure mode: the agent exists in the folder but never fires.
- **B03** — Same precise/open axis and same 5-section body list. Closed with the design-philosophy line "they optimized for lock-down at the frontier and judgment in the interior" — a straight Teardown move.
- **BCRY** — Left the carry-out sentence and the WantQuote prop identical. It's already terse, one-clause, and honest about the mechanism; a rewrite would only weaken the anchor.
- **BHTF** — Same paste-line and same 4 checks, in the same order. Named the failure mode explicitly at the tail ("won't behave like an agent; it'll behave like a broken command") so the checks read as a design gate rather than a checklist.
- **BOUT** — Left identical. Title + "Liam, in for Bear" is the standard NBB sign-off (IN-FOR-BEAR LAW); the reference nbb-cwc-workshops sheet uses the same shape.

## Beat inserted (SKILL.md Step 3)

- **B_LLM** — new beat between BHTF and BOUT. `llm_exercise.prompt` gives any frontier LLM the full agent-file spec from the video (single markdown file, YAML fields, "Use this agent when" + 4-part examples, 5-section body in 2nd person) and asks it to draft the exact worked example the video plants: a Python security reviewer. `dig_deeper` asks how to split that single reviewer into finder + fixer agents and what handoff each body would carry. Shot type = CARD per the SKILL.md schema.

## Judgment calls

- **Kept BHTF; did not fold it into B_LLM.** BHTF is a "your turn" paste into a live Claude Code session — a CLI-agent design-gate exercise. B_LLM is a paste into any frontier LLM chat surface — no CLI, produces a useful output on its own. Different surfaces, different exercises; folding them would collapse the CLI-vs-frontier distinction the video's whole subject cares about. SKILL.md says "insert one beat before the outro," not "replace BHTF." Order is now B00→B01→B02→B03→BCRY→BHTF→B_LLM→BOUT.
- **Left the WantQuote prop text on BCRY unchanged.** Preserved on-screen card copy that still fits the register (SKILL.md permits this and the reference nbb sheets do the same).
- **Kept @HumanitariansAI in BOUT's OutroCTA handle.** Matches the reference nbb-cwc-workshops conversion; the metadata channel_title/folderLabel were already @HumanitariansAI in the scaffold and I did not have authority to retarget the channel. If the NikBearBrown outro is meant to point at @NikBearBrown / brutalist.art, that's a scaffold change to make upstream.
- **Left all GRAPHIC production_viz labels/chips/captions and Remotion prop text unchanged.** They already read as Teardown (short, mechanical, no soft hedges).
