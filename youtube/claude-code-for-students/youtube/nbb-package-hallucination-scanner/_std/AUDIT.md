# AUDIT — nbb-package-hallucination-scanner
_Generated 2026-07-25T10:12:56_

## Beat Classification

| Beat | Narration | Visual | Class | Fix |
|------|-----------|--------|-------|-----|
| NBB00 | I like that the scanner checks each import against the PyP | remotion:ClaudeComposerAsk | EXEMPT | leave as-is (bookend) |
| B00 | Claude imports requests_oauth_helper — a name that doesn't | remotion:NikBearBrownOpen | EXEMPT | leave as-is (bookend) |
| B01 | Hallucinated package names appear across thousands of mode | None:None | SHOWS | leave as-is (SHOWS) |
| B02 | We ask Claude to write a package auditor that reads import | remotion:NikBearBrownTerminalAsk | EXEMPT | leave as-is (bookend) |
| B03 | Claude writes the auditor using requests and the PyPI API. | remotion:NikBearBrownCodeBlock | EXEMPT | leave as-is (bookend) |
| B04 | Scanner run: requests — EXISTS. numpy — EXISTS. requests_o | None:None | SHOWS | leave as-is (SHOWS) |
| B05 | We extend the scanner with a --npm flag for JavaScript imp | remotion:NikBearBrownTerminalAsk | EXEMPT | leave as-is (bookend) |
| B06 | npm scan: react — EXISTS. lodash — EXISTS. react-query-opt | None:None | SHOWS | leave as-is (SHOWS) |
| B07 | The hallucination rate is low but the recurrence rate is h | None:None | SHOWS | leave as-is (SHOWS) |
| B08 | Next: write a five-artifact Software Design Document with  | None:None | SHOWS | leave as-is (SHOWS) |
| NBB01 | Let's recap with Claude. Here's what the body just demonst | remotion:ClaudeVerdictArtifact | EXEMPT | leave as-is (bookend) |
| NBB02 | Take this prompt, run it on your own — pick any cancer typ | remotion:ClaudeComposerAsk | EXEMPT | leave as-is (bookend) |
| NBB03 | Catch a Package Hallucination Before It Becomes a Slopsqua | remotion:ClaudeTitleOutro | EXEMPT | leave as-is (bookend) |

## TELLS → SHOWS Upgrades

(none)

## QC

No TELLS found — video already compliant.
