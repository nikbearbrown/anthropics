## C15 — The Principal Hierarchy: Why Claude Has Three Bosses

- **slug:** claude-constitution-three-principals
- **source:** ../anthropics/claude-constitution/20260120-constitution.md §"Claude's three types of principals"
- **bucket:** RESEARCH / PAPERS → claude-scout lens → claude-explainer builder
- **premise:** Claude doesn't just have one user — it has three overlapping principals (Anthropic, operators, users) with different levels of trust and different types of authority, and the Constitution explicitly describes how Claude navigates conflicts between them.
- **channel:** claude-liam (Kokoro am_onyx, Teardown register, @NikBearBrown)
- **teachable claim:** When you interact with Claude through an app, the app operator's system prompt has more authority than your user request — not because Claude is being unhelpful, but because operators take responsibility for their deployment and Anthropic has granted them that authority by contract.

### Ask beat (B00 — cold open, ClaudeComposerAsk)
- command: `Who does Claude actually work for?`
- topic: `AI DESIGN · The Principal Hierarchy`
- segment: `Claude's Three Bosses`
- greeting: `Hola, Liam` (Wagwan check: not 0)

### Spine
B00 ASK → B01 the naive picture: Claude works for "the user" → B02 the actual structure: Anthropic (training-time rules) > operators (system prompt, deployment context) > users (conversation) → B03 how conflicts resolve: operators can restrict but not weaponize; users get a floor of protection Claude never violates regardless of operator instructions → B04 why this design: accountability (operators sign Terms of Service, users often anonymous) → HANDOFF → OUTRO

### Visual beats (4 suggested)
1. **B01 — Remotion concept illustration:** The naive picture: one user, one Claude, one relationship. Label: "how most people think it works."
2. **B02 — Manim layered diagram:** Three concentric rings: innermost = Anthropic's training-time hardcoded behaviors; middle ring = operator's system prompt permissions; outer ring = user's conversational requests. Arrows show which layer can expand/restrict which. The hierarchy is visualized as nested authority.
3. **B03 — Remotion animated split card:** Two columns: "Operators CAN do..." (restrict topics, require a persona, limit to certain tasks) vs "Operators CANNOT do..." (weaponize Claude against users, violate basic user dignity, override hardcoded safety behaviors). Items appear one by one in each column.
4. **B04 — ClaudeComposerAsk micro-beat:** An example: a user asks Claude (deployed as a customer service bot) a question outside the bot's scope. Claude declines — but it tells the user it can't help with that here, and that they can seek help elsewhere. The "floor of protection" in action.

### Register notes
Teardown: the principal hierarchy is the most underexplained thing about Claude's behavior. Users who feel Claude is "refusing for no reason" are usually running into an operator restriction they can't see. The Teardown line: "The system prompt is not a bug — it's the contract that makes operators accountable for how Claude behaves on their platform."

### Est length
~125 s (4 beats, mixed definitional + structure content_type)

### Scores
- Teachability: 5/5 — the three-principal model resolves a genuine confusion most Claude users have
- Visual potential: 4/5 — the layered authority diagram is the strong visual; the split card is clean
- Audience pull: 5/5 — anyone who uses Claude through an app has wondered "why won't it do this"
- Freshness: 4/5 — the Constitution is public; the principal hierarchy explanation is less known
- **Total: 18/20**
