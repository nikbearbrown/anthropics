# SHOTLIST — cc-rewind-respec

17 beats · 16:9 · 5:11 measured (Kokoro am_onyx). Every non-terminal beat names its `leaves_terminal_because`.

| # | Beat | Component | Mode / palette | What lands |
|---|---|---|---|---|
| 00 | B00 · COLD OPEN — THE DRIFT | CCSession | default, CC | FF3 dedupe.py + unittest OK + Liam's `dedupe([1,1.0])` returns `[1, 1.0]` |
| 01 | BIDEA · THE IDEA | BrutalistHesitantWriter | CC (bg #1F1E1B, ink #F2F0E9, accent #D97757), serif 78 | 4 lines; "fix it again" reconsidered into "respecify it" |
| 02 | BDEFS · DEFINITIONS | CCDefinitions | CC | fix-forward / /rewind / respecify / context pollution / negative constraint |
| 03 | B01 · FF1 — THE VAGUE ASK | CCSession | accept-edits, CC | Ask + Reads + Write dedupe.py |
| 04 | B02 · FF1 — VERIFY | CCSession | default, CC | `cat dedupe.py` (linear scan) + unittest OK |
| 05 | B03 · FF2 — SPEED IT UP | CCSession | accept-edits, CC | `--resume` ask + Write two-branch + unittest OK + Claude summary |
| 06 | B04 · FF3 — SIMPLER — THE CORRECTION | CCSession | accept-edits, CC | `--resume` ask + Write repr one-liner + `cat` + unittest OK |
| 07 | B05 · FF3 — VERIFY, AND THE DRIFT | CCSession | default, CC | Liam's `dedupe([1,1.0])` → `[1,1.0]`; `dedupe([True,1])` → `[True,1]` — the check the tests didn't run |
| 08 | B06 · WHY IT DRIFTED | CCPlainShell | zsh, dark | session-context log growing across three resumes |
| 09 | B07 · REWIND — RESTORE THE CHECKPOINT | CCPlainShell | zsh, dark | `git reset --hard f5ef78b` + new session id; `# no --resume. a new claude -p is /clear.` |
| 10 | B08 · RESPEC — THE FAILURE AS CONSTRAINT | CCSession | accept-edits, CC | 4-part respec prompt + Reads + Write |
| 11 | B09 · RESPEC — VERIFY | CCSession | default, CC | unittest OK + `[1]` + `[True]` |
| 12 | B10 · CONDUCT — THE BOONDOGGLE SCORE | CCBoondoggleScore | CC | 7 steps, dangerous middle = step 4; PF·1 PA·1 IJ·1 TO·0 EI·0 |
| 13 | B11 · HUMAN — THE LEDGER | CCHumanLedger | CC | 4 MUST/SHOULD human · 4 CAN/SHOULD AI; closing lands last |
| 14 | BVDT · VERDICT | ClaudeVerdictArtifact | CC | verdict.md · 4 lines · last line FALSIFIABLE |
| 15 | BHTF · YOUR TURN | ClaudeComposerAsk | CC | greeting "Your turn."; composer types the recipe prompt |
| 16 | BOUT · OUTRO | ClaudeTitleOutro | CC | Title + @NikBearBrown + mascot; "Liam, in for Bear." |

Every asset is written by the pipeline from `beat_sheet.json` props — no pantry stills, no image-to-video, no clips folder needed. `clips/` and `media/` are placeholders per the folder contract.
