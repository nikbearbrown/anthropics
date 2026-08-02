import sys,json,pathlib,math,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
DUR={}
try:
 d=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in d["beats"]}
except Exception: pass
def hold(s,b,u=1): s.wait(max(.1,DUR.get(b,10)-u))
def heading(t,size=29): return Text(t,font=DISPLAY,font_size=size,color=INK).to_edge(UP)

class B02_ChangingFrame(Scene):
 def construct(self):
  orbit=Circle(radius=2,color=INK); nucleus=Dot(color=CRIMSON,radius=.18); pts=[orbit.point_at_angle(a) for a in [0,PI/2,PI]]; electrons=VGroup(*[Dot(p,color=TEAL) for p in pts]); velocities=VGroup(Arrow(pts[0],pts[0]+UP*1.1,color=TEAL,buff=.1),Arrow(pts[1],pts[1]+LEFT*1.1,color=TEAL,buff=.1),Arrow(pts[2],pts[2]+DOWN*1.1,color=TEAL,buff=.1)); labels=VGroup(Text("different velocity direction",font=SERIF,font_size=29,color=INK).shift(DOWN*2.8),Text("no single inertial rest frame",font=MONO,font_size=35,color=CRIMSON).shift(UP*2.6))
  self.play(FadeIn(heading("AN ORBITING ELECTRON'S REST FRAME KEEPS CHANGING")),Create(orbit),FadeIn(nucleus),FadeIn(electrons),FadeIn(velocities),FadeIn(labels),run_time=1); hold(self,"B02")

class B03_TransformedField(Scene):
 def construct(self):
  E=Arrow(LEFT*3,RIGHT*3,color=CRIMSON,buff=0); v=Arrow(DOWN*2,UP*2,color=TEAL,buff=0); B=Circle(radius=.9,color=INK).add_tip(tip_length=.25); labs=VGroup(Text("E",font=MONO,font_size=36,color=CRIMSON).next_to(E,UP),Text("v",font=MONO,font_size=36,color=TEAL).next_to(v,RIGHT),Text("B' ~ -v x E / c^2",font=MONO,font_size=42,color=INK).shift(DOWN*2.6)); B.shift(RIGHT*3+UP*1.5)
  self.play(FadeIn(heading("THE ELECTRIC FIELD BECOMES MAGNETIC IN THE MOVING FRAME",24)),GrowArrow(E),GrowArrow(v),Create(B),FadeIn(labs),run_time=1); hold(self,"B03")

class B04_NonCollinearBoosts(Scene):
 def construct(self):
  o=Dot(color=INK); b1=Arrow(ORIGIN,RIGHT*2.5,color=TEAL,buff=.1); b2=Arrow(RIGHT*2.5,RIGHT*2.5+UP*2,color=CRIMSON,buff=.1); direct=Arrow(ORIGIN,RIGHT*2.5+UP*2,color=INK,buff=.1); arc=Arc(radius=1,start_angle=0,angle=.7,color=CRIMSON).add_tip(tip_length=.2).shift(LEFT*2+UP*1); labs=VGroup(Text("boost 1",font=SERIF,font_size=26,color=TEAL).next_to(b1,DOWN),Text("boost 2",font=SERIF,font_size=26,color=CRIMSON).next_to(b2,RIGHT),Text("BOOST + ROTATION",font=DISPLAY,font_size=32,color=INK).shift(DOWN*2.3))
  self.play(FadeIn(heading("NON-COLLINEAR LORENTZ BOOSTS DO NOT JUST ADD")),FadeIn(o),GrowArrow(b1),GrowArrow(b2),GrowArrow(direct),Create(arc),FadeIn(labs),run_time=1); hold(self,"B04")

