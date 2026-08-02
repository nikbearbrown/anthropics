# Three title options

**Inside the Train, Nothing Moves**

**Why a Train at 300 mph Feels Still**

**Motion Needs a Witness**

---

## TL;DR

Motion is invisible without a reference frame to compare against. Distance and displacement are different because one counts the path, the other counts the net change; velocity and speed differ in the same way. Graphs encode motion as geometry — slopes reveal velocity, areas reveal displacement.

---

## Chapter opening: The paradox of motion

You're sitting in a high-speed train. The rails blur beneath you, yet as you look at a coffee cup on the table in front of you, it sits perfectly still. A person standing outside watching the train pass sees that same cup hurtling at 280 kilometers per hour. Who is right?

Both are. The motion you see depends entirely on where you choose to stand and measure from.

This sounds like a riddle, but it is the foundation of all physics. For three centuries, physicists have built their understanding of the world on a simple fact: motion is not a property of objects. Motion is a *relationship* between an object and something else — a reference frame. Before you can describe how fast something moves, or in which direction, you must answer the question: *moving relative to what?*

This chapter builds the language for talking about motion clearly. That language has three parts. First, how do we specify position and measure the path versus the net change? Distance and displacement are not the same word by accident; they measure different things. Second, how do we describe rates — how fast something travels, and does direction matter? Speed and velocity wear similar names, but they do opposite work in the physics. Third, how do we extract motion from a graph? A curved line on paper is not motion. But the slope of that line, or the area underneath it, encodes motion information with precision that words cannot match.

By the end of this chapter, you will be able to:
- Identify and draw the consequences of choosing different reference frames
- Calculate and distinguish distance from displacement  
- Calculate and distinguish speed from velocity
- Extract velocity, displacement, and acceleration from position-time and velocity-time graphs
- Solve problems using graphical representations of motion

**Prerequisites:** You can convert units (miles to kilometers, hours to seconds). You can calculate an average (add two numbers, divide by two). You know what the Greek letter Δ means: *change in*. You have seen a coordinate grid.

