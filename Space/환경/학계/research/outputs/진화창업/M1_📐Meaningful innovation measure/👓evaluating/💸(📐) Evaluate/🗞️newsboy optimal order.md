
## Understanding the Critical Fractile in TAXIE's Context

The critical fractile is a concept from the newsvendor model that provides a mathematical way to balance two competing risks:

1. **Overage Cost (C₀)**: The cost of testing with too many vehicles if the hypothesis turns out to be false (wasted investment)
2. **Underage Cost (C𝓊)**: The opportunity cost of testing with too few vehicles if the hypothesis is actually true (missed opportunity)

### The Critical Fractile Formula

The formula is: F(n*) = C𝓊/(C₀+C𝓊)

For TAXIE:

- C₀ ≈ $100K per vehicle (cost of each additional EV if the concept fails)
- C𝓊 ≈ $50K per vehicle (lost opportunity per vehicle not tested if concept would succeed)

Plugging these values in: F(n*) = $50K/($100K+$50K) = $50K/$150K = 0.33

### What 0.33 Means for TAXIE

This 0.33 critical fractile is telling TAXIE that:

1. The optimal test size (n*) is the point where there's a 33% chance that if the hypothesis is true, it would have been validated by that sample size.
    
2. In statistical terms, n* is the 33rd percentile of the distribution of sample sizes needed for validation.
    
3. Because overage costs (C₀) are twice the underage costs (C𝓊), TAXIE should be more concerned about over-testing than under-testing.
    

### Why 2-3 Vehicles?

To determine exactly what sample size corresponds to the 0.33 critical fractile, we need to consider TAXIE's prior beliefs:

1. **Prior Belief Distribution**: With TAXIE's relatively uncertain prior (approximately 60% belief that the concept would be viable), and considering the diminishing returns of sample information, the probability distribution suggests that:
    
    - With 1 vehicle: There's roughly a 20% chance of getting a clear signal
    - With 2 vehicles: This increases to around 30%
    - With 3 vehicles: This reaches approximately 35-40%
2. **Diminishing Returns**: The probability of detecting a viable concept increases with each additional vehicle, but with diminishing returns:
    
    - The jump from 0→1 vehicles provides the most information
    - 1→2 vehicles adds significant but less information
    - 2→3 vehicles adds moderate information
    - 3→4 vehicles adds much less new information
3. **Optimal Stopping Point**: When we look for the point where F(n) ≈ 0.33, it falls between 2-3 vehicles. This indicates that if the concept is truly viable, there's about a 33% chance that 2-3 vehicles would be sufficient to validate it.
    

### Practical Implications

For TAXIE's founder, this means:

1. **Start with 3 EVs**: This provides enough vehicles to test the most critical hypotheses (charging infrastructure, range sufficiency, and initial price acceptance testing).
    
2. **Hard Stop at 3**: The critical fractile indicates that testing with more than 3 vehicles would be inefficient given TAXIE's cost structure. The marginal value of information from a 4th vehicle would not justify its $100K cost.
    
3. **Staged Approach**: If the 3-vehicle test shows promise, TAXIE can consider expanding to test remaining hypotheses. If not, they can exit without wasting resources on a larger fleet.
    

This approach embodies rational resource allocation under uncertainty - the essence of the newsvendor model as applied to entrepreneurial testing.