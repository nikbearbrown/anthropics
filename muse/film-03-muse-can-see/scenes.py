#!/usr/bin/env python3
"""scenes.py — Muse Can See (Film 3).
Manim scenes for the 14-beat script. House template: 1920x1080,
INK/PAPER/ACCENT/BLUE/GREEN/GREY/CARD, safe area +/-6.3 x, +/-3.4 y.
"""
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

TITLE_FONT = 64
BODY_FONT = 40
SMALL_FONT = 30


def title_card(title, sub=None):
    grp = VGroup()
    t = Text(title, font_size=TITLE_FONT, color=INK).move_to(ORIGIN)
    grp.add(t)
    if sub is not None:
        s = Text(sub, font_size=BODY_FONT, color=GREY).next_to(t, DOWN, buff=0.4)
        grp.add(s)
    plate = RoundedRectangle(
        corner_radius=0.25, width=grp.width + 1.6, height=grp.height + 1.2,
        fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=3,
    ).move_to(grp.get_center())
    return VGroup(plate, grp)


def check_mark(pos, scale=0.5, color=GREEN):
    l1 = Line(LEFT * 0.25 + DOWN * 0.05, ORIGIN, color=color, stroke_width=10)
    l2 = Line(ORIGIN, RIGHT * 0.35 + UP * 0.35, color=color, stroke_width=10)
    g = VGroup(l1, l2).scale(scale).move_to(pos)
    return g


def cross_mark(pos, scale=0.5, color=ACCENT):
    l1 = Line(LEFT * 0.3 + DOWN * 0.3, RIGHT * 0.3 + UP * 0.3,
              color=color, stroke_width=10)
    l2 = Line(LEFT * 0.3 + UP * 0.3, RIGHT * 0.3 + DOWN * 0.3,
              color=color, stroke_width=10)
    g = VGroup(l1, l2).scale(scale).move_to(pos)
    return g


def bullet(pos, color=ACCENT, r=0.09):
    return Dot(pos, radius=r, color=color)


