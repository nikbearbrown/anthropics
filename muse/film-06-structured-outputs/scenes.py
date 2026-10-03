"""scenes.py — Structured Outputs (Film 6). Manim visuals, house template."""
from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080

INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def check_mark(pos, scale=0.35, color=GREEN):
    """Two-Line check mark (checker's stub has no Checkmark)."""
    l1 = Line(LEFT * 0.2 * scale, ORIGIN, color=color, stroke_width=int(8 * scale / 0.35))
    l2 = Line(ORIGIN, RIGHT * 0.45 * scale + UP * 0.45 * scale, color=color,
              stroke_width=int(8 * scale / 0.35))
    return VGroup(l1, l2).move_to(pos)


def cross_mark(pos, scale=0.35, color=ACCENT):
    """Two crossing Lines = X mark."""
    w = int(8 * scale / 0.35)
    l1 = Line(LEFT * 0.35 * scale + DOWN * 0.35 * scale,
              RIGHT * 0.35 * scale + UP * 0.35 * scale, color=color, stroke_width=w)
    l2 = Line(LEFT * 0.35 * scale + UP * 0.35 * scale,
              RIGHT * 0.35 * scale + DOWN * 0.35 * scale, color=color, stroke_width=w)
    return VGroup(l1, l2).move_to(pos)


def bullet(pos, color=ACCENT):
    return Dot(pos, radius=0.09, color=color)


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.3, width=9.5, height=3.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.4)
    grp = VGroup(plate, t)
    if sub:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.35)
        grp.add(s)
    return grp


