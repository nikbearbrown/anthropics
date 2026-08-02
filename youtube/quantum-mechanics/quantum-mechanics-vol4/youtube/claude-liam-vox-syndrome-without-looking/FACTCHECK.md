# Factcheck

VERDICT: PASS

- The example is explicitly the three-qubit repetition code protecting against one physical X error, not general quantum error correction.
- The encoded state is `alpha|000> + beta|111>` and the stated syndrome convention is disagreement bits `(q1 xor q2, q2 xor q3)`.
- Syndrome mapping is consistent: no error `00`, q1 `10`, q2 `11`, q3 `01`.
- Both logical branches yield the same syndrome for a given error, so syndrome measurement does not reveal alpha or beta.
- Syndrome extraction is not called disturbance-free; it is scoped as preserving coherence within the logical/error subspace.
- Stabilizer-group formalism, surface codes, and fault-tolerance claims are excluded.

