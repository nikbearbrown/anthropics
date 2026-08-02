"""vox_scenes.py — The Word That Erased 70,000 People (vox-truman-usefulness, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'. B01 and B08 are archive
STILL beats — no scenes here (they render as slates until pantry intake). Durations
read from this reel's beat_sheet.json; fallback to estimates.

Color law (teardown palette):
  INK   #2A1A0E = what the word names; the abstraction as framed; named/concrete things
  CRIMSON #C8102E = what the word erases; people, human reality, the deaths hidden by the noun
  GOLD (wash #F6D8DC) = editor's-pen sweep — used under 'usefulness' (B02) and
                        'legacy access patterns' (B09); NEVER as text color

Exclusions honored: no debate about justification of the bombing, no Japan surrender
context, no bomb physics. Strict rhetorical mechanism only.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

DUR = {
    "B02": 13.0, "B03": 12.0, "B04": 12.0, "B05": 13.0,
    "B06": 11.5, "B07": 12.0, "B09": 14.0, "B10": 14.0, "B11": 14.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 10.0)
                for b in _BS["beats"]})
except Exception:
    pass


# -----------------------------------------------------------------------
# B02 — The Truman sentence in large display type; gold sweep lands on
#        'usefulness'. The visual object: the sentence itself.
# -----------------------------------------------------------------------

class B02_TrumanSentence(Scene):
    def construct(self):
        total = DUR["B02"]
        # sentence split across three lines for legibility at display size
        line1 = Text("Sixteen hours ago an American airplane", font=SERIF,
                     color=INK, font_size=36)
        line2 = Text("dropped one bomb on Hiroshima, Japan,", font=SERIF,
                     color=INK, font_size=36)
        line3 = Text("and destroyed its usefulness to the enemy.", font=SERIF,
                     color=INK, font_size=36)
        block = VGroup(line1, line2, line3).arrange(DOWN, buff=0.22)
        block.scale_to_fit_width(12.2)
        block.move_to(UP * 0.3)
        attr = Text("— Truman administration statement, August 6, 1945",
                    font=SERIF, color=INK, font_size=22, slant=ITALIC)
        attr.next_to(block, DOWN, buff=0.55)

        # gold highlight bar: pre-positioned, then grows rightward via scale
        # 'usefulness to the enemy.' is approx the last 38% of line3 width
        usefulness_w = line3.width * 0.38
        bar_final_cx = line3.get_left()[0] + line3.width * 0.62 + usefulness_w / 2
        bar_y = line3.get_bottom()[1] - 0.04
        bar = Rectangle(width=usefulness_w, height=line3.height + 0.18)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.move_to([bar_final_cx, bar_y, 0])
        bar.set_z_index(-1)
        # start tiny (width near zero) at left edge of its final position
        bar.scale(np.array([0.01, 1.0, 1.0]))

        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(line2, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(line3, shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(attr, shift=UP * 0.08), run_time=0.5)
        self.wait(1.2)
        # gold sweep: scale bar from ~0 width to full width (single .animate method)
        line3.set_z_index(1)
        self.add(bar)
        self.play(bar.animate.scale(np.array([100.0, 1.0, 1.0])), run_time=0.9)
        self.wait(max(0.5, total - 4.55))


# -----------------------------------------------------------------------
# B03 — THE QUESTION card. Question on screen, narration carries the full
#        two-sentence form. Card is the anchor phrase.
# -----------------------------------------------------------------------

class B03_QuestionCard(Scene):
    def construct(self):
        total = DUR["B03"]
        eye = Text("WRITING", font=DISPLAY, color=INK, font_size=22,
                   weight="MEDIUM")
        eye.to_corner(UL, buff=0.7)
        q = Text("How does one noun carry the moral weight?",
                 font=SERIF, color=INK, font_size=44, weight="BOLD")
        q.scale_to_fit_width(11.8)
        q.move_to(UP * 0.3)
        u = Line(q.get_corner(DL) + DOWN * 0.14, q.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        sub = Text("what every press release since has been doing",
                   font=SERIF, color=INK, font_size=28, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.45)

        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(q), Create(u), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.0))


# -----------------------------------------------------------------------
# B04 — THE PROBLEM: each factual clause verified — all true.
#        Three chips appear one by one; each one is technically correct.
#        The PROBLEM beat: the sentence passes a naive fact-check.
# -----------------------------------------------------------------------

class B04_FactCheck(Scene):
    def construct(self):
        total = DUR["B04"]
        header = SerifLabel("Every clause checks out.", INK, size=30)
        header.to_edge(UP, buff=0.9)

        chip1 = LabelChip("American airplane", accent=SLATE, size=24)
        chip2 = LabelChip("one bomb dropped", accent=SLATE, size=24)
        chip3 = LabelChip("usefulness destroyed", accent=SLATE, size=24)
        chips = VGroup(chip1, chip2, chip3).arrange(DOWN, buff=0.45)
        chips.move_to(LEFT * 1.5 + DOWN * 0.2)

        ok1 = SerifLabel("factually true", INK, size=26)
        ok2 = SerifLabel("factually true", INK, size=26)
        ok3 = SerifLabel("factually true", INK, size=26)
        checks = VGroup(ok1, ok2, ok3).arrange(DOWN, buff=0.45)
        checks.move_to(RIGHT * 2.8 + DOWN * 0.2)

        q = SerifLabel("So where is the rhetoric?", CRIMSON, size=30)
        q.to_edge(DOWN, buff=0.8)

        self.play(FadeIn(header[0]), Create(header[1]), run_time=0.6)
        self.play(FadeIn(chip1, shift=RIGHT * 0.3), FadeIn(ok1, shift=LEFT * 0.2),
                  run_time=0.7)
        self.play(FadeIn(chip2, shift=RIGHT * 0.3), FadeIn(ok2, shift=LEFT * 0.2),
                  run_time=0.7)
        self.play(FadeIn(chip3, shift=RIGHT * 0.3), FadeIn(ok3, shift=LEFT * 0.2),
                  run_time=0.7)
        self.play(FadeIn(q, shift=UP * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 3.4))


# -----------------------------------------------------------------------
# B05 — THE MECHANISM: split screen. Left: isotype figures + hospital
#        cross + small marks (human reality, CRIMSON). Right: large INK
#        text 'usefulness' (the abstraction). The split is the mechanism.
# -----------------------------------------------------------------------

class B05_SplitScreen(Scene):
    def construct(self):
        total = DUR["B05"]

        divider = Line(UP * 3.6, DOWN * 3.6, color=SLATE, stroke_width=1.6)
        divider.move_to(ORIGIN)

        # Left side: human reality label + figures grid (CRIMSON)
        left_label = SerifLabel("what was there", CRIMSON, size=26)
        left_label.move_to(LEFT * 3.5 + UP * 2.9)

        # isotype grid: people + hospital cross + children marks
        people_grid = IsotypeGrid([24], [CRIMSON], per_row=6, size=0.18, gap=0.1)
        people_grid.move_to(LEFT * 3.5 + UP * 0.8)

        hosp_h = Rectangle(width=0.22, height=0.64)
        hosp_h.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        hosp_v = Rectangle(width=0.64, height=0.22)
        hosp_v.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        hospital = VGroup(hosp_h, hosp_v).move_to(LEFT * 3.5 + DOWN * 0.85)

        hosp_label = Text("hospitals", font=SERIF, color=CRIMSON, font_size=20,
                          slant=ITALIC)
        hosp_label.next_to(hospital, DOWN, buff=0.15)

        children_grid = IsotypeGrid([8], [CRIMSON], per_row=4,
                                    size=0.14, gap=0.08)
        children_grid.move_to(LEFT * 3.5 + DOWN * 1.85)
        child_label = Text("children", font=SERIF, color=CRIMSON,
                           font_size=20, slant=ITALIC)
        child_label.next_to(children_grid, DOWN, buff=0.12)

        # Right side: the abstraction — one word
        right_label = SerifLabel("what the sentence named", INK, size=26)
        right_label.move_to(RIGHT * 3.1 + UP * 2.9)
        right_label.scale_to_fit_width(5.6)

        usefulness = Text("usefulness", font=SERIF, color=INK,
                          font_size=72, weight="BOLD")
        usefulness.move_to(RIGHT * 3.1 + DOWN * 0.2)

        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(left_label[0]), Create(left_label[1]),
                  FadeIn(right_label[0]), Create(right_label[1]),
                  run_time=0.7)
        self.play(people_grid.count_up(2.0), run_time=2.0)
        self.play(FadeIn(hospital), FadeIn(hosp_label), run_time=0.6)
        self.play(children_grid.count_up(0.8), run_time=0.8)
        self.play(FadeIn(child_label), run_time=0.4)
        self.play(FadeIn(usefulness, scale=0.85), run_time=0.9)
        self.wait(max(0.5, total - 5.9))


# -----------------------------------------------------------------------
# B06 — THE MECHANISM: two-column layout. Named concretely (INK chips)
#        vs. abstracted away (CRIMSON chip). The mechanism named.
# -----------------------------------------------------------------------

class B06_Selection(Scene):
    def construct(self):
        total = DUR["B06"]

        col_left_label = SerifLabel("named concretely", INK, size=26)
        col_left_label.move_to(LEFT * 3.2 + UP * 2.7)

        col_right_label = SerifLabel("abstracted away", CRIMSON, size=26)
        col_right_label.move_to(RIGHT * 2.8 + UP * 2.7)

        # concrete named things (INK chips, SLATE accent for neutral structure)
        chip_airplane = LabelChip("airplane", accent=SLATE, size=26)
        chip_bomb = LabelChip("one bomb", accent=SLATE, size=26)
        chip_hiroshima = LabelChip("Hiroshima", accent=SLATE, size=26)
        left_chips = VGroup(chip_airplane, chip_bomb, chip_hiroshima)
        left_chips.arrange(DOWN, buff=0.4).move_to(LEFT * 3.2 + DOWN * 0.2)

        # abstracted noun (CRIMSON)
        chip_usefulness = LabelChip("usefulness", accent=CRIMSON, size=30)
        chip_usefulness.move_to(RIGHT * 2.8 + DOWN * 0.2)

        # mech_label positioned on the right column to avoid crossing the divider
        mech_label = SerifLabel("the selection is the argument", CRIMSON, size=24)
        mech_label.move_to(RIGHT * 2.8 + DOWN * 2.1)
        mech_label.scale_to_fit_width(5.2)

        divider = Line(UP * 3.2, DOWN * 2.8, color=SLATE, stroke_width=1.2)
        divider.move_to(ORIGIN + LEFT * 0.4)

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(col_left_label[0]), Create(col_left_label[1]),
                  FadeIn(col_right_label[0]), Create(col_right_label[1]),
                  run_time=0.6)
        self.play(FadeIn(chip_airplane, shift=RIGHT * 0.25), run_time=0.5)
        self.play(FadeIn(chip_bomb, shift=RIGHT * 0.25), run_time=0.5)
        self.play(FadeIn(chip_hiroshima, shift=RIGHT * 0.25), run_time=0.5)
        self.play(FadeIn(chip_usefulness, scale=0.9), run_time=0.7)
        self.play(FadeIn(mech_label[0]), Create(mech_label[1]), run_time=0.6)
        self.wait(max(0.5, total - 3.8))


# -----------------------------------------------------------------------
# B07 — THE MECHANISM: 'usefulness' in large display, HandRing traces
#        around it (editor's pen — used once). Then two chips appear:
#        what it names (INK) vs. what it covers (CRIMSON).
# -----------------------------------------------------------------------

class B07_SelectionIsArgument(Scene):
    def construct(self):
        total = DUR["B07"]

        big_word = Text("usefulness", font=SERIF, color=INK,
                        font_size=96, weight="BOLD")
        big_word.move_to(UP * 0.8)

        not_a_lie = SerifLabel("a selection, not a lie", INK, size=30)
        not_a_lie.next_to(big_word, DOWN, buff=0.5)

        chip_names = LabelChip("names: military utility", accent=SLATE, size=24)
        chip_names.move_to(LEFT * 2.8 + DOWN * 2.4)

        chip_covers = LabelChip("covers: people erased", accent=CRIMSON, size=24)
        chip_covers.move_to(RIGHT * 2.4 + DOWN * 2.4)

        # HandRing around the word — the one editor's pen
        ring = HandRing(big_word, color=CRIMSON)

        self.play(FadeIn(big_word, scale=0.85), run_time=0.8)
        self.play(FadeIn(not_a_lie[0]), Create(not_a_lie[1]), run_time=0.7)
        self.play(Create(ring), run_time=1.1)
        self.play(FadeIn(chip_names, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(chip_covers, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.5, total - 3.8))


# -----------------------------------------------------------------------
# B09 — THE EXAMPLE: illustrative press-release quote card.
#        Gold sweep under 'legacy access patterns'. Then CRIMSON chip
#        reveals who it covers: '40,000 users — no access'.
# -----------------------------------------------------------------------

class B09_PressRelease(Scene):
    def construct(self):
        total = DUR["B09"]

        eye = LabelChip("illustrative", accent=SLATE, size=20)
        eye.to_corner(UL, buff=0.6)

        # quote card — the invented press release sentence
        quote_text = (
            "The service change eliminates legacy access patterns."
        )
        q_line = Text(quote_text, font=SERIF, color=INK, font_size=38)
        q_line.scale_to_fit_width(11.6)
        q_line.move_to(UP * 0.9)

        attr = Text("— invented press release (illustrative)",
                    font=SERIF, color=INK, font_size=22, slant=ITALIC)
        attr.next_to(q_line, DOWN, buff=0.45)

        # gold bar sweep under 'legacy access patterns'
        # 'legacy access patterns' is approx the last 56% of the line
        lap_w = q_line.width * 0.56
        bar_final_cx = q_line.get_left()[0] + q_line.width * 0.44 + lap_w / 2
        bar_y = q_line.get_bottom()[1] - 0.04
        bar = Rectangle(width=lap_w, height=q_line.height + 0.18)
        bar.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        bar.move_to([bar_final_cx, bar_y, 0])
        bar.set_z_index(-1)
        # start tiny then grow via single .animate.scale
        bar.scale(np.array([0.01, 1.0, 1.0]))
        q_line.set_z_index(1)

        # what it names vs. what it covers — same split as B06/B07
        col_names = LabelChip("names: service change", accent=SLATE, size=22)
        col_names.move_to(LEFT * 2.8 + DOWN * 2.2)

        col_covers = LabelChip("covers: 40,000 users -- no access",
                               accent=CRIMSON, size=22)
        col_covers.move_to(RIGHT * 2.0 + DOWN * 2.2)
        col_covers.scale_to_fit_width(5.8)

        self.play(FadeIn(eye, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(q_line, shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(attr, shift=UP * 0.08), run_time=0.5)
        self.wait(0.8)
        self.add(bar)
        self.play(bar.animate.scale(np.array([100.0, 1.0, 1.0])), run_time=0.9)
        self.wait(0.6)
        self.play(FadeIn(col_names, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(col_covers, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 5.0))


# -----------------------------------------------------------------------
# B10 — THE PRACTICE: two-step heuristic chips appear sequentially.
#        The concrete actionable move.
# -----------------------------------------------------------------------

class B10_ThePractice(Scene):
    def construct(self):
        total = DUR["B10"]

        header = SerifLabel("The move", INK, size=32)
        header.to_edge(UP, buff=0.9)

        step1_label = Text("1", font=DISPLAY, color=SLATE, font_size=36,
                           weight="MEDIUM")
        step1_text = Text(
            "Find the subject of destroyed / eliminated / sunset",
            font=SERIF, color=INK, font_size=30
        )
        step1_text.scale_to_fit_width(9.8)
        step1 = VGroup(step1_label, step1_text).arrange(RIGHT, buff=0.35)
        step1.move_to(UP * 0.6)

        step2_label = Text("2", font=DISPLAY, color=CRIMSON, font_size=36,
                           weight="MEDIUM")
        step2_text = Text(
            "Is it a function, not a person? Name what it covers.",
            font=SERIF, color=INK, font_size=30
        )
        step2_text.scale_to_fit_width(9.8)
        step2 = VGroup(step2_label, step2_text).arrange(RIGHT, buff=0.35)
        step2.move_to(DOWN * 0.6)

        anchor = SerifLabel("that is the analysis", CRIMSON, size=28)
        anchor.to_edge(DOWN, buff=0.75)

        self.play(FadeIn(header[0]), Create(header[1]), run_time=0.6)
        self.play(FadeIn(step1, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(step2, shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(anchor[0]), Create(anchor[1]), run_time=0.6)
        self.wait(max(0.5, total - 2.8))


# -----------------------------------------------------------------------
# B11 — RECAP / endcard. "The selection is the argument." + WRITING kicker.
# -----------------------------------------------------------------------

class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]

        t1 = Text("The selection", font=SERIF, color=INK,
                  font_size=62, weight="BOLD")
        t2 = Text("is the argument.", font=SERIF, color=INK,
                  font_size=62, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.4)
        u = Line(t2.get_corner(DL) + DOWN * 0.16,
                 t2.get_corner(DR) + DOWN * 0.16,
                 color=CRIMSON, stroke_width=2)
        kicker = Text("WRITING", font=DISPLAY, color=SLATE,
                      font_size=26, weight="MEDIUM")
        kicker.next_to(u, DOWN, buff=0.55)

        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(kicker, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.2))
