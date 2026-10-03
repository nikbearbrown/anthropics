#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-claude-on-an-issue.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #29 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B09 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-code-action, read RAW from GitHub main on 2026-09-27 (commit 756cc22e,
2026-09-25): README.md, docs/capabilities-and-limitations.md, docs/usage.md, docs/setup.md,
docs/faq.md, docs/security.md, examples/claude.yml, and three src files for the exact comment
wording (sources/live_2026-09-27_*). The local copy (pulled 2026-08-27) matches on README,
capabilities and setup; usage/faq/security differ only in lines the film does not use.
Cast (different from the security-review film's PR crate on a belt): the ISSUE BOARD (a kraft pin
board on a dark stand; white cards pin to it: the issue, the @claude comment, then Claude's tracking
comment with checkboxes), the REPO (a kraft tray of code pages, the workflow page among them), the
SAFE (a dark box holding the key), the GATE (two posts and a bar), the RUNNER (a dark server stack
whose lights come on), the BRANCH (a grey main line with a claude/ line forking off it, commit dots
landing), the PR card and three locked buttons (review, approve, merge), and a dashed fence.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "@claude on an Issue"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "It's set up once, by a repository admin. Install the Claude GitHub app on the repository. Store your Anthropic API key as a repository secret, named Anthropic API key, in capitals. And copy the example workflow file, claude dot Y M L, into your repository's workflows folder. In Claude Code, the install GitHub app command walks you through the app and the secret.",
      "B00_Setup", "A kraft tray of code pages drops in ('repo'); a small dark app block snaps onto its rim ('Claude app'); a key drops into a dark safe beside it ('ANTHROPIC_API_KEY'); a white workflow page slides into the tray ('claude.yml').",
      [{"at": 0.1, "event": "the repo tray"}, {"at": 0.3, "event": "the Claude app plugs in"}, {"at": 0.55, "event": "the key goes into the secret safe"}, {"at": 0.8, "event": "the workflow page lands"}]),
 beat("B01", "Now someone comments on an issue, and the comment contains the trigger phrase: at Claude, by default. It has to be a whole word, so at Claude dash bot won't start it. The trigger phrase setting changes the words, and the workflow can also start on assigning the issue to a chosen user, or on a label.",
      "B01_Mention", "A kraft pin board rises on a dark stand; an issue card pins to it ('issue'); a comment card slides in under it and '@claude' lands beside it; a small avatar disc and a label tag pop up beside the card as the other two triggers.",
      [{"at": 0.1, "event": "the issue board"}, {"at": 0.25, "event": "the @claude comment"}, {"at": 0.5, "event": "whole word only"}, {"at": 0.85, "event": "assignee and label triggers"}]),
 beat("B02", "GitHub sends that new comment to the workflow. The workflow checks that the comment contains the phrase. Then the action checks that the person who wrote it has write access to the repository. Only users with write access can start Claude. Then the gate opens.",
      "B02_Gate", "A copy of the comment card slides from the board to a gate (two posts and a bar) ('claude.yml'); a check lands for the phrase; a badge lights for write access ('write access'); the bar lifts.",
      [{"at": 0.1, "event": "the event travels to the workflow"}, {"at": 0.35, "event": "the phrase is found"}, {"at": 0.65, "event": "write access checked"}, {"at": 0.9, "event": "the gate opens"}]),
 beat("B03", "The job starts on a runner. The read me says where: the action executes entirely on your own GitHub runner, and its calls to Claude go to the provider you chose. The job checks out your repository, and hands Claude the key from the secret.",
      "B03_Runner", "A dark server stack rises past the gate ('runner'); its lights come on one by one; a thin cable draws up to a small block ('API'); a copy of the code pages slides from the repo onto the runner; the key rides from the safe into it.",
      [{"at": 0.1, "event": "the runner"}, {"at": 0.4, "event": "entirely on your runner"}, {"at": 0.6, "event": "only model calls go out"}, {"at": 0.85, "event": "checkout and the key"}]),
 beat("B04", "Its first move is one comment on the issue: Claude Code is working. That's the tracking comment. As Claude works, it updates that same comment with a to-do list, and the boxes tick as each task is done. It doesn't post a second comment. It only acts by updating its first one.",
      "B04_Tracking", "A white card pins under the @claude comment ('tracking'), a terracotta dot spinning on it; three checkbox rows appear; the boxes tick one by one; the card grows, no second card appears.",
      [{"at": 0.1, "event": "one comment appears"}, {"at": 0.4, "event": "a to-do list"}, {"at": 0.6, "event": "boxes tick"}, {"at": 0.85, "event": "one comment only"}]),
 beat("B05", "To do the work, it reads the issue, its comments, and the code. Then it does one of two things. If you asked a question, it answers in the tracking comment. If you asked for a change, it changes the code.",
      "B05_Context", "A lens slides over the issue card, the comments, then the code pages on the runner; a fork draws from the runner: one grey path back to the tracking card ('answer'), one to the right ('change').",
      [{"at": 0.1, "event": "reads the issue and comments"}, {"at": 0.3, "event": "reads the code"}, {"at": 0.6, "event": "a question: answer in the comment"}, {"at": 0.85, "event": "a change: edit the code"}]),
 beat("B06", "Started from an issue, it always creates a new branch for the work, named with the claude slash prefix, which the branch prefix setting can change. Its commits are pushed to that branch, and nowhere else. Started from an open pull request, it pushes to that pull request's branch instead.",
      "B06_Branch", "At the right a grey main line runs with commit dots ('main'); a new line forks up from it ('claude/'); commit dots fly from the runner and land on the new line one by one; a terracotta tip marks its end.",
      [{"at": 0.1, "event": "a new branch forks"}, {"at": 0.35, "event": "the claude/ prefix"}, {"at": 0.6, "event": "commits land on it"}, {"at": 0.85, "event": "open PR: its own branch"}]),
 beat("B07", "It doesn't open the pull request for you. When it's done, the tracking comment links to the branch, and to a pre-filled page for a new pull request: Create PR. You press it. That way your branch protection rules still apply, and you keep final control.",
      "B07_PRLink", "A pill slides out under the tracking card ('Create PR'); the cursor presses it; a kraft PR card rises at the branch tip ('pull request'); a check lands beside the cursor.",
      [{"at": 0.1, "event": "no PR is opened by Claude"}, {"at": 0.4, "event": "the Create PR link"}, {"at": 0.6, "event": "you press it"}, {"at": 0.85, "event": "your rules, your control"}]),
 beat("B08", "The docs also list what it cannot do. It cannot submit formal pull request reviews. For security reasons, it cannot approve pull requests. And it cannot merge branches, rebase, or do other git operations beyond pushing commits. Those stay with you.",
      "B08_Cannot", "Three dark buttons rise under the PR card ('review', 'approve', 'merge'); a padlock snaps onto each as it is named; the cursor hovers them.",
      [{"at": 0.2, "event": "no formal review"}, {"at": 0.45, "event": "no approval"}, {"at": 0.7, "event": "no merge, no rebase"}, {"at": 0.9, "event": "those stay with you"}]),
 beat("B09", "Its reach is small on purpose. It only sees the repository, and the issue or pull request, it was started in. It can't run Bash commands unless the workflow allows them. And the Claude GitHub app has no write access to workflow files, so it can't change its own setup.",
      "B09_Scope", "A dashed fence draws around the board, repo and runner; a small dark terminal block appears on the runner with a padlock ('Bash'); the workflow page lifts from the repo and a padlock lands on it.",
      [{"at": 0.15, "event": "one repo, one issue"}, {"at": 0.5, "event": "no Bash unless allowed"}, {"at": 0.85, "event": "workflow files locked"}]),
]


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


