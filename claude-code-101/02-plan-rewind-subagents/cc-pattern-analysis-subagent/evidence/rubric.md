# Rubric — Binary Search

The submission is an explanation of binary search on a sorted list of integers.
It is scored on five criteria. Full credit means the student explains the
criterion clearly enough that a peer could implement it correctly.

1. **Precondition** — the input list must be sorted. The student names it.
2. **Loop invariant** — at each step, the target (if present) is inside the
   half-open interval `[lo, hi)` (or an equivalent statement). The student
   states an invariant, not just "we shrink the range".
3. **Midpoint arithmetic** — the midpoint is computed as `lo + (hi - lo) // 2`,
   NOT `(lo + hi) // 2`, to avoid integer overflow on large lists. The student
   names the overflow reason, or uses the safe form and says it is safe.
4. **Termination** — the loop terminates when `lo == hi`, with the target found
   or absent. The student states the termination condition explicitly.
5. **Complexity** — O(log n) time, O(1) extra space. The student names both.
