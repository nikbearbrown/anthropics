import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def sphere(center=ORIGIN,r=2.25):
 c=Circle(radius=r,color=TEAL,stroke_width=4).move_to(center); eq=Ellipse(width=2*r,height=.65,color=SLATE,stroke_width=2).move_to(center); axis=Line(center+DOWN*r,center+UP*r,color=SLATE,stroke_width=2); return VGroup(c,eq,axis)

class B02_BitVsQubit(Scene):
 def construct(self):
  d=DUR.get("B02",9); self.add(bg(),ttl("TWO CHOICES VERSUS A CONTINUOUS PURE STATE")); bits=VGroup(Dot(radius=.22,color=INK),Dot(radius=.22,color=INK)).arrange(DOWN,buff=2).move_to(LEFT*4); labs=VGroup(Text("0",font=MONO,font_size=28,color=INK).next_to(bits[0],LEFT),Text("1",font=MONO,font_size=28,color=INK).next_to(bits[1],LEFT),Text("classical bit",font=SERIF,font_size=27,color=INK).move_to(LEFT*4+DOWN*2.8)); sph=sphere(RIGHT*3); arrow=Arrow(RIGHT*3,RIGHT*4+UP*1.4,color=CRIMSON,buff=0); q=Text("pure qubit",font=SERIF,font_size=27,color=CRIMSON).move_to(RIGHT*3+DOWN*2.8); self.play(FadeIn(bits,labs),Create(sph),GrowArrow(arrow),FadeIn(q),run_time=1); self.wait(max(.1,d-1))

class B03_FourParameters(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),ttl("TWO COMPLEX AMPLITUDES")); st=Text("|psi> = alpha |0> + beta |1>",font=MONO,font_size=42,color=CRIMSON).move_to(UP*1.1); row=VGroup(*[Text(x,font=MONO,font_size=30,color=INK) for x in ["Re alpha","Im alpha","Re beta","Im beta"]]).arrange(RIGHT,buff=.65).move_to(DOWN*.7); cap=Text("4 real parameters",font=SERIF,font_size=34,color=TEAL).move_to(DOWN*2.2); self.play(Write(st),FadeIn(row,cap),run_time=1); self.wait(max(.1,d-1))

class B04_Normalize(Scene):
 def construct(self):
  d=DUR.get("B04",9); self.add(bg(),ttl("NORMALIZATION REMOVES ONE")); eq=Text("|alpha|^2 + |beta|^2 = 1",font=MONO,font_size=44,color=CRIMSON).move_to(UP*1.2); nums=VGroup(Text("4 real",font=MONO,font_size=38,color=INK),Text("- 1 constraint",font=MONO,font_size=35,color=CRIMSON),Text("= 3",font=MONO,font_size=48,color=TEAL)).arrange(DOWN,buff=.5).move_to(DOWN*.8); self.play(Write(eq),FadeIn(nums),run_time=1); self.wait(max(.1,d-1))

class B05_GlobalPhase(Scene):
 def construct(self):
  d=DUR.get("B05",10); self.add(bg(),ttl("GLOBAL PHASE REMOVES ONE MORE")); a=Text("|psi>",font=MONO,font_size=42,color=INK).move_to(LEFT*4.5+UP*1.1); b=Text("e^(i gamma) |psi>",font=MONO,font_size=38,color=CRIMSON).move_to(RIGHT*4+UP*1.1); link=DoubleArrow(LEFT*2.8,RIGHT*.7,color=SLATE,buff=0).shift(UP*1.1); eq=Text("same measurement probabilities",font=SERIF,font_size=30,color=TEAL).move_to(DOWN*.5); count=Text("3 - 1 = 2 physical parameters",font=MONO,font_size=38,color=CRIMSON).move_to(DOWN*2); self.play(FadeIn(a,b),GrowArrow(link),FadeIn(eq,count),run_time=1); self.wait(max(.1,d-1))

