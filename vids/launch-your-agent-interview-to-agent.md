## launch-your-agent-interview-to-agent

- **Source path:** launch-your-agent/ (README.md, .claude/skills/launch-your-agent/, cma-primitives.md, interview-to-config.md)
- **Teachable claim:** A Claude Code skill can interview you about what you want built, then launch a live Claude Managed Agent in your own account — scoped v0, graded against your own definition of done, iterated, and put on a scheduled deployment — with the whole flow costing cents and ending in a resumable `my-agent/` folder.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium-long (6–8 min)

### Visual beats
1. Cold open: `claude` → `/launch-your-agent` → the skill starts asking questions instead of writing code — the interview IS the config
2. The mapping beat: interview answers → CMA primitives (agent, environment, graded run, scheduled deployment), drawn as answers snapping onto primitive slots (interview-to-config.md is the source)
3. Launch: the exact API payloads land in the Console — a live agent exists in YOUR account, not a demo sandbox
4. Grade-and-iterate loop: the run graded against the user's own definition of done; one iteration shown
5. Closer: `/wrap-up` — the overview page, every primitive you now own, and NEXT-DIRECTIONS.md's v1/v2 plan

### Score
- Teachability: 4/5 — the four-phase flow is clear, though CMA primitives need a beat of setup
- Visual: 5/5 — interview → payload → live Console agent is a complete on-screen arc
- Pull: 4/5 — "build your agent by being interviewed" lands for the technical-founder viewer
- Freshness: 5/5 — CMA launch tooling is the newest surface in the repo set
- **Total: 18/20**
