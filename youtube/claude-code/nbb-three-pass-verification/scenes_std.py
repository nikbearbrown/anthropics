from manim import *
import numpy as np

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


def _fit(mobj, max_width):
    if mobj.width > max_width:
        mobj.scale(max_width / mobj.width)
    return mobj


class Scene_B01_NbbThreePass(Scene):
    """B01 PROBLEM — three-stack card: Tests / The Gap / Pass 3."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("PROBLEM", font_size=24, color=INK, font=FONT).to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=3).shift(UP * 1.6)
        self.play(Create(spark), run_time=0.2)

        line1 = _fit(Text("Tests verify code against tests.", font_size=34, color=INK, font=FONT), 11.0).shift(UP * 0.9)
        line2 = _fit(Text("A human reading the SDD aloud catches the gap:", font_size=28, color=INK, font=FONT), 11.0).shift(UP * 0.0)
        line3 = _fit(Text("what was built vs. what was needed.", font_size=28, color=INK, font=FONT), 11.0).shift(DOWN * 0.7)
        line4 = _fit(Text("Pass 3 is the pass the test runner cannot run.", font_size=32, color=TERRA, font=FONT), 11.0).shift(DOWN * 1.7)

        self.play(Write(line1), run_time=0.5)
        self.play(Write(line2), run_time=0.4)
        self.play(Write(line3), run_time=0.4)
        self.play(Write(line4), run_time=0.5)
        self.wait(max(0.01, 8.0))


class Scene_B04_NbbThreePass(Scene):
    """B04 OUTPUT — three-pass verdict panel with PASS/FAIL badges."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("OUTPUT", font_size=24, color=INK, font=FONT).to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        rows = [
            ("Pass  1", "functional — happy path",        "PASS", INK),
            ("Pass  2", "edge case: empty state",         "FAIL", TERRA),
            ("Pass  3", "SDD  gap: two clicks deep",      "FAIL", TERRA),
        ]

        row_h = 1.05
        y_top = 1.5
        for i, (label, note, badge, badge_color) in enumerate(rows):
            y = y_top - i * row_h
            box = Rectangle(width=11.0, height=0.9, color=INK, stroke_width=1.5,
                            fill_color=BG, fill_opacity=1).move_to([0, y, 0])
            lbl = Text(label, font_size=30, color=INK, font=FONT, weight=BOLD).move_to(box).align_to(box, LEFT).shift(RIGHT * 0.3)
            note_t = _fit(Text(note, font_size=26, color=INK, font=FONT), 6.0).move_to(box).align_to(box, LEFT).shift(RIGHT * 2.2)
            badge_t = Text(badge, font_size=28, color=badge_color, font=FONT, weight=BOLD).move_to(box).align_to(box, RIGHT).shift(LEFT * 0.4)
            self.play(FadeIn(box), Write(lbl), Write(note_t), FadeIn(badge_t), run_time=0.5)

        note = _fit(Text("Loop back to Pass 1 recommended.", font_size=26, color=INK, font=FONT), 10.0).to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.5)
        self.wait(max(0.01, 14.0))


class Scene_B06_NbbThreePass(Scene):
    """B06 OUTPUT — verdict card after amending SDD."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("OUTPUT", font_size=24, color=INK, font=FONT).to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        spark = Line(LEFT * 0.6, RIGHT * 0.6, color=TERRA, stroke_width=3).shift(UP * 1.6)
        self.play(Create(spark), run_time=0.2)

        line1 = _fit(Text("Pass 3 re-run: all needs satisfied.", font_size=36, color=TERRA, font=FONT), 11.0).shift(UP * 0.9)
        line2 = _fit(Text("\"At a glance\" was removed from the SDD,", font_size=28, color=INK, font=FONT), 11.0).shift(UP * 0.1)
        line3 = _fit(Text("not added to the build.", font_size=28, color=INK, font=FONT), 11.0).shift(DOWN * 0.6)
        line4 = _fit(Text("Done is relative to the spec.", font_size=32, color=INK, font=FONT), 11.0).shift(DOWN * 1.6)

        self.play(Write(line1), run_time=0.5)
        self.play(Write(line2), run_time=0.4)
        self.play(Write(line3), run_time=0.4)
        self.play(Write(line4), run_time=0.5)
        self.wait(max(0.01, 10.0))


class Scene_B07_NbbThreePass(Scene):
    """B07 SUMMARY — the three-pass protocol as a labeled column."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("SUMMARY", font_size=24, color=INK, font=FONT).to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = _fit(Text("The three-pass protocol", font_size=36, color=INK, font=FONT), 11.0).shift(UP * 2.0)
        self.play(Write(title), run_time=0.4)

        rows = [
            ("Pass  1", "functional",   "test  runner"),
            ("Pass  2", "edge cases",   "test  runner"),
            ("Pass  3", "SDD  needs",   "human, aloud"),
        ]
        y_top = 0.8
        row_h = 1.15
        for i, (label, kind, who) in enumerate(rows):
            y = y_top - i * row_h
            color = TERRA if i == 2 else INK
            box = Rectangle(width=10.0, height=0.95, color=color, stroke_width=1.5,
                            fill_color=BG, fill_opacity=1).move_to([0, y, 0])
            lbl = Text(label, font_size=30, color=color, font=FONT, weight=BOLD).move_to(box).align_to(box, LEFT).shift(RIGHT * 0.3)
            kind_t = _fit(Text(kind, font_size=26, color=INK, font=FONT), 4.5).move_to(box).align_to(box, LEFT).shift(RIGHT * 2.0)
            who_t = _fit(Text(who, font_size=26, color=color, font=FONT), 4.5).move_to(box).align_to(box, RIGHT).shift(LEFT * 0.4)
            self.play(FadeIn(box), Write(lbl), Write(kind_t), Write(who_t), run_time=0.45)

        self.wait(max(0.01, 8.0))


class Scene_B08_NbbThreePass(Scene):
    """B08 NEXT STEPS — bridge card to the next reel."""
    def construct(self):
        self.camera.background_color = BG
        act = Text("NEXT  STEPS", font_size=24, color=INK, font=FONT).to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        spark = Line(LEFT * 0.8, RIGHT * 0.8, color=TERRA, stroke_width=3).shift(UP * 0.9)
        self.play(Create(spark), run_time=0.2)

        line1 = _fit(Text("Next:", font_size=32, color=INK, font=FONT), 11.0).shift(UP * 0.1)
        line2 = _fit(Text("demonstrate the solve-verify asymmetry.", font_size=38, color=TERRA, font=FONT), 11.0).shift(DOWN * 0.9)

        self.play(Write(line1), run_time=0.4)
        self.play(Write(line2), run_time=0.6)
        self.wait(max(0.01, 5.0))
