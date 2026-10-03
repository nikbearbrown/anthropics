"""scenes.py — Your First Prompts (Film 2 of the Muse series).
13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat."""
from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.25, width=11.5, height=2.6,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = VGroup(plate, t)
    if sub is not None:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


def bullet(pos, color=ACCENT, r=0.12):
    return Dot(point=[pos[0], pos[1], 0], radius=r, color=color)


def check_mark(pos, scale=1.0, color=GREEN):
    return VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4, color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


def labeled_box(label, pos, w=3.4, h=1.6, box_color=INK, label_size=36):
    box = Rectangle(width=w, height=h, stroke_color=box_color, stroke_width=4,
                    fill_color=CARD, fill_opacity=1).move_to(pos)
    lab = Text(label, font_size=label_size, color=INK).move_to(box.get_center())
    return VGroup(box, lab)


class M01_Bidea(Scene):
    def construct(self):
        # browser window card with terracotta header
        win = RoundedRectangle(corner_radius=0.3, width=10.5, height=5.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        header = RoundedRectangle(corner_radius=0.25, width=10.5, height=1.1,
                                   fill_color=ACCENT, fill_opacity=1,
                                   stroke_width=0).move_to([0, 2.25, 0])
        url = Text("dev.meta.ai", font_size=40, color=CARD).move_to([0, 2.25, 0])
        self.play(FadeIn(win), Create(header))
        self.play(Write(url))
        dots = VGroup(*[bullet([-4.2 + i * 0.9, 0.4, 0], color=BLUE) for i in range(6)])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.12))
        cursor = Arrow(LEFT * 1.2 + DOWN * 0.8, RIGHT * 0.6 + UP * 0.2,
                       color=INK, stroke_width=10, buff=0).move_to([3.4, -1.4, 0])
        self.play(GrowArrow(cursor))
        tag_dot = bullet([-3.4, -2.2, 0], color=ACCENT, r=0.14)
        tag = Text("you are here", font_size=36, color=INK).next_to(tag_dot, RIGHT, buff=0.3)
        self.play(FadeIn(tag_dot), Write(tag))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        head = Text("Four terms", font_size=48, color=INK).to_edge(UP, buff=0.7)
        head_rule = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
        head_rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(head_rule))
        terms = [
            ("Playground", "the web app where you prompt the model"),
            ("Spend limit", "the cap you set on your card"),
            ("Reasoning effort", "how hard the model thinks, from low to extra high"),
            ("Prompt", "the text you send it"),
        ]
        for i, (term, gloss) in enumerate(terms):
            y = 1.5 - i * 1.35
            card = RoundedRectangle(corner_radius=0.2, width=11.0, height=1.05,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=INK, stroke_width=2).move_to([0, y, 0])
            d = bullet([-5.0, y, 0])
            t = Text(term, font_size=34, color=ACCENT).move_to([-3.4, y, 0])
            g = Text(gloss, font_size=28, color=GREY).move_to([1.4, y, 0])
            self.play(FadeIn(card), FadeIn(d), Write(t))
            self.play(Write(g))
        self.wait(1.2)


