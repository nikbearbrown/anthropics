# Source outline — MetaMuse Code Essentials (course transcript, inspiration)

Full transcript of Andrew Brown's ~3-hour MetaMuse Code Essentials course.
This outline is the working source; the verbatim transcript is the inspiration
behind it. Timestamps are from the transcript chapters.

## 1. Introduction & course overview (0:00–0:49)
- Meta's new models (Muse Spark) + new coding harness (Muse Code).
- Thesis: a first-class company with its own trained models and its own
  harness, fully vertically integrated, is an option worth using in the EI space.

## 2. Models, architecture & pricing (0:49–12:08)
- Llama (well known); course focus is Spark and Glimmer.
- Muse Spark: v1.2 latest checkpoint (1.1 earlier); multimodal (text, image,
  video, audio in/out).
- Contributor offering: deep discounts for sharing data; much lower rate
  limits (~100 req/min mentioned).
- Muse Glimmer: 30B parameters, open weights (not open source), runs on a
  single GPU (e.g. RTX 5090 32GB); trained on 100+ languages.
- Benchmarks: "Goldilocks" — upper-middle on most leaderboards, "third best at
  everything"; fast and cost-effective.
- Pricing: token usage, no subscription. Roughly $1.25/M input, $0.10/M output
  (transcript audio is garbled here — verify against docs before filming).
  No batch pricing at time of recording. Web-search grounding billed per 1k queries.
- REST API; OpenAI-compatible AND Anthropic-messages-compatible (change base
  URL; note: no `/v1` hyphen on the Meta endpoint). No first-party SDK by design.
- Works with OpenCode, Claude Code, Codex harnesses; Muse Code is Meta's own.

## 3. Meta AI playground (12:14–14:59)
- dev.meta.ai / developers.meta.com; attach card, set a spend limit (no $5
  minimum; charged once past ~$1).

## 4. Prompting + vision (14:59–20:59)
- Reasoning effort levels; streaming; grounded search toggle; JSON schema.
- JLPT N5 grammar list prompt (quality test); NHK News Easy screenshot
  transcription — 100% accurate incl. kanji/kana.

## 5. Website from a reference image (20:59–26:00)
- Retro PHP-Nuke three-column concept for a tech community; system instruction
  (front-end dev, single HTML file, no CSS framework, flexbox, lean markup,
  mobile-friendly); judging output; asking for one more pass.

## 6. Brainstorming + mermaid diagrams (26:00–36:38)
- Community-engagement plugin ideas; mermaid mind map; iterating outer
  branches into grounded examples; editor tooling friction (not the model).

## 7. Search grounding (36:45–44:52)
- Same question with/without grounding (Dodge Grand Caravan control arms,
  Canada); grounded answer adds retailers, shipping, price reality;
  grounding can't penetrate blocked product pages.

## 8. Structured outputs / JSON Schema (44:57–59:58)
- Schema constrains reasoning, not just format; Japanese-grader rubric schema;
  challenge → attempt → graded JSON; feeding JSON back to render an HTML report.

## 9. Programmatic API use (59:58–1:14:39)
- API key generation; OpenAI SDK with base-URL swap; Anthropic SDK port
  (messages structure, system role, max_tokens); debugging via error messages.

## 10. Agent SDK framework (1:14:45–1:21:38)
- Anthropic agent SDK driving a coding task (tic-tac-toe in Ruby).

## 11. LangChain with Muse (1:21:38–1:36:38)
- TypeScript; OpenAI-compatible integration; env config; debugging with the
  agent SDK's help.

## 12. Claude Code pointed at Muse (1:36:49–1:44:14)
- Wrapper script injecting the Meta API key via env; launching Claude Code on
  Muse Spark 1.2; a small refactor task.

## 13. Muse Code CLI (1:44:22–3:00:31)
- Single-line install; bubblewrap sandbox; skills loaded from everywhere.
- agents.md as project context (`muse init`).
- settings.json (global), trust files, reasoning effort default.
- Reasoning effort control: low / medium / high / extra high (per-session vs default).
- Sessions: resume, status (tokens, context %), compact, clear.
- Goal feature: decomposing + driving a backend build autonomously.
- Full-stack: Go + SQLite on one VM, Docker Compose (backend/frontend/MinIO),
  React frontend wired to real endpoints.
- Model switching via CLI; YOLO mode (full permissions, no sandbox);
  headless mode (`-p`, JSON output, prompt files).
- Custom skills (create + trigger); project memory (memory.md);
  approval modes (on-request / untrusted / never); guardrail toggles;
  MCP servers (add via settings, restart, debug — DuckDuckGo VQD lesson).

## Factcheck flags (verify against Meta docs before any film)
- Exact input/output pricing numbers; contributor discount + rate limits.
- Glimmer parameter count and GPU requirement; language count.
- Batch pricing availability (transcript says none — may have changed).
- Playground URL and billing mechanics; the `/v1` base-URL quirk.
- Benchmark claims ("third best", "upper middle") — attribute or cut.
