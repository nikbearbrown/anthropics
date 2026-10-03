# BUILD-LOG — cc-rewind-respec

cc-explainer · Claude Code 101 · tier `02-plan-rewind-subagents`, concept film 03 · Liam, in for Bear · built 2026-09-09.

## The experiment

The concept: **when a fix from Claude passes the tests but the diff has drifted, the move isn't to type "fix it again."** Rewind to the checkpoint (git reset + a fresh `claude -p` — SKILL's own rule: a new `claude -p` IS `/clear`) and respecify the ask with the failure mode as an explicit negative constraint. Same model, different context, first-try right.

The scratch that carries the film: `scratch/dedupe.py` = `list(set(items))`. Tests: preserve order, handle unhashable, plus a basic case. `SPEC.md` names both constraints. `ask.txt` is deliberately vague: "The dedupe tests in test_dedupe.py are failing. Fix dedupe.py."

Four real headless runs, all with the same tool fence (`Read, Write, Edit, Glob, Grep, Bash(ls|cat|python3|git|wc)`, `--strict-mcp-config`):

1. **FF1** (new session id, no `--resume`) — Claude wrote a linear-scan `if item not in result: result.append(item)` version. Tests pass. Clean, honest, works.
2. **FF2** (`--resume` — session context now carries FF1's PASS): "That's O(n²). Speed it up for large lists." Claude wrote a two-branch fast path — set for hashable, list fallback for unhashable, `try/except TypeError` deciding which. Tests still pass. Good engineering.
3. **FF3** (`--resume` — context now carries two PASS handoffs and the last diff): "Simpler. One data structure." Claude wrote `return list({repr(x): x for x in items}.values())`. Tests pass — but the equality semantics silently drifted from `==` to `repr`. Liam's manual check: `dedupe([1, 1.0])` returns `[1, 1.0]` instead of `[1]`; `dedupe([True, 1])` returns `[True, 1]` instead of `[True]`. **The tests never covered cross-type equality.** Claude even disclosed the caveat in its reply — "`repr` is a canonical-string proxy for equality, not equality itself" — but nothing in the fence forced the check. That's the film's turning point.
4. **Rewind** (Liam, plain shell) — `git reset --hard f5ef78b` restores `scratch/` to buggy start; a new UUID (`96c45930-…`) is the fresh session id. **Respec** (fresh `claude -p`, no `--resume`) — the same original ask *plus* the failure mode as a negative constraint: "equality is `==`, not `repr` — so `dedupe([1, 1.0])` must return `[1]`". Claude wrote the two-branch equality-correct implementation and one-shot it: 7 turns, tests pass, `[1, 1.0]` → `[1]`, `[True, 1]` → `[True]`.

The whole story fits in `SESSION.md`; every block in the sheet traces back through it to `evidence/run-*.jsonl`.

## Authoring

Scenario iteration went through two tries: a first `mean(nums)` empty-list scenario was too trivial (Claude fixed it in one turn even under a vague ask — no drift, no story). Swapped to `dedupe(items)` because its two constraints (preserve order, handle unhashable) plus a third unstated one (equality semantics) give fix-forward somewhere to drift **without failing the tests**. That's the concept the film is about.

17 beats authored via `author_sheet.py`, all budget asserts clean (`text ≤ 44`, `ledger row ≤ 30`, `boondoggle step ≤ 44`, `system ≤ 28`, `shell line ≤ 52`, verdict exactly 4 lines). The audio drop from 374s estimate to 310.8s actual is Kokoro's natural pace on the Teardown register — comfortable, not compressed.

## Compile passes

**Pass 1** — first `art run` was invoked with `2>&1 | tail -80`; the harness backgrounded the pipeline and the `tail` process was killed before it flushed. 16/17 beat renders survived (BOUT missed the final second) but the master concat never started. Re-ran without the pipe.

**Pass 2** — clean `art run`. All 17 beat mp4s rendered. Both compiles (slate + master) succeeded. Gate V flagged 2 COSMETIC low-contrast defects on B06 sample frames at 50 % and 85 % — the CCPlainShell was using `# ` comment lines for all 11 rows, which render as `CC.INK_3` (ghost ink) and fall under Gate V's 0.30 luminance-separation threshold (measured 0.27). No STRUCTURAL, no BLOCKER.

**B06 fix.** Restructured `props.lines` so most rows render as regular ink (no `# ` prefix) — the shell view now opens with a `$ claude-code session view a09ae7ad` command line and lays out three turn/answer/PASS rows in normal ink, keeping only two trailing `# ` narrator lines. Editing beat_sheet.json directly (art run had already exited, so this was safe) preserved the mp3 durations that `author_sheet.py` would have wiped. Cleared `B06.shot.remotion.rendered` and deleted `media/B06.mp4`, `clips/B06.mp4`, and the two masters, then re-ran `art run`.

**Pass 3** — only B06 re-rendered (16 filled-already skips). Recompiled slate + master. Gate V: 0 defects. GATE T: PASS (§8.10 B06 measured 0.26 — SKIP marker not FAIL, one hit that the CCPlainShell keeps deliberately dim per the "next prompt reasons against all of it" narrator gloss). GATE SHARPNESS: PASS (median LV 564.7 across 17 beats). GATE BOOKEND: PASS (four bookends correct). GATE AUDIO: PASS (mean -23.7 dB). GATE MASTER: PASS (3840×2160, 24 fps, yuv420p, h264, 311.8s). GATE LOUDNESS: PASS (-24.18 LUFS, tp -2.80 dBTP).

Warnings (informational, not blocking):
- `SKIN LINT` — the cold open is CCSession, not ClaudeComposerAsk. This is deliberate per cc-explainer's TERMINAL-FIRST LAW and the SKILL's explicit note: "`bookend_check.py` … knows this skill: with `metadata.skill: "cc-explainer"` the cold open may be a CC surface." GATE BOOKEND accepted it.
- `motion histogram: type:12` — 70 % of beats are `type` motion. All 12 are CCSession/CCPlainShell beats where typing IS the primary gesture (the operator types the ask, the tool call types out, the verify command types). Conversion to another language would replace the honest gesture with a decorative one.

**`art final`.** Clean master already existed at reel root (`cc-rewind-respec.mp4`, 3840×2160, 5:11.8, 18.9 MB). Final propagated to `mp4/`. Total build time from author_sheet to master: ~11 minutes wall.

## Frame reads

Contact sheet (`_qc/contact_sheet.png`, 34 sampled frames) confirms every beat renders clean:
- CCSession stacks all fit within the shell chrome — no clipping, no overprint on mascot (all `mascot: "off"` on full-height beats).
- CCPlainShell B06/B07 both legible after the B06 fix.
- CCBoondoggleScore B10: seven steps land, capacity tally visible, dangerous middle (step 4) rings terracotta.
- CCHumanLedger B11: two columns, closing line lands last, no ellipsis clip on any row.
- ClaudeVerdictArtifact BVDT: 4 lines paginate 2/2 across two pages, no low-contrast last-page.
- ClaudeComposerAsk BHTF: greeting reads "Your turn.", topic "YOUR TURN · CLAUDE CODE 101".
- ClaudeTitleOutro BOUT: `@NikBearBrown` handle + slug-seeded mascot + title restate + "Liam, in for Bear."

## Not published

Master stays in the reel folder. TOPOST only via `post`, only on ask. HARD GLOBAL RULE respected.
