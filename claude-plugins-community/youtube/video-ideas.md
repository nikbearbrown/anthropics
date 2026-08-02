# Claude Plugins — Community Video Ideas

## Candidate 1 — Why prompt-burned subtitles hallucinate while ASR endpoints don't
- Source: `quickdesign/skills/quickdesign/references/auto-subtitle.md`
- Topic: Subtitle accuracy; when to offload to specialized tools
- Hook: Seedance can burn captions into video via prompt, but they hallucinate — mismatched words, wrong timing, paraphrased dialogue.
- Key case: User requests burned-in captions in a Seedance prompt. Seedance renders "beutiful product" over audio that says "beautiful product." User reruns with the dedicated `quickdesign video subtitle` endpoint; captions now match every word at word-level timing.
- The Question: X (prompt-burned subtitles) should be convenient, but this case shows systematic hallucination; why would delegating to a specialized tool help?
- Core idea: The dedicated subtitle endpoint extracts the actual audio from the video, runs ElevenLabs ASR to get word-level timing, and renders captions with libass (subtitle engine) grounded in real speech data. Image generation models can't see or reason about audio — they guess at captions. ASR + rendering sees.
- Visual object: Two vertically stacked video frames side by side (top: AI-hallucinated misaligned captions over video; bottom: real ASR captions perfectly synced).
- Manim move: compare
- Example seed: User generates a 15s UGC reel. With Seedance prompt-burning: captions lag the speech by 2 frames and skip the second sentence. With `quickdesign video subtitle --style tiktok`: captions arrive word-on-word, animated per-word, zero hallucination.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: video generation, ASR, libass
- Exclusions: Don't explain Seedance's rendering pipeline, don't dive into ElevenLabs API details, don't cover other subtitle tools.
- Score: 9/10

## Candidate 2 — Async job submission lets long operations free the terminal
- Source: `quickdesign/README.md` (image/video generate + status/wait commands)
- Topic: Async job patterns; terminal blocking vs. polling
- Hook: Video generation can take 8–15 minutes. If the CLI blocks waiting, the user's terminal is stuck. But the CLI doesn't have to block.
- Key case: User runs `quickdesign video generate --prompt "..." --duration 90 --wait`. The command blocks for 12 minutes. Meanwhile, in another terminal, a colleague runs the same command without `--wait`, gets a job ID back instantly, runs other tasks, then polls `quickdesign video wait <jobId>` when ready.
- The Question: X (synchronous wait) should be simple and guaranteed, but this case shows the terminal locks up; why would async-with-polling be worth the extra complexity?
- Core idea: The CLI spawns the job asynchronously (returns a jobId immediately), storing the ID on disk or returning it to stdout. The user can then either block with `--wait` (simple case) or come back later with `quickdesign video wait <jobId> --timeout 30m` (non-blocking case). The same job can be queried by multiple clients.
- Visual object: Timeline with a decision point: "generate (instant, returns ID)" → branches into (A) "wait (blocks terminal, get result)", or (B) "do other work, poll later (terminal free, same result)."
- Manim move: split
- Example seed: User spawns a 90s Seedance video (`--wait` omitted), gets job ID "sora-12345" back in 2s, runs `quickdesign spy brands --search "nike"` in the meantime (5 min), then `quickdesign video wait sora-12345 -o final.mp4`. Total time: 13 min. Terminal never blocked.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: job queues, polling, exit codes
- Exclusions: Don't explain webhook callbacks or streaming responses, don't cover job timeout tuning or retry strategies, don't dive into the API backend.
- Score: 7/10

