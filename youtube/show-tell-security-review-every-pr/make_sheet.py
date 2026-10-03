#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-security-review-every-pr.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #8 in show-tell-ideas.md (the last in the batch).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-code-security-review/ (README.md in full; action.yml; claudecode/prompts.py,
findings_filter.py, github_action_audit.py, constants.py; scripts/comment-pr-findings.js;
.claude/commands/security-review.md; docs/ both files).
Cast (the conveyor language of show-tell-five-ways-to-wire-an-agent and show-tell-claude-plugin-portal):
a pale BELT with a dashed centre line; the pull request as a kraft CRATE with terracotta tape; the repo's
files as PAGES (grey = unchanged, white with a terracotta dot = changed); Claude as a dark SCANNER ARCH
over the belt (a dark station, as in five-ways) with a light and a terracotta scan line; FINDINGS as white
flags on dark-kraft poles; the FILTER as a kraft-framed mesh screen with a grey bin; the PR PAGE as a white
panel with a dark title bar and code lines; the MERGE GATE as an ink arch with a bar; the reviewer as a
cursor; the terminal as a dark card; an outside crate (grey) with a tucked note; an approval barrier.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "A Security Review on Every Pull Request"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's a pull request: a crate on a belt, on its way to being merged. The security review is a GitHub Action, a job GitHub runs when a pull request opens. It puts Claude over the belt, as a security reviewer.",
      "B00_Belt", "A pale belt draws in; a taped kraft crate slides onto it ('pull request') and rides toward the far end; a dark scanner arch drops over the belt ('Claude'), and its light turns terracotta.",
      [{"at": 0.1, "event": "the belt"}, {"at": 0.25, "event": "the crate: a pull request"}, {"at": 0.55, "event": "a GitHub Action: the arch arrives"}, {"at": 0.85, "event": "Claude's light comes on"}]),
 beat("B01", "Open the crate. Most of the repo stays behind. Only the changed files go under review. Claude can read the rest for context, but it's told to report only what this pull request adds, not old problems.",
      "B01_Diff", "Close-up: the crate's lid flips off; a grid of file pages rises out ('repo'), most grey, three white with a terracotta dot; the grey ones sink back; the three changed pages slide onto the belt ('diff'); a dashed grey line glances back at the crate (context) and fades; an ink check lands by the three.",
      [{"at": 0.1, "event": "the crate opens"}, {"at": 0.3, "event": "the repo's files rise"}, {"at": 0.5, "event": "only the changed files go on"}, {"at": 0.75, "event": "context, but report only what's new"}]),
 beat("B02", "The changed files pass under the scanner. Claude reads them for meaning, not just patterns, looking for things like injection, broken authentication, exposed secrets and weak crypto. Each suspect becomes a finding: the line, how serious, how it could be exploited, and a fix.",
      "B02_Scan", "The three pages ride under the dark arch; a terracotta scan line sweeps each; white finding flags pop up on dark-kraft poles above two of them ('finding'); one flag opens into a finding card (a dark title bar and four grey lines: line, severity, exploit, fix).",
      [{"at": 0.12, "event": "pages ride under the arch"}, {"at": 0.35, "event": "the scan line sweeps"}, {"at": 0.6, "event": "findings flag up"}, {"at": 0.85, "event": "a finding card: line, severity, exploit, fix"}]),
 beat("B03", "Before anything is posted, a filter catches likely false positives. Hard rules drop low-impact kinds, like denial of service and rate limits. Then Claude re-checks each finding, and drops the ones it isn't confident in.",
      "B03_Filter", "Four finding flags ride toward a kraft-framed mesh screen ('filter'); the first flag hits the mesh and drops into a grey bin below; a second is checked by the arch's light and also drops ('dropped'); two pass through.",
      [{"at": 0.12, "event": "the filter screen"}, {"at": 0.4, "event": "hard rules drop one"}, {"at": 0.7, "event": "Claude's re-check drops another"}, {"at": 0.9, "event": "two pass"}]),
 beat("B04", "What's left lands on the pull request as review comments, pinned to the exact lines, each with a thumbs up and a thumbs down. The prompt puts it plainly: better to miss a theoretical issue than flood you with false positives.",
      "B04_Comment", "Close-up: the pull request's page (white panel, dark title bar, grey code lines) ('pull request'); two flags fly in and pin to two lines as comment cards ('comments'); an up and a down reaction pill appear under each; a faint crowd of ghost flags gathers at the edge and fades away.",
      [{"at": 0.12, "event": "the pull request's page"}, {"at": 0.35, "event": "comments pin to lines"}, {"at": 0.55, "event": "thumbs up / down"}, {"at": 0.85, "event": "no flood"}]),
 beat("B05", "Then a person decides. The action posts a comment review. It doesn't approve the pull request, and it doesn't merge it. You read each comment, fix what's real, and dismiss what isn't.",
      "B05_Human", "Wide: the crate, carrying two comment flags, waits at an ink merge gate with its bar down ('merge'); a dashed grey line from the arch's light reaches toward the gate and stops short; a cursor arrives ('you'); one flag turns into an ink check (fixed), the other fades (dismissed); the cursor lifts the bar, it turns terracotta, and the crate rides through.",
      [{"at": 0.12, "event": "the gate is closed"}, {"at": 0.35, "event": "Claude can't open it"}, {"at": 0.6, "event": "you read, fix, dismiss"}, {"at": 0.9, "event": "you merge"}]),
 beat("B06", "You can also run the same review yourself. Claude Code ships a slash command, slash security review, that reviews the pending changes on your branch. Copy it into your project, and you can tune it.",
      "B06_Local", "A dark terminal card on a kraft desk slab; a prompt chevron and a caret; '/security-review' types beside it; a small scanner arch rises over a small crate on the desk, a scan line sweeps, and a flag pops; a white page ('security-review.md') copies out of the terminal into a project folder and gains a line.",
      [{"at": 0.12, "event": "your own desk"}, {"at": 0.35, "event": "/security-review"}, {"at": 0.6, "event": "the pending changes are reviewed"}, {"at": 0.85, "event": "copy it and tune it"}]),
 beat("B07", "One caution, in the repo's own words: the action is not hardened against prompt injection. A pull request could carry text written to steer the reviewer. So run it only on trusted pull requests, and have a maintainer approve outside contributors before their workflows run.",
      "B07_Trust", "Wide: a grey crate from outside arrives on the belt ('outside') with a white note tucked in its top; a dashed grey line curls from the note toward the arch's light; an ink barrier drops across the belt before the arch ('approval'); a cursor pulls the note out; a check lands on the barrier, the bar lifts and the crate rides on.",
      [{"at": 0.12, "event": "not hardened against prompt injection"}, {"at": 0.35, "event": "a note that steers"}, {"at": 0.6, "event": "trusted pull requests only"}, {"at": 0.85, "event": "a maintainer approves first"}]),
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
    "Guten Tag. This is Liam, in for Bear. Anthropic's claude code security review won't catch every security bug. It reads one pull request at a time, and only what changed. So the real question is the risks this change adds.",
    "BrutalistHesitantWriter",
    {"text": "Will Claude catch\nevery security bug?", "triggerWords": "every security bug", "replacementWords": "the risks this change adds",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'Will Claude catch every security bug?'"}, {"at": 0.6, "event": "backspaces 'every security bug' -> 'the risks this change adds' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (catch every security bug) and corrects it to the real one (the risks this change adds).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A pull request: a proposed change, waiting for review before it's merged. The diff: just the lines a change adds or removes. And a false positive: a flagged problem that isn't real.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "pull request", "meaning": "a proposed change, waiting for review before it's merged"},
               {"term": "diff", "meaning": "just the lines a change adds or removes"},
               {"term": "false positive", "meaning": "a flagged problem that isn't real"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.12, "event": "'pull request' lands"}, {"at": 0.45, "event": "'diff' lands"}, {"at": 0.72, "event": "'false positive' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Add anthropics/claude-code-security-review to this repo as a GitHub Action. Trigger it on pull requests only, "
             "read the API key from a repository secret, and exclude our vendored and generated folders. It must never run "
             "on untrusted pull requests, so tell me how to require approval for outside contributors. I'll treat its "
             "comments as leads to check, not verdicts.")
