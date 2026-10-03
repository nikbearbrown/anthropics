# CONVERT-LOG — financial-services--claude-liam-catalyst-calendar

Source register: **Plain** (per source `metadata.register`; scaffold defaulted to Teardown).
Target register: **Teardown** (Feynman × MKBHD).
Voice: Kokoro `am_onyx` — Liam, in for Bear. Untouched by this pass.

## What changed

- Removed `_variant_todo` from metadata.
- Rewrote every `narration_text` in the Teardown register. Facts unchanged: catalyst-calendar is a folder containing a SKILL.md; Claude reads the file, executes the Steps section linearly with no branching unless a step says so; scope is earnings dates, conferences, product launches, regulatory decisions, macro events; same universe → same calendar every run; nothing outside the page appears.
- **B00**: added Liam's in-for-Bear cold-open beat (IN-FOR-BEAR LAW). "Here's what's actually happening" replaces the softer "Someone might ask" opener.
- **B01, B02, B03**: rewritten in Teardown — explain the machinery, name the trade the design makes (transparency over concealment; reproducibility over cleverness; scope-of-the-page over open-ended coverage). No new facts. On-screen `SkillTeardown*` card copy kept intact — it already matches the register.
- **BCRY**: carry-out sentence preserved verbatim (it's already a Teardown-shaped "X isn't Y; it's Z" line and it's the on-screen quote card).
- **BHTF**: converted from "your turn handoff" → **LLM EXERCISE** beat (per SKILL.md §Step 3). Added `llm_exercise: { prompt, dig_deeper }`; narration includes the "Go deeper:" follow-up; rewrote the `ClaudeComposerAsk.command` prop to mirror the paste-ready prompt (three-step SKILL.md → walk the steps → run against five public U.S. tech companies) so on-screen composer and pasteable prompt agree. Second-to-last position preserved. Kept `folderLabel = @HumanitariansAI` on this body beat's composer chip (SKILL.md is explicit only about the *outro* handle changing; sibling nbb sheets in this book do the same).
- **BOUT**: swapped `OutroSeries` → `OutroCTA` with `handle = "@NikBearBrown"` and `line = "Claude, Catalyst Calendar. Liam, in for Bear. www.brutalist.art"`. Narration now reads the URL aloud ("Brutalist dot art.").

## Judgement calls

- **Preserved on-screen card copy** on B00 (hesitant-writer text + trigger/replacement), B01, B02, B03 and BCRY. The card copy was already register-neutral or Teardown-shaped; changing it would drift from the audio without adding meaning. Only narration and outro chrome moved.
- **Preserved `estimated_duration_s` shape, bumped where it lied by more than ~2s**. Audio measured by `generate_audio_kokoro.py` is the master clock; estimates are planning hints. Bumps: B00 14→17, B01 15→22, B02 10→15, B03 21→25, BHTF 21→33 (added dig-deeper), BOUT 4→6 (added URL clause). BCRY unchanged.
- **BHTF `estimated_duration_s` 21 → 33** — the paste-ready prompt + dig-deeper materially lengthens the read.
- **`metadata.register`** flipped `Plain` → `Teardown`. Kept `source_register: "Plain"` as provenance so a later pass can see what was converted from.
- **`carry_out` field kept.** It matches BCRY narration verbatim and is a useful summary marker in metadata.

## Ending order (verified)

```
B00  hesitant writer cold open
B01  anatomy
B02  pipeline
B03  mechanism + scope
BCRY carry-out
BHTF LLM EXERCISE            ← second-to-last
BOUT outro (NikBearBrown)    ← last
```

## Not done (out of scope)

- No audio regenerated. No render. No compile. Downstream `generate_audio_kokoro.py` + `compile.py` still needs to run.
