import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def bloch(theta=55,phase=35,scale=1):
 o=DOWN*.3; r=2.4*scale; a=np.deg2rad(theta); p=np.deg2rad(phase)
 sphere=Circle(radius=r,color=SLATE).move_to(o); equator=Ellipse(width=2*r,height=.65*r,color=SLATE).move_to(o)
 axis=DoubleArrow(o+DOWN*r*1.2,o+UP*r*1.25,color=INK,buff=0,stroke_width=3)
 tip=o+np.array([r*np.sin(a)*np.cos(p),r*np.cos(a),0])
 vec=Arrow(o,tip,color=CRIMSON,buff=0,stroke_width=7)
 lat=Ellipse(width=2*r*np.sin(a),height=.45*r*np.sin(a),color=TEAL).move_to(o+UP*r*np.cos(a))
 return VGroup(sphere,equator,axis,lat,vec)
class B02_Tilt(Scene):
 def construct(self):
  d=DUR.get('B02',10); self.add(bg(),ttl('A TILTED SPIN PRECESSES AROUND B')); b=bloch(); field=Arrow(DOWN*2.8,UP*2.8,color=TEAL,buff=0).shift(LEFT*4); lab=Text('B along z',font=MONO,font_size=29,color=TEAL).move_to(LEFT*4+DOWN*3.1); self.play(GrowArrow(field),Create(b),FadeIn(lab),run_time=1.2); self.wait(max(.1,d-1.2))
