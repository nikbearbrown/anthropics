# CLAUDE.md — Thursday study group sign-up page

## What this is

`signup.html` — a one-page sign-up form for our Thursday study group.
Twelve people. They already know each other.

## Constraints

- One HTML file. No frameworks. No external scripts or stylesheets.
- No emoji. No exclamation marks in headings.
- No email or password field. No account. No sign-up wall.
- One typeface. One accent colour (#D97757), used once.
- Never use the word "welcome".
- `python3 check.py` must pass before you say the build is done.

## Lessons Learned

### 2026-08-14 — the email wall
The bare run built a full email/password sign-up form. A wall, for twelve
friends. Dangerous middle: Claude read "sign-up page" as the internet's
generic sign-up flow and filled the silence with the average of the web.
Constraint added: no email/password field.

### 2026-08-21 — the server-side Thursday
Second run computed "next Thursday" in Python at request time. Passed the
checker, but the page needed regeneration every week. Dangerous middle:
Claude picked the first correct-looking approach and did not consider the
lifetime of the artefact. Rewrote to `new Date().getDay()` in the browser.
Constraint added: computed dates in the browser only.

### 2026-08-28 — the welcome header
Copy said "Welcome to the study group" — twice, once in the H1 and once in
the meta description. Dangerous middle: Claude filled a title slot with
the most common phrase for that slot. Constraint added: never the word
"welcome". Silence in the header is fine.
