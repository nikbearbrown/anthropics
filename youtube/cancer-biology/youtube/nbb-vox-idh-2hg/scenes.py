from manim import *

config.background_color = "#FFFFFF"

class STD_NBB01_nbb_vox_idh_2hg(Scene):
    """SHOW-DONT-TELL retrofit for NBB01 in nbb-vox-idh-2hg.
    Narration: 'Here is what the body demonstrated. IDH1 carries a neomorphic mutation — it does'
    Duration: 41.7s  Lines: 11  font_sz: 20
    """
    def construct(self):
        config.background_color = "#FFFFFF"
        INK = "#2A1A0E"
        ACC = "#C8102E"

        heading_str = "The mechanism"
        body_lines = ["IDH1 neomorphic mutation: gains a new reaction, makes 2HG.", "2HG is a structural mimic of alpha-KG \u2014 fits but blocks the", "demethylase.", "Competitive inhibition: erasers stall, methyl marks pile up", "on differentiation genes.", "Blasts are stuck \u2014 not proliferating too fast, but unable to", "read the next instruction.", "Ivosidenib blocks mutant IDH1 \u2192 2HG drops \u2192 demethylases", "recover \u2192 blasts mature.", "Trade-off: only works in IDH-mutant disease. The mutation IS", "the therapeutic window."]
        spark_str = "Poison by resemblance."

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

        reveal_t = max(0.30, 3.72)
        for lobj in line_objs:
            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)
            self.wait(max(0.01, reveal_t * 0.10))

        if spark_str:
            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)
            spark_txt.move_to([0, -3.4, 0])
            self.play(FadeIn(spark_txt), run_time=0.4)

        self.wait(max(0.01, 0.30))
