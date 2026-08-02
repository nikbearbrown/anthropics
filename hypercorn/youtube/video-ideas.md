# Hypercorn Video Ideas

## Candidate 1 — Backpressure prevents memory exhaustion by blocking the application layer

- Source: `docs/discussion/backpressure.rst`
- Topic: Backpressure and blocking propagation in async I/O
- Hook: When a client reads slowly, how does the server avoid buffering the entire response in memory?
- Key case: Video streaming where the client's network is slow and its buffer fills; server keeps generating response data at 100 MB/s but client reads at 10 MB/s.
- The Question: Without any explicit memory limits, why doesn't the server accumulate 1 GB of unsent response data?
- Core idea: Backpressure propagates backward through the async stack. When the TCP send buffer fills (because the client reads slowly), the `await send()` call blocks the application coroutine. The coroutine stops generating new data, so memory stays bounded. The server yields, not the client.
- Visual object: A pipe network with a narrowing bottleneck that forces upstream flow to slow and then halt.
- Manim move: accumulate
- Example seed: Server generates 100 MB/s response; client reads 10 MB/s. Without backpressure, 1 GB fills in 10 seconds. With backpressure, `await send()` blocks after 50 MB buffers, halting generation. Memory stays bounded at ~50 MB.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: async/await, socket send buffers, event loop behavior
- Exclusions: Network protocol details, socket buffer sizes, h11/h2 library internals
- Score: 7/10

## Candidate 2 — Rapid reset mitigation forces connection recycling cost onto the attacker

- Source: `docs/discussion/dos_mitigations.rst`
- Topic: Attack cost distribution through connection limits
- Hook: How does the server ensure that rapid stream opening/closing attacks cost the attacker as much as the server?
- Key case: Attacker opens 1000 HTTP/2 streams and closes them rapidly to exhaust server resources. Server is configured with `keep_alive_max_requests = 100`.
- The Question: Why does limiting requests per connection prevent resource exhaustion even when streams are recycled?
- Core idea: Creating a connection incurs fixed cost (TCP setup, TLS handshake). If the server limits to 100 requests per connection and then closes, the attacker must pay the connection-setup cost repeatedly. Over time, attacker and server both pay N handshakes for N connections. Cost becomes symmetric.
- Visual object: A request counter that increments toward a limit, resets to zero, and increments a connection counter.
- Manim move: accumulate
- Example seed: Attacker sends 100 requests, server closes connection (limit hit). Attacker must open a new connection and pay another TLS handshake. Over 10 connections, attacker pays 10 handshakes; server pays 10 handshakes. Cost is symmetric.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: HTTP keep-alive semantics, connection setup costs, HTTP/2 stream lifecycle
- Exclusions: Other DoS attacks (slow loris, flood attacks), NGINX configurations, TLS handshake cryptography details
- Score: 7/10

## Candidate 3 — Event sequencing branches on cancellation and drops buffered messages

- Source: `docs/discussion/flow.rst`
- Topic: Protocol state machine branching on cancellation signals
- Hook: When a client closes the connection mid-request, why does the server stop sending buffered events instead of delivering them?
- Key case: Server has accepted `http.request[more_body=True]` and has a buffered `http.request[more_body=False]` event ready to send to the application. TCP connection closes. The buffered body event is dropped and only `http.disconnect` is sent.
- The Question: Why doesn't the protocol deliver buffered events before shutdown instead of discarding them?
- Core idea: The state machine checks for closure (TCP Closed event) eagerly and immediately sends `StreamClosed`, halting event production. Buffering completed events would delay closure detection and waste memory on unreachable data. Eager checking is more efficient and responsive.
- Visual object: A sequence diagram that branches at the closure point—one path shows normal body events, the other skips them and jumps to disconnect.
- Manim move: split
- Example seed: Normal flow: Request → Body(more=True) → Body(more=False) → Disconnect. Cancel flow: Request → Body(more=True) → [TCPServer Closed] → Disconnect (Body more=False is never generated).
- Length band: 2–3 min
- Still lanes: geo
- Prerequisites: ASGI message flow, HTTP request streaming, protocol state machines
- Exclusions: h11/h2 library internals, TCP-level socket closure mechanics, ASGI 2 vs ASGI 3 differences
- Score: 7/10

## Candidate 04 — A "closed" connection still delivers the response because TCP has two independent pipes

- Source: `docs/discussion/closing.rst`
- Topic: TCP half-close and one-directional EOF in HTTP
- Hook: The client signals it is done sending — why does the server keep writing data back through what just "closed"?
- Key case: A 50 MB file upload completes; the client sends the final empty byte string (`b""`) signaling end-of-body. The server has not yet computed its response. The server still delivers a full `200 OK` with a response body over the same connection.
- The Question: EOF should mean the connection is done; the client sent EOF; so why is data still flowing in the other direction?
- Core idea: A TCP connection is two independent byte streams, one per direction. Sending EOF closes only the client→server stream. The server→client stream remains open and writable. Hypercorn reads the EOF, stops waiting for further request data, then continues writing the response — following HTTPWG guidance that half-close must not abort the response direction.
- Visual object: A bidirectional pipe split into two one-way arrows: the left arrow grays out and stops on EOF; the right arrow stays lit and carries the response.
- Manim move: split
- Example seed: Client sends 50 MB upload, final chunk = `b""`. Server receives EOF, marks request body complete, begins processing. Server writes `200 OK` + 1 KB JSON body. Client receives response. Server then sends its own EOF. Full close happens only when both directions have sent EOF.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: TCP sockets as bidirectional byte streams, HTTP/1.1 request/response lifecycle
- Exclusions: HTTP/2 stream half-close (DATA frame with END_STREAM flag), TLS shutdown alert sequence, RST_STREAM behavior

- Score: 8/10