OPEN = [
 remotion("BIDEA", "the question",
    "Namaste. This is Liam, in for Bear. When you type, at Claude, on a GitHub issue, it's easy to ask what Claude will say back, as if it were a chat. But the Claude Code Action runs a whole job for your repository. So the real question is what Claude does when you tag it on an issue.",
    "BrutalistHesitantWriter",
    {"text": "What does Claude say\nwhen I tag it on an issue?", "triggerWords": "Claude say", "replacementWords": "Claude do",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'What does Claude say when I tag it on an issue?'"}, {"at": 0.6, "event": "backspaces 'Claude say' -> 'Claude do' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (what does Claude say when I tag it) and corrects it to the real one (what does Claude do).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A GitHub Action: a step GitHub runs when something happens in your repository. A runner: the machine the job runs on. The trigger phrase: the words in a comment that start the job. By default, it's at Claude. And a branch: a separate line of commits, apart from main.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "GitHub Action", "meaning": "a step GitHub runs when something happens"},
               {"term": "runner", "meaning": "the machine the job runs on"},
               {"term": "trigger phrase", "meaning": "the words that start Claude: @claude"},
               {"term": "branch", "meaning": "a separate line of commits"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'GitHub Action' lands"}, {"at": 0.35, "event": "'runner' lands"}, {"at": 0.6, "event": "'trigger phrase' lands"}, {"at": 0.8, "event": "'branch' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = 'Using gh, open one issue in this repo titled "Fix a typo", then comment on it: @claude fix one typo in README.md'
SPOKEN_PROMPT = ("Using G H, open one issue in this repo titled Fix a typo, then comment on it: "
                 "at Claude, fix one typo in the read me")
CHECKS = ["Check: does one Claude comment tick its boxes?",
          "Check: is there a claude/ branch and a Create PR link?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In one test repository of your own, run the install GitHub app command in Claude Code first. Then paste this: " + SPOKEN_PROMPT + ". "
    "Then check two things. Does one Claude comment appear on the issue? Do its boxes tick? "
    "And is there a new claude slash branch, with a Create PR link?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn issue-board-and-runner scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B03", "B04", "B05", "B06", "B07", "B08", "B09"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.57-0.86 throughout; B00 (0.10-0.15), B01 and B02 (0.53) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": "Att Claude on an Issue. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · GITHUB ACTIONS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Hindi (Namaste)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who use GitHub issues in class or team repos and want to see what actually happens when they tag @claude",
    "source_doc": "anthropics/claude-code-action, read RAW from GitHub main @ 756cc22e on 2026-09-27: README.md, docs/capabilities-and-limitations.md, docs/usage.md, docs/setup.md, docs/faq.md, docs/security.md, examples/claude.yml, src comment/branch files (sources/live_2026-09-27_*); the local copy was diffed",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude Code", "Claude Code Action", "GitHub Actions", "GitHub issues", "@claude", "pull requests",
             "tracking comment", "branches", "CI", "Anthropic", "Nik Bear Brown"]},
    "beats": B}

# keep measured audio fields across re-runs (audio-first: never lose the clock)
old = {}
p = HERE / "beat_sheet.json"
if p.exists():
    for ob in json.load(open(p))["beats"]:
        old[ob["beat_id"]] = ob
for b in B:
    ob = old.get(b["beat_id"])
    if ob and ob.get("narration_text") == b["narration_text"]:
        for k in ("actual_duration_s", "audio_file"):
            if k in ob:
                b[k] = ob[k]
p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(len(B), "beats; est", round(sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in B)), "s")
