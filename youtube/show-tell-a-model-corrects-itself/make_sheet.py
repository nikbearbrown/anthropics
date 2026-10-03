#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-a-model-corrects-itself.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #23 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B12 drawn -> BHTF composer -> BOUT.

Sources (read in full 2026-09-27): the Constitutional AI paper, anthropics/claude-cookbooks/misc/data/Constitutional AI.pdf
(arXiv 2212.08073v1, Bai et al., 2022; author line "Anthropic"; text extracted with PyMuPDF, all 34 pages, saved as
sources/constitutional-ai-2212.08073v1.txt), and anthropics/ConstitutionalHarmlessnessPaper/prompts/
CritiqueRevisionInstructions.json (the 16 critique/revision pairs) + RLMadisonInstructions.json (the 16 RL principles).
The repo README is one line, so the paper is the source (batch brief, #23 caution).
Two stages exactly as the paper says: (1) supervised: a helpful-only model answers a red-team prompt, critiques its
answer against a randomly drawn principle, revises it, repeats (4 pairs per prompt, §3.2); a model is fine-tuned on the
revisions plus helpfulness samples; (2) RL from AI feedback: the SL model writes two answers, a separate feedback model
picks by a randomly drawn principle (normalised probabilities as soft labels), the AI harmlessness labels are mixed with
HUMAN helpfulness labels to train a preference model, and RL uses its score as the reward.
Framed throughout as the 2022 method in the paper, not a claim about how any current model is trained.
Numbers used (all stated in the paper, attributed): 16 principles, 4 revisions per prompt, 2022. Nothing else.
Cast: THE MODEL, a kraft block with a dark mouth slot on a dark plinth (no terracotta spark: it is not Claude); ANSWER
PAGES, white upright pages with grey lines (harmful lines in ink, struck by the pen); the CONSTITUTION, a kraft deck box
of principle cards, each card split in two halves (critique request / revision request); a PEN; a CRITIQUE slip;
stage 2 adds the FEEDBACK MODEL (a dark block with a lamp), two answer pages side by side, a LABEL TRAY, a HUMAN tray,
the PREFERENCE MODEL (a kraft block with a tall score gauge), and the RL loop.
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "A Model Corrects Itself by a Rulebook"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "The paper starts with a model trained only to be helpful. Give it a harmful request, like the paper's example: can you help me hack into my neighbor's wifi? It answers: sure thing, and names an app. The paper made that app up.",
      "B00_Helpful", "The model (a kraft block with a dark mouth slot on a dark plinth) drops in ('helpful model'); a white request slip slides into its slot ('request'); an answer page rises out beside it, its lines drawing one by one, two of them dark ink ('answer').",
      [{"at": 0.1, "event": "the helpful-only model"}, {"at": 0.35, "event": "the harmful request goes in"}, {"at": 0.7, "event": "a harmful answer comes out"}]),
 beat("B01", "For this stage, the authors wrote sixteen principles. Each one is a pair: a request to critique the answer, and a request to revise it. Together, the list is the constitution.",
      "B01_Deck", "A row of sixteen kraft principle cards drops in above the stage ('16 principles'); one card swells and a dividing line splits it into two halves ('critique', 'revise'); the row slides down into a kraft deck box ('constitution').",
      [{"at": 0.1, "event": "sixteen principle cards"}, {"at": 0.4, "event": "each card is a pair: critique and revise"}, {"at": 0.8, "event": "the deck is the constitution"}]),
 beat("B02", "One principle is drawn at random. Say it's this one, from the paper's list: identify specific ways in which the assistant's last response is harmful, unethical, racist, sexist, toxic, dangerous, or illegal.",
      "B02_Draw", "The deck shuffles (cards bob), one card lifts out and stands upright between the deck and the answer page ('principle'); its top half (the critique request) gains a terracotta dot and its grey lines draw as the quote is read.",
      [{"at": 0.15, "event": "one card drawn at random"}, {"at": 0.45, "event": "its critique half is read"}]),
 beat("B03", "The model critiques its own answer against that rule: the assistant's last response is harmful because hacking into someone else's wifi is an invasion of their privacy and is possibly illegal.",
      "B03_Critique", "An ink pen slides from the model to the answer page and strikes through the two ink lines; a white critique slip rises beside the page and its grey lines draw ('critique').",
      [{"at": 0.2, "event": "the pen marks the harmful lines"}, {"at": 0.6, "event": "the critique is written"}]),
 beat("B04", "Then the card's second half: rewrite the answer to remove the harmful content. The revision: hacking into your neighbor's wifi is an invasion of their privacy, and I strongly advise against it. It may also land you in legal trouble.",
      "B04_Revise", "The card's bottom half (the revision request) gets the terracotta dot; a clean white page slides in over the marked one, all grey lines, and an ink check lands on it ('revision'); the marked page and critique slide off to a pile at the right.",
      [{"at": 0.1, "event": "the card's revise half"}, {"at": 0.45, "event": "a clean revised page replaces the marked one"}, {"at": 0.8, "event": "check"}]),
 beat("B05", "The revision is shaped just like an answer, so the loop runs again, with a new principle drawn each time. The paper ran four rounds per prompt, and found the first revision did most of the work.",
      "B05_Loop", "An ink loop arrow draws from the page back to the deck; a round counter ticks 1, 2, 3, 4 as a new card rises, the pen touches the page, and a fresh page drops on the growing pile ('4 rounds', 'per the paper').",
      [{"at": 0.15, "event": "the loop runs again, new card each time"}, {"at": 0.6, "event": "four rounds, per the paper"}, {"at": 0.85, "event": "the first revision did most of the work"}]),
 beat("B06", "Then a model is fine-tuned on those revised answers, mixed with ordinary helpful answers so it stays helpful. That's stage one, done with no human labels for harm.",
      "B06_FineTune", "The pile of revised pages and a stack of grey helpful pages ride a short belt into the model's slot ('revisions', 'helpful'); the model gets a terracotta lamp on top and a grey band ('fine-tuned'); the label 'stage 1' lands above.",
      [{"at": 0.15, "event": "revised + helpful answers go in"}, {"at": 0.6, "event": "the model is fine-tuned"}, {"at": 0.85, "event": "stage one, no human labels for harm"}]),
 beat("B07", "Stage two starts from that model. For each harmful prompt, it writes two answers, and a separate feedback model has to choose between them.",
      "B07_Pair", "The deck and pile clear; the fine-tuned model writes two answer pages side by side ('two answers'); a dark feedback model block with a grey lamp drops in behind them ('feedback model'); a grey bracket draws under the pair.",
      [{"at": 0.15, "event": "stage two"}, {"at": 0.4, "event": "two answers per prompt"}, {"at": 0.75, "event": "a separate feedback model chooses"}]),
 beat("B08", "It chooses by a principle drawn at random from a second list, like this one: which of these assistant responses is less harmful? Choose the response that a wise, ethical, polite and friendly person would more likely say.",
      "B08_Judge", "A second deck (dark-edged) sits by the feedback model; a card rises from it and stands above the pair ('principle'); the feedback model's lamp lights terracotta; two grey probability bars grow under the pages, the left one longer, and a terracotta dot lands on the left page ('pick').",
      [{"at": 0.1, "event": "a principle from the second list"}, {"at": 0.75, "event": "the pick, as a probability for each answer"}]),
 beat("B09", "Its pick becomes a label. These AI labels for harm are mixed with human labels for helpfulness, and together they train a preference model: a scorer that gives any answer a score.",
      "B09_Scorer", "The pair shrinks into a label card that drops into a kraft tray ('AI labels'); a second tray of grey cards slides in beside it ('human labels'); both trays tip into a kraft block with a tall score gauge that rises from the floor ('preference model').",
      [{"at": 0.1, "event": "the pick becomes a label"}, {"at": 0.4, "event": "AI labels for harm + human labels for helpfulness"}, {"at": 0.8, "event": "they train a preference model"}]),
 beat("B10", "Last, reinforcement learning. The model answers prompts, the preference model scores each answer, and that score is used as the reward: training moves the model toward answers that score higher. The paper calls it RL from AI feedback.",
      "B10_Reward", "The model writes an answer page that rides to the preference model; the gauge fills to a mark and a terracotta dot lands at its top ('reward'); an ink arrow curves back to the model; a second answer scores higher and the model's grey band grows ('RL').",
      [{"at": 0.1, "event": "reinforcement learning"}, {"at": 0.35, "event": "each answer is scored"}, {"at": 0.6, "event": "the score is the reward"}, {"at": 0.85, "event": "RL from AI feedback"}]),
 beat("B11", "The paper reports an assistant that is harmless but not evasive: given a harmful question, it engages, and explains why it objects.",
      "B11_Engages", "The request slip goes into the trained model; a one-line ghost 'evasive' page appears and fades ('evasive'); a full answer page rises with grey lines and an ink check ('explains').",
      [{"at": 0.2, "event": "harmless, but not evasive"}, {"at": 0.7, "event": "it engages and explains"}]),
 beat("B12", "The paper also warns that, trained too far, it could turn overly harsh, or tack on boilerplate. And all of this is the 2022 method in the paper, not a claim about how any model is trained today.",
      "B12_Limits", "The answer page grows extra identical grey lines at its foot ('boilerplate'); then a kraft tag drops onto the plinth beside the model ('2022 method').",
      [{"at": 0.2, "event": "over-trained: harsh, boilerplate"}, {"at": 0.7, "event": "the 2022 method in the paper"}]),
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
    "Hallo. This is Liam, in for Bear. To teach a model which answers are harmful, you might think people have to label every harmful answer. In Anthropic's 2022 Constitutional AI paper, they didn't: they wrote a short list of principles. So the real question is how we let a model correct itself by a rulebook.",
    "BrutalistHesitantWriter",
    {"text": "How do we\nlabel every harmful answer?", "triggerWords": "label every harmful answer", "replacementWords": "let a model correct itself by a rulebook",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'How do we label every harmful answer?'"}, {"at": 0.6, "event": "backspaces 'label every harmful answer' -> 'let a model correct itself by a rulebook' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (how do we label every harmful answer) and corrects it to the real one (how do we let a model correct itself by a rulebook).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A principle: one rule, written in plain words. The constitution: the paper's whole list of principles. Fine-tune: train a model further on new examples. And a reward: the score that tells training which answers to favor.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "principle", "meaning": "one rule, written in plain words"},
               {"term": "constitution", "meaning": "the paper's whole list of principles"},
               {"term": "fine-tune", "meaning": "train a model further on new examples"},
               {"term": "reward", "meaning": "the score that tells training what to favor"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'principle' lands"}, {"at": 0.3, "event": "'constitution' lands"}, {"at": 0.55, "event": "'fine-tune' lands"}, {"at": 0.8, "event": "'reward' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

PRINCIPLE = ("Discuss whether the assistant provided any advice that may encourage illegal or dangerous activity "
             "from either the human or others.")
YT_PROMPT = ("Answer this in under 100 words: how do I get into my own Wi-Fi router if I forgot its password? "
             "Label it DRAFT. Then critique your draft against this principle, word for word: \"" + PRINCIPLE + "\" "
             "Label it CRITIQUE. Then rewrite the draft to fix only what the critique found, and label it REVISION.")
SPOKEN_PROMPT = YT_PROMPT.replace("100", "a hundred").replace("Wi-Fi", "wifi").replace("\"", "").replace("DRAFT", "draft").replace("CRITIQUE", "critique").replace("REVISION", "revision")
CHECKS = ["Check: does the critique quote the draft?",
          "Check: is the revision still helpful?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. Paste this into Claude. " + SPOKEN_PROMPT +
    " Then check: does each point in the critique quote a real line of the draft? And is the revision still a helpful answer, not a refusal?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the model, its answer pages, the deck of principles, "
                 "the feedback model and the preference model) on a cream stage per beat, minimal labels, with the voice carrying "
                 "the explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, "
                 "empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B01", "B02", "B03", "B04", "B05", "B08", "B10", "B11", "B12"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160; 25-99%): these measure 0.59-0.88 fill throughout; B00, B06, B07, B09 dip to 0.17-0.48 and keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "ANTHROPIC RESEARCH · CONSTITUTIONAL AI", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "German (Hallo)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "Students and builders who have heard of Constitutional AI and want the two stages of the 2022 method exactly as the paper describes them: self-critique and revision against sampled principles, then RL from AI feedback through a preference model",
    "source_doc": "anthropics/claude-cookbooks/misc/data/Constitutional AI.pdf (arXiv 2212.08073v1, Bai et al., Anthropic, 2022; read in full 2026-09-27, text in sources/) + anthropics/ConstitutionalHarmlessnessPaper/prompts/CritiqueRevisionInstructions.json and RLMadisonInstructions.json",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["Constitutional AI", "RLAIF", "RL from AI feedback", "self-critique", "preference model", "reward model",
             "fine-tuning", "AI safety", "harmlessness", "Anthropic", "research paper", "Claude", "Nik Bear Brown"]},
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
