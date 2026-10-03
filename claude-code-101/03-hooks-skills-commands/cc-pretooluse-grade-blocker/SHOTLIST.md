# SHOTLIST — cc-pretooluse-grade-blocker

15 beats · 16:9 · Liam (Kokoro `am_onyx`) on every beat · measured ≈ 296 s (4:56).

| Beat | Pattern | What is on screen | Source of the block content |
|---|---|---|---|
| B00 | CCSession (mascot off) | Bare run: 4 prompt blocks (the ask), Read students.csv, Write summary.md, three grade lines | `SESSION.md` §Run 1 |
| BIDEA | BrutalistHesitantWriter | "A note in CLAUDE.md is a hope" reconsidered to "hook" | authored per SKILL |
| BDEFS | CCDefinitions | 5 terms: PreToolUse · tool_input · matcher · exit 2 · settings.json | authored |
| B01 | CCSession (mascot off) | Build ask (5 prompt blocks), Read BUILD-ASK.txt, Bash mkdir, Write hooks/block-grades.py, "36 lines · stdlib · 2 regexes" | `SESSION.md` §Run 2 |
| B02 | CCSession (mascot off) | The refusal: "Also write .claude/settings.local.json" → permission dialog quote → "Drop this JSON in yourself." | `run-build-resume.jsonl` |
| B03 | CCPlainShell | `cat .claude/settings.local.json` (matcher + command) + `wc -l` → 15 | `evidence/settings.local.json` |
| B04 | CCSession (mascot off) | Three unit tests: bad.json (exit 2 + stderr), quantity.json (exit 0 "top 15%"), ok.json (exit 0) | SESSION.md VERIFY |
| BFLOW | FlowDiagram (skin=claude) | Six nodes (claude → harness → hook + stdin → exit 2 → denied → retry) | authored from run-hooked |
| B05 | CCSession (mascot off) | Hooked run: Read csv, Write blocked (is_error), stderr message, Read block-grades.py | `run-hooked.jsonl` |
| BSHOW | CCPlainShell | wc bare vs hooked (13/17), grep grade counts (3/0), footer line about the teacher | evidence + counts |
| BCONDUCT | CCBoondoggleScore | 6 steps, dangerous middle = step 3 (Claude tries to wire, refused), tally PF/PA/TO | authored from SESSION |
| BHUMAN | CCHumanLedger | AI: draft/read/retry/refuse-to-wire · Human: define/pick/wire/unit-test | authored |
| BVDT | ClaudeVerdictArtifact | 4 lines, last one FALSIFIABLE | authored |
| BHTF | ClaudeComposerAsk | Your Turn prompt read aloud | authored |
| BOUT | ClaudeTitleOutro | Title restated · @NikBearBrown · Liam, in for Bear | LOCK |