SPOKEN_PROMPT = YT_PROMPT.replace("anthropics/claude-code-security-review", "Anthropic's claude code security review")
# "API" stays as written: Kokoro's lexicon says it right (eɪpiːaɪ); spelled "A P I" it reduces the A to a schwa.
CHECKS = ["Check: the workflow. Pull requests only, key in a secret?",
          "Check: repo settings. Outside contributors need approval?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code: " + SPOKEN_PROMPT + " Then check two things yourself. Does the workflow run on "
    "pull requests only, with the key in a secret? And in your repo settings, do outside contributors need approval?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Review Every Pull Request", "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn conveyor scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = set()   # beats measured to fill >= 55% without the waiver (set after the first Gate V pass)
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · SECURITY REVIEW", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Guten Tag)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers and maintainers who want an automated security pass on every pull request without mistaking it for a guarantee",
    "source_doc": "anthropics/claude-code-security-review (README.md in full; action.yml; claudecode/prompts.py, findings_filter.py, github_action_audit.py, constants.py; scripts/comment-pr-findings.js; .claude/commands/security-review.md; docs/custom-filtering-instructions.md, docs/custom-security-scan-instructions.md), read 2026-09-26",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude Code", "security review", "claude-code-security-review", "/security-review", "GitHub Actions",
             "pull requests", "code review", "false positives", "prompt injection", "AppSec", "diff-aware scanning",
             "Anthropic", "Claude", "Nik Bear Brown"]},
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
