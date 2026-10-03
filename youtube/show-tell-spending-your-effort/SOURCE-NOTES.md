# SOURCE NOTES: show-tell-spending-your-effort

**What this is.** The verified source material for the effort-dial show-tell film Bear asked for on 2026-09-26 ("show-tell for this film as well", with 16 reference frames from Anthropic's effort animation, saved in `reference/`). **Why.** The builder fact-checks against these primaries, not against the frames. **Found.** The frames match Thariq Shihipar's post, with one correction to a second-hand summary: the 5/5 sanitizer run was at **xhigh**, not high.

## Primary 1: Thariq Shihipar, "Spending your effort", claude.dev/blog/spending-your-effort/ (Sep 25, 2026)
Read 2026-09-26 by WebFetch (summarised extraction; the builder should re-fetch and quote exactly):
- Definition: "Effort gives the model an approximation of how much compute you want it to spend on the task."
- The analogy: asked to do a task in 12 hours straight, you'd assume they want you to try very hard; given 1 hour, you'd deliver the best version that meets the task and expect to iterate. Claude adjusts its verification and independent judgment the same way.
- Levels (his words): Low "for when I want quick responses that are in the loop, e.g. brainstorming, sketching, easy changes"; Medium "for most of my regular software engineering work, e.g. new feature implementation"; High "for work where verification is important or there are edge cases, e.g. fixing a bug"; Max "When I want Claude to operate fully autonomously to solve difficult problems". Check the article for his line on **xhigh**; the frames show the dial with XHIGH but no use-case card for it.
- The example: Terminal-Bench 3.0, html-js-filter (an HTML sanitizer), Fable 5.1. Low: 1/5, about 2 minutes, one pass, tested against one hand-written page. **xhigh: 5/5**, about 33 minutes: adversarially reviewed its own draft, read the installed parser's source, ran test suites (the frame says "an XSS test suite"), and wrote a fuzzer.
- The loop: give Claude a spec and have it interview you about missing details → implement on low effort → review (iterate on low as needed) → verify and test on high effort.
- Changing effort in Claude Code: the `/effort` command, mid-conversation.

## Primary 2: Anthropic docs, platform.claude.com/docs/en/build-with-claude/effort
- Five levels: low, medium, high, xhigh, max. "Effort is a behavioral signal, not a strict token budget."
- Effort affects all output tokens: text, tool calls, and thinking. "Lower effort also means fewer and terser tool calls."
- Opus 5.5 defaults to **medium**; most other models default to high.
- xhigh: "Long-running agentic and coding tasks (over 30 minutes)". max: "Absolute maximum capability with no constraints on token spending."

## Secondary (orientation only; do not cite for facts)
- github.com/Wladefant/super-board/issues/228: a third-party summary. It says "High effort (~33 min)", which is wrong (the article says xhigh). It gives Thariq's X post as x.com/trq212/status/2103576349499855160.

## Frame notes (composition only; redraw in the Claude palette, isometric, never trace)
The dial with LOW / MEDIUM / HIGH / XHIGH / MAX; a use-case card per level; "What is effort, really?"; two clocks (1 hour / 12 hours); "Effort = how much checking and judgement"; the html-js-filter side-by-side (1/5 against 5/5 with four checks); the four-step loop around the dial; `/effort`.
