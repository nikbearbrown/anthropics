from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamPrompt(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: A prompt saved in chat history is a text. A prompt card is a text plus a standar"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "CARD-VS-CHAT":
            act = Text("CARD-VS-CHAT", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A prompt saved in chat history is a text":
            line1 = Text("A prompt saved in chat history is a text", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "A prompt card is a text plus a standard":
            line2 = Text("A prompt card is a text plus a standard", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The card has eight fields: purpose, inputs, constraints, for":
            line3 = Text("The card has eight fields: purpose, inputs, constraints, for", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A prompt saved in chat history is a text":
            uline = Line(LEFT * min(4.0, len("A prompt saved in chat history is a text") * 0.18), RIGHT * min(4.0, len("A prompt saved in chat history is a text") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B02_ClaudeLiamPrompt(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: The review criteria field is the one most writers skip and the most important fo"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "REVIEW-CRITERIA-FIELD":
            act = Text("REVIEW-CRITERIA-FIELD", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The review criteria field is the one most writers skip and t":
            line1 = Text("The review criteria field is the one most writers skip and t", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It answers: after Claude returns the output, what specifical":
            line2 = Text("It answers: after Claude returns the output, what specifical", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The field converts review from a glance to a gate":
            line3 = Text("The field converts review from a glance to a gate", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The review criteria field is the one most writers skip and t":
            uline = Line(LEFT * min(4.0, len("The review criteria field is the one most writers skip and t") * 0.18), RIGHT * min(4.0, len("The review criteria field is the one most writers skip and t") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B03_ClaudeLiamPrompt(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The failure modes field requires honesty: \'tends to merge action items when note"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "FAILURE-MODES-HONEST":
            act = Text("FAILURE-MODES-HONEST", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The failure modes field requires honesty: \'tends to merge ac":
            line1 = Text("The failure modes field requires honesty: \'tends to merge ac", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\' Not generic - tested on the actual failure":
            line2 = Text("\' Not generic - tested on the actual failure", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A card without an honest failure mode was tested on a clean ":
            line3 = Text("A card without an honest failure mode was tested on a clean ", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The failure modes field requires honesty: \'tends to merge ac":
            uline = Line(LEFT * min(4.0, len("The failure modes field requires honesty: \'tends to merge ac") * 0.18), RIGHT * min(4.0, len("The failure modes field requires honesty: \'tends to merge ac") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
