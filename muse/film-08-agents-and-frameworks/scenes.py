"""scenes.py — Agents and Frameworks (Film 8). Manim visuals, house template."""
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


def bullet(pos, color=ACCENT):
    return Dot(pos, radius=0.09, color=color)


def title_card(title, sub=None, width=9.5, height=3.2, tsize=54):
    plate = RoundedRectangle(corner_radius=0.3, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=tsize, color=INK).move_to(plate.get_center() + UP * 0.4)
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


def small_card(label, pos, width=2.9, height=1.0, tsize=30):
    plate = RoundedRectangle(corner_radius=0.14, width=width, height=height,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(label, font_size=tsize, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("drop Muse into tools you already use")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        labels = ["SDKs", "frameworks", "a harness"]
        x = -3.2
        for lab in labels:
            c = small_card(lab, DOWN * 2.2 + RIGHT * x)
            d = bullet(DOWN * 2.2 + RIGHT * x + UP * 0.95, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
            x += 3.2
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("Agent SDK", "runs an agentic loop for you", LEFT * 3.1 + UP * 0.9),
            ("Framework", "chains, memory, tools", RIGHT * 3.1 + UP * 0.9),
            ("Harness", "the cockpit around the model", LEFT * 3.1 + DOWN * 1.1),
            ("Wrapper", "a script that adapts one tool", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Sdk(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = small_card("the agent SDK", UP * 2.2, width=4.2, height=1.1, tsize=34)
        self.play(FadeIn(head, shift=DOWN * 0.2))
        nodes = ["plan", "call tools", "iterate"]
        xs = [-3.4, 0.0, 3.4]
        prev = None
        for lab, x in zip(nodes, xs):
            c = small_card(lab, RIGHT * x + DOWN * 0.3, width=2.6, height=1.0, tsize=30)
            self.play(FadeIn(c, shift=RIGHT * 0.2))
            if prev is not None:
                a = Arrow(prev.get_right(), c.get_left(), color=INK, buff=0.15, stroke_width=6)
                self.play(Create(a))
            prev = c
        self.wait(1.2)


class M04_B02Task(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        term = small_card("tic-tac-toe, in Ruby", UP * 2.2, width=5.2, height=1.1, tsize=34)
        self.play(FadeIn(term, shift=DOWN * 0.2))
        rows = ["game state", "win checking", "game loop"]
        y = 0.9
        for lab in rows:
            plate = RoundedRectangle(corner_radius=0.14, width=5.6, height=0.85,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2).move_to(DOWN * 0.1 + UP * y)
            d = bullet(plate.get_left() + RIGHT * 0.4)
            t = Text(lab, font_size=30, color=INK).next_to(d, RIGHT, buff=0.25)
            self.play(FadeIn(VGroup(plate, d, t), shift=LEFT * 0.3))
            y -= 1.25
        self.wait(1.2)


class M05_B03Result(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # tic-tac-toe grid
        v1 = Line(UP * 1.5 + LEFT * 0.8, DOWN * 1.5 + LEFT * 0.8, color=INK, stroke_width=6)
        v2 = Line(UP * 1.5 + RIGHT * 0.8, DOWN * 1.5 + RIGHT * 0.8, color=INK, stroke_width=6)
        h1 = Line(LEFT * 2.0 + UP * 0.5, RIGHT * 2.0 + UP * 0.5, color=INK, stroke_width=6)
        h2 = Line(LEFT * 2.0 + DOWN * 0.5, RIGHT * 2.0 + DOWN * 0.5, color=INK, stroke_width=6)
        self.play(Create(v1), Create(v2), Create(h1), Create(h2))
        marks = [
            ("X", LEFT * 1.4 + UP * 1.0, BLUE),
            ("O", RIGHT * 0.0 + UP * 1.0, ACCENT),
            ("X", LEFT * 1.4 + DOWN * 0.0, BLUE),
            ("O", RIGHT * 1.4 + DOWN * 1.0, ACCENT),
            ("X", LEFT * 1.4 + DOWN * 1.0, BLUE),
        ]
        for ch, pos, col in marks:
            m = Text(ch, font_size=72, color=col).move_to(pos)
            self.play(FadeIn(m, scale=1.4))
        chk = check_mark(RIGHT * 3.6 + UP * 0.5, scale=0.5)
        cap = Text("a finished game, from a description", font_size=28,
                   color=GREY).move_to(RIGHT * 3.2 + DOWN * 1.6)
        self.play(FadeIn(chk), Write(cap))
        self.wait(1.2)


class M06_B04Langchain(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        c1 = small_card("LangChain", LEFT * 4.0, width=3.0, height=1.1, tsize=32)
        c2 = small_card("OpenAI-compatible integration", ORIGIN, width=5.0, height=1.1, tsize=28)
        c3 = small_card("Muse", RIGHT * 4.0, width=2.6, height=1.1, tsize=32)
        self.play(FadeIn(c1, shift=RIGHT * 0.3))
        a1 = Arrow(c1.get_right(), c2.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a1), FadeIn(c2, shift=RIGHT * 0.3))
        a2 = Arrow(c2.get_right(), c3.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a2), FadeIn(c3, shift=RIGHT * 0.3))
        d = bullet(DOWN * 1.6, color=BLUE)
        self.play(FadeIn(d))
        self.wait(1.2)


class M07_B05Config(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rows = ["base URL", "API key", "model name"]
        y = 1.2
        plates = []
        for lab in rows:
            p = small_card(lab, LEFT * 2.6 + UP * y, width=3.6, height=0.9, tsize=28)
            self.play(FadeIn(p, shift=LEFT * 0.2))
            plates.append(p)
            y -= 1.2
        muse_card = small_card("Muse", RIGHT * 3.4, width=2.8, height=1.2, tsize=34)
        a = Arrow(LEFT * 0.6, RIGHT * 1.8, color=INK, buff=0.1, stroke_width=6)
        self.play(FadeIn(muse_card, shift=LEFT * 0.3))
        self.play(Create(a))
        self.wait(1.2)


class M08_B06Debug(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        err = RoundedRectangle(corner_radius=0.18, width=3.4, height=1.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=4).move_to(LEFT * 3.6)
        err_t = Text("the error", font_size=32, color=INK).move_to(err.get_center())
        self.play(FadeIn(VGroup(err, err_t), shift=RIGHT * 0.2))
        bubble = Circle(radius=0.6, color=BLUE, stroke_width=5).move_to(ORIGIN)
        tail = Line(bubble.get_bottom() + LEFT * 0.2,
                    bubble.get_bottom() + DOWN * 0.5 + LEFT * 0.3,
                    color=BLUE, stroke_width=5)
        self.play(Create(bubble), Create(tail))
        fix = RoundedRectangle(corner_radius=0.18, width=3.4, height=1.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=GREEN, stroke_width=4).move_to(RIGHT * 3.6)
        fix_t = Text("the fix", font_size=32, color=INK).move_to(fix.get_center())
        self.play(FadeIn(VGroup(fix, fix_t), shift=LEFT * 0.2))
        chk = check_mark(RIGHT * 3.6 + UP * 1.3, scale=0.4)
        self.play(FadeIn(chk))
        self.wait(1.2)


class M09_B07Wrapper(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        c1 = small_card("Claude Code", LEFT * 3.8 + UP * 0.6, width=3.4, height=1.1, tsize=30)
        c2 = small_card("wrapper script", LEFT * 3.8 + DOWN * 1.0, width=3.4, height=1.1, tsize=30)
        c3 = small_card("Muse Spark 1.2", RIGHT * 3.4, width=3.6, height=1.2, tsize=30)
        self.play(FadeIn(c1, shift=RIGHT * 0.2), FadeIn(c2, shift=RIGHT * 0.2))
        a = Arrow(LEFT * 1.8, RIGHT * 1.4, color=INK, buff=0.1, stroke_width=6)
        self.play(Create(a), FadeIn(c3, shift=LEFT * 0.2))
        d = bullet(DOWN * 2.4, color=ACCENT)
        self.play(FadeIn(d))
        self.wait(1.2)


class M10_B08Launch(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        term = small_card("a small refactor task", UP * 2.0, width=5.4, height=1.1, tsize=32)
        self.play(FadeIn(term, shift=DOWN * 0.2))
        dots = []
        for i in range(3):
            d = Dot(LEFT * 1.2 + RIGHT * i * 1.2, radius=0.16, color=BLUE)
            self.play(FadeIn(d))
            dots.append(d)
        chk = check_mark(RIGHT * 2.6, scale=0.5)
        cap = Text("the harness couldn't tell", font_size=30, color=GREY).move_to(DOWN * 1.6)
        self.play(FadeIn(chk), Write(cap))
        self.wait(1.2)


class M11_B09Odd(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        c1 = small_card("it works", LEFT * 2.8, width=3.2, height=1.2, tsize=32)
        self.play(FadeIn(c1, shift=RIGHT * 0.2))
        chk = check_mark(LEFT * 2.8 + UP * 1.3, scale=0.4)
        self.play(FadeIn(chk))
        c2 = small_card("it looks odd", RIGHT * 2.8, width=3.2, height=1.2, tsize=32)
        c2.rotate(0.12)
        self.play(FadeIn(c2, shift=LEFT * 0.2))
        wave = ParametricFunction(lambda t: np.array([t, 0.15 * np.sin(6 * t), 0]),
                                  t_range=[-1.2, 1.2], color=ACCENT, stroke_width=5)
        wave.move_to(RIGHT * 2.8 + DOWN * 1.4)
        self.play(Create(wave))
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # phase 1: recap
        recap = RoundedRectangle(corner_radius=0.25, width=10.5, height=4.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3)
        rh = Text("recap", font_size=36, color=GREY).move_to(recap.get_top() + DOWN * 0.55)
        lines = ["act one — the SDK drove the task",
                 "act two — one config block",
                 "act three — compatible, not native"]
        phase1 = VGroup(recap, rh)
        self.play(FadeIn(phase1, shift=DOWN * 0.2))
        y = 0.9
        for lab in lines:
            d = bullet(LEFT * 4.4 + UP * y, color=BLUE)
            t = Text(lab, font_size=30, color=INK).next_to(d, RIGHT, buff=0.3)
            phase1.add(d, t)
            self.play(FadeIn(VGroup(d, t), shift=LEFT * 0.2))
            y -= 1.0
        self.wait(0.6)
        # phase 2: your turn
        self.play(FadeOut(phase1))
        turn = RoundedRectangle(corner_radius=0.25, width=10.5, height=4.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3)
        th = Text("your turn", font_size=36, color=ACCENT).move_to(turn.get_top() + DOWN * 0.55)
        t1 = Text("point one tool you already use", font_size=30, color=INK).move_to(UP * 0.6)
        t2 = Text("at the Muse base URL", font_size=30, color=INK).move_to(DOWN * 0.1)
        t3 = Text("did it just work,", font_size=28, color=GREY).move_to(DOWN * 0.9)
        t4 = Text("or did it look odd?", font_size=28, color=GREY).move_to(DOWN * 1.55)
        phase2 = VGroup(turn, th, t1, t2, t3, t4)
        self.play(FadeIn(phase2, shift=DOWN * 0.2))
        self.wait(0.6)
        # phase 3: outro
        self.play(FadeOut(phase2))
        outro = title_card("Agents and Frameworks", "@NikBearBrown",
                           width=10.5, height=4.6, tsize=54)
        nxt = Text("Next: Muse Code, the Harness", font_size=30, color=GREY)
        nxt.next_to(outro, DOWN, buff=0.4)
        self.play(FadeIn(VGroup(outro, nxt), shift=UP * 0.2))
        self.wait(1.2)
