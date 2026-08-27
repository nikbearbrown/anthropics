from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B17_ClaudeLiamLegal(Scene):
    """Beat B17 — SHOW: bar/proportion chart. Narration: The health check first: your monthly burn rate, and your runway — how many month"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT IV":
            act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("The health check first: your monthly burn rate, and your run"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("The number you keep avoiding, made plain in seconds"[:30] if "The number you keep avoiding, made plain in seconds" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.70))


class Scene_B18_ClaudeLiamLegal(Scene):
    """Beat B18 — SHOW: bar/proportion chart. Narration: Then the part that earns its keep: scenario modeling. Raise prices by, say, fift"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT IV":
            act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Then the part that earns its keep: scenario modeling"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Raise prices by, say, fifteen percent - where\'s the break-ev"[:30] if "Raise prices by, say, fifteen percent - where\'s the break-ev" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 16.60))


class Scene_B04_ClaudeLiamLegal(Scene):
    """Beat B04 — SHOW: coverage comparison. Narration: Structured first-pass coverage. It won't catch everything a specialist would — but it catches what you'd otherwise miss entirely."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT I", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("First-pass coverage", font_size=34, color=INK, font=font)
        title.shift(UP * 2.8)
        self.play(Write(title), run_time=0.4)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=3.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt_none = ax.c2p(1, 5)
        pt_plugin = ax.c2p(2, 72)
        bar_w = 0.65

        bar_none = Rectangle(width=bar_w, height=abs(pt_none[1]-origin[1]),
                              color=INK, fill_color=INK, fill_opacity=0.25, stroke_width=1)
        bar_none.move_to([pt_none[0], (pt_none[1]+origin[1])/2, 0])

        bar_plugin = Rectangle(width=bar_w, height=abs(pt_plugin[1]-origin[1]),
                                color=TERRA, fill_color=TERRA, fill_opacity=0.85, stroke_width=0)
        bar_plugin.move_to([pt_plugin[0], (pt_plugin[1]+origin[1])/2, 0])

        lbl_none = Text("No review", font_size=22, color=INK, font=font)
        lbl_none.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl_plugin = Text("Plugin first-pass", font_size=22, color=INK, font=font)
        lbl_plugin.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar_none, DOWN), Write(lbl_none), run_time=0.5)
        self.play(GrowFromEdge(bar_plugin, DOWN), Write(lbl_plugin), run_time=0.6)

        spark = Text("Better than no review.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 11.7 - 3.1))


class Scene_B07_ClaudeLiamLegal(Scene):
    """Beat B07 — SHOW: three-color flag chart. Narration: Green for standard terms, yellow for items worth a second look, red for real concerns."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT II", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("Risk flags", font_size=34, color=INK, font=font)
        title.shift(UP * 2.8)
        self.play(Write(title), run_time=0.4)

        ax = Axes(x_range=[0, 4, 1], y_range=[0, 10, 2],
                  x_length=7, y_length=3.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        positions = [1, 2, 3]
        heights   = [7, 5, 3]
        colors    = ["#4CAF50", "#FFA726", "#D32F2F"]
        labels    = ["Standard", "Attention", "Concern"]

        for x, h, col, lbl in zip(positions, heights, colors, labels):
            pt = ax.c2p(x, h)
            bar = Rectangle(width=0.55, height=abs(pt[1]-origin[1]),
                            color=col, fill_color=col, fill_opacity=0.88, stroke_width=0)
            bar.move_to([pt[0], (pt[1]+origin[1])/2, 0])
            text = Text(lbl, font_size=21, color=INK, font=font)
            text.next_to(ax.c2p(x, 0), DOWN, buff=0.25)
            self.play(GrowFromEdge(bar, DOWN), Write(text), run_time=0.55)

        spark = Text("Green, yellow, red.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 14.8 - 3.7))


class Scene_B09_ClaudeLiamLegal(Scene):
    """Beat B09 — SHOW: time comparison. Narration: Thorough reading drops from hours to minutes."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT II", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("Review time", font_size=34, color=INK, font=font)
        title.shift(UP * 2.8)
        self.play(Write(title), run_time=0.4)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=3.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt_hours = ax.c2p(1, 85)
        pt_mins  = ax.c2p(2, 12)
        bar_w = 0.65

        bar_hours = Rectangle(width=bar_w, height=abs(pt_hours[1]-origin[1]),
                               color=INK, fill_color=INK, fill_opacity=0.75, stroke_width=0)
        bar_hours.move_to([pt_hours[0], (pt_hours[1]+origin[1])/2, 0])

        bar_mins = Rectangle(width=bar_w, height=abs(pt_mins[1]-origin[1]),
                              color=TERRA, fill_color=TERRA, fill_opacity=0.85, stroke_width=0)
        bar_mins.move_to([pt_mins[0], (pt_mins[1]+origin[1])/2, 0])

        lbl_hours = Text("Hours", font_size=22, color=INK, font=font)
        lbl_hours.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl_mins = Text("Minutes", font_size=22, color=INK, font=font)
        lbl_mins.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar_hours, DOWN), Write(lbl_hours), run_time=0.6)
        self.play(GrowFromEdge(bar_mins, DOWN), Write(lbl_mins), run_time=0.6)

        arrow = Arrow(ax.c2p(1.35, 55), ax.c2p(1.65, 20), color=TERRA, stroke_width=3)
        self.play(Create(arrow), run_time=0.4)

        spark = Text("Review as default.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 13.1 - 3.3))


class Scene_B13_ClaudeLiamLegal(Scene):
    """Beat B13 — SHOW: triage branch. Narration: Routine and low-stakes, the screen is enough. Complex, or high-stakes, and a red flag is your signal to escalate."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT III", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("Triage", font_size=40, color=INK, font=font)
        title.shift(UP * 2.5)
        self.play(Write(title), run_time=0.4)

        line = Line([-3.5, 0.2, 0], [3.5, 0.2, 0], color=INK, stroke_width=1.5)
        self.play(Create(line), run_time=0.3)

        # Left column — routine
        left_head = Text("Routine", font_size=30, color=INK, font=font, weight=BOLD)
        left_head.shift(LEFT * 2.5 + UP * 1.2)
        left_body = Text("Screen is enough", font_size=26, color=INK, font=font)
        left_body.shift(LEFT * 2.5 + DOWN * 0.2)

        # Right column — high stakes
        right_head = Text("High-stakes", font_size=30, color=TERRA, font=font, weight=BOLD)
        right_head.shift(RIGHT * 2.0 + UP * 1.2)
        right_body = Text("Escalate to a person", font_size=26, color=INK, font=font)
        right_body.shift(RIGHT * 2.0 + DOWN * 0.2)

        self.play(Write(left_head), run_time=0.4)
        self.play(Write(left_body), run_time=0.4)
        self.play(Write(right_head), run_time=0.4)
        self.play(Write(right_body), run_time=0.4)

        spark = Text("Know which you're in.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 11.7 - 3.5))


class Scene_B21_ClaudeLiamLegal(Scene):
    """Beat B21 — SHOW: accelerator vs CFO distinction. Narration: Finance plugin gives analysis a CFO would produce — but the consequential call stays with a human."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT IV", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        line = Line([-0.1, 2.5, 0], [-0.1, -1.5, 0], color=INK, stroke_width=1.5)
        self.play(Create(line), run_time=0.3)

        left_head = Text("Plugin", font_size=30, color=INK, font=font, weight=BOLD)
        left_head.shift(LEFT * 2.5 + UP * 1.8)
        left_body = Text("The analysis", font_size=26, color=INK, font=font)
        left_body.shift(LEFT * 2.5 + UP * 0.9)
        left_sub = Text("burn rate, runway,\nscenario outputs", font_size=22, color=INK, font=font)
        left_sub.shift(LEFT * 2.5 + DOWN * 0.3)

        right_head = Text("Human", font_size=30, color=TERRA, font=font, weight=BOLD)
        right_head.shift(RIGHT * 2.0 + UP * 1.8)
        right_body = Text("The decision", font_size=26, color=INK, font=font)
        right_body.shift(RIGHT * 2.0 + UP * 0.9)
        right_sub = Text("hire, cut, commit —\nyour call", font_size=22, color=INK, font=font)
        right_sub.shift(RIGHT * 2.0 + DOWN * 0.3)

        self.play(Write(left_head), run_time=0.3)
        self.play(Write(left_body), Write(left_sub), run_time=0.5)
        self.play(Write(right_head), run_time=0.3)
        self.play(Write(right_body), Write(right_sub), run_time=0.5)

        spark = Text("The call stays human.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 12.1 - 3.5))


class Scene_B23_ClaudeLiamLegal(Scene):
    """Beat B23 — SHOW: cost-rises-over-time curve. Narration: The cost of fixing it climbs the longer it hides. Monthly reviews and automatic screening catch it while it's still cheap."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT V", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        title = Text("Cost of a hidden problem", font_size=32, color=INK, font=font)
        title.shift(UP * 2.8)
        self.play(Write(title), run_time=0.4)

        ax = Axes(x_range=[0, 6, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=3.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  x_axis_config={"include_tip": False},
                  y_axis_config={"include_tip": False},
                  tips=False)
        ax.shift(DOWN * 0.4)

        x_label = Text("Time hidden →", font_size=20, color=INK, font=font)
        x_label.next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = Text("Cost →", font_size=20, color=INK, font=font)
        y_label.next_to(ax.y_axis.get_end(), UP, buff=0.1)

        self.play(Create(ax), Write(x_label), Write(y_label), run_time=0.5)

        curve = ax.plot(lambda x: 3 * (np.exp(0.6 * x) - 1),
                        x_range=[0, 5.5], color=TERRA, stroke_width=3)
        self.play(Create(curve), run_time=1.0)

        # Mark "catch early" point
        early_dot = Dot(ax.c2p(1, 3*(np.exp(0.6)-1)), color="#4CAF50", radius=0.12)
        early_lbl = Text("catch early\n(cheap)", font_size=19, color=INK, font=font)
        early_lbl.next_to(early_dot, UP+RIGHT, buff=0.15)

        late_dot = Dot(ax.c2p(5, 3*(np.exp(3)-1)), color="#D32F2F", radius=0.12)
        late_lbl = Text("catch late\n(expensive)", font_size=19, color=INK, font=font)
        late_lbl.next_to(late_dot, LEFT+UP, buff=0.15)

        self.play(FadeIn(early_dot), Write(early_lbl), run_time=0.4)
        self.play(FadeIn(late_dot), Write(late_lbl), run_time=0.4)

        spark = Text("Early is cheapest.", font_size=26, color=TERRA, font=font)
        spark.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(spark), run_time=0.4)

        self.wait(max(0.01, 15.2 - 4.3))