## Candidate 3 — Edit-mode prompts preserve source authenticity while compose-mode regenerates
- Source: `quickdesign/skills/quickdesign/references/avatar-edit-not-regenerate.md`
- Topic: Prompt phrasing and image model behavior; preserving source fidelity
- Hook: A creator uploads a phone selfie. You ask an image model to add a product to it. If you say "compose a frame," you get a fresh AI render. If you say "edit the photo," you get the original with a tweak — same grain, same light, same authenticity.
- Key case: Creator uploads a casual selfie (lo-fi, phone-captured grain, soft daylight). You prompt: "Compose a vertical 9:16 UGC creator selfie holding a sneaker." Banana renders a new image (polished lighting, removed grain, looks AI-made). Same creator, same image, but you change the verb: "Edit @Image1 to add a sneaker." Banana modifies the source (preserves grain, lighting, phone-selfie vibe).
- The Question: X (prompt phrasing shouldn't affect output) seems true, but these two prompts produce radically different authenticity; why does the verb choice matter?
- Core idea: Nano-banana-2 interprets "compose" as "render a fresh image inspired by these references" (which triggers tone-up, grain-removal, polish filters), and "edit" as "modify the source pixels" (which leaves the source's photographic character intact). The verb gates which code path the model takes.
- Visual object: Two side-by-side frames of the same person: (left) fresh AI-rendered selfie (flawless skin, studio lighting, synthetic); (right) modified selfie (original grain, casual lighting, real phone-photo feel).
- Manim move: compare
- Example seed: Creator Alice uploads a selfie (grainy, soft window-light). Prompt A: "Compose a UGC selfie holding a coffee mug." Banana renders a new face with studio lighting — Alice sees herself but polished. Prompt B: "Edit @Image1: add a coffee mug." Banana keeps Alice's exact grain and lighting, adds the mug. For UGC, Prompt B works because it preserves "realness."
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: image generation models, UGC authenticity
- Exclusions: Don't explain Gemini Flash or banana's architecture, don't cover compose-vs-edit for non-UGC use cases, don't dive into prompt engineering tuning.
- Score: 7/10

## Candidate 04 — Why "copyright restrictions" can mean three completely different things
- Source: `quickdesign/skills/quickdesign/references/brand-and-moderation.md`
- Topic: Moderation filter opacity; diagnosing aliased error messages in generative AI
- Hook: Seedance returns "may be related to copyright restrictions" whether you used a brand name, an aggressive verb, or an oral-contact detail — three different rules, one indistinguishable error.
- Key case: User prompts "Nike sneaker slammed on counter by creator holding it in her mouth." Generation fails: "may be related to copyright restrictions." User removes "Nike" — still fails. User changes "slammed" to "placed" — still fails. User removes the mouth-contact detail — passes. Three moderation rules fired at different attempts; the error string never changed.
- The Question: X (the error message) should identify what to fix; this case required three separate eliminations with no feedback between them; why would a moderation system collapse distinct causes into one signal?
- Core idea: Exposing which specific rule fired hands adversarial users a map for routing around it. So the system emits a single coarse "rejected" signal regardless of cause. Legitimate users pay the diagnostic cost: systematic elimination of candidate triggers with no gradient toward the real cause.
- Visual object: A three-branch tree — brand name node, aggressive verb node, oral-contact node — with all three arrows collapsing into one red leaf labeled "may be related to copyright restrictions."
- Manim move: collapse
- Example seed: Prompt "Nike Air being slammed down on a table by a sneakerhead holding it in his mouth." One error. Remove "Nike" → same error. Change "slammed" → "set" → same error. Remove mouth-contact framing → passes. Three eliminations, one error string throughout, no progress signal at any step.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: content moderation concepts, generative AI generation pipelines
- Exclusions: Don't explain nano-banana-2's separate Gemini oral-content policy, don't list specific trigger words or attempt to map the full rule set, don't cover kie.ai's Seedance moderation architecture.
- Score: 8/10

## Candidate 05 — Why a favorable crypto swap leaves a non-zero residual in the clearing account
- Source: `tres-finance-plugin/README.md`
- Topic: ASC 845 non-monetary exchange accounting; crypto clearing account zero-out
- Hook: A company swaps ETH for more USDC than the ETH is worth on the open market. Both legs hit the ledger. The clearing account should net to zero — but it doesn't, and GAAP is the reason.
- Key case: ETH market price: $1,900. Company swaps 1 ETH for 2,000 USDC (favorable rate). Ledger: outflow $1,900 ETH, inflow $2,000 USDC. Clearing account: +$100 residual. ASC 845 (Nonmonetary Transactions) requires the inflow to be repriced at the outflow's fair market value ($1,900), not the swap rate. After `tres-asc845-swap-reprice-skill` sets manual fiat value of the USDC inflow to $1,900: clearing = $0.
- The Question: X (recording both swap legs at the exchange rate) should balance the clearing account; this case shows a $100 residual; why does GAAP measure the inflow by what was surrendered rather than what was received?
- Core idea: ASC 845 treats a non-monetary exchange as: sell the asset given up at its FMV, then buy the asset received at that same FMV. The exchange rate between the two assets is irrelevant to the carrying value — preventing favorable-rate swaps from creating artificial gains on the ledger at the moment of exchange.
- Visual object: A two-row ledger — left column: 1 ETH out at $1,900; right column: 2,000 USDC in at $2,000. Red cell: clearing $100. Arrow labeled "ASC 845 reprice." Updated row: USDC in repriced to $1,900. Clearing cell turns green: $0.
- Manim move: accumulate
- Example seed: Company swaps 1 ETH → 2,000 USDC when ETH market = $1,900. Ledger shows $1,900 out / $2,000 in. Clearing: $100 residual. Skill queries the subtransaction, previews the reprice, applies `setManualFiatValue` to USDC inflow at $1,900. Clearing: $0. Audit passes.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: double-entry bookkeeping, fair value measurement, basic GAAP
- Exclusions: Don't explain FIFO/LIFO cost basis strategies, don't cover the GraphQL/MCP tool call mechanics, don't dive into impairment accounting or realized gain/loss recognition post-swap.
- Score: 7/10
