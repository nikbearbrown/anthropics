# SESSION.md — cc-stop-prompting-claude

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Four fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, on two writing tasks under two conditions. Persona: **Bear**, a professor of applied AI, drafting short notes for his class and a reply to a student. Same two tasks in both conditions; only the folder changes.

Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`; `--permission-mode acceptEdits`. Scratch lived at `/tmp/cc-stop-scratch/{bare,files}/` — **outside the books tree** — so no ancestor `CLAUDE.md` auto-loaded (verified: probing from inside the reel folder returned `books/CLAUDE.md`; probing from `/tmp/` returned none). The reel's `evidence/` copy is the record.

## The two tasks (asks are byte-identical between conditions except for the omitted preamble)

| # | Task | Ask (short form) |
|---|---|---|
| **A** | Note to the class | Wednesday's guest lecture is rescheduled to next Friday because of weather. Nothing to do. |
| **B** | Reply to a student | Priya missed today's quiz; she is unwell. Medical make-up allowed if she sends a note from health services within a week. |

## Two conditions

| Condition | What was in the folder | What Bear typed each session |
|---|---|---|
| **bare** | `README.md` only | the FULL Bear-voice preamble **+** the ask, every time |
| **files** | `README.md` + `CLAUDE.md` (once, 26 lines) | the ask only |

The `CLAUDE.md` file (`evidence/CLAUDE.md`, verbatim) states the voice rules (no exclamations, no emoji, banned words `delve/leverage/robust/unlock/empower/unleash/harness`, banned phrases `I hope this finds you well` / `excited to announce` / `in today's world`, address the class as "class", sign as "— Bear", never invent names/dates/URLs, format plain-text-only). `evidence/check.py` encodes the same rules as a script that prints `PASS` or `FAIL:<rule>` per file.

## Bytes typed to Claude

```
> wc -c ask-bare-a.txt ask-bare-b.txt ask-files-a.txt ask-files-b.txt CLAUDE.md
     975 ask-bare-a.txt
     999 ask-bare-b.txt
     146 ask-files-a.txt
     171 ask-files-b.txt
    1256 CLAUDE.md
```

Bare cost per session ≈ 987 bytes typed. Files cost per session ≈ 159 bytes typed, plus 1256 bytes written **once** into CLAUDE.md. Ratio for two tasks: `1974 / 317 = 6.2×`. Ratio at ten tasks: `9870 / 1585 = 6.2×` (bare compounds; files does not — the file is amortized).

## Run: bare-A (Class note, session `aba74a4f-…`)

- **CLAUDE:** `Class, Wednesday's guest lecture is moved to next Friday because of the weather. Same time, same link. Nothing you need to do on your end. See you then.` `— Bear`
- **RESULT:** turns=1 · 3.6 s · $0.086

⚠ **Bare-A invented a URL** — "Same time, same link." The bare preamble literally said "Do not invent names, dates, room numbers, URLs, or citations." The rule was in the prompt; the output ignored it. See B05 of the reel.

## Run: bare-B (Reply to Priya, session `ea6704ee-…`)

- **CLAUDE:** `Hi Priya, sorry you're not feeling well. You can take a make-up quiz if you send a note from health services within a week.` `— Bear`
- **RESULT:** turns=1 · 3.4 s · $0.055

## Run: files-A (Class note, session `62738b1b-…`)

- **CLAUDE:** `Class, Wednesday's guest lecture is moved to next Friday because of the weather. Nothing to do on your end.` `— Bear`
- **RESULT:** turns=1 · 9.1 s · $0.095 (CLAUDE.md auto-loaded: `cache_creation` +311 tokens vs bare-A, ≈ the file's size)

No invented link.

## Run: files-B (Reply to Priya, session `19daf2ed-…`)

- **CLAUDE:** `Priya, no problem. Send a note from health services within a week and we'll schedule a make-up quiz. Feel better.` `— Bear`
- **RESULT:** turns=1 · 4.0 s · $0.057

## Liam's VERIFY (plain shell in `evidence/`)

```
> wc -w note-bare-a.txt note-bare-b.txt note-files-a.txt note-files-b.txt
      30 note-bare-a.txt
      26 note-bare-b.txt
      21 note-files-a.txt
      22 note-files-b.txt
> python3 check.py note-bare-a.txt note-bare-b.txt note-files-a.txt note-files-b.txt
PASS: note-bare-a.txt
PASS: note-bare-b.txt
PASS: note-files-a.txt
PASS: note-files-b.txt
> grep -c "link\|room\|Zoom" note-bare-a.txt note-bare-b.txt note-files-a.txt note-files-b.txt
note-bare-a.txt:1
note-bare-b.txt:0
note-files-a.txt:0
note-files-b.txt:0
> wc -l /tmp/cc-stop-scratch/files/CLAUDE.md
      26 /tmp/cc-stop-scratch/files/CLAUDE.md
```

## What the runs gave the film

1. Both conditions **PASS the voice checker** — the file is not "how you get output that follows the rules" (a longer prompt gets that too). The file is **how you stop retyping the rules**.
2. **Bytes typed to Claude per two tasks:** bare 1974, files 317 + 1256-once. Bare grows linearly with sessions; files amortizes. At 10 tasks: `6.2×` more typing in bare, and the gap widens.
3. **Bare-A invented `link` — the rule was in the prompt.** A rule you retype every session is a rule you can lose. A rule in a file is a rule that stays. The receipt is what Claude *didn't* invent when CLAUDE.md was the source.
4. `cache_creation` tokens tell the mechanical story: files-A loaded ~311 tokens more than bare-A into the cache — the size of CLAUDE.md — proving the file was in the session's context, not the message.
