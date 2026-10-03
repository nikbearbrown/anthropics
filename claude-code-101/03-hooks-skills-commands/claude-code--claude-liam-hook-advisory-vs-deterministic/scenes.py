from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class B01_ClaudeLiamHook(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: Claude weighted the NEVER instruction against the prompt\'s pull — \'summarize stu"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "NEVER-IGNORED":
            act = Text("NEVER-IGNORED", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Claude weighted the NEVER instruction against the prompt\'s p":
            line1 = Text("Claude weighted the NEVER instruction against the prompt\'s p", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "This is probabilistic behavior: Claude is a language model, ":
            line2 = Text("This is probabilistic behavior: Claude is a language model, ", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "md rules are intentions that Claude tries to follow":
            line3 = Text("md rules are intentions that Claude tries to follow", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Claude weighted the NEVER instruction against the prompt\'s p":
            uline = Line(LEFT * min(4.0, len("Claude weighted the NEVER instruction against the prompt\'s p") * 0.18), RIGHT * min(4.0, len("Claude weighted the NEVER instruction against the prompt\'s p") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class B02_ClaudeLiamHook(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: A hook is a shell script that runs on a system event — before a file write, befo"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "HOOK-ANATOMY":
            act = Text("HOOK-ANATOMY", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A hook is a shell script that runs on a system event - befor":
            line1 = Text("A hook is a shell script that runs on a system event - befor", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The PreToolUse hook receives a JSON payload on stdin describ":
            line2 = Text("The PreToolUse hook receives a JSON payload on stdin describ", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The script checks the payload":
            line3 = Text("The script checks the payload", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A hook is a shell script that runs on a system event - befor":
            uline = Line(LEFT * min(4.0, len("A hook is a shell script that runs on a system event - befor") * 0.18), RIGHT * min(4.0, len("A hook is a shell script that runs on a system event - befor") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class B03_ClaudeLiamHook(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: You do not need to write the hook script. Ask Claude to write it. Describe the p"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ASK-CLAUDE-PATTERN":
            act = Text("ASK-CLAUDE-PATTERN", font_size=36, color="#3D3929", font=font)
            act.scale(min(1.0, 10.5 / max(0.1, act.width)))
            act.to_edge(UP, buff=0.8)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "You do not need to write the hook script":
            line1 = Text("You do not need to write the hook script", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 10.5 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Ask Claude to write it":
            line2 = Text("Ask Claude to write it", font_size=40, color="#3D3929", font=font)
            line2.scale(min(1.0, 10.5 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Describe the pattern to block - any grade letter followed by":
            line3 = Text("Describe the pattern to block - any grade letter followed by", font_size=40, color="#3D3929", font=font)
            line3.scale(min(1.0, 10.5 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "You do not need to write the hook script":
            uline = Line(LEFT * min(4.0, len("You do not need to write the hook script") * 0.18), RIGHT * min(4.0, len("You do not need to write the hook script") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
