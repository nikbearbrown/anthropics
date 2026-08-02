import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));DUR={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=43,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
def box(t,c=TEAL,w=2.1):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.82).set_fill(GROUND,1).set_stroke(c,3);q=Text(t,font=MONO,color=c,font_size=25).move_to(r)
 if q.width>w*.85:q.scale_to_fit_width(w*.85)
 return VGroup(r,q)
class B02_OneState(Scene):
 def construct(self):
  k=VGroup(*[box(f"|{i:03b}>",TEAL,1.45) for i in range(8)]).arrange(RIGHT,buff=.16);brace=Brace(k,DOWN,color=SLATE);lab=Text("ONE coherent state",font=SERIF,color=CRIMSON,font_size=32,slant=ITALIC).next_to(brace,DOWN);self.play(LaggedStart(*[FadeIn(x) for x in k],lag_ratio=.09),run_time=1);self.play(GrowFromCenter(brace),FadeIn(lab),run_time=.5);self.wait(max(.5,DUR["B02"]-1.5))
class B03_Oracle(Scene):
 def construct(self):
  left=VGroup(*[box(f"x{i}",TEAL,1.3) for i in range(6)]).arrange(DOWN,buff=.14).to_edge(LEFT,buff=1.2);gate=box("U_f",CRIMSON,2.1);right=VGroup(*[box(f"phase {i}",SLATE,1.8) for i in range(6)]).arrange(DOWN,buff=.14).to_edge(RIGHT,buff=.9);arr=Arrow(left.get_right(),gate.get_left(),color=INK);arr2=Arrow(gate.get_right(),right.get_left(),color=INK);self.play(FadeIn(left),run_time=.5);self.play(GrowArrow(arr),FadeIn(gate),GrowArrow(arr2),FadeIn(right),run_time=1);self.wait(max(.5,DUR["B03"]-1.5))
class B04_MeasureOne(Scene):
 def construct(self):
  cloud=VGroup(*[box(str(i),SLATE,1.1) for i in range(8)]).arrange(RIGHT,buff=.15);m=Text("MEASURE",font=DISPLAY,color=CRIMSON,font_size=42,weight=BOLD).next_to(cloud,DOWN,buff=.8);one=box("outcome 5",TEAL,3).next_to(m,DOWN,buff=.65);self.play(FadeIn(cloud),run_time=.5);self.play(FadeIn(m),run_time=.4);self.play(FadeOut(cloud),FadeIn(one,scale=1.2),run_time=.6);self.wait(max(.5,DUR["B04"]-1.5))
class B05_RandomSampling(Scene):
 def construct(self):
  a=title("SUPERPOSITION + IMMEDIATE MEASUREMENT","one sample, not all answers",CRIMSON).to_edge(UP,buff=.7);dots=VGroup(*[Dot(color=SLATE,radius=.12).move_to([(-5+i*1.1),np.sin(i*2)*1.2,0]) for i in range(10)]);self.play(FadeIn(a),run_time=.6);self.play(LaggedStart(*[FadeIn(d) for d in dots],lag_ratio=.1),run_time=1);self.wait(max(.5,DUR["B05"]-1.6))
class B06_AmplitudeArrows(Scene):
 def construct(self):
  origins=[LEFT*4+UP*1.7,LEFT*1.3+UP*1.7,RIGHT*1.3+UP*1.7,RIGHT*4+UP*1.7];angs=[.2,2.5,.2,.8];g=VGroup(*[Arrow(o,o+np.array([np.cos(a),np.sin(a),0])*1.7,color=c,buff=0,tip_length=.2) for o,a,c in zip(origins,angs,[TEAL,CRIMSON,TEAL,SLATE])]);lab=title("AMPLITUDE = ARROW","length gives magnitude · direction gives phase").to_edge(DOWN,buff=.8);self.play(LaggedStart(*[GrowArrow(x) for x in g],lag_ratio=.15),run_time=1.2);self.play(FadeIn(lab),run_time=.5);self.wait(max(.5,DUR["B06"]-1.7))
class B07_Cancel(Scene):
 def construct(self):
  o=ORIGIN;left=Arrow(o,o+LEFT*3,color=CRIMSON,buff=0);right=Arrow(o,o+RIGHT*3,color=TEAL,buff=0);zero=Text("SUM = 0",font=DISPLAY,color=INK,font_size=52,weight=BOLD).to_edge(DOWN,buff=1);self.play(GrowArrow(left),GrowArrow(right),run_time=.9);self.play(FadeIn(zero),run_time=.5);self.wait(max(.5,DUR["B07"]-1.4))
