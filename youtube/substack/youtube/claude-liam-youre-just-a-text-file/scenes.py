from manim import *

config.background_color = "#FFFFFF"

class STD_B02_claude_liam_youre_just_a_(Scene):
    """SHOW-DONT-TELL retrofit for B02 in claude-liam-youre-just-a-text-file.
    Narration: "Here's what actually goes into the file. Not a bio. Not a resume. The patterns —"
    Duration: 21.3s  Lines: 11  font_sz: 20
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "100 questions across 6 categories"
        body_lines = ["Beliefs & contrarian takes \u2014 what you'd defend to the death.", "Writing mechanics \u2014 sentence structure, how you open and", "close, punctuation.", "Aesthetic crimes \u2014 what makes you cringe in other people's", "writing.", "Voice & personality \u2014 humor, tone, how you handle", "disagreement.", "Reference points \u2014 the people, books, phrases that shaped", "your thinking.", "Anti-patterns \u2014 what you'd never write, words you'd never", "use."]
        spark_str = "Patterns, not biography."

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=20)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 1.87)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B04_claude_liam_youre_just_a_(Scene):
    """SHOW-DONT-TELL retrofit for B04 in claude-liam-youre-just-a-text-file.
    Narration: 'After the interview, Prompt 2 runs compression. Claude takes the 100 answers and'
    Duration: 19.3s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Prompt 2 \u2014 distill to one file"
        body_lines = ["Take all 100 answers. Extract the repeating patterns.", "Write a dense voice document: how I open, how I close,", "the words I use, the words I'd never use, my hot takes.", "Output: one file I can upload into any AI, anywhere.", "This is not a bio. It's a behavioral fingerprint."]
        spark_str = "One file, full voice."

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.71)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B05_claude_liam_youre_just_a_(Scene):
    """SHOW-DONT-TELL retrofit for B05 in claude-liam-youre-just-a-text-file.
    Narration: 'The setup: Claude, Cowork mode, Opus 4.7, extended thinking turned on. Use voice'
    Duration: 18.2s  Lines: 5  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "Before you start the interview"
        body_lines = ["Claude desktop app \u2192 Cowork tab.", "Model: Opus 4.7. Thinking: Extended.", "Voice input: Wispr Flow (free) \u2014 talk, don't type.", "Block 2 hours. No interruptions.", "Answer fast. First instinct over polished answer."]
        spark_str = "Talk, don't type."

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 3.49)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))

class STD_B06_claude_liam_youre_just_a_(Scene):
    """SHOW-DONT-TELL retrofit for B06 in claude-liam-youre-just-a-text-file.
    Narration: 'What comes out the other side: Claude writes first drafts you could have written'
    Duration: 18.5s  Lines: 6  font_sz: 28
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#3D3929"
        ACC = "#D97757"

        heading_str = "The file does three things"
        body_lines = ["First drafts in your voice \u2014 before you've", "thought of the sentence.", "Catches your patterns \u2014 the ones you didn't know", "were patterns.", "Travels anywhere \u2014 Claude, ChatGPT, Gemini,", "whatever ships next."]
        spark_str = "Drafts before you think."

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
            lobj = Text(txt, font="EB Garamond", color=col, font_size=28)
            line_objs.append(lobj)

        group = VGroup(*line_objs).arrange(DOWN, buff=0.48, aligned_edge=LEFT)
        group.move_to([0, -0.7, 0])
        group.align_to([-6.0, 0, 0], LEFT)

        reveal_t = max(0.30, 2.96)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
