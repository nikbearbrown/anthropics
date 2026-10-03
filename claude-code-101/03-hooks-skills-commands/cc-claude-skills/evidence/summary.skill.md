## What

A Q3 platform retrospective from engineering all-hands: API p95 latency drifted from 180 ms to 340 ms not because of the two well-tested, flag-gated features that shipped, but because the feature-flag evaluator fetches its rules from a config service on every request and began getting throttled during the daily 09:00 traffic spike once request volume crossed a threshold.

## Why it matters

The regression sat invisible on dashboards for three days because instrumentation covered only the team's own service, not the third-party config service that was the actual bottleneck. Compounding the cost, the team then spent six weeks debating a full evaluator replacement versus a targeted cache — a stall that itself took longer than the eventual fix and blocked any latency recovery in the meantime.

## What's new

The team chose the smaller path: a results cache for the evaluator, written in a week, paired with an invalidation contract written in a second week, and shipped behind its own flag. p95 is back to 190 ms and holding. Two generalizable lessons landed: instrument the machinery you did not write, and when a debate stalls, run the small experiment — the cache took less time to build than the argument about whether to build it.

## What to do

Next quarter, audit every third-party client the platform depends on for the same failure pattern: hidden per-request work behind an API that looks free. Extend dashboards to cover those external dependencies so latency regressions in code you did not write become visible on day one, and default to running a small, reversible experiment whenever a build-versus-migrate debate exceeds the cost of just trying the smaller option.
