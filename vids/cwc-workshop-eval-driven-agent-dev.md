## cwc-workshop-eval-driven-agent-dev

- **Source path:** cwc-workshops/eval-driven-agent-development/
- **Teachable claim:** The right way to iterate on a Claude Managed Agent is to write the eval before you write the agent — a LibreOffice-rendering grader that scores slide decks lets you run automated regression tests on every prompt change before you ship it.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–6 min)

### Visual beats
1. The workflow: agent creates slide deck → Docker renders it → grader scores it — end-to-end shown
2. Eval run output: per-slide scores appearing as the batch completes — the feedback signal made concrete
3. Prompt change → re-run eval → score change: showing how evals drive iteration rather than vibes
4. Two-phase approach: audit (is the eval trustworthy?) then sweep (which model + settings wins?)

### Score
- Teachability: 5/5 — eval-first agent development is the key discipline most builders skip
- Visual: 4/5 — slide deck rendering + score output is visually interesting
- Pull: 4/5 — anyone building a production agent should see this workflow
- Freshness: 5/5 — Managed Agents + programmatic eval is new territory
- **Total: 18/20**
