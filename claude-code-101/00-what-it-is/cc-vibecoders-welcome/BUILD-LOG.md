# BUILD-LOG — cc-vibecoders-welcome

cc-explainer · Claude Code 101 · tier `00-what-it-is`, first in watch order ·
Liam, in for Bear (Kokoro `am_onyx`) on every beat — LIAM LAW · Teardown ·
16:9 · built 2026-09-08. **The first reel built with the `cc-explainer` skill.**

---

## What this reel is, and is not

The copied source concept — `claude-cowork--claude-liam-claude-code`,
"Vibecoders Welcome" — was a Liam-narrated card reel: two use cases, seven
setup steps, a DESIGN.md tip, a shadcn tip, four situations to skip Claude Code.
Good advice, none of it *shown*, and several lines datable (vendor names, plan
tiers, "bypass permissions in settings").

This reel keeps the concept — a person who does not write code builds a small
personal tool and decides whether it is right — and replaces the cards with a
**real session**. Everything on screen happened. The setup advice is stripped
(FACTCHECK → Stripped), not because it is wrong but because it cannot be
checked against a transcript, and a cc-explainer's whole claim is that its
body is a receipt.

## The session (REAL-SESSION LAW)

Run headless — `claude -p`, Claude Code 2.1.150 — in a fresh git repo with one
`README.md`, tools fenced to the repo (`Read, Write, Edit, Glob, Grep,
Bash(ls|cat|wc|grep)`), `--max-turns` bounded. Two turns, Liam's VERIFY
commands run by hand between them. Transcript: `SESSION.md`; raw stream-json,
both versions of `index.html`, and the correction diff: `evidence/`.

**Headless mode has no plan card.** Interactive Claude Code shows a plan box
in plan mode; `-p` does not. Claude's plan arrived as a sentence — *"I'll
create a single `index.html` with the form, a table of logged books,
localStorage persistence, and a delete option."* B01 shows that sentence as a
`text` block rather than a `CCPlanCard`. That is the honest render, and it is
better teaching than a card would have been: the unasked-for feature is
**announced in the plan**, and Liam's lesson is that she has to *listen to the
end of the sentence*. Recorded here so nobody "upgrades" B01 to a plan card
the session never produced.

**What the session gave the film for free.** Three things happened that no
author would have dared script:

1. Turn 1 added two features nobody asked for — a per-row `remove` button
   (announced) and a sort (not announced; it surfaces only in the post-hoc
   summary as "sorted newest-finished first"). One announced, one silent. The
   dangerous middle, twice, at two different visibility levels.
2. Turn 2 removed exactly both — 14 deletions, 0 additions, 1 file — and
   said "Nothing else touched."
