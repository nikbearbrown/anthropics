# CONVERT-LOG — nbb cut of claude-for-legal--claude-liam-demand-received

Converted `beat_sheet.nbb.json` from the scaffold (Plain register) to the NikBearBrown / Teardown cut. Source `beat_sheet.json` untouched.

## What changed

- **Every `narration_text` rewritten in the Teardown register** (Feynman × MKBHD). B00 reframes the misconception as a design-mechanism reveal ("It runs a triage — extract, cross-check, assess, recommend — and only then decides who touches the response"). NB01 adds the design-choice line: "They optimized for read-and-edit-by-a-lawyer over anything you couldn't audit." NB02 names the trade explicitly: "predictable over clever … you give up on the tricks the model might have reached for on its own." NB03 renames the pipeline's output — "a decision about who touches this thing next, not the response itself." BCRY sharpens the carry-out: "the judgment lives in the checklist; Claude is just doing what the checklist said." All facts preserved (five-stage pipeline, hand-off to matter-intake / demand-intake, SKILL.md as the program, linear-Steps default). Word counts and `estimated_duration_s` bumped where narration lengthened; timings will be reset by the audio pass.
- **BCRY on-screen quote** updated to match the new register (kept the same content, just the tighter phrasing). `sparkLine` "Escalation hands off. Not Claude's call." left as-is — it already fits the register.
- **B00 hesitant-writer props** untouched — `triggerWords: "reply"` → `replacementWords: "triage it"` still lands from the rewritten opener ("does Claude just reply?" → "does it just triage it?").
- **BHTF → LLM EXERCISE.** The old "paste this into Claude" prompt required the demand-received Skill installed. Rewrote it as a standalone paste-ready prompt that works in any frontier LLM without the plugin: gives the model the five-step frame and asks it to run the triage itself. Added the `llm_exercise` object with `prompt` and `dig_deeper`. `runningText` broadened from "paste this into Claude…" to "paste this into Claude, ChatGPT, or Gemini…" per sibling pattern. `act` renamed from "your turn handoff" to "LLM EXERCISE".
- **BOUT switched from `OutroSeries` → `OutroCTA`** per the marketing/sales/installing-plugins sibling pattern: `handle: "@NikBearBrown"`, `line` and narration extended to "Claude, Demand Received — the demand-received Skill, taken apart. Liam, in for Bear. More reels at brutalist.art." Duration bumped 6→9s.
- **`_variant_todo` removed** from metadata. Metadata `purpose` rewritten to describe the Teardown carry-out (mechanism + design choice + trade-off), not the Plain-register one.

## Judgement calls

- Kept `folderLabel: "@HumanitariansAI"` in the Claude composer (BHTF) — siblings do the same; the `@NikBearBrown` handle appears only in the outro CTA, matching precedent.
- Kept `style_preset: "humanitarians"` and `ground: "#F3EBDD"` from the scaffold; the palette field is already set to `teardown` where it counts, and stripping the HAI ground would collide with the BrutalistHesitantWriter's fixed `bg: "#F3EBDD"` prop on B00.
- Preserved every `beat_id`, every `graphic.production_viz.label`/`chips`/`caption`, and every `shot.remotion.pattern`. Only two card-copy strings changed: the BCRY quote (to track the tightened narration) and the NB02/NB03 captions (to carry the design-choice language: "predictable over clever", "the output is who touches it, not the reply").
- Did not touch `actual_duration_s` on any beat — the audio pass will overwrite those.
