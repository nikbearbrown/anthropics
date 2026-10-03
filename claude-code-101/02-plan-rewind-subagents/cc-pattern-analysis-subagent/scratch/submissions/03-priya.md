# Binary search — Priya

You compare the middle element to what you are looking for and go left or
right. `mid = (lo + hi) // 2`. If the middle matches, done. If not, cut the
range in half based on which side the target must be on.

The loop keeps running while there are elements left to look at. The number
of steps is log base 2 of n, roughly.
