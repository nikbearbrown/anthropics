# FACTCHECK — cc-rewind-respec

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (four real headless runs) and `evidence/`.

**Verification boundary.** Every number, sentence, and code line on screen comes from the four runs' stream-json (`run-ff1.jsonl`, `run-ff2.jsonl`, `run-ff3.jsonl`, `run-respec.jsonl`), the two saved dedupe.py versions (`evidence/dedupe.ff3.py`, `evidence/dedupe.respec.py`), the test file, `SPEC.md`, `ask.txt`, and Liam's plain-shell drift check (`evidence/drift.txt`). Claude's sentences are verbatim spans. Product strings (`--resume`, `--session-id`, `/clear`, `/rewind`) are the CLI's own words; SKILL.md is the source for "a new `claude -p` IS `/clear`". No datable values are shown or spoken (model versions, prices, timestamps).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | `python3 -m unittest test_dedupe.py` → 3 tests, OK | PASS | verified live against `evidence/dedupe.ff3.py`; identical to `run-ff3.jsonl` final Bash tool | — |
| 2 | B00, B04 | The FF3 `dedupe.py`, verbatim: `return list({repr(x): x for x in items}.values())` | PASS | `evidence/dedupe.ff3.py`; `run-ff3.jsonl` Write payload | — |
| 3 | B00, B05, B09 | `dedupe([1, 1.0])` → `[1, 1.0]` on FF3; `[1]` on respec | PASS | `evidence/drift.txt` (ran against `dedupe.ff3.py`); Liam's post-respec check in SESSION.md | — |
| 4 | B00 | "the caveat is right there" / Claude's own reply | PASS | `run-ff3.jsonl` assistant text: "`repr` is a canonical-string proxy for equality, not equality itself…" | — |
| 5 | BIDEA | "Three fixes in, tests still pass. And the diff has drifted." | PASS | SESSION.md summary + `evidence/drift.txt` | — |
| 6 | BDEFS | Definitions of fix-forward, /rewind, respec, context pollution, negative constraint | PASS | fix-forward: `--resume` behavior per Claude Code docs (session id preserves conversation); /rewind: SKILL.md "the interactive UI: plan-mode cards, the IDE, rewind"; a new `claude -p` IS `/clear`: SKILL.md, quoted verbatim in narration; context pollution & negative constraint: concept-sheet framing (`claude-code--claude-liam-vox-rewind-respec/beat_sheet.json` B04) | — |
| 7 | B01 | The ask (verbatim); Reads on test_dedupe.py, dedupe.py, SPEC.md; Write dedupe.py | PASS | `evidence/ask.txt`; `run-ff1.jsonl` tool sequence (opening `Bash ls` shown; two `python`-not-in-fence denials omitted for height per exemplar convention) | — |
| 8 | B02 | The FF1 dedupe.py, verbatim; unittest → OK | PASS | `run-ff1.jsonl` Write payload; final Bash tool succeeded (after two `python` denials — omitted for height) | — |
| 9 | B02 | "In is Python's equality operator, so lists work" | PASS | Claude's own final text in `run-ff1.jsonl`: "…using `in` (which uses equality, so lists work)" | — |
| 10 | B03 | The FF2 follow-up (verbatim); Write; unittest → OK; "n squared" spoken as "n squared" | PASS | `run-ff2.jsonl`. The narration says "n squared"; the on-screen prompt block reads `That's O(n squared). Speed it up.` to avoid rendering issues with the superscript — the meaning and Claude's interpretation are unchanged | — |
| 11 | B03 | Claude's summary: "n) for hashable items; linear scan only for unhashable" | PASS | verbatim (split into two 44-char blocks): "Now O(n) amortized for hashable items (set membership), falling back to linear scan only for the unhashable subset." | — |
| 12 | B04 | "Simpler. One data structure." (verbatim ask) + Write repr one-liner + unittest → OK | PASS | `run-ff3.jsonl` — ask, Write payload, final Bash success | — |
| 13 | B05 | `[1, 1.0]` and `[True, 1]` outputs against FF3 code | PASS | `evidence/drift.txt` (ran live 2026-09-09 against `dedupe.ff3.py`) | — |
| 14 | B06 | Session-context growth: three PASS handoffs plus the last diff | PASS | derived from the three assistant-text spans in `run-ff{1,2,3}.jsonl`; the mechanism (context pollution) is the concept-sheet's B04 framing | — |
| 15 | B07 | `git reset --hard f5ef78b` → "HEAD is now at f5ef78b buggy start"; new UUID `96c45930-…`; "a new `claude -p` is `/clear`" | PASS | shell output verified live; UUID matches `evidence/sid-respec.txt`; SKILL.md quote verbatim | — |
| 16 | B08 | The respec prompt broken across four prompt blocks; Reads; Write | PASS | `evidence/respec-ask.txt`; `run-respec.jsonl` tool sequence. The respec is shown as four short prompt blocks for legibility; the full text is in the ask file and is quoted verbatim in the narration when Liam reads it | — |
| 17 | B09 | unittest → OK; `dedupe([1,1.0])` → `[1]`; `dedupe([True,1])` → `[True]` | PASS | live-verified against `evidence/dedupe.respec.py`; captured in SESSION.md VERIFY | — |
| 18 | B10 | Seven-step Boondoggle Score with dangerous middle = step 4 | PASS | maps 1:1 to SESSION.md; capacity tally (PF·1, PA·1, IJ·1, TO·0, EI·0) matches | — |
| 19 | B11 | Ledger rows — AI/human capacities named against this session, not principle | PASS | each row references a real event in this session (drift catch = PA; rewind choice = IJ; Claude's caveat = "name a caveat in its reply") | — |
| 20 | BVDT | Verdict lines quote/summarise the receipts verbatim | PASS | rows 1–3, 12; falsifiable line names a check any viewer can run | — |
| 21 | BHTF | Viewer's prompt | EXEMPT | instruction | — |
| 22 | all | Model/version strings, prices, timestamps ("Claude Code 2.1.150", "$0.31") | EXEMPT | recorded in SESSION.md and FACTCHECK, never spoken or shown on screen | — |
| 23 | metadata | slug, title, playlist, tier, folderLabel, handle, palette, register | EXEMPT | authoring metadata; not on screen | — |
