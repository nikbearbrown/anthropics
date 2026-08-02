import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
class B02_Radio(Scene):
 def construct(self):
  d=DUR.get('B02',15); self.add(bg(),ttl('THE HYDROGEN REST LINE')); rows=VGroup(Text('f0 = 1420.4058 MHz',font=MONO,font_size=39,color=CRIMSON),Text('lambda = 21.106 cm',font=MONO,font_size=39,color=TEAL),Text('Doppler shift -> gas velocity',font=MONO,font_size=32,color=INK),Text('emission or absorption',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.6); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B03_Multiplet(Scene):
 def construct(self):
  d=DUR.get('B03',15); self.add(bg(),ttl('TWO SPIN-HALVES MAKE 3 + 1 STATES')); top=VGroup(*[RoundedRectangle(width=2,height=1.2,corner_radius=.15,color=TEAL).set_fill(TEAL,.1) for _ in range(3)]).arrange(RIGHT,buff=.7).shift(UP*.8); bot=RoundedRectangle(width=2,height=1.2,corner_radius=.15,color=CRIMSON).set_fill(CRIMSON,.1).shift(DOWN*1.4); labs=VGroup(Text('F = 1 triplet',font=MONO,font_size=31,color=TEAL).move_to(UP*2.3),Text('F = 0 singlet',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*2.5)); self.play(Create(top),Create(bot),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Sign(Scene):
 def construct(self):
  d=DUR.get('B04',15); self.add(bg(),ttl('ONE RELATIVE SIGN · DIFFERENT TOTAL SPIN')); eqs=VGroup(Text('(|up down> + |down up>) / sqrt(2)',font=MONO,font_size=34,color=TEAL),Text('versus',font=SERIF,font_size=30,color=INK),Text('(|up down> - |down up>) / sqrt(2)',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B05_Relative(Scene):
 def construct(self):
  d=DUR.get('B05',13); self.add(bg(),ttl('GLOBAL PHASE IS NOT RELATIVE PHASE')); left=VGroup(Text('- (a|1> + b|2>)',font=MONO,font_size=32,color=SLATE),Text('same physical ray',font=SERIF,font_size=28,color=SLATE)).arrange(DOWN,buff=.5).shift(LEFT*3); right=VGroup(Text('a|1> - b|2>',font=MONO,font_size=34,color=CRIMSON),Text('different interference',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN,buff=.5).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B06_Symmetry(Scene):
 def construct(self):
  d=DUR.get('B06',15); self.add(bg(),ttl('THE SIGN SELECTS EXCHANGE SYMMETRY')); plus=VGroup(Text('+',font=DISPLAY,font_size=70,color=TEAL),Text('symmetric',font=MONO,font_size=30,color=TEAL),Text('F = 1, m = 0',font=MONO,font_size=29,color=TEAL)).arrange(DOWN).shift(LEFT*3); minus=VGroup(Text('-',font=DISPLAY,font_size=70,color=CRIMSON),Text('antisymmetric',font=MONO,font_size=30,color=CRIMSON),Text('F = 0',font=MONO,font_size=29,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(plus,minus),run_time=1); self.wait(max(.1,d-1))
class B07_F2(Scene):
 def construct(self):
  d=DUR.get('B07',16); self.add(bg(),ttl('TOTAL-SPIN EIGENVALUES')); eqs=VGroup(Text('F^2 |F,m> = F(F+1) hbar^2 |F,m>',font=MONO,font_size=32,color=INK),Text('F = 1  ->  2 hbar^2',font=MONO,font_size=37,color=TEAL),Text('F = 0  ->  0',font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B08_Hyperfine(Scene):
 def construct(self):
  d=DUR.get('B08',16); self.add(bg(),ttl('HYPERFINE COUPLING TURNS SYMMETRY INTO ENERGY')); eq=Text('Se dot Ip = (F^2 - Se^2 - Ip^2) / 2',font=MONO,font_size=33,color=INK).move_to(UP*1.7); levels=VGroup(Line(LEFT*3,RIGHT*3,color=TEAL).shift(UP*.3),Line(LEFT*3,RIGHT*3,color=CRIMSON).shift(DOWN*1.5)); labs=VGroup(Text('triplet: + hbar^2/4',font=MONO,font_size=29,color=TEAL).move_to(UP*.7),Text('singlet: - 3 hbar^2/4',font=MONO,font_size=29,color=CRIMSON).move_to(DOWN*2)); self.play(FadeIn(eq),Create(levels),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Chain(Scene):
 def construct(self):
  d=DUR.get('B09',15); self.add(bg(),ttl('ONE GAP · THREE EQUIVALENT SCALES')); chain=VGroup(Text('Delta E = 5.874 micro-eV',font=MONO,font_size=35,color=CRIMSON),Text('f = Delta E / h = 1420.4 MHz',font=MONO,font_size=33,color=INK),Text('lambda = c / f = 21.1 cm',font=MONO,font_size=35,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(chain),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',19); self.add(bg(),ttl('YOUR TURN: A 100 kHz REDSHIFT')); eqs=VGroup(Text('Delta f / f0 approx -v/c',font=MONO,font_size=36,color=INK),Text('v approx 21 km/s away',font=MONO,font_size=40,color=CRIMSON),Text('frequency shift -> line-of-sight velocity',font=SERIF,font_size=30,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',16); self.add(bg(),Text('WHY ONE MINUS SIGN LIGHTS UP THE GALAXY',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('relative sign -> total-spin symmetry',font=MONO,font_size=32,color=TEAL).move_to(UP*.8),Text('hyperfine coupling -> energy gap',font=MONO,font_size=32,color=INK).move_to(DOWN*.4),Text('gap -> 21 cm emission or absorption',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=18.03
  self.add(bg(),ttl('Radio telescopes map neutral hydrogen ar'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Radio telescopes map neutral hydrogen around a rest fre',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('4 megahertz, wavelength 21',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=16.68
  self.add(bg(),ttl('The line comes from hyperfine splitting '))
  stmt=Text('The line comes from hyperfine splitting in hydrogen\'s g',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Electron and proton each have spin one-half',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.49
  self.add(bg(),ttl('The two states use the same up-down'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The two states use the same up-down basis vectors and a',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('But this is a relative sign between components, not one',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.15
  self.add(bg(),ttl('That sign selects a total-spin eigenstat'))
  stmt=Text('That sign selects a total-spin eigenstate',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Up-down plus down-up, divided by root two, is the F equ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=16.3
  self.add(bg(),ttl('Why does the sign determine total spin?'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Why does the sign determine total spin? Apply total F s',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The cross terms add for the symmetric plus state and ca',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=18.09
  self.add(bg(),ttl('The ground-state hyperfine Hamiltonian i'))
  stmt=Text('The ground-state hyperfine Hamiltonian is proportional ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The dot product is one half of F squared minus the two ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=17.86
  self.add(bg(),ttl('The gap is tiny: about 5.87 micro-electr'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The gap is tiny: about 5',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('87 micro-electron-volts',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=19.41
  self.add(bg(),ttl('Your turn. A hydrogen line arrives 100'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('A hydrogen line arrives 100 kilohertz below the 1420',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('4 megahertz rest frequency',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
