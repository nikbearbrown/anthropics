import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def well_wave(n,y=0,col=TEAL,squared=False,lean=0):
 xs=np.linspace(0,1,350); pts=[]
 for x in xs:
  val=np.sin(n*PI*x); val=val*val if squared else val
  if squared and lean: val*=np.exp(lean*(2*x-1)-abs(lean))
  pts.append(np.array([-5+10*x,y+1.6*val,0]))
 return VMobject(color=col,stroke_width=4).set_points_smoothly(pts)
def walls(y=0): return VGroup(Line(np.array([-5,y,0]),np.array([-5,y+2.2,0]),color=INK),Line(np.array([5,y,0]),np.array([5,y+2.2,0]),color=INK),Line(np.array([-5,y,0]),np.array([5,y,0]),color=SLATE))

class B02_States(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("TWO STATIONARY DENSITIES")); w1=well_wave(1,1.1,TEAL,True).scale(.48).move_to(LEFT*3.6+DOWN*.4); w2=well_wave(2,1.1,CRIMSON,True).scale(.48).move_to(RIGHT*3.6+DOWN*.4); labs=VGroup(Text("n=1: one arch",font=MONO,font_size=25,color=TEAL).move_to(LEFT*3.6+DOWN*2.3),Text("n=2: center node",font=MONO,font_size=25,color=CRIMSON).move_to(RIGHT*3.6+DOWN*2.3),Text("each |phi_n|^2 is fixed",font=SERIF,font_size=29,color=INK).move_to(DOWN*3.1)); self.play(Create(w1),Create(w2),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("How can two fixed patterns",font=SERIF,font_size=42,color=INK).move_to(UP*.5),Text("make a moving one?",font=SERIF,font_size=45,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_AmplitudeSum(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("ADD AMPLITUDES FIRST")); eq=Text("psi = c1 phi1 exp(-iE1t/hbar) + c2 phi2 exp(-iE2t/hbar)",font=MONO,font_size=28,color=INK); a=Text("not  |phi1|^2 + |phi2|^2",font=MONO,font_size=29,color=CRIMSON).move_to(DOWN*1.7); self.play(Write(eq),run_time=1); self.play(FadeIn(a),run_time=.7); self.wait(max(.1,d-1.7))

class B05_CrossTerm(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("SQUARING THE SUM CREATES INTERFERENCE")); terms=VGroup(Text("|psi|^2 =",font=MONO,font_size=31,color=INK),Text("|c1 phi1|^2 + |c2 phi2|^2",font=MONO,font_size=29,color=TEAL),Text("+ 2 Re[c1* c2 phi1 phi2 exp(-i DeltaE t/hbar)]",font=MONO,font_size=25,color=CRIMSON)).arrange(DOWN,buff=.7); tag=Text("time-dependent cross term",font=SERIF,font_size=28,color=CRIMSON).move_to(DOWN*2.8); self.play(FadeIn(terms[:2]),run_time=.8); self.play(FadeIn(terms[2],tag),run_time=.8); self.wait(max(.1,d-1.6))

class B06_Positive(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("POSITIVE CROSS TERM: DENSITY LEANS LEFT")); w=well_wave(1,-1,TEAL,True,lean=-1.6); ws=walls(-1); clock=Text("cos(DeltaE t / hbar) = +1",font=MONO,font_size=27,color=CRIMSON).move_to(UP*2.2); self.play(Create(ws),Create(w),FadeIn(clock),run_time=1); self.wait(max(.1,d-1))

class B07_Negative(Scene):
 def construct(self):
  d=DUR.get("B07",10); self.add(bg(),ttl("HALF A BEAT LATER: DENSITY LEANS RIGHT")); w=well_wave(1,-1,TEAL,True,lean=1.6); ws=walls(-1); clock=Text("cos(DeltaE t / hbar) = -1",font=MONO,font_size=27,color=CRIMSON).move_to(UP*2.2); self.play(Create(ws),Create(w),FadeIn(clock),run_time=1); self.wait(max(.1,d-1))

class B08_Cycle(Scene):
 def construct(self):
  d=DUR.get("B08",11); self.add(bg(),ttl("ONE FULL SLOSH CYCLE")); leans=[-1.6,0,1.6,0]; groups=[]
  for i,l in enumerate(leans):
   g=VGroup(well_wave(1,-.5,TEAL,True,l).scale(.23),Text(["left","center","right","center"][i],font=MONO,font_size=20,color=INK).move_to(DOWN*1.6)).move_to(np.array([-5.1+i*3.4,0,0])); groups.append(g)
  arrows=VGroup(*[Arrow(np.array([-3.9+i*3.4,0,0]),np.array([-2.9+i*3.4,0,0]),color=SLATE,buff=0) for i in range(3)]); self.play(FadeIn(VGroup(*groups)),GrowFromCenter(arrows),run_time=1.1); self.wait(max(.1,d-1.1))

class B09_PositionTrace(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("THE MEAN POSITION OSCILLATES AT THE ENERGY GAP")); ax=Axes(x_range=[0,2*PI,PI/2],y_range=[-.8,.8,.4],x_length=10,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda t:.6*np.cos(t),x_range=[0,2*PI],color=TEAL); labs=VGroup(Text("time",font=MONO,font_size=23,color=INK).next_to(ax,DOWN),Text("<x>-L/2",font=MONO,font_size=23,color=INK).next_to(ax,LEFT),Text("omega = (E2-E1)/hbar",font=MONO,font_size=27,color=CRIMSON).move_to(UP*2.4)); self.play(Create(ax),Create(curve),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B10_EnergyWeights(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("ENERGY PROBABILITIES DO NOT SLOSH")); bars=VGroup(Rectangle(width=2.2,height=2.8,color=TEAL,fill_color=TEAL,fill_opacity=.25).move_to(LEFT*2),Rectangle(width=2.2,height=2.8,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.25).move_to(RIGHT*2)); labs=VGroup(Text("P(E1)=|c1|^2",font=MONO,font_size=25,color=TEAL).next_to(bars[0],DOWN),Text("P(E2)=|c2|^2",font=MONO,font_size=25,color=CRIMSON).next_to(bars[1],DOWN),Text("constant in time",font=SERIF,font_size=30,color=INK).move_to(UP*2.4)); self.play(GrowFromEdge(bars,DOWN),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B11_OneState(Scene):
 def construct(self):
  d=DUR.get("B11",10); self.add(bg(),ttl("NO SECOND CLOCK, NO BEAT")); one=VGroup(Text("c2 = 0",font=MONO,font_size=38,color=CRIMSON),Text("psi = c1 phi1 exp(-iE1t/hbar)",font=MONO,font_size=28,color=INK),Text("|psi|^2 is stationary",font=SERIF,font_size=34,color=TEAL)).arrange(DOWN,buff=.75); self.play(FadeIn(one),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("EACH EIGENSTATE IS STATIONARY",font=DISPLAY,font_size=30,color=TEAL).move_to(UP*1.7),Text("their relative phase is not",font=SERIF,font_size=40,color=CRIMSON),Text("the cross term makes probability slosh",font=SERIF,font_size=29,color=INK).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.67
  self.add(bg(),ttl('The ground state has one arch and'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The ground state has one arch and the second state has ',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Each state by itself only gains a global phase, so its ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.69
  self.add(bg(),ttl('The relative phase advances at angular f'))
  stmt=Text('The relative phase advances at angular frequency E two ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('When its cosine is positive, interference adds probabil',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.87
  self.add(bg(),ttl('Half a beat later, the cosine changes'))
  stmt=Text('Half a beat later, the cosine changes sign',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The side that gained probability now loses it, and the ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.33
  self.add(bg(),ttl('Over a full beat period, the density'))
  stmt=Text('Over a full beat period, the density rocks left, become',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The walls do not push it',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.88
  self.add(bg(),ttl('If the state contains only one energy,'))
  stmt=Text('If the state contains only one energy, there is no seco',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Motion in the density requires coherent superposition o',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
