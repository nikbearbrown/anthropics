# Reorganize the classroom site — schedule on the front page

## Context

The site is currently a two-page hop: `index.html` is a landing page whose only real job is to link to `schedule.html`, which holds the actual reading list. Visitors come specifically to see what's being read, so the extra click is friction. This change puts the five reading items directly on the front page as a summary, while keeping `schedule.html` intact as the canonical schedule page linked from the front.

Out of scope, and explicitly not touched: `notes.md` (teacher-only per the README and its own header), `schedule.html` (stays as-is — the canonical schedule page), and `README.md` (its file list is still accurate).

## The change

**`index.html`** — expand from a stub landing page into a front page that shows the schedule inline:
- Keep the existing `<title>` (`INFO 7375 — Thursday Study Group`) and inline style block, unchanged.
- `<h1>` stays `INFO 7375 — Thursday Study Group`.
- Preserve the intro tagline: `We meet Thursdays at 6pm. Twelve of us, one whiteboard, no slides.`
- Add the five schedule items inline as an `<ol>`, copied verbatim from `schedule.html` so the two views can't drift on wording:
  1. Sep 11 — the loop: read, edit, run, verify
  2. Sep 18 — plan mode: freeze before the byte changes
  3. Sep 25 — three files: CLAUDE.md, DESIGN.md, PROJECT.md
  4. Oct 2  — subagents and separate contexts
  5. Oct 9  — hooks: the harness under the harness
- Replace the current "See the schedule for what we're working on this term" sentence with a link line that sits with the list — something like: `Full details on the <a href="schedule.html">schedule</a> page.` The link to `schedule.html` is preserved (per your instruction), just repositioned so it reads as "see the canonical page" rather than "click through to find out."

**`schedule.html`** — unchanged. It remains the canonical schedule page, including its "back" link to `index.html`.

**`notes.md`** — unchanged.

**`README.md`** — unchanged. Its file list (`index.html`, `schedule.html`, `notes.md`) is still accurate.

## Note on the two copies of the list

The five items now appear in two places (`index.html` and `schedule.html`). When the schedule changes, both need updating. That's a deliberate trade you've chosen — front-page visibility over single-source. I'll flag it in a one-line HTML comment in `index.html` above the `<ol>` so the next editor sees the coupling.

## Verification

Open `index.html` in a browser from this directory (or `python3 -m http.server` and hit `localhost:8000`) and confirm:
- Title, tagline, and the five-item schedule all render on the front page.
- The link to `schedule.html` still works and lands on the canonical schedule page.
- `schedule.html` renders unchanged, including its "back" link to `index.html`.
- `notes.md` is not linked from anywhere on the site.
