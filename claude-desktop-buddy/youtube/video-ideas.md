# claude-desktop-buddy Video Ideas

## Candidate 1 — State machines make invisible state visible
- Source: `README.md` (## The seven states)
- Topic: State-driven animation feedback on constrained displays
- Hook: A desk pet needs to tell you what Claude is doing without text—but the same animation looping forever feels broken.
- Key case: When a permission prompt arrives, the pet shifts to "attention" state (LED blinks constantly), and if you approve in under 5s, it rewards you with "heart" state (floating hearts).
- The Question: Why design seven distinct states instead of showing a running counter of sessions?
- Core idea: State machines map internal triggers (running sessions, pending approvals, token milestones) to external signals (animations, LED behavior). The device learns the mapping once and reuses it for every decision.
- Visual object: Pet animation cycling through frames as state changes
- Manim move: transform
- Example seed: 2 sessions running → busy state (sweating loop). One approves in 3 seconds → heart state (floating hearts appear). Neither running for 5 minutes → back to idle (blinking).
- Length band: 2–3 min
- Still lanes: state diagram (geo), animation frames (raster)
- Prerequisites: state machines, feedback loops
- Exclusions: permission prompt UI design, the specific pet species library
- Score: 9/10

## Candidate 2 — Streaming files over 20-byte pipes without buffering
- Source: `README.md` (## GIF pets), `REFERENCE.md` (## Folder push)
- Topic: Constraint-driven protocol design for tiny-MTU transfers
- Hook: BLE has a 20-byte packet limit. Character packs are 180KB. How do you push large files to a device with 520KB total storage without it running out of RAM?
- Key case: The bufo character pack (184,320 bytes) streams to the device in sequential chunks. Each chunk writes to flash, the device acks with a byte count, and the desktop waits before sending the next chunk.
- The Question: Why does sequential acking prevent the device from buffering the whole file?
- Core idea: Each chunk completes a write-and-ack cycle before the next arrives. Flow control is enforced in the protocol: desktop never sends chunk N+1 until chunk N is acked. No operation holds more than one chunk + line buffer in RAM.
- Visual object: Progress bar accumulating bytes, or table of chunk-by-chunk transfers
- Manim move: accumulate
- Example seed: manifest.json is 412 bytes, arrives in 5 chunks of ~80 bytes. Device writes chunk 1, acks "n=80". Desktop sends chunk 2. Device writes and acks "n=160". Repeat until 412 complete.
- Length band: 2–3 min
- Still lanes: data flow (c2v), chunk sequence (geo)
- Prerequisites: BLE basics, flash storage constraints
- Exclusions: detailed Nordic UART spec, compression algorithms (covered in live workflow)
- Score: 8/10

## Candidate 3 — One-line summaries from multi-session state
- Source: `REFERENCE.md` (## Heartbeat snapshot)
- Topic: Information collapse for tiny displays
- Hook: Claude can have 5 sessions open simultaneously—some running, some waiting on approval, some idle. A 2-inch screen has room for one text line. What gets shown?
- Key case: Desktop sends `"total": 3, "running": 1, "waiting": 1, "msg": "approve: Bash"`. The device displays the message and knows to blink the LED. The three sessions collapse into a single signal.
- The Question: Why prioritize waiting > running > idle instead of cycling through all sessions?
- Core idea: Prioritization is implicit in message generation. Waiting always wins (highest stakes), then running, then idle. The device displays the highest-priority event; lower-priority state is invisible but not lost—it reappears when high-priority clears.
- Visual object: Heartbeat snapshot table, or the single text line on screen
- Manim move: collapse
- Example seed: Open 5 sessions. 3 are generating (running=3). Message: "Generating: 3". User approves a tool. Now running=2, waiting=1 (one more tool pending). Message changes to "approve: Bash". Device LED blinks.
- Length band: ~1 min
- Still lanes: snapshot table (geo), message prioritization diagram (c2v)
- Prerequisites: multi-session systems, display constraints
- Exclusions: permission prompt protocol details, token counting
- Score: 8/10

## Candidate 4 — Pairing that bootstraps encryption without re-typing
- Source: `REFERENCE.md` (## Security and pairing)
- Topic: Out-of-band credential exchange on asymmetric displays
- Hook: Bluetooth is sniffable. Transcript snippets flow over this link. How do you encrypt without asking the user to manually enter a long PIN every time they reconnect?
- Key case: First pairing: device shows a 6-digit passkey on its screen. User types it into Claude on the desktop. Link is now AES-CCM-encrypted and bonded. Next reconnect reuses the stored long-term key automatically—no passkey prompt.
- The Question: Why show the passkey on the device instead of having the desktop generate a random PIN?
- Core idea: DisplayOnly IO capability signals to the OS that the device can only display, not input. The OS then sends the passkey to the device for display and prompts the human to enter it on the other end. Once the pairing is complete, the LTK is stored and future connections skip the ceremony.
- Visual object: 6-digit passkey on the 135×240 screen; timeline showing plain → encrypted transition
- Manim move: transform
- Example seed: Device boots, shows "847263" on screen. User opens Claude, clicks Connect, sees "Enter the code on your device." Enters 847263. Both devices now have the same LTK. Next day, user wakes the device; reconnect is instant and encrypted.
- Length band: 2–3 min
- Still lanes: pairing flow diagram (geo), passkey display (raster), encryption before/after (c2v)
- Prerequisites: BLE security, public-key cryptography basics
- Exclusions: GATT characteristic encryption flags, LTK storage details, OS-specific APIs
- Score: 7/10

## Candidate 5 — Array rotation makes static loops feel alive
- Source: `README.md` (## GIF pets, manifest description), `characters/bufo/README.md`
- Topic: Creating perceived variety from deterministic sequences
- Hook: The same animation looping forever makes a desk pet look stuck. But you can't fit 100 unique clips on a tiny device.
- Key case: Bufo's idle state is an array of 9 GIFs: `["idle_0.gif", "idle_1.gif", ..., "idle_8.gif"]`. Each loop, the device advances the index. A user glancing at the screen multiple times sees different blinks and glances.
- The Question: Why rotate through a carousel instead of designing one "perfect" idle loop?
- Core idea: Cyclic indexing (index = (index + 1) % array.length) requires tiny logic overhead but produces high perceived variety. The device doesn't know or care about animation content; it just increments and wraps. The carousel technique is write-once-use-everywhere: any state with an array gets variety for free.
- Visual object: Carousel of idle-state GIFs; viewer sees it cycle
- Manim move: rotate
- Example seed: Bufo idle: blink_left → blink_right → glance_up → neutral → blink_left (repeat). Viewer checks the device 6 times over an hour and sees 6 different expressions, not the same one.
- Length band: ~1 min
- Still lanes: array rotation diagram (geo), animation preview (raster)
- Prerequisites: animation loops, state machines
- Exclusions: GIF compression (candidate 2), sprite rendering code
- Score: 7/10

## Candidate 06 — Token accumulation predicts when the pet deserves to celebrate
- Source: `README.md` (## The seven states), `REFERENCE.md` (## Heartbeat snapshot)
- Topic: Threshold-triggered reward states from accumulated work counters
- Hook: A pet that celebrates randomly feels broken; one that celebrates when "enough work happened" feels earned—but what counts as work?
- Key case: After 50,000 cumulative output tokens, the pet enters `celebrate` state (confetti, bouncing). A parallel counter, `tokens_today`, resets at local midnight and survives app restarts, giving the pet a daily rhythm independent of the milestone counter.
- The Question: Why count output tokens as the work metric instead of sessions opened or time elapsed?
- Core idea: Output tokens are a direct proxy for Claude's computational effort. Each heartbeat snapshot delivers the running total; the device compares against the last milestone and fires `celebrate` when the gap exceeds 50 K. Sessions can open without generating output; time passes during lunch. Tokens only accumulate when Claude is actually producing.
- Visual object: Filling accumulation bar with a threshold line; bar crosses and the celebrate animation bursts
- Manim move: accumulate
- Example seed: Three sessions produce 12 K, 19 K, and 17 K tokens (total 48 K). A fourth session adds a 3 K-token explanation. Bar crosses 50 K. Celebrate fires for one loop. Milestone counter resets to 0; `tokens_today` continues climbing until midnight resets it independently.
- Length band: ~1 min
- Still lanes: accumulation bar with threshold (geo), token counter increment (c2v)
- Prerequisites: state machines (Candidate 1), counters and threshold comparisons
- Exclusions: token pricing or API cost implications, NVS storage internals, how `tokens_today` persists across restarts
- Score: 7/10
