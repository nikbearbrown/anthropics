# BUILD PROMPT — stop-hitting-claude-limits

## Episode concept
A teardown of why Claude usage limits get hit so fast, explained through the core mechanic (cumulative context re-reading) and five clusters of the author's 23 habits that address it. Visual style: analytical chart + comparison illustrations.

## Beat-by-beat production notes

**B01 — ClaudeComposerAsk (0–9s)**
Cold open. Composer UI. Question: "Why do I keep hitting my usage limit by 2pm?" Answer preview appears: Claude explains it re-reads the full conversation on every message. Liam greeting: "Annyeong. This is Liam, in for Bear."

**B02 — Token accumulation curve (9–18s)**
Animated line chart. X-axis: message 1 through 30. Y-axis: cumulative tokens consumed. The curve bends sharply upward. At message 30, a terracotta callout: "31× message 1". This is the central mechanic beat — give it visual weight.

**B03 — SPARK: Convert first (18–26s)**
Spark card. Eyebrow: CLAUDE COWORK. Copy: "Convert first, upload second." Sub-text: PDF page = 1,500–3,000 tokens (author's claim). Workflow: export to .md, paste clean prose.

**B04 — Illustration: Plan in Chat / build in Cowork + batch (26–36s)**
Two-column illustration. Left: CHAT lane with rough sketch/sticky-note planning. Right: COWORK lane with final file. Bridge arrow. Below: side-by-side of 3 separate bubbles (3× reloads) vs. 1 combined bubble (1 reload).

**B05 — SPARK: AskUserQuestion (36–44s)**
Spark card. Copy: "Ask me questions first." Sub: show the 30-word template prompt. Reinforce that option-clicks cost almost nothing vs. 500-word walls.

**B06 — SPARK: Edit don't follow up (44–54s)**
Spark card. Copy: "Edit. Don't follow up." Sub: surgical section redo + the Chat Edit button mechanic.

**B07 — Illustration: Tool-match table + context caps (54–64s)**
Three-row table illustration. Tool-match: Chat/Haiku → quick; Cowork/Opus → reports; Code/Sonnet → charts. Sidebar: "About Me < 2,000 words" and "Restart @ 15–20 msgs". Projects = upload once, cached.

**B08 — HANDOFF (64–75s)**
Handoff card. Three user paths: Cowork daily (1,2,5), Chat user (8,15,17), $20 plan (6,13,22). Specific and actionable.

**B09 — OUTRO (75–81s)**
Outro card. Title: MESSAGE 30 COSTS 31 TIMES MORE. Sign-off: "This is Liam, in for Bear."

## Remotion component hints
- `TokenCurveChart` — animated SVG line chart, axis labels in SF Mono, terracotta annotation at x=30
- `TwoLaneCompare` — reusable left/right split with arrow bridge; parameterize lane labels + content
- `BubbleCompare` — row of 3 message bubbles vs. 1 merged bubble with token count badges
- `ToolMatchTable` — three-row table component with icon slots; sidebar callout box
- `SparkCard` — standard spark card: eyebrow / big copy / sub-text; terracotta accent stripe

## Rebuild notes
Source is markdown — no infographic to rebuild. All visuals are original compositions.

## Audio notes
NO AUDIO in this pass. Gate P = slate only.
