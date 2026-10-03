"""scenes.py — Muse in Code (Film 7). Manim visuals, 1920x1080."""
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


def title_card(title, sub=None):
    g = VGroup()
    t = Text(title, color=INK, font_size=64).move_to(ORIGIN)
    g.add(t)
    if sub:
        s = Text(sub, color=GREY, font_size=36).next_to(t, DOWN, buff=0.4)
        g.add(s)
    return g


def check_mark(pos, scale=0.5, color=GREEN):
    l1 = Line(LEFT * 0.25 + DOWN * 0.1, ORIGIN, color=color, stroke_width=8)
    l2 = Line(ORIGIN, RIGHT * 0.5 + UP * 0.35, color=color, stroke_width=8)
    g = VGroup(l1, l2).scale(scale).move_to(pos)
    return g


def cross_mark(pos, scale=0.6, color=ACCENT):
    l1 = Line(LEFT * 0.4 + DOWN * 0.4, RIGHT * 0.4 + UP * 0.4,
              color=color, stroke_width=10)
    l2 = Line(LEFT * 0.4 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.4,
              color=color, stroke_width=10)
    return VGroup(l1, l2).scale(scale).move_to(pos)


def bullet(pos, color=ACCENT, r=0.12):
    return Dot(pos, radius=r, color=color)


def card(text, w=5.0, h=1.2, fs=34, color=INK):
    r = RoundedRectangle(width=w, height=h, corner_radius=0.15,
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=GREY, stroke_width=2)
    t = Text(text, color=color, font_size=fs).move_to(r.get_center())
    return VGroup(r, t)


def section_head(text):
    return Text(text, color=INK, font_size=48).to_edge(UP, buff=0.7)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Muse in Code")
        hook = title_card("from the playground to a program")
        box = RoundedRectangle(width=3.2, height=2.0, corner_radius=0.2,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=BLUE, stroke_width=4)
        box.move_to(LEFT * 3.5)
        arrow = Arrow(LEFT * 1.6, RIGHT * 0.6, color=ACCENT, stroke_width=10,
                      buff=0.2)
        dot = bullet(RIGHT * 3.5, color=GREEN, r=0.3)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(box), run_time=0.5)
        self.play(Write(hook), run_time=1.0)
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(FadeIn(dot), run_time=0.5)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Four terms")
        terms = [
            ("API key", "a secret string that says who you are"),
            ("Base URL", "the address your code calls"),
            ("SDK", "a wrapper around raw HTTP"),
            ("REST", "talking to the API directly"),
        ]
        cards = VGroup(*[
            card(f"{t} — {d}", w=9.5, h=1.0, fs=30)
            for t, d in terms
        ]).arrange(DOWN, buff=0.35).next_to(head, DOWN, buff=0.6)
        self.play(FadeIn(head), run_time=0.6)
        for i, c in enumerate(cards):
            d = bullet(c.get_left() + LEFT * 0.5 + UP * 0.0, color=ACCENT)
            self.play(FadeIn(c), FadeIn(d), run_time=0.6)
        self.wait(1.2)


