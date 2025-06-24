# Figure: Parameter Space Evolution (G1 vs G2)

This figure visualizes how the three approaches (prediction, prescription, prediction-prescription) evolve in the 3D parameter space (q, βr, βc).

## G1 Case: Symmetric Responsiveness (βr = βc = β)

Starting from (0,1,1):
- **Prediction (green)**: Moves to (0,2,2) - learns both β parameters but keeps q=0
- **Prescription (brown)**: Moves to (ln(3/2),1,1) - optimizes q but doesn't learn
- **Prediction-Prescription (purple)**: Moves to (ln(3/2),2,2) - optimizes q AND learns β

All approaches move in their full dimensional space (1D for prescription on q-axis, 2D for prediction on βr-βc plane, 3D for integrated approach).

## G2 Case: Asymmetric Responsiveness (βr << βc)

Starting from (0,1,1):
- **Prediction (green)**: Moves to (0,2,5) - learns both parameters despite βr being less relevant
- **Prescription (brown)**: Moves to (ln(3/2),1,1) - uses wrong q* due to incorrect β assumption
- **Prediction-Prescription (purple)**: Moves to (ln(4),2,1) - learns only βr, ignores βc

**Key Insight**: The integrated approach intelligently reduces dimensionality by ignoring less relevant parameters (βc when βr<<βc), achieving better results with less computation.

![Parameter Space Evolution Diagram]
- Left panel: G1 symmetric case - all parameters matter equally
- Right panel: G2 asymmetric case - integrated approach exploits structure by selective learning
