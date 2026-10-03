"""scenes.py — Muse Code, the Harness (Film 9). Manim visuals, house template."""
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


def terminal_window(pos, width=7.0, height=3.6):
    frame = RoundedRectangle(corner_radius=0.2, width=width, height=height,
                             fill_color=INK, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    bar = RoundedRectangle(corner_radius=0.12, width=width - 0.3, height=0.5,
                           fill_color=GREY, fill_opacity=1,
                           stroke_color=GREY, stroke_width=1)
    bar.move_to(frame.get_top() + DOWN * 0.32)
    return VGroup(frame, bar)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("Meta's own coding harness")
        card.shift(LEFT * 1.4)
        term = terminal_window(RIGHT * 4.6 + DOWN * 0.4, width=3.6, height=2.6)
        self.play(FadeIn(card, shift=DOWN * 0.3))
        self.play(Create(term), run_time=0.8)
        self.play(card.animate.shift(RIGHT * 1.4), term.animate.shift(LEFT * 1.4),
                  run_time=1.2)
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(title))
        cards = [
            term_card("Harness", "the loop around the model", LEFT * 2.9 + UP * 1.2),
            term_card("agents.md", "project context", RIGHT * 2.9 + UP * 1.2),
            term_card("Reasoning effort", "low, medium, high, extra high",
                      LEFT * 2.9 + DOWN * 1.3),
            term_card("Session", "work you can resume", RIGHT * 2.9 + DOWN * 1.3),
        ]
        for c in cards:
            d = bullet(c.get_center() + LEFT * 2.9)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d), run_time=0.7)
        self.wait(1.2)


class M03_B01Install(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("one line installs it", font_size=44, color=INK).to_edge(UP, buff=0.7)
        term = terminal_window(ORIGIN + DOWN * 0.3, width=8.6, height=3.2)
        cmd = Text("$ one line, run once", font_size=38, color=CARD)
        cmd.move_to(term[0].get_center() + UP * 0.3)
        cursor = Rectangle(width=0.28, height=0.5, fill_color=GREEN,
                           fill_opacity=1, stroke_color=GREEN)
        cursor.next_to(cmd, RIGHT, buff=0.15)
        self.play(Write(title))
        self.play(Create(term), run_time=0.8)
        self.play(Write(cmd), run_time=1.4)
        self.play(FadeIn(cursor))
        self.play(cursor.animate.set_fill(opacity=0.2), run_time=0.4)
        self.play(cursor.animate.set_fill(opacity=1), run_time=0.4)
        self.wait(1.2)


class M04_B02Launch(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("first launch", font_size=44, color=INK).to_edge(UP, buff=0.7)
        term = terminal_window(ORIGIN + DOWN * 0.4, width=8.6, height=3.6)
        prompt = Text("muse>", font_size=42, color=CARD)
        prompt.move_to(term[0].get_left() + RIGHT * 1.0 + UP * 0.9)
        cursor = Rectangle(width=0.24, height=0.46, fill_color=GREEN,
                           fill_opacity=1, stroke_color=GREEN).next_to(prompt, RIGHT, buff=0.15)
        self.play(Write(title))
        self.play(Create(term), run_time=0.8)
        self.play(Write(prompt), FadeIn(cursor), run_time=0.8)
        files = VGroup(*[
            RoundedRectangle(corner_radius=0.08, width=1.7, height=0.5,
                             fill_color=CARD, fill_opacity=0.9,
                             stroke_color=CARD, stroke_width=1
                             ).move_to(term[0].get_center() + LEFT * 2.6 + i * RIGHT * 2.1 + DOWN * 0.7)
            for i in range(4)
        ])
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.2) for f in files],
                              lag_ratio=0.25), run_time=1.2)
        self.wait(1.2)


