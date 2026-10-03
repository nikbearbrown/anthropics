# BUILD-LOG — cc-subagent-context

cc-explainer · Claude Code 101 · tier `02-plan-rewind-subagents` · Liam, in for Bear · built 2026-09-09.

**The experiment.** One tiny build (add `late_penalty(days_late, base_score)` to `grader.py` using the study group's late-submission rules from five policy docs) under two conditions, each a fresh headless `claude -p` run against a byte-identical scratch project:

- **Inline** — main session Reads all five policies. Result: `late_penalty` implemented, four tests pass, and `3,266` tokens of policy content live in the main session's KV cache for the remainder of the run. Total `cache_creation_input_tokens`: **71,416**.
- **Subagent** — one `Agent` call summarises the five policies (subagent's own window). The summary lands in main at **435 tokens** — a working demonstration of the isolation the concept promised. But Claude 2.1.150's default is to double-check: it then opened all five policies in the main session anyway, adding **3,170 more tokens** on top. The mechanism worked; the discipline didn't. Total: **78,069**.

Both runs produced correct code and passing tests (`python3 -m unittest test_grader -v` → OK, 4 tests). The two `grader.py` versions ship different implementations of the same rules (inline used a per-day `if/elif` cascade; subagent used a dict lookup with a 50% cap) — both computed the one-day-late case as `base − 10%`.

**Reframing.** The concept sheet's title claim ("Subagent Saved 48%") is not what happens by default in Claude Code 2.1.150. The subagent DOES save context — its 435-token return is 7.5× smaller than reading the five files directly — but only if the human enforces the boundary. The film keeps the title, makes the reframing explicit ("the subagent isolates; only the human enforces"), and turns the falsifiable line into the acid test: *a run where Claude, given the summary, refuses the redundant read on its own.*

**Compile.** ONE pass:

```
GATE-F           PASS
GATE-L           PASS
GATE-BANNED-CARD PASS
GATE-SWEEP-WARN  PASS
GATE-G           PASS
GATE-V           frames=28  BLOCKER=0  STRUCTURAL=0  COSMETIC=0   PASS
GATE-T           PASS (§8.10 min-contrast: B03 0.45, B06 0.24, BVDT 0.62)
GATE-SHARPNESS   PASS  median LV=690.3
GATE-BOOKEND     PASS
GATE-AUDIO       PASS  mean_volume −23.6 dB
GATE-MASTER      PASS  3840×2160  24fps  yuv420p  h264  278.6s
GATE-LOUDNESS    PASS  −24.16 LUFS  tp=−2.88 dBTP
GATE-RECEIPTS    PASS
content-check    PASS
frame-check      PASS
lane-check       PASS
```

Two advisories, neither blocking:
- `SKIN LINT B00`: cold open is `CCSession` where COLD OPEN LAW for palette=claude prefers `ClaudeComposerAsk`. GATE BOOKEND's `cc-explainer` override permits CC surfaces in the cold open (per SKILL.md), so this stays.
- Motion histogram: `type` at 57% (over the ~40% pantry cap). This is a CC-explainer where the body IS the typing session; the cap is a general-explainer heuristic. Leave as-is.

Frames spot-checked at 85% of each dense beat (B01, B03, B05, B06, B07, B08, BVDT): all read clean — no clipping, no overprint, ledger and score rows within measured budgets, mechanism topology on B03 legible, verdict paginated correctly (6 lines, 3 pages, 2/2/2).

**Master**: `cc-subagent-context.mp4` — 278.6 s (4:39), 3840×2160, h264/yuv420p, 18.5 MB, in the reel folder.

**Not published.** TOPOST only via `post`, only on ask.
