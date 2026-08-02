# Anthropic courses Video Ideas

## Candidate 1 — Why does changing one number in a prompt cascade into wildly different outputs?
- Source: `prompt_engineering_interactive_tutorial/README.md`
- Topic: Prompt refinement through iteration
- Hook: A prompt that fails silently can be fixed, but you must observe which specific phrase caused the failure.
- Key case: Student submits "Explain quantum physics" → Claude produces 10-page essay → student adds "in one paragraph for a five-year-old" → Claude produces one short paragraph.
- The Question: Which prompt elements reliably predict which response improvements?
- Core idea: Direct feedback loop between prompt edits and response changes; each observation narrows design space.
- Visual object: Split-screen: original response vs. revised response after single phrase addition.
- Manim move: `compare`
- Example seed: User asks "Summarize this essay" → gets 5 pages back → adds "in fewer than 100 words" → gets 85 words exactly.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: basic prompt writing
- Exclusions: do not explain model internals or why Claude behaves differently (focus on observable input–output loop only)
- Score: 8/10

## Candidate 2 — A prompt stays broken until you name what it should do differently.
- Source: `real_world_prompting/03_prompt_engineering.ipynb`
- Topic: Systematic prompt improvement workflow
- Hook: You have a vague goal and a broken prompt; the fix is not "try again" but a measurable process.
- Key case: Summarization prompt fails on medical papers → add "focus on study design" → test on 10 papers → 7/10 pass → add "list limitations in final paragraph" → test again → 9/10 pass.
- The Question: What's the sequence of steps that turns a consistently failing prompt into one that works on new data?
- Core idea: Iterative loop accumulates small refinements; each test reveals one missing constraint; each constraint addition pushes success rate up.
- Visual object: Line chart of pass rate over iterations (steps climb from 20% → 40% → 70% → 90%).
- Manim move: `accumulate`
- Example seed: Customer-support chatbot ignores policy docs at first → add "reference [Policy section 3.2]" → test with 20 tickets → 60% cite policy correctly → refine citation format → 85% cite correctly.
- Length band: 3–5 min
- Still lanes: c2v with metric overlay
- Prerequisites: prompt writing, test harness (code)
- Exclusions: do not teach domain-specific constraints (medical, legal); focus on the measurement-feedback cycle only
- Score: 8/10

## Candidate 3 — Claude has 10 tools and must pick one; what decides the choice?
- Source: `tool_use/05_tool_choice.ipynb`
- Topic: Tool selection logic under ambiguity
- Hook: The same request could invoke multiple tools; Claude's decision depends on tool descriptions and one hidden parameter.
- Key case: User asks "estimate the expense"; could call `calculator`, `statistical_tool`, or `budget_estimator`. Tool-choice parameter controls which one responds.
- The Question: What information drives Claude toward one tool instead of equally plausible alternatives?
- Core idea: Tool-choice parameter (auto/any/required) + tool description clarity reshape invocation probability; ambiguous descriptions cause wrong tool to be selected.
- Visual object: Request flowing into decision node; three outgoing branches, one highlighted based on parameter setting.
- Manim move: `split`
- Example seed: "What time is sunset?" → could call `calendar_tool` or `astronomy_tool` → if descriptions are identical, pick unpredictably; add precision ("return exact time and refraction offset") → clarifies which tool owns the answer.
- Length band: 2–3 min
- Still lanes: c2v (request to tool routing)
- Prerequisites: function calling basics, tool definitions
- Exclusions: omit tool-calling protocol details; focus on decision logic only
- Score: 8/10

## Candidate 4 — Three graders see the same output and give three different grades.
- Source: `prompt_evaluations/README.md`
- Topic: Evaluation method trade-offs
- Hook: You have one output; is it correct? The answer depends on which grader you ask.
- Key case: Prompt output: "The capital of France is Paris, France." Code grader checks format (pass). Human grader sees redundancy and rates lower. Model grader notes unnecessary words and scores 0.8 instead of 1.0.
- The Question: Why do different grading methods assess the same output differently?
- Core idea: Graders filter by different criteria. Code catches structure/format. Human catches intent misses. Model grader catches subtle semantic wrongness. Each surfaces a different failure mode.
- Visual object: Single output fanning into three parallel evaluation pipelines; three different pass/fail or score results emerge.
- Manim move: `split`
- Example seed: Legal document summary checked by: (1) code grader (word count within bounds? yes), (2) human lawyer (did it miss case law? maybe), (3) model grader (does it contradict any clause? no, but score 0.82 due to tone).
- Length band: 2–3 min
- Still lanes: c2v (three grading paths)
- Prerequisites: prompt evaluation fundamentals
- Exclusions: do not explain promptfoo internals or model-grading implementation; focus on why grader choice matters
- Score: 7/10

## Candidate 5 — Why does showing one word at a time feel faster than waiting for all words at once?
- Source: `anthropic_api_fundamentals/05_Streaming.ipynb`
- Topic: Streaming response delivery
- Hook: The user sees instant feedback; tokens arrive one at a time and a renderer accumulates them into words.
- Key case: User hits "send" at 0ms → token "The" arrives at 100ms → "capital" at 150ms → "of" at 200ms → full phrase rendered as it arrives; complete response after 2.5s. Non-streamed: waiting silent until 2.5s, then full response appears.
- The Question: Why does distributing delivery across time feel like improvement when total time is nearly identical?
- Core idea: Streaming emits tokens as generated; client accumulates and renders; perceived latency drops because partial output is visible within 100ms, not zero.
- Visual object: Text appearing character-by-character on screen with cursor blinking after each token.
- Manim move: `accumulate`
- Example seed: Claude response "The answer is 42" — streaming shows "The" (100ms) then "answer" (150ms) then final — vs. non-streaming: silence then entire phrase at 2.5s.
- Length band: ~1 min
- Still lanes: raster with streaming indicator or text cursor
- Prerequisites: understanding tokens
- Exclusions: do not explain token generation or model inference; focus on delivery and rendering only
- Score: 7/10

## Candidate 06 — The JSON you need is hiding in a tool you never plan to call
- Source: `tool_use/03_structured_outputs.ipynb`
- Topic: Coercing structured output via tool schema
- Hook: Asking Claude to "output JSON" still produces prose; defining a fake tool you never execute makes the problem vanish.
- Key case: Evaluation pipeline needs `{"label": "pass", "score": 0.91, "reason": "..."}` on every call. Prompt says "Return valid JSON" → Claude outputs "Here is the JSON: ..." with prose wrapper → downstream parser raises exception. Define a `record_result` tool with identical schema → Claude invokes it → pure JSON lives in the `tool_use` block → parser succeeds on every call.
- The Question: Asking for JSON should produce JSON; routing output through a tool schema you don't need should not fix a formatting problem — why does it?
- Core idea: Tool invocation is a structurally distinct output channel from text generation; filling a schema forces the model into a mode where the output must conform to field types and names, rather than layering a formatting preference on top of free-form text.
- Visual object: Two code blocks side by side — raw message output with prose contamination vs. `tool_use` block containing clean JSON — one green checkmark (parser passes), one red X (parser fails).
- Manim move: `transform`
- Example seed: "Classify this review as positive/negative/neutral with a 0–1 confidence." Free-text: "I'd say **positive** (about 0.8 confident)." Tool schema mode: `{"label": "positive", "confidence": 0.8}` — illustrative.
- Length band: 2–3 min
- Still lanes: c2v (output-channel switching)
- Prerequisites: JSON basics, tool use overview
- Exclusions: omit tool-choice mechanics (covered in Candidate 3), API request structure, server-side parsing of the `tool_use` block
- Score: 9/10
