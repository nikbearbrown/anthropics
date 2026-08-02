# claude-tag-plugins Video Ideas

## Candidate 1 — Why your configured plugin won't load

- Source: `claude-tag-troubleshoot/README.md`
- Topic: Plugin loading diagnosis workflow
- Hook: Configured plugin doesn't activate; silent failure, no error message.
- Key case: Datadog plugin added in admin settings, agent claims skill doesn't exist when invoked.
- The Question: A configured plugin should load and expose its skills; why didn't it?
- Core idea: Plugins load through distinct stages (configured → mounted → loaded → available). The `/debug-plugins` command traces which stage failed by inspecting the filesystem, launch command, and startup logs—then prescribes a fix.
- Visual object: Linear pipeline with 4–5 checkpoints (configured, mounted, loaded, available); one checkpoint highlighted red as the failure point.
- Manim move: scan, accumulate, collapse
- Example seed: Plugin configured, mount directory exists, but startup logs show `EACCES: permission denied on plugin.json`. Fix: `chmod 644 ~/.claude/plugins/datadog/plugin.json`.
- Length band: 2–3 min
- Still lanes: c2v, geo (filesystem paths)
- Prerequisites: agent configuration, basic file permissions
- Exclusions: full agent architecture, other admin settings (inheritance, presets), skill-to-query matching
- Score: 8/10

## Candidate 2 — Why credential API calls fail outside the agent runtime

- Source: `README.md` (Authentication section)
- Topic: Credential injection and environment mismatch
- Hook: Your API curl scripts work in the agent but return 401 locally. Code is identical.
- Key case: Datadog query `curl -H "Authorization: Bearer $DD_API_KEY" ...` succeeds in agent, fails locally with `Unauthorized`.
- The Question: Why does the same code succeed in the agent runtime but fail outside it?
- Core idea: The agent runtime has a credential injector that replaces `$DD_API_KEY` and similar variables with real secrets before outbound requests. Local execution has no injector, so the variable remains unset or holds a placeholder, and auth fails.
- Visual object: Single API request flowing through two environments; agent runtime path shows injector transforming `$TOKEN` to real secret; local path shows empty value.
- Manim move: split, transform
- Example seed: Same curl command, same header, but locally the variable is empty string so auth fails; in the agent, the injector fills it.
- Length band: ~1 min
- Still lanes: c2v, raster (request packet inspection)
- Prerequisites: environment variables, HTTP authentication (Bearer tokens)
- Exclusions: credential configuration in runtime, secure storage practices, CI/CD injection
- Score: 7/10

## Candidate 03 — Why `jobs.query` returned no data even though it succeeded

- Source: `bigquery/skills/bigquery-api/references/api.md`
- Topic: BigQuery sync-to-async query crossover
- Hook: You called the synchronous query endpoint and got back `"jobComplete": false` with an empty rows array — but no error.
- Key case: A `jobs.query` call with default `timeoutMs` of 10 s on a 30-second query returns before the query finishes; the response carries `jobComplete: false` and a `jobId`, but zero rows.
- The Question: `jobs.query` should return results; this call did not and reported no error; why?
- Core idea: `jobs.query` is "sync with a deadline." If the query beats the timeout, results arrive inline. If the deadline fires first, the server returns a job handle instead of data. The caller must detect `jobComplete: false` and switch to a polling loop — repeated `jobs.getQueryResults` calls with `pageToken` — until the flag flips.
- Visual object: A race between two countdown timers — query duration and timeout — with a fork at the finish line: one branch delivers rows, the other delivers a job handle.
- Manim move: split, trace
- Example seed: `timeoutMs=5000`, query takes 8 s → response: `{jobComplete: false, jobId: "bq-job-abc"}` → three `getQueryResults` polls at 2 s intervals → third poll: `{jobComplete: true, rows: [...]}`.
- Length band: 2–3 min
- Still lanes: c2v, raster (response JSON comparison between the two branches)
- Prerequisites: REST APIs, JSON responses, the concept of polling
- Exclusions: `jobs.insert` async-first workflow, query job configuration fields (priority, maximumBytesBilled), dryRun mode
- Score: 8/10

## Candidate 04 — Why BigQuery returns `"42"` when you asked for an integer

