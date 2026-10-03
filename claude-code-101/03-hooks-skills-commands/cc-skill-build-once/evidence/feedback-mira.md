# Feedback — Mira O., week 4

## 1. Mechanism
Mira correctly identifies the underlying reason: "The mean adds every value and divides by how many there are, so one really big number pulls the whole thing up. The median just picks the middle after sorting, so it doesn't care how big the biggest number is." That captures the core asymmetry — the mean is a function of every value's magnitude while the median only depends on rank order — which is exactly why the median resists outliers. **pass**

## 2. Example
The arithmetic checks out. For `[2, 3, 4, 5, 100]`, the sum is 2 + 3 + 4 + 5 + 100 = 114, and 114 / 5 = 22.8, matching the stated mean. The sorted list has 4 as its middle element, so the median is 4 as claimed. **pass**

## 3. Argument
The example does real work rather than decorating the claim. It contrasts a mean of 22.8 (dragged well above every value except the outlier) against a median of 4 (sitting where the bulk of the data lives), which is a direct demonstration of the mechanism named in the first sentence. The final clause — "the 4 is a better summary of the group because most of the numbers are near it" — closes the loop back to the claim. **pass**

## 4. Precision of language
The everyday phrasing is mostly fine, but two spots are looser than they need to be. "It doesn't care how big the biggest number is" is true for this example but overstated in general — the median is unaffected only as long as changing the extreme values does not cross the middle position; better phrased as "the median depends only on the rank of the middle value, not on how far the extremes sit from it." Similarly, "pulls the whole thing up" would be sharper as "shifts the mean toward the outlier in proportion to its distance." **needs work**

## Growth
Next, learn to say *why* rank-based statistics are robust in general terms — that estimators depending only on order (median, quantiles) have a bounded response to any single value, while estimators depending on magnitude (mean, variance) do not.