class M01_Bidea(Scene):
    def construct(self):
        card = title_card("what if the model could", "look at your screen?")
        self.play(FadeIn(card), run_time=0.8)
        frame = RoundedRectangle(corner_radius=0.15, width=5.0, height=2.6,
                                 stroke_color=INK, stroke_width=4,
                                 fill_opacity=0)
        frame.to_edge(DOWN, buff=0.9)
        eye_outer = Ellipse(width=1.6, height=0.9, color=BLUE, stroke_width=6)
        pupil = Dot(color=BLUE, radius=0.22)
        eye = VGroup(eye_outer, pupil).move_to(frame.get_center())
        self.play(Create(frame), run_time=0.8)
        self.play(Create(eye_outer), FadeIn(pupil), run_time=0.8)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        title = Text("four terms", font_size=TITLE_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        plate = RoundedRectangle(corner_radius=0.2, width=12.6, height=0.9,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3,
                                 ).move_to(title.get_center())
        self.play(FadeIn(plate), FadeIn(title), run_time=0.6)
        terms = [
            ("Vision", "the model reading an image you give it"),
            ("Transcription", "turning that image into text, character by character"),
            ("Reference image", "a picture you hand the model: build from this"),
            ("System instruction", "standing orders before it starts"),
        ]
        y = 1.6
        for name, gloss in terms:
            dot = bullet(LEFT * 5.6 + UP * y)
            nm = Text(name, font_size=BODY_FONT, color=INK
                      ).next_to(dot, RIGHT, buff=0.3).align_to(dot, LEFT)
            nm.shift(RIGHT * 0.0)
            nm.move_to([dot.get_center()[0] + 0.35 + nm.width / 2, y, 0])
            gl = Text(gloss, font_size=SMALL_FONT, color=GREY
                      ).next_to(nm, RIGHT, buff=0.5)
            if gl.get_right()[0] > 6.0:
                gl.scale(6.0 / gl.get_right()[0] * 0.95)
                gl.next_to(nm, RIGHT, buff=0.5)
            self.play(FadeIn(dot), FadeIn(nm), FadeIn(gl), run_time=0.6)
            y -= 1.05
        self.wait(1.2)


class M03_B01Shot(Scene):
    def construct(self):
        label = Text("one word: transcribe", font_size=BODY_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(label), run_time=0.6)
        frame = RoundedRectangle(corner_radius=0.2, width=8.4, height=4.4,
                                 stroke_color=INK, stroke_width=4,
                                 fill_color=CARD, fill_opacity=1)
        frame.move_to(DOWN * 0.3)
        dots = VGroup(*[Dot(radius=0.09, color=c).move_to(
            frame.get_corner(UL) + RIGHT * (0.5 + 0.45 * i) + DOWN * 0.35)
            for i, c in enumerate([ACCENT, BLUE, GREEN])])
        shot = Rectangle(width=7.4, height=2.9, stroke_color=GREY,
                         stroke_width=2, fill_color=PAPER, fill_opacity=1)
        shot.next_to(dots, DOWN, buff=0.25).align_to(frame, LEFT).shift(
            RIGHT * 0.5 + DOWN * 0.35)
        lines = VGroup(*[
            Line(LEFT * 3.2 + UP * (0.9 - 0.55 * i),
                 RIGHT * 3.2 + UP * (0.9 - 0.55 * i),
                 color=GREY, stroke_width=3).move_to(shot.get_center() + UP * (0.9 - 0.55 * i))
            for i in range(4)
        ])
        word = Text("transcribe", font_size=BODY_FONT, color=ACCENT
                    ).next_to(frame, DOWN, buff=0.35)
        self.play(Create(frame), FadeIn(dots), run_time=0.8)
        self.play(FadeIn(shot), Create(lines), run_time=0.8)
        self.play(Write(word), run_time=0.8)
        self.wait(1.2)


class M04_B02Percent(Scene):
    def construct(self):
        title = Text("his verdict", font_size=TITLE_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)
        words = ["kanji", "hiragana", "katakana"]
        y = 1.8
        for w in words:
            cm = check_mark(LEFT * 2.6 + UP * y, scale=0.55)
            t = Text(w, font_size=BODY_FONT, color=INK
                     ).next_to(cm, RIGHT, buff=0.4)
            self.play(Create(cm), FadeIn(t), run_time=0.6)
            y -= 1.0
        pct = Text("100%", font_size=150, color=GREEN
                   ).move_to(RIGHT * 3.2 + DOWN * 0.4)
        ring = Circle(radius=1.55, color=GREEN, stroke_width=8
                      ).move_to(pct.get_center())
        self.play(GrowFromCenter(pct), run_time=0.7)
        self.play(Create(ring), run_time=0.6)
        self.wait(1.2)


class M05_B03Footnote(Scene):
    def construct(self):
        card = title_card("whose fault?", "check before you blame")
        self.play(FadeIn(card), run_time=0.7)
        row_y = -1.9
        t_model = Text("model", font_size=BODY_FONT, color=INK
                       ).move_to(LEFT * 2.6 + UP * row_y)
        cm = cross_mark(t_model.get_center() + LEFT * 1.7, scale=0.55)
        t_editor = Text("editor", font_size=BODY_FONT, color=INK
                        ).move_to(RIGHT * 2.6 + UP * row_y)
        ring = Circle(radius=0.95, color=BLUE, stroke_width=6
                      ).move_to(t_editor.get_center())
        self.play(Create(cm), FadeIn(t_model), run_time=0.7)
        self.play(Create(ring), FadeIn(t_editor), run_time=0.7)
        self.wait(1.2)


class M06_B04Ref(Scene):
    def construct(self):
        title = Text("reference image: PHP-Nuke", font_size=BODY_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)
        rails = VGroup()
        xs = [-4.0, 0.0, 4.0]
        widths = [2.6, 4.6, 2.6]
        for x, w in zip(xs, widths):
            r = Rectangle(width=w, height=4.6, stroke_color=INK, stroke_width=4,
                          fill_color=CARD, fill_opacity=1
                          ).move_to([x, -0.4, 0])
            rails.add(r)
        self.play(Create(rails[0]), run_time=0.5)
        self.play(Create(rails[1]), run_time=0.5)
        self.play(Create(rails[2]), run_time=0.5)
        cap = Text("three columns, early-2000s internet", font_size=SMALL_FONT,
                   color=GREY).next_to(rails, DOWN, buff=0.4)
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(1.2)


class M07_B05Sys(Scene):
    def construct(self):
        card = title_card("front-end developer", "the job description")
        self.play(FadeIn(card), run_time=0.7)
        chips = ["one file", "no framework", "flexbox", "mobile"]
        row = VGroup()
        for c in chips:
            t = Text(c, font_size=SMALL_FONT, color=INK)
            p = RoundedRectangle(corner_radius=0.35, width=t.width + 0.8,
                                 height=0.85, fill_color=BLUE,
                                 fill_opacity=0.18, stroke_color=BLUE,
                                 stroke_width=3)
            g = VGroup(p, t.move_to(p.get_center()))
            row.add(g)
        row.arrange(RIGHT, buff=0.5).move_to(DOWN * 2.2)
        for g in row:
            self.play(FadeIn(g), run_time=0.5)
        wheel = Text("the steering wheel", font_size=SMALL_FONT,
                     color=GREY).next_to(row, DOWN, buff=0.4)
        self.play(FadeIn(wheel), run_time=0.6)
        self.wait(1.2)


class M08_B06Result(Scene):
    def construct(self):
        title = Text("it builds", font_size=TITLE_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)
        xs = [-4.0, 0.0, 4.0]
        widths = [2.6, 4.6, 2.6]
        rails = VGroup(*[
            Rectangle(width=w, height=4.2, stroke_color=INK, stroke_width=3,
                      fill_color=CARD, fill_opacity=1).move_to([x, -0.5, 0])
            for x, w in zip(xs, widths)
        ])
        self.play(Create(rails), run_time=0.6)
        mods = [
            ("system load", 0, 1.1), ("who's online", 0, 0.1),
            ("shoutbox", 2, 0.6), ("feed", 1, 1.1), ("top 10", 1, 0.0),
        ]
        for name, rail_i, dy in mods:
            t = Text(name, font_size=SMALL_FONT, color=INK)
            p = RoundedRectangle(corner_radius=0.15, width=t.width + 0.5,
                                 height=0.7, fill_color=GREEN,
                                 fill_opacity=0.15, stroke_color=GREEN,
                                 stroke_width=2)
            g = VGroup(p, t.move_to(p.get_center()))
            g.move_to([xs[rail_i], -0.5 + dy, 0])
            if g.width > widths[rail_i] - 0.4:
                g.scale((widths[rail_i] - 0.4) / g.width)
            self.play(FadeIn(g), run_time=0.5)
        self.wait(1.2)


class M09_B07Judge(Scene):
    def construct(self):
        note = Text("more spacing", font_size=BODY_FONT, color=INK
                    ).move_to(LEFT * 3.4 + UP * 0.8)
        plate = RoundedRectangle(corner_radius=0.2, width=note.width + 1.2,
                                 height=1.4, fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3,
                                 ).move_to(note.get_center())
        self.play(FadeIn(plate), FadeIn(note), run_time=0.6)
        arr = Arrow(LEFT * 1.4 + UP * 0.8, RIGHT * 1.2 + UP * 0.8,
                    color=ACCENT, stroke_width=8, buff=0.1)
        stamp_t = Text("one more pass", font_size=BODY_FONT, color=ACCENT)
        stamp_p = RoundedRectangle(corner_radius=0.2,
                                   width=stamp_t.width + 1.0, height=1.4,
                                   fill_opacity=0, stroke_color=ACCENT,
                                   stroke_width=4).move_to(
                                       RIGHT * 3.6 + UP * 0.8)
        stamp = VGroup(stamp_p, stamp_t.move_to(stamp_p.get_center()))
        self.play(Create(arr), run_time=0.6)
        self.play(Create(stamp), run_time=0.7)
        cap = Text("specific feedback, specific direction", font_size=SMALL_FONT,
                   color=GREY).to_edge(DOWN, buff=1.0)
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(1.2)


class M10_B08Iterate(Scene):
    def construct(self):
        title = Text("draft vs ceiling", font_size=TITLE_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)
        base = Line(LEFT * 5 + DOWN * 2.4, RIGHT * 5 + DOWN * 2.4,
                    color=INK, stroke_width=4)
        self.play(Create(base), run_time=0.5)
        b1 = Rectangle(width=1.8, height=1.2, fill_color=GREY,
                       fill_opacity=0.6, stroke_width=0
                       ).move_to(LEFT * 2.6 + DOWN * 2.4 + UP * 0.6)
        b2 = Rectangle(width=1.8, height=3.4, fill_color=ACCENT,
                       fill_opacity=0.85, stroke_width=0
                       ).move_to(RIGHT * 2.6 + DOWN * 2.4 + UP * 1.7)
        l1 = Text("single-shot", font_size=SMALL_FONT, color=INK
                  ).next_to(b1, DOWN, buff=0.3)
        l2 = Text("iterate", font_size=SMALL_FONT, color=INK
                  ).next_to(b2, DOWN, buff=0.3)
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.7)
        self.wait(1.2)


