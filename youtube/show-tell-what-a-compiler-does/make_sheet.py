#!/usr/bin/env python3
"""make_sheet.py — beat_sheet.json for show-tell-what-a-compiler-does.

SHOW-TELL (Bear 2026-09-26): every body beat is ONE drawn isometric illustration in the Claude palette, labels only,
Liam's voice explains. Card #22 in show-tell-ideas.md (Batch 2).
Spine: BIDEA hesitant writer -> BDEFS terms -> B00..B12 drawn -> BHTF composer -> BOUT.

Sources: anthropics/claudes-c-compiler/DESIGN_DOC.md ("High-Level Pipeline", "Source Tree", "Compilation Pipeline
(Data Flow)", "Key Design Decisions", "Assembler and Linker Architecture") and README.md, both read in full
2026-09-27 and diffed against the raw upstream files (raw.githubusercontent.com/anthropics/claudes-c-compiler/main/):
identical (sources/live_*). The film explains what a compiler does, stage by stage, using THIS compiler's pipeline,
named as the design doc names it: preprocessor -> lexer -> parser -> sema -> IR lowering -> mem2reg (SSA) ->
optimization passes (+ phi elimination) -> code generation for four chips -> peephole -> builtin assembler ->
builtin linker -> ELF. The README's own caveat is quoted as worded ("None of it has been validated for correctness."
"The docs may be wrong" "I do not recommend you use this code"). No person is credited. Claude wrote it only as the
README says it. No numbers beyond the files' own ("up to 3 iterations", four targets).
Cast: the SOURCE PAGE (a white sheet with grey lines and a terracotta dot); TOKEN TILES (kraft tiles with grey
span tabs); the SYNTAX TREE (kraft nodes, grey edges); the SYMBOL TABLE (a grey-outlined card); IR STRIPS (white strips
with grey bars) and STACK SLOTS (small open kraft boxes); REGISTERS (dark tabs); the PHI dot (terracotta); the four
CHIP DOORS (dark blocks, one lamp each); ASSEMBLY STRIPS; BYTE TILES; the .o BLOCK; the ELF BOX (kraft, taped shut).
"""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
SLUG = HERE.name
TITLE = "What a Compiler Does"


def beat(bid, narration, cls, image, show):
    return {"beat_id": bid, "act": "show-tell", "lane": "manim", "proof_gate": "SHOW",
            "narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
            "voice": "am_onyx", "engine": "kokoro",
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": image, "show": show, "manim": {"class": cls},
                     "motion_claim": image}}


