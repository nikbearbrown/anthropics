"""scenes.py — Capstone: Ship a Full-Stack App (Film 11). Manim visuals, house template."""
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


def file_card(label, pos, width=3.4, height=1.6):
    plate = RoundedRectangle(corner_radius=0.16, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3).move_to(pos)
    t = Text(label, font_size=38, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


def mini_card(label, pos, width=2.8, height=0.9):
    plate = RoundedRectangle(corner_radius=0.12, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(label, font_size=30, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("from idea to running containers")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        dot = Dot(LEFT * 4.5 + DOWN * 2.4, radius=0.28, color=ACCENT)
        lab = Text("idea", font_size=30, color=INK).next_to(dot, DOWN, buff=0.15)
        self.play(FadeIn(dot, scale=1.4), Write(lab))
        box = Rectangle(width=2.0, height=1.4, color=BLUE, stroke_width=4,
                        fill_color=CARD, fill_opacity=1).move_to(RIGHT * 4.5 + DOWN * 2.4)
        boxlab = Text("container", font_size=30, color=INK).next_to(box, DOWN, buff=0.15)
        self.play(Transform(dot, box), FadeOut(lab), run_time=0.8)
        self.play(Write(boxlab))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        terms = [
            ("Goal", "decomposes, drives the build"),
            ("Stack", "Go, SQLite, React"),
            ("Compose", "one file, every service"),
            ("Endpoint", "a URL the backend answers"),
        ]
        pos = [LEFT * 4.8 + UP * 0.6, RIGHT * 4.8 + UP * 0.6,
               LEFT * 4.8 + DOWN * 1.6, RIGHT * 4.8 + DOWN * 1.6]
        for (term, gloss), p in zip(terms, pos):
            c = term_card(term, gloss, p)
            d = bullet(p + UP * 1.05, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Doc(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("act one: the plan", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        doc = file_card("backend doc", LEFT * 3.4 + DOWN * 0.4, width=3.6, height=2.0)
        self.play(FadeIn(doc, shift=RIGHT * 0.3))
        stamp = file_card("contract", RIGHT * 3.4 + DOWN * 0.4, width=3.6, height=2.0)
        arr = Arrow(LEFT * 1.2 + DOWN * 0.4, RIGHT * 1.2 + DOWN * 0.4,
                    color=ACCENT, stroke_width=8, buff=0.2)
        self.play(Create(arr))
        self.play(FadeIn(stamp, shift=LEFT * 0.3))
        chk = check_mark(RIGHT * 3.4 + DOWN * 0.4 + RIGHT * 1.1 + UP * 0.6)
        self.play(Create(chk))
        self.wait(1.2)


class M04_B02Stack(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the stack", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        labels = ["Go", "SQLite", "one VM"]
        xs = [-3.4, 0.0, 3.4]
        for lab, x in zip(labels, xs):
            c = mini_card(lab, RIGHT * x + DOWN * 0.6, width=3.0, height=1.1)
            d = bullet(RIGHT * x + DOWN * 1.5, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.25), FadeIn(d))
        banner = Text("no bill", font_size=36, color=GREEN).move_to(DOWN * 2.4)
        frame = SurroundingRectangle(banner, color=GREEN, buff=0.25, corner_radius=0.15)
        self.play(Write(banner), Create(frame))
        self.wait(1.2)


class M05_B03Sql(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("raw SQL — deliberately", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        card = file_card("raw SQL", LEFT * 3.6, width=3.2, height=1.6)
        self.play(FadeIn(card, shift=RIGHT * 0.3))
        for i in range(4):
            glyph = Line(LEFT * 0.1 + DOWN * (0.35 * i), RIGHT * 2.2 + DOWN * (0.35 * i),
                         color=GREY, stroke_width=6).move_to(RIGHT * 1.6 + DOWN * (0.5 * i))
            d = bullet(RIGHT * 0.2 + DOWN * (0.5 * i), color=ACCENT)
            self.play(Create(glyph), FadeIn(d), run_time=0.35)
        self.wait(1.2)


class M06_B04Goal(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the goal feature", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        goal = Dot(UP * 1.4, radius=0.3, color=ACCENT)
        glab = Text("goal", font_size=32, color=INK).next_to(goal, UP, buff=0.15)
        self.play(FadeIn(goal, scale=1.5), Write(glab))
        prev = goal
        for i in range(4):
            step = Dot(LEFT * (2.7 - 1.8 * i) + DOWN * 0.9, radius=0.18, color=BLUE)
            arr = Arrow(prev.get_center(), step.get_center(), color=GREY,
                        stroke_width=5, buff=0.25)
            self.play(Create(arr), FadeIn(step, scale=1.3), run_time=0.4)
            prev = step
        self.wait(1.2)


class M07_B05Decompose(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("watch the decomposition", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        root = Dot(UP * 1.8, radius=0.25, color=ACCENT)
        rlab = Text("goal", font_size=28, color=INK).next_to(root, UP, buff=0.12)
        self.play(FadeIn(root, scale=1.4), Write(rlab))
        branches = ["endpoints", "tables", "auth", "posts"]
        xs = [-4.2, -1.4, 1.4, 4.2]
        for lab, x in zip(branches, xs):
            node = Dot(RIGHT * x + DOWN * 0.6, radius=0.16, color=BLUE)
            arr = Arrow(root.get_center(), node.get_center(), color=GREY,
                        stroke_width=4, buff=0.2)
            t = Text(lab, font_size=26, color=INK).next_to(node, DOWN, buff=0.15)
            self.play(Create(arr), FadeIn(node, scale=1.3), Write(t), run_time=0.4)
            chk = check_mark(node.get_center() + UP * 0.55, scale=0.22)
            self.play(Create(chk), run_time=0.25)
        self.wait(1.2)


class M08_B06Build(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the build runs", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        plate = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(LEFT * 1.8 + DOWN * 0.2)
        self.play(FadeIn(plate, shift=RIGHT * 0.3))
        for i in range(5):
            glyph = Line(ORIGIN, RIGHT * (3.4 - 0.4 * i), color=BLUE,
                         stroke_width=7).move_to(plate.get_center() + UP * (1.0 - 0.5 * i) + LEFT * 0.4)
            self.play(Create(glyph), run_time=0.3)
        lens = file_card("you are the judgment", RIGHT * 4.4 + DOWN * 0.2, width=3.4, height=1.4)
        self.play(FadeIn(lens, shift=LEFT * 0.3))
        self.wait(1.2)


class M09_B07Mvp(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        mvp = file_card("MVP", UP * 0.6, width=3.6, height=1.8)
        self.play(FadeIn(mvp, shift=DOWN * 0.4))
        chk = check_mark(UP * 0.6 + RIGHT * 1.3 + UP * 0.5, scale=0.4)
        self.play(Create(chk))
        labels = ["register", "post", "database"]
        xs = [-3.2, 0.0, 3.2]
        for lab, x in zip(labels, xs):
            d = Dot(RIGHT * x + DOWN * 1.8, radius=0.2, color=GREY)
            t = Text(lab, font_size=28, color=INK).next_to(d, DOWN, buff=0.15)
            self.play(FadeIn(d, scale=1.3), Write(t), run_time=0.35)
            d2 = Dot(RIGHT * x + DOWN * 1.8, radius=0.2, color=GREEN)
            self.play(Transform(d, d2), run_time=0.3)
        self.wait(1.2)


class M10_B08Compose(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("Docker Compose", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        frame = RoundedRectangle(corner_radius=0.25, width=10.4, height=2.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(DOWN * 0.4)
        flab = Text("compose", font_size=32, color=GREY).move_to(frame.get_center() + UP * 0.95)
        self.play(FadeIn(frame, shift=UP * 0.3), Write(flab))
        services = ["backend", "frontend", "MinIO"]
        xs = [-3.4, 0.0, 3.4]
        for lab, x in zip(services, xs):
            c = mini_card(lab, RIGHT * x + DOWN * 0.55, width=3.0, height=1.0)
            d = bullet(RIGHT * x + DOWN * 1.35, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.25), FadeIn(d), run_time=0.4)
        self.wait(1.2)


class M11_B09React(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("wired to real endpoints", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        left = file_card("React", LEFT * 3.4 + DOWN * 0.3, width=3.2, height=1.6)
        right = file_card("endpoints", RIGHT * 3.4 + DOWN * 0.3, width=3.2, height=1.6)
        self.play(FadeIn(left, shift=RIGHT * 0.3), FadeIn(right, shift=LEFT * 0.3))
        arr = Arrow(LEFT * 1.5 + DOWN * 0.3, RIGHT * 1.5 + DOWN * 0.3,
                    color=ACCENT, stroke_width=9, buff=0.25)
        self.play(Create(arr))
        for i in range(3):
            pulse = Dot(DOWN * (1.9 + 0.45 * i), radius=0.12, color=GREEN)
            self.play(FadeIn(pulse, scale=1.5), run_time=0.3)
        self.wait(1.2)


class M12_B10Rough(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the demo", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        reg = mini_card("register", LEFT * 2.2 + UP * 0.3, width=3.0, height=1.0)
        post = mini_card("post", RIGHT * 2.2 + UP * 0.3, width=3.0, height=1.0)
        self.play(FadeIn(reg, shift=UP * 0.25))
        self.play(Create(check_mark(LEFT * 2.2 + UP * 0.3 + RIGHT * 1.1, scale=0.25)))
        self.play(FadeIn(post, shift=UP * 0.25))
        self.play(Create(check_mark(RIGHT * 2.2 + UP * 0.3 + RIGHT * 1.1, scale=0.25)))
        rough = RoundedRectangle(corner_radius=0.18, width=7.0, height=1.4,
                                 fill_color=CARD, fill_opacity=0.55,
                                 stroke_color=GREY, stroke_width=2).move_to(DOWN * 1.9)
        rlab = Text("rough edges: styling, edge cases", font_size=30, color=GREY).move_to(rough.get_center())
        self.play(FadeIn(rough), Write(rlab))
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap — 3 lines, one per act
        recap = title_card("recap")
        self.play(FadeIn(recap, shift=DOWN * 0.3))
        lines = [
            "act one: the plan — doc, boring stack, raw SQL",
            "act two: the build — goal decomposes, MVP stands",
            "act three: the ship — compose, real endpoints",
        ]
        phase1 = VGroup(recap)
        for i, ln in enumerate(lines):
            d = bullet(LEFT * 4.4 + UP * (0.4 - 0.55 * i), color=ACCENT)
            t = Text(ln, font_size=30, color=INK).next_to(d, RIGHT, buff=0.2)
            row = VGroup(d, t).move_to(DOWN * (1.6 - 0.55 * i))
            self.play(FadeIn(d, scale=1.3), Write(t), run_time=0.5)
            phase1.add(row)
        self.wait(0.6)
        self.play(FadeOut(phase1))
        # Phase 2: your turn
        turn = title_card("your turn", "one backend doc. then the stack plan.")
        self.play(FadeIn(turn, shift=DOWN * 0.3))
        pen = bullet(DOWN * 2.2, color=BLUE)
        self.play(FadeIn(pen, scale=1.5))
        turn_g = VGroup(turn, pen)
        self.wait(0.6)
        self.play(FadeOut(turn_g))
        # Phase 3: outro
        out = title_card("@NikBearBrown", "Next film: Muse the Agent")
        self.play(FadeIn(out, shift=DOWN * 0.3))
        self.wait(1.2)