class B05_ThomasRate(Scene):
 def construct(self):
  eq=VGroup(Text("LOW-SPEED THOMAS RATE",font=DISPLAY,font_size=33,color=INK),Text("Omega_T ~ (a x v)/(2 c^2)",font=MONO,font_size=47,color=TEAL),Text("scale ~ (v^2/c^2) Omega_orbit",font=MONO,font_size=37,color=INK),Text("NOT half the orbital frequency",font=DISPLAY,font_size=31,color=CRIMSON)).arrange(DOWN,buff=.55)
  self.play(FadeIn(heading("THE REST-FRAME AXES PRECESS KINEMATICALLY")),FadeIn(eq),run_time=1); hold(self,"B05")

class B06_SubtractRates(Scene):
 def construct(self):
  naive=Arrow(DOWN*1.8,UP*2,color=CRIMSON,buff=0); thomas=Arrow(DOWN*1.8,UP*.2,color=TEAL,buff=0).shift(RIGHT*2); effective=Arrow(DOWN*1.8,UP*.9,color=INK,buff=0).shift(RIGHT*4); minus=Text("-",font=MONO,font_size=55,color=INK).shift(RIGHT*1); equals=Text("=",font=MONO,font_size=45,color=INK).shift(RIGHT*3); labs=VGroup(Text("naive Larmor",font=SERIF,font_size=27,color=CRIMSON).next_to(naive,DOWN),Text("Thomas",font=SERIF,font_size=27,color=TEAL).next_to(thomas,DOWN),Text("relative spin rate",font=SERIF,font_size=27,color=INK).next_to(effective,DOWN)); VGroup(naive,thomas,effective,minus,equals,labs).shift(LEFT*2)
  self.play(FadeIn(heading("MEASURE SPIN PRECESSION RELATIVE TO THE ROTATING FRAME")),GrowArrow(naive),FadeIn(minus),GrowArrow(thomas),FadeIn(equals),GrowArrow(effective),FadeIn(labs),run_time=1); hold(self,"B06")

class B07_ThomasHalf(Scene):
 def construct(self):
  bar=Rectangle(width=9,height=1,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.25).shift(UP*.7); half=Rectangle(width=4.5,height=1,color=TEAL,fill_color=TEAL,fill_opacity=.55).align_to(bar,LEFT).shift(UP*.7); labels=VGroup(Text("naive transformed-field coupling",font=SERIF,font_size=29,color=CRIMSON).shift(UP*1.7),Text("after Thomas subtraction",font=SERIF,font_size=29,color=TEAL).shift(DOWN*.4),Text("H_SO = 1/2 H_naive",font=MONO,font_size=49,color=INK).shift(DOWN*2))
  self.play(FadeIn(heading("CENTRAL ATOMIC MOTION LEAVES EXACTLY ONE HALF")),FadeIn(bar),FadeIn(half),FadeIn(labels),run_time=1); hold(self,"B07")

class B08_Hamiltonian(Scene):
 def construct(self):
  g=VGroup(Text("H_SO = (1/(2m^2 c^2))",font=MONO,font_size=37,color=INK),Text("x (1/r) dV/dr x L dot S",font=MONO,font_size=37,color=CRIMSON)).arrange(DOWN,buff=.45).shift(UP*.5); coul=Text("Coulomb: (1/r)dV/dr ~ 1/r^3",font=MONO,font_size=37,color=TEAL).shift(DOWN*1.8)
  self.play(FadeIn(heading("THE CORRECTED SPIN-ORBIT OPERATOR")),FadeIn(g),FadeIn(coul),run_time=1); hold(self,"B08")

class B09_LDotS(Scene):
 def construct(self):
  left=VGroup(Text("j = 3/2",font=DISPLAY,font_size=32,color=TEAL),Text("L dot S = +1/2 hbar^2",font=MONO,font_size=28,color=INK)).arrange(DOWN,buff=.55).move_to(LEFT*3.2); right=VGroup(Text("j = 1/2",font=DISPLAY,font_size=32,color=CRIMSON),Text("L dot S = -1 hbar^2",font=MONO,font_size=28,color=INK)).arrange(DOWN,buff=.55).move_to(RIGHT*3.2); diff=Text("difference = 3/2 hbar^2",font=MONO,font_size=42,color=INK).shift(DOWN*2)
  self.play(FadeIn(heading("THE TWO 2p j LEVELS SAMPLE DIFFERENT L dot S")),FadeIn(left),FadeIn(right),FadeIn(diff),run_time=1); hold(self,"B09")

