![[🖼️(effectiveness, 🟧🟧🟧) 2025-06-27-11.svg]]
%%[[🖼️(effectiveness, 🟧🟧🟧) 2025-06-27-11.md|🖋 Edit in Excalidraw]]%%
# Figure: Expected Cost Curves by Quality (G0, G1, G2)

This figure shows how expected cost varies with quality choice q for the three model specifications.

## G0: Linear Model
- Expected cost function: L(q) = Cu·q² + Co·(1-q)² - V·q·(1-q)
- Quadratic curve with minimum at q* = (V+2Co)/(2(Cu+Co+V))
- For the example with Cu=1, Co=2, V=2: q* = 1/2
- Symmetric parabola reflecting linear stakeholder responses

## G1: Symmetric Sigmoid Model (βr = βc = 1)
- Expected cost with symmetric S-curves: Pc = 1/(1+e^(-q)), Pr = 1/(1+e^(q))
- Optimal quality: q* = ln((2Co+V)/(2Cu+V))
- For Cu=1, Co=2, V=2: q* = ln(3/2) ≈ 0.405
- Steeper curve around optimum due to sigmoid nonlinearity

## G2: Asymmetric Sigmoid Model (βr << βc)
- When resource partners barely respond to quality while customers are highly sensitive
- Optimal quality shifts dramatically: q* depends on which stakeholder dominates
- For the limiting case: q* = ln(4) ≈ 1.386
- Asymmetric curve reflecting different stakeholder sensitivities

**Key Insight**: The shape and location of the cost minimum fundamentally changes with stakeholder response functions, demonstrating why assuming the wrong model (e.g., using G1 when reality is G2) leads to suboptimal decisions.

[[]]
![Expected Cost Curves]
- X-axis: Quality q
- Y-axis: Expected Cost
- Three curves showing how optimal q* shifts across models
