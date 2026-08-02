# AUDIT — claude-liam-spec-prompt-audit
_Generated 2026-07-25T10:12:56_

## Beat Classification

| Beat | Narration | Visual | Class | Fix |
|------|-----------|--------|-------|-----|
| B00 | Two prompts, one minute apart, same model. The specificati | remotion:NikBearBrownOpen | EXEMPT | leave as-is (bookend) |
| B01 | A specification prompt is not a longer prompt — it is a di | None:None | SHOWS | leave as-is (SHOWS) |
| B02 | We run two prompts side by side: a weak vague request, and | remotion:NikBearBrownTerminalAsk | EXEMPT | leave as-is (bookend) |
| B03 | The specification output uses csv.reader with encoding utf | remotion:NikBearBrownCodeBlock | EXEMPT | leave as-is (bookend) |
| B04 | Two outputs, side by side. The specification version: 42 l | None:None | SHOWS | leave as-is (SHOWS) |
| B05 | We run the weak prompt twice and show the two outputs diff | remotion:NikBearBrownTerminalAsk | EXEMPT | leave as-is (bookend) |
| B06 | Weak prompt run 1: pandas. Weak prompt run 2: openpyxl. Bo | None:None | SHOWS | leave as-is (SHOWS) |
| B07 | A specification is not a longer prompt. It is a set of inv | None:None | SHOWS | leave as-is (SHOWS) |
| B08 | Next: catch a package hallucination before it becomes a sl | None:None | SHOWS | leave as-is (SHOWS) |
| B09 | Nik Bear Brown. Build it with a CLI. Then take it apart. A | remotion:NikBearBrownOutro | EXEMPT | leave as-is (bookend) |

## TELLS → SHOWS Upgrades

(none)

## QC

No TELLS found — video already compliant.
