# BUILD-LOG — cc-five-claudes-explained

cc-explainer · Claude Code 101 · tier `00-what-it-is`, film 02 in the film order ·
Liam, in for Bear (Kokoro `am_onyx`) on every beat — LIAM LAW · Teardown · 16:9 ·
built 2026-09-08. The second reel built with the `cc-explainer` skill.

## What this reel is, and is not

The copied concept — `claude-cowork--claude-liam-five-claudes-explained`, "Five
Products. One Name.", from a Ruben Hassid infographic — was a Liam-narrated card
reel: five products, each with setup steps, a "biggest mistake", and a price. Its
own FACTCHECK marked the prices DATABLE and the rest AUTHOR'S CLAIM; one setup
line was wrong on its face. This reel keeps the five names — they are what Liam
typed — and replaces the body with a real session in which Claude Code is asked
which of the five it is and told to prove it with commands.

## The session (REAL-SESSION LAW)

Headless `claude -p`, Claude Code 2.1.150, session
`76868a34-6d8f-4776-86ee-293691bd9fbf`, fresh git repo with one `README.md`,
tools fenced to `Read, Glob, Grep, Write` + an allow-list of read-only Bash
commands. Two turns; Liam's VERIFY and SKEPTIC commands run by hand in a plain
terminal. Transcript: `SESSION.md`; raw stream-json and the file Claude wrote:
`evidence/`.

What the session gave the film for free:

1. **The fence, in the product's words.** Two of Claude's own `ls` calls were
   blocked — "Claude Code may only list files in the allowed working directories
   for this session." Also visible: three chained commands bounced by the
   allow-list ("This Bash command contains multiple operations …") before Claude
   re-issued them one at a time. Not shown (the fence itself is the lesson).
2. **An inference dressed as evidence.** Claude stamped Cowork **Present** because
   the folder path contains `CoWork`. The folder was made from the desktop app;
   only the human knows which program he launched.
3. **A clean retraction** on one re-prompt with an evidence rule — "a folder name
   is not an identification" — and a file with one PRESENT and four UNVERIFIED
   FROM HERE.
4. **A wrong label that survived the correction**: Cowork filed as "a website /
   hosted service" (it is a mode of the desktop app). The rule covered statuses,
   not labels. That is the Popper move of B07 and the second MUST of B09.

## Components

`CCSkepticAudit`, `CCBoondoggleScore`, `CCHumanLedger` (built for the first
cc-explainer) and **`CCPlainShell`** — built during this compile (see below).

## Gates and compile record

| Pass | What happened |
|---|---|
| 1 | Full render 13/13. Gate V 0/0/0. **GATE T FAIL** on B03: the plain-shell beat was on `BrutalistAdaptCLI` — a cream-page vox terminal with a hardcoded "zsh — adapt this template" title, type under the §8.1 floor, and a half-empty canvas. Wrong on the merits, not only for the gate. |
| 2 | Built `CCPlainShell` for the CC kit: a dark plain terminal at CCSession's type size, no mode footer, no Clawd, no product strings — the honest surface for a command the session's fence blocked. B03 moved onto it. Frame reads also found `CCHumanLedger` rows ellipsizing past ~34 characters (three AI rows, one human row) and the `CCBoondoggleScore` header wrapping — strings shortened at the source, narration untouched (audio is the clock), props merged surgically, B03/B08/B09 re-rendered. `run` → every gate RAN-PASS (Gate V 0/0/0, GATE T PASS, BOOKEND PASS, −24.15 LUFS) → `final` → master. |

Also caught before compile: narration said Skills were "two folders of markdown";
`claude-refactor/` is empty. Corrected and B03 audio regenerated alone
(FACTCHECK row 13).

**Final:** `cc-five-claudes-explained.mp4` · 3840×2160 · 269.54 s (4:30) ·
mean −23.7 dB · Liam on every beat · every beat a real render.

## Restructure (Bear, 2026-09-08 evening)

"Remove the skepticism beat … Hume, Plato etc is just confusing. Add a Hesitant
writer at beat two describing what the idea of the film is … a definitions card."
Done on all three films and in the skill: the SKEPTIC beat (B07) removed with
its audio and render; `BIDEA` (BrutalistHesitantWriter, CC palette — the idea of
the film, one word reconsidered) and `BDEFS` (`CCDefinitions`, built for this:
the terminal · Cowork · Projects · Skills · the fence) inserted after the cold open. Existing beats kept their audio and
renders (stamps restored after an accidental sheet regenerate); only the two new
beats were voiced and rendered, then `run` → `final`.

**Not published.** Master stays here; TOPOST only via `post`, only on ask.
