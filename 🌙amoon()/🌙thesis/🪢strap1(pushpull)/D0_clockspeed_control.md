# D0' Clockspeed Control: Managing Push-Pull Balance

## Core Decision Variable
τ = cycle time between optimization rounds

## Impact on Strategy
- **Small τ (fast cycles)**: System becomes more pull-like
  - Daily or weekly adjustments
  - Quick response to market changes
  - Example: Zara's 2-3 week design cycles

- **Large τ (slow cycles)**: System becomes more push-like  
  - Quarterly or annual planning
  - Batch optimization based on forecasts
  - Example: Traditional automotive model years

## Key Trade-off
Fast cycles enable responsiveness but increase coordination costs.
Slow cycles enable efficiency but risk forecast errors.

## Mathematical Connection
- As τ → 0: Continuous learning (pure pull)
- As τ → ∞: One-shot optimization (pure push)
- Optimal τ* balances learning value vs. adjustment costs
