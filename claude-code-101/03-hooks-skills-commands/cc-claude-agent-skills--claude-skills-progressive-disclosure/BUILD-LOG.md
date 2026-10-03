# BUILD-LOG — cc-claude-agent-skills--claude-skills-progressive-disclosure

cc-explainer · Claude Code 101 · tier `03-hooks-skills-commands`, "Unlimited Knowledge, A Hundred Words of Context" · Liam, in for Bear · built 2026-09-10.

## The experiment

Same scratch project — a Q3 platform-review `article.md`, a `check.py` definition of done, and a two-tiered `exec-summary` skill (`.claude/skills/exec-summary/SKILL.md` with `references/house-style.md` and `references/length.md`) — three fresh headless `claude -p` runs, Claude Code 2.1.150:

- **Run A** (bare, no `.claude/skills/` in folder) — ask `Please summarize article.md into summary.md.` → 0 `Skill()` fires, Read `article.md`, Write `summary.md` (single `#` heading, ad-hoc prose). `check.py` FAIL. 14.6 s.
- **Run B** (skill present, natural ask) — ask `Write an executive summary of article.md into summary.md.` → 1 `Skill(exec-summary)` fire, Read `article.md`, Write `summary.md` (four `##` sections). No reference reads (the body's own conditional held). `check.py` PASS. 25.8 s.
- **Run C** (skill present, strict-style ask) — ask ends with `following our house style precisely.` → 1 `Skill(exec-summary)` fire, Read `references/house-style.md` (the body's `if 'house style' in ask` matched), Read `article.md`, Write `summary.md` (rules from the reference cited in Claude's closing sentence). `references/length.md` never read (the body's other conditional never matched). `check.py` PASS. 16.3 s.

Skill context loaded per run: **0 · 158 · 353 words** for the same skill folder — three depths from one skill, one ask apart. That is progressive disclosure by tier: description resident, body on `Skill()` match, references on the body's own condition.

## Iteration

- One authoring pass. Body-conditional tightening of `SKILL.md` between the first and second Run B: the initial body said "For house-style rules, read `references/house-style.md`" unconditionally and Claude read BOTH references — the tiers collapsed. Tightening the body to "**only if** the ask uses the words 'house style', 'style guide', or 'strict style'" — plus the length trigger — gave the three-tier separation shown in the film.
- One compile pass to review cut: GATE V 0/0/0, GATE T PASS, BOOKEND PASS, GATE MASTER PASS, LOUDNESS PASS.
- One kit-display fix: B03/B05/B07 shell prompts rendered `\"name\":\"Skill\"` with visible backslash-quotes (a Python-source artefact of quoting inside a JSON string). Changed the on-screen command to single-quoted (`'"name":"Skill"'`), which is what a real shell would use. Cleared `shot.remotion.rendered` on those three beats and re-rendered them; every other beat's audio + render stamp was preserved by a merge script (regenerate to `beat_sheet.json`, then splice `actual_duration_s`, `audio_file`, and `shot.remotion.rendered` back from the previous sheet when props are unchanged). Second run through all gates: PASS again.
- Frame reads at 90 % on the dense beats (B01, B05, B07, B08, B09, BVDT) — clean; all step and ledger strings within budget after authoring-time trimming.

## Advisories left in place

- `SKIN LINT: B00: palette=claude but the cold open is 'CCSession' — COLD OPEN LAW wants ClaudeComposerAsk`. Advisory only — GATE BOOKEND is the enforced check and passes; the skill's `SKILL.md` explicitly allows a CC surface as the cold open when `metadata.skill: "cc-explainer"` is set (which it is). Kept CCSession for the cold open because TERMINAL-FIRST LAW is the local rule.
- `motion histogram: type carries 10/15 beats (66%) — over the ~40% pantry cap`. Advisory only. The film is intentionally terminal-forward: eight of ten `type` motions are the ASK typing into `CCSession` or Liam typing bang commands into a shell — that IS the film. Not converted.

## Master

- `cc-claude-agent-skills--claude-skills-progressive-disclosure.mp4` — 3840×2160 h264/aac, 24fps, 301.6 s (5:01). Kokoro `am_onyx` on every beat, free. Slate cut also written (labelled) as `-slate.mp4`.

## Not published

TOPOST only via `post`, only on Bear's ask. Master stays in the reel folder.
