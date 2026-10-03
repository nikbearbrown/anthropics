# CHECKS-REPORT — cc-three-file-system-simulator

Written before the first compile (per SKILL.md step 5). Read alongside `FACTCHECK.md`.

## SHOW / HOLD / CARD (per beat)

| Beat | Surface | Motion | Class |
|---|---|---|---|
| B00 | `CCSession` bare | type | SHOW (session) |
| BIDEA | `BrutalistHesitantWriter` | type | SHOW (writer) — leaves terminal: not in any session |
| BDEFS | `CCDefinitions` | drawon | CARD — leaves terminal: for chat-window audience |
| B01 | `CCSession` bare / verify | type | SHOW (verify) |
| B02 | `CCPlainShell` | type | HOLD — leaves terminal: files, no session |
| B03 | `CCSession` three-files / run | type | SHOW (session + correction) |
| B04 | `CCSession` three-files / verify | type | SHOW (verify) |
| BFLOW | `FlowDiagram` | drawon | CARD — leaves terminal: BFLOW (the gate is implied) |
| BSHOW | captured `media/BSHOW.mp4` | hold | SHOW (the sim running) |
| B05 | `CCBoondoggleScore` | drawon | CONDUCT |
| B06 | `CCHumanLedger` | drawon | HUMAN |
| BVDT | `ClaudeVerdictArtifact` | hold | BOOKEND |
| BHTF | `ClaudeComposerAsk` | (default) | BOOKEND |
| BOUT | `ClaudeTitleOutro` | hold | BOOKEND |

**Non-terminal beats:** BIDEA, BDEFS, BFLOW, BSHOW, B05, B06, BVDT, BHTF, BOUT.
Two consecutive non-terminal beats: BFLOW → BSHOW (both name reasons: BFLOW is the
gate the session implies; BSHOW is the receipt the build produced). B05 → B06 →
BVDT → BHTF → BOUT is the closing-block sequence, expected on every cc-explainer.

## BUILD-SHOW LAW (Bear, 2026-09-09) — ARMED

`metadata.build: true`. This is a build film (verb: *build a simulation*). Both
required beats present, immediately before CONDUCT:

- **BFLOW** — `FlowDiagram` (claude skin), 8 nodes / 8 edges. Every node label is
  a real filename or role from `SESSION.md`. The `FAIL → fix page` reply edge
  is the film's real correction cycle from the three-file run.
- **BSHOW** — `media/BSHOW.mp4` (8.0s), four states of the three-file page
  captured from `evidence/index.three.html` via Chrome headless with N calls to
  the page's own `step()` function pre-render. Provenance in
  `media/BSHOW.source.txt`. Not a mock. Not a mock-up. The build's own JS.

## Teaching arc

- **Predict → reveal.** The bare run's plan predicts what the page will contain
  ("speed control and step-through for class"). B01 reveals: the plan is exactly
  what shipped, and it fails the checker on five constraints the teacher never
  named because the teacher never got to.
- **Concrete before abstract.** Two real files, on screen, compared against a
  script. The concept ("three files gate the build") lands in BFLOW *after* the
  audience has seen the mechanism run.
- **Useful friction (the correction cycle).** B03 shows Claude failing the
  checker on `font-family: inherit` and fixing the page (not the script) twice.
  Nothing dramatised; nothing scripted; the correction is the film's evidence
  that this is a receipt.
- **Falsifiability (BVDT last line).** "A bare run that, unprompted, chooses
  one interaction, one button, and one palette." — a single counterexample
  falsifies the argument. Recorded on the artifact.
- **Handoff to practice (BHTF).** The viewer's prompt is Claude interviewing
  them to *write* their own three files, before building. It hands the tool to
  them, in the same order this film introduced it.

## Duration / voice

- 14 beats · narrated total ~4:55 · plus pauses/holds, target 5:30–6:15.
- Every beat: Liam, `am_onyx`, Kokoro (free/local). No paid voice.
- BOUT holds ~6s (title + handle + mascot).

## Kit gotchas honoured

- Every `CCSession` text block ≤ 44 chars (author_sheet asserts).
- Every `CCHumanLedger` row ≤ 30 chars (author_sheet asserts ≤ 34, actual ≤ 33).
- Every `CCBoondoggleScore` step ≤ 46 chars (author_sheet asserts).
- `CCSession` blocks / cues arrays same length (asserts).
- `mascot: 'off'` on every full-stack `CCSession` beat (B00/B01/B03/B04).
- `ClaudeVerdictArtifact` has **4 lines** (not 5).
- Status blocks use `tokens: "1.2k tokens"` without leading `↓` — n/a here (no status blocks).
- `ClaudeTitleOutro` carries `handle: "@NikBearBrown"` and `subline: ""`.
- `ClaudeComposerAsk` greeting is `Your turn.` and topic carries `YOUR TURN`.
- `metadata.skill = "cc-explainer"` for GATE BOOKEND cold-open override.

## Never publish

Master stays in `mp4/`. `books/youtube/TOPOST/` is not touched.
