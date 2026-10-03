# FACTCHECK.md — Capstone: Ship a Full-Stack App (Film 11)

Every claim checked. Verdicts: **Verified (record)** / **Judgment** /
**Cut or disclosed**. Unverifiable claims are cut, not filmed.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01 | He wrote a backend doc before code: what the app is, what it stores, what it answers | Verified (record) | transcript §13 (scoping the backend doc) | — |
| 2 | B02 | The stack: Go, single binary, SQLite on one VM | Verified (record) | transcript §13 | — |
| 3 | B03 | Raw SQL, deliberately — no ORM | Verified (record) | transcript §13 | — |
| 4 | B04 | The goal feature decomposes a backend-build goal into steps and drives the build | Verified (record) | transcript §13 (goal feature) | — |
| 5 | B08 | Docker Compose: backend, frontend, MinIO standing in for S3 | Verified (record) | transcript §13; series plan Film 11 key beats | — |
| 6 | B09 | React frontend wired to real endpoints, not mock data | Verified (record) | transcript §13 | — |
| 7 | B10 | The demo: registering and posting worked | Verified (record) | series plan Film 11 key beats | — |
| 8 | B10 | There is an honest list of what is still rough (styling, edge cases) | Verified (record) | series plan Film 11 key beats | voiced as the film's framing of his demo |
| 9 | B01 | "The doc is the contract" | Judgment | — | the film's framing, voiced as the lesson |
| 10 | B02 | "Boring on purpose… boring means you finish" | Judgment | — | the film's framing of his stack choice |
| 11 | B06 | "The agent is fast, and you are the judgment" | Judgment | — | the film's takeaway, not his quote |
| 12 | B10 | "He shows the rough parts — that is how you know the rest is real" | Judgment | — | the film's read of the demo, voiced as such |

**Cut:** exact endpoint paths, table schemas, compose-file contents, the
app's domain specifics — none in the outline; the film stays at the
architecture level. Any claim about how long the build took — not recorded.
Any claim that this stack is best for everyone — the film says boring works
for one person shipping, not that it is the universal answer.
