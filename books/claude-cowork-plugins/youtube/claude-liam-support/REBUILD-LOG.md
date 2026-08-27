# REBUILD-LOG — claude-liam-support

## Session: 2026-08-27

### Narration changes (Phase 1 authorized edits only)

| Beat | Field | Old | New | Source |
|------|-------|-----|-----|--------|
| BVDT | narration_text | "" (empty) | "Four jobs from one plugin: triage, draft, knowledge base, and sentiment. For a solo operator, that's the difference between two hours of context-switching and thirty focused minutes on what matters. Recurring questions become reusable FAQ answers — volume falls instead of climbing. Claude drafts; you review before send. You own the edge cases." | Authored from body: B04 (four jobs), B12 (30 min vs 2 hr), B16 (FAQ deflection), B20 (draft/decide contract) |

### Non-narration fixes

| Beat | Field | Old | New | Rule |
|------|-------|-----|-----|------|
| BVDT | artifactHeading | "Key findings" | "Support plugin — what holds" | Check 4: placeholder heading |
| BVDT | artifactLines | ["Key finding one", "Key finding two", "Key finding three"] | [four authored lines from body] | Check 4: placeholder verdict |
| BHTF | props.folderLabel | "@claude-liam" | "@NikBearBrown" | Check 9: channel handle, not brand key |

### scenes_std.py fixes

| Scene | Field | Old | New | Rule |
|-------|-------|-----|-----|------|
| B06 | ACT label | "ACT II" | "ACT  II" | Check 5b: doubled space |
| B06 | lbl1 text | "Then drafting"[:30] | "Consistent" | Check 5b: category noun not narration fragment |
| B06 | lbl2 text | "It generates replies..."[:30] | "Variable" | Check 5b: category noun not narration fragment |
| B06 | note text | "A first draft, not a form letter"[:60] | "A first draft, not a form letter." | Check 5b: complete sentence |
| B07 | ACT label | "ACT II" | "ACT  II" | Check 5b: doubled space |
| B07 | lbl1 text | "Third, sentiment"[:30] | "Flagged" | Check 5b: category noun not narration fragment |
| B07 | lbl2 text | "Not every request..."[:30] | "Missed" | Check 5b: category noun not narration fragment |
| B07 | note text | "It points your attention..."[:60] (truncated, trailing space) | "It points your attention at the messages that need it." | Check 5b: complete sentence, no truncation |