B = [
 beat("B00", "A compiler turns code written in C into a program a chip can run. Claude's C Compiler, which its read me says Claude wrote in Rust, from scratch, does it as one pipeline, with no outside tools. Let's follow one file through every stage.",
      "B00_Pipeline", "A white source page ('C source') waits at the left of a long pale belt; four machines rise onto the belt (three kraft, the last one dark with four lamps); the page rides through them in turn and comes out at the far end as a kraft box taped shut ('ELF program').",
      [{"at": 0.1, "event": "the C source page"}, {"at": 0.4, "event": "one pipeline of machines"}, {"at": 0.8, "event": "out comes a program"}]),
 beat("B01", "First, the preprocessor. It works on the raw text: it pastes in each header named by a hash include, expands every macro, and drops any code that an if def switches off.",
      "B01_Preprocess", "The source page grows large ('preprocessor'); a header page slides in and merges at its top ('#include'); one line with a kraft macro tag widens into three lines ('macro'); a bracketed block of two lines fades out and the page closes up.",
      [{"at": 0.1, "event": "the page"}, {"at": 0.45, "event": "a header pastes in"}, {"at": 0.7, "event": "a macro expands"}, {"at": 0.9, "event": "switched-off code drops out"}]),
 beat("B02", "Next, the lexer chops that text into tokens. Each name, number and symbol becomes one tile, and every tile keeps its span: where in the file it came from.",
      "B02_Lex", "One line of the page lifts out and stretches into a long white strip ('lexer'); a terracotta scan line sweeps along it and the strip splits into kraft tiles of different widths ('tokens'); a small grey span tab drops under each tile, with a grey thread back to the page.",
      [{"at": 0.1, "event": "one line of text"}, {"at": 0.35, "event": "cut into token tiles"}, {"at": 0.8, "event": "each keeps its span"}]),
 beat("B03", "The parser reads the tokens in order and builds a syntax tree, which shows how the pieces fit together. It works by recursive descent: each grammar rule calls the rules for the parts inside it.",
      "B03_Parse", "The tiles rise one by one, left to right, and settle as the leaves of a tree; grey edges draw up to kraft branch nodes and a root ('syntax tree', 'parser'); the root lights, then each branch in turn, top down.",
      [{"at": 0.15, "event": "tokens read in order"}, {"at": 0.4, "event": "a tree grows"}, {"at": 0.75, "event": "each rule calls the rules inside it"}]),
 beat("B04", "Then semantic analysis checks that the tree makes sense. It works out the type of every expression, computes constant values ahead of time, and records each name in a symbol table.",
      "B04_Sema", "Grey type tabs stamp onto the tree's nodes one by one ('types'); a small subtree folds up into a single node with a terracotta dot (a constant computed); a grey-outlined card at the right fills with rows as the name leaves send copies ('symbol table').",
      [{"at": 0.1, "event": "the tree is checked"}, {"at": 0.35, "event": "types stamp on"}, {"at": 0.6, "event": "a constant computed"}, {"at": 0.85, "event": "names go into the symbol table"}]),
 beat("B05", "Lowering turns the checked tree into I R, an in-between language that's the same for every chip. At first, every local variable gets a stack slot: its own box in memory.",
      "B05_Lower", "The tree shrinks away to the left and a column of white IR strips drops in, one by one ('IR'); below them a row of small open kraft boxes appears ('stack slots'), and a grey thread ties each variable strip to its box.",
      [{"at": 0.1, "event": "the tree becomes IR"}, {"at": 0.5, "event": "same for every chip"}, {"at": 0.75, "event": "each local gets a stack slot"}]),
 beat("B06", "A pass called mem to reg then promotes those slots into registers. The result is S S A form, and where two paths through the code meet, a phi node picks which value arrives.",
      "B06_SSA", "The threads cut and the stack-slot boxes sink away; a dark register tab snaps onto each strip ('registers'); the column splits into two short paths that rejoin at one strip, where a terracotta dot lands ('phi node').",
      [{"at": 0.1, "event": "slots promoted to registers"}, {"at": 0.55, "event": "two paths"}, {"at": 0.85, "event": "a phi node where they meet"}]),
 beat("B07", "Now the optimizer runs a chain of passes over the I R, looping up to three times. Constant folding does the math it can already see, and dead code elimination deletes what nothing uses. Last, phi nodes become plain register copies.",
      "B07_Optimize", "A grey loop track draws around the IR column with three round markers ('up to 3 rounds'); two strips merge into one (folding); two strips fade out and the column closes up (dead code); the terracotta phi dot turns into a plain grey strip ('optimizer').",
      [{"at": 0.1, "event": "passes loop over the IR"}, {"at": 0.45, "event": "constants folded"}, {"at": 0.65, "event": "dead code deleted"}, {"at": 0.9, "event": "phi nodes become copies"}]),
 beat("B08", "Then the back end. The same I R can go to one of four chips: x eighty-six sixty-four, i six eighty-six, A. Arch sixty-four, or risk five sixty-four. The chosen code generator writes assembly for that chip.",
      "B08_Codegen", "Four dark doors rise in a row, each with a grey lamp; the lamps light one by one as the chips are named; the first door's lamp turns terracotta ('x86-64'); the IR column slides into it and a column of white assembly strips comes out ('assembly').",
      [{"at": 0.1, "event": "the back end"}, {"at": 0.3, "event": "four chips"}, {"at": 0.8, "event": "assembly for the chosen chip"}]),
 beat("B09", "Each back end then runs a peephole optimizer over its assembly. It finds wasted patterns, like storing a value and loading it straight back, and cuts the waste.",
      "B09_Peephole", "The assembly column grows large ('peephole'); a terracotta scan line runs down it; a grey bracket closes on a store strip and the load strip under it ('store, load'); the load strip slides out and the column closes up.",
      [{"at": 0.1, "event": "the peephole pass"}, {"at": 0.55, "event": "a store then a load"}, {"at": 0.85, "event": "the waste is cut"}]),
 beat("B10", "The built-in assembler turns that text into machine code. It parses each line, encodes each instruction as bytes, and writes an object file, a dot o.",
      "B10_Assemble", "The strips ride into a kraft press ('assembler'); out the other side comes a row of grey byte tiles, one group per strip; the tiles pack into a kraft block ('.o file').",
      [{"at": 0.1, "event": "text into the assembler"}, {"at": 0.5, "event": "each instruction becomes bytes"}, {"at": 0.85, "event": "an object file"}]),
 beat("B11", "Last, the built-in linker. It reads the object file with the C runtime and libraries, resolves every symbol, finding where each named function lives, patches the code to point there, and writes the finished ELF executable.",
      "B11_Link", "The .o block slides left; two more kraft blocks slide in beside it ('runtime + libs'); grey cables draw from the .o block to the other two; the three push together into one kraft box, which closes under terracotta tape ('ELF', 'linker').",
      [{"at": 0.1, "event": "the linker"}, {"at": 0.3, "event": "object file, runtime, libraries"}, {"at": 0.55, "event": "symbols resolved, code patched"}, {"at": 0.85, "event": "the ELF executable"}]),
 beat("B12", "One warning, in the read me's own words: None of it has been validated for correctness. The docs may be wrong. And, I do not recommend you use this code. So use it to learn the stages, not to build real software.",
      "B12_Warning", "The taped ELF box sits centre-left; beside it a large empty check box draws in and stays empty ('not validated'); the design doc's white page slides in at the right with a grey question tab ('docs may be wrong').",
      [{"at": 0.15, "event": "not validated for correctness"}, {"at": 0.5, "event": "the docs may be wrong"}, {"at": 0.8, "event": "learn from it; don't ship with it"}]),
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
    "Salaam. This is Liam, in for Bear. It's tempting to ask how a compiler turns your code into a program in one go. But it doesn't happen in one go. So the real question is what a compiler does at each stage.",
    "BrutalistHesitantWriter",
    {"text": "What does a compiler\ndo to my code in one go?", "triggerWords": "do to my code in one go", "replacementWords": "do at each stage",
     "fontSize": 70, "charMs": 22, "hesitateBetween": 6, "hesitateWithin": 1, "mistakeRate": 2, "jitter": 20,
     "seed": SLUG, "banner": ""},
    [{"at": 0.0, "event": "types 'What does a compiler do to my code in one go?'"}, {"at": 0.6, "event": "backspaces 'do to my code in one go' -> 'do at each stage' on the spoken correction"}],
    lead_silence_s=0.8, motion_claim="The writer types the naive question (what does a compiler do to my code in one go) and corrects it to the real one (what does a compiler do at each stage).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}),
 remotion("BDEFS", "terms",
    "A compiler: a program that turns source code into a program a chip can run. A token: one word of code, like a name, a number, or a symbol. I R: the compiler's own in-between language. And assembly: a chip's instructions, written as text.",
    "ClaudeDefinitions",
    {"title": "Terms In This Film",
     "terms": [{"term": "compiler", "meaning": "turns source code into a program a chip can run"},
               {"term": "token", "meaning": "one word of code: a name, a number, a symbol"},
               {"term": "IR", "meaning": "the compiler's own in-between language"},
               {"term": "assembly", "meaning": "a chip's instructions, written as text"}],
     "folderLabel": "@NikBearBrown"},
    [{"at": 0.05, "event": "'compiler' lands"}, {"at": 0.3, "event": "'token' lands"}, {"at": 0.55, "event": "'IR' lands"}, {"at": 0.8, "event": "'assembly' lands"}], gate="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: four prerequisites, one line each."}),
]

