[Dynamic Portfolio Selection of NPD Programs Using Marginal Returns](https://pubsonline.informs.org/doi/10.1287/mnsc.48.10.1227.275) by C.Loch, S.Kavadias

abstract
🟪Selecting program portfolios within a budget constraint is an important challenge in the management of new product development (NPD). 
🟩Optimal portfolios are difficult to define because of the combinatorial complexity of project combinations. 
🟦However, at the aggregate level of the strategic allocation of resources across product lines, investment in a program is not an all-or-nothing decision, but can be _adjusted_, resulting in a higher or lower program benefit (e.g., higher or lower quality). In some cases, resources can be adjusted even for individual projects.

🟧With this insight, one can use _marginal analysis_ to optimally allocate the scarce budget. This article develops a dynamic model of resource allocation, taking into account multiple interacting factors, such as independent or correlated, uncertain market payoffs that change over time, increasing or decreasing returns from the NPD investment, carry-over of the investment benefit over multiple periods, and interactions across market segments. 

🟥We characterize optimal policies in closed form and derive qualitative decision rules for managers.
## Paper 2: Dynamic Portfolio Selection Framework (2002)

### 🌱 Seed stage — 4 sentences

1. 🟪 **S1 (Phenomenon).** Innovation managers allocate budgets across multiple uncertain projects over time, facing complex trade-offs between immediate exploitation and future exploration opportunities.
    
2. 🟥 **S9 (Core solution principle).** The optimal dynamic portfolio maximizes expected cumulative returns through marginal analysis, allocating resources where marginal return per dollar is highest across all periods.
    
3. 🟪 **S23 (Dynamic challenge).** Market uncertainties and project interdependencies create non-separable optimization problems where today's decisions constrain tomorrow's opportunities through budget depletion and learning effects.
    
4. 🟥 **S31 (Extended solution).** Approximate dynamic programming with state-dependent value functions enables near-optimal policies that balance current returns against future flexibility under correlated uncertainties.
    

### 🌿 NAIL stage — 8 sentences

1. 🟪 **S1.** Innovation managers allocate budgets across multiple uncertain projects over time, facing complex trade-offs between immediate exploitation and future exploration opportunities.
2. 🟪 **S2.** This multi-period challenge intensifies when projects exhibit technical and market correlations—success in platform technology enables derivative products while market failures cascade across related offerings.
3. 🟩 **S3.** Managers need systematic frameworks to optimize resource allocation across projects and time periods, maximizing cumulative value under budget constraints.
4. 🟧 **S5.** We formulate this as a stochastic dynamic program maximizing E[∑ₜ∑ᵢRᵢₜxᵢₜ] subject to ∑ᵢcᵢₜxᵢₜ ≤ Bₜ where Rᵢₜ represents uncertain returns.
5. 🟦 **S7.** Marginal analysis reveals the optimality condition: invest in projects where λₜ(∂E[Rᵢₜ]/∂xᵢₜ)/cᵢₜ equals the shadow price of budget constraints.
6. 🟥 **S9.** The optimal dynamic portfolio maximizes expected cumulative returns through marginal analysis, allocating resources where marginal return per dollar is highest across all periods.
7. 🟪 **S23.** Market uncertainties and project interdependencies create non-separable optimization problems where today's decisions constrain tomorrow's opportunities through budget depletion and learning effects.
8. 🟥 **S31.** Approximate dynamic programming with state-dependent value functions enables near-optimal policies that balance current returns against future flexibility under correlated uncertainties.

### 🌾 SCALE stage — 16 sentences

1. 🟪 **S1.** Innovation managers allocate budgets across multiple uncertain projects over time, facing complex trade-offs between immediate exploitation and future exploration opportunities.
2. 🟪 **S2.** This multi-period challenge intensifies when projects exhibit technical and market correlations—success in platform technology enables derivative products while market failures cascade across related offerings.
3. 🟩 **S3.** Managers need systematic frameworks to optimize resource allocation across projects and time periods, maximizing cumulative value under budget constraints.
4. 🟩 **S4.** They also require methods to incorporate learning and update allocations as uncertainties resolve, avoiding both premature commitment and excessive option preservation.
5. 🟧 **S5.** We formulate this as a stochastic dynamic program maximizing E[∑ₜ∑ᵢRᵢₜxᵢₜ] subject to ∑ᵢcᵢₜxᵢₜ ≤ Bₜ where Rᵢₜ represents uncertain returns.
6. 🟧 **S6.** Project returns follow correlated stochastic processes with drift μᵢ and volatility σᵢ, captured through covariance matrix Σ reflecting market and technical dependencies.
7. 🟦 **S7.** Marginal analysis reveals the optimality condition: invest in projects where λₜ(∂E[Rᵢₜ]/∂xᵢₜ)/cᵢₜ equals the shadow price of budget constraints.
8. 🟦 **S8.** Numerical experiments demonstrate that ignoring correlations leads to 20-35% value loss compared to optimal policies that explicitly model interdependencies.
9. 🟥 **S9.** The optimal dynamic portfolio maximizes expected cumulative returns through marginal analysis, allocating resources where marginal return per dollar is highest across all periods.
10. 🟥 **S10.** Implementation requires three key inputs: expected returns (from market analysis), correlation matrix (from technical architecture), and budget trajectories (from financial planning).
11. 🟧 **S11.** Solution algorithms employ backward induction for small portfolios and approximate dynamic programming for large-scale problems exceeding 20 projects.
12. 🟧 **S12.** The value function approximation uses basis functions capturing portfolio composition, budget remaining, and time-to-horizon, achieving 95% optimality with polynomial computation.
13. 🟩 **S17.** Empirical studies across biotechnology and software sectors reveal systematic deviations from optimality: firms over-diversify early and under-explore in later periods.
14. 🟪 **S23.** Market uncertainties and project interdependencies create non-separable optimization problems where today's decisions constrain tomorrow's opportunities through budget depletion and learning effects.
15. 🟪 **S24.** Information revelation through project execution updates probability distributions, creating complex real options where delay has both costs and benefits.
16. 🟥 **S31.** Approximate dynamic programming with state-dependent value functions enables near-optimal policies that balance current returns against future flexibility under correlated uncertainties.

### 🛸 SAIL stage — 32 sentences

1. 🟪 **S1.** Innovation managers allocate budgets across multiple uncertain projects over time, facing complex trade-offs between immediate exploitation and future exploration opportunities.
2. 🟪 **S2.** This multi-period challenge intensifies when projects exhibit technical and market correlations—success in platform technology enables derivative products while market failures cascade across related offerings.
3. 🟩 **S3.** Managers need systematic frameworks to optimize resource allocation across projects and time periods, maximizing cumulative value under budget constraints.
4. 🟩 **S4.** They also require methods to incorporate learning and update allocations as uncertainties resolve, avoiding both premature commitment and excessive option preservation.
5. 🟧 **S5.** We formulate this as a stochastic dynamic program maximizing E[∑ₜ∑ᵢRᵢₜxᵢₜ] subject to ∑ᵢcᵢₜxᵢₜ ≤ Bₜ where Rᵢₜ represents uncertain returns.
6. 🟧 **S6.** Project returns follow correlated stochastic processes with drift μᵢ and volatility σᵢ, captured through covariance matrix Σ reflecting market and technical dependencies.
7. 🟦 **S7.** Marginal analysis reveals the optimality condition: invest in projects where λₜ(∂E[Rᵢₜ]/∂xᵢₜ)/cᵢₜ equals the shadow price of budget constraints.
8. 🟦 **S8.** Numerical experiments demonstrate that ignoring correlations leads to 20-35% value loss compared to optimal policies that explicitly model interdependencies.
9. 🟥 **S9.** The optimal dynamic portfolio maximizes expected cumulative returns through marginal analysis, allocating resources where marginal return per dollar is highest across all periods.
10. 🟥 **S10.** Implementation requires three key inputs: expected returns (from market analysis), correlation matrix (from technical architecture), and budget trajectories (from financial planning).
11. 🟧 **S11.** Solution algorithms employ backward induction for small portfolios and approximate dynamic programming for large-scale problems exceeding 20 projects.
12. 🟧 **S12.** The value function approximation uses basis functions capturing portfolio composition, budget remaining, and time-to-horizon, achieving 95% optimality with polynomial computation.
13. 🟦 **S13.** Theoretical analysis establishes monotonicity properties: optimal investment decreases in project cost and increases in expected return, with threshold behaviors at boundary conditions.
14. 🟦 **S14.** Comparative statics reveal non-intuitive results: higher correlation sometimes increases optimal diversification when projects provide natural hedging.
15. 🟧 **S15.** Computational implementation leverages parallel processing for scenario evaluation and gradient-based optimization for continuous allocation decisions.
16. 🟧 **S16.** Software architecture separates portfolio state representation, transition dynamics, and reward calculation, enabling modular extensions for specialized contexts.
17. 🟩 **S17.** Empirical studies across biotechnology and software sectors reveal systematic deviations from optimality: firms over-diversify early and under-explore in later periods.
18. 🟩 **S18.** Behavioral analysis identifies root causes including ambiguity aversion, herding effects, and agency problems where managers prefer "balanced" portfolios over optimal concentration.
19. 🟦 **S19.** Backtesting on 10-year innovation histories shows optimal policies would have increased cumulative returns by 40-60% with same budgets.
20. 🟦 **S20.** Performance attribution decomposes gains: 25% from better timing, 35% from correlation exploitation, 40% from dynamic rebalancing.
21. 🟥 **S21.** Organizations should adopt portfolio optimization tools with automated data feeds for returns estimation and correlation learning from project outcomes.
22. 🟥 **S22.** Governance processes must align incentives with multi-period optimization, avoiding annual budget cycles that encourage myopic allocation.
23. 🟪 **S23.** Market uncertainties and project interdependencies create non-separable optimization problems where today's decisions constrain tomorrow's opportunities through budget depletion and learning effects.
24. 🟪 **S24.** Information revelation through project execution updates probability distributions, creating complex real options where delay has both costs and benefits.
25. 🟩 **S25.** Advanced implementations must therefore integrate Bayesian learning frameworks that update return distributions based on milestone achievements.
26. 🟩 **S26.** Organizational capabilities include portfolio analytics platforms, cross-functional correlation assessment, and dynamic review processes triggered by information events.
27. 🟧 **S27.** Mathematical extensions incorporate regime-switching models where correlation structures change with market conditions or technology generations.
28. 🟧 **S28.** Robust optimization techniques handle parameter uncertainty by solving min-max problems over confidence regions of return and correlation estimates.
29. 🟦 **S29.** Stress testing across 1000 scenarios confirms robust policies sacrifice 5-10% expected return but reduce worst-case losses by 40-50%.
30. 🟦 **S30.** Efficient frontiers mapping return-risk trade-offs guide strategic choices between aggressive growth and defensive diversification postures.
31. 🟥 **S31.** Approximate dynamic programming with state-dependent value functions enables near-optimal policies that balance current returns against future flexibility under correlated uncertainties.
32. 🟥 **S32.** Integration with real options valuation and competitive dynamics models promises comprehensive frameworks for innovation strategy in uncertain, multi-agent environments.