class B08_Reinforce(Scene):
 def construct(self):
  a=Arrow(LEFT*4,LEFT*1,color=TEAL,buff=0);b=Arrow(LEFT*1,RIGHT*2,color=TEAL,buff=0);big=Arrow(LEFT*4,RIGHT*2,color=CRIMSON,buff=0,stroke_width=9);lab=Text("ALIGNED AMPLITUDES ADD",font=DISPLAY,color=INK,font_size=42,weight=BOLD).to_edge(DOWN,buff=.9);self.play(GrowArrow(a),GrowArrow(b),run_time=.8);self.play(ReplacementTransform(VGroup(a.copy(),b.copy()),big),FadeIn(lab),run_time=.8);self.wait(max(.5,DUR["B08"]-1.6))
class B09_BiasedDistribution(Scene):
 def construct(self):
  bars=VGroup();vals=[.3,.15,.25,3.6,.2,.1,.3]
  for i,v in enumerate(vals):
   r=Rectangle(width=.75,height=v).set_fill(CRIMSON if i==3 else SLATE,.8).set_stroke(width=0).align_to(DOWN*2.2,DOWN).shift(RIGHT*(i-3)*1.15);bars.add(r)
  base=Line(LEFT*5,RIGHT*5,color=INK).shift(DOWN*2.2);lab=Text("interference reshapes probabilities",font=SERIF,color=TEAL,font_size=31,slant=ITALIC).to_edge(UP,buff=.7);self.play(Create(base),LaggedStart(*[GrowFromEdge(r,DOWN) for r in bars],lag_ratio=.1),FadeIn(lab),run_time=1.4);self.wait(max(.5,DUR["B09"]-1.4))
class B10_NoiseCancel(Scene):
 def construct(self):
  x=np.linspace(-5,5,120);p=VMobject(color=CRIMSON).set_points_smoothly([np.array([u,np.sin(u*2.5)+1.4,0]) for u in x]);q=VMobject(color=TEAL).set_points_smoothly([np.array([u,-np.sin(u*2.5)-1.4,0]) for u in x]);flat=Line(LEFT*5,RIGHT*5,color=INK,stroke_width=5);lab=title("ENGINEER THE PHASE","unwanted pattern cancels · useful structure survives",CRIMSON).to_edge(DOWN,buff=.7);self.play(Create(p),Create(q),run_time=1);self.play(Transform(VGroup(p,q),flat),FadeIn(lab),run_time=.9);self.wait(max(.5,DUR["B10"]-1.9))
class B11_Recipe(Scene):
 def construct(self):
  g=VGroup(box("STRUCTURE",TEAL,2.7),box("PHASE",CRIMSON,2.7),box("INTERFERE",TEAL,2.7),box("MEASURE",CRIMSON,2.7)).arrange(RIGHT,buff=.28);ar=VGroup(*[Arrow(g[i].get_right(),g[i+1].get_left(),color=SLATE,buff=.08,tip_length=.15) for i in range(3)]);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.15),run_time=1);self.play(*[GrowArrow(x) for x in ar],run_time=.7);self.wait(max(.5,DUR["B11"]-1.7))
class B12_Correction(Scene):
 def construct(self):
  rows=VGroup(title("SUPERPOSITION","carries many amplitudes"),title("INTERFERENCE","filters the global pattern",CRIMSON),title("MEASUREMENT","extracts one biased result")).arrange(DOWN,buff=.45);self.play(LaggedStart(*[FadeIn(r,shift=UP*.1) for r in rows],lag_ratio=.18),run_time=1.4);self.wait(max(.5,DUR["B12"]-1.4))
class B14_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Quantum Speed Isn't",font=DISPLAY,color=WHITE,font_size=50,weight=BOLD);b=Text("Trying Everything at Once",font=SERIF,color="#D7C8FF",font_size=39,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,DUR["B14"]-.7))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.0
  self.add(bg(),ttl('Repeat that naive strategy and it behave'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Repeat that naive strategy and it behaves like random s',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Many populated branches are useless if the answer remai',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Now measurement becomes useful. The circ'))
  stmt=Text('Now measurement becomes useful',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The circuit has reshaped the distribution so a revealin',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B12_SDT(Scene):
 # B12 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('So the correction is precise: superposit'))
  stmt=Text('So the correction is precise: superposition lets one ev',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Interference filters their global pattern',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B14_SDT(Scene):
 # B14 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.0
  self.add(bg(),ttl('Quantum speed is not trying everything a'))
  stmt=Text('Quantum speed is not trying everything at once',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It is engineering interference so one measurement says ',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
