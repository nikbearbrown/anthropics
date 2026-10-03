# BUILD-PROMPT — cc-claude-skills--claude-liam-skill-creator

Build a **cc-explainer** reel about the **Skill Creator** — specifically, the description-optimizer's inner loop done by hand at n = 6 so a viewer can see the mechanism instead of trusting it.

## Reel folder

`anthropics/claude-code-101/03-hooks-skills-commands/cc-claude-skills--claude-liam-skill-creator/`

## The concept, in one sentence

A skill's description is the one line the router reads to decide whether the skill fits. The instinct is to craft it; the correct move is to measure it — same folder, two descriptions, three asks each, count the fires.

## What the film shows

- **B00 cold open** — a fresh headless run with a nine-word description ("Helper for meeting notes.") — the router fires the skill on its own; four rows of `actions.md`, checker PASSes.
- **BIDEA** — the misconception: description is *crafted*. The correction: it is *measured*.
- **BDEFS** — five terms (skill, description, trigger, router, eval).
- **B01** — Liam's VERIFY on the vague run: grep the Skill event → 1; wc → 4; `check_actions.py` → PASS.
- **B02** — the two SKILL.md files compared: same body, different description (9 words vs 63).
- **B03** — the pushy-A1 run: same ask, same Skill() fire, same output shape.
- **B04** — the near-miss ask ("Summarize notes.txt for someone who missed the meeting.") — neither description fires; prose reply, no `actions.md`.
- **B05** — the six-cell tally grepped out of every run + `trigger-tally.txt`.
- **B06 CONDUCT** — Boondoggle Score: pick the ask, draft two descriptions, run the six sessions, read the null result honestly.
- **B07 HUMAN** — ledger: what only the human can do here (pick asks that would separate the descriptions; read the tally as it stands; call a null result a null result).
- **BVDT / BHTF / BOUT** — the your-turn closing block; the FALSIFIABLE line is "an ask on which one description fires and the other doesn't."

## Persona

Liam (in for Bear), Kokoro `am_onyx`, free. Cold open opens with "This is Liam, in for Bear."; outro closes with "Skill Creator. Liam, in for Bear." No Ada. No paid voice.

## Scenes

All from the CC kit and Claude bookends — none authored for this reel:

- `CCSession` (B00, B01, B03, B04) · `CCPlainShell` (B02, B05) · `CCDefinitions` (BDEFS) · `BrutalistHesitantWriter` (BIDEA) · `CCBoondoggleScore` (B06) · `CCHumanLedger` (B07) · `ClaudeVerdictArtifact` (BVDT) · `ClaudeComposerAsk` (BHTF) · `ClaudeTitleOutro` (BOUT).

## Publishing

**None.** Master stays in this reel folder. Bear decides staging via `post` on ask; TOPOST is the only surface the publisher will accept.
