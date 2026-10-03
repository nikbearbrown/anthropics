# CHECKS-REPORT — cc-claude-skills

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands`, film 04 · Liam, in for Bear · 2026-09-10.

## SHOW / HOLD / CARD

| Slot | Beat | Kind | Kit component | Terminal? | Why |
|---|---|---|---|---|---|
| SHOW | B00 | Cold open — bare | CCSession | in | the ask arrives and its ad-hoc output prints; nothing routed |
| HOLD | BIDEA | The idea | BrutalistHesitantWriter | out (writer beat) | the film's argument, not in any session |
| CARD | BDEFS | Definitions | CCDefinitions | out (definitions) | five terms a chat-window audience won't have |
| SHOW | B01 | Bare — VERIFY | CCPlainShell | out (post-hoc plain shell) | window is closed; grep-check on the transcript file |
| CARD | B02 | The folder | CCPlainShell | out (reading the folder) | shows the built SKILL.md and its frontmatter |
| SHOW | B03 | Skill — the run | CCSession | in | Skill() fires as a tool call, then Read/Write/check |
| SHOW | B04 | Skill — VERIFY | CCPlainShell | out (post-hoc plain shell) | Skill count, heading count, checker PASS |
| SHOW | B05 | The other ask | CCSession | in | correction cycle — a different ask fires the same skill |
| CARD | BFLOW | Where the skill sits | CCHarnessMap | out (BFLOW) | the ask→description→skill→loop chain, drawn |
| SHOW | BSHOW | The built file | CCPlainShell | out (BSHOW) | `cat summary.md` — the four sections the skill wrote |
| CARD | BCOND | Conduct (Boondoggle) | CCBoondoggleScore | out (score) | who did what, six steps |
| CARD | BHUM | Human ledger | CCHumanLedger | out (ledger) | must / should for human and AI |
| CARD | BVDT | Verdict | ClaudeVerdictArtifact | out (bookend) | four lines, last one falsifiable |
| CARD | BHTF | Your turn | ClaudeComposerAsk | out (bookend) | the viewer's prompt |
| CARD | BOUT | Outro | ClaudeTitleOutro | out (bookend) | title restate, `@NikBearBrown`, no subline |

Two consecutive card beats: BCOND → BHUM → BVDT → BHTF → BOUT. Each is in the mandated closing block; each names its own reason.

## Teaching arc

- **PREDICT** (B00, cold open): show the bare failure — one ask, an ad-hoc shape, no file, no receipt.
- **BEFORE-VS-AFTER** (B01 → B04): the transcript's `Skill()` count is 0 in the bare run and 1 in the skill run; the same two commands run twice, the answers are visibly different.
- **CONCRETE-BEFORE-ABSTRACT** (B02 before B03): the audience sees the folder (its two files, its frontmatter) before they see the tool call that fires from it. The description is on screen before the film explains what it does.
- **CORRECTION CYCLE** (B05): the "other ask" is the sceptic beat repurposed — the routing is semantic, not literal, and the film says so on camera. The rule is the finding, not the setup.
- **BUILD-SHOWN** (BFLOW → BSHOW): the chain is drawn, then the file the chain produced is read. CONDUCT is scored against a build the viewer has just seen.
- **FALSIFIABLE** (BVDT): "a skill run where changing the ask changed the output shape" — a run of the same skill against another ask, checked for divergent headings, would falsify.
- **SCAFFOLDED HANDOFF** (BHTF): the viewer's prompt doesn't ask them to write a skill from scratch — it asks Claude to interview them, then write the skill and the checker on the viewer's behalf. The viewer names the four inputs; the tool produces the SKILL.md.

## BUILD-SHOW status

BUILD-SHOW: armed (`metadata.build: true`).
- BFLOW: 1 beat (CCHarnessMap — MODEL core, YOUR ASK → DESCRIPTION MATCH → SKILL LOAD → YOUR LOOP)
- BSHOW: 1 beat (CCPlainShell — `cat summary.md`, the four sections the skill produced)

## Gates before compile

- Kit budgets — `python3 author_sheet.py` prints `budget: clean` (text ≤ 44, ledger ≤ 34, score ≤ 46, shell ≤ 52, verdict = 4, terms ≤ 18, meanings ≤ 70).
- BVDT: exactly 4 lines, last starts `FALSIFIABLE:`.
- BOUT props: `handle: "@NikBearBrown"`, `subline: ""`, `slug: "cc-claude-skills"`.
- Audio: Kokoro `am_onyx` for every beat, measured; `mp3/timings.json` present.
- SESSION.md: present. FACTCHECK.md: `factcheck_check.py` prints `clean`.
- BUILD gate — `metadata.build: true`, BFLOW + BSHOW present.
- Never edit `beat_sheet.json` while `art run` is alive.
