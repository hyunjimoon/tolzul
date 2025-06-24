# D1' Pull Strategy: Learn β then Bet

## Core Principle
Observe market response first, then optimize quality based on actual stakeholder parameters.

## Key Characteristics
- **Information flow**: Market → β → q*
- **Trigger**: Actual stakeholder responses
- **Example**: Toyota's kanban system - produce only when downstream signals need

## Mathematical Sequence
1. Observe stakeholder responses to current q
2. Infer β parameters from responses  
3. Optimize q* = argmin E[C(q|β)]

## When to Use
- High demand uncertainty
- Fast-changing markets
- When wrong assumptions are costly