class B10_NumericalSplit(Scene):
 def construct(self):
  g=VGroup(Text("<1/r^3>_2p = 1/(24 a0^3)",font=MONO,font_size=37,color=TEAL),Text("Delta E_SO = m c^2 alpha^4 / 32",font=MONO,font_size=40,color=INK),Text("= 4.53 x 10^-5 eV",font=MONO,font_size=52,color=CRIMSON)).arrange(DOWN,buff=.65)
  self.play(FadeIn(heading("THE THOMAS-CORRECTED 2p SPLITTING")),FadeIn(g),run_time=1); hold(self,"B10")

class B11_NaiveCorrect(Scene):
 def construct(self):
  a=VGroup(Text("NAIVE",font=DISPLAY,font_size=32,color=CRIMSON),Text("9.06 x 10^-5 eV",font=MONO,font_size=41,color=CRIMSON)).arrange(DOWN,buff=.5).move_to(LEFT*3); b=VGroup(Text("THOMAS-CORRECTED",font=DISPLAY,font_size=30,color=TEAL),Text("4.53 x 10^-5 eV",font=MONO,font_size=41,color=TEAL)).arrange(DOWN,buff=.5).move_to(RIGHT*3); cap=Text("Darwin term = 0 for p states",font=MONO,font_size=35,color=INK).shift(DOWN*2.1)
  self.play(FadeIn(heading("THE HALF ALREADY FIXES THIS j-SPLITTING")),FadeIn(a),FadeIn(b),FadeIn(cap),run_time=1); hold(self,"B11")

class B12_Scope(Scene):
 def construct(self):
  items=VGroup(*[Text("• "+x,font=SERIF,font_size=28,color=TEAL if i==0 else INK) for i,x in enumerate(["low-speed central electrostatic limit","exact Thomas rate contains gamma factors","electron g factor is near, not exactly, two","Dirac theory includes the structure automatically","radiative QED adds smaller refinements"])]).arrange(DOWN,aligned_edge=LEFT,buff=.42)
  self.play(FadeIn(heading("THE SEMICLASSICAL HALF HAS A DOMAIN")),LaggedStart(*[FadeIn(x,shift=RIGHT*.2) for x in items],lag_ratio=.12),run_time=1); hold(self,"B12")

