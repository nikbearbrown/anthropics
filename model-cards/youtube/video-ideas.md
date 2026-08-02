# Model Cards Video Ideas

## Candidate 1 — Why do overlapping constraints lock features you never explicitly forbade?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Constraint composition in domain policy design
- Hook: A basic economy booking can upgrade to business class, but this doesn't unlock the ability to change flight routes
- Key case: Customer books basic economy SFO→NYC. Requests change to SFO→LAX. Agent: "Basic economy flight segments cannot be modified." Customer upgrades to business. Agent still: "Reservations booked as basic economy cannot modify flights, regardless of subsequent cabin changes."
- The Question: When constraints are independent (cabin-change is one gate; flight-immutability is another), why doesn't upgrading one gate retroactively unlock another?
- Core idea: Constraints are stateless filters applied at booking-time. Adding a cabin upgrade doesn't retroactively remove a flight-lock—it's a separate rule, and both apply independently to the same reservation.
- Visual object: A matrix showing actions (change flight, change cabin, cancel) × conditions (booking origin, current cabin, time-since-booking), with cells color-coded allowed/forbidden; watch restrictions persist across column changes
- Manim move: morph
- Example seed: Customer booked basic economy AUS→DEN two weeks ago. Tries: change to AUS→MIA (blocked: basic economy). Then upgrades to business (allowed: cabin upgrades work). Tries again: change to AUS→MIA (still blocked: origin constraint survives cabin change). Payoff: the flight-lock was embedded at booking, not released by cabin upgrade.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: refund amounts, payment method details, fare differences
- Score: 9/10

## Candidate 2 — Why does re-reading your own order catch errors that parsing misses?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Confirmation as synchronization checkpoint
- Hook: Before any database update (booking, cancellation, modification), the agent must list all details and obtain explicit "yes" from the user
- Key case: Agent shows: "Cancel reservation ABC: refund $450 to credit card ••4567, 2 passengers, refund in 5–7 days." User: "Wait—I wanted a travel certificate, not a card refund!" Agent re-lists with corrected payment method, user re-confirms, then executes.
- The Question: Why does forcing the user to re-affirm their choices catch mistakes that would be silent in an "parse-then-execute" flow?
- Core idea: Confirmation is a synchronization barrier where the agent's representation of the action and the user's mental intent must match exactly. The user's brain catches mismatches the parser ignored.
- Visual object: A timeline: user intent (internal, hidden) → agent parses into action → agent lists details → user scans and corrects or approves → execute; show intent and parsed representation diverging, then converging at confirmation
- Manim move: split
- Example seed: Customer requests to book for 2 passengers with $30 travel insurance. Agent lists: "Insurance: $60 (2 × $30)." Customer stops: "I only wanted it for one!" Catches the mistake before payment commits.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific airline rules, payment processing
- Score: 9/10

## Candidate 3 — How does forcing agents to act one-at-a-time contain error blast radius?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Serial protocol as error isolation
- Hook: Agents and users are forbidden from batching: "only make one tool call at a time, and if you make a tool call, you should not respond to the user simultaneously"
- Key case: User asks "change flights, add baggage, and waive the rebooking fee." Agent: "I'll do one at a time. Changing your flights to [itinerary]. Confirm?" If the flight change fails (route unavailable), the user sees it before requesting baggage addition; baggage addition never happens.
- The Question: Why does serialization (one action per turn) improve error recovery compared to queuing multiple actions at once?
- Core idea: Each turn's output becomes input to the user's next decision. If action 1 fails, the user cancels action 2 before it amplifies the problem. Batching hides failures until the final state is broken.
- Visual object: Two parallel timelines—batch (3 actions queued, 1 fails mid-queue, all three states mixed)—vs. serial (action 1 completes, user decides next move, catch issue early)
- Manim move: compare
- Example seed: Customer modifies 3 flight segments in one reservation. Batch: queue all 3, segment 1 succeeds, segment 2 fails (flight cancelled), segment 3 succeeds (now reservation is logically broken). Serial: complete segment 1, user notices "segment 2 is on same flight—is it cancelled too?" Agent checks before attempting segment 2.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific tool implementation
- Score: 8/10