class B03_Latitude(Scene):
 def construct(self):
  d=DUR.get('B03',9); self.add(bg(),ttl('CONSTANT LATITUDE · MOVING AZIMUTH')); b=bloch(); z=DashedLine(DOWN*.3,UP*1.05,color=TEAL); labs=VGroup(Text('<Sz> fixed',font=MONO,font_size=30,color=TEAL).move_to(LEFT*4+UP*1),Text('phi advances',font=MONO,font_size=30,color=CRIMSON).move_to(RIGHT*4+UP*1)); self.play(Create(b),Create(z),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B04_Question(Scene):
 def construct(self):
  d=DUR.get('B04',11); self.add(bg(),ttl('WHAT MOVES IF THE z PROJECTION DOES NOT?')); left=Text('<Sz> = constant',font=MONO,font_size=40,color=TEAL).move_to(LEFT*3); right=VGroup(CurvedArrow(DOWN*1.5,UP*1.5,color=CRIMSON),Text('constant rate',font=SERIF,font_size=31,color=CRIMSON).move_to(RIGHT*3+DOWN*2)).move_to(RIGHT*3); self.play(FadeIn(left),Create(right),run_time=1); self.wait(max(.1,d-1))
class B05_NoAlign(Scene):
 def construct(self):
  d=DUR.get('B05',11); self.add(bg(),ttl('A STATIC FIELD DOES NOT SUPPLY DISSIPATION')); align=Arrow(DOWN*1.8,UP*1.8,color=SLATE,buff=0).shift(LEFT*3); pre=bloch(scale=.65).shift(RIGHT*3); cross=Cross(align,color=CRIMSON); labs=VGroup(Text('simple alignment',font=MONO,font_size=26,color=SLATE).move_to(LEFT*3+DOWN*2.7),Text('precession',font=MONO,font_size=28,color=TEAL).move_to(RIGHT*3+DOWN*2.7)); self.play(GrowArrow(align),Create(pre),Create(cross),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B06_Phases(Scene):
 def construct(self):
  d=DUR.get('B06',14); self.add(bg(),ttl('TWO PHASE CLOCKS CREATE ONE RELATIVE PHASE')); c1=Circle(radius=1.5,color=TEAL).shift(LEFT*3); c2=Circle(radius=1.5,color=CRIMSON).shift(RIGHT*3); h1=Arrow(c1.get_center(),c1.get_center()+UP*1.2,color=TEAL,buff=0); h2=Arrow(c2.get_center(),c2.get_center()+RIGHT*1.1+UP*.4,color=CRIMSON,buff=0); labs=VGroup(Text('|up>',font=MONO,font_size=29,color=TEAL).move_to(LEFT*3+DOWN*2.3),Text('|down>',font=MONO,font_size=29,color=CRIMSON).move_to(RIGHT*3+DOWN*2.3),Text('relative phase = azimuth',font=SERIF,font_size=33,color=INK).move_to(DOWN*3.1)); self.play(Create(c1),Create(c2),GrowArrow(h1),GrowArrow(h2),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B07_Rate(Scene):
 def construct(self):
  d=DUR.get('B07',12); self.add(bg(),ttl('THE LARMOR RATE SCALES WITH FIELD')); eq=Text('|omega| = |gamma| B',font=MONO,font_size=48,color=CRIMSON).move_to(UP*1.5); axes=Axes(x_range=[0,4,1],y_range=[0,4,1],x_length=7,y_length=3,axis_config={'color':SLATE}).shift(DOWN*1.2); line=axes.plot(lambda x:x,x_range=[0,4],color=TEAL); labs=VGroup(Text('B',font=MONO,font_size=25,color=INK).move_to(RIGHT*4+DOWN*2.7),Text('|omega|',font=MONO,font_size=25,color=INK).move_to(LEFT*4+UP*.7)); self.play(FadeIn(eq),Create(axes),Create(line),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))
class B08_Amplitudes(Scene):
 def construct(self):
  d=DUR.get('B08',13); self.add(bg(),ttl('MAGNITUDES FIXED · RELATIVE PHASE MOVES')); bars=VGroup(Rectangle(width=1.2,height=3,color=TEAL,fill_color=TEAL,fill_opacity=.18),Rectangle(width=1.2,height=1.7,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.18)).arrange(RIGHT,buff=1.5).shift(LEFT*3); labels=VGroup(Text('|alpha|^2',font=MONO,font_size=27,color=TEAL).next_to(bars[0],DOWN),Text('|beta|^2',font=MONO,font_size=27,color=CRIMSON).next_to(bars[1],DOWN)); clock=VGroup(Circle(radius=1.7,color=SLATE),Arrow(ORIGIN,UP*1.35+RIGHT*.7,color=CRIMSON,buff=0)).shift(RIGHT*3); self.play(FadeIn(bars,labels),Create(clock),run_time=1); self.wait(max(.1,d-1))
class B09_MRI(Scene):
 def construct(self):
  d=DUR.get('B09',17); self.add(bg(),ttl('PROTON RESONANCE IN CLINICAL FIELDS')); rows=VGroup(Text('1.5 T   ->   63.9 MHz',font=MONO,font_size=40,color=TEAL),Text('3.0 T   ->  127.7 MHz',font=MONO,font_size=40,color=CRIMSON),Text('f = |gamma|B / (2 pi)',font=MONO,font_size=33,color=INK),Text('RF pulse near resonance · detect ensemble response',font=SERIF,font_size=30,color=INK)).arrange(DOWN,buff=.65); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',20); self.add(bg(),ttl('YOUR TURN: 60 DEG AT 1.5 T')); eqs=VGroup(Text('<Sz> = (hbar/2) cos(60 deg)',font=MONO,font_size=35,color=INK),Text('= hbar/4   (constant)',font=MONO,font_size=38,color=TEAL),Text('azimuth cycles at about 63.9 MHz',font=MONO,font_size=31,color=CRIMSON)).arrange(DOWN,buff=.7); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',14); self.add(bg(),Text('THE SPINNING COMPASS INSIDE EVERY MRI',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('fixed amplitudes',font=MONO,font_size=35,color=TEAL).move_to(UP*.8),Text('relative phase advances',font=MONO,font_size=35,color=INK).move_to(DOWN*.4),Text('Bloch azimuth precesses at |gamma|B',font=MONO,font_size=32,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.73
  self.add(bg(),ttl('Drop a proton into a magnetic field'))
  stmt=Text('Drop a proton into a magnetic field pointing up',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The proton\'s spin arrow tilts at some angle — and then,',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.81
  self.add(bg(),ttl('The z-component stays exactly fixed the '))
  stmt=Text('The z-component stays exactly fixed the whole time',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Only the horizontal part rotates',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.7
  self.add(bg(),ttl('Naive picture: a field should simply pul'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Naive picture: a field should simply pull the spin into',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('But without dissipation, even a classical magnetic mome',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B06_SDT(Scene):
 # B06 SDT retrofit: generic reveal with underline
 def construct(self):
  d=14.63
  self.add(bg(),ttl('The mechanism: the field makes each spin'))
  stmt=Text('The mechanism: the field makes each spin eigenstate adv',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The up-state gains phase at one speed, the down-state a',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=13.23
  self.add(bg(),ttl('Why does Lz stay fixed? The phase'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Why does Lz stay fixed? The phase advance on each eigen',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The polar angle is unchanged',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=18.24
  self.add(bg(),ttl('In a 1.5 tesla clinical MRI scanner,'))
  stmt=Text('5 tesla clinical MRI scanner, proton frequency is about',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('9 megahertz — nearly 64 million cycles per second',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=18.09
  self.add(bg(),ttl('Your turn. A proton spin is tilted'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('A proton spin is tilted 60 degrees from z in a 1',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('5 tesla field',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
