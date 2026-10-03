# PROMPTS — cc-claude-101

Every ask Liam typed at Claude Code (the model heard the JSONL form; the on-screen form is display-condensed where noted in FACTCHECK.md).

## Concrete (B00)

JSONL (verbatim):
> Read notes.md and write actions.md as a checklist of every action item that has a specific person's name attached, one per line as '- [ ] <who>: <what> (<when>)'.

On-screen (condensed):
> Read notes.md; write actions.md — every action item with a named person, one per line as '- [ ] who: what (when)'.

## Vague, no file (B02)

Verbatim (JSONL and on-screen):
> What should I focus on this week?

## Vague, with file (B03)

Verbatim (JSONL and on-screen):
> Read notes.md and tell me if I'm doing a good job managing this project.

## Correction (B04)

JSONL (verbatim):
> Read notes.md and extract every first-person commitment (a sentence where I said I would do something), one per line, to commitments.txt.

On-screen (condensed):
> Read notes.md; extract every first-person commitment, one per line, to commitments.txt.

## YOUR TURN (BHTF)

> I'm going to ask you a vague question in a minute. Before I ask, write down what a right answer would have to look like — a shape I could check with a shell command, or a file that either exists or doesn't. Then I'll ask, and we'll see if my ask matches the answer I said I wanted.
