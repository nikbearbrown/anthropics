# FACTCHECK.md — While You Were Away: Scheduled Tasks

Every named claim checked against `tYOI-WoLS_o.txt` (Anthropic Cowork demo,
beat 4: the scheduling section). ASR quality transcript; proper nouns
verified against transcript context.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B01 | "Cowork can also work on its own, running tasks on a schedule while you focus on something else" | PASS | Transcript: "Cowork can also work on its own, running tasks on a schedule while you focus on something else." | — |
| 2 | B02 | The hourly drive-folder example (check shared drive for added/modified docs; note who changed what; summarize what's new; group by client; save to daily updates folder) | PASS | Transcript's full instruction quoted in beat 4: "Every hour, check the content team's shared drive folder for any documents that were added or modified. For each one, note who made the changes and summarize what's new. Group the changes by client. Save the summary as a doc in my daily updates folder." | Paraphrased for narration; on-screen rows are the five steps. |
| 3 | B03 | Claude drafts the prompt; you review; cadence editable to hourly, daily, weekdays, or manual; accept creates the task | PASS | Transcript: "Claude drafts a prompt for a scheduled task, which you can review. You can make changes, such as updating the cadence to hourly, daily, weekdays, or manual. When everything looks right, you can accept the proposal." | — |
| 4 | B04 | Accept → task pinned to the scheduled page in the left sidebar | PASS | Transcript: "Claude then creates a scheduled task and adds it to the scheduled page in the left sidebar." | — |
| 5 | B05 | Runs automatically while the desktop app is open; each run is its own Cowork session with fresh context; works from the latest state of files and connected tools | PASS | Transcript: "Claude runs it automatically while your desktop app is open. Each run executes as its own Cowork session with fresh contacts, so Claude always works from the latest state of your files and connected tools." | "fresh contacts" is ASR for "fresh context" — corrected in narration. |
| 6 | B06 | Computer must be awake and the desktop app open; a missed run fires as soon as you're back, with a delay notice | PASS | Transcript: "For a scheduled task to run on its cadence, your computer needs to be awake and the Claude desktop app needs to stay open. If your computer was asleep or the app was closed when a task was due, Cowork runs it as soon as you're back and lets you know it was delayed." | — |
| 7 | B07 | Review past runs, edit instructions, change cadence, trigger on demand from the scheduled page | PASS | Transcript: "You can review past runs, edit the instructions, change the cadence, or trigger it on demand from the scheduled page." | — |
| 8 | B08 | Set-up connectors are available to scheduled tasks | PASS | Transcript: "Any connectors you've set up are available for scheduled tasks." | — |
| 9 | B10 | "Schedule the recurring, skip the one-off" — clock work vs steering work | JUDGMENT | The film's rule of thumb, built from the demo's contrast with film 2's live steering. Not stated in the transcript. | Kept; flagged here as the film's framing. |
| 10 | B09 | The morning-digest picture (open the laptop, the digest is waiting) | JUDGMENT | Illustrative scenario of the demo's drive-digest example, not a transcript claim. | Kept; flagged here. |

Strip-the-datable: no prices, no plan names, no version numbers, no "latest"
claims. All capability claims are transcript-sourced and attributed in
SOURCES.md.
