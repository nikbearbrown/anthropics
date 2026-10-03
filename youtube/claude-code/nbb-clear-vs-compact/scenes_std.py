from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbClearVs(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: The context window is the running transcript of every prompt, output, tool call,"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "WHAT-CONTEXT-DOES":
            act = Text("WHAT-CONTEXT-DOES", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The context window is the running transcript of every prompt":
            line1 = Text("The context window is the running transcript of every prompt", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Everything in it does two things: it consumes the budget, an":
            line2 = Text("Everything in it does two things: it consumes the budget, an", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The failed first attempt is still in there":
            line3 = Text("The failed first attempt is still in there", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The context window is the running transcript of every prompt":
            uline = Line(LEFT * min(4.0, len("The context window is the running transcript of every prompt") * 0.18), RIGHT * min(4.0, len("The context window is the running transcript of every prompt") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B02_NbbClearVs(Scene):
    """Beat B02 — SHOW: layer stack diagram. Narration: slash-clear wipes the conversation. The code on disk stays. CLAUDE.md stays. Pro"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "CLEAR-MECHANICS":
            act = Text("CLEAR-MECHANICS", font_size=24, color="#2A1A0E", font=font)
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
                             color="#2A1A0E", stroke_width=2,
                             fill_color="#C8102E" if i == 0 else "#2A1A0E",
                             fill_opacity=0.12 + i * 0.06)
            box.move_to(UP * y)
            txt = Text(lbl[:60], font_size=24, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
            txt.move_to(box)
            self.play(FadeIn(box), Write(txt), run_time=0.5)

        self.wait(max(0.01, 11.00))


class Scene_B03_NbbClearVs(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: slash-compact summarizes the conversation instead of erasing it. Use compact whe"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "COMPACT-VS-CLEAR":
            act = Text("COMPACT-VS-CLEAR", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text — compact vs clear decision
        line1 = Text("slash-compact — summarize, don't erase", font_size=36, color="#2A1A0E", font=font)
        line1.scale(min(1.0, 12.0 / max(0.1, line1.width)))
        line1.shift(UP * 0.3)
        self.play(Write(line1), run_time=0.5)

        line2 = Text("Still load-bearing? compact.", font_size=32, color="#2A1A0E", font=font)
        line2.scale(min(1.0, 10.0 / max(0.1, line2.width)))
        line2.shift(DOWN * 0.6)
        self.play(Write(line2), run_time=0.4)

        line3 = Text("Finished and in the way? clear.", font_size=32, color="#C8102E", font=font)
        line3.scale(min(1.0, 10.0 / max(0.1, line3.width)))
        line3.shift(DOWN * 1.4)
        self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline under the primary term
        uline = Line(LEFT * 2.2, RIGHT * 2.2, color="#C8102E", stroke_width=2)
        uline.shift(UP * 0.05)
        self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
