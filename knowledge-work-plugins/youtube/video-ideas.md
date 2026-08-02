# Knowledge Work Plugins Video Ideas

## Candidate 1 — Why YUV→RGB color space conversion can destroy video app performance if done naively

- Source: `partner-built/zoom-plugin/skills/video-sdk/windows/examples/dotnet-winforms/README.md`
- Topic: Pixel-by-pixel rendering performance in low-latency video
- Hook: Your WinForms video app displays smooth video locally, but the Frame rate tanks when you add a simple Bitmap display — the bottleneck isn't the color conversion math, it's the C# marshaling overhead
- Key case: Zoom SDK delivers raw YUV420 video frames to a WinForms app; developer loops through pixels with SetPixel() to render to a PictureBox; frame drops from 60fps to 6fps
- The Question: YUV420 uses 4:1 color subsampling; you need full RGB — why does per-pixel SetPixel make this 100x slower than a direct memory write?
- Core idea: SetPixel() is a marshaled function call for each pixel (lock overhead, type coercion, bounds check). LockBits() acquires a single pointer to the Bitmap's native memory, then raw memcopy writes RGB bytes without per-pixel function calls — quantitative difference: 16ms vs 1600ms per frame
- Visual object: Memory layout diagram showing YUV420 planes (Y full res, U and V quarter-res) expanding to RGB pixel grid; side-by-side timeline comparing SetPixel loop vs LockBits write performance
- Manim move: scan (scan the YUV420 layout showing color plane subsampling and reconstruction), then transform (morph the planes into full RGB output)
- Example seed: 720×480 video frame. Y plane 518,400 bytes, U plane 129,600 bytes, V plane 129,600 bytes (total 777,600). YUV→RGB via ITU-R BT.601: R = (298*(Y−16) + 409*(V−128) + 128) >> 8 (apply to all 345,600 pixels). SetPixel: 1600ms. LockBits + memcopy: 16ms. Illustrative at build time.
- Length band: 2–3 min
- Still lanes: raster (bitmap memory layout, YUV planes), c2v (color space math)
- Prerequisites: RGB vs YUV color model, .NET Bitmap marshaling, video codec basics, frame rate constraints
- Exclusions: Don't explain H.264/H.265 encoding, don't cover ITU-R full color standards (BT.601 only), don't detail WinForms threading (separate issue)
- Score: 8/10

_No other concepts passed the motion-and-question selection bar._

## Candidate 02 — Responding to a webhook after processing it silently doubles every event

- Source: `partner-built/zoom-plugin/skills/rtms/references/quickstart.md`
- Topic: Webhook response ordering and the retry loop it controls
- Hook: Your RTMS session logger records every meeting start — but some sessions appear twice in the database, only in production, only under load.
- Key case: A Node.js handler receives `meeting.rtms_started`, writes to a database, then calls `res.status(200).send()`. The write takes 4 seconds. Zoom's delivery system waited 3 seconds, declared the endpoint unresponsive, and re-delivered. Two WebSocket sessions open to the same meeting; two rows inserted.
- The Question: HTTP 200 and the database write are logically independent — why does their ordering determine whether the event fires once or twice?
- Core idea: Webhook platforms measure round-trip latency from the receiver's perspective. A 200 that arrives late is indistinguishable from a dropped packet. The platform retries with backoff — treating the tardy acknowledgment as silence. Decoupling the response from the processing (respond first, process async) terminates the retry loop before it fires.
- Visual object: Two vertical timelines (Zoom server ↔ handler): left shows processing-first → 3s timeout → retry → second WebSocket; right shows 200-first → async processing → no retry → one WebSocket.
- Manim move: split (two timelines side by side, events accumulate differently on each)
- Example seed: Event arrives t=0. DB write takes 4s. Zoom timeout is 3s. Zoom retries at t=3. Handler responds 200 at t=4. Result: 2 sessions opened, 2 rows written. With `res.status(200).send()` moved to line 1: event arrives t=0, 200 sent at t=0.001, DB write finishes at t=4, Zoom never retries. Illustrative at build time.
- Length band: 2–3 min
- Still lanes: c2v (two-timeline sequence diagram), raster (code diff: before/after reordering)
- Prerequisites: HTTP request/response model, webhook delivery semantics, idempotency concept
- Exclusions: Don't cover HMAC URL validation (separate handshake), don't explain queue-based retry solutions (Kafka, SQS) — the card resolves on ordering alone
- Score: 7/10

## Candidate 03 — Why your C# video callback silently stops arriving after a few minutes

- Source: `partner-built/zoom-plugin/skills/video-sdk/windows/examples/dotnet-winforms/README.md`
- Topic: GC-invisible native pointers and the gcroot pin that saves them
- Hook: Your WinForms video app works perfectly for two minutes, then frames stop — no exception, no log entry, just silence.
- Key case: A managed `VideoPreviewHandler` delegate is passed to the native Zoom SDK callback system. The GC runs a collection cycle. It traces managed roots (stack, statics, GC handles) and finds no reference to the delegate — the only holder is a raw C++ pointer the GC cannot traverse. The delegate is freed. The next native callback writes to released memory and fires nothing.
- The Question: The native SDK is clearly using the delegate object — why does the GC collect it?
- Core idea: The .NET garbage collector traces from managed roots only. A raw `void*` in native memory is invisible to the tracer. `gcroot<T^>` wraps the managed reference in a GC handle stored inside native memory — a handle IS a managed root, so the GC sees it and keeps the object alive exactly as long as the native code needs it.
- Visual object: A bipartite graph: left = managed heap (delegate node, GC root nodes); right = native memory (raw pointer, gcroot handle node). Animate a GC sweep: raw pointer → delegate fades and disappears; add gcroot handle → sweep bounces off.
- Manim move: decay (delegate fades under GC without gcroot), then transform (gcroot handle added, sweep blocked)
- Example seed: `OnFrame` delegate allocated at 0x4A00. Native handler stores raw `void*`. GC runs: no managed root → freed. Next callback reads 0x4A00 → undefined. With `gcroot<ZoomSDKManager^>`: GC handle registered → sweep skips → callback fires, Bitmap received. Illustrative at build time.
- Length band: 2–3 min
- Still lanes: raster (managed heap / native memory layout), c2v (GC root graph, gcroot structure)
- Prerequisites: .NET garbage collection basics, managed vs. native memory model, what a GC root is
- Exclusions: Don't explain C++/CLI syntax depth, don't cover `pin_ptr` or `GCHandle` directly — gcroot is the card's one mechanism; don't extend into Dispose/finalizer cleanup order (separate topic)
- Score: 6/10
