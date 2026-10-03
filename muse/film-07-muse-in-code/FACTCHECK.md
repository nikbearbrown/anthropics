# FACTCHECK.md — Muse in Code (Film 7 of 12)

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01 | API keys are generated in the Meta developer console | Verified (record) | transcript §9 | — |
| 2 | B01 | Copy the key once; it won't show again; keep it in env, not code | Verified (record) | standard practice, consistent with the course's treatment | — |
| 3 | B02 | Muse speaks the OpenAI chat-completions dialect; swap the base URL | Verified (record) | transcript §9 | — |
| 4 | B02 | No `/v1` path segment to append; the domain alone is the endpoint | Verified (record) | film brief (Bear's notes) | — |
| 5 | B03 | Raw REST = one HTTP POST; JSON request, JSON answer, no library needed | Verified (record) | transcript §9 | — |
| 6 | B04 | OpenAI SDK: same chat-completions call, only the base URL changes | Verified (record) | transcript §9 | — |
| 7 | B05 | Anthropic SDK: messages array with roles; system role for instructions; explicit max tokens | Verified (record) | transcript §9 | — |
| 8 | B06 | The instructor debugged calls by reading the API's error messages | Verified (record) | transcript §9 | — |
| 9 | B07 | "REST is enough; SDKs add convenience, not capability" | Judgment | instructor's stance; voiced as "honestly" + "in my reading" framing | kept, labeled |
| 10 | B08 | No first-party Meta SDK; that's deliberate | Judgment | transcript §9 shows no first-party SDK; "deliberate" is the instructor's reading | voiced as "in the instructor's reading" |
| 11 | B08 | "The API is the SDK" | Judgment | the film's takeaway line | kept, labeled as takeaway |
| 12 | BHTF | One API call tonight is a reasonable first step | Judgment | pedagogical judgment | kept |

No claims were cut: the film avoids exact endpoint hostnames and specific
model-name strings precisely so nothing unverifiable is asserted. No fresh
primary-source verification was performed; records rest on Bear's course
notes (the film's commissioned source).
