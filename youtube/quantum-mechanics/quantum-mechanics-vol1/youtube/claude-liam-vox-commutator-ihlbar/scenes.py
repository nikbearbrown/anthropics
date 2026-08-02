import sys,json,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def stack(*ss): return VGroup(*[Text(s,font=MONO,font_size=34,color=(CRIMSON if i==len(ss)-1 else INK)) for i,s in enumerate(ss)]).arrange(DOWN,buff=.65)
class B02_Position(Scene):
 def construct(self):
  d=DUR.get('B02',8); self.add(bg(),ttl('POSITION MULTIPLIES')); eq=Text('x_hat psi(x) = x psi(x)',font=MONO,font_size=46,color=CRIMSON); arrow=Arrow(LEFT*4,RIGHT*4,color=SLATE,buff=0).shift(DOWN*1.4); labs=VGroup(Text('input state',font=SERIF,font_size=28,color=INK).move_to(LEFT*4+DOWN*2),Text('weighted by position x',font=SERIF,font_size=28,color=TEAL).move_to(RIGHT*4+DOWN*2)); self.play(Write(eq),GrowArrow(arrow),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B03_Momentum(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('MOMENTUM DIFFERENTIATES')); eq=Text('p_hat = -i hbar d/dx',font=MONO,font_size=48,color=CRIMSON).move_to(UP*.7); note=Text('derivatives notice products',font=SERIF,font_size=32,color=TEAL).move_to(DOWN*1.2); self.play(Write(eq),FadeIn(note),run_time=1); self.wait(max(.1,d-1))
class B04_XP(Scene):
 def construct(self):
  d=DUR.get('B04',9); self.add(bg(),ttl('FIRST p, THEN x')); eqs=stack('p psi = -i hbar psi\'','x(p psi) = -i hbar x psi\''); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B05_PX(Scene):
 def construct(self):
  d=DUR.get('B05',10); self.add(bg(),ttl('FIRST x, THEN p: THE PRODUCT RULE APPEARS')); eqs=stack('p(x psi) = -i hbar d(x psi)/dx','d(x psi)/dx = psi + x psi\'','p(x psi) = -i hbar(psi + x psi\')'); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B06_Cancel(Scene):
 def construct(self):
  d=DUR.get('B06',10); self.add(bg(),ttl('SUBTRACT xp - px')); lines=VGroup(Text('-i hbar x psi\'',font=MONO,font_size=38,color=INK),Text('- [ -i hbar psi - i hbar x psi\' ]',font=MONO,font_size=36,color=INK),Text('x psi\' terms cancel',font=SERIF,font_size=29,color=TEAL),Text('= + i hbar psi',font=MONO,font_size=48,color=CRIMSON)).arrange(DOWN,buff=.5); self.play(FadeIn(lines[:2]),run_time=.6); self.play(FadeIn(lines[2:]),run_time=.6); self.wait(max(.1,d-1.2))
class B07_Identity(Scene):
 def construct(self):
  d=DUR.get('B07',8); self.add(bg(),ttl('THE CANONICAL COMMUTATOR')); eq=Text('[x_hat, p_hat] = i hbar I',font=MONO,font_size=54,color=CRIMSON); note=Text('true on every suitable state in the common domain',font=SERIF,font_size=27,color=TEAL).move_to(DOWN*1.6); self.play(Write(eq),FadeIn(note),run_time=1); self.wait(max(.1,d-1))
class B08_Reverse(Scene):
 def construct(self):
  d=DUR.get('B08',9); self.add(bg(),ttl('REVERSE ORDER · REVERSE SIGN')); left=Text('[x,p] = +i hbar',font=MONO,font_size=39,color=CRIMSON).move_to(LEFT*3.5); right=Text('[p,x] = -i hbar',font=MONO,font_size=39,color=TEAL).move_to(RIGHT*3.5); arrow=DoubleArrow(LEFT*.9,RIGHT*.9,color=SLATE,buff=0); self.play(FadeIn(left,right),GrowArrow(arrow),run_time=1); self.wait(max(.1,d-1))
class B09_NotMeasurement(Scene):
 def construct(self):
  d=DUR.get('B09',10); self.add(bg(),ttl('OPERATOR COMPOSITION IS NOT A MEASUREMENT SEQUENCE')); a=VGroup(Text('xp psi',font=MONO,font_size=43,color=CRIMSON),Text('mathematical action',font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.5).move_to(LEFT*3.5); b=VGroup(Text('measure x, then p',font=MONO,font_size=34,color=SLATE),Text('a different physical protocol',font=SERIF,font_size=28,color=INK)).arrange(DOWN,buff=.5).move_to(RIGHT*3.5); sep=Line(UP*2,DOWN*2,color=SLATE); self.play(FadeIn(a,b,sep),run_time=1); self.wait(max(.1,d-1))
class B10_Robertson(Scene):
 def construct(self):
  d=DUR.get('B10',10); self.add(bg(),ttl('NONCOMMUTATION SETS A SPREAD BOUND')); general=Text('Delta A Delta B >= |<[A,B]>| / 2',font=MONO,font_size=36,color=INK).move_to(UP*1.1); specific=Text('Delta x Delta p >= hbar / 2',font=MONO,font_size=48,color=CRIMSON).move_to(DOWN*.7); self.play(Write(general),run_time=.7); self.play(FadeIn(specific),run_time=.5); self.wait(max(.1,d-1.2))
class B11_StateSpread(Scene):
 def construct(self):
  d=DUR.get('B11',9); self.add(bg(),ttl('A PROPERTY OF THE PREPARED STATE')); x=Rectangle(width=2,height=1,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12).move_to(LEFT*3); p=Rectangle(width=6,height=1,color=TEAL,fill_color=TEAL,fill_opacity=.12).move_to(RIGHT*2); labels=VGroup(Text('narrow Delta x',font=MONO,font_size=27,color=CRIMSON).move_to(LEFT*3+DOWN*1.3),Text('broad Delta p',font=MONO,font_size=27,color=TEAL).move_to(RIGHT*2+DOWN*1.3),Text('no photon kick required',font=SERIF,font_size=30,color=INK).move_to(DOWN*2.7)); self.play(FadeIn(x,p,labels),run_time=1); self.wait(max(.1,d-1))
class B12_Recap(Scene):
 def construct(self):
  d=DUR.get('B12',8); self.add(bg(),Text('THE UNAVOIDABLE REMAINDER',font=DISPLAY,font_size=34,color=TEAL).move_to(UP*2.3),Text('momentum differentiates',font=MONO,font_size=33,color=INK).move_to(UP*.8),Text('product rule adds psi',font=MONO,font_size=35,color=CRIMSON).move_to(DOWN*.4),Text('[x,p] = i hbar',font=MONO,font_size=47,color=TEAL).move_to(DOWN*2)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: derive — sequential step build
 def construct(self):
  d=5.67
  self.add(bg(),ttl('Position is the multiplication operator:'))
  s0=Text('Position is the multiplication operator: x hat a',font=SERIF,font_size=30,color=CRIMSON).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.70))
  self.wait(max(0.01,d*0.3))
class B03_SDT(Scene):
 # B03 SDT retrofit: derive — sequential step build
 def construct(self):
  d=7.38
  self.add(bg(),ttl('Momentum in the position representation '))
  s0=Text('Momentum in the position representation is a der',font=SERIF,font_size=30,color=CRIMSON).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.70))
  self.wait(max(0.01,d*0.3))
class B04_SDT(Scene):
 # B04 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=6.31
  self.add(bg(),ttl('First apply momentum, then position. The'))
  step1=Text('First apply momentum, then position',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('The result is minus i h bar x times psi prime',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('result',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B05_SDT(Scene):
 # B05 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=8.98
  self.add(bg(),ttl('Now reverse the operators: momentum acts'))
  step1=Text('Now reverse the operators: momentum acts on x psi',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('Differentiation sees both factors, so the product ',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('result',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.94
  self.add(bg(),ttl('Because this holds for every suitable wa'))
  stmt=Text('Because this holds for every suitable wave function, th',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=7.85
  self.add(bg(),ttl('Reverse the commutator and the sign reve'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Reverse the commutator and the sign reverses: p x minus',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Order is the entire point',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.01
  self.add(bg(),ttl('This algebra is not literally position m'))
  stmt=Text('This algebra is not literally position measurement foll',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It compares two compositions of mathematical operators ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.54
  self.add(bg(),ttl('The bound describes the spreads of a'))
  stmt=Text('The bound describes the spreads of a prepared state',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It does not require a photon kick, and it does not say ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
