import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def gaussian(sig=1,color=CRIMSON,shift=ORIGIN): return FunctionGraph(lambda x:2*np.exp(-x*x/(2*sig*sig)),x_range=[-5,5],color=color,stroke_width=4).shift(shift)
class B02_OneKet(Scene):
 def construct(self):
  d=DUR.get('B02',9); self.add(bg(),ttl('ONE STATE · TWO COMPONENT LISTS')); ket=Text('|psi>',font=MONO,font_size=56,color=INK).move_to(UP*1.7); left=VGroup(Text('position basis',font=SERIF,font_size=30,color=TEAL),Text('psi(x) = <x|psi>',font=MONO,font_size=34,color=TEAL)).arrange(DOWN).move_to(LEFT*3+DOWN*.7); right=VGroup(Text('momentum basis',font=SERIF,font_size=30,color=CRIMSON),Text('phi(p) = <p|psi>',font=MONO,font_size=34,color=CRIMSON)).arrange(DOWN).move_to(RIGHT*3+DOWN*.7); self.play(FadeIn(ket,left,right),run_time=1); self.wait(max(.1,d-1))
class B03_Axes(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('KEEP THE VECTOR FIXED · CHANGE THE AXES')); v=Arrow(ORIGIN,RIGHT*3+UP*2,color=CRIMSON,buff=0,stroke_width=7); axes1=VGroup(Line(LEFT*4,RIGHT*4,color=SLATE),Line(DOWN*2.5,UP*2.5,color=SLATE)); axes2=VGroup(Line(LEFT*3+DOWN*2,RIGHT*3+UP*2,color=TEAL),Line(LEFT*2+UP*3,RIGHT*2+DOWN*3,color=TEAL)); lab=Text('components change · vector does not',font=MONO,font_size=31,color=INK).move_to(DOWN*3); self.play(Create(axes1),GrowArrow(v),Transform(axes1,axes2),FadeIn(lab),run_time=1.5); self.wait(max(.1,d-1.5))
class B04_Position(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('POSITION REPRESENTATION')); g=gaussian(.75); lab=VGroup(Text('|psi(x)|^2',font=MONO,font_size=34,color=CRIMSON).move_to(UP*2.2),Text('narrow in x',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.3)); self.play(Create(g),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B05_Momentum(Scene):
 def construct(self):
  d=DUR.get('B05',9); self.add(bg(),ttl('MOMENTUM REPRESENTATION')); g=gaussian(2.2,TEAL); lab=VGroup(Text('|phi(p)|^2',font=MONO,font_size=34,color=TEAL).move_to(UP*2.2),Text('broad in p',font=SERIF,font_size=31,color=CRIMSON).move_to(DOWN*2.3)); self.play(Create(g),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B06_Map(Scene):
 def construct(self):
  d=DUR.get('B06',10); self.add(bg(),ttl('FOURIER TRANSFORM = UNITARY BASIS MAP')); x=Text('psi(x)',font=MONO,font_size=45,color=TEAL).shift(LEFT*3); p=Text('phi(p)',font=MONO,font_size=45,color=CRIMSON).shift(RIGHT*3); a=DoubleArrow(LEFT*1.6,RIGHT*1.6,color=INK,buff=0); labs=VGroup(Text('Fourier',font=SERIF,font_size=30,color=INK).move_to(UP*.7),Text('not time evolution · no physical kick',font=MONO,font_size=29,color=SLATE).move_to(DOWN*2)); self.play(FadeIn(x,p,labs),GrowArrow(a),run_time=1); self.wait(max(.1,d-1))
class B07_Widths(Scene):
 def construct(self):
  d=DUR.get('B07',10); self.add(bg(),ttl('GAUSSIAN WIDTHS TRADE INVERSELY')); narrow=gaussian(.65,CRIMSON,LEFT*3+DOWN*.4).scale(.55); broad=gaussian(2.0,TEAL,RIGHT*3+DOWN*.4).scale(.55); labs=VGroup(Text('small sigma_x',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*2.3),Text('large sigma_p',font=MONO,font_size=27,color=TEAL).move_to(RIGHT*3+DOWN*2.3),Text('sigma_x sigma_p = hbar/2',font=MONO,font_size=35,color=INK).move_to(UP*2)); self.play(Create(narrow),Create(broad),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B08_Phase(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('SAME POSITION DENSITY · DIFFERENT PHASE')); env=gaussian(1.5,SLATE).shift(UP*.1); flat=Line(LEFT*4,RIGHT*4,color=TEAL).shift(DOWN*.8); ramp=Line(LEFT*4+DOWN*2,RIGHT*4+UP*.1,color=CRIMSON); labs=VGroup(Text('|psi|^2 same',font=MONO,font_size=29,color=SLATE).move_to(UP*2.5),Text('phase 0',font=MONO,font_size=27,color=TEAL).move_to(LEFT*4+DOWN*2.5),Text('phase kx',font=MONO,font_size=27,color=CRIMSON).move_to(RIGHT*4+DOWN*2.5)); self.play(Create(env),Create(flat),Create(ramp),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Unitary(Scene):
 def construct(self):
  d=DUR.get('B09',9); self.add(bg(),ttl('UNITARITY PRESERVES PHYSICAL INFORMATION')); rows=VGroup(Text('integral |psi(x)|^2 dx = 1',font=MONO,font_size=35,color=TEAL),Text('integral |phi(p)|^2 dp = 1',font=MONO,font_size=35,color=CRIMSON),Text('inner products preserved',font=SERIF,font_size=33,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_Caveat(Scene):
 def construct(self):
  d=DUR.get('B10',9); self.add(bg(),ttl('THE METAPHOR HAS A BOUNDARY')); left=VGroup(Text('TURNING YOUR HEAD',font=DISPLAY,font_size=31,color=TEAL),Text('finite-dimensional analogy',font=SERIF,font_size=28,color=TEAL)).arrange(DOWN).shift(LEFT*3); right=VGroup(Text('EXACT MAP',font=DISPLAY,font_size=31,color=CRIMSON),Text('complex Fourier integral',font=SERIF,font_size=28,color=CRIMSON)).arrange(DOWN).shift(RIGHT*3); self.play(FadeIn(left,right),run_time=1); self.wait(max(.1,d-1))
class B11_Number(Scene):
 def construct(self):
  d=DUR.get('B11',10); self.add(bg(),ttl('ONE-NANOMETER MINIMUM-UNCERTAINTY PACKET')); rows=VGroup(Text('sigma_x = 1.0 nm',font=MONO,font_size=37,color=TEAL),Text('sigma_p,min = hbar / (2 sigma_x)',font=MONO,font_size=35,color=INK),Text('= 5.27 x 10^-26 kg m/s',font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B12_Shadows(Scene):
 def construct(self):
  d=DUR.get('B12',9); self.add(bg(),ttl('TWO SHADOWS · ONE STATE')); ket=Dot(ORIGIN,radius=.3,color=INK); x=Arrow(ORIGIN,LEFT*4+DOWN*1.5,color=TEAL,buff=0); p=Arrow(ORIGIN,RIGHT*4+DOWN*1.5,color=CRIMSON,buff=0); labs=VGroup(Text('position shadow',font=MONO,font_size=28,color=TEAL).move_to(LEFT*4+DOWN*2.3),Text('momentum shadow',font=MONO,font_size=28,color=CRIMSON).move_to(RIGHT*4+DOWN*2.3),Text('|psi> fixed',font=MONO,font_size=32,color=INK).move_to(UP*1)); self.play(FadeIn(ket,labs),GrowArrow(x),GrowArrow(p),run_time=1); self.wait(max(.1,d-1))
class B13_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B13',10); self.add(bg(),ttl('YOUR TURN: HALVE sigma_x')); rows=VGroup(Text('sigma_x -> sigma_x / 2',font=MONO,font_size=37,color=TEAL),Text('sigma_p -> 2 sigma_p',font=MONO,font_size=37,color=CRIMSON),Text('product remains hbar/2',font=SERIF,font_size=33,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B14_Recap(Scene):
 def construct(self):
  d=DUR.get('B14',9); self.add(bg(),Text('WHY FOURIER IS LIKE TURNING YOUR HEAD',font=DISPLAY,font_size=35,color=CRIMSON).move_to(UP*2.3),Text('one abstract ket',font=MONO,font_size=36,color=INK).move_to(UP*.8),Text('two basis-dependent component lists',font=MONO,font_size=32,color=TEAL).move_to(DOWN*.4),Text('exact map: unitary Fourier transform',font=MONO,font_size=31,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.57
  self.add(bg(),ttl('Write the physical state as one ket,'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Write the physical state as one ket, psi',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Its components in the position basis are psi of x',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.03
  self.add(bg(),ttl('In the position basis, each component an'))
  stmt=Text('In the position basis, each component answers: what pro',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('A localized packet has a narrow position profile',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.53
  self.add(bg(),ttl('In the momentum basis, each component an'))
  stmt=Text('In the momentum basis, each component answers the same ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Squaring its magnitude gives momentum probability densi',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.99
  self.add(bg(),ttl('The Fourier transform is the unitary map'))
  stmt=Text('The Fourier transform is the unitary map between these ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It does not kick the particle or evolve time',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.82
  self.add(bg(),ttl('For a minimum-uncertainty Gaussian, the '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('For a minimum-uncertainty Gaussian, the width tradeoff ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Make the position Gaussian narrower and the momentum Ga',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=14.68
  self.add(bg(),ttl('The transform carries phase information '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The transform carries phase information as well as magn',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Two position wavefunctions can have the same position d',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.3
  self.add(bg(),ttl('Turning your head is a metaphor, not'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Turning your head is a metaphor, not a literal rotation',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Position and momentum bases are connected by a complex ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B11_SDT(Scene):
 # B11 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=14.51
  self.add(bg(),ttl('Take a Gaussian with position standard d'))
  step1=Text('Take a Gaussian with position standard deviation o',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('The minimum possible momentum standard deviation i',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('result',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B12_SDT(Scene):
 # B12 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.72
  self.add(bg(),ttl('Nothing mysterious happened between the '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Nothing mysterious happened between the two plots',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Position localization requires many momentum basis comp',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B13_SDT(Scene):
 # B13 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=12.46
  self.add(bg(),ttl('Your turn. Halve the position width of'))
  step1=Text('Halve the position width of a minimum-uncertainty ',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('What happens to momentum width? It doubles',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('The uncertainty product stays h-bar over two, whil',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
