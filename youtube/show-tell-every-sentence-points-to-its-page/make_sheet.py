#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-every-sentence-points-to-its-page.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #15 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-cookbooks/misc/using_citations.ipynb (read in full), checked against the RAW
live docs page (platform.claude.com/docs/en/build-with-claude/citations.md, fetched with curl 2026-09-27,
saved in sources/live_citations-2026-09-27.md). The notebook's model list is out of date: the film names
NO model (the live page says "All active models support citations").
Cast: a pale TABLE; three DOCUMENTS on it (a white plain-text page, a PDF stack, a column of kraft
custom-content blocks), each with a small toggle (terracotta knob = citations on); sentences drawn as grey
bars; an ANSWER page whose lines write in one by one; ink THREADS from an answer line to a highlighted
passage, with a terracotta dot where they land; a CITED-TEXT slip; two token meters; a magnifier.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Every Sentence Points to Its Page"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "You put your documents in the request, next to your question, and switch citations on for each one. It's all or none: every document in the request, or none of them. Every active Claude model supports it.",
      "B00_Table", "A pale table; three documents drop onto it (a white text page, a PDF stack, a column of kraft blocks) and a question card slides in beside them ('documents', 'question'); a small toggle by each document flips its knob to terracotta, one after another ('citations on'); then all three flip off together and on together (all or none).",
      [{"at": 0.1, "event": "three documents drop onto the table"}, {"at": 0.3, "event": "the question card"}, {"at": 0.55, "event": "the toggles flip on, all three"}]),
 beat("B01", "First, each document is cut into chunks. Plain text and PDFs are cut into sentences. Claude can cite one sentence, or chain a few in a row into a passage, but never less than one sentence.",
      "B01_Chunks", "The text page grows to fill the stage; a terracotta scan line sweeps down it and each ghost line splits into separate sentence bars in alternating greys ('sentences'); two neighbouring sentences darken together and an ink bracket joins them ('passage').",
      [{"at": 0.1, "event": "the page grows"}, {"at": 0.3, "event": "the scan cuts sentences"}, {"at": 0.7, "event": "two sentences chained into a passage"}]),
 beat("B02", "Then Claude answers in pieces. Each piece is a text block: one claim, with a list of the citations behind it. As each claim lands, a thread runs back to the passage it came from, and names the document it's in.",
      "B02_Threads", "The text page and the PDF sit at the left, numbered 0 and 1; an answer page lands at the right ('answer'); its lines write in one at a time, and as each lands an ink thread arcs from it to a sentence on one of the documents, which turns dark grey, with a terracotta dot where the thread lands.",
      [{"at": 0.1, "event": "the answer page"}, {"at": 0.3, "event": "claim 1 writes, a thread to document 0"}, {"at": 0.75, "event": "claim 2, a thread to document 1"}]),
 beat("B03", "For plain text, the pointer is a character range: where the passage starts and where it stops, counted from zero. In the docs' own example, the grass is green runs from character zero to twenty.",
      "B03_Characters", "The text page is large at centre with one thread landing on a highlighted sentence; two ink flags rise at its start and its end, numbered 0 and 20; a terracotta dot runs along the sentence from the start flag to the end flag ('characters').",
      [{"at": 0.1, "event": "the cited sentence"}, {"at": 0.4, "event": "start and end flags"}, {"at": 0.75, "event": "0 to 20"}]),
 beat("B04", "For a PDF, it's a page range, counted from one. The text is pulled out and cut into sentences too. But only text can be cited. A picture on the page can't be, and a scanned page with no text can't be cited at all.",
      "B04_Pages", "The PDF's three pages fan out in a row, numbered 1, 2, 3 ('pages'); a thread lands on a sentence on page 2; a dashed ghost thread heads for a picture on page 3 and fades before it gets there; a blank scanned page slides in and no thread reaches it.",
      [{"at": 0.1, "event": "pages fan out, numbered from 1"}, {"at": 0.35, "event": "a thread lands on page 2"}, {"at": 0.65, "event": "the picture gets no thread"}, {"at": 0.85, "event": "the scan gets none"}]),
 beat("B05", "Custom content is your own chunks, used as they are. Claude won't cut them any smaller, so the pointer is a block index, counted from zero. Use it for lists and transcripts, or whenever you want to choose the size yourself.",
      "B05_Blocks", "The column of kraft blocks of different sizes, numbered 0 to 3 ('blocks'); a thread lands on block 2 and the whole block lifts and its top warms; a new block of a different size drops onto the column.",
      [{"at": 0.1, "event": "your own blocks, numbered from 0"}, {"at": 0.4, "event": "a thread takes a whole block"}, {"at": 0.8, "event": "you choose the size"}]),
 beat("B06", "Each citation also hands back the cited text: the exact words. Those words don't count toward your output tokens, the way asking Claude to write out quotes would. And the pointers are guaranteed valid. They point only into documents you sent.",
      "B06_CitedText", "A thread runs from the text page to the answer; a white slip rides along it from the page to the answer ('cited text'); two meters beside it: 'quoting' fills tall while 'citations' stays short; an ink check lands above the thread's landing dot.",
      [{"at": 0.1, "event": "the cited-text slip rides back"}, {"at": 0.45, "event": "quoting fills, citations stays low"}, {"at": 0.8, "event": "a check at the thread's end"}]),
 beat("B07", "Every cited sentence points to its page. But not every line gets a citation. In the notebook's own example, your order likely hasn't shipped yet came back with none. That's Claude reasoning, not quoting. A line with no thread is the one to check yourself.",
      "B07_NoThread", "The answer page with two threaded lines to the source page; a third line writes and no thread comes; an ink ring circles it ('no citation'); a magnifier slides over the line ('answer' labels the page).",
      [{"at": 0.15, "event": "two threaded lines"}, {"at": 0.4, "event": "a third line, no thread"}, {"at": 0.85, "event": "the magnifier: check it yourself"}]),
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
    "Salaam. This is Liam, in for Bear. It's easy to think the way to get sources is to ask Claude to quote them. The citations feature does better: each cited sentence comes back pointing to its place in your documents. So the real question is where each sentence points.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nget Claude to quote its sources?", "triggerWords": "get Claude to quote its sources", "replacementWords": "see where each sentence points",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get Claude to quote its sources?'"}, {"at": 0.6, "event": "backspaces 'get Claude to quote its sources' -> 'see where each sentence points' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I get Claude to quote its sources) and corrects it to the real one (how do I see where each sentence points).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A document: a source you hand Claude inside the request. A citation: a pointer from part of the answer back to a place in a document. And a chunk: the smallest piece Claude can cite.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "document", "meaning": "a source you hand Claude inside the request"},
               {"term": "citation", "meaning": "a pointer from the answer to a place in a document"},
               {"term": "chunk", "meaning": "the smallest piece Claude can cite"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'document' lands"}, {"at": 0.4, "event": "'citation' lands"}, {"at": 0.75, "event": "'chunk' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: three prerequisites, one line each."}),
]

