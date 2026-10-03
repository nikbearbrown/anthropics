# SESSION.md — cc-cwc-how-we-claude-code

The real Claude Code sessions this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, one small task, three phases of the Anthropic CWC workflow (Brainstorm → Design → Verify) applied one at a time. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{bare,design,verify}.jsonl`; every generated file kept in `evidence/`; harvested inputs kept in `evidence/{ask.txt,brief.md,fixture.py,mock1-4.html}`.

```
Build workshop.html — a one-page landing for our Saturday intro-to-git workshop.
```

| Condition | What was in the folder | What ran |
|---|---|---|
| **bare** | `README.md` (3 lines), `task.txt` | one ask, one page, no discipline |
| **design** | same | *Phase 2 — Design.* One ask, four divergent HTML mockups |
| **verify** | `brief.md` (Phase 1 output), `mock2.html` (Design pick), `fixture.py` (Phase 3 DOM contract) | *Phases 1 + 2 + 3.* One ask, converge to a page that must pass the fixture |

`brief.md` (`evidence/brief.md`) and `fixture.py` (`evidence/fixture.py`) are Liam's — the Brainstorm output and the definition of done, hand-written before the verify run.

## Run: bare (session `564333d3-…`)

- **Bash** `pwd && ls -la` · **Read** `README.md` · **Read** `task.txt`
- **CLAUDE:** The task is intentionally minimal — I'll build a clean single-file landing page with sensible placeholders where you'd normally drop in specifics (date, time, venue, signup link).
- **Write** `workshop.html` (130 lines)
- **CLAUDE:** Built `workshop.html` — self-contained single file (no external CSS/JS), mobile-responsive, ~5KB. Placeholders you'll want to fill in: the actual date, the venue, and whether the RSVP flow is email or a form link.
- **RESULT:** success · turns=5 · 53.2 s · $0.384

What was invented (kept in `evidence/workshop.bare.html`): a lede ("A hands-on morning for people who have heard 'just commit it' one too many times."), a `<dl>` of When/Where/Bring/Cost, four hourly-agenda sections (10:00 → 12:45), five subsections (Who it's for / What you'll leave with / Rough agenda / RSVP), an RSVP-by-`mailto:` to `bear@bearbrown.co` (my system's git email, pulled from context), and a footer "Hosted by Bear. Coffee provided. Questions welcome." — 130 lines of decisions nobody made.

## Run: design — Phase 2, diverge (session `dcbf6b63-…`)

- **Read** `task.txt`
- **CLAUDE:** Task is a landing page for a Saturday intro-to-git workshop. I'll build four genuinely divergent directions: (1) clean modern SaaS, (2) terminal/hacker aesthetic, (3) hand-drawn zine, (4) editorial magazine.
- **Write** `mock1.html` · **Write** `mock2.html` · **Write** `mock3.html` · **Write** `mock4.html`
- **CLAUDE:** Four self-contained mockups written. **mock1** — Modern SaaS landing (blue accent, sticky nav, hero + feature grid + hourly schedule + inline register form + FAQ; voice: crisp, functional). **mock2** — Terminal/TTY aesthetic (green-on-black, monospace, ASCII banner, prompts framing each section, a `git diff` "before/after brain" block, register form styled as stdin; voice: hackerly and dry). **mock3** — Hand-drawn zine (warm dotted paper, chunky Bodoni display, wonky rotated header with red drop-shadow, sticker chips, notebook-ruled schedule, red RSVP block; voice: warm and playful). **mock4** — Editorial magazine ("The Saturday Review", Bodoni masthead, two-column justified body with drop cap, sidebar of facts + pull quote, numbered sections; voice: literary and unhurried).
- **RESULT:** success · turns=6 · 297.1 s · $0.990

## Run: verify — Phase 3, converge to the fixture (session `746ba72a-…`)

- **Bash** `ls .../scratch/workshop/` · **Read** `brief.md` · **Read** `task.txt` · **Read** `mock2.html` · **Read** `fixture.py`
- **CLAUDE:** Now I understand the setup. Let me check the fixture requirements: no external assets, monospace font, exactly one `<h1>`, a `<form>` with `name="name"` input, an `#register` control, no email field, no banned words (welcome, amazing, awesome, join us, excited), under 200 lines. The mock2.html has an email input (banned), no `name` attributes on inputs, no `#register` id, and is 202 lines.
- **Write** `workshop.html` · **Bash** `python3 fixture.py` → `FAIL: no monospace font-family (voice: terminal)`
- **CLAUDE:** The fixture wants a literal `font-family:` declaration. My CSS uses the `font:` shorthand. Let me add explicit `font-family`.
- **Edit** `workshop.html` · **Bash** `python3 fixture.py` → `PASS: workshop.html meets brief.md's definition of done (153 lines)`
- **CLAUDE:** PASS at 153 lines. `workshop.html` is built — terminal aesthetic from mock2.html, with the fixture-required changes: explicit `font-family` monospace, `name="name"` input, `id="register"` submit button, no email field, and no banned words.
- **RESULT:** success · turns=11 · 147.8 s · $0.851

