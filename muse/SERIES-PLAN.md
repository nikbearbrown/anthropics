# SERIES-PLAN.md — Muse tutorial film series

**Series:** How to use Muse (Meta's Muse Spark / Muse Glimmer models and the
Muse Code harness), taught as lecture films.
**Channel:** @NikBearBrown · **Persona:** Liam, in for Bear · **Voice:** Kokoro `am_onyx`
**Skill:** `lecture` (brutalist.art) · **Register:** Teardown
**Status:** plan — no film built yet. Films are built in order, one complete
pre-render package at a time.

## What this series is

A newcomer to Muse should be able to watch the series in order and go from
"what is Muse" to shipping a real full-stack app with Muse Code — without
having read anything else or seen any other film (self-contained law: no "as
we saw last time", no "this chapter").

## The set of lectures (12 films)

### Film 1 — What Muse Is
- **Core promise:** the viewer can name the three models, say what each is for,
  and explain why a vertically integrated model company matters.
- **Source coverage:** course intro + models/pricing section (transcript 0:00–12:08).
- **Key beats:** the vertical-integration idea (own models + own harness);
  Muse Spark 1.2 (managed, multimodal); Muse Glimmer (30B open weights, single
  GPU); Llama in one line; benchmarks as the "Goldilocks" model; token pricing
  vs subscriptions; contributor pricing and its rate-limit tradeoff.
- **Est.:** 6–8 min.

### Film 2 — Your First Prompts
- **Core promise:** the viewer can open the Meta AI playground, set a spend
  limit, and run a first prompt with the right reasoning effort.
- **Source coverage:** playground walkthrough + first prompts (12:14–17:00).
- **Key beats:** creating the account; spend limits (no $5 minimum, charged
  past $1); the playground controls (model picker, reasoning effort,
  streaming); a first real prompt (the JLPT grammar list); reading output
  quality like a practitioner.
- **Est.:** 5–7 min.

### Film 3 — Muse Can See
- **Core promise:** the viewer knows two visual superpowers: transcribing
  images and building a web page from a reference image.
- **Source coverage:** vision transcription + PHP-Nuke website build (17:00–26:00).
- **Key beats:** screenshot → accurate transcription (NHK News Easy);
  reference image → single-file HTML (the retro three-column concept); writing
  the system instruction (front-end developer, no CSS framework, flexbox,
  mobile-friendly); judging the result and asking for one more pass.
- **Est.:** 7–9 min.

### Film 4 — Thinking on Canvas
- **Core promise:** the viewer can use Muse as a brainstorming partner that
  draws its thinking.
- **Source coverage:** community-engagement brainstorm + mermaid mind maps
  (26:00–36:38).
- **Key beats:** from "make funner plugins" to a bullet list of ideas; asking
  for a mermaid mind map; iterating (outer branches → grounded examples);
  what to do when the diagram tooling fights back.
- **Est.:** 5–7 min.

### Film 5 — Grounded Answers
- **Core promise:** the viewer knows when to turn on search grounding and what
  it costs.
- **Source coverage:** grounded vs ungrounded comparison (36:45–44:52).
- **Key beats:** the same question twice (Dodge Grand Caravan control arms);
  what grounding adds (current prices, Canadian retailers, shipping reality);
  the per-query cost; what grounding cannot reach (blocked product pages).
- **Est.:** 5–7 min.

### Film 6 — Structured Outputs
- **Core promise:** the viewer can make Muse return JSON that obeys a schema —
  and turn that JSON into something a human can read.
- **Source coverage:** JSON schema grading rubric + report page (44:57–59:58).
- **Key beats:** why schema constrains reasoning, not just formatting; building
  the rubric schema; the Japanese-grader loop (challenge → attempt → graded
  JSON); feeding the JSON back in to render an HTML report.
- **Est.:** 7–9 min.

### Film 7 — Muse in Code
- **Core promise:** the viewer can call Muse from Python three ways: raw REST,
  the OpenAI SDK, and the Anthropic SDK.
- **Source coverage:** programmatic API integration (59:58–1:14:39).
- **Key beats:** generating an API key; the base-URL swap (no `/v1` hyphen
  quirk); minimal OpenAI-SDK call; porting it to the Anthropic SDK (messages
  structure, system vs developer role); reading the error messages when it
  breaks.
- **Est.:** 7–9 min.

### Film 8 — Agents and Frameworks
- **Core promise:** the viewer can drop Muse into the agent tools they already
  use.
- **Source coverage:** agent SDK + LangChain + Claude Code on Muse (1:14:45–1:44:14).
- **Key beats:** the Anthropic agent SDK driving a coding task; LangChain via
  the OpenAI-compatible integration (TypeScript); the wrapper script that
  launches Claude Code pointed at Muse Spark; what "works but looks odd"
  means in a foreign harness.
- **Est.:** 7–9 min.

### Film 9 — Muse Code, the Harness
- **Core promise:** the viewer can install Muse Code and drive it: configure,
  prompt, resume, and run it headless.
- **Source coverage:** install through headless mode (1:44:22–2:43:09).
- **Key beats:** single-line install; `agents.md` as project memory;
  settings.json and reasoning effort (low → extra high); sessions: resume,
  status, compact, clear; YOLO mode and when not to use it; headless mode for
  scripts.
- **Est.:** 9–12 min.

### Film 10 — Memory, Skills, and Guardrails
- **Core promise:** the viewer can teach Muse Code their preferences, extend
  it with skills and MCP servers, and keep it sandboxed.
- **Source coverage:** skills, memory, approvals, sandbox, MCP (2:37:52–3:00:31).
- **Key beats:** project memory (the CSS rule, done right); creating a custom
  skill and triggering it; approval modes (on-request / untrusted / never);
  Bubblewrap sandboxing and network policy; adding an MCP server and
  debugging it when it fails (the DuckDuckGo lesson: MCP working ≠ source
  cooperating).
- **Est.:** 8–10 min.

### Film 11 — Capstone: Ship a Full-Stack App
- **Core promise:** the viewer watches a real app go from idea to running
  containers, driven by goals.
- **Source coverage:** Tech Nuke backend + frontend integration (1:58:21–2:36:02).
- **Key beats:** scoping the backend doc (Go, single binary, SQLite on one VM);
  the goal feature decomposing and driving the build; Docker Compose (backend,
  frontend, MinIO standing in for S3); wiring the React frontend to real
  endpoints; registering, posting, and the honest list of what is still rough.
- **Est.:** 10–14 min.

### Film 12 — Muse the Agent: What It Does, Who Pays, and How to Survive It
- **Core promise:** the viewer understands what Meta's consumer agent actually
  is, how Meta makes money from it, where the sharp edges are, and the five
  rules that keep an agent from ruining their week.
- **Source coverage:** `source/muse-agent-brief.md` (§§1–6),
  `source/session-summary-blast-radius.md` (Parts I–V),
  `source/compartmentalization.md`.
- **Key beats:** what the agent is (goal → plan → acts, approval before
  consequential actions; endurance, not intelligence — "it saves time, not
  thought"); what it does (errands, connectors, small business, the missing
  creative tools); pricing tiers and the transaction-fee business model (who
  really pays; the intent layer; why heavy non-transacting users are pure
  cost); security concerns (Full Disk Access, deny-list vs allow-list,
  prompt injection as adversarial probability, approval fatigue, trust by
  design); the safe setup (assume breach, blast radius, caps outside the
  agent, the short list: email, money, credentials, public voice);
  compartmentalization as the mental model (bulkheads, Saltzer & Schroeder,
  the recoverability 2×2); the five rules for ordinary people.
- **Est.:** 12–16 min. The capstone of the series: everything Films 1–11
  taught about using the models, applied to surviving the agent.
- **Note:** this film is about the muse.ai consumer agent, distinct from the
  Spark/Code developer track of Films 1–11. If Bear prefers, it can stand
  alone outside the numbered series.

## Per-film package (what "done" means)

Each film ships as a pre-render package in `muse/film-NN-<slug>/`, containing
the lecture-skill output contract adapted to the film-builder gate:

| File | What it is |
|---|---|
| `ACTS.md` | Coverage map: source section → act, LEFT OUT with reasons, cast per act |
| `SHOTLIST.md` | Per body beat: about \| lane \| runner-up \| why this one wins |
| `FACTCHECK.md` | Every claim: Verified (record) / Judgments (judgment) / Cut or disclosed |
| `make_sheet.py` | Generates `beat_sheet.json`; asserts beat counts and totals |
| `beat_sheet.json` | The script: generated, indented |
| `scenes.py` | The visuals (Manim + Remotion per the lecture lane picks) |
| `SOURCES.md` | Fact → source table |
| `BUILD-LOG.md` | Dated build steps, including failures |
| `CHECKS-REPORT.md` | QC results per scene + issues found and fixed |
| `PROMPTS.md` | Prompts that shaped the film, in order ("no generation prompts" if none) |
| `CLAUDE-CODE-RENDER.md` | Render instructions for Bear's Mac |

Spine per film (lecture law): BIDEA hesitant writer → BDEFS key terms →
acts → BVDT recap → BHTF your turn → BOUT @NikBearBrown outro. No cap on
length; one film per lecture; never split, never pad.

## Build order

1. This plan (done — pushed).
2. Per film, in order: read the source slice → ACTS.md → SHOTLIST.md →
   FACTCHECK.md → make_sheet.py → beat_sheet.json → scenes.py → static QC
   gate (0 errors, 0 warnings) → docs → push the 11 files → verify via API →
   log in FRICTIONAL.md.
3. Bear renders locally with Kokoro `am_onyx` + the render instructions.
   Nothing is published without his word.

## Open questions for Bear

- Series title card wording (working title: "Muse").
- Whether Films 9–11 should stay three films or compress to two.
- Film 12 stands alone as the Muse-agent film — confirm it stays in the
  numbered series or ships as a standalone.
- Any source material beyond the transcript and the three briefs to fold in
  (docs, the Meta developer site) before Film 1's factcheck.
