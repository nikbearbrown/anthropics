# BUILD PROMPT — claude-fable-5

## Episode concept
Fable 5 is Anthropic's most powerful model — and the most expensive to misuse. The cost compounds with every turn because Claude re-reads the entire conversation history at each exchange. This reel is a teardown of the cost mechanism and a concrete playbook: aim Fable at a hard goal, cap yourself at two turns, then switch to Opus 4.8 and finish the work there. Viewers who watch this will never mindlessly chat their way through a Fable session again.

## Beat-by-beat production notes

**B01 — COMPOSER_ASK (cold open)**
Show the Claude composer with the question appearing: "How do I use Fable 5 without it costing a fortune?" The answer preview fades in: "Keep sessions short, lead with a goal, then switch to Opus…" Liam byline bottom-left.

**B02 — ILLUSTRATION (cost curves)**
Two side-by-side graphs on cream paper, hand-drawn. Left panel labeled "Before" in a warm-pink pill: bill curve climbs steeply with turns, results lag behind, terracotta dot marks the expensive peak. Right panel labeled "After" in a green pill: results spike in the first two turns (terracotta dot at the good peak), bill stays nearly flat. X-axis: Turns. Y-axis labels: Your Bill / Results. Keep it sparse and readable. This directly conceptualizes the source infographic — do not trace or reproduce the original image.

**B03 — SPARK CARD (two-turn cap)**
Copy "Fable 2 turns max" — the number "2" in terracotta. Sub explains the switch to Opus 4.8.

**B04 — SPARK CARD (goals not tasks)**
Copy "Goals, not tasks" — "Goals" in terracotta. Sub contrasts the wasted task prompt vs the goal-driven prompt.

**B05 — ILLUSTRATION (four lines)**
Four numbered lines, hand-lettered, generous leading. Numbers in terracotta. Each line: bold short label + one supporting sentence below. No dense paragraphs. Labels: (1) Lead with outcome. (2) Evidence only. (3) Advise vs Act. (4) Decide, don't survey.

**B06 — SPARK CARD (Fable playbook)**
Copy "The Fable playbook" in EB Garamond. Sub: "Hard goal · 2 turns max · Switch to Opus · Save in Project." The middle dot separators in terracotta.

**B07 — HANDOFF CARD**
Copy "Aim Fable at one hard decision" — large EB Garamond. Sub walks through the three-step loop. Eyebrow "YOUR TURN."

**B08 — OUTRO CARD**
Full cream background. "DON'T USE FABLE 5 BROKE" large all-caps EB Garamond. Byline "this is Liam, in for Bear."

## Remotion component hints
- **ClaudeComposerAsk**: props.ask = "How do I use Fable 5 without it costing a fortune?" / props.answer_preview = "Keep sessions short, lead with a goal, then switch to Opus…"
- **IllustrationBeat B02**: before/after dual cost-curve — hand-drawn, terracotta accent on Before bill peak and After results peak
- **SparkCard B03**: eyebrow "CLAUDE COWORK", copy "Fable 2 turns max", sub "One hard goal. Then switch to Opus 4.8 for the rest.", accent #D97757
- **SparkCard B04**: eyebrow "CLAUDE COWORK", copy "Goals, not tasks", sub "Fable plans end-to-end. Tasks waste its ceiling.", accent #D97757
- **IllustrationBeat B05**: four-line list, hand-lettered, terracotta line numbers
- **SparkCard B06**: eyebrow "CLAUDE COWORK", copy "The Fable playbook", sub "Hard goal · 2 turns max · Switch to Opus · Save in Project.", accent #D97757
- **HandoffCard B07**: eyebrow "YOUR TURN", copy "Aim Fable at one hard decision", sub "Goal in two sentences. Ask-me-first. Switch to Opus after turn two."
- **OutroCard B08**: eyebrow "CLAUDE COWORK", copy "DON'T USE FABLE 5 BROKE", sub "this is Liam, in for Bear"

## Audio notes
NO AUDIO in this pass. Gate P = slate only.
