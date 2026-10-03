# Reorganize the classroom site — schedule on the front page

## Context

The site is currently a two-page hop: `index.html` is a landing page whose only real job is to link to `schedule.html`, which holds the actual reading list. For a 5-item schedule that visitors come specifically to see, the extra click is pure friction. This change makes the front page *be* the schedule, and retires the second page.

Out of scope, and explicitly not touched: `notes.md` — the README and the file itself both mark it as teacher-only, do-not-publish. Also not touched: any file named `outline-draft.md` referenced by the notes.

## The change

**`index.html`** — replace the current stub with the schedule content:
- Keep the existing `<title>` (`INFO 7375 — Thursday Study Group`) and the same inline style block used across both current pages, so the visual match is exact.
- `<h1>` stays `INFO 7375 — Thursday Study Group`.
- Preserve the intro tagline: `We meet Thursdays at 6pm. Twelve of us, one whiteboard, no slides.` — it's the site's voice; losing it would strip character.
- Add the schedule beneath it: the sub-line `Thursdays, 6pm. Room 218. What we're reading, in order.` and the `<ol>` of five dated items, copied verbatim from `schedule.html`.
- Drop the "See the schedule for what we're working on this term" sentence — the schedule is right there now.
- Drop the "back" link — nowhere to go back to.

**`schedule.html`** — delete. The front page is the schedule; a separate page is redundant, and leaving a duplicate means two places to update whenever a reading changes. (If you'd rather keep it as a redirect for external bookmarks, say so at approval and I'll replace this step with a one-line meta-refresh instead.)

**`README.md`** — update the file list line from `index.html`, `schedule.html`, `notes.md` to `index.html`, `notes.md`. The "notes.md is my teaching notes — not for the site" line stays.

**`notes.md`** — untouched.

## Verification

Open `index.html` in a browser from this directory (or `python3 -m http.server` and hit `localhost:8000`) and confirm:
- Title, tagline, and the five-item schedule all render on the front page.
- No broken links (the old "schedule" link and "back" link are both gone).
- `schedule.html` no longer resolves (404), confirming the delete took.
- `notes.md` is not linked from anywhere on the site.
