from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_NbbCoworkAccess(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: Cowork\'s access ladder has six rungs. Chat only — no file access. Uploaded task """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "LADDER-OVERVIEW":
            act = Text("LADDER-OVERVIEW", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Cowork\'s access ladder has six rungs":
            line1 = Text("Cowork\'s access ladder has six rungs", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Chat only - no file access":
            line2 = Text("Chat only - no file access", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Uploaded task files - you attach exactly what you want":
            line3 = Text("Uploaded task files - you attach exactly what you want", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Cowork\'s access ladder has six rungs":
            uline = Line(LEFT * min(4.0, len("Cowork\'s access ladder has six rungs") * 0.18), RIGHT * min(4.0, len("Cowork\'s access ladder has six rungs") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B02_NbbCoworkAccess(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: Connectors are the common mistake. Connecting a cloud drive usually means connec"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "CONNECTOR-SCOPE-ERROR":
            act = Text("CONNECTOR-SCOPE-ERROR", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Connectors are the common mistake":
            line1 = Text("Connectors are the common mistake", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Connecting a cloud drive usually means connecting the entire":
            line2 = Text("Connecting a cloud drive usually means connecting the entire", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The connector does not know you meant three files":
            line3 = Text("The connector does not know you meant three files", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Connectors are the common mistake":
            uline = Line(LEFT * min(4.0, len("Connectors are the common mistake") * 0.18), RIGHT * min(4.0, len("Connectors are the common mistake") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B03_NbbCoworkAccess(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The safest rung for document-heavy one-off tasks is uploaded task files. You cho"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "UPLOAD-AS-FLOOR":
            act = Text("UPLOAD-AS-FLOOR", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The safest rung for document-heavy one-off tasks is uploaded":
            line1 = Text("The safest rung for document-heavy one-off tasks is uploaded", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "You choose the files":
            line2 = Text("You choose the files", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "You attach them":
            line3 = Text("You attach them", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The safest rung for document-heavy one-off tasks is uploaded":
            uline = Line(LEFT * min(4.0, len("The safest rung for document-heavy one-off tasks is uploaded") * 0.18), RIGHT * min(4.0, len("The safest rung for document-heavy one-off tasks is uploaded") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))
