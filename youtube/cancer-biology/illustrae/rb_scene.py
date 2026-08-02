from manim import *

config.background_color = "#FFFFFF"
SKY="#56B4E9"; BLUE="#0072B2"; GREEN="#009E73"; GRAY="#7c7c7c"

class RbConvergence(Scene):
    def construct(self):
        # --- geometry (ported from plates_gen.py p05) ---
        in_ys=[2.3,0.9,-0.5,-1.9]
        inputs=VGroup(*[
            RoundedRectangle(width=2.0,height=1.0,corner_radius=0.18,
                color=SKY,fill_color=SKY,fill_opacity=0.16,stroke_width=3.2
            ).move_to([-5.0,y,0]) for y in in_ys])
        gate=RoundedRectangle(width=1.9,height=1.9,corner_radius=0.22,
                color=BLUE,fill_color=BLUE,fill_opacity=0.18,stroke_width=4.2).move_to([0.4,0.2,0])
        final=RoundedRectangle(width=1.8,height=1.05,corner_radius=0.18,
                color=GREEN,fill_color=GREEN,fill_opacity=0.16,stroke_width=3.4).move_to([5.0,0.2,0])
        conv=gate.get_left()
        arrows=VGroup(*[
            Arrow(start=r.get_right(),end=conv,buff=0.12,color=GRAY,
                  stroke_width=3.2,max_tip_length_to_length_ratio=0.09,
                  max_stroke_width_to_length_ratio=6) for r in inputs])
        out_arrow=Arrow(start=gate.get_right(),end=final.get_left(),buff=0.12,
                  color=GRAY,stroke_width=3.4,max_tip_length_to_length_ratio=0.16)

        # --- choreography ---
        self.play(LaggedStart(*[FadeIn(r,shift=RIGHT*0.4) for r in inputs],
                              lag_ratio=0.18,run_time=1.4))
        self.play(Create(gate),run_time=0.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.12,run_time=1.5))
        self.play(Flash(gate.get_center(),color=BLUE,line_length=0.35,num_lines=16,
                        flash_radius=1.3),
                  gate.animate.set_fill(BLUE,opacity=0.34).scale(1.10),run_time=0.5)
        self.play(gate.animate.scale(1/1.10).set_fill(BLUE,opacity=0.18),run_time=0.35)
        self.play(GrowArrow(out_arrow),FadeIn(final,shift=RIGHT*0.3,scale=1.05),run_time=0.8)
        self.wait(0.8)
