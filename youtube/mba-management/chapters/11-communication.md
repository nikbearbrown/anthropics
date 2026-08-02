# Chapter 11 — Communication

*The message arrived. The warning didn't.*

---

On January 27, 1986, engineers at Morton Thiokol knew the O-ring seals on the Space Shuttle Challenger would fail in cold weather. They had tested them. The overnight temperature at Cape Canaveral was forecast to drop to 36 degrees Fahrenheit — well below the minimum safe operating temperature of 53 degrees. They prepared a memo. It was technical, dense with data. It recommended delay.

The memo was transmitted. The data arrived. Nobody in the Launch Control Center received the warning.

What happened between sending and receiving is not a story of negligence. It is a story of machinery. At each level of the chain of command, a technically correct message was received, encoded into a new form, and transmitted upward. The engineers' message — encoded as "these seals will fail, do not launch" — was decoded at the next level as "Thiokol has some engineering concerns." That message was re-encoded and sent further up. By the time it reached the Flight Director, it had become a resolved engineering judgment call. The recommendation to delay had been received as a data point, processed, and filed. The warning — the weight of what the engineers actually knew — was gone.

Seven astronauts died 73 seconds after liftoff.

The system did not fail. The message traveled. The communication system worked exactly as it was designed to work. What it was not designed to carry — and what it therefore could not carry — was the engineers' conviction. Their certainty. The thing they knew that could not fit into a memo format, that could not survive re-encoding at three hierarchical levels, that needed a face-to-face conversation in a room where the people making the decision could see the engineers' faces and hear the word "catastrophic" said by someone who meant it.

This chapter is about that gap. Why the message you send is almost never the message that gets heard. What machinery carries it. Where the machinery breaks.

<!-- → [IMAGE: timeline of the Challenger communication chain — January 27 evening to January 28 liftoff; each node shows the message form as it traveled upward: "seals will fail at 36°F" → "Thiokol has engineering concerns" → "concern reviewed and resolved" → liftoff; caption: "the message traveled; the warning did not"] -->

---

## The basic process and where it fails

Shannon and Weaver, two Bell Labs engineers in 1948, gave us the first useful map of communication: a sender encodes a message, transmits it through a channel, a receiver decodes it. Between sender and receiver sits noise — anything that distorts the message. The receiver sends feedback back to the sender, which closes the loop.

This model is more honest than the simple idea of "telling someone something," but it still leaves out almost everything.

Encoding is not neutral. A manager under pressure who says "I want this completed today and I don't care what it costs" often does care what it costs — the emotional state, the urgency, the phrasing have encoded something different from the thought the manager held. Words are imprecise instruments. The encoder chooses the best words available and hopes they carry the meaning intact.

Decoding is not neutral. You receive a message in a moment of exhaustion, after a difficult morning, reading an email on your phone at midnight. The same message would mean something different if you read it in a conference room at 9 a.m. with the sender across the table. Context invades decoding at every moment.

Feedback is the most important and most distorted part of the chain. The mechanism for correcting misunderstanding depends entirely on the receiver feeling safe enough to report honest feedback. When a manager asks "Do you understand?" and the report nods, the manager believes comprehension happened — even if the nod means "I am afraid to ask again." Feedback in a power-imbalanced relationship becomes noise. You say yes when you mean I don't know. You smile when you mean I'm confused. The communication system accumulates false confirmation, and the sender operates on a fictional account of what was understood.

Three types of noise distort the channel.

*Semantic noise* is distortion in meaning. The word "robust" sounds like technical competence until you realize that one engineer means "tested thoroughly," another means "built with redundancy," and a third means "able to handle edge cases." The same word arrives at each decoder and unpacks differently. This is the primary failure in the Challenger memo: the phrase "lower than expected performance margin" meant "catastrophic risk" to the engineers who wrote it and "acceptable uncertainty" to the managers who read it. The word arrived. The meaning did not.

*Physical noise* is simpler: the Slack message arrives with a typo that inverts the meaning. The conference call cuts out. The memo is forty pages long and the critical recommendation is on page thirty-one.

*Psychological noise* is the most consequential. You have decided this person is untrustworthy, political, or trying to cover themselves. A message from someone you have filed as incompetent lands differently than the same message from someone you respect. The Challenger engineers had been categorized by NASA management as contractors — people with skin in the game of getting a launch approved. Their message was decoded through that filter. It arrived as advocacy, not warning.

