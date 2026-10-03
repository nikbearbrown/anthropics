# ACTS.md — Muse in Code (Film 7 of 12)

**Exact title:** Muse in Code

**Core promise:** By the end, the viewer can call Muse from their own code
three ways — raw REST, the OpenAI SDK, and the Anthropic SDK — and knows how
to debug the calls when they break.

**Structure:** hook + key terms + three acts (8 body beats) + recap + your
turn + outro. 13 beats, ~282 s (~4m42s).

- **Hook (BIDEA):** the playground is a sandbox; today we take Muse out of
  it.
- **Key terms (BDEFS):** API key · Base URL · SDK · REST.
- **Act 1 — Access (2 beats):** B01 generating an API key (copy it once, env
  not code); B02 the base-URL swap — Muse speaks the chat-completions
  dialect, with no `/v1` path segment.
- **Act 2 — Three ways (4 beats):** B03 raw REST (one POST, JSON back, no
  library); B04 the OpenAI SDK (same call, only the address changes);
  B05 the Anthropic SDK port (messages array, system vs user roles, explicit
  max tokens); B06 debugging via error messages (run, read, fix, repeat).
- **Act 3 — The stance (2 beats):** B07 REST is enough (SDKs add convenience,
  not capability); B08 no first-party Meta SDK — by design, in the
  instructor's reading; the API is the SDK.
- **BVDT:** exactly 3 lines, one per act.
- **BHTF:** make one API call from your own code, any of the three ways, and
  print what comes back.
- **BOUT:** "Muse, in for Bear. Thanks for watching." + teaser for Film 8
  (Agents and Frameworks).

**Tone:** teardown-like, direct, hands-on. The film treats the API as
machinery to take apart: key, address, three ways in, errors as
documentation.

**What this film is not:** not a full API reference; not a Python tutorial;
not the agent-SDK or Muse Code story (that's Films 8–9); no pricing
detail (that's Film 1).

**Cast per act (one look):** key = terracotta key glyph + masked card;
address = two URL cards with the `/v1` struck through; the three ways =
request/response arrows, two unchanged code cards, the messages-array card;
errors = error rows fixed one by one with green checks; the stance = ringed
REST card, crossed-out "first-party SDK" box.

**Source facts:**
- API key generation happens in the Meta developer console. (transcript §9)
- The OpenAI SDK is used with a base-URL swap; no `/v1` path segment is
  appended. (transcript §9 / film brief)
- The Anthropic SDK port uses the messages structure: a messages array with
  roles, system instructions in the system role, max tokens set explicitly.
  (transcript §9)
- Debugging happened through the API's error messages. (transcript §9)
- No first-party Meta SDK is presented in the course; the API speaks
  OpenAI- and Anthropic-compatible dialects. (transcript §9 — "by design" is
  the instructor's reading, labeled as judgment in FACTCHECK.md)

**LEFT OUT (with reasons):**
- Streaming responses — a playground control in Film 2, not part of the
  code story here.
- The agent SDK — Film 8's subject.
- LangChain integration — Film 8's subject.
- Exact endpoint hostnames — not in the source notes; the film stays at the
  "swap the domain" level rather than printing an unverified URL.
- Model names in the request body — the film says "the model name" without
  asserting a specific string, to avoid stating a wrong one.
