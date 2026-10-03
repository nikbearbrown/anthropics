# SESSION.md — cc-three-files

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, same one-sentence ask (`evidence/ask.txt`), three conditions. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{bare,barecheck,three}.jsonl`; the three pages in `evidence/index.{bare,barecheck,three}.html`; the three files and the checker in `evidence/`; harvested transcript `evidence/transcript.txt`.

```
Build the sign-up page for our Thursday study group as index.html.
```

| Condition | What was in the folder |
|---|---|
| **bare** | `README.md` (three lines), `ask.txt` |
| **barecheck** (unplanned) | the same plus `check.py` — the first "bare" attempt, where the definition-of-done script had been left in the folder by mistake; kept as a third condition |
| **three** | the same plus `CLAUDE.md` (5 lines), `DESIGN.md` (7), `PROJECT.md` (7), and `check.py` |

The three files (`evidence/CLAUDE.md`, `DESIGN.md`, `PROJECT.md`, verbatim) were written by Liam before the run. `check.py` (`evidence/check.py`) is PROJECT.md's "what is done" as a script: no external requests, no external script/stylesheet, no emoji, no exclamation mark in a heading, no email/password field, one `font-family`, never the word "welcome".

## Run: bare (session `c7740e7c-…`)

- **TOOL** `Bash` `ls -la …` · **Read** `README.md` · **Read** `ask.txt`
- **CLAUDE:** I'll create a self-contained `index.html` sign-up page. Since there's no backend specified, I'll use `mailto:` as the submission target so it works out-of-the-box.
- **TOOL** `Write` `index.html` (212 lines)
- **CLAUDE:** Created `index.html` — a single-file, mobile-responsive sign-up page for the Thursday study group with name/email/focus/experience/notes fields. Submits via `mailto:` to `organizer@example.com` (swap in the real address before sharing).
- **RESULT:** success · turns=5 · 46.2 s · $0.248

## Run: barecheck (session `82cd44e3-…`)

- **TOOL** `Bash` `ls -la` · **Read** `README.md` · **Read** `ask.txt` · **Read** `check.py`
- **CLAUDE:** I'll build a self-contained index.html sign-up page for the Thursday study group, following the constraints in check.py (no external resources, no emojis, no email/password fields, single font-family, no "welcome", no exclamation marks in h1-h3).
- **TOOL** `Write` `index.html` (195 lines) · **TOOL** `Bash` `python3 check.py` → `PASS: index.html meets PROJECT.md's definition of done`
- **CLAUDE:** `index.html` created and passing `check.py`. It's a self-contained page: header block with meeting time/place, a short description of how the group runs, and a sign-up form (name, free-form contact field, date, what you're working on, expected frequency, reminder opt-in). All styling is inline, single serif font-family, no external assets, no email/password fields, no emojis.
- **RESULT:** success · turns=7 · 49.5 s · $0.290

## Run: three (session `38422d22-…`)

- **TOOL** `Bash` `ls -la` · **Read** `check.py` · **Read** `PROJECT.md` · **Read** `DESIGN.md` · **Read** `README.md` · **Read** `ask.txt` (CLAUDE.md is auto-loaded, not Read)
- **CLAUDE:** I have the constraints. Let me build `index.html` — one column, system font, name field only, next-Thursday computed in the browser.
- **TOOL** `Write` `index.html` (95 lines) · **TOOL** `Bash` `python3 check.py` → `PASS: index.html meets PROJECT.md's definition of done`
- **CLAUDE:** `check.py` passes. `index.html` is one column, system-font, name-only sign-up with the next Thursday computed in the browser and the #D97757 button. Today (Wed 2026-09-09) it renders "Thursday, September 10."
- **RESULT:** success · turns=9 · 68.6 s · $0.367

## Liam's VERIFY (plain shell, in `evidence/`; `check.py` run against each page by symlinking it to `index.html`)

```
> wc -l index.bare.html index.barecheck.html index.three.html
     212 index.bare.html
     195 index.barecheck.html
      95 index.three.html
> python3 check.py            # bare
FAIL: emoji
FAIL: email/password field (sign-up wall)
> python3 check.py            # barecheck
PASS: index.html meets PROJECT.md's definition of done
> python3 check.py            # three
PASS: index.html meets PROJECT.md's definition of done
> grep -o "<input[^>]*>" index.bare.html | head -2
<input type="text" name="name" autocomplete="name" required />
<input type="email" name="email" autocomplete="email" required />
> grep -o "<input[^>]*>" index.three.html
<input class="field" type="text" id="name" name="name" autocomplete="given-name" required>
> grep -c "#D97757" index.three.html
1
> grep -n "getDay" index.three.html
75:    var offset = (4 - now.getDay() + 7) % 7;
> grep -c "reminder\|Reminder" index.barecheck.html
4
> grep -o "font-family[^;]*" index.barecheck.html | head -1
font-family: Georgia, "Times New Roman", serif
> wc -l CLAUDE.md DESIGN.md PROJECT.md
       5 CLAUDE.md
       7 DESIGN.md
       7 PROJECT.md
      19 total
```

Emoji in the bare page: 📅 🕕 📍 (three). The bare page's `mailto:` target is built in JavaScript from `organizer@example.com`.

## What the runs gave the film

1. Bare: 212 lines of decisions nobody made — emoji, an email field (a sign-up wall for twelve friends), a `mailto:` to a placeholder address. Fails the definition of done twice.
2. Three files (19 lines of Liam's): 95 lines; its plan sentence is the files' content; one input (a first name), the one accent colour once, the next Thursday computed on line 75; it ran the checker itself because CLAUDE.md said to. Pass.
3. The unplanned middle case: the checker alone. It built to the script and passed — then added a contact field, a date, a frequency, a reminder opt-in, in a serif face. Done is a script; who it's for is not. That is what PROJECT.md is for.
