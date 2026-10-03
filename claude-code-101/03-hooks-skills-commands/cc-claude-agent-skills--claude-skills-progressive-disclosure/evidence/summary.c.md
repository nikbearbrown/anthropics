## What
Support first-response time rose from 42 to 121 minutes across Q3 as free-tier volume grew and on-call lost two engineers. A per-plan priority floor now protects paying tickets, and backlog sits at 63 minutes and falling.

## Why it matters
The auto-triage classifier labelled 94% of tickets correctly but routed short, precise paying-customer questions into the low-priority queue, so headline accuracy hid a systematic misroute at the tail where revenue sits.

## What's new
Rotating unassigned tickets to the on-call pager fixed the tail but doubled interruption cost, and a second classifier shifted the failure mode without changing the rate. A per-plan floor that keeps any paid ticket at medium or above shipped and holds.

## What to do
Keep the classifier and keep the floor. Track first-response by plan rather than in aggregate so a tail misroute cannot hide behind a 94% headline again.