<!-- → [INFOGRAPHIC: Shannon-Weaver communication model annotated for organizational use — sender → encoding → channel → decoding → receiver, with noise arrows hitting each stage, feedback arrow returning, and labels showing where each Challenger failure occurred] -->

The only corrective is real feedback — not nodding, not compliance, but the receiver reporting what they actually heard. This is why managers who ask "What did you take away from that?" get better results than managers who ask "Do you understand?" The first question requires the receiver to reconstruct the message. The second question only requires them to decide whether it is safe to say no.

---

## The channel and what it can carry

Not all messages should travel the same way. Some need the full bandwidth of human conversation. Others travel better in writing. The concept that captures this is *media richness*.

Daft and Lengel, two organizational communication researchers, ranked channels by the amount of information they can carry. Face-to-face conversation is the richest. You get real-time feedback, nonverbal cues — face, body, tone, pace — the ability to sense confusion and adjust mid-sentence, to ask "wait, do you see what I mean?" and watch the answer cross their face before they say it. Video conference is nearly as rich, though something is lost without physical presence. A phone call is leaner — you lose the face entirely, you are reading only tone and word choice, and the distance makes the connection feel severable. Email is much leaner still: asynchronous, tone-invisible, frozen at the moment of writing. A memo is the leanest operational channel — slow, formal, no feedback mechanism at all.

The critical rule: task complexity and emotional weight determine how rich a channel you need.

For routine information — the meeting is at 3 PM, we will ship Thursday — lean channels work. The message is unambiguous. No feedback is needed. Email saves everyone time. But for complex, ambiguous, or emotionally loaded messages — "I have concerns about your fit for this role," "I think we are about to make a catastrophic mistake" — lean channels fail. The receiver cannot see your face, cannot sense your certainty, cannot ask "wait, are you saying what I think you're saying" and watch you answer. The message gets decoded in silence, in whatever emotional state the receiver happens to be in, through whatever filters they have built around the topic.

This is the Challenger failure at the channel level. O-ring failure risk is complex and emotionally loaded — it contradicts the dominant organizational emotion (schedule pressure, launch optimism). It was sent through a written memo, re-encoded at each hierarchical level, and arrived at the decision-maker stripped of emotional weight. A face-to-face conversation between Thiokol's engineers and the Flight Director would have transmitted not just the data but the engineers' conviction. Conviction is encoded in face, voice, the way someone holds themselves when they are frightened. That signal cannot survive encoding into a memo format. It requires a rich channel.

<!-- → [TABLE: media richness spectrum — rows: face-to-face, video call, phone, email/Slack, formal memo; columns: richness level, what it carries well, what it loses, best use case, failure mode] -->

Tom Allen, an MIT researcher, studied communication frequency among engineers as a function of desk distance. The result was the Allen Curve: beyond about 50 meters, communication frequency drops sharply. This is not because people dislike walking. It is because richness drives frequency. If someone is at your desk, you have a conversation. If someone is across the building, you send an email. The channel shifts, and lower-richness channels are used less often because they carry less — so there is less reason to use them. An office where half the team is remote and half is in-building creates a two-tier information system. The in-person people pick up ambient information — hallway conversations, shared lunch, the background radiation of organizational life. The remote people get the formal channel, which is leaner, slower, and filtered before it arrives.

The solution is not to force everyone in-person. The solution is to be deliberate: which communication moments require richness, which can happen asynchronously, and which should be the same experience for everyone regardless of location. Most organizations do not think about this. They default to whatever is convenient for the people making the decision, which is usually the people already in the room.

<!-- → [CHART: the Allen Curve — x-axis: distance between desks in meters (0–50m shown, with drop-off); y-axis: weekly communication frequency; student should see the steep drop at ~10–15m and near-flat line after 50m; callout: "remote vs. same-building is less different than you think — both are far past the curve's knee"] -->

---

## Hierarchy and the death of upward information

Communication in an organization does not happen in a vacuum. It happens inside a structure that shapes what gets said and what gets heard.

Three directions. **Downward communication** — from manager to direct report — is asymmetrical by design. The person receiving it is in a weaker power position. Their feedback is constrained. They cannot easily say "I disagree" or "I don't understand this" without professional risk. Downward communication carries built-in distortion: the person at the receiving end will filter their response to protect themselves.