class B06_Angles(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("TWO PARAMETERS BECOME TWO ANGLES")); s=sphere(); arrow=Arrow(ORIGIN,RIGHT*1.25+UP*1.55,color=CRIMSON,buff=0); theta=Arc(radius=.8,start_angle=PI/2-.67,angle=.67,color=INK); phi=Arc(radius=1.15,start_angle=0,angle=.75,color=CRIMSON).shift(DOWN*.15); labs=VGroup(Text("theta = latitude",font=MONO,font_size=28,color=INK).move_to(LEFT*4+UP*.5),Text("phi = longitude",font=MONO,font_size=28,color=CRIMSON).move_to(LEFT*4+DOWN*.7)); self.play(Create(s),GrowArrow(arrow),Create(theta),Create(phi),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B07_Parameterization(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("THE STANDARD PURE-QUBIT FORM")); l1=Text("|psi> = cos(theta/2) |0>",font=MONO,font_size=39,color=INK); l2=Text("+ e^(i phi) sin(theta/2) |1>",font=MONO,font_size=39,color=CRIMSON); lines=VGroup(l1,l2).arrange(DOWN,buff=.7); note=Text("one ray · two angles",font=SERIF,font_size=32,color=TEAL).move_to(DOWN*2.1); self.play(Write(l1),run_time=.7); self.play(Write(l2),run_time=.7); self.play(FadeIn(note),run_time=.4); self.wait(max(.1,d-1.8))

class B08_Poles(Scene):
 def construct(self):
  d=DUR.get("B08",9); self.add(bg(),ttl("THE POLES ARE THE DEFINITE STATES")); s=sphere(LEFT*2); n=Dot(LEFT*2+UP*2.25,radius=.18,color=CRIMSON); so=Dot(LEFT*2+DOWN*2.25,radius=.18,color=CRIMSON); labs=VGroup(Text("north: theta=0  ->  |0>",font=MONO,font_size=25,color=INK),Text("south: theta=pi -> |1>",font=MONO,font_size=25,color=INK)).arrange(DOWN,buff=1.4).move_to(RIGHT*3.5); self.play(Create(s),FadeIn(n,so,labs),run_time=1); self.wait(max(.1,d-1))

class B09_Equator(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("THE EQUATOR HAS EQUAL MAGNITUDES")); s=sphere(); arrows=VGroup(*[Arrow(ORIGIN,2*np.array([np.cos(a),.28*np.sin(a),0]),color=CRIMSON,buff=0) for a in [0,.8,1.6,2.4]]); labs=VGroup(Text("P(0) = P(1) = 1/2",font=MONO,font_size=32,color=INK).move_to(DOWN*2.9),Text("longitude phi stores relative phase",font=SERIF,font_size=28,color=CRIMSON).move_to(UP*2.9)); self.play(Create(s),LaggedStart(*[GrowArrow(a) for a in arrows],lag_ratio=.15),FadeIn(labs),run_time=1.3); self.wait(max(.1,d-1.3))

class B10_PlusY(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("A CONCRETE POINT: +y")); axes=VGroup(Line(LEFT*2.4,RIGHT*2.4,color=SLATE),Line(DOWN*2.4,UP*2.4,color=SLATE)).move_to(LEFT*3); arr=Arrow(LEFT*3,LEFT*3+UP*2,color=CRIMSON,buff=0); state=Text("theta=pi/2, phi=pi/2",font=MONO,font_size=29,color=INK).move_to(RIGHT*3+UP*1.4); probs=VGroup(Text("z:  P(0)=P(1)=1/2",font=MONO,font_size=28,color=INK),Text("y:  P(+y)=1",font=MONO,font_size=32,color=CRIMSON)).arrange(DOWN,buff=.7).move_to(RIGHT*3+DOWN*.5); self.play(Create(axes),GrowArrow(arr),FadeIn(state,probs),run_time=1); self.wait(max(.1,d-1))

class B11_MixedStates(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("SURFACE FOR PURE · INTERIOR FOR MIXED")); outer=Circle(radius=2.35,color=TEAL,stroke_width=5); pure=Dot(RIGHT*2.35,radius=.2,color=CRIMSON); mixed=Dot(RIGHT*.9+UP*.5,radius=.2,color=INK); center=Dot(radius=.2,color=SLATE); labs=VGroup(Text("pure state",font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*4.2),Text("mixed state",font=MONO,font_size=25,color=INK).move_to(RIGHT*3+UP*.6),Text("completely mixed",font=MONO,font_size=24,color=SLATE).move_to(LEFT*2.2+DOWN*.4)); self.play(Create(outer),FadeIn(pure,mixed,center,labs),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("WHY A GLOBE?",font=DISPLAY,font_size=34,color=TEAL).move_to(UP*2.6)); steps=VGroup(Text("4 real coordinates",font=MONO,font_size=36,color=INK),Text("minus normalization",font=MONO,font_size=31,color=CRIMSON),Text("minus global phase",font=MONO,font_size=31,color=CRIMSON),Text("= 2 physical angles",font=MONO,font_size=42,color=TEAL)).arrange(DOWN,buff=.52); self.add(steps); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.07
  self.add(bg(),ttl('A classical bit offers two isolated choi'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('A classical bit offers two isolated choices: zero or on',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('A pure qubit includes those poles and a continuous fami',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B03_SDT(Scene):
 # B03 SDT retrofit: derive — sequential step build
 def construct(self):
  d=6.87
  self.add(bg(),ttl('Start with alpha times zero plus beta'))
  s0=Text('Start with alpha times zero plus beta times one',font=SERIF,font_size=30,color=INK).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.23))
  s1=Text('Alpha and beta are complex',font=SERIF,font_size=30,color=INK).shift(UP*0.4)
  s1.set_max_width(12)
  self.play(Write(s1),run_time=max(0.01,d*0.23))
  s2=Text('That is four real numbers',font=SERIF,font_size=30,color=CRIMSON).shift(UP*-0.7)
  s2.set_max_width(12)
  self.play(Write(s2),run_time=max(0.01,d*0.23))
  self.wait(max(0.01,d*0.3))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.74
  self.add(bg(),ttl('Normalization says the squared magnitude'))
  stmt=Text('Normalization says the squared magnitudes add to one',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('That one constraint removes one real degree of freedom,',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.3
  self.add(bg(),ttl('Multiplying the entire state by the same'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Multiplying the entire state by the same phase changes ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Global phase is physically redundant, so one more param',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.34
  self.add(bg(),ttl('Write those two parameters as angles the'))
  stmt=Text('Write those two parameters as angles theta and phi',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Theta sets latitude from the north pole',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.92
  self.add(bg(),ttl('At the north pole theta is zero,'))
  stmt=Text('At the north pole theta is zero, so the state is zero',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('At the south pole theta is pi, so it is one, apart from',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.19
  self.add(bg(),ttl('On the equator, zero and one have'))
  stmt=Text('On the equator, zero and one have equal magnitude',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Longitude phi changes their relative phase, producing p',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=10.2
  self.add(bg(),ttl('For theta equals pi over two and'))
  step1=Text('For theta equals pi over two and phi equals pi ove',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  step2_obj=Text('A z measurement is still fifty-fifty',font=SERIF,font_size=30,color=INK).shift(UP*0.3)
  step2_obj.set_max_width(12)
  self.play(FadeIn(step2_obj),run_time=max(0.01,d*0.2))
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('a y measurement is certain plus',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.73
  self.add(bg(),ttl('One crucial qualifier: the surface repre'))
  stmt=Text('One crucial qualifier: the surface represents pure qubi',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Statistical mixtures live inside the Bloch ball, with t',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
