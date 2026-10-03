# CHECKS-REPORT — cc-claude-agent-skills--claude-skills-progressive-disclosure

**skill.** cc-explainer · 101 tier 03 · Liam, in for Bear · palette `claude`.

## SHOW / HOLD / CARD

- SHOW — the three CCSession beats that are the real runs (B00, B02, B04, B06), and their VERIFY siblings (B03, B05, B07). One CCPlainShell (B01) — three tiers on disk.
- HOLD — BVDT (the four-line verdict, `ClaudeVerdictArtifact`), BOUT (`ClaudeTitleOutro`).
- CARD — one, BDEFS (`CCDefinitions`) — five terms a chat-window user may not know.

## LOOP

- Cycle 1 (BARE, B02+B03) — no skill in folder; VERIFY = grep Skill=0, check FAIL. Fails on purpose; this is the before.
- Cycle 2 (CORRECTION, B04+B05) — same folder + skill; VERIFY = grep Skill=1, refs=0, check PASS. Description matched, body loaded, references untouched.
- Cycle 3 (ESCALATION, B06+B07) — same folder + skill + a strict-style ask; VERIFY = grep Skill=1, refs=1, length=0, check PASS. Body's conditional matched, one reference loaded, the other stayed cold.

Two VERIFY steps in every cycle are Liam's `grep` and `python3 check.py` on the transcript and the output — the ✓ is his, not Claude's.

## Teaching arc

- Predict-before-reveal — the film asks (implicit): how much of the skill actually loads? Answer arrives in B05/B07's grep counts.
- Concrete-before-abstract — the three runs come first (measured, numeric); the tier language arrives on top of the measurements.
- Useful friction — the misconception ("resident") is corrected explicitly in BIDEA; the closing verdict names a falsifiable observation, so a viewer can disprove the film with one grep.
- Handoff to practice — BHTF hands a five-line concrete task (write description + two body conditionals) that reproduces the same three tiers on a skill the viewer designs.

## BUILD-SHOW

- Not armed — concept film. This film explains a Claude Code feature (skill progressive disclosure); it does not build a running artifact. `metadata.build` is unset. BFLOW and BSHOW are correctly absent.

## Terminal-first accounting

- Body beats on `CCSession`: B00, B02, B03, B04, B05, B06, B07 (7).
- Body beats off-terminal, with a named reason:
  - BIDEA — `BrutalistHesitantWriter` — the idea of the film is not in any session; the writer types it and corrects the one word the film exists to fix.
  - BDEFS — `CCDefinitions` — definitions for a chat-window audience.
  - B01 — `CCPlainShell` — the three tiers of the skill are files on disk (`wc`, `head`), not in a session.
- Closing block: B08 (`CCBoondoggleScore`), B09 (`CCHumanLedger`) — both left the terminal to render the two required diagrams.
- Bookends: BVDT (`ClaudeVerdictArtifact`), BHTF (`ClaudeComposerAsk`), BOUT (`ClaudeTitleOutro`).

Two consecutive non-terminal beats: BIDEA + BDEFS (both reason-named), and B08 + B09 (closing-block requirement). No unreasoned pair.

## Duration

- Measured: 300.6 s (5:00), audio-first, Kokoro `am_onyx`.
- Within the 4–8 min band for a 16:9 cc-explainer with a full body plus closing block.
