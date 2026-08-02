# HTTP Core Video Ideas

## Candidate 1 — Connection pooling makes subsequent requests 5× faster
- Source: `docs/connection-pools.md`
- Topic: Connection reuse feedback loop
- Hook: The same example.com request takes 0.529s first, then consistently 0.095s after—why the cliff?
- Key case: Making five sequential GET requests to www.example.com in a loop shows the performance drop-off and plateau.
- The Question: Why should request latency decrease to 1/5 after the first attempt?
- Core idea: TCP connection handshake (three-way) happens once per host; subsequent requests reuse the open socket.
- Visual object: Bar chart of five request durations, with the sharp cliff drop after the first.
- Manim move: morph
- Example seed: `httpcore.ConnectionPool()` with five `http.request("GET", "https://www.example.com/")` calls timed.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: TCP, socket
- Exclusions: SSL/TLS handshake details, internal pool queueing
- Score: 9/10

## Candidate 2 — HTTP/2 collapses ten connections down to one
- Source: `docs/http2.md`
- Topic: Multiplexing efficiency
- Hook: Twenty concurrent requests to Wikipedia spawn eight separate connections with HTTP/1.1 but fit into one with HTTP/2—how?
- Key case: The exact log output showing `<HTTPConnection ... HTTP/1.1 ...>` eight times, then a single `<HTTPConnection ... HTTP/2 ... Request Count: 20>`.
- The Question: Why can one connection carry the load of eight under a new protocol?
- Core idea: HTTP/2 binary framing and stream multiplexing allow multiple logical streams on a single TCP connection; HTTP/1.1 requires one connection per concurrent request.
- Visual object: Two side-by-side diagrams—eight labeled connection boxes vs. one box with 20 streams inside.
- Manim move: collapse
- Example seed: `ThreadPoolExecutor` submitting 20 requests to `https://en.wikipedia.org/wiki/{year}` for years 2000–2020; measure `http.connections` count.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: HTTP/1.1 concurrency model
- Exclusions: ALPN negotiation, server push, stream prioritization
- Score: 8/10

## Candidate 3 — Timeout stages place emergency exits at different request checkpoints
- Source: `docs/extensions.md`
- Topic: Request lifecycle emergency exits
- Hook: The same request can fail in four different ways—pool starvation, connect hang, read hang, write hang—each needing a different timeout value.
- Key case: Set `extensions={"timeout": {"connect": 5.0, "pool": 10.0}}` and observe that pool blocking triggers at 10s but a stuck handshake triggers at 5s.
- The Question: Why should a connection-pool timeout differ from a network-connect timeout?
- Core idea: Four timeout types (pool, connect, read, write) apply at different pipeline stages; configure each to handle distinct bottlenecks independently.
- Visual object: Timeline showing a request's path through pool-wait → connect → write → read, with timeout cutoffs at each stage.
- Manim move: split
- Example seed: `extensions={"timeout": {"pool": 10.0, "connect": 5.0, "read": 10.0, "write": 5.0}}` applied to a request stalling at connect.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Request/response cycle
- Exclusions: Retry logic, exponential backoff, circuit breakers
- Score: 8/10

## Candidate 4 — Streaming response bodies keep memory constant, not proportional to file size
- Source: `docs/quickstart.md`
- Topic: Unbounded response handling
- Hook: A 100MB response read into memory as `response.content` explodes RAM usage; `iter_stream()` holds only the current chunk.
- Key case: Download a large binary file chunk by chunk: `for chunk in response.iter_stream(): output_file.write(chunk)`.
- The Question: How do you receive a 100MB response without loading 100MB into RAM?
- Core idea: `iter_stream()` returns an iterator yielding chunks; process and discard each chunk rather than buffering the whole response.
- Visual object: Memory usage graph—flat line with streaming, sharp spike with buffered read.
- Manim move: slosh
- Example seed: `with httpcore.stream('GET', 'https://example.com/100mb.bin') as response:` then iterate and write chunks.
- Length band: ~1 min
- Still lanes: c2v with memory raster
- Prerequisites: Iterators
- Exclusions: Backpressure, TCP window sizing, chunked encoding details
- Score: 6/10

## Candidate 05 — The same 12 bytes produce two completely different wire formats depending on how you hand them over
- Source: `docs/quickstart.md`
- Topic: HTTP body framing: Content-Length vs. chunked encoding
- Hook: Passing `b'Hello, world'` as bytes sends `Content-Length: 12`; passing the same text via a file object sends `Transfer-Encoding: chunked`—identical payload, incompatible wire formats.
- Key case: `content=b'Hello, world'` → server echoes `'Content-Length': '12'`; `content=open("hello-world.txt", "rb")` → server echoes `'Transfer-Encoding': 'chunked'` with the same body.
- The Question: Why would two representations of identical bytes require the receiver to use a completely different framing protocol?
- Core idea: HTTP receivers must know when the body ends; bytes have a pre-known length so a single header suffices; iterables may not—chunked encoding prefixes each chunk with its hex length and uses a `0\r\n\r\n` sentinel to signal termination at send time.
- Visual object: Two wire-format strips side by side—`Content-Length: 12\r\n\r\nHello, world` vs. `b\r\nHello, world\r\n0\r\n\r\n`—with the terminator highlighted.
- Manim move: transform
- Example seed: `httpcore.request('POST', 'https://httpbin.org/post', content=b'Hello, world')` shows `Content-Length: 12`; repeat with `content=open('hello-world.txt','rb')` to show `Transfer-Encoding: chunked`; label illustrative at build time.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: HTTP headers, bytes vs. iterators
- Exclusions: HTTP/2 DATA frames (which replace chunked entirely), gzip content-encoding, multipart bodies
- Score: 9/10

## Candidate 06 — HTTP hands the raw socket to the caller the moment a server replies 101
- Source: `docs/extensions.md`
- Topic: Protocol escape hatch via HTTP Upgrade
- Hook: An ordinary HTTP GET request can permanently surrender its TCP connection to WebSocket—after status 101, all HTTP machinery steps aside and you write raw frames directly to the socket.
- Key case: `if response.status != 101: raise Exception("Failed to upgrade")` — then `network_steam.write(ws_connection.send(message))` sends WebSocket frames through `response.extensions["network_stream"]`, bypassing every HTTP abstraction.
- The Question: How does a strict request/response protocol hand control to a bidirectional streaming protocol without closing or replacing the connection?
- Core idea: The `Upgrade` header signals a protocol switch; server 101 confirms it; httpcore exposes `response.extensions["network_stream"]` giving direct socket read/write — the HTTP state machine terminates at that point and the caller owns the byte stream.
- Visual object: State-machine strip: `[HTTP Request] → [101 Response] → [escape hatch] → [Raw Socket] → [WebSocket Frames]`, with the HTTP box going grey after the hatch opens.
- Manim move: morph
- Example seed: `headers = {b"Upgrade": b"WebSocket", b"Connection": b"Upgrade", b"Sec-WebSocket-Key": base64.b64encode(os.urandom(16)), b"Sec-WebSocket-Version": b"13"}; with httpcore.stream("GET", url, headers=headers) as r: ws = r.extensions["network_stream"]; ws.write(wsproto_frame)`; label illustrative at build time.
- Length band: 3–5 min
- Still lanes: c2v
- Prerequisites: TCP, HTTP request/response cycle
- Exclusions: WebSocket SHA-1 key verification handshake details, CONNECT tunneling (separate use case of the same primitive), TLS re-negotiation after upgrade
- Score: 9/10