YT_PROMPT = ("Write a short Python script that sends README.md to Claude as a plain-text document with citations on, "
             "and asks what this project does. Print each text block of the answer, then under it the cited text "
             "and its character range, or NO CITATION if it has none.")
SPOKEN_PROMPT = (YT_PROMPT.replace("sends README.md", "sends the read me")
                 .replace("or NO CITATION", "or no citation"))
CHECKS = ["Check: README at each range matches the quote?",
          "Check: is each uncited line actually true?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude Code, in any repo with a read me: " + SPOKEN_PROMPT + " Then check two things yourself. "
    "Does the read me, cut at each range, match the quoted text? And is each line with no citation actually true?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn table-pages-and-threads scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B02", "B03", "B04", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): these measure 0.60-0.69 throughout; B00 (0.57), B01 (0.40), B05 (0.50) and B06 (0.50) dip below 0.55 and keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE API · CITATIONS", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Arabic (Salaam)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and developers who ask Claude questions about documents and want answers they can check line by line",
    "source_doc": "anthropics/claude-cookbooks/misc/using_citations.ipynb (read in full 2026-09-27); checked against the raw live docs page platform.claude.com/docs/en/build-with-claude/citations.md (fetched with curl 2026-09-27, saved in sources/)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude API", "citations", "document", "PDF", "plain text", "custom content", "cited text",
             "grounding", "RAG", "sources", "Anthropic", "cookbook", "Nik Bear Brown"]},
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
