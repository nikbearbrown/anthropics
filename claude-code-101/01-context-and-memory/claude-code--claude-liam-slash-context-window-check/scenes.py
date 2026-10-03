from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class B01_ClaudeLiamSlash(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: The context window is a fixed working surface. When it fills, Claude begins drop"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "WHY-IT-DEGRADES":
            act = Text("WHY-IT-DEGRADES", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The context window is a fixed working surface":
            line1 = Text("The context window is a fixed working surface", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "When it fills, Claude begins dropping earlier content - incl":
            line2 = Text("When it fills, Claude begins dropping earlier content - incl", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Liu 2025 shows quality degrades monotonically with window le":
            line3 = Text("Liu 2025 shows quality degrades monotonically with window le", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The context window is a fixed working surface":
            uline = Line(LEFT * min(4.0, len("The context window is a fixed working surface") * 0.18), RIGHT * min(4.0, len("The context window is a fixed working surface") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class B02_ClaudeLiamSlash(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: Three tools manage the window. /context: run it before any new task to see what """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THREE-TOOLS":
            act = Text("THREE-TOOLS", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Three tools manage the window":
            line1 = Text("Three tools manage the window", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "/context: run it before any new task to see what is filling ":
            line2 = Text("/context: run it before any new task to see what is filling ", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "/clear: wipes the conversation; safe because durable rules l":
            line3 = Text("/clear: wipes the conversation; safe because durable rules l", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Three tools manage the window":
            uline = Line(LEFT * min(4.0, len("Three tools manage the window") * 0.18), RIGHT * min(4.0, len("Three tools manage the window") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class B03_ClaudeLiamSlash(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The structural fix for heavy reading is a subagent. Instead of pasting 25 studen"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "SUBAGENT-ALTERNATIVE":
            act = Text("SUBAGENT-ALTERNATIVE", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The structural fix for heavy reading is a subagent":
            line1 = Text("The structural fix for heavy reading is a subagent", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Instead of pasting 25 student submissions into the main sess":
            line2 = Text("Instead of pasting 25 student submissions into the main sess", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The main session sees three paragraphs, not 25 submissions":
            line3 = Text("The main session sees three paragraphs, not 25 submissions", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The structural fix for heavy reading is a subagent":
            uline = Line(LEFT * min(4.0, len("The structural fix for heavy reading is a subagent") * 0.18), RIGHT * min(4.0, len("The structural fix for heavy reading is a subagent") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