def term_card(term, gloss, pos):
    plate = RoundedRectangle(corner_radius=0.18, width=5.2, height=1.7,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(term, font_size=36, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = Text(gloss, font_size=24, color=GREY).move_to(plate.get_center() + DOWN * 0.4)
    return VGroup(plate, t, g)


def schema_card(pos, width=6.2, height=4.4):
    return RoundedRectangle(corner_radius=0.18, width=width, height=height,
                            fill_color=CARD, fill_opacity=1,
                            stroke_color=INK, stroke_width=3).move_to(pos)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("make the model fill in your form")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        form = RoundedRectangle(corner_radius=0.12, width=1.6, height=2.0,
                                color=BLUE, stroke_width=6, fill_opacity=0).shift(LEFT * 1.3 + DOWN * 0.4)
        form_line = Line(LEFT * 0.5 + DOWN * 0.4, RIGHT * 0.5 + DOWN * 0.4,
                         color=BLUE, stroke_width=5)
        brace_l = Text("{", font_size=80, color=ACCENT).shift(RIGHT * 1.3 + DOWN * 0.55)
        brace_r = Text("}", font_size=80, color=ACCENT).shift(RIGHT * 1.9 + DOWN * 0.55)
        self.play(Create(form), Create(form_line), Write(brace_l), Write(brace_r))
        self.play(form.animate.shift(RIGHT * 1.3), form_line.animate.shift(RIGHT * 1.3),
                  run_time=1.0)
        ring = Circle(radius=0.95, color=GREEN, stroke_width=6).move_to(DOWN * 0.4)
        self.play(Create(ring))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("JSON Schema", "a contract for the shape of an answer", LEFT * 3.1 + UP * 0.9),
            ("Constraint", "the contract forces the model's thinking", RIGHT * 3.1 + UP * 0.9),
            ("Rubric", "a schema that grades: score, feedback, categories", LEFT * 3.1 + DOWN * 1.1),
            ("Report", "the grade a human can read", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Why(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        blob = Circle(radius=1.05, color=GREY, fill_opacity=0.35, stroke_width=4).shift(LEFT * 3.9)
        blob_t = Text("a guess", font_size=36, color=INK).move_to(blob.get_center())
        self.play(FadeIn(blob), Write(blob_t))
        arrow = Arrow(LEFT * 2.4, LEFT * 1.0, color=INK, buff=0.15, stroke_width=6)
        self.play(Create(arrow))
        card = schema_card(RIGHT * 2.2, width=4.6, height=3.4)
        card_t = Text("exactly these fields", font_size=30, color=INK).move_to(card.get_center() + UP * 0.8)
        field1 = Line(LEFT * 1.6, RIGHT * 1.6, color=GREY, stroke_width=4).move_to(card.get_center())
        field2 = Line(LEFT * 1.6, RIGHT * 1.6, color=GREY, stroke_width=4).move_to(card.get_center() + DOWN * 0.6)
        self.play(FadeIn(card), Write(card_t))
        self.play(Create(field1), Create(field2))
        cap = Text("it has to actually score", font_size=30, color=INK).next_to(card, DOWN, buff=0.35)
        self.play(Write(cap))
        self.play(FadeIn(check_mark(card.get_center() + DOWN * 1.45), scale=0.8))
        self.wait(1.2)


class M04_B02Rubric(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the rubric as a schema", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        card = schema_card(DOWN * 0.4, width=7.2, height=4.6)
        self.play(FadeIn(card))
        rows = [
            ("score / 100", 1.4),
            ("grammar: mark + comment", 0.45),
            ("vocabulary: mark + comment", -0.5),
            ("feedback: for the student", -1.45),
        ]
        for label, y in rows:
            d = bullet(LEFT * 3.0 + UP * y + DOWN * 0.4)
            t = Text(label, font_size=32, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
        cap = Text("the schema is the test plan", font_size=30, color=GREY).next_to(card, DOWN, buff=0.3)
        self.play(Write(cap))
        self.wait(1.2)


class M05_B03Save(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("write it once", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        base = schema_card(LEFT * 3.2, width=4.2, height=3.2)
        base_t = Text("rubric", font_size=34, color=INK).move_to(base.get_center())
        self.play(FadeIn(base), Write(base_t))
        copies = []
        for i in range(3):
            c = schema_card(LEFT * 0.2 + RIGHT * i * 1.9, width=3.4, height=2.7)
            ct = Text("rubric", font_size=28, color=INK).move_to(c.get_center())
            arrow = Arrow(base.get_right(), c.get_left(), color=GREY, buff=0.1, stroke_width=5)
            self.play(Create(arrow), FadeIn(c), Write(ct))
            self.play(FadeIn(check_mark(c.get_center() + DOWN * 1.0), scale=0.6))
            copies.append(c)
        self.wait(1.2)


class M06_B04Challenge(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        ch = RoundedRectangle(corner_radius=0.2, width=5.0, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=ACCENT, stroke_width=3).shift(LEFT * 3.0 + UP * 0.3)
        ch_t = Text("challenge", font_size=36, color=ACCENT).move_to(ch.get_center() + UP * 0.7)
        ch_line = Text("a Japanese sentence,\na tricky grammar point", font_size=28,
                       color=INK).move_to(ch.get_center() + DOWN * 0.3)
        self.play(FadeIn(ch), Write(ch_t))
        self.play(Write(ch_line))
        arrow = Arrow(LEFT * 0.4, RIGHT * 1.6, color=INK, buff=0.15, stroke_width=6)
        self.play(Create(arrow))
        at = RoundedRectangle(corner_radius=0.2, width=5.0, height=2.6,
                              fill_color=CARD, fill_opacity=1,
                              stroke_color=BLUE, stroke_width=3).shift(RIGHT * 3.4 + UP * 0.3)
        at_t = Text("attempt", font_size=36, color=BLUE).move_to(at.get_center() + UP * 0.7)
        self.play(FadeIn(at), Write(at_t))
        l1 = Text("translation", font_size=28, color=INK).move_to(at.get_center() + DOWN * 0.1)
        l2 = Text("grammar explanation", font_size=28, color=INK).move_to(at.get_center() + DOWN * 0.6)
        d1 = bullet(l1.get_left() + LEFT * 0.25, color=BLUE)
        d2 = bullet(l2.get_left() + LEFT * 0.25, color=BLUE)
        self.play(FadeIn(d1), Write(l1))
        self.play(FadeIn(d2), Write(l2))
        self.wait(1.2)


class M07_B05Attempt(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.2, width=7.6, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3)
        self.play(FadeIn(card))
        t1 = Text("the translation reads fine", font_size=34, color=INK).move_to(card.get_center() + UP * 0.9)
        t2 = Text("the grammar read seems right", font_size=34, color=INK).move_to(card.get_center())
        self.play(Write(t1))
        self.play(Write(t2))
        ring = Circle(radius=1.1, color=ACCENT, stroke_width=6).move_to(t2.get_center())
        self.play(Create(ring))
        cap = Text("looks fine. That is the problem.", font_size=32, color=INK).next_to(card, DOWN, buff=0.35)
        self.play(Write(cap), FadeIn(bullet(cap.get_left() + LEFT * 0.3, color=ACCENT)))
        self.wait(1.2)


class M08_B06Graded(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = schema_card(ORIGIN, width=7.6, height=5.0)
        self.play(FadeIn(card))
        score = Text("70/100", font_size=64, color=ACCENT).move_to(card.get_center() + UP * 1.5)
        self.play(Write(score))
        rows = [
            ("grammar: marked down — wrong particle", 0.5),
            ("vocabulary: fine", -0.4),
            ("feedback: for the student", -1.3),
        ]
        for label, y in rows:
            d = bullet(LEFT * 3.3 + UP * y)
            t = Text(label, font_size=30, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
        self.wait(1.2)


class M09_B07Read(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        score = Text("70/100", font_size=88, color=ACCENT).shift(LEFT * 3.6)
        self.play(Write(score))
        row_plate = RoundedRectangle(corner_radius=0.16, width=5.6, height=1.5,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=ACCENT, stroke_width=4).shift(RIGHT * 2.4 + UP * 0.6)
        row_t = Text("grammar: wrong particle\nnamed and corrected", font_size=28,
                     color=INK).move_to(row_plate.get_center())
        self.play(FadeIn(row_plate), Write(row_t))
        arrow = Arrow(LEFT * 1.6 + UP * 0.4, row_plate.get_left(), color=INK,
                      buff=0.15, stroke_width=6)
        self.play(Create(arrow))
        cap = Text("you know exactly where the thirty went", font_size=30, color=INK).shift(DOWN * 2.6)
        d = bullet(cap.get_left() + LEFT * 0.3, color=GREEN)
        self.play(Write(cap), FadeIn(d))
        self.wait(1.2)


class M10_B08Feed(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        jcard = RoundedRectangle(corner_radius=0.18, width=4.2, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).shift(LEFT * 3.4)
        jt = Text("graded JSON", font_size=32, color=INK).move_to(jcard.get_center() + UP * 1.0)
        jscore = Text("70/100", font_size=40, color=ACCENT).move_to(jcard.get_center())
        self.play(FadeIn(jcard), Write(jt))
        self.play(Write(jscore))
        arrow = Arrow(LEFT * 1.1, RIGHT * 1.1, color=INK, buff=0.15, stroke_width=6)
        self.play(Create(arrow))
        self.play(FadeIn(check_mark(ORIGIN + DOWN * 1.6), scale=0.7))
        rcard = RoundedRectangle(corner_radius=0.18, width=4.2, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=3).shift(RIGHT * 3.4)
        rt = Text("report", font_size=32, color=BLUE).move_to(rcard.get_center() + UP * 1.0)
        rl1 = Line(LEFT * 1.4, RIGHT * 1.4, color=GREY, stroke_width=4).move_to(rcard.get_center())
        rl2 = Line(LEFT * 1.4, RIGHT * 1.4, color=GREY, stroke_width=4).move_to(rcard.get_center() + DOWN * 0.6)
        self.play(FadeIn(rcard), Write(rt))
        self.play(Create(rl1), Create(rl2))
        cap = Text("the data survives the trip", font_size=30, color=INK).shift(DOWN * 2.7)
        self.play(Write(cap), FadeIn(bullet(cap.get_left() + LEFT * 0.3, color=BLUE)))
        self.wait(1.2)


class M11_B09Report(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        page = RoundedRectangle(corner_radius=0.2, width=6.6, height=5.2,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3)
        self.play(FadeIn(page))
        hdr = Text("70/100", font_size=52, color=ACCENT).move_to(page.get_center() + UP * 1.9)
        self.play(Write(hdr))
        secs = [
            ("grammar — marked down", -0.2),
            ("vocabulary — fine", -0.9),
            ("feedback, for the student", -1.6),
        ]
        for label, y in secs:
            d = bullet(LEFT * 2.8 + UP * (y + 0.6) + DOWN * 0.2, color=BLUE)
            t = Text(label, font_size=28, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
        ring = Ellipse(width=7.4, height=6.0, color=GREEN, stroke_width=5, fill_opacity=0)
        self.play(Create(ring))
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap
        plate = RoundedRectangle(corner_radius=0.2, width=9.4, height=4.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3)
        head = Text("recap", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head), FadeIn(plate))
        recaps = ["a schema is a contract: it constrains reasoning",
                  "the grader loop: challenge, attempt, graded JSON",
                  "feed the JSON back: a report a human can read"]
        y = 1.0
        recap_grp = VGroup()
        for r in recaps:
            d = bullet(LEFT * 4.1 + UP * y)
            t = Text(r, font_size=30, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
            recap_grp.add(d, t)
            y -= 1.3
        self.wait(0.8)
        self.play(FadeOut(plate), FadeOut(recap_grp), FadeOut(head))
        # Phase 2: your turn
        card = title_card("your turn", "One tiny schema, three fields. Something you wrote this week.")
        self.play(FadeIn(card, shift=UP * 0.3))
        q = Text("When the format stops being your problem,\nthe content finally is.", font_size=30,
                 color=GREY).next_to(card, DOWN, buff=0.4)
        pencil = Line(LEFT * 0.5, RIGHT * 0.5, color=ACCENT, stroke_width=8).next_to(q, DOWN, buff=0.3)
        self.play(Write(q), Create(pencil))
        self.wait(0.8)
        self.play(FadeOut(card), FadeOut(q), FadeOut(pencil))
        # Phase 3: outro
        outro = title_card("Structured Outputs", "@NikBearBrown")
        self.play(FadeIn(outro, shift=DOWN * 0.3))
        nxt = Text("Next: Muse in Code", font_size=34, color=BLUE).next_to(outro, DOWN, buff=0.4)
        bar = Line(LEFT * 1.5, RIGHT * 1.5, color=BLUE, stroke_width=6).next_to(nxt, DOWN, buff=0.25)
        self.play(Write(nxt), Create(bar))
        self.wait(1.2)
