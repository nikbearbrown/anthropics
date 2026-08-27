from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class B01_ClaudeLiamPlan(Scene):
    """Beat B01 — SHOW: bar/proportion chart. Narration: Check one: does any step modify, rename, or delete originals? If yes, is there a"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "RISKY-STEP":
            act = Text("RISKY-STEP", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
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

        lbl1 = Text("Check one: does any step modify, rename, or delete originals"[:30], font_size=40, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("\'Delete duplicates\' is a write operation"[:30] if "\'Delete duplicates\' is a write operation" else "Comparison", font_size=40, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "\'Move to archive\' is a write operation":
            note = Text("\'Move to archive\' is a write operation"[:60], font_size=40, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.00))


class B02_ClaudeLiamPlan(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: Check two: is there a step where a human sees the output before it becomes final"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "MISSING-VERIFICATION":
            act = Text("MISSING-VERIFICATION", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Check two: is there a step where a human sees the output bef":
            line1 = Text("Check two: is there a step where a human sees the output bef", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "If every step runs to completion before you see anything, ve":
            line2 = Text("If every step runs to completion before you see anything, ve", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Check two: is there a step where a human sees the output bef":
            uline = Line(LEFT * min(4.0, len("Check two: is there a step where a human sees the output bef") * 0.18), RIGHT * min(4.0, len("Check two: is there a step where a human sees the output bef") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class B03_ClaudeLiamPlan(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: If the plan has a problem, do not approve and hope. Redirect. The redirect form:"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "REDIRECT-FORM":
            act = Text("REDIRECT-FORM", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "If the plan has a problem, do not approve and hope":
            line1 = Text("If the plan has a problem, do not approve and hope", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The redirect form: \'Do not act yet":
            line2 = Text("The redirect form: \'Do not act yet", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Add a backup step after step three that copies originals to ":
            line3 = Text("Add a backup step after step three that copies originals to ", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "If the plan has a problem, do not approve and hope":
            uline = Line(LEFT * min(4.0, len("If the plan has a problem, do not approve and hope") * 0.18), RIGHT * min(4.0, len("If the plan has a problem, do not approve and hope") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))