class M11_B09Mobile(Scene):
    def construct(self):
        title = Text("mobile-friendly", font_size=BODY_FONT,
                     color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.6)
        phone = RoundedRectangle(corner_radius=0.4, width=3.4, height=5.6,
                                 stroke_color=INK, stroke_width=5,
                                 fill_color=CARD, fill_opacity=1
                                 ).move_to(DOWN * 0.2)
        self.play(Create(phone), run_time=0.7)
        stack = VGroup(*[
            Rectangle(width=2.6, height=1.1, stroke_color=BLUE, stroke_width=3,
                      fill_color=BLUE, fill_opacity=0.12
                      ).move_to(phone.get_center() + UP * (1.5 - 1.35 * i))
            for i in range(3)
        ])
        for s in stack:
            self.play(FadeIn(s), run_time=0.4)
        cm = check_mark(phone.get_center() + RIGHT * 2.9, scale=0.6)
        cap = Text("columns collapse", font_size=SMALL_FONT, color=GREY
                   ).next_to(phone, DOWN, buff=0.35)
        self.play(Create(cm), FadeIn(cap), run_time=0.7)
        self.wait(1.2)


class M12_BvdtHtfOut(Scene):
    def construct(self):
        # phase 1: recap
        head = Text("recap", font_size=TITLE_FONT,
                    color=INK).to_edge(UP, buff=0.7)
        self.play(FadeIn(head), run_time=0.5)
        lines = [
            "Act 1: reads screenshots — 100% on Japanese text.",
            "Act 2: reference image + system instruction = a whole website.",
            "Act 3: never single-shot; judge, feedback, requirements up front.",
        ]
        shown = VGroup()
        y = 1.3
        for ln in lines:
            dot = bullet(ORIGIN)
            t = Text(ln, font_size=SMALL_FONT, color=INK)
            if t.width > 10.6:
                t.scale(10.6 / t.width)
            row = VGroup(dot, t).arrange(RIGHT, buff=0.35, aligned_edge=UP)
            row.move_to([0, y, 0])
            self.play(FadeIn(row), run_time=0.6)
            shown.add(row)
            y -= 1.0
        self.wait(0.8)
        self.play(FadeOut(head), FadeOut(shown), run_time=0.5)
        # phase 2: your turn
        card = title_card("screenshot it. transcribe it.",
                          "What did it get right? What did it miss?")
        self.play(FadeIn(card), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(card), run_time=0.5)
        # phase 3: outro
        out = title_card("Muse Can See", "@NikBearBrown")
        nxt = Text("Next: Thinking on Canvas", font_size=BODY_FONT,
                   color=GREY).next_to(out, DOWN, buff=0.6)
        self.play(FadeIn(out), run_time=0.7)
        self.play(FadeIn(nxt), run_time=0.6)
        self.wait(1.2)
