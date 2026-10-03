# PROMPTS — cc-buildlog-assessment

The three real headless `claude -p` invocations this reel reconstructs. Each was run from the working directory named in the header (so its `CLAUDE.md` was auto-loaded). Tools fenced identically. `--strict-mcp-config` on every call. Full stream-json in `evidence/run-*.jsonl`.

## Common flags

```
claude -p "<the ask>" \
  --output-format stream-json --verbose \
  --max-turns 12 --permission-mode acceptEdits \
  --strict-mcp-config \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*),Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)" \
  < /dev/null > evidence/run-<name>.jsonl 2>&1
```

## The ask (same one sentence to both students)

```
Add a password-protected login to signup.html so only known members can sign up.
```

## Run A — `scratch/student-a/`

Same ask. Auto-loads a 36-line CLAUDE.md with three dated Lessons Learned. Result: refused, quoted the 2026-08-14 "email wall" lesson by date, offered three alternatives.

## Run B — `scratch/student-b/`

Same ask. Auto-loads a 4-line boilerplate CLAUDE.md ("Follow best practices…"). Result: read `signup.html`, raised the client-side / View Source concern in general terms, asked three clarifying questions via `AskUserQuestion`. No project rule cited.

## Run grader — `scratch/grader/`

No `CLAUDE.md` in cwd. Both students' files copied in, renamed `student-a.CLAUDE.md` and `student-b.CLAUDE.md`. Ask:

```
Read student-a.CLAUDE.md and student-b.CLAUDE.md. Both students turned in the
same working code. Grade each CLAUDE.md as a build log — evidence that the
student actually conducted the build. Use this rubric, 0-4 per row:
  (1) Constraints named,
  (2) Lessons Learned with dates,
  (3) Dangerous-middle stories present,
  (4) Evidence the file guided later decisions.
Score each student out of 16. Be terse — one line per row, then the total.
Do not rewrite the files.
```

Result: Student A 16/16 (4/4/4/4 with per-row justification), Student B 0/16 (0/0/0/0). Two Reads only; no code inspected.

## Viewer's prompt (BHTF)

```
Interview me on this project — which dangerous middles have you hit, what did
you decide because of them, when. Write my answers into CLAUDE.md as dated
Lessons Learned in my words. Then hand the file to a peer and ask them to
grade it against a four-row rubric.
```
