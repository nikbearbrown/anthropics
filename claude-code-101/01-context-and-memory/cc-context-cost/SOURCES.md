# SOURCES — cc-context-cost
Primary: `SESSION.md` — one real eight-message headless session (Claude Code 2.1.150, 2026-09-09) on the gradebook repo; per-call usage in `evidence/turns.json`; raw `turn*.jsonl`; `session.diff`. Messages 9–12 of the same session feed `cc-clear-vs-compact` and `cc-context-check`.
Concept: `claude-cowork--claude-liam-stop-hitting-claude-limits` ("Message 30 Costs 31 Times More") — the mechanism is kept and measured; the multiplier is corrected by the receipts; its habit clusters are out of scope here.
Product facts: prompt caching (cache reads billed at a fraction of fresh input) — Anthropic API pricing; `/context` breakdown from the same session.
Doctrine: CONDUCT ← `info-7375-conducting-ai`; HUMAN ← `info-7375-irreducibly-human`.
Interface: the CC kit; `CCDefinitions`, `CCPlainShell`, `CCBoondoggleScore`, `CCHumanLedger`; `BrutalistHesitantWriter` (CC palette). Narration Kokoro `am_onyx`, Liam in for Bear.