class M03_B01(Scene):
    def construct(self):
        head = Text("The account", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        card = RoundedRectangle(corner_radius=0.3, width=10.0, height=4.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=3).move_to([0, -0.4, 0])
        self.play(FadeIn(card))
        chip = Rectangle(width=1.6, height=1.1, stroke_color=BLUE, stroke_width=4,
                         fill_color=BLUE, fill_opacity=0.25).move_to([-3.4, 0.9, 0])
        chip_lab = Text("card", font_size=30, color=INK).move_to(chip.get_center())
        self.play(Create(chip), Write(chip_lab))
        rail = Line(LEFT * 3.4, RIGHT * 3.4, color=GREY, stroke_width=8).move_to([0.4, -0.9, 0])
        self.play(Create(rail))
        knob = Dot(point=[2.2, -0.9, 0], radius=0.22, color=ACCENT)
        knob_lab = Text("$30", font_size=36, color=ACCENT).next_to(knob, UP, buff=0.25)
        self.play(FadeIn(knob), Write(knob_lab))
        tag_dot = bullet([-4.2, -2.3, 0], color=GREEN, r=0.14)
        tag = Text("a cap, not a deposit", font_size=34, color=INK).next_to(tag_dot, RIGHT, buff=0.3)
        self.play(FadeIn(tag_dot), Write(tag))
        self.wait(1.2)


class M04_B02(Scene):
    def construct(self):
        old = Text("$5 minimum", font_size=60, color=GREY).move_to([0, 1.4, 0])
        strike = Line(LEFT * 2.6, RIGHT * 2.6, color=ACCENT, stroke_width=8).move_to([0, 1.4, 0])
        self.play(Write(old))
        self.play(Create(strike))
        coin = Circle(radius=0.9, stroke_color=ACCENT, stroke_width=6,
                      fill_color=ACCENT, fill_opacity=0.2).move_to([0, -0.6, 0])
        coin_lab = Text("$1", font_size=48, color=INK).move_to(coin.get_center())
        self.play(FadeOut(old), FadeOut(strike), Create(coin), Write(coin_lab))
        cm = check_mark([2.6, -0.6, 0], scale=0.9)
        tag = Text("no minimum", font_size=40, color=INK).move_to([-2.8, -0.6, 0])
        self.play(Create(cm[0]), Create(cm[1]), Write(tag))
        self.wait(1.2)


class M05_B03(Scene):
    def construct(self):
        head = Text("The controls", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        labels = ["model picker", "effort", "streaming", "toggles"]
        for i, lab in enumerate(labels):
            x = -4.5 + i * 3.0
            dial = Circle(radius=0.85, stroke_color=GREY, stroke_width=5,
                          fill_color=CARD, fill_opacity=1).move_to([x, 0.2, 0])
            d = bullet([x, 1.6, 0], color=BLUE)
            t = Text(lab, font_size=30, color=INK).move_to([x, -1.1, 0])
            self.play(FadeIn(d), Create(dial))
            dial_lit = Circle(radius=0.85, stroke_color=ACCENT, stroke_width=7,
                              fill_color=CARD, fill_opacity=1).move_to([x, 0.2, 0])
            self.play(Transform(dial, dial_lit), Write(t))
        self.wait(1.2)


class M06_B04(Scene):
    def construct(self):
        prompt_card = RoundedRectangle(corner_radius=0.25, width=8.5, height=1.3,
                                       fill_color=BLUE, fill_opacity=0.15,
                                       stroke_color=BLUE, stroke_width=3).move_to([0, 2.3, 0])
        prompt = Text("JLPT N5 grammar points?", font_size=36, color=INK).move_to(prompt_card.get_center())
        self.play(FadeIn(prompt_card), Write(prompt))
        rows = []
        for i in range(40):
            col, row = i % 4, i // 4
            x = -4.2 + col * 2.8
            y = 0.9 - row * 0.42
            rows.append(Line([x - 0.9, y, 0], [x + 0.9, y, 0],
                             color=GREY, stroke_width=5))
        wave1, wave2 = VGroup(*rows[:20]), VGroup(*rows[20:])
        self.play(LaggedStart(*[Create(r) for r in wave1], lag_ratio=0.04))
        self.play(LaggedStart(*[Create(r) for r in wave2], lag_ratio=0.04))
        cm = check_mark([5.2, -2.9, 0], scale=1.1)
        self.play(Create(cm[0]), Create(cm[1]))
        self.wait(1.2)


class M07_B05(Scene):
    def construct(self):
        center = [0, -1.6, 0]
        arc = Arc(radius=3.6, start_angle=0, angle=PI, arc_center=[*center, 0],
                  color=GREY, stroke_width=5)
        self.play(Create(arc))
        import math
        labels = ["low", "medium", "high", "extra high"]
        for i, lab in enumerate(labels):
            ang = math.pi - i * (math.pi / 3)
            px = center[0] + 3.6 * math.cos(ang)
            py = center[1] + 3.6 * math.sin(ang)
            d = bullet([px, py, 0], color=BLUE if i < 3 else ACCENT, r=0.16)
            t = Text(lab, font_size=32, color=INK).move_to([px, py - 0.55, 0])
            self.play(FadeIn(d), Write(t))
        needle = Line([*center, 0], [center[0] - 3.6, center[1], 0],
                      color=ACCENT, stroke_width=10)
        self.play(Create(needle))
        self.play(Rotate(needle, angle=PI, about_point=[*center, 0]))
        tag_dot = bullet([-3.6, -2.9, 0], color=GREEN, r=0.14)
        tag = Text("match the problem", font_size=36, color=INK).next_to(tag_dot, RIGHT, buff=0.3)
        self.play(FadeIn(tag_dot), Write(tag))
        self.wait(1.2)


class M08_B06(Scene):
    def construct(self):
        head = Text("Read it like a practitioner", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rows = ["answer?", "formatting?", "second look?"]
        for i, lab in enumerate(rows):
            y = 1.1 - i * 1.5
            plate = RoundedRectangle(corner_radius=0.2, width=9.0, height=1.1,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2).move_to([0, y, 0])
            t = Text(lab, font_size=38, color=INK).move_to([-2.6, y, 0])
            cm = check_mark([2.8, y, 0], scale=0.85)
            self.play(FadeIn(plate), Write(t))
            self.play(Create(cm[0]), Create(cm[1]))
        self.wait(1.2)


class M09_B07(Scene):
    def construct(self):
        big = Text("$5", font_size=150, color=ACCENT).move_to([-4.2, 0.6, 0])
        self.play(Write(big))
        bars = VGroup()
        for i in range(5):
            h = 1.0 + i * 0.9
            bar = Rectangle(width=1.1, height=h, stroke_color=BLUE, stroke_width=3,
                            fill_color=BLUE, fill_opacity=0.55)
            bar.move_to([-1.6 + i * 1.5, -2.2 + h / 2, 0])
            bars.add(bar)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.18))
        tag_dot = bullet([-4.6, -2.6, 0], color=GREEN, r=0.14)
        tag = Text("hundreds of prompts", font_size=36, color=INK).next_to(tag_dot, RIGHT, buff=0.3)
        self.play(FadeIn(tag_dot), Write(tag))
        self.wait(1.2)


class M10_B08(Scene):
    def construct(self):
        head = Text("The meter", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        lab_in = Text("in", font_size=36, color=INK).move_to([-4.6, 0.9, 0])
        bar_in = RoundedRectangle(corner_radius=0.15, width=4.0, height=0.7,
                                  fill_color=BLUE, fill_opacity=0.7,
                                  stroke_width=0).move_to([-2.0, 0.9, 0])
        lab_out = Text("out", font_size=36, color=INK).move_to([-4.6, -0.5, 0])
        bar_out = RoundedRectangle(corner_radius=0.15, width=6.0, height=0.7,
                                   fill_color=ACCENT, fill_opacity=0.7,
                                   stroke_width=0).move_to([-1.0, -0.5, 0])
        self.play(Write(lab_in), GrowFromEdge(bar_in, LEFT))
        self.play(Write(lab_out), GrowFromEdge(bar_out, LEFT))
        chip = RoundedRectangle(corner_radius=0.2, width=3.2, height=1.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=3).move_to([3.6, 0.2, 0])
        chip_lab = Text("extra high", font_size=30, color=ACCENT).move_to(chip.get_center())
        self.play(FadeIn(chip), Write(chip_lab))
        bar_in_big = RoundedRectangle(corner_radius=0.15, width=10.0, height=0.7,
                                      fill_color=BLUE, fill_opacity=0.7,
                                      stroke_width=0).move_to([1.0, 0.9, 0])
        bar_out_big = RoundedRectangle(corner_radius=0.15, width=11.0, height=0.7,
                                       fill_color=ACCENT, fill_opacity=0.7,
                                       stroke_width=0).move_to([1.5, -0.5, 0])
        self.play(Transform(bar_in, bar_in_big), Transform(bar_out, bar_out_big))
        self.wait(1.2)


class M11_B09(Scene):
    def construct(self):
        head = Text("Honest friction", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rows = ["no copy button", "save and attach", "lab bench, not chat app"]
        for i, lab in enumerate(rows):
            y = 1.2 - i * 1.5
            plate = RoundedRectangle(corner_radius=0.2, width=9.5, height=1.1,
                                     fill_color=GREY, fill_opacity=0.25,
                                     stroke_color=GREY, stroke_width=3).move_to([0, y, 0])
            sq = Square(side_length=0.4, stroke_color=GREY, stroke_width=4,
                        fill_opacity=0).move_to([-4.0, y, 0])
            t = Text(lab, font_size=36, color=GREY).move_to([-0.6, y, 0])
            self.play(FadeIn(plate), Create(sq), Write(t))
        self.wait(1.2)


class M12_B10(Scene):
    def construct(self):
        left = labeled_box("API key", [-3.8, 0, 0], w=3.6, h=1.8, box_color=BLUE, label_size=40)
        self.play(Create(left[0]), Write(left[1]))
        arrow = Arrow(LEFT * 1.6, RIGHT * 1.6, color=INK, stroke_width=10).move_to([0, 0, 0])
        self.play(GrowArrow(arrow))
        right = labeled_box("your code", [3.8, 0, 0], w=3.6, h=1.8, box_color=ACCENT, label_size=40)
        self.play(Create(right[0]), Write(right[1]))
        tag_dot = bullet([-3.2, -2.4, 0], color=GREEN, r=0.14)
        tag = Text("later films' territory", font_size=34, color=GREY).next_to(tag_dot, RIGHT, buff=0.3)
        self.play(FadeIn(tag_dot), Write(tag))
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        # phase 1: recap — 4 lines
        head = Text("Recap", font_size=48, color=INK).to_edge(UP, buff=0.7)
        head_rule = Line(LEFT * 1.8, RIGHT * 1.8, color=ACCENT, stroke_width=5)
        head_rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(head_rule))
        lines = [
            "1 card on file \u00b7 spend limit \u00b7 no minimum",
            "2 model \u00b7 effort \u00b7 streaming \u00b7 toggles",
            "3 tokens in and out \u00b7 five dollars goes a long way",
            "4 honest friction \u00b7 code comes next",
        ]
        recap_g = VGroup(head, head_rule)
        for i, ln in enumerate(lines):
            y = 1.3 - i * 1.15
            d = bullet([-5.2, y, 0], color=BLUE)
            t = Text(ln, font_size=30, color=INK).move_to([-0.2, y, 0])
            recap_g.add(d, t)
            self.play(FadeIn(d), Write(t))
        self.wait(0.6)
        # phase 2: your turn
        self.play(FadeOut(recap_g))
        card = title_card("Your turn")
        self.play(FadeIn(card))
        turn_g = VGroup(card)
        steps = ["Open the playground.", "Set a spend limit.", "Run one prompt."]
        for i, s in enumerate(steps):
            d = bullet([-4.4, -0.2 - i * 0.8, 0], color=ACCENT)
            t = Text(s, font_size=34, color=INK).next_to(d, RIGHT, buff=0.3)
            turn_g.add(d, t)
            self.play(FadeIn(d), Write(t))
        q1 = Text("Did it answer well? What did the meter say?",
                 font_size=30, color=GREY).move_to([0, -2.9, 0])
        turn_g.add(q1)
        self.play(Write(q1))
        self.wait(0.6)
        self.play(FadeOut(turn_g))
        # phase 3: outro
        out = title_card("Your First Prompts", "@NikBearBrown")
        self.play(FadeIn(out))
        nxt = Text("Next: Muse Can See", font_size=40, color=ACCENT).move_to([0, -2.6, 0])
        nd = bullet([-3.4, -2.6, 0], color=ACCENT)
        self.play(FadeIn(nd), Write(nxt))
        self.wait(1.2)
