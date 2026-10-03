#!/usr/bin/env python3
"""make_sheet.py — show-tell: Your Resume Is Data, Not a Document.

Bear's brief, 2026-09-27: the committee work and other work is not in the resume.json;
mine the interfolio dossier for it; make the case for keeping a resume as JSON rather
than a Word doc that AI edits in place — he has known students who ended up claiming
defense skills they did not have, because AI added them and nobody noticed.

Run from books/:  python3 anthropics/youtube/show-tell-resume-json/make_sheet.py
"""
import json, os

SLUG = "show-tell-resume-json"
TITLE = "Your Resume Is Data, Not a Document"
HERE = os.path.dirname(os.path.abspath(__file__))


def beat(bid, narration, cls, intent, show, **extra):
    b = {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show,
                  "manim": {"class": cls}}}
    b.update(extra)
    return b


def remotion(bid, act, narration, pattern, props, show, gate="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": "bookend", "proof_gate": gate,
         "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
         "voice": "am_onyx", "engine": "kokoro",
         "shot": {"type": "REMOTION", "source": "own", "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


BODY = [
 beat("B00",
   "Here is a resume as most people keep it. One document. You open it, edit it, save it. Every version writes over "
   "the one before.",
   "B00_OneDocument",
   "An isometric page sits on the cream stage with a few ink text lines; a pencil sweeps across it and the "
   "lines under the sweep are replaced. A faint ghost of the old lines fades out beneath. Label: resume.doc",
   [{"at": 0.15, "event": "page lands with text lines"},
    {"at": 0.6, "event": "pencil sweeps; lines are overwritten"},
    {"at": 0.85, "event": "the old lines fade to ghost and vanish"}],
   motion_claim="The overwrite is the motion: the previous version disappears as the new one lands."),

 beat("B01",
   "Now you ask a model to tune it for a job. It rewrites your bullets, tightens your verbs. And sometimes it adds a "
   "line you never wrote.",
   "B01_ModelEdits",
   "The same page. Three ink lines lift, re-set slightly tighter, and settle. Then a FOURTH line slides in "
   "from off-stage and settles between two real ones, drawn in the same ink as the rest. No highlight, no marker.",
   [{"at": 0.2, "event": "three lines lift and re-set"},
    {"at": 0.7, "event": "a fourth line slides in and settles among them"}],
   motion_claim="The inserted line arrives in the same ink and the same rhythm as the real ones — that is the whole danger."),

 beat("B02",
   "I have known students whose resumes claimed defense skills they did not have, because a model added them and "
   "nobody caught it. The page looked better, so it went out.",
   "B02_Unnoticed",
   "Pull back: the page rides into an outbox tray. A magnifier passes over it and stops on the inserted line, "
   "which is indistinguishable from its neighbours; the magnifier moves on without stopping. Label: sent",
   [{"at": 0.25, "event": "page slides into the outbox"},
    {"at": 0.6, "event": "magnifier passes over the inserted line"},
    {"at": 0.85, "event": "magnifier moves on; 'sent' lands"}],
   motion_claim="The magnifier crossing the fake line without catching it is the claim: nothing on the page marks it as added."),

 beat("B03",
   "So keep it as data instead. One record, named fields: education, experience, skills, service. Every line is "
   "something you can point at and check.",
   "B03_TheRecord",
   "The page transforms into an isometric card of stacked field rows, each row a labelled slot: education, "
   "experience, skills, service. Rows drop in one at a time with a thin ink outline. Label: resume.json",
   [{"at": 0.3, "event": "the page becomes a stack of field rows"},
    {"at": 0.55, "event": "rows land one by one"},
    {"at": 0.9, "event": "'resume.json' lands beside the stack"}],
   motion_claim="Rows landing as named slots is the difference from prose: the structure is what makes a line checkable."),

 beat("B04",
   "Then you read it yourself, line by line, and mark it attested, with a date. You are the only one who can say "
   "it is true.",
   "B04_Attest",
   "A cursor moves down the field rows; a terracotta check lands beside each as it passes. At the bottom a small "
   "slip stamps onto the card. Label beside the slip: attested · 2026-09-27",
   [{"at": 0.2, "event": "cursor descends the rows"},
    {"at": 0.55, "event": "checks land row by row"},
    {"at": 0.85, "event": "the attested slip stamps on with its date"}],
   motion_claim="The checks land one per row, in order — verification is per line, not per document."),

 beat("B05",
   "Now the letters come out of the record, not your last edit. A cover letter for this posting, a short resume for "
   "that one. The record stays. The output is disposable.",
   "B05_Generate",
   "The card stays centre-stage. Two thin pages peel off it and slide away to the right, each stamped with a "
   "small terracotta dot. The card is unchanged. Labels beside the pages: cover letter, targeted CV",
   [{"at": 0.25, "event": "first page peels off and slides away"},
    {"at": 0.55, "event": "second page peels off"},
    {"at": 0.85, "event": "the card sits unchanged"}],
   motion_claim="Pages leaving while the card stays put is the direction of the arrow: the record generates, never the reverse."),

 beat("B06",
   "Mine was missing my committee work entirely. So I pulled it from the promotion dossier I had already written. "
   "Three committees, and a task team that surveyed six hundred and seventy-nine students.",
   "B06_MissingField",
   "A binder stands beside the card with a visible gap in the card's field stack. Three pages lift out of the "
   "binder and drop into the gap, which closes. A small counter beside them climbs to 679.",
   [{"at": 0.2, "event": "binder appears; a gap shows in the stack"},
    {"at": 0.55, "event": "three pages lift out and drop into the gap"},
    {"at": 0.88, "event": "counter reaches 679"}],
   motion_claim="The gap closing is the motion: the material already existed in another document and was simply absent from this one."),

 beat("B07",
   "And a section I had never written down: teaching other people's faculty to use a company's tools well. "
   "Twenty-five course assistants for courses I do not teach. Seven hundred learners in one course the Dean commissioned.",
   "B07_BridgeWork",
   "A new field row grows onto the card, taller than the rest. Out of it, small server-lights fan out to a row of "
   "distant boxes that are NOT the card — other people's courses. A counter beside them climbs to 700.",
   [{"at": 0.25, "event": "the new row grows on the card"},
    {"at": 0.55, "event": "lights fan out to other courses"},
    {"at": 0.9, "event": "counter reaches 700"}],
   motion_claim="The lights reaching boxes outside the card carries the claim: the work served courses that were not his."),

 beat("B08",
   "Then the part I did not expect. My own job matcher reads four fields, and service is not one of them. The collector "
   "that searched three thousand postings never read the resume at all. A field no tool reads is one you have to say "
   "out loud yourself.",
   "B08_FourFields",
   "The card again. A scan beam sweeps it, but only four rows light; the service and bridge-work rows stay grey as the "
   "beam passes over them. Beside the card, a separate stack of tiny postings has NO cable running to the card.",
   [{"at": 0.2, "event": "scan beam sweeps the card"},
    {"at": 0.5, "event": "four rows light; two stay grey"},
    {"at": 0.85, "event": "the postings stack sits with no cable to the card"}],
   motion_claim="The beam skipping two rows, and the missing cable, are both the finding: the data exists and nothing consumes it."),
]

OPEN = [
 remotion("BIDEA", "the question",
   "Hallo. This is Liam, in for Bear. Most people ask how to update a resume. The better question is where the resume lives.",
   "BrutalistHesitantWriter",
   {"text": "How do I update\nmy resume?", "triggerWords": "update", "replacementWords": "where does it live",
    "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
    "seed": SLUG, "banner": ""},
   [{"at": 0.0, "event": "types 'How do I update my resume?'"},
    {"at": 0.62, "event": "backspaces 'update' → 'where does it live' on the spoken correction"}],
   lead_silence_s=0.8,
   motion_claim="The writer types the maintenance question and corrects it into the one about where the truth is kept.",
   qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),

 remotion("BDEFS", "terms",
   "Three terms. A resume dot JSON: your resume as named fields instead of prose, so each line can be checked. "
   "Attested: you read a field yourself and dated it. And generated output: a letter built from the record, meant to "
   "be thrown away.",
   "ClaudeDefinitions",
   {"title": "Terms In This Film",
    "terms": [{"term": "resume.json", "meaning": "your resume as named fields, not prose — so every line can be pointed at and checked"},
              {"term": "attested", "meaning": "you read the field yourself and dated it; nothing is true because a model wrote it"},
              {"term": "generated output", "meaning": "a cover letter or targeted resume built from the record, and meant to be discarded"}],
    "folderLabel": "@NikBearBrown"},
   [{"at": 0.12, "event": "'resume.json' lands"}, {"at": 0.52, "event": "'attested' lands"}, {"at": 0.8, "event": "'generated output' lands"}],
   gate="CARD",
   qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Here is my resume as a document. Convert it to JSON with named fields for education, experience, skills, "
             "and service. Do not improve it, do not add anything, and do not reword my bullets. For every line you "
             "cannot source from what I gave you, put it in a list called unsourced instead of in the record.")

YOURTURN = remotion("BHTF", "your turn",
  "Your turn. Paste this into Claude: " + YT_PROMPT + " Then check two things. If the unsourced list is empty, did it "
  "drop something instead of flagging it? And is there a skill in the file you could not defend in an interview "
  "tomorrow? Cut it now, not then.",
  "ClaudeComposerAsk",
  {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": "Turn Your Resume Into Data",
   "command": YT_PROMPT, "runningText": "paste this into Claude…",
   "output": ["Check: is the unsourced list empty — or did it drop something instead of flagging it?",
              "Check: any skill in the file you could not defend in an interview tomorrow?"],
   "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5", "effortLabel": "High"},
  [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
   {"at": 0.1, "event": "the prompt types in full"},
   {"at": 0.8, "event": "two check lines land"}])

SPARSE = ("show-tell style (Bear, 2026-09-26): one drawn object or scene on a cream stage per beat, minimal labels, "
          "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
          "are waived; edge-bleed, empty-frame and contrast still apply.")
for b in BODY:
    b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE}

B = OPEN + BODY + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": f"{TITLE}. At Nik Bear Brown.", "estimated_duration_s": 4.0,
          "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own",
                   "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro",
                                "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE · RESUME AS DATA", "skill": "show-tell",
    "style_preset": "show-tell", "channel": "claude-liam", "persona": "Liam (in for Bear)",
    "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration",
    "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9",
    "width": 3840, "height": 2160, "caption_policy": "none", "greeting_language": "German/Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": ("show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card, "
        "no verdict card; Your Turn is the Claude.ai composer; spoken outro stays."),
    "audience": "anyone whose resume is a Word document they let a model edit",
    "source_doc": ("Bear's brief 2026-09-27. Facts from books/interfolio/packet/Section-E3-Service-Statement.docx and "
        "Appendix-C-Service-Materials.docx; the file changed is "
        "info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/facts/professor-bear-cv.json; the "
        "four-fields claim is RESUME_REQUIRED in the-reallocation-engine-fresh/.claude/skills/greenhouse-watch/"
        "scripts/greenhouse_watch.py; the never-reads-the-resume claim is lectern/collect.py."),
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["resume json", "AI resume", "job search", "attestation", "Claude", "Nik Bear Brown"]},
    "beats": B}

with open(os.path.join(HERE, "beat_sheet.json"), "w", encoding="utf-8") as f:
    json.dump(sheet, f, indent=1, ensure_ascii=False)
    f.write("\n")
est = sum(b["estimated_duration_s"] for b in B)
print(f"wrote beat_sheet.json — {len(B)} beats, {len(BODY)} drawn, ~{est:.0f}s estimated")
