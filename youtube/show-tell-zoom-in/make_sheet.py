#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-zoom-in.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the
Claude palette, labels only, Liam's voice explains. Card #32 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B10 drawn -> BHTF composer -> BOUT.

Source: anthropics/claude-cookbooks multimodal/crop_tool.ipynb, read RAW from GitHub main on
2026-09-27 (repo main @ 813fbeec; the notebook last changed in 6c63a145, 2026-07-23, "Rewrite the
crop-tool cookbook around a measured zoom tool"), plus the two live vision docs it cites
(vision.md, vision-coordinates.md). The local copy (47ebd6a5) is the OLD crop_image version with
normalized 0-1 inputs; the live notebook's tool is `zoom` with PIXEL inputs x1, y1, x2, y2, crops
from the full-resolution original and magnifies. The film follows the live notebook.
Cast: the CHART (a white card, grey grid, grey series, line A in grey and line E in deep kraft that
nearly touch at one spot), the PATCH grid, the ORIGINAL (big chart card) and the VIEW (the resized
copy), CLAUDE (a dark block with a terracotta spark) and its ZOOM tool (a small dark tag), YOUR CODE
(a kraft box), the FRAME (the zoom box drawn on the chart), the TILE (the magnified crop), the LOOP
(arcs between Claude and your code), a scanned FORM, and two bars.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "Zoom In"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "Here's the problem this cookbook starts from. Claude sees an image once, at a fixed effective resolution. On a dense chart, a small label, or two lines that nearly touch, can be too small to make out. The cookbook says no amount of prompting recovers it.",
      "B00_Chart", "A white chart card rises on the stage; grey series lines draw across it; two lines (A grey, E kraft) draw and nearly touch at one spot; a tiny grey label sits by a peak ('tiny label'); a terracotta dot marks the spot ('nearly touch').",
      [{"at": 0.1, "event": "the chart"}, {"at": 0.35, "event": "one look, fixed resolution"}, {"at": 0.6, "event": "the tiny label, the near-touch"}, {"at": 0.85, "event": "prompting can't recover it"}]),
 beat("B01", "The reason is how Claude sees. It reads an image in patches, squares twenty-eight pixels on a side. Each patch is one visual token, and each model has a budget of them. An image over the budget is scaled down before Claude sees it, and the small details shrink with it.",
      "B01_Patches", "A grid of patches draws over the chart ('patches'); one patch is outlined and both lines fit inside it ('one patch'); a copy of the chart shrinks down to a smaller card ('scaled down').",
      [{"at": 0.1, "event": "the patch grid"}, {"at": 0.4, "event": "one patch holds both lines"}, {"at": 0.7, "event": "over budget: scaled down"}, {"at": 0.9, "event": "details shrink"}]),
 beat("B02", "So the cookbook's first step happens in your code. Keep the full-resolution original. Then resize a copy to exactly the size Claude will see, using resized size, a function from Claude's vision docs. That copy is what you send. Now any pixel Claude names lines up with the copy you hold.",
      "B02_Resize", "The big chart slides down-left ('original'); a kraft box lands beside it ('your code'); a smaller copy of the chart rises top-left ('copy'); corner ticks line up on the copy.",
      [{"at": 0.1, "event": "keep the original"}, {"at": 0.35, "event": "resize a copy"}, {"at": 0.65, "event": "send the copy"}, {"at": 0.9, "event": "pixels line up"}]),
 beat("B03", "Next, give Claude a tool named zoom. It takes four numbers: x one, y one, x two, and y two. Those are the left, top, right and bottom edges of a region, in pixels, counted from the top-left corner. An earlier version of this cookbook used numbers from zero to one. The vision docs say Claude works best with pixel coordinates, so the current one uses pixels.",
      "B03_Tool", "A dark Claude block with a terracotta spark lands right ('Claude'); a small dark tag snaps onto it ('zoom'); on the copy, an origin dot at the top-left ('0, 0'); a frame draws with its two corners marked ('x1, y1', 'x2, y2'); a pale '0 to 1' tag is crossed out.",
      [{"at": 0.1, "event": "the zoom tool"}, {"at": 0.3, "event": "four numbers"}, {"at": 0.55, "event": "edges in pixels from the top-left"}, {"at": 0.85, "event": "not 0 to 1: pixels"}]),
 beat("B04", "Now ask. The cookbook's question: at month forty-eight, which line is higher: the Widget A line, or the Widget E line? In the full view, the two lines nearly touch. So instead of answering, Claude calls zoom, with a box around that spot.",
      "B04_Ask", "A question slip slides into Claude ('A or E?'); the spot on the copy pulses; a frame draws around it; a small call card travels from Claude down to your code ('zoom call').",
      [{"at": 0.1, "event": "the question"}, {"at": 0.45, "event": "the lines nearly touch"}, {"at": 0.75, "event": "Claude calls zoom"}]),
 beat("B05", "Your code runs the call. It maps the box from the copy onto the full-resolution original, and cuts the region out of the original, not the copy. So the crop keeps every pixel the source image has.",
      "B05_Crop", "The frame on the copy is echoed, scaled up, onto the original ('same box'); the region lifts out of the original as a tile ('crop'); the copy's frame stays empty.",
      [{"at": 0.1, "event": "the call arrives"}, {"at": 0.35, "event": "the box maps onto the original"}, {"at": 0.65, "event": "cut from the original"}, {"at": 0.9, "event": "every pixel kept"}]),
 beat("B06", "Then it scales the crop up, to the largest size the image budget allows, so each detail covers more patches. It sends that back as the tool result: the magnified crop, as a JPEG, and one line of text naming the region. JPEG, because every result stays in the conversation, and a few big PNG crops can pass the API's request size limit.",
      "B06_Magnify", "The tile grows to a large magnified crop where A and E are clearly apart ('magnified'); a patch grid draws over it, the gap now spans several patches; the tile rides back to Claude with a grey text strip ('JPEG').",
      [{"at": 0.1, "event": "scaled up to the budget"}, {"at": 0.35, "event": "more patches per detail"}, {"at": 0.6, "event": "sent back as the result"}, {"at": 0.85, "event": "JPEG: results accumulate"}]),
 beat("B07", "Claude looks at the magnified crop. If it still can't tell, it zooms again, tighter. In the cookbook's run, it zoomed twice, then answered: Widget E is higher. Asked the same question without the tool, it had said Widget A, which was wrong.",
      "B07_Again", "The magnified crop sits centre; a smaller frame draws inside it; a second, tighter crop grows ('zoom 2'); E sits clearly above A at the month line; a check lands by E ('E higher'); a small 'A' slip is crossed out ('no tool').",
      [{"at": 0.1, "event": "Claude reads the crop"}, {"at": 0.3, "event": "zooms again, tighter"}, {"at": 0.6, "event": "answers: E"}, {"at": 0.85, "event": "without the tool: A, wrong"}]),
 beat("B08", "A loop drives all of this. Claude asks, your code crops and returns, and Claude looks again. The loop ends when Claude answers with words instead of a zoom call. The cookbook's runner also stops after twenty rounds, as a guard against a loop that runs away.",
      "B08_Loop", "Claude above, your code below; an ink arc draws down ('ask'), another draws back up ('crop'); a terracotta dot circles the loop twice; an answer card leaves Claude ('answer'); a small counter plate shows the cap ('max 20').",
      [{"at": 0.1, "event": "the loop"}, {"at": 0.4, "event": "ask, crop, look again"}, {"at": 0.65, "event": "ends with words"}, {"at": 0.9, "event": "capped at twenty rounds"}]),
 beat("B09", "The chart is only the example. The cookbook says the same pattern works wherever the detail is small next to the whole image: dense documents, screenshots, schematics, and scans of paper forms.",
      "B09_Anywhere", "The chart slides away; a scanned form card rises with many grey lines and a tiny field ('scanned form'); the same frame draws round the field; a magnified tile of it grows beside ('same move').",
      [{"at": 0.15, "event": "the chart was the example"}, {"at": 0.5, "event": "any small detail"}, {"at": 0.85, "event": "the same zoom"}]),
 beat("B10", "Does it help? The cookbook reports that on a public chart-reading benchmark, the zoom tool more than doubled accuracy. It isn't free. Each zoom is another round trip, and it re-sends the conversation plus a magnified crop. You trade tokens and time for detail.",
      "B10_Payoff", "Two grey bars grow side by side ('no tool', 'zoom tool'), the second more than twice the first ('more than 2x', 'per the cookbook'); then a stack of token slabs climbs beside them ('tokens').",
      [{"at": 0.15, "event": "the benchmark"}, {"at": 0.35, "event": "more than doubled"}, {"at": 0.6, "event": "not free"}, {"at": 0.85, "event": "tokens and time for detail"}]),
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
    "Bonjour. This is Liam, in for Bear. When Claude can't read a tiny label on a chart, it's tempting to ask how to make Claude see better. But Anthropic's cookbook doesn't change how Claude sees. It hands Claude a tool. So the real question is how to let Claude zoom in.",
    "BrutalistHesitantWriter",
    {"text": "How do I make Claude see better\non a dense chart?", "triggerWords": "make Claude see better", "replacementWords": "let Claude zoom in",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do I make Claude see better on a dense chart?'"}, {"at": 0.6, "event": "backspaces 'make Claude see better' -> 'let Claude zoom in' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (make Claude see better) and corrects it to the real one (let Claude zoom in).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A tool: a function your code runs when Claude asks for it. A patch: a small square of pixels that Claude sees as one unit. Coordinates: numbers that name a spot in the image, here in pixels. And a crop: one region, cut out of an image.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "tool", "meaning": "a function your code runs when Claude asks"},
               {"term": "patch", "meaning": "a square of pixels Claude sees as one unit"},
               {"term": "coordinates", "meaning": "numbers that name a spot, in pixels"},
               {"term": "crop", "meaning": "one region cut out of an image"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.1, "event": "'tool' lands"}, {"at": 0.35, "event": "'patch' lands"}, {"at": 0.6, "event": "'coordinates' lands"}, {"at": 0.8, "event": "'crop' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Add a zoom tool to my image-question script, the way Anthropic's crop_tool cookbook does it: "
             "inputs x1, y1, x2, y2 in pixels; crop from the full-resolution original, scale the crop up, "
             "and print every region Claude asks for.")
SPOKEN_PROMPT = ("Add a zoom tool to my image question script, the way Anthropic's crop tool cookbook does it. "
                 "Inputs x one, y one, x two, y two, in pixels. Crop from the full-resolution original, scale the crop up, "
                 "and print every region Claude asks for")
CHECKS = ["Check: does each region cover the detail?",
          "Check: does the answer change with the tool off?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Open Claude Code in a project with a script that asks Claude about an image, and paste this: " + SPOKEN_PROMPT + ". "
    "Then check two things. First: does each printed region cover the detail the question is about? "
    "And does the answer change when you turn the tool off?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn chart-and-zoom scene on a cream stage per beat, minimal labels, "
                 "with the voice carrying the explanation. The negative space is the style, so only underfill and clustered "
                 "are waived; edge-bleed, empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B03", "B04", "B05", "B06", "B07"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): 0.68-0.86 throughout; B00 (0.40), B01 (0.21 after the downscale), B02 (0.42 at 25%), B08 (0.37), B09 (0.18), B10 (0.00-0.26) keep the waiver
for b in B:
    if b["beat_id"] not in FILLS_ON_ITS_OWN:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": SPARSE_REASON}
B = OPEN + B + [YOURTURN]
B.append({"beat_id": "BOUT", "act": "outro", "lane": "bookend", "proof_gate": "SHOW",
          "narration_text": "Zoom In. At Nik Bear Brown.", "estimated_duration_s": 4.0, "voice": "am_onyx", "engine": "kokoro",
          "shot": {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                   "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""}}},
          "kind": "outro_voice", "tail_silence_s": 1.0})

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE API · VISION", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "French (Bonjour)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Developers and students who send images to Claude and want it to read small detail in charts, documents and screenshots",
    "source_doc": "anthropics/claude-cookbooks multimodal/crop_tool.ipynb, read RAW from GitHub main @ 813fbeec on 2026-09-27 (notebook rewritten in 6c63a145, 2026-07-23), plus the live vision.md and vision-coordinates.md it cites (sources/live_*); the stale local copy (47ebd6a5) was diffed",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Claude", "Claude API", "vision", "tool use", "zoom tool", "crop tool", "image analysis", "charts",
             "Anthropic cookbook", "agentic loop", "Anthropic", "Nik Bear Brown"]},
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
