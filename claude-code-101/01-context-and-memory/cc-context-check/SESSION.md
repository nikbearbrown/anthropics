# SESSION.md — cc-context-check

The real Claude Code run this reel reconstructs (REAL-SESSION LAW). Message 12 of the session recorded in `../cc-context-cost/SESSION.md` (same session id, Claude Code 2.1.150, 2026-09-09, `gradebook` repo), run after `/compact` (message 9) and one more question (message 10). Raw stream-json: `evidence/turn12.jsonl`; the command's full output: `evidence/context-output.md`; the whole session's per-call context: `evidence/turns.json`.

## Message 12 — `/context` (resumed session)

**Liam typed:** `/context`

- **RESULT:** success; the product's own report, verbatim (first two tables):

```
## Context Usage

**Model:** claude-opus-4-7
**Tokens:** 36.7k / 1m (4%)

### Estimated usage by category

| Category                | Tokens | Percentage |
|-------------------------|--------|------------|
| System prompt           | 9k     | 0.9%       |
| System tools            | 8.9k   | 0.9%       |
| System tools (deferred) | 19.2k  | 1.9%       |
| Custom agents           | 329    | 0.0%       |
| Memory files            | 465    | 0.0%       |
| Skills                  | 4.2k   | 0.4%       |
| Messages                | 14.2k  | 1.4%       |
| Free space              | 930k   | 93.0%      |
| Autocompact buffer      | 33k    | 3.3%       |

### Memory Files
| Type    | Path                              | Tokens |
| Project | …/context-cost-session/CLAUDE.md  | 465    |
```

(The Custom Agents and Skills tables that follow list the Vercel plugin's agents and skills and the user's `is-done` skill — the plugins installed on this Mac, not part of the film's claim.)

### Liam's VERIFY (plain shell, `evidence/`)

```
> grep -E "^\| (System prompt|System tools|Messages|Free space|Autocompact)" context-output.md
| System prompt | 9k | 0.9% |
| System tools | 8.9k | 0.9% |
| System tools (deferred) | 19.2k | 1.9% |
| Messages | 14.2k | 1.4% |
| Free space | 930k | 93.0% |
| Autocompact buffer | 33k | 3.3% |
> python3 -c "print(9+8.9+19.2+0.329+0.465+4.2+14.2)"
56.294          # the categories sum past the 36.7k headline: deferred tools are listed but not loaded
> python3 -c "…turns.json…"     # what the receipts said one message earlier
msg 10 (after /compact)  36,670 tokens read
```

Finding: `/context` works headless and prints a breakdown of the window: at this point 36.7k of a 1M-token window (4 %). Before you have typed anything, the fixed part is there — system prompt 9k, tools 8.9k (+19.2k deferred, listed but not loaded), skills 4.2k, CLAUDE.md 465. The conversation itself — Messages — is 14.2k after compaction. The 36.7k headline matches the 36,670 the receipts showed on message 10. The "Autocompact buffer" (33k) is the reserve the product keeps so it can compact before the window fills.
