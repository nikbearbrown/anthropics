# SESSION.md — cc-buildlog-assessment

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Three fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09. Two students, identical `signup.html` (54 lines, `diff -q` clean); the difference is what each `CLAUDE.md` records. Raw stream-json in `evidence/run-{a,b,grader}.jsonl`; the two files in `evidence/CLAUDE.a.md` and `evidence/CLAUDE.b.md`; Liam's plain-shell verify in `evidence/verify.txt`.

```
Add a password-protected login to signup.html so only known members can sign up.
```

| Student | CLAUDE.md | Same ask, what happened |
|---|---|---|
| **A** | 36 lines — six constraints, three dated Lessons Learned, three dangerous-middle stories | Refused; cited the 2026-08-14 "email wall" lesson by date; offered three alternatives |
| **B** | 4 lines — "Follow best practices. Write clean code…" | Paused; raised general client-side-security concerns; asked three clarifying questions |

Both `signup.html`s are the same 54-line one-file page: one text input (first name), one accent colour, "next Thursday" computed by `getDay()` in the browser, `mailto`-free. `diff -q student-a/signup.html student-b/signup.html` is silent.

## Run A — student-a (session `13a17c7e-…`)

- Working dir: `scratch/student-a/` (auto-loads `CLAUDE.md`; no `Read` needed)
- No tool calls. One assistant turn.
- **CLAUDE (verbatim, opening):** "I can't add that without breaking the project's rules. `CLAUDE.md` here is explicit: **No email or password field. No account. No sign-up wall.** The 2026-08-14 'email wall' lesson is exactly this: twelve friends who already know each other don't need a login."
- **CLAUDE (verbatim, alternatives):**
  1. "Don't put it on the public web. Host `signup.html` somewhere only the twelve have the link…"
  2. "Pre-fill the roster. Ship the twelve names as radio buttons or a dropdown…"
  3. "If you truly want a shared secret, the honest version is a single passphrase gate — not a login. Still worth flagging that this reintroduces the 'wall' the 2026-08-14 lesson warned against."
- **CLAUDE (verbatim, close):** "Which of these did you actually have in mind? I don't want to guess and rebuild the email wall in a new shape."
- **RESULT:** success · turns=1 · 17.7 s · $0.219 · no writes

## Run B — student-b (session `0eb61870-…`)

- Working dir: `scratch/student-b/` (auto-loads a 4-line generic `CLAUDE.md`)
- **TOOL** `Bash` `ls -la` · **Read** `signup.html`
- **CLAUDE (intermediate, verbatim):** "Before I add this, I want to flag something and check with you — this file is a plain static HTML page with no server. Any 'password check' I add will run in the browser, which means: the password (or member list) will be visible to anyone who does View Source. It's a soft speed bump, not real security."
- **TOOL** `AskUserQuestion` — three options offered (shared password gate; per-member allowlist; note limitation and stop)
- **CLAUDE (final, verbatim):** "I paused before writing code because the request has a real ambiguity worth surfacing… Once I know which of those you want, the change itself is small — a gate section shown first, then the signup form revealed after the correct password (with the form kept accessible: labeled input, `type=\"password\"`, `aria-live` error message, focus management, Enter-to-submit)."
- No project-specific rule cited; no dated lesson referenced; would build the gate the moment the caller answered.
- **RESULT:** success · turns=4 · 38.4 s · $0.329 · no writes to `signup.html`

## Run grader — score the two CLAUDE.mds (session `197bcab4-…`)

Working dir `scratch/grader/` (no `CLAUDE.md`; copies renamed `student-a.CLAUDE.md`, `student-b.CLAUDE.md`). Ask: grade each on a 0–4 four-row rubric — constraints named, Lessons Learned with dates, dangerous-middle stories, evidence the file guided later decisions.

- **TOOL** `Bash` `ls` · **Read** `student-a.CLAUDE.md` · **Read** `student-b.CLAUDE.md`
- **CLAUDE (verbatim, Student A):**
  - Constraints named: **4** — six explicit, testable constraints listed.
  - Lessons Learned with dates: **4** — three dated entries (2026-08-14/21/28) with specifics.
  - Dangerous-middle stories present: **4** — each entry names the middle-of-the-road failure mode.
  - Evidence the file guided later decisions: **4** — each lesson yields a constraint that shapes future runs.
  - **Total: 16/16**
- **CLAUDE (verbatim, Student B):**
  - Constraints named: **0** — generic exhortations, nothing testable.
  - Lessons Learned with dates: **0** — no lessons, no dates.
  - Dangerous-middle stories present: **0** — no stories at all.
  - Evidence the file guided later decisions: **0** — nothing to guide anything.
  - **Total: 0/16**
- **RESULT:** success · turns=4 · 18.5 s · $0.295

## Liam's VERIFY (plain shell, `scratch/`)

```
> wc -l student-a/signup.html student-b/signup.html student-a/CLAUDE.md student-b/CLAUDE.md
      54 student-a/signup.html
      54 student-b/signup.html
      36 student-a/CLAUDE.md
       4 student-b/CLAUDE.md

> diff -q student-a/signup.html student-b/signup.html
(silent — identical)

> grep -c '^### 20' student-a/CLAUDE.md student-b/CLAUDE.md
student-a/CLAUDE.md:3
student-b/CLAUDE.md:0

> grep -c 'Dangerous middle' student-a/CLAUDE.md student-b/CLAUDE.md
student-a/CLAUDE.md:3
student-b/CLAUDE.md:0

> grep -c 'Constraint added' student-a/CLAUDE.md student-b/CLAUDE.md
student-a/CLAUDE.md:3
student-b/CLAUDE.md:0

> grep '^### ' student-a/CLAUDE.md
### 2026-08-14 — the email wall
### 2026-08-21 — the server-side Thursday
### 2026-08-28 — the welcome header
```

## What the runs gave the film

1. **Same code, different CLAUDE.md.** Both students turn in the same 54-line `signup.html`. From the code alone, they are indistinguishable. The `CLAUDE.md` is not.
2. **The file's decisions leak into the next session.** Student A's Claude refused a new ask and quoted a Lessons Learned entry **by date** as its reason. It didn't compute the rule from first principles; it looked it up in the file the student had written. Student B's Claude worried in general terms about client-side security and asked what to build.
3. **A fresh Claude, given only the two files, scored them 16/16 and 0/16.** Not from the code — from the record of decisions. The file is inspectable. It is gradeable. It is the assessment artefact.

That is what the film is about: AI can generate the code. It cannot generate the record of decisions the human made — and the CLAUDE.md, dated and specific, is that record.
