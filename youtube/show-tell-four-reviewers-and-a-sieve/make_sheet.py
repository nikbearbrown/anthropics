#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-four-reviewers-and-a-sieve.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #31 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B16 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-plugins-official/plugins/code-review/ — README.md, commands/code-review.md and
.claude-plugin/plugin.json (the plugin has no agents/ folder: the reviewers are defined inside the command file).
All read in full 2026-09-27 and byte-compared with the raw files on GitHub main (fa59bc90): identical (sources/live_*).
THE TITLE: the card says "Four Reviewers"; that is the README's summary ("Launches 4 parallel agents"). The command file,
which is what Claude executes, says "launch 5 parallel Sonnet agents" and describes five. The film follows the command
file, says the README's four aloud (B16), and is titled "Five Reviewers and a Sieve". The slug keeps the card's name.
The cut is the command's own words: "Filter out any issues with a score less than 80." Nothing is averaged: each issue is
scored once, by its own Haiku agent. The slip scores on screen are illustrations (EXEMPT), drawn from the rubric's scale.
Cast (not the security-review film's PR crate on a belt, not #29's issue board): a kraft TABLE with the pull request (a
stack of white pages) on it, a gate arm at its left, five kraft REVIEWER figures around it, finding SLIPS in a rail, a
vertical confidence RULER (0..100), the SIEVE (a mesh tray on legs) with a BIN under it, and the PR COMMENT card.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Five Reviewers and a Sieve"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Anthropic's official plugin directory has a code review plugin. It adds one command, slash code review, and you run it on a pull request. It uses the GitHub command line tool to read the pull request and to post back to it.",
      "B00_Table", "A kraft table rises on dark legs; a stack of white pages (the pull request) slides onto it ('pull request'); the command label lands ('/code-review'); a grey cable draws from a small dark block to the stack.",
      [{"at": 0.1, "event": "the plugin"}, {"at": 0.4, "event": "one command, run on a pull request"}, {"at": 0.8, "event": "the GitHub command line tool"}]),
 beat("B01", "Step one. A small, fast Haiku agent checks whether the pull request needs a review at all. If it's closed, a draft, automated or obviously simple, or it already has a review from Claude, the command stops right there.",
      "B01_Eligible", "A gate arm drops across the table's front; a small grey checker figure stands by it ('eligible?'); four ghost boxes beside it fill with ink ticks as the four conditions are named; the arm lifts.",
      [{"at": 0.1, "event": "a Haiku agent checks"}, {"at": 0.45, "event": "closed, draft, simple, reviewed"}, {"at": 0.85, "event": "or it stops"}]),
 beat("B02", "Step two. Another Haiku agent lists the project's Claude dot M D files: the one at the root, and any in the folders this pull request touched. It returns their paths, not their contents.",
      "B02_Paths", "A white list card lands below the table ('CLAUDE.md'); three path rows draw in, each with a small page icon; the page icons stay closed.",
      [{"at": 0.1, "event": "another Haiku agent"}, {"at": 0.5, "event": "root, and touched folders"}, {"at": 0.85, "event": "paths, not contents"}]),
 beat("B03", "Step three. A Haiku agent reads the pull request, and returns a short summary of the change.",
      "B03_Summary", "A small white summary card slides out of the page stack and lands on the table beside it ('summary').",
      [{"at": 0.2, "event": "reads the pull request"}, {"at": 0.7, "event": "a short summary"}]),
 beat("B04", "Step four is the review itself. Five Sonnet agents sit down at once, in parallel, and each one reviews the change on its own, from its own angle. Each returns a list of issues, and why it flagged each one.",
      "B04_Five", "Five kraft reviewer figures pop up around the back of the table at once ('five reviewers'); a grey line draws from each to the page stack.",
      [{"at": 0.1, "event": "step four"}, {"at": 0.35, "event": "five agents, in parallel"}, {"at": 0.85, "event": "issues, and why"}]),
 beat("B05", "Reviewer one checks the change against the Claude dot M D rules. The command reminds it that those rules were written for Claude as it writes code, so not every rule applies in a review.",
      "B05_Rules", "Reviewer one's head gets a terracotta dot; a page icon rises beside it ('rules'); a white finding slip flies from it into the rail.",
      [{"at": 0.1, "event": "reviewer one: rules"}, {"at": 0.6, "event": "written for writing code"}, {"at": 0.85, "event": "a finding"}]),
 beat("B06", "Reviewer two reads only the changed lines, and does a shallow scan for obvious bugs. Large bugs only: no small issues, and no nitpicks.",
      "B06_Bugs", "Reviewer two lights; a lens sweeps across the page stack ('bugs'); two finding slips fly into the rail.",
      [{"at": 0.1, "event": "reviewer two: changed lines"}, {"at": 0.5, "event": "obvious bugs"}, {"at": 0.85, "event": "no nitpicks"}]),
 beat("B07", "Reviewer three reads the git blame and history of the code that changed, looking for bugs that only show up in light of that history.",
      "B07_History", "Reviewer three lights; a short grey commit line with dots draws behind it ('git history'); one finding slip flies into the rail.",
      [{"at": 0.1, "event": "reviewer three: git blame"}, {"at": 0.7, "event": "bugs in light of history"}]),
 beat("B08", "Reviewer four reads earlier pull requests that touched the same files, and checks whether the comments left on them also apply here.",
      "B08_OldPRs", "Reviewer four lights; a small stack of older kraft PR cards slides in beside it ('old PRs'); one finding slip flies into the rail.",
      [{"at": 0.1, "event": "reviewer four: earlier pull requests"}, {"at": 0.7, "event": "old comments that apply"}]),
 beat("B09", "Reviewer five reads the code comments in the changed files, and checks that the change follows what those comments say.",
      "B09_Comments", "Reviewer five lights; a speech-bubble shape rises beside it ('code comments'); one finding slip flies into the rail, which now holds six.",
      [{"at": 0.1, "event": "reviewer five: code comments"}, {"at": 0.7, "event": "follows the comments"}]),
 beat("B10", "Step five scores every issue. Each one gets its own Haiku agent, which scores its confidence that the issue is real, from zero to a hundred. For a rules issue, it double-checks that the Claude dot M D really calls it out.",
      "B10_Score", "A small grey scorer disc pops beside each of the six slips at once ('confidence'); an ink score numeral lands next to each slip; a grey thread draws from the CLAUDE.md list card to the rules slip.",
      [{"at": 0.1, "event": "one scorer per issue"}, {"at": 0.5, "event": "zero to a hundred"}, {"at": 0.85, "event": "rules issues double-checked"}]),
 beat("B11", "The command hands every scoring agent the same scale, word for word. Zero: a false positive, or a pre-existing issue. Twenty five: it might be real. Fifty: real, but minor. Seventy five: highly confident, and important. A hundred: absolutely certain.",
      "B11_Scale", "A tall vertical ruler draws to the right of the rail; its five ticks land one at a time with ink numerals 0, 25, 50, 75, 100 as each is spoken; a grey marker climbs the ruler.",
      [{"at": 0.1, "event": "the same scale"}, {"at": 0.3, "event": "0 and 25"}, {"at": 0.6, "event": "50 and 75"}, {"at": 0.9, "event": "100"}]),
 beat("B12", "Step six is the sieve. Any issue scoring under eighty is filtered out. Notice where that line sits: an issue at seventy five, highly confident, still falls through. Only what scores eighty or more stays on the mesh.",
      "B12_Sieve", "A terracotta dot marks 80 on the ruler ('80'); the sieve (a mesh tray on legs) rises with a bin under it; the six slips move onto the mesh; four drop through into the bin, the 75 last; two stay.",
      [{"at": 0.1, "event": "the sieve"}, {"at": 0.3, "event": "under eighty, out"}, {"at": 0.6, "event": "seventy five falls through"}, {"at": 0.9, "event": "eighty and up stay"}]),
 beat("B13", "What scores low? The command lists false positives to drop, including pre-existing issues, nitpicks a senior engineer wouldn't raise, anything a linter, type checker or compiler would catch, and real issues on lines the pull request didn't change.",
      "B13_Noise", "Three more ghost slips drop through the mesh into the bin; three labels land beside the bin, one at a time ('pre-existing', 'nitpicks', 'linter's job').",
      [{"at": 0.1, "event": "what scores low"}, {"at": 0.35, "event": "pre-existing, nitpicks"}, {"at": 0.65, "event": "what a linter catches"}, {"at": 0.9, "event": "unchanged lines"}]),
 beat("B14", "If nothing reaches eighty, the command stops there. If something does, step seven: one more Haiku agent repeats the first check, in case the pull request was closed or reviewed in the meantime.",
      "B14_Recheck", "The two surviving slips sit on the mesh; the gate arm at the table drops again and the checker figure's four boxes re-tick ('still eligible?'); the arm lifts.",
      [{"at": 0.1, "event": "nothing reaches eighty: stop"}, {"at": 0.5, "event": "repeat the first check"}, {"at": 0.85, "event": "closed or reviewed meanwhile"}]),
 beat("B15", "Step eight. It comments on the pull request, using the GitHub command line tool. The comment stays brief, uses no emojis, and cites each issue with a link to the exact lines, using the full commit hash.",
      "B15_Comment", "A white comment card rises above the sieve ('PR comment'); the two surviving slips fly into it as numbered rows 1 and 2; a grey link bar draws under each row; a grey thread runs from the card to the pull request stack.",
      [{"at": 0.1, "event": "step eight: comment"}, {"at": 0.5, "event": "brief, no emojis"}, {"at": 0.85, "event": "a link to the exact lines"}]),
 beat("B16", "One more thing. The plugin's readme describes four reviewers. The command file, which is what Claude actually follows, launches five. That file is also where the eighty lives, and the readme says to change the threshold there.",
      "B16_TwoFiles", "Two white pages stand side by side below the comment ('README', 'command file'); four small figure marks draw on the first, five on the second; a cursor clicks the 80 on the ruler.",
      [{"at": 0.1, "event": "the readme: four"}, {"at": 0.45, "event": "the command file: five"}, {"at": 0.8, "event": "the eighty lives there"}]),
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
    "Hallo. This is Liam, in for Bear. When Claude reviews a pull request, you might ask what it will flag. But Anthropic's code review plugin flags plenty, then throws most of it away. So the real question is: which flags survive?",
    "BrutalistHesitantWriter",
    {"text": "What will Claude flag\nin my pull request?", "triggerWords": "What will Claude flag", "replacementWords": "Which flags survive",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'What will Claude flag in my pull request?'"}, {"at": 0.6, "event": "backspaces 'What will Claude flag' -> 'Which flags survive' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (what will Claude flag in my pull request) and corrects it to the real one (which flags survive).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A pull request: a proposed change to a repository, waiting for review. Claude dot M D: a file of project rules that Claude reads. Git blame: a record of who last changed each line, and in which commit. And a false positive: a flag that looks like a problem, but isn't one.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "pull request", "meaning": "a proposed change, waiting for review"},
               {"term": "CLAUDE.md", "meaning": "a file of project rules Claude reads"},
               {"term": "git blame", "meaning": "who last changed each line, in which commit"},
               {"term": "false positive", "meaning": "a flag that looks like a problem but isn't"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'pull request' lands"}, {"at": 0.3, "event": "'CLAUDE.md' lands"}, {"at": 0.55, "event": "'git blame' lands"}, {"at": 0.8, "event": "'false positive' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Review my branch's changes against main the way the code-review plugin does. Run five separate passes: "
             "CLAUDE.md rules, obvious bugs in the changed lines, git blame and history, comments on earlier pull requests "
             "that touched these files, and code comments in the changed files. Score each issue 0-100 for confidence that "
             "it is real. List every issue with its score, mark which ones survive a cut at 80, and post nothing.")
SPOKEN_PROMPT = ("Review my branch's changes against main the way the code review plugin does. Run five separate passes: "
                 "Claude dot M D rules, obvious bugs in the changed lines, git blame and history, comments on earlier pull requests "
                 "that touched these files, and code comments in the changed files. Score each issue from zero to a hundred for "
                 "confidence that it is real. List every issue with its score, mark which ones survive a cut at eighty, and post nothing.")
CHECKS = ["Check: is each survivor on a line you changed?",
          "Check: read one dropped issue. Was it noise?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In Claude Code, on a branch with changes, paste this. " + SPOKEN_PROMPT +
    " Then check: is every issue that survived on a line you actually changed? And read one issue that fell below eighty. Was it really noise, or did the sieve lose something?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the table with the pull request, its reviewers, the "
                 "rail of finding slips, the ruler, the sieve and bin) on a cream stage per beat, minimal labels, with the "
                 "voice carrying the explanation. The negative space is the style, so only underfill and clustered are "
                 "waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {f"B{n:02d}" for n in range(7, 17)}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): B07-B16 fill 0.58-0.81 throughout, no defects; B00-B06 (0.13-0.47) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE CODE · CODE REVIEW PLUGIN", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers, team leads and students who use Claude Code on GitHub and want to see exactly how the official code-review plugin's /code-review command works: eligibility checks, five parallel reviewers with different angles, a separate 0-100 confidence score for every issue, the cut at 80, and the one linked comment it posts",
    "source_doc": "anthropics/claude-plugins-official/plugins/code-review/ (README.md, commands/code-review.md, .claude-plugin/plugin.json), read in full 2026-09-27 and byte-compared with the raw files on GitHub main (sources/live_*)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["code review", "Claude Code", "code-review plugin", "/code-review", "pull request", "confidence score",
             "false positives", "CLAUDE.md", "git blame", "parallel agents", "Claude plugins", "Claude", "Anthropic",
             "Nik Bear Brown"]},
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
