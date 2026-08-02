from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_AccessLadderExplained(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: The access ladder has seven positions. Uploaded task files — you attach the spec"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "LADDER-RUNGS":
            act = Text("LADDER-RUNGS", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The access ladder has seven positions":
            line1 = Text("The access ladder has seven positions", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Uploaded task files - you attach the specific files; access ":
            line2 = Text("Uploaded task files - you attach the specific files; access ", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Local folder - a workspace you designate; scope risk is what":
            line3 = Text("Local folder - a workspace you designate; scope risk is what", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The access ladder has seven positions":
            uline = Line(LEFT * min(4.0, len("The access ladder has seven positions") * 0.18), RIGHT * min(4.0, len("The access ladder has seven positions") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B02_AccessLadderExplained(Scene):
    """Beat B02 — SHOW: layer stack diagram. Narration: Read-only sounds safe. The risk is scope, not write access. Cowork can read anyt"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "READ-NOT-SAFE":
            act = Text("READ-NOT-SAFE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["Read-only sounds safe", "The risk is scope, not write access", "Cowork can read anything inside the connected scope and draw"] if t]
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


class Scene_B03_AccessLadderExplained(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: Before enabling any connector, ask: what does this connector actually access? Is"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "CONNECTOR-QUESTION":
            act = Text("CONNECTOR-QUESTION", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Before enabling any connector, ask: what does this connector":
            line1 = Text("Before enabling any connector, ask: what does this connector", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The upload rung is not a limitation - it is the correct acce":
            line2 = Text("The upload rung is not a limitation - it is the correct acce", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Before enabling any connector, ask: what does this connector":
            uline = Line(LEFT * min(4.0, len("Before enabling any connector, ask: what does this connector") * 0.18), RIGHT * min(4.0, len("Before enabling any connector, ask: what does this connector") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))
