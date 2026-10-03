from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_AgenticLoopNot(Scene):
    """Beat B01 — SHOW: bar/proportion chart. Narration: Claude.ai is turn-based. You type. The model produces text. You read. You decide"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "TWO-MODELS":
            act = Text("TWO-MODELS", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("ai is turn-based"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The model produces text"[:30] if "The model produces text" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "You decide what to do":
            note = Text("You decide what to do"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.00))


class Scene_B02_AgenticLoopNot(Scene):
    """Beat B02 — SHOW: five calibration questions as a numbered enumeration."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("FIVE QUESTIONS", font_size=28, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        questions = [
            "1.   What  files  are  here?",
            "2.   What  is  this  project  for?",
            "3.   What  would  you  change?",
            "4.   What  would  you  not  change?",
            "5.   What  are  you  uncertain  about?",
        ]

        lines = VGroup(*[
            Text(q, font_size=36, color="#3D3929", font=font)
            for q in questions
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        lines.next_to(act, DOWN, buff=0.8)

        for line in lines:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)

        caption = Text("Ten  minutes.   Hours  saved.", font_size=30, color="#D97757", font=font)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.5)

        self.wait(max(0.01, 11.00))


class Scene_B03_AgenticLoopNot(Scene):
    """Beat B03 — SHOW: contrast card, Skip vs Calibrate consequences."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("CALIBRATION DISCIPLINE", font_size=28, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.5)
        self.play(FadeIn(act), run_time=0.3)

        skip_hdr = Text("Skip", font_size=44, color="#3D3929", font=font)
        cal_hdr  = Text("Calibrate", font_size=44, color="#D97757", font=font)

        # Doubled spaces defeat the EB-Garamond zero-width space bug at small sizes.
        skip_items = [
            "dependency  you  did  not  install",
            "config  edit  that  breaks  another  repo",
            "structure  you  did  not  expect",
        ]
        cal_items = [
            "know  what  Claude  sees",
            "correct  wrong  assumptions",
            "first  file  change  is  on  purpose",
        ]

        skip_lines = VGroup(*[
            Text("—   " + s, font_size=28, color="#3D3929", font=font)
            for s in skip_items
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        cal_lines = VGroup(*[
            Text("—   " + s, font_size=28, color="#3D3929", font=font)
            for s in cal_items
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        skip_col = VGroup(skip_hdr, skip_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        cal_col  = VGroup(cal_hdr,  cal_lines ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        cols = VGroup(skip_col, cal_col).arrange(RIGHT, buff=1.3, aligned_edge=UP)
        cols.next_to(act, DOWN, buff=0.7)

        self.play(FadeIn(skip_hdr), FadeIn(cal_hdr), run_time=0.4)
        for a, b in zip(skip_lines, cal_lines):
            self.play(Write(a), run_time=0.35)
            self.play(Write(b), run_time=0.35)

        caption = Text("First  session:  calibrate,  not  build.", font_size=30, color="#3D3929", font=font)
        caption.to_edge(DOWN, buff=0.5)
        self.play(Write(caption), run_time=0.5)

        self.wait(max(0.01, 10.00))
