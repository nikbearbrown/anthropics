# Tailscale Connection Hint Video Ideas

## Candidate 1 — Parallel probes expose which component actually failed
- Source: `hint.js`
- Topic: Multi-point health check diagnostics
- Hook: One graph dropping flat doesn't necessarily mean your connection died—how do you tell what actually broke?
- Key case: Your service crashes and returns 500 errors, but the infrastructure health probe keeps responding. The graphs show completely different patterns.
- The Question: A single failed health check should indicate system failure; here, one probe failed while the other succeeded; why doesn't one failed probe predict complete failure?
- Core idea: Parallel polling of both the target service and infrastructure creates independent signal streams; divergence between streams reveals which component actually failed
- Visual object: Two line graphs overlaid side-by-side, moving in lockstep when healthy, splitting into divergent patterns when one fails
- Manim move: split (one request splits into two parallel probes), compare (two graphs' trajectories diverge)
- Example seed: You reach out to `api.local`; it times out with 500s. Meanwhile `kcprr.internal.local` ping succeeds every poll. First graph flatlines, second graph stays active. Interpretation: "Tailscale up, service down."
- Length band: 2–3 min
- Still lanes: c2v, raster with timelines
- Prerequisites: HTTP health checks, TCP/HTTP basics, Tailscale concepts
- Exclusions: DNS internals, kcprr implementation, probe interval tuning
- Score: 9/10

## Candidate 2 — Polling loop detects recovery without human intervention
- Source: `hint.js`
- Topic: Autonomous recovery via background polling
- Hook: An error page is supposed to wait for user action—but this one auto-advances when your connection returns. How does it know?
- Key case: You're staring at the hint page, you reconnect Tailscale 30 seconds later, and without you clicking anything, the page automatically navigates back to your original destination.
- The Question: A client error page should require user action to retry; in this case, autonomous action occurred without any user input; what mechanism enabled the page to act on its own?
- Core idea: Background polling loop continuously retries the original request; when response status transitions from failure to success, logic triggers automatic navigation
- Visual object: A pulsing spinner or heartbeat indicator representing the background polling, morphing to a "redirecting..." state when success occurs
- Manim move: accumulate (polls accumulate over time), morph (spinner indicator transforms to redirect state)
- Example seed: You hit `http://dashboard.local`. DNS fails. Hint page loads with pulsing "checking..." indicator polling every 2 seconds. After 45 seconds you reconnect Tailscale in the system tray. Next poll gets 200. Spinner morphs to "taking you back..." and page navigates. Zero manual retry clicks.
- Length band: 2–3 min
- Still lanes: c2v, geo with polling timeline
- Prerequisites: HTTP status codes, JavaScript timers, polling patterns
- Exclusions: Exponential backoff strategies, connection timeout tuning, race conditions between polling and navigation
- Score: 8/10

## Candidate 03 — A browser error page you never asked for can be silently replaced
- Source: `background.js`
- Topic: Browser extension event interception before error-page render
- Hook: Chrome's DNS failure page looks like the browser's final verdict—but an extension can intercept that verdict before it's ever delivered to the user.
- Key case: A developer navigates to `http://dashboard.corp.local`. DNS returns NXDOMAIN. Chrome would normally commit its own "DNS_PROBE_FINISHED_NXDOMAIN" page—instead, the tab is already showing a custom diagnostics page within milliseconds.
- The Question: A navigation error should terminate at Chrome's built-in error page; in this case the tab shows something else entirely; what gave the extension the authority to substitute it?
- Core idea: `webNavigation.onErrorOccurred` fires before the browser commits the error page to the tab; the service worker filters by `.local` hostname and calls `chrome.tabs.update()` to redirect the tab to a custom URL, racing ahead of the native error render
- Visual object: A horizontal navigation-lifecycle timeline with a marked interception point sitting just before the "error page committed" stage
- Manim move: trace (follow the navigation event through the browser pipeline, highlight where the hook fires), transform (error-page node morphs into hint-page node at the interception point)
- Example seed: `http://payroll.corp.local` starts navigating. DNS → NXDOMAIN. Chrome fires `onErrorOccurred`. Service worker receives event, checks `hostname.endsWith(".local")`, calls `tabs.update(tabId, {url: "tailscale-hint.html?target=http://payroll.corp.local"})`. Hint page renders. Chrome's own error page never appears. Elapsed time: ~5 ms after DNS failure.
- Length band: 2–3 min
- Still lanes: c2v, raster with browser-architecture diagram
- Prerequisites: DNS basics, Chrome extension architecture, browser navigation lifecycle
- Exclusions: Manifest V3 service worker lifecycle, `<all_urls>` permission trade-offs, hint-page polling and auto-redirect behavior (covered in Candidates 1 & 2)
- Score: 8/10
