from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamClear(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: The context window is the running transcript of every prompt, output, tool call,"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "WHAT-CONTEXT-DOES":
            act = Text("WHAT-CONTEXT-DOES", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The context window is the running transcript of every [...]":
            line1 = Text("The context window is the running transcript of every [...]", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Everything in it does two things: it consumes the [...]":
            line2 = Text("Everything in it does two things: it consumes the [...]", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The failed first attempt is still in there":
            line3 = Text("The failed first attempt is still in there", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The context window is the running transcript of every [...]":
            uline = Line(LEFT * min(4.0, len("The context window is the running transcript of every [...]") * 0.18), RIGHT * min(4.0, len("The context window is the running transcript of every [...]") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B02_ClaudeLiamClear(Scene):
    """Beat B02 — SHOW: layer stack diagram. Narration: slash-clear wipes the conversation. The code on disk stays. CLAUDE.md stays. Pro"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "CLEAR-MECHANICS":
            act = Text("CLEAR-MECHANICS", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["slash-clear wipes the conversation", "The code on disk stays", "Project files stay"] if t]
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

        self.wait(max(0.01, 11.00))


class Scene_B03_ClaudeLiamClear(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: slash-compact summarizes the conversation instead of erasing it. Use compact whe"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "COMPACT-VS-CLEAR":
            act = Text("COMPACT-VS-CLEAR", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "slash-compact summarizes the conversation instead of [...]":
            line1 = Text("slash-compact summarizes the conversation instead of [...]", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Use compact when the context is long but still load- [...]":
            line2 = Text("Use compact when the context is long but still load- [...]", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Use clear when the context is finished and in the way [...]":
            line3 = Text("Use clear when the context is finished and in the way [...]", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "slash-compact summarizes the conversation instead of [...]":
            uline = Line(LEFT * min(4.0, len("slash-compact summarizes the conversation instead of [...]") * 0.18), RIGHT * min(4.0, len("slash-compact summarizes the conversation instead of [...]") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
