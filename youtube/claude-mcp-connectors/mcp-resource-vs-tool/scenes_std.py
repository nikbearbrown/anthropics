from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_McpResourceVs(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: An MCP server exposes two types of capabilities. Resources are passive — documen"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "TWO-TYPES":
            act = Text("TWO-TYPES", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "An MCP server exposes two types of capabilities":
            line1 = Text("An MCP server exposes two types of capabilities", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Resources are passive - documents, schemas, data files":
            line2 = Text("Resources are passive - documents, schemas, data files", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "When the agent reads a resource, it pulls context into memor":
            line3 = Text("When the agent reads a resource, it pulls context into memor", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "An MCP server exposes two types of capabilities":
            uline = Line(LEFT * min(4.0, len("An MCP server exposes two types of capabilities") * 0.18), RIGHT * min(4.0, len("An MCP server exposes two types of capabilities") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 12.00))


class Scene_B02_McpResourceVs(Scene):
    """Beat B02 — SHOW: concept illustration card. Narration: Most practitioners reading a list of MCP capabilities will not know which items """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "INSPECTION-PROBLEM":
            act = Text("INSPECTION-PROBLEM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Most practitioners reading a list of MCP capabilities will n":
            line1 = Text("Most practitioners reading a list of MCP capabilities will n", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The names do not always signal the type":
            line2 = Text("The names do not always signal the type", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A capability called \'update-tracker\' is obviously a tool":
            line3 = Text("A capability called \'update-tracker\' is obviously a tool", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Most practitioners reading a list of MCP capabilities will n":
            uline = Line(LEFT * min(4.0, len("Most practitioners reading a list of MCP capabilities will n") * 0.18), RIGHT * min(4.0, len("Most practitioners reading a list of MCP capabilities will n") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B03_McpResourceVs(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: There is a second risk when resources and tools coexist. An agent that reads a d"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "PROMPT-INJECTION-PATH":
            act = Text("PROMPT-INJECTION-PATH", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "There is a second risk when resources and tools coexist":
            line1 = Text("There is a second risk when resources and tools coexist", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "An agent that reads a document via a resource and has a comm":
            line2 = Text("An agent that reads a document via a resource and has a comm", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The retrieved document contains instructions the agent follo":
            line3 = Text("The retrieved document contains instructions the agent follo", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "There is a second risk when resources and tools coexist":
            uline = Line(LEFT * min(4.0, len("There is a second risk when resources and tools coexist") * 0.18), RIGHT * min(4.0, len("There is a second risk when resources and tools coexist") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))
