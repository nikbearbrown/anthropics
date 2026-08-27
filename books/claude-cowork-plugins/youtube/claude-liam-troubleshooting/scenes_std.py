from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamTroubleshooting(Scene):
    """Beat B01 — frustration → abandonment. Diagnose stays in the game."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 75)
        pt2 = ax.c2p(2, 25)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Diagnose", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Abandon", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Diagnosing is how you stay in the game.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.10))


class Scene_B06_ClaudeLiamTroubleshooting(Scene):
    """Beat B06 — broad default vs your context. Context sharpens output."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 35)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Broad default", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Your context", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Feed the plugin your context and the output sharpens past generic.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.80))


class Scene_B07_ClaudeLiamTroubleshooting(Scene):
    """Beat B07 — big scope vs narrow scope. Narrow scope cuts latency."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 35)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Everything", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("One slice", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Scope to one date range or folder and latency drops with it.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.40))