## Candidate 4 — How do constraints on the test harness reveal true agent capability?
- Source: `claude-opus-4-5-20251101/tau2/airline_user_prompt.md`
- Topic: Simulation grounding as measurement integrity
- Hook: Simulated users are forbidden from hallucinating: "Never make up or hallucinate information not provided in the scenario instructions…Never make up the results of tool calls"
- Key case: Agent asks "What's the customer's account balance?" The scenario instruction doesn't specify it. A hallucinating user guesses "around $500." A grounded user says "I don't have that information." The grounded user forces the agent to call a balance-lookup tool; the hallucinating user lets the agent succeed by guessing.
- The Question: How do constraints on what the test environment can do (what users can say) change what capability the test actually measures?
- Core idea: A permissive test harness (users hallucinate, provide unstated info) lets agents appear smart by guessing. A constrained harness (users speak only from scenario + tool results) forces agents to query tools and follow procedures. Constraint reveals true behavior.
- Visual object: Two side-by-side test runs—hallucinating user (agent appears successful at guessing)—vs. grounded user (agent's tool-use is exposed and correct); show success-rate difference
- Manim move: scan
- Example seed: Agent asks if customer is refund-eligible. Hallucinating sim: "You're probably eligible?" Agent responds based on guess, counts as success. Grounded sim: "I don't know, can you check?" Agent calls eligibility tool, counts as success only if tool-use is correct.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific tool implementations
- Score: 7/10

## Candidate 5 — Why does the same action produce different outcomes based on customer properties?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md` (refunds section)
- Topic: User properties as independent permission gates
- Hook: Whether a basic economy customer can cancel for free depends on membership tier, not just the booking details
- Key case: Customer A (regular member, no insurance, within 24 hrs): refund approved. Customer B (gold member, with insurance, same scenario): refund + $100 travel certificate. Customer C (regular, has insurance, cancelling for health): refund (insurance covers). Same action, three outcomes.
- The Question: How do user properties (membership, insurance status) act as independent permission gates that stack to unlock different outcomes?
- Core idea: Each user property (tier, insurance, trip type) is a separate gating rule. They don't cascade or override—they layer. A customer can satisfy one gate but not another, producing fine-grained permissions.
- Visual object: A decision tree branching on membership (regular→silver→gold), then insurance (yes/no), then reason (health/weather/other), with leaf nodes showing refund outcomes
- Manim move: accumulate
- Example seed: Regular + no insurance + want refund = no. Add insurance = yes (insurance unlocked it). Change to gold member = yes + $100 cert (tier unlocks bonus). Each property addition opens a new branch, not replacing the old one.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific refund amounts
- Score: 7/10

## Candidate 06 — Why do overlapping constraints lock features you never explicitly forbade?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Constraint composition in domain policy design
- Hook: A basic economy booking can upgrade to business class, but this doesn't unlock the ability to change flight routes
- Key case: Customer books basic economy SFO→NYC. Requests change to SFO→LAX. Agent: "Basic economy flight segments cannot be modified." Customer upgrades to business. Agent still: "Reservations booked as basic economy cannot modify flights, regardless of subsequent cabin changes."
- The Question: When constraints are independent (cabin-change is one gate; flight-immutability is another), why doesn't upgrading one gate retroactively unlock another?
- Core idea: Constraints are stateless filters applied at booking-time. Adding a cabin upgrade doesn't retroactively remove a flight-lock—it's a separate rule, and both apply independently to the same reservation.
- Visual object: A matrix showing actions (change flight, change cabin, cancel) × conditions (booking origin, current cabin, time-since-booking), with cells color-coded allowed/forbidden; watch restrictions persist across column changes
- Manim move: morph
- Example seed: Customer booked basic economy AUS→DEN two weeks ago. Tries: change to AUS→MIA (blocked: basic economy). Then upgrades to business (allowed: cabin upgrades work). Tries again: change to AUS→MIA (still blocked: origin constraint survives cabin change). Payoff: the flight-lock was embedded at booking, not released by cabin upgrade.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: refund amounts, payment method details, fare differences
- Score: 9/10

## Candidate 07 — Why does re-reading your own order catch errors that parsing misses?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Confirmation as synchronization checkpoint
- Hook: Before any database update (booking, cancellation, modification), the agent must list all details and obtain explicit "yes" from the user
- Key case: Agent shows: "Cancel reservation ABC: refund $450 to credit card ••4567, 2 passengers, refund in 5–7 days." User: "Wait—I wanted a travel certificate, not a card refund!" Agent re-lists with corrected payment method, user re-confirms, then executes.
- The Question: Why does forcing the user to re-affirm their choices catch mistakes that would be silent in an "parse-then-execute" flow?
- Core idea: Confirmation is a synchronization barrier where the agent's representation of the action and the user's mental intent must match exactly. The user's brain catches mismatches the parser ignored.
- Visual object: A timeline: user intent (internal, hidden) → agent parses into action → agent lists details → user scans and corrects or approves → execute; show intent and parsed representation diverging, then converging at confirmation
- Manim move: split
- Example seed: Customer requests to book for 2 passengers with $30 travel insurance. Agent lists: "Insurance: $60 (2 × $30)." Customer stops: "I only wanted it for one!" Catches the mistake before payment commits.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific airline rules, payment processing
- Score: 9/10

## Candidate 08 — How does forcing agents to act one-at-a-time contain error blast radius?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md`
- Topic: Serial protocol as error isolation
- Hook: Agents and users are forbidden from batching: "only make one tool call at a time, and if you make a tool call, you should not respond to the user simultaneously"
- Key case: User asks "change flights, add baggage, and waive the rebooking fee." Agent: "I'll do one at a time. Changing your flights to [itinerary]. Confirm?" If the flight change fails (route unavailable), the user sees it before requesting baggage addition; baggage addition never happens.
- The Question: Why does serialization (one action per turn) improve error recovery compared to queuing multiple actions at once?
- Core idea: Each turn's output becomes input to the user's next decision. If action 1 fails, the user cancels action 2 before it amplifies the problem. Batching hides failures until the final state is broken.
- Visual object: Two parallel timelines—batch (3 actions queued, 1 fails mid-queue, all three states mixed)—vs. serial (action 1 completes, user decides next move, catch issue early)
- Manim move: compare
- Example seed: Customer modifies 3 flight segments in one reservation. Batch: queue all 3, segment 1 succeeds, segment 2 fails (flight cancelled), segment 3 succeeds (now reservation is logically broken). Serial: complete segment 1, user notices "segment 2 is on same flight—is it cancelled too?" Agent checks before attempting segment 2.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific tool implementation
- Score: 8/10

## Candidate 09 — How do constraints on the test harness reveal true agent capability?
- Source: `claude-opus-4-5-20251101/tau2/airline_user_prompt.md`
- Topic: Simulation grounding as measurement integrity
- Hook: Simulated users are forbidden from hallucinating: "Never make up or hallucinate information not provided in the scenario instructions…Never make up the results of tool calls"
- Key case: Agent asks "What's the customer's account balance?" The scenario instruction doesn't specify it. A hallucinating user guesses "around $500." A grounded user says "I don't have that information." The grounded user forces the agent to call a balance-lookup tool; the hallucinating user lets the agent succeed by guessing.
- The Question: How do constraints on what the test environment can do (what users can say) change what capability the test actually measures?
- Core idea: A permissive test harness (users hallucinate, provide unstated info) lets agents appear smart by guessing. A constrained harness (users speak only from scenario + tool results) forces agents to query tools and follow procedures. Constraint reveals true behavior.
- Visual object: Two side-by-side test runs—hallucinating user (agent appears successful at guessing)—vs. grounded user (agent's tool-use is exposed and correct); show success-rate difference
- Manim move: scan
- Example seed: Agent asks if customer is refund-eligible. Hallucinating sim: "You're probably eligible?" Agent responds based on guess, counts as success. Grounded sim: "I don't know, can you check?" Agent calls eligibility tool, counts as success only if tool-use is correct.
- Length band: ~1 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific tool implementations
- Score: 7/10

## Candidate 10 — Why does the same action produce different outcomes based on customer properties?
- Source: `claude-opus-4-5-20251101/tau2/airline_policy.md` (refunds section)
- Topic: User properties as independent permission gates
- Hook: Whether a basic economy customer can cancel for free depends on membership tier, not just the booking details
- Key case: Customer A (regular member, no insurance, within 24 hrs): refund approved. Customer B (gold member, with insurance, same scenario): refund + $100 travel certificate. Customer C (regular, has insurance, cancelling for health): refund (insurance covers). Same action, three outcomes.
- The Question: How do user properties (membership, insurance status) act as independent permission gates that stack to unlock different outcomes?
- Core idea: Each user property (tier, insurance, trip type) is a separate gating rule. They don't cascade or override—they layer. A customer can satisfy one gate but not another, producing fine-grained permissions.
- Visual object: A decision tree branching on membership (regular→silver→gold), then insurance (yes/no), then reason (health/weather/other), with leaf nodes showing refund outcomes
- Manim move: accumulate
- Example seed: Regular + no insurance + want refund = no. Add insurance = yes (insurance unlocked it). Change to gold member = yes + $100 cert (tier unlocks bonus). Each property addition opens a new branch, not replacing the old one.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: specific refund amounts
- Score: 7/10

## Candidate 11 — Why does saying "one more thing" after a tool call permanently break your order?
- Source: `claude-opus-4-5-20251101/tau2/retail_policy.md`
- Topic: One-shot commit as irreversible state transition
- Hook: Modifying order items is a single-use operation—once the tool fires, neither further item changes nor cancellation are possible on that order
- Key case: Customer wants blue shirt changed to red. Agent asks "anything else?" Customer: "That's it." Agent calls modify_items (blue→red). Customer: "Oh wait, also change size M to L!" Agent: cannot modify or cancel—the order is permanently locked in 'pending (items modified)' state with the wrong size.
- The Question: If the customer gave incomplete information and the agent called the API anyway, why can't the agent just call modify_items again with the size correction?
- Core idea: The modify_items API is a one-shot gate that permanently advances order state, simultaneously consuming the agent's only chance to modify AND removing the ability to cancel. The agent must accumulate all intended changes across the conversation before committing once.
- Visual object: A staging buffer filling with change-requests turn by turn; a single commit arrow fires and seals the buffer; the "modify" and "cancel" buttons on the order card gray out permanently
- Manim move: accumulate
- Example seed: Customer orders red (M) shirt + black jeans. Mentions shirt change first, jeans change a turn later. If agent commits after the shirt mention, the jeans stay black forever and the whole order can no longer be cancelled. Correct flow: agent asks "anything else?" twice, collects both changes, commits once.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: none
- Exclusions: payment processing for price differences, the exchange-delivered-order path (same one-shot mechanism, don't cover twice), order-status lifecycle for cancel/return operations

- Score: 8/10