class M05_B03Skills(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("skills load from everywhere", font_size=44, color=INK).to_edge(UP, buff=0.7)
        term = terminal_window(ORIGIN + DOWN * 0.3, width=5.4, height=3.4)
        packets = VGroup(*[
            VGroup(
                RoundedRectangle(corner_radius=0.14, width=2.6, height=1.0,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=3),
                Text(label, font_size=28, color=INK),
            )
            for label in ("project", "home", "community")
        ])
        packets[0].move_to(LEFT * 5.2 + UP * 1.6)
        packets[1].move_to(RIGHT * 5.2 + UP * 1.6)
        packets[2].move_to(DOWN * 3.2)
        self.play(Write(title))
        self.play(Create(term), run_time=0.8)
        for p in packets:
            self.play(p.animate.move_to(term[0].get_center()), run_time=0.9)
            self.play(FadeOut(p), run_time=0.3)
        check = check_mark(term[0].get_center() + UP * 1.0, scale=0.5)
        self.play(FadeIn(check, scale=1.5))
        self.wait(1.2)


class M06_B04AgentsMd(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("agents.md: the project's voice", font_size=44, color=INK).to_edge(UP, buff=0.7)
        plate = RoundedRectangle(corner_radius=0.2, width=7.6, height=4.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2)
        plate.move_to(DOWN * 0.3)
        fname = Text("agents.md", font_size=36, color=ACCENT)
        fname.move_to(plate.get_top() + DOWN * 0.55)
        rows = ["what's this repo", "how to build it", "what are the rules"]
        row_grp = VGroup()
        for i, r in enumerate(rows):
            d = bullet(plate.get_left() + RIGHT * 0.7 + DOWN * (1.5 + i * 0.85) + UP * 0.3)
            t = Text(r, font_size=30, color=INK).next_to(d, RIGHT, buff=0.25)
            row_grp.add(VGroup(d, t))
        self.play(Write(title))
        self.play(FadeIn(plate, shift=DOWN * 0.3))
        self.play(Write(fname), run_time=0.7)
        for r in row_grp:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(1.2)


class M07_B05Settings(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("settings.json: the global rules", font_size=44, color=INK).to_edge(UP, buff=0.7)
        plate = RoundedRectangle(corner_radius=0.2, width=8.2, height=3.8,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2)
        plate.move_to(DOWN * 0.3)
        keys = VGroup(
            Text("reasoning_effort: medium", font_size=32, color=INK),
            Text("trust: ~/projects", font_size=32, color=INK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(plate.get_center())
        keyring = Circle(radius=0.5, color=ACCENT, stroke_width=6).next_to(plate, RIGHT, buff=0.6)
        self.play(Write(title))
        self.play(FadeIn(plate, shift=DOWN * 0.3))
        self.play(Write(keys[0]), run_time=0.8)
        self.play(Write(keys[1]), run_time=0.8)
        self.play(Create(keyring))
        self.wait(1.2)


class M08_B06Effort(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("reasoning effort: four stops", font_size=44, color=INK).to_edge(UP, buff=0.7)
        stops = ["low", "medium", "high", "extra high"]
        dial = VGroup()
        for i, s in enumerate(stops):
            seg = RoundedRectangle(corner_radius=0.16, width=2.6, height=1.3,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2)
            seg.move_to(LEFT * 4.5 + i * RIGHT * 3.0 + UP * 0.9)
            lab = Text(s, font_size=32, color=INK).move_to(seg.get_center())
            dial.add(VGroup(seg, lab))
        ring = RoundedRectangle(corner_radius=0.2, width=2.9, height=1.6,
                                fill_opacity=0, stroke_color=ACCENT, stroke_width=6)
        ring.move_to(dial[0].get_center())
        bar_bg = RoundedRectangle(corner_radius=0.1, width=9.0, height=0.55,
                                  fill_color=GREY, fill_opacity=0.5,
                                  stroke_color=GREY, stroke_width=1).move_to(DOWN * 1.9)
        bar = RoundedRectangle(corner_radius=0.1, width=1.2, height=0.55,
                               fill_color=ACCENT, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=1)
        bar.move_to(bar_bg.get_left() + RIGHT * 0.6)
        self.play(Write(title))
        self.play(LaggedStart(*[FadeIn(d, shift=UP * 0.2) for d in dial], lag_ratio=0.2),
                  run_time=1.2)
        self.play(FadeIn(ring), FadeIn(bar_bg), FadeIn(bar), run_time=0.6)
        widths = [1.2, 3.4, 5.8, 8.6]
        for i in range(1, 4):
            self.play(ring.animate.move_to(dial[i].get_center()),
                      bar.animate.set_width(widths[i], about_point=bar_bg.get_left()),
                      run_time=0.7)
        self.wait(1.2)


class M09_B07Resume(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("sessions survive", font_size=44, color=INK).to_edge(UP, buff=0.7)
        line = Line(LEFT * 5.5, RIGHT * 5.5, color=GREY, stroke_width=4).move_to(DOWN * 0.3)
        gap_l = LEFT * 1.2 + DOWN * 0.3
        gap_r = RIGHT * 1.2 + DOWN * 0.3
        d1 = Dot(LEFT * 3.4 + DOWN * 0.3, radius=0.28, color=BLUE)
        d2 = Dot(RIGHT * 3.4 + DOWN * 0.3, radius=0.28, color=BLUE)
        arc = CurvedArrow(gap_l, gap_r, angle=-TAU / 3, color=ACCENT, stroke_width=5)
        lab = Text("resume", font_size=32, color=ACCENT).next_to(arc, DOWN, buff=0.25)
        self.play(Write(title))
        self.play(Create(line), run_time=0.7)
        self.play(FadeIn(d1), run_time=0.4)
        self.play(Create(arc), Write(lab), run_time=0.9)
        self.play(FadeIn(d2, scale=1.6), run_time=0.6)
        self.wait(1.2)


class M10_B08Status(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("status, compact, clear", font_size=44, color=INK).to_edge(UP, buff=0.7)
        plate = RoundedRectangle(corner_radius=0.2, width=8.0, height=3.6,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=2)
        plate.move_to(DOWN * 0.3)
        lab = Text("tokens used", font_size=32, color=INK)
        lab.move_to(plate.get_top() + DOWN * 0.7)
        track = RoundedRectangle(corner_radius=0.1, width=6.4, height=0.6,
                                 fill_color=GREY, fill_opacity=0.4,
                                 stroke_color=GREY, stroke_width=1)
        track.next_to(lab, DOWN, buff=0.5)
        fill = RoundedRectangle(corner_radius=0.1, width=6.4 * 0.62, height=0.6,
                                fill_color=BLUE, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=1)
        fill.move_to(track.get_left() + RIGHT * (6.4 * 0.62) / 2)
        pct = Text("context 62%", font_size=30, color=INK).next_to(track, DOWN, buff=0.35)
        arrow = CurvedArrow(track.get_right() + UP * 0.2, track.get_left() + UP * 0.2,
                            angle=TAU / 3, color=ACCENT, stroke_width=5)
        clab = Text("compact", font_size=28, color=ACCENT).next_to(arrow, UP, buff=0.2)
        self.play(Write(title))
        self.play(FadeIn(plate, shift=DOWN * 0.3))
        self.play(Write(lab), run_time=0.6)
        self.play(Create(track), Create(fill), run_time=0.7)
        self.play(Write(pct), run_time=0.6)
        self.play(Create(arrow), Write(clab), run_time=0.8)
        self.play(fill.animate.set_width(6.4 * 0.25, about_point=track.get_left()),
                  pct.animate.become(Text("context 25%", font_size=30, color=INK)
                                     .next_to(track, DOWN, buff=0.35)),
                  run_time=0.9)
        self.wait(1.2)


class M11_B09Yolo(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("YOLO mode", font_size=44, color=INK).to_edge(UP, buff=0.7)
        red = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.4,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=4)
        red.move_to(LEFT * 3.0 + DOWN * 0.3)
        rl = Text("YOLO mode", font_size=36, color=ACCENT).move_to(red.get_center() + UP * 0.9)
        rs = Text("full permissions · no sandbox", font_size=24, color=INK)
        rs.move_to(red.get_center() + DOWN * 0.1)
        tri = Triangle(color=ACCENT, stroke_width=6, fill_opacity=0)
        tri.scale(0.5).move_to(red.get_center() + DOWN * 1.0)
        green = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=GREEN, stroke_width=4)
        green.move_to(RIGHT * 3.0 + DOWN * 0.3)
        gl = Text("a machine you can lose", font_size=30, color=GREEN)
        gl.move_to(green.get_center())
        gcheck = check_mark(green.get_center() + DOWN * 1.0, scale=0.5)
        self.play(Write(title))
        self.play(FadeIn(red, shift=UP * 0.2), run_time=0.6)
        self.play(Write(rl), run_time=0.6)
        self.play(Write(rs), run_time=0.6)
        self.play(Create(tri), run_time=0.6)
        self.play(FadeIn(green, shift=UP * 0.2), run_time=0.6)
        self.play(Write(gl), FadeIn(gcheck, scale=1.5), run_time=0.8)
        self.wait(1.2)


class M12_B10Headless(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("headless mode", font_size=44, color=INK).to_edge(UP, buff=0.7)
        n1 = VGroup(
            RoundedRectangle(corner_radius=0.16, width=3.0, height=1.5,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2),
            Text("prompt", font_size=32, color=INK))
        n1.move_to(LEFT * 4.2 + DOWN * 0.3)
        n2 = VGroup(
            RoundedRectangle(corner_radius=0.16, width=3.0, height=1.5,
                             fill_color=INK, fill_opacity=1,
                             stroke_color=INK, stroke_width=2),
            Text("muse -p", font_size=32, color=CARD))
        n2.move_to(DOWN * 0.3)
        n3 = VGroup(
            RoundedRectangle(corner_radius=0.16, width=3.0, height=1.5,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=BLUE, stroke_width=3),
            Text("JSON", font_size=32, color=INK))
        n3.move_to(RIGHT * 4.2 + DOWN * 0.3)
        a1 = Arrow(n1.get_right(), n2.get_left(), color=ACCENT, stroke_width=6, buff=0.2)
        a2 = Arrow(n2.get_right(), n3.get_left(), color=ACCENT, stroke_width=6, buff=0.2)
        self.play(Write(title))
        self.play(FadeIn(n1, shift=RIGHT * 0.2), run_time=0.6)
        self.play(Create(a1), FadeIn(n2, shift=RIGHT * 0.2), run_time=0.7)
        self.play(Create(a2), FadeIn(n3, shift=RIGHT * 0.2), run_time=0.7)
        self.play(a1.animate.shift(RIGHT * 0.3), rate_func=there_and_back, run_time=0.5)
        self.play(a2.animate.shift(RIGHT * 0.3), rate_func=there_and_back, run_time=0.5)
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        recap_title = Text("the takeaway", font_size=44, color=INK).to_edge(UP, buff=0.7)
        rows = VGroup(*[
            VGroup(bullet(ORIGIN, color=BLUE),
                   Text(t, font_size=30, color=INK).next_to(bullet(ORIGIN), RIGHT, buff=0.3))
            for t in ("one command installs it",
                      "agents.md + settings.json + four effort stops",
                      "sessions resume · YOLO stays on disposable machines · headless is a tool")
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.55).move_to(DOWN * 0.2)
        phase1 = VGroup(recap_title, rows)
        self.play(Write(recap_title))
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(0.8)

        self.play(FadeOut(phase1))
        turn = title_card("your turn: one question", sub="ask it about your own code")
        phase2 = VGroup(turn)
        self.play(FadeIn(turn, shift=UP * 0.2))
        self.wait(0.8)

        self.play(FadeOut(phase2))
        outro = title_card("Muse, in for Bear. Thanks for watching.",
                           sub="Next: Memory, Skills, and Guardrails")
        self.play(FadeIn(outro, shift=UP * 0.2))
        self.wait(1.2)
