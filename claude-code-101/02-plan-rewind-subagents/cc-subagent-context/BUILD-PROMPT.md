# BUILD-PROMPT — cc-subagent-context

The reel is a cc-explainer built from two real headless `claude -p` runs
against a small scratch project (a study-group grader with five policy
docs). The goal is honest: show the subagent mechanism working (a
435-token summary crosses back into the main session instead of 3,266
tokens of policy content), and then show Claude 2.1.150's default of
opening the source docs anyway after the subagent returns — cancelling
the win. The film's fix is the human's: remove Read from the sources.
The concept film's original claim ("Subagent Saved 48%") becomes the
falsifiable frame: it saves the fraction the human is willing to enforce.

- Skill: `cc-explainer` (Terminal-First LAW; REAL-SESSION LAW; LIAM LAW).
- Persona: Liam, in for Bear. Kokoro `am_onyx` everywhere.
- Spine: COLD OPEN → THE IDEA → DEFINITIONS → INLINE (2) → THE MECHANISM
  → SUBAGENT PROMISE → THE CATCH → THE FIX → CONDUCT → HUMAN →
  VERDICT → YOUR TURN → OUTRO. 14 beats, ~5:30.
- Every `CCSession` block traces to `SESSION.md`; every number is in
  `evidence/analyze3.py` output.
- Rebuild: `python3 author_sheet.py && ./brutalist-art/art run
  anthropics/claude-code-101/02-plan-rewind-subagents/cc-subagent-context
  && ./brutalist-art/art final ...`
- Rules on: TERMINAL-FIRST (11/14 in terminal, others `leaves_terminal_because`),
  TYPES-NOT-NARRATES (prompt blocks = what he typed), VERBATIM STRINGS,
  VERIFY IS A COMMAND, OUTRO-LOCK, BUILD-SHOW not armed (concept film).