- Source: `bigquery/skills/bigquery-api/references/api.md`
- Topic: BigQuery wire-format cell encoding
- Hook: Your schema declares INT64, but every value in the response is a string inside `{"v": "42"}`, not a JSON number.
- Key case: `tabledata.list` on a table with a TIMESTAMP column returns `{"v": "1.7234567e9"}` — a float seconds-since-epoch encoded as a string — instead of a date string or numeric.
- The Question: A typed database should return typed JSON values; every value arrived as a string; why?
- Core idea: BigQuery's wire format wraps all scalar values uniformly in `{"v": "..."}` strings; schema is the only source of type truth. Repeated fields nest as `{"v": [{"v": ...}]}` and structs as `{"v": {"f": [...]}}`. A caller that skips schema consultation and reads JSON types directly will silently misparse every numeric and boolean column.
- Visual object: A two-column table mapping schema types to wire JSON: INT64 → `"42"`, BOOL → `"true"`, TIMESTAMP → `"1.7234e9"` — the type column stays the same while the value column transforms into uniform strings.
- Manim move: transform, scan
- Example seed: Schema: `[{name:"count", type:"INT64"}, {name:"active", type:"BOOL"}]`. Raw response: `{"f":[{"v":"7"},{"v":"true"}]}`. Naive parse treats `"7"` as string; schema-aware parse casts to int 7 and bool true.
- Length band: ~1 min
- Still lanes: c2v, raster (JSON diff annotated by schema column)
- Prerequisites: JSON types, basic SQL schemas
- Exclusions: nested RECORD/ARRAY schemas beyond one level, parameterized queries, BIGNUMERIC precision edge cases
- Score: 7/10

## Candidate 05 — Why a batch of 10 Asana requests still hits the rate limit

- Source: `asana/skills/asana-api/references/api.md`
- Topic: Asana batch API and rate-limit accumulation
- Hook: You replaced 10 sequential Asana calls with one `POST /batch` and still received a 429.
- Key case: A batch body with 10 task-read actions fires against an org near its per-minute limit; the entire batch returns 429, the same outcome as making the calls one by one.
- The Question: Batching requests should reduce rate-limit pressure; why did the same 429 threshold trigger?
- Core idea: Asana's batch API reduces HTTP round trips, not request tokens. Each action inside a batch is counted individually against the per-minute rate limiter — a 10-action batch burns 10 tokens, identical to 10 sequential calls. If any action would exceed the limit, the whole batch is rejected with 429.
- Visual object: Two horizontal timelines — sequential calls and a single batch call — each showing 10 identical tick marks accumulating on the same rate-limit counter.
- Manim move: accumulate, duplicate
- Example seed: Rate limit: 100 req/min. Prior calls: 95. Batch of 10 arrives → counter tries to reach 105 → 429, all 10 actions fail. Split into two batches of 5 separated by a wait → first batch succeeds (100), counter resets, second batch succeeds.
- Length band: ~1 min
- Still lanes: c2v, raster (rate-limit counter visualization)
- Prerequisites: HTTP rate limiting, REST APIs
- Exclusions: Asana's separate concurrent-request limiter, webhook delivery, pagination patterns
- Score: 7/10

## Candidate 06 — Why `jobs.get` returns 404 for a job that definitely exists

- Source: `bigquery/skills/bigquery-api/references/api.md`
- Topic: BigQuery job location pinning and misleading 404
- Hook: You submitted a BigQuery job, received the job ID in the response, then fetched it by that ID — and got 404 Not Found.
- Key case: Job created with `location: "EU"` in the configuration; subsequent `GET /projects/p/jobs/job123` (no `?location=EU` param) routes to the US endpoint, which has no record of the job — returning `404 notFound` even though the job ran successfully in EU.
- The Question: The job was confirmed created and its ID was returned; why does fetching it by ID return 404?
- Core idea: BigQuery shards jobs by region. Every post-creation call — `jobs.get`, `jobs.cancel`, `jobs.getQueryResults` — must pass the same `?location=` as the job's origin. A missing or wrong location silently routes the request to a different regional endpoint where the job does not exist, producing a misleading 404 rather than a location-mismatch error.
- Visual object: A world map split into US and EU zones; a job icon stamped with "EU" sitting in the EU zone; a lookup arrow hitting the US zone endpoint and bouncing back with a 404 while the job sits untouched in EU.
- Manim move: split, trace
- Example seed: Create job → server confirms `location: "EU"`. `GET .../jobs/abc` → 404. Add `?location=EU` → 200, `status.state: "DONE"`. The job existed the whole time; only the routing was wrong.
- Length band: ~1 min
- Still lanes: geo, c2v
- Prerequisites: REST APIs, geographic regions, HTTP 404 semantics
- Exclusions: multi-region dataset configuration, data residency compliance rules, choosing a location at query time
- Score: 7/10
