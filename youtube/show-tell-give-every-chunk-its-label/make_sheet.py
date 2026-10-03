#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-give-every-chunk-its-label.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #16 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B07 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-cookbooks/capabilities/contextual-embeddings/guide.ipynb
("Enhancing RAG with Contextual Retrieval"), every cell and output read in full 2026-09-27.
Only one number is shown on screen: the notebook's 35% ("Averaged across all data sources we tested,
Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35%"), quoted and attributed.
Cast: a long white DOCUMENT page that is cut into four CHUNK cards (one hero card with a terracotta dot);
Claude as a kraft READER block with a terracotta spark; a kraft CONTEXT NOTE tab that sits on the front of
a chunk; a dark EMBED block; a pale INDEX map of grey dots; a kraft BM25 board of grey word slips; a kraft
CACHE shelf; a QUESTION pill; a RERANK frame with a scan line. Not the filing cabinet ("How a Skill Loads")
and not the tray ("Context Is a Budget").
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Give Every Chunk Its Label"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Retrieval augmented generation, or RAG, lets Claude answer from your own documents. First, each document is cut into chunks, so a search can hand Claude just the piece it needs.",
      "B00_Cut", "A long white document page drops onto the stage ('document'); three ink cut lines draw across it; the page splits into four white chunk cards that slide apart ('chunks'); one card carries a terracotta dot.",
      [{"at": 0.1, "event": "the document lands"}, {"at": 0.5, "event": "cut lines draw"}, {"at": 0.8, "event": "four chunk cards slide apart"}]),
 beat("B01", "But a chunk on its own can lose its context. Cut out of its file, it may not say which file it came from, or what it's part of. Embedded alone, it's harder to find.",
      "B01_Lost", "The other cards fade; the hero card grows to centre ('chunk'); a ghost dashed outline of the document it came from fades behind it; an ink question mark pops beside it ('?'); a search lens glides across the stage and passes the card by ('search').",
      [{"at": 0.1, "event": "one chunk alone"}, {"at": 0.45, "event": "which file? the question mark"}, {"at": 0.8, "event": "the search glides past"}]),
 beat("B02", "The fix is called contextual embeddings. For each chunk, Claude reads the whole document and the chunk, and writes a short note that situates the chunk within the document. The notebook's prompt asks for just that note, and nothing else.",
      "B02_Note", "Claude, a kraft block with a terracotta spark, drops in at centre ('Claude'); the whole document slides in at the left ('document') and the hero card sits at the right; ink reading lines draw from both to Claude; a kraft note tab rises out of Claude and arcs onto the front of the card ('context').",
      [{"at": 0.1, "event": "Claude"}, {"at": 0.3, "event": "the whole document plus the chunk"}, {"at": 0.6, "event": "the context note lands on the card"}]),
 beat("B03", "That note goes in front of the chunk, and the two are embedded together, as one text. Now the chunk carries its context into the search index.",
      "B03_Embed", "Claude and the document leave; the labelled card slides into a dark embed block ('embed'); a terracotta dot comes out the other side and lands on a pale index map of grey dots ('index').",
      [{"at": 0.15, "event": "note in front of the chunk"}, {"at": 0.45, "event": "embedded together"}, {"at": 0.8, "event": "the dot lands in the index"}]),
 beat("B04", "Does it help? Averaged across all the data sources Anthropic tested, contextual embeddings reduced the top twenty chunk retrieval failure rate by thirty five percent. That's from Anthropic's notebook, and it's for the embeddings alone.",
      "B04_Fewer", "The index shrinks to the corner; two grey bars stand side by side, one beside a bare card and one beside a labelled card ('top-20 failures'); the labelled card's bar shrinks by a third; the hero number lands ('35%', 'per Anthropic's notebook').",
      [{"at": 0.2, "event": "two failure bars"}, {"at": 0.55, "event": "the labelled bar shrinks"}, {"at": 0.75, "event": "35%, per Anthropic's notebook"}]),
 beat("B05", "But that means sending the whole document once per chunk. Prompt caching makes it practical. The first call writes the document to the cache, for a small premium. Every later chunk reads it back at a ninety percent discount on those tokens, the notebook says. And it's paid once, when the index is built.",
      "B05_Cache", "Claude sits at centre; the document slides from Claude onto a kraft shelf ('cache'); three chunk cards ride a pale belt past Claude; for each one an ink line flashes from the shelf to Claude and a kraft note drops onto the card ('90% off'); the belt stops at the index.",
      [{"at": 0.1, "event": "one call per chunk"}, {"at": 0.35, "event": "the document goes to the cache shelf"}, {"at": 0.6, "event": "each later chunk reads from the cache"}, {"at": 0.9, "event": "paid once, at build time"}]),
 beat("B06", "The same notes help a keyword search too. B M twenty-five catches exact words, like function names, that meaning-based search can miss. The notebook searches each chunk and its note both ways, then merges the two rankings into one list.",
      "B06_TwoWays", "The index map sits at the left ('embeddings') and a kraft board of grey word slips rises at the right ('BM25'); a question pill drops in above; ink lines draw from it to both; a few dots and slips light; small cards lift from both and stack into one list between them.",
      [{"at": 0.1, "event": "the keyword board"}, {"at": 0.45, "event": "exact words"}, {"at": 0.8, "event": "two rankings merge into one list"}]),
 beat("B07", "Last, reranking. Pull more candidates than you need, then a reranking model scores each one against the question, reading the chunk and its note, and keeps only the best few. The right chunk comes back to Claude, with its context attached.",
      "B07_Rerank", "The one list becomes a longer column of cards inside a kraft frame ('reranker'); a terracotta scan line sweeps down the column; the cards reorder and the hero card with its note rises to the top; the bottom cards fade; the top three slide across to Claude ('best few').",
      [{"at": 0.1, "event": "more candidates"}, {"at": 0.4, "event": "the reranker scores each"}, {"at": 0.7, "event": "the best few stay"}, {"at": 0.9, "event": "the right chunk back to Claude"}]),
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
    "Hallo. This is Liam, in for Bear. When a search over your documents hands Claude the wrong passage, it's tempting to want a better search engine. But the trouble can start earlier, when each document is cut into pieces. So the real question is how to give every chunk its context.",
    "BrutalistHesitantWriter",
    {"text": "How do I\nget a better search engine?", "triggerWords": "get a better search engine", "replacementWords": "give every chunk its context",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I get a better search engine?'"}, {"at": 0.6, "event": "backspaces 'get a better search engine' -> 'give every chunk its context' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do I get a better search engine) and corrects it to the real one (how do I give every chunk its context).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A chunk: a small piece cut from a longer document. An embedding: numbers that capture what a text means. B M twenty-five: a keyword ranking that matches exact words. And a reranker: a model that scores the top results again.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "chunk", "meaning": "a small piece cut from a longer document"},
               {"term": "embedding", "meaning": "numbers that capture what a text means"},
               {"term": "BM25", "meaning": "a keyword ranking that matches exact words"},
               {"term": "reranker", "meaning": "a model that scores the top results again"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'chunk' lands"}, {"at": 0.3, "event": "'embedding' lands"}, {"at": 0.6, "event": "'BM25' lands"}, {"at": 0.8, "event": "'reranker' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Add contextual chunk headers to this repo's RAG pipeline. For each chunk, send Claude the whole document "
             "plus the chunk, and ask for a short note that situates it. Prepend the note before embedding, and keep the "
             "old index. Then write five test questions with their answer chunks, and compare the top five from each index.")
CHECKS = ["Check: read five notes. Each true to its document?",
          "Check: rerun the questions. More hits in the top five?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Open Claude Code in a repo with a small search over documents, and paste this. " + YT_PROMPT +
    " Then check two things yourself. Read five of the notes: is each one true to its document? And rerun your questions: do more of the right chunks land in the top five?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (a document cut into chunk cards, Claude writing a context note, "
                 "an index, a reranker) on a cream stage per beat, minimal labels, with the voice carrying the explanation. "
                 "The negative space is the style, so only underfill and clustered are waived; edge-bleed, empty-frame and "
                 "contrast still apply.")
FILLS_ON_ITS_OWN = set()   # set from the local Gate V pre-check
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE COOKBOOK · CONTEXTUAL RETRIEVAL", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German / Dutch (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers and students building retrieval (RAG) over their own documents with Claude, who want to know why a search misses the right passage and how contextual embeddings fix it",
    "source_doc": "anthropics/claude-cookbooks/capabilities/contextual-embeddings/guide.ipynb ('Enhancing RAG with Contextual Retrieval'; every cell and output read in full 2026-09-27)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "RAG", "retrieval augmented generation", "contextual retrieval", "contextual embeddings", "embeddings",
             "BM25", "hybrid search", "reranking", "prompt caching", "chunking", "claude-cookbooks", "Anthropic", "Nik Bear Brown"]},
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