**Upward communication** — from direct report to manager — is the rarest direction in hierarchical organizations. Research by Rosemary Stewart found that managers spent 12% of their time communicating with superiors, 41% with direct reports, and 47% with peers. If the people at the top are getting only 12% of their communication from upward channels, and if those upward channels are constrained by power dynamics, then executives are making decisions on information that has been sanitized at each level below them.

The specific mechanism is called the MUM effect — an acronym, but also exactly what it describes. People stay mum about bad news when the recipient has power over them. The frontline worker knows the project is behind schedule. She tells her manager, softening it: "We are experiencing some delays but we have a plan." Her manager tells his director, softening it further: "There are some timing challenges being actively managed." The director tells the VP: "The team is on track with some mitigation underway." By the time the VP reports to the CEO, the project is "on track." Seven levels of softening have transformed a critical problem into a managed situation.

**Lateral communication** — between peers — is the least constrained by power, the fastest, and often the most accurate. Colleagues tell each other things they would never tell a boss. They use richer channels. They speak without career risk. Lateral communication is where organizations actually figure out what is happening.

<!-- → [INFOGRAPHIC: the MUM effect in action — a 5-level hierarchy with the same message passed upward through each level; show the actual words at each level transforming from "we will miss the deadline by 6 weeks" to "timeline is being actively managed"; student should trace the softening at each step and see how a critical fact becomes invisible by the time it reaches the top] -->

<!-- → [INFOGRAPHIC: how information travels in three directions — upward (thin arrow, progressively filtered), downward (thick arrow, authority-laden), lateral (wide arrow, rapid and accurate); annotations showing where each type distorts and why] -->

Amy Edmondson's research on team performance found something that initially made no sense: the best teams reported more problems than the worst teams. The explanation: the best teams had no fewer problems. They just reported them. She named the underlying condition *psychological safety* — the shared belief that you can raise a concern, disagree with the boss, admit a mistake, and not be punished for it. Psychological safety does not mean there are no consequences. It means the consequences for speaking up are less severe than the consequences of silence.

Building psychological safety is explicit managerial work. It requires rewarding bad news. When someone tells you the project is behind, the response that builds safety is "thank you for telling me now" — not "how did this happen?" It requires asking "What am I missing?" It requires admitting your own uncertainty and mistakes loud enough that people hear it. It requires treating disagreement as useful information rather than insubordination.

The Challenger engineers tried to say "do not launch." They did not feel safe saying it plainly — they encoded it carefully, trying to be clear without being insubordinate. They sent it through channels. They were polite. They were heard as cautious but manageable. A psychologically safe system would have allowed one of those engineers to say, in plain language, to the right person, in a rich channel: "If you launch tomorrow, people will die." They could not say that. So they said it in a memo, and the memo arrived without the weight.

---

## The grapevine and what it reveals

In the 1950s and 1960s, researchers studied how information actually moves through organizations. What they found surprised them. Informal networks — the grapevine — moved information faster and more accurately than formal channels.

Keith Davis, the pioneer of this research, found that in many organizations, 75 to 95 percent of grapevine information was accurate. This is not the children's telephone game where "the operator sits down" becomes "the operator has sat down" after ten retellings. This is a social network under selective pressure for truth. People repeat what they heard if it is important and credible. They stop repeating things that do not check out. Accurate information propagates. False information dies out.

The grapevine is faster than formal communication because it does not go through channels. "Did you hear they are laying people off?" travels peer-to-peer through lunch conversations, Slack DMs, hallway chats. It uses the richest medium available. It faces no authority obstruction. And it is doing something the formal channel is not: it is carrying the emotional weight of the information, the context, the interpretation, the "what does this mean for us."

<!-- → [CHART: grapevine accuracy vs. formal channel — bar chart comparing accuracy rate (grapevine ~75-95%, formal channel lower) and speed of information transmission; student should see that the "informal" network is both faster and more accurate than the official one] -->

When a company sends a formal announcement saying "We are not making any changes" and employees simultaneously learn through the grapevine that the company is exploring layoffs, the grapevine is not failing. The grapevine is compensating for the formal channel's failure to carry truth. The formal channel has been used for perception management. The grapevine has rushed in to fill the gap with what people actually know.