Note the built-in correction cycle: Claude wrote the page, ran the fixture itself, it failed, Claude read the failure, edited, ran again, PASS. Claude's ✓ became evidence via `python3 fixture.py`, not "let me know if you want me to iterate".

## Liam's VERIFY (plain shell, in `evidence/`)

```
> wc -l workshop.bare.html workshop.three.html mock1.html mock2.html mock3.html mock4.html
     130 workshop.bare.html
     153 workshop.three.html
     199 mock1.html
     201 mock2.html
     239 mock3.html
     270 mock4.html
    1192 total
> grep -c "welcome\|Welcome" workshop.bare.html workshop.three.html
workshop.bare.html:1
workshop.three.html:0
> grep -oE "<input[^>]*>" workshop.three.html
<input type="text" name="name" placeholder="alex kim">
<input type="text" name="goal" placeholder="what does 'rebase' actually do">
> ln -sf workshop.three.html workshop.html && python3 fixture.py && rm workshop.html
PASS: workshop.html meets brief.md's definition of done (153 lines)
> grep -c 'id="register"' workshop.three.html
1
> grep -oE 'font-family:[^;]*' workshop.three.html | head -1
font-family:ui-monospace,SFMono-Regular,"JetBrains Mono","Fira Code",Menlo,Consolas,monospace
```

The four mockups' divergence, in one line each — the body-font choice:

```
> for f in mock*.html; do echo "$f"; grep 'body{font:' $f | head -1; done
mock1.html   body{font:16px/1.55 -apple-system,BlinkMacSystemFont,…                    sans-serif
mock2.html   body{font:14.5px/1.6 ui-monospace,SFMono-Regular,…Menlo,Consolas,monospace}
mock3.html   body{font:17px/1.55 "Bodoni 72","Didot",Georgia,serif} + Courier accents  mixed
mock4.html   body{font:17px/1.6 "Iowan Old Style",Georgia,serif}                       serif
```

Four different type systems for the same paragraph. That is what "generate four directions before you commit" buys.

## What the runs gave the film

1. **Bare** — 130 lines of decisions nobody made: an invented lede, a four-slot hourly agenda, a mailto to `bear@bearbrown.co` because my git config was in context, "Coffee provided" in the footer, the word "welcome". No form, but a `<dl>` labelled `Cost: Free`. Polished. Not mine.
2. **Design** — 4 fully-rendered pages in 297 seconds — sans / mono / mixed / serif — same ask, four philosophies. The pick is a decision only Liam can make; the point is he made it looking at four options instead of one. He picked `mock2` (terminal — the tool teaches itself the moment you open it).
3. **Verify** — the pick + `brief.md` + `fixture.py` fed back into a fresh run. Claude wrote the page, ran the check itself (because the instructions said to), the check failed on a font shorthand, Claude edited, ran again, PASS at 153 lines. The gap between mockup and working product was a test suite — and Claude closed it without a human turn.
