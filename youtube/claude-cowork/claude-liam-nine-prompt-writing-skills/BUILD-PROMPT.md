# BUILD PROMPT — nine-prompt-writing-skills

## Episode concept
A tutorial showing how nine slash-command skills from how-to-ai.guide form a pipeline from "Messy Idea" to "Ready to use prompt." The reel rebuilds the infographic flowchart as native Remotion animation, tier by tier, never showing the original JPEG.

## Beat-by-beat production notes

**B01 — ClaudeComposerAsk (0–9s)**
Cold open. "Kia ora. This is Liam, in for Bear." Composer question: "My prompts keep coming out vague. What's the fastest way to fix that?" Answer: /prompt-master intro.

**B02 — SPARK: Messy in. Ready out. (9–17s)**
Frame the problem and solution in one spark card before revealing the flowchart. Sets expectation: nine skills, one pipeline, three outputs (clear goal / full context / your voice).

**B03 — REBUILD: Flowchart Tier 1 — Skills 01–04 (17–29s)**
Build the top of the flowchart from scratch. START node (scribble icon = messy idea) → arrow → Skill 01 card. Then three cards below: Skills 02, 03, 04 with stagger. Each card: number in terracotta, skill name in serif, slash command in SF Mono, one-line description in sans.

**B04 — REBUILD: Flowchart Tier 2 — Skills 05–07 (29–40s)**
Continue building the flowchart downward. Arrow from Skill 04 branches into Skills 05, 06, 07. Same card design, distinct robot-icon placeholder colors. Arrow from 07 exits left indicating the next tier.

**B05 — REBUILD: Flowchart Tier 3 — Skills 08–09 + FINISH (40–50s)**
Final tier. Skills 08 and 09 cards appear with connecting arrows. Arrow from 09 points to FINISH node: "Ready to use prompt — clear goal · full context · your voice." Complete flowchart is now fully visible.

**B06 — SPARK: One slash away. (50–58s)**
Distill the practical starting path: /prompt-master → /grill-me if vague → /personal-voice for tone. Point to how-to-ai.guide for the full library.

**B07 — REBUILD: Before/After panel (58–68s)**
Side-by-side comparison. Left: vague prompt → generic output. Right: /prompt-master + /personal-voice → structured output skeleton. Animated reveal: left fades, divider draws, right reveals.

**B08 — HANDOFF (68–79s)**
"Run /prompt-master on your next idea." how-to-ai.guide link. Specific action, clear reason.

**B09 — OUTRO (79–85s)**
Ink background, cream text. "NINE SKILLS THAT WRITE YOUR PROMPTS." "This is Liam, in for Bear."

## Remotion component hints
- `SkillCard` — reusable card: number badge (terracotta), skill name (EB Garamond bold), slash command (SF Mono), one-line description (system sans), pixel-robot icon placeholder (colored square/emoji)
- `SkillFlowTier1/2/3` — flowchart sections; draw connecting arrows via SVG path with drawon animation; stagger SkillCard reveals
- `FlowArrow` — animated SVG arrow; props: start point, end point, direction
- `StartNode` — scribble illustration placeholder + "START / Messy Idea" label
- `FinishNode` — rounded box with "FINISH" eyebrow label (terracotta), title, bullet list draw-on
- `BeforeAfterSkillPanel` — 50/50 split; left panel: vague prompt bubble + grey skeleton bars; right panel: slash-badge chain + structured skeleton

## Rebuild notes (image-sourced reel)
The original JPEG (`nine-claude-prompt-writing-skills.jpeg`) must NOT appear as a shot. Every element must be rebuilt:
- **9 skill cards** — built with `SkillCard` component
- **Flowchart arrows** — built with `FlowArrow` SVG animation
- **START node** — built with `StartNode` (scribble placeholder)
- **FINISH node** — built with `FinishNode` (bullet list animation)
- **Pixel-robot icons** — placeholder colored squares/simple pixel art; can be swapped for actual icons at Gate 0
- **Color palette** for skill cards matches muted palette from image: gold, green, blue, teal, purple, blue, pink, black (see beat_sheet.json for hex values per card)

## Audio notes
NO AUDIO in this pass. Gate P = slate only.