Wise managers do not try to suppress the grapevine. They cannot — it is an emergent property of human communication. Instead they read it as a diagnostic: if the grapevine is moving fast and dark, the formal communication system is failing to carry important information. The manager's job is to identify what that information is and start transmitting it through formal channels, with truth.

---

## Context: when the same word means different things

Edward Hall, an anthropologist, noticed that cultures communicate in fundamentally different ways. In some cultures, meaning is carried almost entirely in explicit words. "We will meet Tuesday at 2 PM in the conference room." The context is minimal. The words carry the full message. Hall called this *low-context* communication — the style of German, Dutch, and American business culture.

In other cultures, meaning is embedded in context. The relationship, the history, the unspoken assumptions, the tone, the setting — these carry as much meaning as the words. A manager in a high-context culture might say "You will understand what we need from you" without specifying what is needed, because the relationship is the channel and the relationship carries the understanding. Hall called this *high-context* communication — the style of Japanese, Chinese, Arab, and many relationship-based cultures.

This is not a value difference. It is a channel difference. Low-context cultures compensate for the leanness of written communication by making everything explicit in the writing. High-context cultures assume richness in the relationship and encode meaning there. When people from high-context and low-context cultures work together, the miscommunication is systematic and often invisible.

A person from a low-context culture thinks they are being respectfully direct. The person from a high-context culture hears disrespect — too explicit, treating the task as more important than the relationship, communicating as if there were no relationship. A person from a high-context culture thinks they are communicating clearly through the relationship. The person from a low-context culture hears vagueness — hiding behind politeness, refusing to be concrete, making assumptions rather than stating facts. Neither is wrong. They are using different channels for different signals about what carries meaning.

