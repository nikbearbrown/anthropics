# BUILD-PROMPT — cc-plan-mode-interruption

The one-page paste-in you would hand another Claude Code session to reproduce this reel from the same concept folder.

```
Build a cc-explainer film called "Plan Mode: Freeze Before the Byte Changes" (slug cc-plan-mode-interruption)
for the Claude Code 101 series. The film's argument is that plan mode is a freeze, not a pause: same one-sentence
ask, run twice — first with --permission-mode acceptEdits, then with --permission-mode plan. Under acceptEdits,
Claude Code changes three files and deletes one. Under plan, Claude produces a plan document (via the ExitPlanMode
tool call) and writes zero bytes to disk. When the plan proposes to delete a file the user wants kept, the human
re-prompts in plan mode (--resume), and Claude issues a revised plan — still zero bytes changed.

Method:
1. Build a scratch classroom-site repo: index.html (landing), schedule.html (the reading list),
   notes.md (teacher-only), README.md, ask.txt. Commit the baseline.
2. Run three real headless sessions with `claude -p ... --output-format stream-json --verbose
   --max-turns N --strict-mcp-config --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*)
   ,Bash(cat:*),Bash(python3:*),Bash(git:*),Bash(wc:*)"`, using --session-id / --resume:
   Run A (acceptEdits), git reset --hard, Run B (plan), Run C (--resume, plan). Save every
   *.jsonl into evidence/.
3. Save the plan text from each plan-mode run by pulling the `plan` argument from the
   `ExitPlanMode` tool_use in the JSONL; store as evidence/plan-b.md, evidence/plan-c.md.
4. SESSION.md pastes the three transcripts, tools, verbatim spans, and Liam's plain-shell
   git checks. FACTCHECK.md walks every claim on screen back to SESSION.md.
5. Author the beat sheet (author_sheet.py) on the cc-three-files pattern: B00 cold open of
   Run A (CCSession, accept-edits), BIDEA (BrutalistHesitantWriter, 'pause' → 'freeze'),
   BDEFS (CCDefinitions, four terms), B01 bare-verify CCSession, B02 plan-run CCSession,
   B03 plan-verify CCSession (git diff empty), B04 the plan itself on CCPlainShell,
   B05 the correction CCSession, B06 CCBoondoggleScore, B07 CCHumanLedger, BVDT (4 lines,
   FALSIFIABLE last), BHTF ("Your turn."), BOUT ClaudeTitleOutro. Every text block ≤44 chars,
   ledger rows ≤30, score steps ≤44, verdict 4 or 6 lines, mascot 'off' on full stacks.
6. python3 runtime/scripts/generate_audio_kokoro.py <reel> — voice is am_onyx (Liam).
7. python3 runtime/qc/factcheck_check.py <reel> — must print `clean`.
8. ./brutalist-art/art run <reel> → read _qc/REPORT.md & TYPECHECK.md → fix in-place →
   ./brutalist-art/art final <reel>.
9. BUILD-LOG.md summarises what the three runs gave the film and every compile pass; write
   CC-BUILT.txt into the *concept* folder with the reel's absolute path.

Never publish. Master stays in the reel folder. TOPOST only on explicit ask.
```
