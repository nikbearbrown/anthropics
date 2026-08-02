# CAJAL figure candidates — prompt-engineering-for-cli-ai-coding-agents (previz track)

Mechanism and workflow figures mined from chapter text. Blank unannotated vector — no baked text.
Okabe-Ito, white bg, 1pt strokes, no red-green, no 3D perspective, ≤6–8 components.

---

## 1. read-reason-act-observe-loop  — four-stage closed agentic coding loop with ground-truth feedback arrow  (MC · cycle diagram · Critical)
*Source: chapter 01 — "The Agentic Coding Loop"*

**PASTE:** Draw a blank four-node clockwise cycle on a white background: four rounded rectangles arranged equidistantly in a square formation, connected by single-headed arrows curving clockwise between adjacent nodes. The arrow from the bottom-left node (Observe) back to the top-left node (Read) is visually emphasized — made thicker and bold — to indicate the load-bearing feedback edge. Four small icons beside the Observe node suggest signal types: a check mark, a number, a diff-arrow, a triangle — representing test output, exit code, diff, and stack trace. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] four stages: Read (top-left), Reason (top-right), Act (bottom-right), Observe (bottom-left); emphasized Observe-to-Read back-arrow; four signal-type small icons beside Observe node.
- [O] square clockwise arrangement; four clockwise arrows; one thicker return arrow from Observe to Read; signal icons beside Observe.
- [P] flat vector, Okabe-Ito: Read node Blue #0072B2, Reason node Sky Blue #56B4E9, Act node Orange #E69F00, Observe node Bluish Green #009E73, return arrow Black #000000 thick, standard arrows neutral gray, signal icons neutral gray. No baked text.
- [E] exclude: code example annotations, specific test framework names, "open loop" comparison panel, the self-report failure path.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 2. task-taxonomy-oracle-plane  — bounded-vs-open-ended by mechanical-vs-judgment 2×2 classification plane  (VG · systems diagram · Critical)
*Source: chapter 03 — "Taxonomy of Agentic Coding Tasks"*

**PASTE:** Draw a blank two-by-two classification plane on a white background: a square divided into four quadrants by a horizontal and a vertical axis line, each axis with a small arrowhead at its far end. The bottom-left quadrant has a bold border. A diagonal arrow starts from the top-right quadrant and points toward the bottom-left quadrant. Five small circles are plotted: three in or near the bottom-left quadrant, one in the upper-right quadrant, one in the middle. No text, no labels. Uniform strokes, flat fills, no shading.
- [S] single-column 89mm, 300 DPI, vector, white bg, square.
- [C] horizontal axis: bounded (left) to open-ended (right); vertical axis: mechanical (bottom) to judgment-laden (top); bottom-left quadrant bold (agent-strong zone); diagonal arrow pointing toward bottom-left encodes "drag-to-bounded" strategy; five plotted tasks as circles.
- [O] square with two axes; bold bottom-left quadrant; diagonal strategy arrow; five scattered circle plots.
- [P] flat vector, Okabe-Ito: axes Black #000000, agent-strong quadrant Bluish Green #009E73 bold border, strategy diagonal arrow Blue #0072B2, circles in agent-strong zone Bluish Green #009E73, circle in human-gate zone Orange #E69F00, middle circle Sky Blue #56B4E9. No baked text.
- [E] exclude: axis tick labels with specific values, task-name annotations on circles, SWE-bench difficulty bars.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 3. tdd-guarded-red-green-loop  — test-protected iteration loop with agent barrier blocking test tampering  (MC · process flowchart · Critical)
*Source: chapter 04 — "Test-Driven Agentic Development"*

**PASTE:** Draw a blank vertical loop diagram on a white background: at the top, a small rectangle (human-owned test, with a bold border and a small padlock icon on its right edge). A downward arrow leads to a medium rectangle (agent: reads, edits implementation, runs suite). A rightward arrow from the agent rectangle leads to a small diamond (decision: passes?). From the diamond, a downward arrow exits to a final small rectangle (done — output); a leftward arrow curves back up to the agent rectangle (iterate). A vertical dashed barrier line runs on the right side of the agent rectangle, separating it from the test rectangle's padlock, indicating the agent cannot cross into the test. No text, no labels.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] four elements: human-owned locked test (top, bold padlock); agent iteration rectangle; pass/fail decision diamond; barrier dashed line preventing agent access to test; output terminal rectangle.
- [O] top-to-bottom flow; barrier line on right side of agent; return arc from decision back to agent; terminal output at bottom.
- [P] flat vector, Okabe-Ito: test rectangle Blue #0072B2 bold with padlock neutral gray, agent rectangle Orange #E69F00, decision diamond Sky Blue #56B4E9, barrier line Vermillion #D55E00 dashed, output rectangle Bluish Green #009E73. No baked text.
- [E] exclude: code syntax inside agent rectangle, specific test-framework icons, multiple test files, a second agent rectangle.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## 4. orchestrator-workers-merge-gate  — multi-agent fan-out/fan-in architecture with isolated worktrees and merge gate  (MC · systems diagram · Important)
*Source: chapter 10 — "Multi-Agent, Multi-Repo Engineering"*

**PASTE:** Draw a blank fan-out/fan-in diagram on a white background: at the top, one large rectangle (orchestrator). Three arrows fan downward from it to three smaller equal rectangles arranged side by side (workers). Each small worker rectangle contains a small circle (its own closed loop). Three arrows fan upward from the workers toward a central diamond (merge gate). One downward arrow exits the diamond leading to a small rectangle (human gate). Uniform strokes, flat fills, no shading, no text.
- [S] single-column 89mm, 300 DPI, vector, white bg, portrait.
- [C] orchestrator (top); three workers (middle row) each with isolated closed-loop circle; merge gate diamond; human gate rectangle at bottom; fan-out arrows from orchestrator to workers; fan-in arrows from workers to merge gate.
- [O] top-to-bottom; orchestrator fans to three workers; workers fan into merge diamond; merge leads to human gate.
- [P] flat vector, Okabe-Ito: orchestrator rectangle Blue #0072B2, worker rectangles Sky Blue #56B4E9, worker loop circles Orange #E69F00, merge diamond Reddish Purple #CC79A7, human gate rectangle Bluish Green #009E73. No baked text.
- [E] exclude: worktree directory paths, git branch labels, specific orchestrator tool names, a fourth worker.

**NEGATIVE:** text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, 3D perspective

---

## Video candidates

FIGURE read-reason-act-observe-loop — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE task-taxonomy-oracle-plane — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.
FIGURE tdd-guarded-red-green-loop — Status: STATIC SUFFICIENT · Criterion: — · Reason: the concept is a classification or taxonomy with no temporal component; animation would impose a false sequence.
FIGURE orchestrator-workers-merge-gate — Status: STATIC SUFFICIENT · Criterion: — · Reason: the mechanism is fully carried by arrow direction and shape arrangement in one frame; motion would not add information a careful static figure does not already hold.

**Chapter recommendation:** None — no entry in this file clears the motion bar; static figures serve every concept here.
