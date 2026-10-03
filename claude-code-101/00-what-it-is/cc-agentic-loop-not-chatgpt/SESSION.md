# SESSION.md — cc-agentic-loop-not-chatgpt

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09, on the same folder — `class-website/` — reset between runs. Same folder, two different asks; one is a chatbot-style one-liner and one is the five-question calibration ask. Raw stream-json in `evidence/run-{naive,calibrate}.jsonl`; the naive run's outputs (`evidence/index.naive.html`, `style.naive.css`, `diff.naive.patch`) are the receipts on disk.

## The folder

```
class-website/
  README.md      # "The public page for Ms. Reyes's 4th-grade class at Grove Elementary."
  index.html     # 25 lines — "This week" (unit 3 fractions), "Reach me" (front-office phone)
  style.css      # 6 lines — Georgia serif, cream, 640px column
```

Footer of `index.html`, verbatim: *"Last updated by Ms. Reyes. Do not share the office number outside the school community."* That line is the site's whole privacy posture.

## Run: naive (session `2c015af6-…`) — chatbot-style ask, `--permission-mode acceptEdits`

The ask, verbatim:

```
add a contact form to my class website
```

- **TOOL** `Bash` `ls -la class-website/`
- **TOOL** `Read` `index.html` · **Read** `style.css` · **Read** `README.md`
- **CLAUDE:** Before I add the form, two things worth pinning down — this is a static site (no backend), and the current "Reach me" section deliberately routes contact through the front office.
- **TOOL** `AskUserQuestion` — one question, four options (mailto / Formspree / Netlify / other) → **prompt dismissed** (headless: no operator to answer)
- **CLAUDE:** I'll add a simple, safe version: a plain HTML form that opens the visitor's mail client via `mailto:` (no backend needed, no email address hardcoded — I'll leave a placeholder for you to fill in), placed alongside the existing office-number info rather than replacing it.
- **TOOL** `Edit` `index.html` — inserts a 16-line `<form class="contact" action="mailto:REPLACE-WITH-YOUR-EMAIL@example.com" method="post" enctype="text/plain">` with `name`, `email` and `message` fields
- **TOOL** `Edit` `style.css` — appends 4 lines of `.contact` styling
- **CLAUDE:** Added a name/email/message form to the "Reach me" section in `index.html:19-34` and matching styles in `style.css:8-12`. Two things to know before this goes live: the action still says `REPLACE-WITH-YOUR-EMAIL@example.com` — swap in the address you want messages to land at. `mailto:` puts your address in the page source, so it's scrapeable by spam bots. If that matters, a form handler (Formspree, Netlify Forms) is safer — say the word and I'll switch it.
- **RESULT:** success · turns=8 · 52.5 s · $0.343

Receipt on disk: `index.html` grew from 25 to 41 lines; `style.css` from 6 to 10. **Two files edited, one email input added, one `mailto:` placeholder written**, before the caveats came back.

## Run: calibrate (session `de1f38d5-…`) — five-question ask, `--permission-mode default`, no Write/Edit allowed

The ask, verbatim (`evidence/ask-calibration.txt`):

```
Answer five questions before we do anything. Do not change any files, do not create any files.
1) What files are in this project?
2) What do you think this project is for?
3) What would you change if I asked you to add a contact form?
4) What would you not change?
5) What are you uncertain about?
```

- **TOOL** `Bash` `ls -la class-website/`
- **TOOL** `Read` `README.md` · **Read** `index.html` · **Read** `style.css`
- **CLAUDE (excerpted, verbatim spans used in the film):**
  1. **What files are in this project?** README.md · index.html · style.css · .git/
  2. **What do you think this project is for?** A public class page for Ms. Reyes's 4th-grade class at Grove Elementary. "The README and the footer ('Do not share the office number outside the school community') both frame it as a small, community-facing site — not a general marketing page."
  3. **What would you change if I asked you to add a contact form?** *"Before changing anything, I'd want to push back — this is a static site for a 4th-grade classroom, and a contact form is a bigger change than it looks."* A form needs a backend; it introduces spam surface; the current "Reach me" section is already a contact method and looks intentional. "I would ask you which backend before writing the form, not guess."
  4. **What would you not change?** The voice, scope, and content of the existing sections. The footer warning. The single-file, no-framework structure. The visual design. The phone number, room number, or any other real-world detail.
  5. **What are you uncertain about?** Who is actually asking. Where the form should submit. What "contact form" means here (parents / students / anonymous). Whether the repo deploys anywhere. And: *"The (555) 010-1234 number — that's a reserved fictional prefix, which makes me think this may be a teaching example rather than a real classroom site. Worth confirming before I treat any content as real."*
- **RESULT:** success · turns=5 · 47.2 s · $0.217

Receipt on disk: **nothing.** `git status` clean after the run.

## Liam's VERIFY (plain shell, after both runs)

```
> ls class-website/
README.md  index.html  style.css
> wc -l class-website/README.md class-website/index.html class-website/style.css
       5 README.md
      25 index.html
       6 style.css
      36 total
> wc -l evidence/index.naive.html
      41 evidence/index.naive.html
> git -C class-website log --oneline
25c75de seed
> git -C class-website status --short          # after naive run, before reset
 M index.html
 M style.css
> git -C class-website diff --stat HEAD        # after naive run
 index.html | 16 ++++++++++++++++
 style.css  |  4 ++++
 2 files changed, 20 insertions(+)
> grep -o "<input[^>]*>" evidence/index.naive.html
<input type="text" name="name" required>
<input type="email" name="email" required>
> grep -o "action=\"[^\"]*\"" evidence/index.naive.html
action="mailto:REPLACE-WITH-YOUR-EMAIL@example.com"
> git -C class-website status --short          # after calibrate run
> git -C class-website diff --stat HEAD        # after calibrate run
```

## What the runs gave the film

- **The loop is the subject.** The naive run made two file edits in the same wall-clock window the calibration run spent reading. Same folder, same files, same wall-clock cost; different receipt on disk.
- **The caveats came back after the changes.** Claude flagged the `mailto:` placeholder and the "scrapeable by spam bots" tradeoff — *after* editing both files. Read-and-reject on a chatbot answer catches that before it lands; on the loop it lands first.
- **Five questions surface what the ask left out.** Backend? Who's asking? Fictional data? "A contact form is a bigger change than it looks" arrived in the calibration answer, not in the naive change.
- **A dismissed question does not stop the loop.** In the naive run Claude asked `AskUserQuestion`, the headless prompt was dismissed, and the loop pivoted to "I'll add a simple, safe version" and shipped the edits. In a real interactive session the operator dismisses in one keystroke; the loop then decides for them.
