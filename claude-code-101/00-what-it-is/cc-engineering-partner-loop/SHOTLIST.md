# SHOTLIST — cc-engineering-partner-loop

| Beat | Duration | Surface | Content |
|---|---|---|---|
| B00 | ~20s | CCSession dark | bare run: ask "Fix the failing tests." → Read × 2 → Bash unittest (fail) → Claude line → Edit → Bash unittest (OK) |
| BIDEA | ~24s | BrutalistHesitantWriter | text: "Claude Code is a code generator." → reconsidered "generator" → "partner"; 4 lines, CC palette |
| BDEFS | ~18s | CCDefinitions | oracle, plan, minimal diff, scope, partner loop |
| B01 | ~19s | CCSession | Liam's verify: `!python3 -m unittest -v` → 5 OK; `!git diff --stat` → 7 ins/1 del; `!grep -c 'raise ValueError'` → 2 |
| B02 | ~15s | CCSession | Partner ask + status:Planning; Reads only (Edit withheld) |
| B03 | ~24s | CCSession | plan block (4 items on ranges.py) + diff block (5 add / 1 del) |
| B04 | ~11s | CCSession | "Plan approved. Apply the diff exactly." → Edit → Bash unittest → OK |
| B05 | ~15s | CCPlainShell | grep on docstring + grep on raises → drift |
| B06 | ~17s | CCSession | re-prompt: docstring-only edit; diff shows one docstring line; unittest OK |
| BFLOW | ~26s | FlowDiagram (claude) | 5 nodes: ORACLE → ASK → PLAN → DIFF → VERIFY; return arrow "decide" dashed |
| BSHOW | ~12s | CCPlainShell | `python3 -m unittest test_ranges -v` full 10-line output |
| BCND | ~30s | CCBoondoggleScore | 6 steps, dangerousMiddle=3, distribution shown |
| BHMN | ~30s | CCHumanLedger | 4 MUST/SHOULD human · 4 CAN/SHOULD AI · closing line |
| BVDT | ~24s | ClaudeVerdictArtifact | 4 verdict lines, last is FALSIFIABLE |
| BHTF | ~15s | ClaudeComposerAsk | greeting "Your turn."; paste-ready oracle-first prompt |
| BOUT | ~4s | ClaudeTitleOutro | title re-read; @NikBearBrown; no subline |

Total narration estimate: **318s / 5:18** (Kokoro `am_onyx` at ~2.9 wps).

Compile master expected: ~5:20–5:40 after silence padding at bookends.
