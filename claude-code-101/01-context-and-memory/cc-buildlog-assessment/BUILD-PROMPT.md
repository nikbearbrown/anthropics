# BUILD-PROMPT — cc-buildlog-assessment

This is the paste-into-any-CLI briefing for rebuilding `cc-buildlog-assessment` from the sources in this folder.

## What this reel is

`cc-explainer` · Claude Code 101 · tier 01-context-and-memory · film 04 · slug `cc-buildlog-assessment`.

Concept: **CLAUDE.md is the assessment artefact.** Two students turn in the same working `signup.html`; from the code alone they are indistinguishable, but their `CLAUDE.md` files differ (36 lines vs 4). A same-one-sentence ask to both surfaces the difference — Student A's Claude quotes a dated Lessons Learned entry, Student B's Claude raises a general concern without a project rule to cite. A third Claude, given only the two files, scores them 16/16 and 0/16.

Operator: Liam, in for Bear (Kokoro `am_onyx`, free/local). Register: Teardown.

## Build spine (13 beats)

```
B00   COLD OPEN                    CCSession   the setup (ls, wc, diff)
BIDEA THE IDEA                     BrutalistHesitantWriter   'code' → 'file'
BDEFS DEFINITIONS                  CCDefinitions  five terms
B01   SAME ASK — STUDENT A         CCSession   refusal citing 2026-08-14
B02   WHY IT KNEW                  CCPlainShell   the three dated headers + Aug-14 body
B03   SAME ASK — STUDENT B         CCSession   Read + general worry + AskUserQuestion
B04   VERIFY — THE FILE IS IT      CCSession   diff, grep -c ×3
B05   THE GRADER                   CCSession   two Reads → 16/16 and 0/16
B06   CONDUCT (Boondoggle)         CCBoondoggleScore   6 steps, dangerousMiddle=2
B07   HUMAN (Ledger)               CCHumanLedger   4 CAN/SHOULD × 4 MUST/SHOULD
BVDT  VERDICT                      ClaudeVerdictArtifact   4 lines incl. FALSIFIABLE
BHTF  YOUR TURN                    ClaudeComposerAsk   greeting "Your turn."
BOUT  OUTRO                        ClaudeTitleOutro   exact title, @NikBearBrown
```

## To rebuild from these sources

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books
REEL=anthropics/claude-code-101/01-context-and-memory/cc-buildlog-assessment

# 1. sanity: the three real runs are already in $REEL/evidence/ and SESSION.md
ls "$REEL"/evidence/  # run-a.jsonl, run-b.jsonl, run-grader.jsonl, verify.txt, both CLAUDE.mds

# 2. re-author the sheet (regenerates beat_sheet.json from author_sheet.py)
python3 "$REEL"/author_sheet.py       # prints "13 beats — est ~334s", no warnings

# 3. audio (Kokoro am_onyx, free)
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py "$REEL"

# 4. paperwork gate
python3 brutalist-art/runtime/qc/factcheck_check.py "$REEL"      # must print "clean"

# 5. review cut → clean master
./brutalist-art/art run   "$REEL"
./brutalist-art/art final "$REEL"
```

## To re-run the sessions (if evidence is missing or stale)

Each session runs headless from the folder that owns its `CLAUDE.md`. See `PROMPTS.md` for the full command; the ask is one sentence and identical for Student A and Student B. Rerunning may produce slightly different phrasings — update `SESSION.md`, `FACTCHECK.md`, and any affected text blocks in `author_sheet.py`.

## Not published

TOPOST via `post` only on explicit ask. Master stays in `$REEL/`.