**Why this chapter matters:** Motion is how the world changes. Before you can explain why things move (forces), or why they move the way they do (Newton's laws), you need to describe motion precisely. This chapter builds that vocabulary. It is foundational to everything that follows.

---

## Core Concept 1: Position, reference frames, and why motion is relative

**Scene: The stadium at dusk**

Stand in a stadium at sunset. The sun, from your viewpoint, sinks steadily toward the horizon. A friend stands in Brazil, on the opposite side of Earth. The sun, from their viewpoint, rises. The sun's position is the same object, the same light. But the description — *setting* or *rising* — depends entirely on where you stand. This is not a metaphor. This is what physicists mean by "reference frame."

**The mechanism**

A reference frame is a coordinate system anchored to something. Usually, you pick something stationary (the ground, the walls of your classroom) and put your zero point — your origin — there. Then, you can describe any other object's position relative to that zero. The object is three meters north of the origin. The object is 1.5 meters above the origin. The position is always a comparison: *where is this thing relative to my chosen zero?*

The word *position* itself means location measured from a chosen starting point. Mathematically, if your origin is at zero, and an object sits at point $d_0$ at the beginning, and at point $d_f$ at the end, then the object's position has changed.

Here is where it gets interesting. If you and I choose *different* origins, we will assign *different* position numbers to the same object. But we will agree on one thing: how much the object's position changed. The change in position is the *displacement*, written as $\Delta d = d_f - d_0$. If I put my origin at my feet and you put your origin ten meters away, we disagree about where the object is. But if that object moves three meters toward the wall, we both record $\Delta d = 3$ meters.

Displacement is frame-independent in its *magnitude*. It is not frame-independent in its *sign*. If I set rightward as positive and you set leftward as positive, the same motion gets opposite signs. That is why direction matters. Displacement includes direction; it is a *vector*. Speed (how fast) does not include direction; it is a *scalar*.

The distinction between vector and scalar is not merely a bookkeeping convention. It matters physically. A scalar quantity — say, temperature at a point on Earth — tells you one number. A vector quantity — say, wind velocity — tells you both magnitude and direction. The direction is not extra information; it is essential. Wind traveling at 20 m/s northward is fundamentally different from wind traveling at 20 m/s eastward. The magnitude is the same; the consequences are not.

**Named trade-off: Distance vs. Displacement**

Distance is the length of the actual path traveled. If you walk to school via a winding route, the distance is the sum of all the steps — 1.5 km west, then 0.8 km north, then 0.6 km east. Total distance traveled: 2.9 km.

Displacement is the straight-line net change from start to finish. Home is your origin. School is 1.5 km west of home. Your displacement is 1.5 km west, regardless of how many detours you took. If you then walk home, your displacement is zero — you ended where you began.

The trade-off: Distance tells you how much ground the object covered. Displacement tells you the object's *net* position change. You need both. Distance is always positive or zero. Displacement can be positive, negative, or zero, depending on whether you chose forward or backward as positive.

**Worked example: The cyclist's round trip**

A cyclist rides 3 km west, then turns and rides 2 km east.

*What is her displacement?* Set west as negative, east as positive. She starts at position $d_0 = 0$. After riding west, she is at $d = -3$ km. After riding east 2 km, she is at $d = -3 + 2 = -1$ km. Displacement is $\Delta d = d_f - d_0 = -1 - 0 = -1$ km. The negative sign tells you: net movement westward.

*What is the distance?* The path length is 3 km + 2 km = 5 km. Distance has no direction, so it is always positive.

*The magnitude of displacement?* The magnitude ignores sign. It is 1 km.

Notice what happened: we *set* a positive direction, applied the sign consistently, and let the math do the work. Displacement is displacement by definition; the negative sign falls out from the choice we made at the start.

**Common misconceptions**

*Misconception 1:* "Displacement is the shortest distance between two points." This is close, but incomplete. Displacement is the *net change in position*, which is a straight line with magnitude and direction. The shortest distance is just the magnitude part. Displacement includes direction.

*Misconception 2:* "If an object goes out and comes back to where it started, the displacement is distance." No. If an object returns to its starting point, the displacement is zero. The distance is whatever the path length was. The object went nowhere (displacement = 0) even though it traveled some distance.

---

## Core Concept 2: Speed and velocity (averages and instantaneous)

**Scene: The car's speedometer**

You glance at the speedometer. It reads 60 km/h. What does that number mean? It is *not* your average speed since the last traffic light. It is your speed *right now*, at this instant. But what is a "speed at an instant"? You did not travel any distance in zero time. How can speed exist at a single moment?

This puzzle — the difference between average and instantaneous — runs through all of motion. Velocity adds a second puzzle: direction.

**The mechanism**

Speed is how fast an object's position changes, measured over some time interval. The formula is simple:

$$v_{\text{avg}} = \frac{\text{distance}}{\text{time}}$$

For a car that travels 150 km in 3.2 hours, the average speed is 150 ÷ 3.2 = 47 km/h.

But a car's speed fluctuates. Instantaneous speed is the speed at a specific moment in time, what the speedometer shows. If you want the instantaneous speed, you must measure the distance traveled in an *infinitesimally small* time interval — so small that the speed does not have time to change during the measurement. This is where calculus enters (we will not need the calculation here, just the concept): instantaneous speed is the limit of average speed as the time interval shrinks to zero.

Velocity is the vector version of speed: it includes direction. Average velocity is:

$$\mathbf{v}_{\text{avg}} = \frac{\text{displacement}}{\text{time}} = \frac{\Delta d}{\Delta t} = \frac{d_f - d_0}{t_f - t_0}$$

Instantaneous velocity is velocity at a specific moment. If velocity is constant, the instantaneous and average are the same. If velocity changes, they differ.

Why does this distinction matter? Because a car traveling north at 60 km/h is in a different state than a car traveling south at 60 km/h. The speeds are identical. The velocities are opposite. In physics, direction is information, not decoration.

**Named trade-off: Speed vs. Velocity**

You drive 150 km to a city, then drive 150 km back home. Total distance: 300 km. Total displacement: 0 km (you ended where you started).

Average speed: 300 km ÷ total time.

Average velocity: 0 km ÷ total time = 0.

The trade-off: Speed captures how *much ground* you covered in how much time. Velocity captures your *net progress* in a direction. Speed is always positive. Velocity can be positive, negative, or zero, depending on your chosen positive direction.

When would you use each? Use speed when you care about fuel consumption or travel time — questions about effort and duration. Use velocity when you care about net displacement — where you end up, and whether you're making progress toward a goal.

**Worked example: The jogger**

Layla jogs 304 m north in 180 seconds.

*What is her average velocity?* Use the formula:

$$\mathbf{v}_{\text{avg}} = \frac{304 \text{ m}}{180 \text{ s}} = 1.7 \text{ m/s north}$$

The direction is essential. If someone asks for your velocity, the answer is incomplete without it.

*What if she jogged the same distance but in a zigzag?* Her average velocity would still be 1.7 m/s north. Velocity depends on displacement, not distance. Distance traveled is longer; velocity is the same because her start and end points were the same.

This is the key difference. Imagine two joggers cover the same start and end points in the same time. One takes a straight path; one takes a winding path. They have the *same* average velocity. They have *different* average speeds. This difference becomes crucial when we study motion in two and three dimensions, where a curved path and a straight path have the same displacement but different distances.

**Common misconceptions**

*Misconception 1:* "Average velocity is the average of the initial and final speeds." Wrong. This is tempting because it works for uniform motion. If you drive at 30 km/h for 50 km, then 60 km/h for another 50 km, your average speed is *not* 45 km/h. It is: total distance ÷ total time = 100 km ÷ (50/30 + 50/60) hours = 40 km/h. The reason: you spend more time at the slower speed. Average velocity is always displacement ÷ time.

*Misconception 2:* "Velocity is just speed with a direction label." Close, but incomplete. Velocity *changes* differently than speed when direction changes. If you walk in a circle at constant speed, your speed is constant but your velocity is *constantly changing* (because direction is changing). This will matter when we discuss acceleration in the next chapter.

---

## Core Concept 3: Reading motion from graphs (position-time and velocity-time)

**Scene: A line on paper**

You have a straight line on a graph. Time is on the horizontal axis. Position is on the vertical axis. What does that line tell you?

It tells you motion. But how? A line is static. Motion is dynamic. How does a static image capture something that changes?

The answer: *the slope of the line is the velocity*. The answer is hidden in the slope.

**The mechanism: Position vs. time**

Consider the graph of a car's motion. At $t = 0$ s, the car is at position $d_0 = 0$ km (home). At $t = 10$ minutes, the car is at position $d_f = 5$ km (school). If you plot these two points and draw a line between them, the line has a slope.

Slope is defined as rise divided by run:

$$\text{slope} = \frac{\text{rise}}{\text{run}} = \frac{\text{change in position}}{\text{change in time}} = \frac{\Delta d}{\Delta t}$$

But $\Delta d / \Delta t$ is the definition of average velocity. The slope of a position-time graph is the average velocity.

If the line is straight, the motion is uniform (constant velocity). If the line is curved, the velocity is changing. To find the instantaneous velocity at a point on a curved graph, draw a tangent line — a straight line that touches the curve at exactly one point. The slope of that tangent is the instantaneous velocity at that moment.

The advantage of the graphical method is visual clarity. A steep slope means fast motion. A shallow slope means slow motion. A horizontal line (zero slope) means the object is stationary. A negative slope means the object is moving backward (in the negative direction).

**Worked example: The jet car on a flat lakebed**

A jet-powered car starts from rest and accelerates across a dry lakebed in Nevada. Here is a position-time graph of its motion. What is the car's average velocity?

Two points from the graph: at $t = 0.5$ s, $d = 525$ m. At $t = 6.4$ s, $d = 2000$ m.

$$v = \frac{\Delta d}{\Delta t} = \frac{2000 - 525}{6.4 - 0.5} = \frac{1475}{5.9} = 250 \text{ m/s}$$

That is 900 km/h — far faster than a highway speed limit, but well short of the land speed record (1,234 km/h, set in 1997). The calculation shows how a graph can encode precise numerical information from just a visual pattern.

**The mechanism: Velocity vs. time**

A velocity-time graph works differently. Time is still on the horizontal axis, but velocity is on the vertical axis. What information does this graph hold?

The *slope* of a velocity-time graph is acceleration — the rate at which velocity changes. We will discuss acceleration deeply in the next chapter.

The *area* under a velocity-time graph is displacement. This is because $v \times t = d$ (rearranging the velocity equation). If velocity is constant, the area is a rectangle: width times height. If velocity varies, you can approximate the area under the curve by breaking it into rectangles and triangles, or by using calculus.

Why does area represent displacement? Because multiplication of velocity and time gives distance: (meters per second) times (seconds) gives (meters). The product is encoded geometrically as the area under the curve.

**Worked example: The drive to and from school**

A car drives to school at a constant velocity of 0.5 km per minute for 10 minutes. Then, for 10 minutes, it drives back home at a constant velocity of –0.5 km per minute (negative because it is moving in the opposite direction).

On a position-time graph, the outbound trip is a straight line with positive slope (moving forward). The return trip is a straight line with negative slope (moving backward).

On a velocity-time graph, the outbound trip is a horizontal line at +0.5 km/min. The return trip is a horizontal line at –0.5 km/min.

*What is the displacement from the area under the velocity-time curve?*

Outbound: area = (0.5 km/min) × (10 min) = 5 km.
Return: area = (–0.5 km/min) × (10 min) = –5 km.
Total displacement: 5 + (–5) = 0 km. The car is back home.

*What is the distance?* Distance is the sum of the absolute values of the areas (because distance is always positive): 5 km + 5 km = 10 km.

**Common misconceptions**

*Misconception 1:* "A curved position-time graph means the object is moving fast." A curve means *velocity is changing*. The steepness of the curve (the slope at that point) tells you the velocity. A shallow curve might represent slow motion with increasing speed, or fast motion with decreasing speed.

*Misconception 2:* "The area under a position-time graph is displacement." No. The slope is velocity (actually, the *change* in position is related to the slope and time interval). The area under a position-time graph has units of (position) × (time), which is not a standard kinematic quantity. Area matters for velocity-time graphs.

---

## Integration: How the concepts fit together

Position, reference frame, distance, displacement, speed, velocity, and graphs are not separate ideas. They are one idea with different faces.

Start with a reference frame: you choose where zero is and what direction is positive.

From the reference frame, position becomes meaningful. Position is always relative; it is a location measured from your zero.

Distance and displacement both measure change in position. Distance counts the path. Displacement counts the net change. The two are equal only if the path is straight in one direction.

Speed and velocity both measure how fast position changes. Speed ignores direction; velocity includes it. They are equal only if the motion is in one direction.

Graphs encode this. A position-time graph with slope $m$ tells you the velocity is $m$. A velocity-time graph with area $A$ tells you the displacement is $A$.

**Integrated worked example**

A student jogs home. She leaves her school at a position 1.2 km east of her home. She jogs west at a constant speed of 2.4 m/s for 8 minutes, then stops for 2 minutes, then jogs west again at 2.4 m/s for 4 more minutes.

*Set up the reference frame.* Home is the origin. East is positive. School is at $d_0 = +1200$ m.

*Calculate her displacement during each phase.*

Phase 1 (jog for 8 minutes): 
- Time: 8 min = 480 s
- Velocity: –2.4 m/s (westward, so negative)
- Displacement: $v \times t = (-2.4 \text{ m/s})(480 \text{ s}) = -1152 \text{ m}$
- Final position: $d = 1200 + (-1152) = 48 \text{ m}$ (east of home)

Phase 2 (stop for 2 minutes):
- Displacement: 0 m
- Final position: still 48 m east of home

Phase 3 (jog for 4 minutes):
- Time: 4 min = 240 s
- Velocity: –2.4 m/s
- Displacement: $(-2.4)(240) = -576 \text{ m}$
- Final position: $48 + (-576) = -528 \text{ m}$ (528 m west of home)

*What is her total displacement?* $\Delta d = -528 - 1200 = -1728 \text{ m}$ westward.

*What is her total distance?* Distance is path length, ignoring stops: 1152 + 576 = 1728 m.

*What is her average velocity?* Total time is 8 + 2 + 4 = 14 minutes = 840 s. Average velocity is $\Delta d / \Delta t = -1728 / 840 = -2.06 \text{ m/s}$ westward. Notice: the stop pulled down the average velocity below the jogging speed because average velocity depends on displacement, not on how much she moved.

*What would the position-time graph look like?* A straight line with negative slope (going down as time goes right) from (0 s, 1200 m) to (480 s, 48 m). Then a horizontal line (no change in position) from (480 s, 48 m) to (600 s, 48 m). Then another straight line with negative slope from (600 s, 48 m) to (840 s, –528 m).

*What would the velocity-time graph look like?* A horizontal line at –2.4 m/s from t = 0 to t = 480 s. A horizontal line at 0 m/s from t = 480 s to t = 600 s. A horizontal line at –2.4 m/s from t = 600 s to t = 840 s. The area under this graph: (–2.4 m/s)(480 s) + 0 + (–2.4 m/s)(240 s) = –1728 m, which matches the total displacement.

---

## Exercises

**Warm-up (direct application)**

1. A student walks from his house (origin) 100 m north to the store, then 50 m south to a friend's house. Set north as positive. Calculate: (a) total distance traveled, (b) displacement, (c) magnitude of displacement.

2. A car travels 200 km in 4 hours. Is this information sufficient to calculate average velocity? Why or why not?

3. A position-time graph shows a horizontal line. What does this tell you about the object's motion?

4. A velocity-time graph shows a horizontal line at +10 m/s for 5 seconds. What is the displacement during this time?

**Application (requires translation)**

5. A toy train travels around a circular track of circumference 12 m. It takes the train 20 seconds to complete one lap. (a) What is the distance traveled? (b) What is the displacement? (c) What is the average speed? (d) What is the average velocity? (e) Why are (c) and (d) different?

6. Two runners start at the same location. Runner A jogs 5 km north in 35 minutes. Runner B jogs 6 km south in 42 minutes. Without calculating, explain which runner has the greater average speed and which has the greater magnitude of average velocity.

7. A velocity-time graph shows a straight line that increases in slope (gets steeper) over time. The line goes from (0 s, 0 m/s) to (10 s, 50 m/s). Estimate the displacement using the area under the curve. (Hint: the shape is a triangle.)

8. A position-time graph shows two segments: a straight line from (0 s, 0 m) to (4 s, 12 m), then another straight line from (4 s, 12 m) to (8 s, 20 m). (a) Calculate the velocity during the first segment. (b) Calculate the velocity during the second segment. (c) Is the overall motion uniform?

**Synthesis (combine concepts)**

9. A cyclist rides from point A to point B (2 km away) at 10 m/s. She rests for 5 minutes. She then rides back from B to A at 15 m/s. (a) Calculate the total displacement. (b) Calculate the total distance. (c) Calculate the total average velocity. (d) Calculate the total average speed. (e) Sketch both the position-time and velocity-time graphs for this motion.

10. Two objects are graphed on the same position-time plot. Object X is a straight line from (0 s, 0 m) to (10 s, 50 m). Object Y is a curve that starts at (0 s, 0 m) and reaches (10 s, 50 m), but the curve is concave down (bends downward). Both objects end at the same position at the same time. What can you infer about their average velocities? Their instantaneous velocities at t = 0? Which one traveled farther?

**Challenge (open-ended)**

11. Imagine a scenario where an object's displacement is zero but its distance is nonzero. Describe the motion. Then sketch what both the position-time and velocity-time graphs would look like.

12. A satellite orbits Earth once every 90 minutes, at a constant speed of 7.8 km/s. (a) What is the satellite's average velocity after one orbit? (b) After half an orbit? (c) Is it possible for an object to have constant speed but changing velocity? Explain using this satellite as an example.

13. On a position-time graph, you see one object moving with constant velocity (straight line) and another accelerating from rest (curved line). Both start at the origin at t = 0 and reach the same final position at the same final time. (a) Which object has the greater average velocity? (b) Which object has the greater instantaneous velocity at the end? (c) Which object traveled faster at the beginning? Explain your reasoning.

---

## Chapter summary

Motion is a relationship, not a property. You cannot say an object is moving without specifying what you are comparing it to — a reference frame. Once you choose a reference frame, position, distance, and displacement become precise. Distance is the path length (always positive). Displacement is the net position change (can be positive, negative, or zero, depending on your chosen positive direction).

Similarly, speed and velocity both measure how fast position changes, but speed ignores direction while velocity includes it. They are the same only if the motion is in one direction.

Graphs encode motion as geometry. The slope of a position-time graph is velocity. The slope of a velocity-time graph is acceleration. The area under a velocity-time graph is displacement.

The central idea to watch for: *Direction matters in physics*. That is why we distinguish distance from displacement, speed from velocity, and carefully label axes on graphs. Without direction, we lose information. This distinction becomes essential in the next chapter, where we study what causes motion to change.

---

## Connections forward

This chapter gives you the vocabulary for describing motion. The next chapter asks: *why* does motion change? Why does a car accelerate? Why does a ball fall? To answer these questions, you need Newton's laws and the concept of force. Motion itself — the kinematics — is only half the story. The causes of motion — the dynamics — are the other half.

One more preview: you will eventually learn that displacement, velocity, and acceleration are all vectors. The skills you are building now — choosing a direction, applying signs consistently, reading graphs — are the foundation for understanding how forces push objects in particular directions, causing their motion to change in precise, calculable ways.

---

**What would change my mind:** If evidence showed that reference frames were not necessary to describe motion (i.e., that motion existed in absolute terms), this chapter's entire foundation would shift. Currently, every experiment confirms that motion is relative. Even Einstein's theories of relativity, which revolutionized physics, did not overturn the principle that motion is frame-dependent — they only showed that the frame-dependence is more subtle than Newton believed.

**Still puzzling:** Why does the human perceptual system make motion relative, yet feel like we are at rest on the ground? We are moving through space at thousands of kilometers per hour (Earth's rotation, orbit around the sun, galaxy's motion through space), yet we feel stationary. The brain chooses the reference frame that feels most useful. This raises deeper questions about perception and reality that physics alone cannot answer, but understanding motion deeply makes the puzzle sharper.

---

**Tags:** kinematics, reference frames, vectors, scalars, displacement, velocity, graphing motion, one-dimensional motion

---

*Byline: Nik Bear Brown, 2026*
---

## LLM Exercise — Chapter 2: Motion in One Dimension (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the ramp-and-flat-surface position-time demo — visual evidence of constant acceleration vs. constant velocity.
**Tool:** **Claude Project** for the entry. Phone for video. Optional **Claude Code** to digitize and graph.

---

**The Prompt:**

```
Chapter 2 demo for my Physics Demos Notebook. Notebook Charter is
in this Claude Project. Chapter 2 taught: position and reference
frames; speed vs. velocity (direction matters for velocity);
average vs. instantaneous; reading position-time and velocity-time
graphs (slope of x-t = velocity; slope of v-t = acceleration; area
under v-t = displacement).

**The Demo:** Roll a ball down a ramp onto a flat surface. Measure
position at equal time intervals. Compare ramp segment (constant
acceleration) to flat segment (approximately constant velocity).

**Materials:**
- A ramp: a textbook on a few magazines, or a board on books, or
  a hardcover book propped at one end.
- A ball that rolls smoothly: marble, ping-pong ball, small
  rubber ball.
- A flat surface continuous with the ramp's foot.
- A measuring tape or ruler. Mark the surface at 10 cm intervals
  with painter's tape or chalk.
- A phone with video recording (or a stopwatch and patience).

**Procedure:**

1. Set up: ramp angle ~10–20 degrees. Mark positions at 10 cm
   intervals from the top of the ramp through the flat surface.
   Total length: aim for 60–80 cm.

2. Predict before observing: The ball should accelerate down the
   ramp (gravity component); it should decelerate slightly on the
   flat (friction). Predict the time to traverse each marked
   interval. Will the times be equal? Decreasing? Increasing?

3. Run the experiment: release the ball from a consistent starting
   point. Record video at 30 or 60 fps. Run 5 trials.

4. Analyze: For each trial, identify the frame the ball passes
   each mark. Compute the time to traverse each interval. Tabulate.

5. Compute average velocity for each interval (distance / time).
   Plot velocity vs. time (centered at midpoint of each interval).

**Use Claude as a thinking partner:**
- Before the demo: "Predict what the velocity-time graph should
  look like for ramp + flat surface. Sketch it in words."
- After the demo: "Here are my measured times and velocities.
  Does the data fit constant acceleration on the ramp and
  approximately constant velocity on the flat? Where does the
  data deviate from the prediction, and what physical effect
  could cause the deviation (slipping, spinning, ramp-foot bump)?"

**Notebook entry should include:**
- The materials and setup (with photo).
- The prediction sketched in advance.
- The data table (time per interval, computed velocity).
- The position-time and velocity-time graphs (sketched by hand
  or generated with Claude Code).
- The verdict: constant acceleration on the ramp? Constant
  velocity on the flat? Magnitudes that make sense?
- One thing that didn't work the first time and what you changed.

End with one specific question the demo raised: e.g., "Why does
the ball seem to lose energy at the ramp-foot transition?" These
questions become the threads for later chapters.
```

---

**What this produces:** A complete demo entry with data, graphs, and analysis. The transition from constant acceleration to constant velocity at the ramp foot is one of physics's most teachable moments — the demo makes it tactile.

**How to adapt this prompt:**

- *For your own project:* Smartphone video at 60 fps gives 16.7 ms time resolution — plenty for marble-on-ramp. If you don't have video, use a stopwatch but expect noisier data.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want to digitize the video frame-by-frame and produce real position-time graphs, Claude Code with OpenCV or video-frame extraction is the right tool. Optional but valuable.
- *For a Claude Project:* The entry goes in the notebook. Photos commit to the project folder.

**Connection to previous chapters:** Ch 1's "model vs. reality" discipline gets exercised — the constant-velocity model will fail on the ramp; the constant-acceleration model will fail on the flat (because of friction).

**Preview of next chapter:** Chapter 3 is acceleration in detail. You'll do a free-fall demo — drop two objects of very different mass and time them. The chapter's claim that g is mass-independent gets tested.


---

## AI Wayback Machine

**Galileo Galilei** worked out the kinematics of falling bodies in the late 16th century.

**Run this:**

```
Who is Galileo Galilei, and how does their work connect to motion in one dimension we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Galileo Galilei"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Galileo Galilei's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Galileo Galilei's framework."

What changes? What gets better? What gets worse?