YT_PROMPT = ("Write add.c, a main that sets x to 2 and y to 3 and returns x + y. Using the C compiler on this machine, "
             "show it to me one stage at a time: the preprocessed text, the tokens, the syntax tree, and the assembly at "
             "-O0 and at -O2. Name the stage that made each one. Then build it and run it.")
SPOKEN_PROMPT = ("Write add dot c, a main that sets x to two and y to three and returns x plus y. Using the C compiler on this machine, "
                 "show it to me one stage at a time: the preprocessed text, the tokens, the syntax tree, and the assembly at "
                 "O zero and at O two. Name the stage that made each one. Then build it and run it.")
CHECKS = ["Check: does echo $? print 5?",
          "Check: at -O2, is the add gone?"]
YOURTURN = remotion("BHTF", "your turn",
    "Your turn. In Claude Code, paste this. " + SPOKEN_PROMPT +
    " Then check: does echo dollar question mark print five? And at O two, is the add instruction gone, folded into a five?",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "CLAUDE CODE · YOUR TURN", "segment": TITLE, "command": YT_PROMPT,
     "runningText": "paste this into Claude Code…",
     "output": CHECKS,
     "folderLabel": "@NikBearBrown", "modelLabel": "Opus 5.5", "effortLabel": "High"},
    [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two check lines land"}])

SPARSE_REASON = ("show-tell style (Bear, 2026-09-26): one drawn scene (the source page, token tiles, a syntax tree, IR strips, "
                 "chip doors, the taped ELF box) on a cream stage per beat, minimal labels, with the voice carrying the "
                 "explanation. The negative space is the style, so only underfill and clustered are waived; edge-bleed, "
                 "empty-frame and contrast still apply.")
FILLS_ON_ITS_OWN = {"B00", "B03"}   # local Gate V pre-check 2026-09-27 (1080p up to 2160, 25-99%): B00 0.64-0.73, B03 0.60-0.61, no defects; the rest keep the waiver
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
    "slug": SLUG, "title": TITLE, "topic": "CLAUDE'S C COMPILER · DESIGN DOC", "skill": "show-tell", "style_preset": "show-tell",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown", "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160,
    "caption_policy": "none", "greeting_language": "Arabic (Salaam)",
    "bookend_exempt": ["cold-open", "bvdt"],
    "bookend_exempt_reason": "show-tell style (Bear, 2026-09-26): opens on the hesitant writer + terms card (Bear, 2026-09-26: 'add hesitant writer as the first beat and key terms like tldr uses as the second'), no verdict card; Your Turn is the Claude.ai composer; spoken outro stays.",
    "audience": "CS students and developers who use a C compiler every day and want to know what happens inside it, stage by stage, shown on one real compiler's pipeline (Claude's C Compiler, which its README says is not validated for correctness)",
    "source_doc": "anthropics/claudes-c-compiler/DESIGN_DOC.md (High-Level Pipeline and stage descriptions) and README.md, read in full 2026-09-27 and diffed against the raw upstream files (sources/live_*)",
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "tags": ["compiler", "C compiler", "Claude's C Compiler", "CCC", "preprocessor", "lexer", "parser", "syntax tree",
             "semantic analysis", "IR", "SSA", "optimizer", "code generation", "assembler", "linker", "ELF", "Rust",
             "Claude", "Anthropic", "Nik Bear Brown"]},
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
