from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_VoxSimulationOwnership(Scene):
    """Beat B01 — SHOW: cycle / feedback loop. Narration: The teacher typed one line: build me an interactive sorting algorithm simulator."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        import numpy as np
        stages = [t for t in ["The teacher typed one line: build me an interactive sorting ", "The agentic loop ran for eight minutes", "The result worked"] if t]
        if not stages:
            stages = ["Input", "Process", "Output"]
        n = len(stages)
        radius = 2.5
        colors = ["#3D3929", "#D97757"] + ["#3D3929"] * 10

        nodes = []
        for i, lbl in enumerate(stages):
            angle = np.pi / 2 - 2 * np.pi * i / n
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.55, color=colors[i % 2], stroke_width=2.5,
                            fill_color="#F2F0E9", fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl[:20], font_size=18, color="#3D3929", font=font)
            txt.scale(min(1.0, 0.9 / max(0.1, txt.width)))
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        # Draw curved arrows between nodes
        for i in range(n):
            start_pos = nodes[i][1]
            end_pos = nodes[(i + 1) % n][1]
            arr = CurvedArrow(start_pos, end_pos, color="#D97757", stroke_width=2.5,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.4)

        self.wait(max(0.01, 8.00))


class Scene_B03_VoxSimulationOwnership(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: Here is the question. A specific natural-language request should produce output """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Here is the question":
            line1 = Text("Here is the question", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "A specific natural-language request should produce output ma":
            line2 = Text("A specific natural-language request should produce output ma", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Here is the simulation where a clear-sounding request produc":
            line3 = Text("Here is the simulation where a clear-sounding request produc", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Here is the question":
            uline = Line(LEFT * min(4.0, len("Here is the question") * 0.18), RIGHT * min(4.0, len("Here is the question") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_VoxSimulationOwnership(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: One line of intent gives Claude one decision: the goal. Every other decision — c"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "One line of intent gives Claude one decision: the goal":
            line1 = Text("One line of intent gives Claude one decision: the goal", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Every other decision - color palette, interaction model, ped":
            line2 = Text("Every other decision - color palette, interaction model, ped", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The defaults are reasonable for some generic simulator":
            line3 = Text("The defaults are reasonable for some generic simulator", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "One line of intent gives Claude one decision: the goal":
            uline = Line(LEFT * min(4.0, len("One line of intent gives Claude one decision: the goal") * 0.18), RIGHT * min(4.0, len("One line of intent gives Claude one decision: the goal") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B05_VoxSimulationOwnership(Scene):
    """Beat B05 — SHOW: bar/proportion chart. Narration: The three-file system moves those decisions from Claude\'s defaults to explicit h"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("The three-file system moves those decisions from Claude\'s de"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("md is the technical constitution: stack, file structure, wha"[:30] if "md is the technical constitution: stack, file structure, wha" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "md is the visual constitution: six named colors, interaction":
            note = Text("md is the visual constitution: six named colors, interaction"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.00))


class Scene_B06_VoxSimulationOwnership(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: The before-and-after. Without three files: one-line prompt produces bright blue,"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The before-and-after":
            line1 = Text("The before-and-after", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Without three files: one-line prompt produces bright blue, d":
            line2 = Text("Without three files: one-line prompt produces bright blue, d", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "With three files: forty-five minutes of file-writing, then t":
            line3 = Text("With three files: forty-five minutes of file-writing, then t", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The before-and-after":
            uline = Line(LEFT * min(4.0, len("The before-and-after") * 0.18), RIGHT * min(4.0, len("The before-and-after") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B07_VoxSimulationOwnership(Scene):
    """Beat B07 — SHOW: two-column comparison. Narration: The DESIGN.md six-color rule. Six named variables: warm white, near-black, terra"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#3D3929", stroke_width=2,
                                     fill_color="#F2F0E9", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("The DESIGN"[:50], font_size=22, color="#3D3929", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#D97757", stroke_width=2,
                                      fill_color="#F2F0E9", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("md six-color rule"[:50] if "md six-color rule" else "Result", font_size=22, color="#3D3929", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#3D3929", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "Six named variables: warm white, near-black, terracotta for ":
            note = Text("Six named variables: warm white, near-black, terracotta for "[:60], font_size=20, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 10.00))


class Scene_B08_VoxSimulationOwnership(Scene):
    """Beat B08 — SHOW: layer stack diagram. Narration: The practical move. The 45-minute test: if you cannot write all three files in 4"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["The practical move", "The 45-minute test: if you cannot write all three files in 4", "Decompose"] if t]
        if not layers_text:
            layers_text = ["Layer 1", "Layer 2", "Layer 3"]

        n = len(layers_text)
        layer_h = 1.2
        layer_w = 9.0
        start_y = (n - 1) * layer_h / 2

        for i, lbl in enumerate(reversed(layers_text)):
            y = start_y - i * layer_h
            alpha = 0.3 + i * 0.2
            box = Rectangle(width=layer_w, height=layer_h * 0.85,
                             color="#3D3929", stroke_width=2,
                             fill_color="#D97757" if i == 0 else "#3D3929",
                             fill_opacity=0.12 + i * 0.06)
            box.move_to(UP * y)
            txt = Text(lbl[:60], font_size=24, color="#3D3929", font=font)
            txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
            txt.move_to(box)
            self.play(FadeIn(box), Write(txt), run_time=0.5)

        self.wait(max(0.01, 10.00))


class Scene_B09_VoxSimulationOwnership(Scene):
    """Beat B09 — SHOW: bar/proportion chart. Narration: Claude can generate the code. Claude cannot generate the lesson. The three files"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Claude can generate the code"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Claude cannot generate the lesson"[:30] if "Claude cannot generate the lesson" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "The three files are the 45 minutes where you make the simula":
            note = Text("The three files are the 45 minutes where you make the simula"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.00))
