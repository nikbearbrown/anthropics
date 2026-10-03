# FACTCHECK — cc-vibecoders-welcome

Status: PASS — checked 2026-09-08 by the build session against `SESSION.md` (the real headless Claude Code session, id `dff47fa4-dd2f-4f65-bd3c-0c03beab300d`) and its `evidence/` files.

**Verification boundary.** Every factual claim in this reel is a claim about
one session that ran on 2026-09-08 and is transcribed verbatim in
`SESSION.md`, with the produced files and diff in `evidence/`. Nothing is
sourced from memory of how Claude Code "usually" behaves. The two
closing-block beats apply doctrine from two INFO-7375 courses to that
session; the doctrine itself is cited, not re-derived. Restructured 2026-09-08 (Bear): the SKEPTIC beat is gone; THE IDEA and DEFINITIONS follow the cold open. Product strings on
screen (`accept edits on`, `◐ medium · /effort`, `esc to interrupt`, the
status verbs) are rendered by the CC kit from `tokens/claudecode.ts` and are
not authored here.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | BIDEA | 'Vibecoding means you describe a tool in plain words, Claude Code writes it, and you decide whether it's right — by reading it' — the writer corrects 'trust' → 'check' | PASS | the session: two unasked features found by reading, one memory file found outside the folder | — |
| 2 | BDEFS | Definitions card: vibecoding · localStorage · tool call · diff · git diff --stat | PASS | plain-language glosses of the words on screen in B02–B06; localStorage per the file itself (`reading-log:v1` key); git per `git diff --stat` output | — |
| 3 | B00 | Liam's ask, shown verbatim in the prompt block | PASS | `SESSION.md` → Turn 1 → "Liam typed" | — |
| 4 | B00 | First tool call was `Bash pwd && ls -la` | PASS | `SESSION.md` Turn 1, first TOOL line; `evidence/turn1.jsonl` | — |
| 5 | B01 | Claude's plan sentence, incl. "and a delete option", verbatim | PASS | `SESSION.md` Turn 1, first CLAUDE line | — |
| 6 | B02 | One `Write index.html`; 286 lines | PASS | Turn 1 TOOL `Write`; `wc -l` in VERIFY-1 = 286 | — |
| 7 | B01, B02, B05 | Claude's plan sentence, summary lines, and turn-2 report | CORRECTED | Turn 1 / Turn 2 CLAUDE text; split at clause boundaries into ≤60-char text blocks because `CCSession` text blocks occupy one row and a long line wraps over the blocks below (B02's summary also drops two parentheticals: "(defaults to today)", "formatted date") — wording otherwise unchanged | split, not reworded |
| 8 | B03 | `grep -c localStorage` → 2 | PASS | VERIFY-1 in `SESSION.md` | — |
| 9 | B03 | grep for `https?://\|<script src\|<link ` → no output | PASS | VERIFY-1 | — |
| 10 | B03 | `sort` at line 221, `remove` button at line 241 | PASS | VERIFY-1; `evidence/index.html.turn1` | — |
| 11 | B04 | Liam's correction prompt, verbatim | PASS | `SESSION.md` Turn 2 → "Liam typed" | — |
| 12 | B04 | Three `Edit` calls on `index.html` | PASS | Turn 2, three TOOL `Edit` lines | — |
| 13 | B04 | Diff: 14 deletions, 0 additions, 1 file; the five diff lines shown are from the real diff | PASS | VERIFY-2 `git diff --stat`; `evidence/turn2.diff` (lines shown are a subset, gutters real) | — |
| 14 | B05 | "Both removed … Nothing else touched." and "Let me save this preference so I don't repeat it." — Claude's words | PASS | Turn 2 CLAUDE text (first sentence trimmed of the parenthetical listing; wording unchanged) | — |
| 15 | B05 | Two `Write` calls outside the repo: `feedback_scope_discipline.md` and `MEMORY.md` under `~/.claude/projects/…/memory/` | PASS | Turn 2 TOOL `Write` ×2; Plato check in `SESSION.md` (`ls` output) | path shortened to `~/.claude/projects/…/memory/` for display |
| 16 | B05 | "Removals are done and the preference is saved." | PASS | Turn 2 final CLAUDE text (second sentence omitted) | — |
| 17 | B06 | `git diff --stat` → `index.html \| 14 --------------` / `1 file changed, 14 deletions(-)` | PASS | VERIFY-2 | — |
| 18 | B06 | grep remove/sort → no output; memory dir lists two files | PASS | VERIFY-2; Plato check | — |
| 19 | B06, B09 | "the note it wrote is about me" / the memory file describes the user's preference | PASS | Plato check — file body: "User wants exactly what they asked for … They read the code before running it" | — |
| 20 | B08 | Five supervisory capacities `[PA][PF][TO][IJ][EI]`; handoff conditions; the dangerous middle | PASS | Gru spec (Conducting AI); `info-7375-conducting-ai/chapters/04–13`; `reference/three-beats.md` | — |
| 21 | B08 | Tally PA 1 · PF 1 · TO 1 · IJ 1 · EI 0 | PASS | Count of `capacity` fields in the B08 props | — |
| 22 | B09 | "the machine cannot tell me when it's done something I'd mind" — Tier 4 framing (weak Type 2 / cannot report its own uncertainty) | PASS | `info-7375-irreducibly-human/chapters/04-tier-4-metacognitive-and-supervisory.md` (Lee et al. 2025 framing) | narration phrases it as a limit, not a number |
| 23 | B10 | "a working tool in two turns" | PASS | Turn 1 RESULT turns=3, Turn 2 RESULT turns=6 — two user turns | — |
| 24 | B10 | "announced one of them" | PASS | Turn 1 CLAUDE text names the delete option; the sort was not announced in the plan sentence (it appears only in the post-hoc summary) | — |
| 25 | B00 | "That's what vibecoding is" — no external definition claimed | EXEMPT | Framing sentence, not a checkable claim | — |
| 26 | B12 | Title restate "Vibecoders Welcome" + "Liam, in for Bear" | PASS | `metadata.title`; OUTRO-LOCK; IN-FOR-BEAR LAW | — |
| 27 | B04 | The three `Edit` children are labelled by the head of each call's `old_string` (`function render() { var books…`, `logEl.innerHTML = books.map(fun…`, `logEl.addEventListener("click",…`) | PASS | `SESSION.md` Turn 2, the three TOOL `Edit` lines; `evidence/turn2.jsonl` | truncated to fit the tool tree, not paraphrased |

## Stripped — what the source concept reel said that this one does not

The copied `claude-cowork--claude-liam-claude-code` sheet carried setup
steps ("download the app and get a paid plan", "turn on bypass permissions",
"connect Netlify and Supabase"), a DESIGN.md tip, a shadcn/ui tip, and
`getdesign.md`. None of that happened in this session, none of it is checkable
against `SESSION.md`, and some of it is datable (vendor names, plan tiers). All
of it stays out. The concept — a non-coder builds a small personal tool and
decides whether it is right — is what survives.

## Datable material

No model names, version numbers, or "as of" phrasing in narration. The Claude
Code version (2.1.150) appears only in `SESSION.md` as provenance.
