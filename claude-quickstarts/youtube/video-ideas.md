# Claude Quickstarts Video Ideas

## Candidate 1 — Bridging the pixel gap between Claude's vision and the desktop
- Source: `browser-use-demo/browser_use_demo/tools/`
- Topic: Coordinate transformation in browser automation
- Hook: Claude sees a resized screenshot but must click on the original desktop—pixels don't align.
- Key case: User asks Claude to click a button on a news website. Claude processes the screenshot at 1456×819 pixels (API standard), the actual browser viewport is 1920×1080, and the button is at different (x, y) on each.
- The Question: If Claude returns coordinates for a 1456×819 image, how do I translate that to the real 1920×1080 screen without the click landing in the wrong spot?
- Core idea: Automatic coordinate scaling via the inverse of the resize ratio. When Claude clicks at (x=700, y=410) on the 1456×819 screenshot, compute the real position as `(700 * 1920/1456, 410 * 1080/819) = (960, 540)`.
- Visual object: Two screenshots side-by-side, one labeled "Claude sees this (1456×819)" and one "Desktop is this (1920×1080)", with a clickpoint marked on each and a scaling formula connecting them.
- Manim move: split
- Example seed: Original screen 2560×1440 (button at x=1280, y=720). Claude processes at 1456×819. Claude returns (x=728, y=409). Scaled click: (728 * 2560/1456, 409 * 1440/819) = (1280, 720)—a perfect hit.
- Length band: 2–3 min
- Still lanes: raster with c2v overlay
- Prerequisites: screen coordinates, image resizing, aspect ratios
- Exclusions: actual DOM navigation, other forms of computer-use coordinate scaling
- Score: 9/10

## Candidate 2 — Stable reference IDs survive viewport chaos
- Source: `browser-use-demo/browser_use_demo/browser_tool_utils/`
- Topic: Element reference targeting in dynamic web UIs
- Hook: Pixel-based automation breaks every time the browser window resizes; element references should survive.
- Key case: User asks Claude to click a submit button at pixel (960, 540) on a 1920×1080 screen. User resizes browser to 1440×900. The button is now at (720, 405). Same button, different pixels.
- The Question: If I tell Claude to click a button by its (x, y) position, how do I ensure the command still works after the page reflows or the window resizes?
- Core idea: Pre-compute stable element references (e.g., `ref="submit_btn_27"`) using JavaScript, then target clicks by ref instead of coordinates. The ref persists; the pixel position doesn't.
- Visual object: A webpage screenshot shrinking and growing (viewport resizing) while a button's `ref=` label stays constant and a coordinate pair shifts beneath it.
- Manim move: morph
- Example seed: Button "Confirm Order" at x=960 y=540 on 1920×1080, then at x=720 y=405 on 1440×900. JavaScript assigns `ref="confirm_order_1"` on both. Claude always clicks `ref="confirm_order_1"` and lands on the button every time.
- Length band: 2–3 min
- Still lanes: raster with code annotations
- Prerequisites: CSS selectors, DOM trees, coordinate brittleness
- Exclusions: JavaScript execution details, CSS specificity rules
- Score: 9/10

## Candidate 3 — Caching pixels you've already seen
- Source: `computer-use-best-practices/README.md`
- Topic: Prompt caching to avoid re-tokenizing repeated screenshots
- Hook: Each agent turn takes a new screenshot, but the desktop often hasn't changed—sending thousands of redundant pixels to the API wastes tokens and time.
- Key case: An agent completes a 50-turn task (e.g., filling a form, navigating between windows). In 35 of those turns, the desktop screenshot is identical. The agent still sends it to Claude all 50 times.
- The Question: If most of the screenshots in a long task are near-duplicates or unchanged, why re-tokenize and re-process them instead of reusing the first one?
- Core idea: Prompt caching with ephemeral control—hash the screenshot, send it with `cache_control={"type": "ephemeral"}` on the first turn, then reference it by cache hash on subsequent turns. The API returns a cache hit (instant, zero tokens) instead of re-tokenizing.
- Visual object: A filmstrip or timeline of 50 sequential screenshots, most identical, with visual markers showing which turns hit the cache (fast, green) vs. required tokenization (slow, red).
- Manim move: accumulate
- Example seed: 50-turn task, 5 unique desktop states visited (A → A → A → B → B → C → C → C → A → A …). First visit to each state sends full screenshot (~2000 tokens). Revisits in later turns are cache hits (~0 tokens). Total: 5 × 2000 = 10,000 tokens instead of 50 × 2000 = 100,000.
- Length band: 3–5 min
- Still lanes: raster with token-count labels
- Prerequisites: prompt context, tokens, LLM API calls, caching semantics
- Exclusions: full caching protocol, cache eviction policies
- Score: 9/10

## Candidate 4 — Persisting progress across context windows
- Source: `autonomous-coding/autonomous_agent_demo.py`
- Topic: Multi-session autonomous work with feature-list checkpoint
- Hook: An agent with 200 features to implement faces fresh context each session—it forgets everything but can't restart from scratch.
- Key case: Agent completes 50 features in session 1 (builds a to-do list, implements features, commits). Session 2 starts with a blank slate and no prior conversation history. Agent must know which 150 features remain without re-reading the entire codebase.
- The Question: If the agent loses all in-context memory between sessions, how does it resume work-in-progress without either repeating completed features or losing track of what's left?
- Core idea: Externalize state to two files: `feature_list.json` (source of truth, each feature marked true/false for passing) and git history (immutable record of commits). Each session: read the feature list, find uncompleted features, implement one, run tests, commit, mark as passing.
- Visual object: A `feature_list.json` file mutating over time (rows checking off, status changing from `"incomplete"` to `"passing"`) across multiple session boundaries shown as vertical dividers.
- Manim move: accumulate
- Example seed: feature_list.json: 200 items, all initially `{"id": 1, "status": "incomplete"}`. Session 1 runs, implements features 1–50, marks them passing, commits. Session 2 reads file, sees items 51–200 uncompleted, starts at item 51. By end of session 2, items 51–100 are passing.
- Length band: 3–5 min
- Still lanes: c2v (JSON diffs), geo (session timeline)
- Prerequisites: version control (git), test suites, API context limits, session persistence
- Exclusions: how the agent generates the initial feature list, detailed testing framework
- Score: 8/10

