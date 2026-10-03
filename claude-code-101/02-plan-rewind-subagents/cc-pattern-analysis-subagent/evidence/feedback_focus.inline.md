# Feedback focus — binary search batch

1. Four of five students write the midpoint as `(lo + hi) // 2` and none of those four mention the integer-overflow reason for preferring `lo + (hi - lo) // 2`.
2. Three of five students (Mira, Priya, Omar) describe the loop as "shrinking the range" or "cutting in half" without ever stating an explicit invariant that the target lives in `[lo, hi)` — exactly the failure mode the rubric calls out.
3. Four of five students omit the O(1) space bound entirely, and Omar additionally states the wrong time complexity (`n log n` worst case), so the complexity criterion is the batch's most consistently under-answered.
