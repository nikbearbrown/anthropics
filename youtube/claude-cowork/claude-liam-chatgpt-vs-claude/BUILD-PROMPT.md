# BUILD PROMPT — chatgpt-vs-claude

## Episode concept
A teardown of 8 ChatGPT vs Claude comparison panels from Ruben Hassid's infographic, rebuilt as native Remotion animation. The reel is honest about the author's opinion framing — every comparison is his view and his testing, not a lab study. Final verdict: images on ChatGPT, everything else on Claude.

## Beat-by-beat production notes

**B01 — ClaudeComposerAsk (0–9s)**
Cold open. "Sawubona. This is Liam, in for Bear." Composer question: "Should I use ChatGPT or Claude? What is actually different?" Answer: the task-split verdict.

**B02 — SPARK: Eight panels. One verdict. (9–17s)**
Caveat card up front. Name the source (Ruben Hassid / how-to-ai.guide) and note it's his opinion. Sets honest expectations before the comparisons.

**B03 — REBUILD: Panels 1–2 (17–28s)**
Panel 1: Skills comparison. Panel 2: Model choice (30 combos vs 1 picker). Draw panel headers first, then body text, then footer note.

**B04 — REBUILD: Panels 3–4 (28–39s)**
Panel 3: Pricing ceiling ($20 vs $100). Panel 4: Speed (16 min Sol-5.6 vs 13 min Fable 5). Timer bar animation for Panel 4.

**B05 — REBUILD: Panels 5–6 (39–50s)**
Panel 5: Work vs Cowork. Panel 6: Codex vs Code. Both have symmetric/tie verdicts — show parity iconography.

**B06 — REBUILD: Panels 7–8 (50–60s)**
Panel 7: Best for images / best for work — the clean split. Panel 8: 151 seats / 150 seats — threshold diagram with cost callout.

**B07 — SPARK: Verdict (60–68s)**
"Images: ChatGPT. Work: Claude." One-line summary of the author's position.

**B08 — SPARK: Caveat (68–77s)**
"Run your own test." Remind viewer these are the author's comparisons. Pricing is datable.

**B09 — HANDOFF (77–86s)**
"Run one task on both this week." Specific, actionable, honest.

**B10 — OUTRO (86–92s)**
Ink bg. "EVERYTHING ELSE ON CLAUDE." "This is Liam, in for Bear."

## Remotion component hints
- `ComparisonPanel` — single panel: colored header row (two labels side by side), body text area, footer note in muted ink. Props: left_label, right_label, body, footer, verdict (drives a small verdict badge: CLAUDE / TIE / SPLIT / BOTH)
- `ComparisonPanelPair` — wraps two `ComparisonPanel` instances side by side with stagger animation (left draws first, right follows at +0.4s)
- `TimerBar` — horizontal progress bar that fills to a proportional width; used for panel 4 timing comparison; props: value, max, label, color
- `ThresholdDiagram` — horizontal seat-count bar (1–200), animated sweep, terracotta vertical line drops at 150, cost callout animates in; used for panel 8
- `IconSplit` — for panel 7: left side renders camera icon, right side renders document icon; each fades in with a 0.3s delay

## Rebuild notes (image-sourced reel)
The original JPEG (`chatgpt-vs-claude-comparison-infographic.jpeg`) must NOT appear as a shot. All 8 panels must be built natively:
- **Panel headers**: two-column label row; left = teal (#00B4B0 approximate), right = terracotta (#D97757)
- **Body text**: system sans, warm ink, ~60% opacity
- **Footer notes**: smaller sans, italic, muted — these are important for factcheck framing
- **Verdict badges**: small pill badge at bottom right of each panel; color-coded (terracotta=Claude wins, neutral=tie, split=both)
- **Panel layout**: 2×4 grid total; reel reveals them in pairs (2 per beat) to allow narration pacing

## Audio notes
NO AUDIO in this pass. Gate P = slate only.
