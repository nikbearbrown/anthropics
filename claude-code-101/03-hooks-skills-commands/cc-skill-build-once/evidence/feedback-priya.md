# Feedback — Priya S., week 4

## 1. Mechanism
Priya names the underlying reason correctly: "the median is the middle after sorting and only depends on rank, not magnitude." That is the right pivot — the mean is a function of every value's magnitude, so a single extreme entry drags it, while the median cares only about the ordinal position of the middle element and so is insensitive to how far the outlier sits from the rest. The opening clause ("Outliers move the mean a lot but move the median almost nothing") states the phenomenon and then the "because…" clause supplies the actual mechanism, which is what the prompt asked for. **pass**

## 2. Example
The arithmetic checks out. The five scores are 1, 6, 6, 7, 8; the sum is 1 + 6 + 6 + 7 + 8 = 28, and 28 / 5 = 5.6, matching the stated mean. Sorted, the third (middle) value is 6, so the median is 6 as claimed. **pass**

## 3. Argument
The example does real work: swapping in one low score (1) leaves four of the five values untouched at 6–8, yet pulls the mean down to 5.6 while the median holds at 6 — a direct, minimal demonstration of the rank-vs-magnitude contrast named in the first sentence. It is not decorative; it is the smallest case that would make the point. The parenthetical "(looks bad for the class)" is a stylistic aside rather than argumentative weight, but it does not undermine the connection between claim and example. **pass**

## 4. Precision of language
The technical vocabulary — "middle after sorting," "rank, not magnitude" — is used correctly, and the phrasing is tight. One spot is looser than it needs to be: "move the median almost nothing" is true here but understates the guarantee, since for a fixed sample size the median is unchanged by *any* movement of a non-middle value that does not cross the middle position; a sharper rewrite would be "outliers can shift the mean without bound, while the median is unchanged as long as the outlier stays on the same side of the middle rank." Also, "the mean drops to 5.6" implicitly compares to an unstated baseline (the outlier-free mean of 6.75) — naming that baseline would make the contrast quantitative rather than rhetorical. **needs work**

## Growth
Next, learn to say that the median is a *rank statistic* with a bounded influence function while the mean's influence function is unbounded — that is the general principle behind the specific behavior Priya described.
