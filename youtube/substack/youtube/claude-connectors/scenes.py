from manim import *

config.background_color = "#FFFFFF"

class STD_B02_claude_connectors(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-connectors.
    Narration: "What changes when you turn a connector on? Everything. Gmail on: ask what's pend"
    Duration: 22.9s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Zero copy-paste. Real context."
        body_lines = ["Gmail on \u2192 Claude reads your inbox. Zero copy-", "pastes.", "Granola on \u2192 Claude reads all meeting", "transcripts. Zero dashboards.", "Slack on \u2192 Claude pulls the full thread. Zero", "tabs.", "Combine them: Granola + Gmail + Slack \u2192 one", "prompt, full context."]
        spark_str = "Context without copy-paste."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.77)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B03_claude_connectors(Scene):
    """SHOW-DONT-TELL retrofit for B03 in claude-connectors.
    Narration: 'Nine useful connectors: Granola for meeting transcripts, HubSpot or Salesforce f'
    Duration: 20.1s  Lines: 8  font_sz: 24
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "The ones worth your fifteen minutes"
        body_lines = ["Granola \u2014 meeting transcripts, action items,", "blockers.", "HubSpot / Salesforce \u2014 deals stuck in pipeline,", "follow-up drafts.", "Notion \u2014 team knowledge base queries without", "opening Notion.", "Google Drive + Gmail + Slack \u2014 combine for full", "work context."]
        spark_str = "Nine apps, zero tabs."

        heading = Text(heading_str or "Key Points", font="EB Garamond",
                       color=INK, font_size=44, weight=BOLD)
        heading.move_to([0, 3.4, 0])
        underline = Line(
            heading.get_left() + DOWN * 0.06,
            heading.get_right() + DOWN * 0.06,
            color=ACC, stroke_width=4,
        )
        underline.next_to(heading, DOWN, buff=0.10)
        self.play(FadeIn(heading), Create(underline), run_time=0.5)

        line_objs = []
        for i, txt in enumerate(body_lines):
            col = ACC if i == 0 else INK
            lobj = Text(txt, font="EB Garamond", color=col, font_size=24)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.41)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