class B13_YourTurn(Scene):
 def construct(self):
  q=VGroup(Text("YOUR TURN",font=DISPLAY,font_size=38,color=INK),Text("naive split",font=SERIF,font_size=30,color=INK),Text("9.06 x 10^-5 eV",font=MONO,font_size=47,color=CRIMSON),Text("apply Thomas factor 1/2",font=MONO,font_size=37,color=TEAL),Text("corrected split = ?",font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.4)
  self.play(FadeIn(q),run_time=.8); hold(self,"B13",.8)

class B14_Answer(Scene):
 def construct(self):
  a=VGroup(Text("ANSWER",font=DISPLAY,font_size=38,color=INK),Text("(1/2)(9.06 x 10^-5)",font=MONO,font_size=41,color=TEAL),Text("= 4.53 x 10^-5 eV",font=MONO,font_size=51,color=CRIMSON),Text("leading hydrogen 2p spin-orbit split",font=SERIF,font_size=29,color=INK)).arrange(DOWN,buff=.55)
  self.play(FadeIn(a),run_time=.8); hold(self,"B14",.8)

class B15_CorrectTitleOutro(Scene):
 def construct(self):
  bg=FullScreenRectangle(fill_color="#1f1d1b",fill_opacity=1,stroke_width=0); title=Text("Why Thomas Precession Halves\nthe Naive Spin-Orbit Coupling",font=DISPLAY,font_size=38,color="#f4efe8",line_spacing=.8); sig=Text("Liam, in for Bear",font=SERIF,font_size=22,color="#c46b4f").shift(DOWN*1.2)
  self.add(bg); self.play(FadeIn(title),FadeIn(sig),run_time=.8); hold(self,"B15",.8)
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.7
  self.add(bg(),ttl('The transformed magnetic field is real, '))
  stmt=Text('The transformed magnetic field is real, and the electro',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Why is their direct coupling wrong by a factor of two? ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.67
  self.add(bg(),ttl('In the electron\'s momentary rest frame, '))
  stmt=Text('In the electron\'s momentary rest frame, the nuclear ele',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Coupling spin to that field produces the naive spin-orb',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=13.31
  self.add(bg(),ttl('But two Lorentz boosts in different dire'))
  stmt=Text('But two Lorentz boosts in different directions do not c',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Their composition includes a rotation',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.42
  self.add(bg(),ttl('That rotation is Thomas precession. At l'))
  stmt=Text('That rotation is Thomas precession',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('At low speed its angular velocity is approximately one ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.61
  self.add(bg(),ttl('The spin\'s precession must be measured r'))
  stmt=Text('The spin\'s precession must be measured relative to this',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Thomas precession points so that it subtracts from the ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.68
  self.add(bg(),ttl('For a central electrostatic potential in'))
  stmt=Text('For a central electrostatic potential in the nonrelativ',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The half belongs to this comparison of precession rates',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: derive — sequential step build
 def construct(self):
  d=12.91
  self.add(bg(),ttl('The corrected operator is one over two'))
  s0=Text('The corrected operator is one over two m squared',font=SERIF,font_size=30,color=INK).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.35))
  s1=Text('For a Coulomb potential, that radial factor is p',font=SERIF,font_size=30,color=CRIMSON).shift(UP*0.4)
  s1.set_max_width(12)
  self.play(Write(s1),run_time=max(0.01,d*0.35))
  self.wait(max(0.01,d*0.3))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.35
  self.add(bg(),ttl('For a hydrogen two-p state, L dot'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('For a hydrogen two-p state, L dot S equals plus one hal',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Their difference is three halves h bar squared',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: calculate — builds line by line to result
 def construct(self):
  d=14.83
  self.add(bg(),ttl('Using the two-p expectation of one over'))
  step1=Text('Using the two-p expectation of one over r cubed, o',font=MONO,font_size=32,color=INK).shift(UP*1.5)
  step1.set_max_width(12)
  self.play(Write(step1),run_time=max(0.01,d*0.3))
  # no step2
  brace=Line(LEFT*5.5,RIGHT*5.5,color=SLATE,stroke_width=1.2).shift(DOWN*0.3)
  self.play(Create(brace),run_time=max(0.01,d*0.1))
  result=Text('result',font=MONO,font_size=46,color=CRIMSON).shift(DOWN*1.2)
  result.set_max_width(12)
  self.play(FadeIn(result),run_time=max(0.01,d*0.25))
  self.wait(max(0.01,d*0.15))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.34
  self.add(bg(),ttl('Without the Thomas half, the same calcul'))
  stmt=Text('Without the Thomas half, the same calculation gives abo',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('No extra Darwin repair is needed for this p-state diffe',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=16.96
  self.add(bg(),ttl('The semiclassical story assumes low spee'))
  stmt=Text('The semiclassical story assumes low speed, a central el',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The exact Thomas rate contains gamma factors',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B13_SDT(Scene):
 # B13 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.54
  self.add(bg(),ttl('Your turn. A naive transformed-field cal'))
  stmt=Text('A naive transformed-field calculation predicts a spin-o',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Apply the Thomas factor',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B14_SDT(Scene):
 # B14 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.94
  self.add(bg(),ttl('Multiply by one half: four point five'))
  stmt=Text('Multiply by one half: four point five three times ten t',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B15_SDT(Scene):
 # B15 SDT retrofit: generic reveal with underline
 def construct(self):
  d=3.99
  self.add(bg(),ttl('Why Thomas Precession Halves the Naive S'))
  stmt=Text('Why Thomas Precession Halves the Naive Spin-Orbit Coupl',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
