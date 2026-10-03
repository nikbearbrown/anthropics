1. Students compute the midpoint as `(lo + hi) // 2` and treat it as the correct form, unaware it can overflow on large inputs and that `lo + (hi - lo) // 2` is the safe version.
2. Students describe "shrinking the range" as a process but do not state a loop invariant — specifically that the target, if present, lies within `[lo, hi)` at every step.
3. Students report complexity incompletely or incorrectly — omitting O(1) extra space, and in one case claiming worst case is O(n log n) instead of O(log n).