3. Then, unasked, it wrote two files **outside the repo**:
   `~/.claude/projects/…/memory/feedback_scope_discipline.md` and
   `MEMORY.md` — auto-memory, working as designed, containing a description
   of the user ("They read the code before running it and expect the spec to
   match the request literally"). `git diff` cannot see it. "Nothing else
   touched" was true of the tree and false of the machine.

Item 3 is the Plato move of the SKEPTIC beat and the spine of the HUMAN beat.
It was not planned. It is why REAL-SESSION LAW exists.

## Persona decisions (overrulable — see SKILL.md)

- **Liam at the keyboard and on the closing block (LIAM LAW, re-narrated 2026-09-08)** —
  your-turn's existing body-voice / recap-voice split, so no new law. The
  handoff line is `Let's recap with Claude.` (LIAM LAW) Liam says "in for
  Bear" on the outro; IN-FOR-BEAR LAW holds.
- B01 carries the executive-summary intent as Claude's own plan sentence
  (see above), not `BrutalistHesitantWriter`.

## Components built for this reel (the skill's three contracts, now real)

`brutalist-art/runtime/remotion/src/scenes/` — registered in `Root.tsx`
under `CC`, indexed, `./art scenes --check` → RENDERABLE:

| Component | Beat | What the motion carries |
|---|---|---|
| `CCSkepticAudit` | B07 | Claude's claim pinned; four moves each with the question and the command; stamps ✓ ✗ ○ land on cue; verdict last |
| `CCBoondoggleScore` | B08 | steps land in dependency order; CLAUDE steps carry a handoff line; HUMAN steps carry `[PA][PF][TO][IJ][EI]`; the dangerous middle ringed; tally with zeros in red |
| `CCHumanLedger` | B09 | AI column lands first, human column second and holds — the order is the argument; MUST rows ruled terracotta; closing line |

Each follows the house shape (schema with `⚠ SET IN BEAT SHEET` defaults,
component, defaultProps, Demo twin), CC tokens only, frame-time only. Stills
of the demo twins were read before authoring.

`tsc --noEmit` on the sandbox tree reports eleven pre-existing errors in
other compositions (`Root.tsx` lines 1007–4866: `handle`, `citation`,
`sparkSize`, `cols`, `glossTerms` …). None touch the three new files. Noted,
not fixed — not this reel's scope.

## Gates

| Gate | Result |
|---|---|
| GATE L | Run for the three closing-block needs; `BrandBoondoggleScore` (demo, `score` only) and `MedhavyTwoColumnCard` (right props, ~25% fill, wrong palette) were the nearest hits — both design leads, neither usable. Three components built. |
| GATE F (paperwork) | `FACTCHECK.md` · `SHOTLIST.md` · `PROMPTS.md` present. `factcheck_check.py`: **clean** after escaping two `\|` inside claim cells (the checker splits on unescaped pipes — first run reported two FC-6 advisories from the shifted columns). 26 rows, 12 beats covered. |
| CHECKS-REPORT | 13 SHOW / 0 CARD / 0 HOLD / 0 PUNT; teaching arc all ✓. Seven consecutive `CCSession` beats logged as by-design under TERMINAL-FIRST. |
| Audio | Kokoro, per-beat voice honoured: `am_onyx` on every beat (re-narrated: the first pass used `af_bella` for B00–B09). Measured **4:28**. |
| `scenes.py` | The sandbox `run.sh` refuses any reel without one (bare file-existence test, then it lists `Scene` classes). Written with **no** Scene classes and a docstring saying why — a placeholder scene would be a stub. |
| Gate V / GATE T | see compile record |

## Compile record

Four passes; the film was complete after pass 2 and the rest was frame QC.

| Pass | What happened |
|---|---|
| 1 | REFUSED — sandbox `run.sh` requires a `scenes.py` (bare existence test). Wrote one with no Scene classes and a docstring saying why. |
| 2 | Full render, 13/13. Gate V 0 BLOCKER / 0 STRUCTURAL / 0 COSMETIC. GATE T **PASS first time**. Lane-check PASS. Audio −24.5 dB. Then **GATE BOOKEND FAILED** ×3: cold open not `ClaudeComposerAsk`; no `BHTF`; outro `handle` empty. |
| 3 | Frame reads found what the gates did not — see below. Six beats patched at the source and merged surgically into the live sheet (audio + build stamps preserved), re-rendered. Bookend gate now failed only on the two id/handle items. |
| 4 | Closing beats renamed `BVDT / BHTF / BOUT` with their mp3 + media files (no re-render, no new audio), outro `handle` + `subline` props added, `metadata.skill` set. **GATE BOOKEND PASS.** `./art final` → GATE T PASS → master. |

**Final (pass 4, superseded):** `cc-vibecoders-welcome.mp4` · 3840×2160 · 269.75 s (4:30) · mean −24.5 dB · every beat a real render, zero slates.

**Defects found by reading frames that no gate flagged**

1. `CCSession` `text` blocks **wrap and overprint** the blocks beneath them
   past ~44 characters (B01, B02, B05). Split at clause boundaries, one block
   per line, wording untouched. Recorded in the skill's kit gotchas with the
   measured budget.
2. `mascot: 'auto'` on a full-height block stack put Clawd **on top of** the
   diff (B04) — `mascot: 'off'` on any beat whose stack reaches the footer.
3. The three `Edit` child labels were my paraphrases; replaced with the real
   `old_string` heads from `SESSION.md` and added FACTCHECK row 27.
4. Two truncations in `CCBoondoggleScore` (step texts) and one in
   `CCSkepticAudit` (the Hume question) — shortened at the source.

**GATE BOOKEND and the new skill.** The checker encodes the ai-explainer
chassis (first beat must be `ClaudeComposerAsk`) but already carries a
documented skill-override mechanism (`simple`, `critiq`). `cc-explainer` was
added to it the same way — cold open may be a CC surface; recap / your-turn /
outro rules untouched. The two remaining failures were mine: the your-turn ids
and the outro `handle` prop, which the gate reads from the sheet even though
the component hardcodes it. Both are now in the skill and the reference sheet.

| 5 | **Re-narrated with Liam (LIAM LAW).** Bear, while watching pass 4's master: "Liam persona ALWAYS. Liam in for Bear." The "Ada" operator was removed from the skill; every beat re-voiced `am_onyx` (cold open now "This is Liam, in for Bear"; the handoff is just "Let's recap with Claude."; the memory note is "about me"). Full regenerate (all 13 mp3s), full re-render, `run` → every gate RAN-PASS (Gate V 0/0/0, GATE T PASS, BOOKEND PASS, loudness −24.15 LUFS) → `final` → master **234.98 s (3:55)**, 3840×2160, mean −23.7 dB. Docs in this folder rewritten Ada → Liam; SESSION.md keeps the transcript unchanged (what was typed is what was typed). |

**Final (pass 5):** `cc-vibecoders-welcome.mp4` · 3840×2160 · 234.98 s (3:55) · mean −23.7 dB · Liam on every beat.

## Restructure (Bear, 2026-09-08 evening)

"Remove the skepticism beat … Hume, Plato etc is just confusing. Add a Hesitant
writer at beat two describing what the idea of the film is … a definitions card."
Done on all three films and in the skill: the SKEPTIC beat (B07) removed with
its audio and render; `BIDEA` (BrutalistHesitantWriter, CC palette — the idea of
the film, one word reconsidered) and `BDEFS` (`CCDefinitions`, built for this:
vibecoding · localStorage · tool call · diff · git diff --stat) inserted after the cold open. Existing beats kept their audio and
renders (stamps restored after an accidental sheet regenerate); only the two new
beats were voiced and rendered, then `run` → `final`.

**Not published.** Master stays here; TOPOST only via `post`, only on ask.
