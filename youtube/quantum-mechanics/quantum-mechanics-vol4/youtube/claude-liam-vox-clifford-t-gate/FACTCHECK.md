# Factcheck

VERDICT: PASS

- H, S, and CNOT are Clifford gates and preserve the Pauli group under conjugation.
- Gottesman-Knill simulation is scoped to stabilizer inputs, Clifford operations, and compatible measurements rather than all possible Clifford-adjacent scenarios.
- T is a non-Clifford pi/4 phase gate; it breaks closed stabilizer propagation.
- The source card's claim that one T gate makes efficient simulation collapse is removed. One or a few T gates are generally manageable; classical costs tend to grow with non-Clifford resource and structure.
- T is not called an irrational-angle gate, and universality is not treated as proof that every circuit is hard.
- The unsupported universal estimate of roughly 1,000 physical qubits per T gate is removed.

