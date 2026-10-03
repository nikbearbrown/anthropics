# BUILD-PROMPT — cc-vibecoders-welcome

Paste-ready prompt to rebuild this reel from a clean session. Toolkit:
`brutalist-art/` (the CC kit lives only there).

---

Build a **cc-explainer** reel — `./art cc-explainer --help` — for Claude Code
101, tier `00-what-it-is`, concept "Vibecoders Welcome": a person who does not
write code builds a small personal tool and decides whether it is right.

**Run the session first. For real.** In a fresh git repo containing only a
`README.md`, headless:

```bash
claude -p "I don't write code. Build me a personal reading log as ONE self-contained index.html file: a form to add a book (title, author, date finished, a 1-5 rating), a list of what I've logged, saved in localStorage so it survives reload. No frameworks, no build step, no external requests. Keep it plain and readable." \
  --output-format stream-json --verbose --max-turns 12 \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(wc:*),Bash(grep:*)" > turn1.jsonl
```

Then run Liam's VERIFY by hand (`wc -l`, `grep -c localStorage`, grep for
`https?://|<script src|<link `, grep for `delete|remove|sort`), commit the
file, and resume the session with a correction written **from what the
VERIFY found** — do not script the correction in advance. Run VERIFY again,
then look **outside the repo**: `ls ~/.claude/projects/*<repo>*/memory/`.
Transcribe everything to `SESSION.md`; keep the jsonl, both `index.html`
versions, and the diff in `evidence/`.

**Author from `SESSION.md` only.** Prompt blocks are what she typed
(TYPES-NOT-NARRATES). Every tool name, arg, diff line and output traces to the
transcript. Claude's own sentences are quoted verbatim; multi-line output is
one `text` block per line. No plan card if headless mode produced none — show
the plan sentence.

**Spine (13 beats):** B00 cold open (the ask, `Exploring`, first tool) → B01
the plan sentence → B02 `Write` + Claude's summary → B03 VERIFY-1 (her
commands) → B04 the correction + deletion-only diff → B05 what else it did
(the memory writes, in Claude's words) → B06 VERIFY-2 incl. the check outside
the repo → **B07 SKEPTIC** (`CCSkepticAudit`: four moves as commands; Plato
fails) → **B08 CONDUCT** (`CCBoondoggleScore`: six steps, step 3 the dangerous
middle, EI 0 named) → **B09 HUMAN** (`CCHumanLedger`) → B10 VERDICT (Liam,
"Let's recap with Claude.") → BHTF YOUR TURN (prompt read in
full) → B12 OUTRO (OUTRO-LOCK).

Voice: Liam `am_onyx` on every beat (LIAM LAW).

**Paperwork before the first compile:** `FACTCHECK.md` in the sandbox's
table format (escape `|` inside cells), `SHOTLIST.md`, `PROMPTS.md`,
`CHECKS-REPORT.md`, and a `scenes.py` with no Scene classes (the sandbox
`run.sh` requires the file).

```bash
python3 author_sheet.py
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py <reel>
python3 brutalist-art/runtime/qc/factcheck_check.py <reel>
./brutalist-art/art run   <reel>
./brutalist-art/art final <reel>      # gates on GATE T
```

Never publish. TOPOST via `post` only, and only when the human asks.
