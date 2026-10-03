"""scenes.py — Grounded Answers (Film 5). Manim visuals, house template."""
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


def chip(label, pos, width=3.4):
    """A small rounded chip for question facets."""
    plate = RoundedRectangle(corner_radius=0.22, width=width, height=0.9,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(label, font_size=30, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


def answer_row(label, pos, width=6.2, color=GREY, marked=False, good=False):
    plate = RoundedRectangle(corner_radius=0.14, width=width, height=0.85,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=color, stroke_width=2).move_to(pos)
    if marked:
        m = check_mark(plate.get_left() + RIGHT * 0.4) if good else cross_mark(
            plate.get_left() + RIGHT * 0.4, color=GREY)
    else:
        m = bullet(plate.get_left() + RIGHT * 0.4, color=color)
    t = Text(label, font_size=30, color=INK).next_to(m, RIGHT, buff=0.25)
    return VGroup(plate, m, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("what the model knows", "vs what it can look up")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        book = Rectangle(width=0.9, height=1.2, color=BLUE, stroke_width=6).shift(
            LEFT * 2.4 + DOWN * 0.2)
        book_spine = Line(book.get_top() + RIGHT * 0.25, book.get_bottom() + RIGHT * 0.25,
                          color=BLUE, stroke_width=4)
        globe = Circle(radius=0.7, color=GREEN, stroke_width=6).shift(RIGHT * 2.4 + DOWN * 0.2)
        mag = Circle(radius=0.35, color=GREEN, stroke_width=5).shift(
            RIGHT * 2.4 + DOWN * 0.2 + RIGHT * 0.55 + UP * 0.55)
        mag_handle = Line(mag.get_corner(DR), mag.get_corner(DR) + RIGHT * 0.45 + DOWN * 0.45,
                          color=GREEN, stroke_width=5)
        self.play(Create(book), Create(book_spine), Create(globe), Create(mag), Create(mag_handle))
        self.play(book.animate.shift(RIGHT * 2.4), book_spine.animate.shift(RIGHT * 2.4),
                  globe.animate.shift(LEFT * 2.4), mag.animate.shift(LEFT * 2.4),
                  mag_handle.animate.shift(LEFT * 2.4), run_time=1.2)
        ring = Circle(radius=0.9, color=ACCENT, stroke_width=6).move_to(ORIGIN + DOWN * 0.2)
        self.play(Create(ring))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("Grounding", "search the web before answering", LEFT * 3.1 + UP * 0.9),
            ("Freshness", "how new the facts are", RIGHT * 3.1 + UP * 0.9),
            ("Cost per query", "what each search is billed at", LEFT * 3.1 + DOWN * 1.1),
            ("Blocked page", "a site the search can't get into", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Question(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the test question", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        chips = ["control arms", "Dodge Grand Caravan", "Canada"]
        y = 0.9
        for lab in chips:
            c = chip(lab, LEFT * 2.2 + UP * y, width=4.6)
            self.play(FadeIn(c, shift=LEFT * 0.3))
            y -= 1.4
        badge = Circle(radius=0.75, color=ACCENT, fill_opacity=0.9, stroke_width=0).shift(
            RIGHT * 3.4 + UP * 0.2)
        badge_t = Text("x2", font_size=52, color=CARD).move_to(badge.get_center())
        self.play(FadeIn(badge, scale=0.6), Write(badge_t))
        self.wait(1.2)


class M04_B02Ungrounded(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        q = chip("the question", LEFT * 4.4 + UP * 1.2, width=3.6)
        self.play(FadeIn(q))
        arrow = Arrow(LEFT * 2.2 + UP * 1.2, RIGHT * 0.2 + UP * 1.2, color=INK, buff=0.1,
                      stroke_width=6)
        self.play(Create(arrow))
        rows = ["generic part info", "no current prices", "no stores"]
        y = 0.2
        for lab in rows:
            r = answer_row(lab, RIGHT * 1.8 + UP * y, width=6.2, color=GREY)
            self.play(FadeIn(r, shift=LEFT * 0.3))
            y -= 1.25
        tag = Text("from memory only", font_size=30, color=GREY).shift(DOWN * 2.9)
        tagline = Line(LEFT * 1.4, RIGHT * 1.4, color=GREY, stroke_width=4).shift(DOWN * 2.35)
        self.play(Create(tagline), FadeIn(tag))
        self.wait(1.2)


class M05_B03Grounded(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        q = chip("the question", LEFT * 4.4 + UP * 2.2, width=3.6)
        self.play(FadeIn(q))
        for i in range(3):
            a = Arrow(LEFT * 2.2 + UP * (2.2 - i * 0.5), RIGHT * 0.2 + UP * (1.2 - i * 0.9),
                      color=BLUE, buff=0.1, stroke_width=5)
            self.play(Create(a), run_time=0.4)
        rows = ["current prices", "Canadian retailers", "shipping times"]
        y = 1.2
        for lab in rows:
            r = answer_row(lab, RIGHT * 1.8 + UP * y, width=6.2, color=GREEN,
                           marked=True, good=True)
            self.play(FadeIn(r, shift=LEFT * 0.3))
            y -= 1.25
        tag = Text("fresh", font_size=34, color=GREEN).shift(DOWN * 2.6)
        ring = Circle(radius=0.7, color=GREEN, stroke_width=5).move_to(tag.get_center())
        self.play(Create(ring), FadeIn(tag))
        self.wait(1.2)


class M06_B04SideBySide(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("side by side", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        lab_l = Text("ungrounded", font_size=32, color=GREY).shift(LEFT * 3.6 + UP * 1.7)
        lab_r = Text("grounded", font_size=32, color=GREEN).shift(RIGHT * 3.6 + UP * 1.7)
        self.play(FadeIn(lab_l), FadeIn(lab_r))
        divider = Arrow(LEFT * 0.6 + UP * 0.2, RIGHT * 0.6 + UP * 0.2, color=INK,
                        buff=0.1, stroke_width=6)
        self.play(Create(divider))
        pairs = [("explains the part", "shows the buying"),
                 ("no prices", "current prices"),
                 ("no stores", "Canadian retailers")]
        y = 0.6
        for left_lab, right_lab in pairs:
            l = answer_row(left_lab, LEFT * 3.6 + UP * y, width=4.8, color=GREY)
            r = answer_row(right_lab, RIGHT * 3.6 + UP * y, width=4.8, color=GREEN,
                           marked=True, good=True)
            m = cross_mark(l[1].get_center(), scale=0.3, color=GREY)
            l2 = VGroup(l[0], m, l[2])
            self.play(FadeIn(l2, shift=RIGHT * 0.2), FadeIn(r, shift=LEFT * 0.2))
            y -= 1.3
        self.wait(1.2)


class M07_B05Added(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("what grounding added", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        labels = ["current prices", "Canadian retailers", "shipping reality"]
        y = 1.4
        for lab in labels:
            r = answer_row(lab, UP * y, width=7.0, color=GREEN, marked=True, good=True)
            d = bullet(DOWN * 2.6 + LEFT * (y * 1.2), color=BLUE)
            self.play(FadeIn(r, shift=LEFT * 0.3), FadeIn(d))
            y -= 1.6
        self.wait(1.2)


class M08_B06Blocked(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        globe = Circle(radius=1.1, color=BLUE, stroke_width=6).shift(LEFT * 3.8 + UP * 0.4)
        self.play(Create(globe))
        wall = VGroup(*[Rectangle(width=0.55, height=2.2, fill_color=GREY, fill_opacity=0.85,
                                  stroke_width=0).shift(LEFT * 3.8 + LEFT * (i - 1) * 0.6 + UP * 0.4)
                        for i in range(3)])
        self.play(FadeIn(wall))
        pages = ["product page A", "product page B", "product page C"]
        y = 1.9
        for lab in pages:
            p = answer_row(lab, RIGHT * 2.4 + UP * y, width=5.6, color=ACCENT,
                           marked=True, good=False)
            stamp = Text("blocked", font_size=24, color=ACCENT).next_to(p, RIGHT, buff=0.2)
            self.play(FadeIn(p, shift=LEFT * 0.3), FadeIn(stamp))
            y -= 1.3
        hole = Text("holes remain", font_size=32, color=GREY).shift(DOWN * 2.7)
        plate = RoundedRectangle(corner_radius=0.18, width=4.6, height=1.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=GREY, stroke_width=2).move_to(hole.get_center())
        self.play(FadeIn(plate), FadeIn(hole))
        self.wait(1.2)


class M09_B07Price(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the price", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        slot = RoundedRectangle(corner_radius=0.2, width=5.4, height=1.1,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).shift(UP * 0.9)
        slot_t = Text("billed per 1k queries", font_size=34, color=INK).move_to(
            slot.get_center())
        self.play(FadeIn(slot), Write(slot_t))
        y = 0.0
        for i in range(4):
            coin = Circle(radius=0.32, color=ACCENT, fill_opacity=0.85,
                          stroke_width=0).shift(RIGHT * (i - 1.5) * 0.85 + UP * 0.9)
            self.play(FadeIn(coin, shift=DOWN * 0.5), run_time=0.4)
        token_lab = Text("token counter", font_size=28, color=GREY).shift(DOWN * 1.5)
        x1 = cross_mark(token_lab.get_left() + LEFT * 0.5, scale=0.35, color=GREY)
        self.play(FadeIn(token_lab), FadeIn(x1))
        note = Text("not billed by the token", font_size=30, color=INK).shift(DOWN * 2.6)
        underline = Line(note.get_left(), note.get_right(), color=ACCENT, stroke_width=4
                         ).next_to(note, DOWN, buff=0.15)
        self.play(FadeIn(note), Create(underline))
        self.wait(1.2)


class M10_B08When(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("when to ground", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rail = RoundedRectangle(corner_radius=0.45, width=3.2, height=1.1,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).shift(UP * 1.4)
        knob = Circle(radius=0.42, color=GREY, fill_opacity=1, stroke_width=0).move_to(
            rail.get_left() + RIGHT * 0.55)
        self.play(FadeIn(rail), FadeIn(knob))
        path_l = chip("timeless question", LEFT * 3.4 + DOWN * 0.6, width=4.4)
        tag_l = Text("memory", font_size=28, color=GREY).next_to(path_l, DOWN, buff=0.2)
        path_r = chip("fresh facts needed", RIGHT * 3.4 + DOWN * 0.6, width=4.4)
        tag_r = Text("ground it", font_size=28, color=GREEN).next_to(path_r, DOWN, buff=0.2)
        self.play(FadeIn(path_l), FadeIn(tag_l))
        ptr = Triangle(color=ACCENT, fill_opacity=1, stroke_width=0).scale(0.3).rotate(
            -90 * DEGREES).next_to(path_l, UP, buff=0.25)
        self.play(FadeIn(ptr))
        self.play(FadeOut(ptr), FadeIn(path_r), FadeIn(tag_r))
        knob2 = Circle(radius=0.42, color=GREEN, fill_opacity=1, stroke_width=0).move_to(
            rail.get_right() + LEFT * 0.55)
        self.play(Transform(knob, knob2))
        ptr2 = Triangle(color=ACCENT, fill_opacity=1, stroke_width=0).scale(0.3).rotate(
            -90 * DEGREES).next_to(path_r, UP, buff=0.25)
        self.play(FadeIn(ptr2))
        self.wait(1.2)


class M11_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        recap = title_card("recap")
        self.play(FadeIn(recap, shift=DOWN * 0.3))
        lines = ["memory explains, grounding informs",
                 "adds facts, can't beat blocked pages",
                 "billed per search — use it when fresh"]
        shown = [recap]
        y = 0.55
        for ln in lines:
            t = Text(ln, font_size=30, color=INK).shift(DOWN * 2.6 + UP * (y + 2.6))
            d = bullet(LEFT * 5.9 + UP * y, color=BLUE)
            self.play(Write(t), FadeIn(d))
            shown += [t, d]
            y -= 0.85
        self.play(*[FadeOut(m) for m in shown])
        your = title_card("your turn", "ask it twice")
        self.play(FadeIn(your, shift=DOWN * 0.3))
        prompt = Text("Pick one fresh question.\nAsk it ungrounded. Ask it grounded.",
                      font_size=32, color=INK, line_spacing=0.6).shift(DOWN * 2.6)
        self.play(Write(prompt))
        self.play(FadeOut(your), FadeOut(prompt))
        outro = title_card("Grounded Answers", "@NikBearBrown")
        nxt = Text("Next: Structured Outputs", font_size=36, color=ACCENT).shift(DOWN * 2.6)
        self.play(FadeIn(outro, shift=DOWN * 0.3), FadeIn(nxt))
        self.wait(1.2)
