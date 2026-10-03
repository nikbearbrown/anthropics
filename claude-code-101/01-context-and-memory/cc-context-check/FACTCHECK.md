# FACTCHECK — cc-context-check

Status: PASS — checked 2026-09-09 by the build session against `SESSION.md` (message 12 of one real session) and `evidence/context-output.md`.

**Verification boundary.** Every row on screen is a verbatim line of the product's `/context` output (`evidence/context-output.md`); the receipt it is compared to is `evidence/turns.json` (message 10). The definitions are high-level product descriptions. The model id appears in the product's own output and is shown on screen as printed, never spoken.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | `/context` headless prints "## Context Usage", "**Model:** claude-opus-4-7", "**Tokens:** 36.7k / 1m (4%)" | PASS | `evidence/context-output.md`; `turn12.jsonl` result | — |
| 2 | B00 | "right after the compact" | PASS | message 9 was `/compact`; message 12 follows messages 10–11 in the same session (`../cc-context-cost/SESSION.md`) | — |
| 3 | B00 | Model id on screen | EXEMPT | the product's own output line, shown as printed; never spoken (datable) | — |
| 4 | BIDEA, BDEFS | "a million tokens" window; the autocompact buffer is reserve for compaction | PASS | the output's "/ 1m" and "Autocompact buffer 33k" rows; Claude Code auto-compacts as the window nears full | — |
| 5 | B01 | The category rows: System prompt 9k · System tools 8.9k · deferred 19.2k · Memory files 465 · Skills 4.2k · Messages 14.2k · Free space 930k · Autocompact buffer 33k | PASS | `evidence/context-output.md` (the Custom agents row, 329, is omitted on screen for height; percentages as printed) | — |
| 6 | B01 | "listed but not loaded until needed" (deferred tools) | PASS | the product's own category name "System tools (deferred)"; the ToolSearch mechanism loads deferred tool schemas on demand | — |
| 7 | B01 | "CLAUDE.md: four hundred sixty-five — the file from three films ago" | PASS | Memory Files table: the gradebook's CLAUDE.md, 465 tokens; it is the file written in `cc-claude-md` | — |
| 8 | B02 | Headline 36.7k vs receipt 36,670 on message 10 | PASS | `context-output.md`; `turns.json` | — |
| 9 | B03 | Five steps; tally PF 1 · PA 1 · IJ 1 · TO 1 · EI 0; "~30k before I type" | PASS | fresh-session first call measured 28,676 (`turns.json`, turn11-fresh) | — |
| 10 | B04 | "It can compact on its own at the edge" | PASS | the Autocompact buffer row; Claude Code's auto-compaction | — |
| 11 | BVDT | Verdict lines | PASS | rows 1, 5, 8 | — |
| 12 | BHTF | The viewer's prompt | EXEMPT | instruction | — |