## Candidate 5 — Two resolutions, one click
- Source: `computer-use-best-practices/computer_use/image.py`
- Topic: Coordinate scaling in macOS computer-use agents
- Hook: macOS returns screenshots at native resolution, but the Claude API expects 1456×819 (for correct vision processing); clicks must reverse the transform.
- Key case: Agent takes a screenshot on a MacBook Pro (2560×1600 display), API resizes it to 1456×819. Agent clicks at (x=728, y=410) on the resized image. The click must land at the corresponding spot on the original 2560×1600 desktop.
- The Question: When the API applies target_image_size() to fit Claude's vision, how do coordinates flow backward from the model's perception to the physical screen?
- Core idea: Precompute the resize ratio, then scale coordinates back: `real_x = model_x * original_width / sent_width`. Example: (728 * 2560 / 1456, 410 * 1600 / 819) lands the click at the right spot on the native display.
- Visual object: Two side-by-side screenshots labeled "Original 2560×1600" and "Claude sees 1456×819", each showing the same desktop scene, with a coordinate pair and scaling formula visibly connecting them.
- Manim move: split
- Example seed: Native display 1920×1080, button at (960, 540). Sent to API at 1456×819. Claude sees button at (728, 409). Scaled click: (728 * 1920/1456, 409 * 1080/819) = (960, 540). Lands exactly on the button.
- Length band: 2–3 min
- Still lanes: raster with c2v formula
- Prerequisites: screen coordinates, image resizing, aspect ratios
- Exclusions: batched tool calls, trajectory recording, other computer-use optimizations
- Score: 8/10

## Candidate 06 — One round trip instead of three: batch tool calls collapse sequential latency
- Source: `computer-use-best-practices/README.md`
- Topic: Batching predictable tool calls to reduce agent round trips
- Hook: When the model can predict every step of a sequence will succeed, waiting for each API result before sending the next one wastes time it didn't need to spend.
- Key case: Agent task: "Open Terminal, type `ls`, press Enter." Model issues action 1 (open Terminal), waits for result, issues action 2 (type `ls`), waits, issues action 3 (press Enter). Three round trips. All three outcomes were predictable before any result arrived.
- The Question: If the model already knows open-terminal → type-ls → press-Enter will succeed in sequence, why does it wait for each result before sending the next command?
- Core idea: `computer_batch` / `browser_batch` let the model emit a list of actions in one API response; the harness executes them in order and returns all results together. When the model issues only one action, `BATCH_REMINDER` is appended to its next context window — a nudge that pushes it to batch on the following turn.
- Visual object: Two side-by-side timelines labeled "Sequential" (3 alternating narrow request bars and wide wait bars) and "Batched" (1 request bar, then 3 result bars returned together), with total elapsed time labeled on each.
- Manim move: collapse
- Example seed: "Open Terminal, type `ls`, press Enter." Sequential: 3 round trips × 5 s = 15 s. Batched: 1 round trip (5 s) + 3 local executions (≈0 s) = 5 s. Three-step sequence saves 10 s (67% reduction). Ten-step sequence saves ~45 s.
- Length band: 2–3 min
- Still lanes: geo (timeline comparison), c2v (batch list structure)
- Prerequisites: API round trips, latency basics, tool use loop
- Exclusions: server-side compaction, prompt caching, trajectory recording, multi-step planning strategies
- Score: 8/10

## Candidate 07 — Screenshots accumulate until a threshold fires and the server forgets
- Source: `computer-use-best-practices/README.md`
- Topic: Threshold-triggered context compression in long agent runs
- Hook: A computer-use agent re-sends every prior screenshot on every API call; after 30 turns the image history alone is 45,000 tokens you pay for even though Claude only needs the current view.
- Key case: 30-turn task. Each turn takes one screenshot at roughly 1,500 tokens. By turn 30, the agent re-sends 30 × 1,500 = 45,000 image tokens in a single call — more than the entire fresh conversation cost at turn 1.
- The Question: If image context accumulates at 1,500 tokens per turn and eventually dominates API cost, why doesn't the agent discard old screenshots as new ones arrive?
- Core idea: `autocompaction_trigger_tokens` sets a threshold. Once total input tokens cross it, the server runs a separate sub-call that condenses older context into a compact summary block; the client drops everything before that block on the next turn. Cost resets without losing semantic progress.
- Visual object: A stacked bar chart growing turn by turn (screenshots in red, text in blue) rising toward a horizontal threshold line, then collapsing to a small "summary" bar at the trigger point, before growing again.
- Manim move: accumulate
- Example seed: Threshold: 40,000 tokens. Turns 1–26 accumulate to ~39,000 tokens (26 × 1,500 image + text). Turn 27 crosses the threshold. Server summarizes → client receives a 2,000-token summary block. Turn 28 starts at 2,000 tokens instead of 42,500.
- Length band: 2–3 min
- Still lanes: geo (stacked-bar timeline), c2v (config line for trigger threshold)
- Prerequisites: token context windows, LLM pricing by token, prompt context accumulation
- Exclusions: prompt caching (different mechanism — avoids re-tokenizing identical screenshots rather than compressing growing history), image pruning heuristics, trajectory recording
- Score: 7/10
