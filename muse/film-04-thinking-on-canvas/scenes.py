"""scenes.py — Thinking on Canvas (Film 4). Manim visuals, house template."""
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


def idea_row(label, pos, width=6.4):
    plate = RoundedRectangle(corner_radius=0.14, width=width, height=0.85,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    d = bullet(plate.get_left() + RIGHT * 0.4)
    t = Text(label, font_size=30, color=INK).next_to(d, RIGHT, buff=0.25)
    return VGroup(plate, d, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("a brainstorming partner that draws")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        bubble = Circle(radius=0.55, color=BLUE, stroke_width=6).shift(LEFT * 1.2 + DOWN * 0.4)
        bubble_tail = Line(bubble.get_bottom() + LEFT * 0.2, bubble.get_bottom() + DOWN * 0.5 + LEFT * 0.4,
                           color=BLUE, stroke_width=6)
        pencil = Line(LEFT * 0.4, RIGHT * 0.4, color=ACCENT, stroke_width=10).shift(RIGHT * 1.2 + DOWN * 0.4)
        self.play(Create(bubble), Create(bubble_tail), Create(pencil))
        self.play(bubble.animate.shift(RIGHT * 1.2), pencil.animate.shift(LEFT * 1.2),
                  bubble_tail.animate.shift(RIGHT * 1.2), run_time=1.2)
        ring = Circle(radius=0.75, color=GREEN, stroke_width=6).move_to(ORIGIN + DOWN * 0.4)
        self.play(Create(ring))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("Brainstorm", "ideas fast, judge later", LEFT * 3.1 + UP * 0.9),
            ("Mermaid", "diagrams in plain text", RIGHT * 3.1 + UP * 0.9),
            ("Mind map", "ideas from one center", LEFT * 3.1 + DOWN * 1.1),
            ("Iteration", "each pass sharper", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Ask(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        blob = Circle(radius=1.0, color=GREY, fill_opacity=0.35, stroke_width=4).shift(LEFT * 4.2)
        blob_t = Text("make the plugins\nfunner", font_size=30, color=INK).move_to(blob.get_center())
        self.play(FadeIn(blob), Write(blob_t))
        arrow = Arrow(LEFT * 2.8, LEFT * 1.6, color=INK, buff=0.1, stroke_width=6)
        self.play(Create(arrow))
        labels = ["deploy confessions", "coffee match", "thunderdome", "kudos terminal"]
        y = 1.9
        for lab in labels:
            row = idea_row(lab, RIGHT * 1.6 + UP * y, width=5.6)
            self.play(FadeIn(row, shift=LEFT * 0.3))
            y -= 1.25
        self.wait(1.2)


class M04_B02Judge(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("judge them out loud", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        labels = ["deploy confessions", "coffee match", "thunderdome", "kudos terminal"]
        verdicts = ["check", "check", "huh", "check"]
        y = 1.7
        for lab, v in zip(labels, verdicts):
            row = idea_row(lab, LEFT * 1.2 + UP * y, width=5.6)
            self.play(FadeIn(row, shift=LEFT * 0.3))
            anchor = row.get_right() + RIGHT * 0.55
            if v == "check":
                mark = check_mark(anchor)
            else:
                mark = Text("huh?", font_size=34, color=GREY).move_to(anchor)
                row[0].set_fill(GREY, opacity=0.25)
            self.play(FadeIn(mark, scale=0.6))
            y -= 1.35
        self.wait(1.2)


class M05_B03Pick(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        row = idea_row("coffee match", LEFT * 3.0, width=5.6)
        self.play(FadeIn(row, shift=RIGHT * 0.3))
        ring = RoundedRectangle(corner_radius=0.2, width=6.0, height=1.15,
                                stroke_color=ACCENT, stroke_width=6,
                                fill_opacity=0).move_to(row.get_center())
        self.play(Create(ring))
        arrow = Arrow(LEFT * 0.4, RIGHT * 1.6, color=INK, buff=0.2, stroke_width=6)
        self.play(Create(arrow))
        frame = Rectangle(width=3.4, height=2.6, color=INK, stroke_width=4).shift(RIGHT * 3.6)
        ft = Text("draw this", font_size=32, color=GREY).move_to(frame.get_center())
        self.play(FadeIn(frame), Write(ft))
        self.wait(1.2)


class M06_B04Map(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        center = Circle(radius=0.7, color=ACCENT, fill_opacity=0.9, stroke_width=0).shift(LEFT * 3.4)
        ct = Text("community", font_size=26, color=CARD).move_to(center.get_center())
        self.play(FadeIn(center), Write(ct))
        angles = [65, 25, -15, -55, -95]
        for i, a in enumerate(angles):
            ang = a * DEGREES
            node_pos = LEFT * 3.4 + np.array([np.cos(ang), np.sin(ang), 0]) * 3.4
            node = Circle(radius=0.42, color=BLUE, fill_opacity=0.85, stroke_width=0).move_to(node_pos)
            edge = Line(center.get_center(), node.get_center(), color=GREY, stroke_width=4)
            self.play(Create(edge), FadeIn(node, scale=0.5))
        self.wait(1.2)


class M07_B05Read(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        center = Circle(radius=0.7, color=ACCENT, fill_opacity=0.9, stroke_width=0).shift(LEFT * 3.4)
        ct = Text("community", font_size=26, color=CARD).move_to(center.get_center())
        self.play(FadeIn(center), Write(ct))
        branches = [
            ("learning\nand growth", 65),
            ("experimentation", 25),
            ("participation", -15),
            ("identity and\nbelonging", -55),
            ("recognition", -95),
        ]
        for label, a in branches:
            ang = a * DEGREES
            node_pos = LEFT * 3.4 + np.array([np.cos(ang), np.sin(ang), 0]) * 3.4
            node = Circle(radius=0.42, color=BLUE, fill_opacity=0.85, stroke_width=0).move_to(node_pos)
            edge = Line(center.get_center(), node.get_center(), color=GREY, stroke_width=4)
            lab = Text(label, font_size=22, color=INK)
            lab.next_to(node, np.array([np.cos(ang), np.sin(ang), 0]), buff=0.25)
            dot = bullet(node.get_center() + UP * 0.55, color=GREEN)
            self.play(Create(edge), FadeIn(node, scale=0.5), Write(lab), FadeIn(dot))
        self.wait(1.2)


class M08_B06Ground(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        center = Circle(radius=0.55, color=ACCENT, fill_opacity=0.9, stroke_width=0).shift(LEFT * 4.4)
        ct = Text("community", font_size=22, color=CARD).move_to(center.get_center())
        self.play(FadeIn(center), Write(ct))
        branch_cols = [BLUE, "#8A5FBF", "#C98A2E", "#2E8B57", "#B8472F"]
        labels = ["learning", "experiment", "participate", "belong", "recognized"]
        for i, (lab, col) in enumerate(zip(labels, branch_cols)):
            y = 2.6 - i * 1.3
            node = Circle(radius=0.34, color=col, fill_opacity=0.9, stroke_width=0).move_to(LEFT * 4.4 + UP * y)
            edge = Line(center.get_center(), node.get_center(), color=GREY, stroke_width=4)
            lt = Text(lab, font_size=20, color=INK).next_to(node, LEFT, buff=0.2)
            self.play(Create(edge), FadeIn(node, scale=0.5), Write(lt))
            for j in range(2):
                leaf_pos = node.get_center() + RIGHT * (1.1 + j * 0.85) + UP * (0.35 - j * 0.7)
                leaf = Circle(radius=0.26, color=col, fill_opacity=0.55, stroke_width=3).move_to(leaf_pos)
                ledge = Line(node.get_center(), leaf.get_center(), color=col, stroke_width=3)
                self.play(Create(ledge), FadeIn(leaf, scale=0.5), run_time=0.5)
        self.wait(1.2)


class M09_B07Editor(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the mermaid part, not the model", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        m_plate = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2).shift(LEFT * 2.9 + DOWN * 0.3)
        m_t = Text("the model", font_size=36, color=INK).move_to(m_plate.get_center())
        self.play(FadeIn(m_plate), Write(m_t))
        self.play(FadeIn(check_mark(m_plate.get_center() + DOWN * 0.75), scale=0.8))
        e_plate = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.2,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2).shift(RIGHT * 2.9 + DOWN * 0.3)
        e_t = Text("the editor", font_size=36, color=INK).move_to(e_plate.get_center())
        self.play(FadeIn(e_plate), Write(e_t))
        for k in range(3):
            glitch = Line(e_plate.get_left() + UP * (0.5 - k * 0.5),
                          e_plate.get_right() + UP * (0.7 - k * 0.5),
                          color=ACCENT, stroke_width=5)
            self.play(Create(glitch), run_time=0.4)
        self.play(FadeIn(cross_mark(e_plate.get_center() + DOWN * 0.75), scale=0.8))
        self.wait(1.2)


class M10_B08Loop(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        words = ["ask", "draw", "refine"]
        nodes = []
        for i, w in enumerate(words):
            ang = 90 * DEGREES + i * 120 * DEGREES
            pos = np.array([np.cos(ang), np.sin(ang), 0]) * 2.4 + DOWN * 0.3
            plate = RoundedRectangle(corner_radius=0.25, width=2.6, height=1.3,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2).move_to(pos)
            t = Text(w, font_size=40, color=INK).move_to(plate.get_center())
            self.play(FadeIn(VGroup(plate, t), shift=DOWN * 0.2))
            nodes.append(plate.get_center())
        arrows = []
        for i in range(3):
            a = Arrow(nodes[i], nodes[(i + 1) % 3], color=GREY, buff=0.5, stroke_width=6)
            arrows.append(a)
            self.play(Create(a))
        for a in arrows:
            self.play(a.animate.set_color(ACCENT).set_stroke(width=10), run_time=0.6)
        self.wait(1.2)


class M11_B09Why(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        frame = Rectangle(width=5.6, height=3.6, color=INK, stroke_width=4).shift(DOWN * 0.5)
        self.play(FadeIn(frame))
        root = Circle(radius=0.3, color=ACCENT, fill_opacity=0.9, stroke_width=0).move_to(frame.get_center() + DOWN * 0.8)
        self.play(FadeIn(root, scale=0.5))
        for a in [50, 90, 130]:
            ang = a * DEGREES
            tip = root.get_center() + np.array([np.cos(ang), np.sin(ang), 0]) * 1.3
            branch = Line(root.get_center(), tip, color=BLUE, stroke_width=5)
            leaf = Dot(tip, radius=0.14, color=GREEN)
            self.play(Create(branch), FadeIn(leaf))
        bulb_c = Circle(radius=0.4, color=ACCENT, fill_opacity=0.85, stroke_width=0).move_to(UP * 2.9)
        bulb_base = Line(LEFT * 0.18 + UP * 2.45, RIGHT * 0.18 + UP * 2.45, color=INK, stroke_width=5)
        cap = Text("thinking on canvas", font_size=36, color=INK).next_to(frame, DOWN, buff=0.3)
        self.play(FadeIn(bulb_c, scale=0.6), Create(bulb_base), Write(cap))
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap
        plate = RoundedRectangle(corner_radius=0.2, width=9.0, height=4.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3)
        head = Text("recap", font_size=40, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head), FadeIn(plate))
        recaps = ["ask, then judge out loud",
                  "draw the map, populate the branches",
                  "loop ask, draw, refine"]
        y = 1.0
        recap_grp = VGroup()
        for r in recaps:
            d = bullet(LEFT * 3.9 + UP * y)
            t = Text(r, font_size=32, color=INK).next_to(d, RIGHT, buff=0.3)
            self.play(FadeIn(d), Write(t))
            recap_grp.add(d, t)
            y -= 1.3
        self.wait(0.8)
        self.play(FadeOut(plate), FadeOut(recap_grp), FadeOut(head))
        # Phase 2: your turn
        card = title_card("your turn", "Pick one idea. Ask for three variations. Ask it to draw the best one.")
        self.play(FadeIn(card, shift=UP * 0.3))
        check = Text("Does the picture show you\nsomething the list didn't?", font_size=30,
                     color=GREY).next_to(card, DOWN, buff=0.4)
        pencil = Line(LEFT * 0.5, RIGHT * 0.5, color=ACCENT, stroke_width=8).next_to(check, DOWN, buff=0.3)
        self.play(Write(check), Create(pencil))
        self.wait(0.8)
        self.play(FadeOut(card), FadeOut(check), FadeOut(pencil))
        # Phase 3: outro
        outro = title_card("Thinking on Canvas", "@NikBearBrown")
        self.play(FadeIn(outro, shift=DOWN * 0.3))
        nxt = Text("Next: Grounded Answers", font_size=34, color=BLUE).next_to(outro, DOWN, buff=0.4)
        bar = Line(LEFT * 1.5, RIGHT * 1.5, color=BLUE, stroke_width=6).next_to(nxt, DOWN, buff=0.25)
        self.play(Write(nxt), Create(bar))
        self.wait(1.2)