class M03_B01Key(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 1 — the key")
        ring = Circle(radius=0.5, color=ACCENT, stroke_width=10)
        stem = Line(ring.get_bottom(), ring.get_bottom() + DOWN * 1.2,
                    color=ACCENT, stroke_width=10)
        tooth1 = Line(stem.get_end(), stem.get_end() + RIGHT * 0.4,
                      color=ACCENT, stroke_width=10)
        tooth2 = Line(stem.get_end() + UP * 0.35,
                      stem.get_end() + UP * 0.35 + RIGHT * 0.4,
                      color=ACCENT, stroke_width=10)
        key = VGroup(ring, stem, tooth1, tooth2).move_to(LEFT * 3.5)
        masked = card("copy it once", w=4.6, h=1.4, fs=36).move_to(RIGHT * 3.0)
        self.play(FadeIn(head), run_time=0.6)
        self.play(Create(ring), run_time=0.5)
        self.play(Create(stem), Create(tooth1), Create(tooth2), run_time=0.6)
        self.play(FadeIn(masked), run_time=0.6)
        self.wait(1.2)


class M04_B02Url(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 1 — the address")
        left = card("base URL", w=3.6, h=1.3, fs=36).move_to(LEFT * 3.6)
        v1 = Text("/v1", color=ACCENT, font_size=44).next_to(left, DOWN,
                                                            buff=0.4)
        strike = Line(v1.get_left() + LEFT * 0.2, v1.get_right() + RIGHT * 0.2,
                      color=ACCENT, stroke_width=8)
        arrow = Arrow(LEFT * 1.2, RIGHT * 1.2, color=ACCENT, stroke_width=10,
                      buff=0.2)
        right = card("muse base url — no /v1", w=5.2, h=1.3,
                     fs=32).move_to(RIGHT * 3.4)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(left), FadeIn(v1), run_time=0.6)
        self.play(Create(strike), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(right), run_time=0.6)
        self.wait(1.2)


class M05_B03Rest(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 2 — way one: raw REST")
        post = card("POST", w=2.6, h=1.4, fs=44, color=BLUE).move_to(LEFT * 3.8)
        js = card("JSON", w=2.6, h=1.4, fs=44,
                  color=GREEN).move_to(RIGHT * 3.8)
        fwd = Arrow(post.get_right(), js.get_left(), color=ACCENT,
                    stroke_width=10, buff=0.3).shift(UP * 0.35)
        back = Arrow(js.get_left(), post.get_right(), color=GREY,
                     stroke_width=10, buff=0.3).shift(DOWN * 0.35)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(post), run_time=0.5)
        self.play(GrowArrow(fwd), run_time=0.5)
        self.play(FadeIn(js), run_time=0.5)
        self.play(GrowArrow(back), run_time=0.5)
        self.wait(1.2)


class M06_B04Openai(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 2 — way two: the OpenAI SDK")
        left = card("same call", w=3.4, h=1.4, fs=36).move_to(LEFT * 3.4)
        right = card("base URL", w=3.4, h=1.4, fs=36).move_to(RIGHT * 3.4)
        arrow = Arrow(left.get_right(), right.get_left(), color=ACCENT,
                      stroke_width=10, buff=0.3)
        note = Text("the code doesn't change", color=GREY,
                    font_size=34).next_to(arrow, DOWN, buff=0.4)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(left), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(right), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.2)


class M07_B05Anthropic(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 2 — way three: the Anthropic SDK")
        rows = VGroup(*[
            card(t, w=6.4, h=1.0, fs=32)
            for t in ["role: system", "role: user", "max tokens"]
        ]).arrange(DOWN, buff=0.35).next_to(head, DOWN, buff=0.6)
        self.play(FadeIn(head), run_time=0.6)
        for r in rows:
            d = bullet(r.get_left() + LEFT * 0.5, color=BLUE)
            self.play(FadeIn(r), FadeIn(d), run_time=0.6)
        self.wait(1.2)


class M08_B06Errors(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 2 — read the errors")
        rows = VGroup(*[
            card(t, w=6.0, h=1.1, fs=34)
            for t in ["bad key", "malformed messages"]
        ]).arrange(DOWN, buff=0.4).move_to(LEFT * 2.2)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(rows[0]), run_time=0.5)
        chk1 = check_mark(rows[0].get_right() + RIGHT * 0.7, scale=0.7)
        self.play(Create(chk1), run_time=0.5)
        self.play(FadeIn(rows[1]), run_time=0.5)
        chk2 = check_mark(rows[1].get_right() + RIGHT * 0.7, scale=0.7)
        self.play(Create(chk2), run_time=0.5)
        self.wait(1.2)


class M09_B07RestEnough(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 3 — which way?")
        rest = card("REST", w=3.0, h=1.4, fs=44, color=BLUE).move_to(LEFT * 2.6)
        sdk = card("SDK", w=3.0, h=1.4, fs=44, color=GREY).move_to(RIGHT * 2.6)
        ring = Circle(radius=1.15, color=ACCENT, stroke_width=8)
        ring.move_to(rest.get_center())
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(rest), FadeIn(sdk), run_time=0.6)
        self.play(Create(ring), run_time=0.6)
        self.wait(1.2)


class M10_B08NoSdk(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Act 3 — no first-party SDK")
        box = card("first-party SDK", w=5.2, h=1.4, fs=36)
        box.move_to(UP * 0.8)
        cross = cross_mark(box.get_center(), scale=1.0)
        claim = card("the API is the SDK", w=5.6, h=1.3, fs=36,
                     color=GREEN).move_to(DOWN * 1.4)
        self.play(FadeIn(head), run_time=0.6)
        self.play(FadeIn(box), run_time=0.5)
        self.play(Create(cross), run_time=0.5)
        self.play(FadeIn(claim), run_time=0.6)
        self.wait(1.2)


class M11_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = section_head("Recap")
        rows = VGroup(*[
            card(t, w=8.6, h=1.0, fs=30)
            for t in ["act one — key, base URL",
                      "act two — three ways, errors",
                      "act three — REST is enough"]
        ]).arrange(DOWN, buff=0.3).next_to(head, DOWN, buff=0.5)
        self.play(FadeIn(head), run_time=0.5)
        for r in rows:
            self.play(FadeIn(r), run_time=0.4)
            chk = check_mark(r.get_right() + RIGHT * 0.6, scale=0.55)
            self.play(Create(chk), run_time=0.4)
        self.play(FadeOut(rows), FadeOut(head), run_time=0.6)
        todo = card("tonight: one API call", w=6.4, h=1.4, fs=38)
        todo.move_to(ORIGIN)
        d = bullet(todo.get_left() + LEFT * 0.6, color=ACCENT, r=0.18)
        self.play(FadeIn(todo), FadeIn(d), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(todo), FadeOut(d), run_time=0.6)
        out = title_card("@NikBearBrown", "Next film: Agents and Frameworks")
        self.play(Write(out), run_time=1.0)
        self.wait(1.2)
