
| Component | Description | SAFE Optimization Context |
|-----------|-------------|---------------------------|
| State (s) | Current condition of the environment | Pre-money valuation, number of common shares, existing SAFEs |
| Action (a) | Possible decisions or strategies | Investment amount, valuation cap for new SAFE |
| Environment (Env) | Models how actions and states interact | PostMoneySAFEModel class, calculating conversion and ownership |
| Utility (U) | Quantifies desirability of outcomes | Founder's payoff (founders_shares * exit_share_price) |
| Expectation (E[]) | Accounts for uncertainty through probabilistic reasoning | Consideration of potential exit valuations |
| Argmax | Selection of action maximizing expected utility | Choosing optimal investment and valuation cap |
| act* | Optimal action taken at each point in time | Finalizing SAFE terms (investment amount and valuation cap) |
Table 1: Component-wise Decomposition of Rational Agency for SAFE Optimization