<!-- → [TABLE: high-context vs. low-context communication — rows: directness of feedback, relationship vs. task priority, role of silence, comfort with ambiguity, example cultures; this is not a ranking, it's a contrast for diagnosis] -->

The solution is not to ask one style to assimilate to the other. It is to name the difference so both sides can translate. "In my culture, I show respect by being direct. When I say something critical, it means I care about the work." "In my culture, the relationship comes before the task. I want to understand you as a person before I can trust your judgment on the work." Naming this makes room for both styles to function. Not naming it creates a communication failure that looks like a personality conflict.

---

## What the machinery requires

Return to the engineers at Thiokol.

They had the right information. They tried to communicate it. They transmitted data through the available channels to the receivers with authority to act. Every part of the communication system functioned. What the system did not have — and what no amount of memo-writing or data transmission could supply — was a channel rich enough to carry conviction, a feedback mechanism safe enough to return honest information upward, and a culture where bad news was received as valuable rather than as threat.

The machinery of communication can be understood and improved. Not to achieve perfect clarity — that is not possible. But to create conditions where the message that needs to be heard has the best possible chance of surviving the journey from sender to receiver.

That requires: matching the channel to the weight of the message. Creating feedback mechanisms that are safe enough to be honest. Understanding that hierarchy systematically distorts upward information and building bypass mechanisms deliberately. Reading the grapevine as diagnostic rather than suppressing it as noise. And recognizing that when a colleague from a different culture seems to be communicating poorly, they may simply be using a channel you have not learned to read.

The Challenger memo arrived. The warning did not. The difference was not the engineers' skill or the NASA managers' intelligence. The difference was the machinery — and the machinery can be changed.

---

## What would change my mind

I am arguing that communication is a system that can be understood and improved. Evidence that would change this: research showing that communication failures are primarily due to individual skill deficits rather than system design, or showing that channel richness does not correlate with message fidelity in organizational settings. So far the research aligns with this account. But organizations are complex. Simpler models that emphasize individual skill have historically underestimated the role of system design.

---

## Still puzzling

What I do not fully understand is why organizations so rarely act on what they know about communication failure. We have known since the 1950s that the grapevine is faster and more accurate than formal channels. We have known since Edmondson's research that psychological safety predicts team performance more strongly than most other factors. We have known since the Challenger investigation what happens when hierarchy prevents bad news from traveling upward. Yet most organizations still operate as if louder, more frequent, more top-down communication is the solution. I suspect this has to do with power: the people making communication policy are the people at the top, and policy that keeps control at the top feels safer to them than policy that empowers the people below.

---

## Exercises

### Warm-up: The machinery in plain sight

1. **Noise classification.** The Challenger memo failed in at least three distinct ways. For each of the three types of noise — semantic, physical, psychological — name one specific moment in the Challenger communication chain where that type of noise distorted the message. Then name one change to the system (not to the people) that would have interrupted each distortion.

2. **Feedback quality.** Your manager just finished explaining a new process to your team. She asks "Does everyone understand?" Three people nod. Two say nothing. One asks a clarifying question. What does each response tell you, and what does it not tell you? Rewrite the manager's question to produce more honest feedback — and explain what mechanism your new question is using to improve on the original.

3. **Channel read.** You receive this message from your manager: "Can you come by my office when you have a moment?" You have been performing well. You also made a small mistake last week. Trace the decoding process: what signals are you interpreting, what context is shaping the interpretation, and what is the gap between what the message says and what you are likely to hear? What could the sender do to reduce that gap without overcommunicating?

### Application: Designing for the machinery

4. **Channel matching.** You are a manager with four messages to deliver today: (a) the team's Q3 budget has been approved; (b) you need to tell a direct report that her recent work quality has slipped and you are worried about her; (c) you need to inform the team of a structural reorganization that will change several people's reporting lines; (d) you need to confirm that tomorrow's 2 PM meeting is still on. For each message, name the channel you would use, explain why, and name the specific failure mode you are avoiding by choosing that channel over the alternatives.

5. **MUM effect bypass.** You are the VP of a 200-person division. You suspect that bad news is being softened as it travels upward to you — your direct reports always seem to have things under control, but the problems you hear about late always turn out to have been visible earlier. Design two specific mechanisms to bypass the MUM effect in your division. For each mechanism, name the exact communication pattern it interrupts and explain how it works.

6. **Grapevine as diagnostic.** You are the CEO of a 75-person company. You notice the grapevine is running hot: people are clustering in small groups, the usual Slack channels have gone quieter, you are catching fragments of conversations about "what's really going to happen." You have not announced anything unusual. What does the active grapevine tell you about the state of your formal communication channels? What is your next move, and why?

### Synthesis: System-level failures

7. **Re-engineer the Challenger communication.** You have been asked to redesign the communication system for the Challenger launch decision — not the engineering, but the communication process. The goal: ensure that a warning of the magnitude the Thiokol engineers were sending would reach the Flight Director in a form that preserved its weight. What are the two or three specific changes to the system — channels, feedback mechanisms, hierarchy bypass — that would have made the most difference? Be specific about which failure mode each change addresses.

8. **Remote team, two-tier risk.** Your company is 40 people. Twenty are in-office in Chicago. Twenty are remote, distributed across time zones. You have noticed that the in-office people seem to know things the remote people don't — they reference conversations that never showed up in Slack, they make decisions in side conversations, the remote people feel behind. Using media richness theory and the Allen Curve, diagnose what is structurally producing this gap. Then propose a communication architecture change — not a cultural change, a structural one — that would reduce the information asymmetry.

### Challenge: Where the framework runs out

9. **Psychological safety and honesty.** The chapter argues that psychological safety creates conditions where people will say what they actually think, which makes organizations more honest and more effective. A critic responds: "Psychological safety just makes it comfortable to say things. It doesn't make what people say more accurate. You can have a psychologically safe culture full of confident wrong beliefs." Engage with this critique seriously. Where is it right? Where does it fail? What would a communication system need to add beyond psychological safety to ensure that the honest messages being sent are also well-calibrated?

---

## LLM Exercise — Chapter 11: Communication

**Project:** Build a Fictional Company (Founder Mode).
**What you're building this chapter:** the communication architecture — channel rules, meeting cadence, async/sync defaults, and the deliberate plan for the grapevine.
**Tool:** **Claude Project** "Founder Handbook" — appends a new section.

---

**The Prompt:**

```
I'm in chapter 11 of building my fictional company. Prior sections
are in the project. This chapter covered: the encoding-channel-
decoding-feedback process model; channel richness (Daft & Lengel —
face-to-face is richest, formal numeric reports are leanest);
barriers (filtering — info distorted as it climbs; selective
perception — receivers see what they expect; information overload;
noise); the formal-organizational chart vs. the grapevine
(grapevine is roughly 75% accurate but selects for what's
emotionally salient over what's important); the MUM effect
(bad news travels up slowly).

The chapter's strongest practical claim: channel choice should
match message content. Rich channels for ambiguous/emotional/high-
stakes content; lean channels for routine/factual/asynchronous
content. Most organizational communication failures are channel
mismatches.

Write the "Communication Architecture" section of the operating
handbook. Cover four things.

1. **The channel matrix.** Build a 2×3 table:
   - Rows: rich (in-person/video) vs. lean (Slack/email/docs).
   - Columns: routine, ambiguous, high-stakes-emotional.
   Fill each cell with: examples of messages that go there, and
   the company's default channel for that quadrant.
   Then specify: what's the "escape rule" — when does an
   email/Slack thread MUST be promoted to a synchronous channel?
   (A useful default: more than three back-and-forth on the same
   ambiguity → call.)

2. **The meeting cadence.** Specify the company's recurring meeting
   structure:
   - Daily/weekly team standups: who attends, what they cover, the
     hard time limit.
   - Weekly leadership meeting: agenda template, decisions vs.
     updates ratio.
   - Monthly all-hands: structure, who speaks, the "no questions
     can be off-limits" rule (and what enforces it).
   - Quarterly planning: the cadence and the role of OKR/goal
     review.
   For each meeting, name: the one thing this meeting is FOR, and
   the one thing it must never become.

3. **The async/sync defaults.** State the company's defaults:
   - When is async strongly preferred (most cross-functional
     coordination, status updates, document review).
   - When is sync required (decisions involving disagreement,
     emotional content, high-stakes announcements, onboarding).
   - The documentation discipline: what async communication MUST
     produce written artifacts (decisions, action items,
     commitments), and what doesn't need to.

4. **The grapevine policy.** The chapter named the grapevine as
   organizationally inevitable and ~75% accurate. Most founders
   try to suppress it (which makes it worse) or claim "we have an
   open culture so there's no grapevine" (which is delusion).
   Specify:
   - The information the founder commits to making public (and
     therefore not requiring grapevine transmission).
   - The information that genuinely cannot be made public (HR
     matters, individual comp, in-progress sensitive decisions).
   - The MUM-effect countermeasure: how bad news gets up to the
     founder despite the natural filtering. Name one specific
     mechanism (e.g., skip-level 1:1s every quarter; anonymous
     question channel before all-hands).

End with a 200-word "Forbidden communication patterns" section.
Examples: surprise reorgs announced in all-hands; Slack-DM
performance feedback; email chains debating decisions that should
have been a 15-minute call. Name the three patterns this company
explicitly forbids and the rule that enforces each.

Output as a single markdown document I can paste into my operating
handbook.
```

---

**What this produces:** A ~1,300-word "Communication Architecture" section with a channel matrix, meeting cadence, async/sync defaults, grapevine policy, and forbidden patterns. The matrix and forbidden-patterns lists are immediately enforceable.

**How to adapt this prompt:**

- *For your own project:* If you're remote-first, the channel matrix tilts heavily lean and the meeting cadence is more deliberate. If you're in-office, the grapevine is faster and the policies need different muscle.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you'll build a meeting-template repo (standup agendas, all-hands templates, decision-log formats), Claude Code is the right tool.
- *For a Claude Project:* The communication architecture is referenced in Chapter 12 (leadership communication), Chapter 14 (conflict communication), and Chapter 16 (change communication).

**Connection to previous chapters:** Chapter 10's psychological-safety design depends on this — PS is built and broken in meeting structures, especially the founder's response patterns in all-hands.

**Preview of next chapter:** Chapter 12 designs the company's leadership philosophy — trait vs. behavioral vs. contingency vs. transformational frameworks, applied to the founder's own development and the company's emerging leadership pipeline.

---

## AI Wayback Machine

**Deborah Tannen** was the linguist whose work on conversational style reshaped how organizations think about workplace communication.

**Run this:**

```
Who is Deborah Tannen, and how does their work connect to communication we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Deborah Tannen"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Deborah Tannen's framework to a current management question.
- Add a constraint: "Answer including criticisms or limits of Deborah Tannen's framework."

What changes? What gets better? What gets worse?
