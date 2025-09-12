2025-05-05


[[taxie.pdf]]

[[🚕taxie sorting hypothesis]]

# TAXIE Entrepreneurial Testing Cost Framework

## Optimality Measure of Experiment θ and Hypothesis φ Testing

$O(\theta, \phi) = \frac{1}{ValidApproxBiasCost(\phi)+ValidStatBiasCost(\phi,N)} \times \frac{1}{VerifApproxBiasCost(\theta|\phi)+VerifConvgCost(\theta|\phi,M)} \times \frac{1}{OpportunityCost(\theta,\phi,N,M)}$

## TAXIE's Actions to Lower Entrepreneurial Testing Cost

|Action to Lower Testing Cost|Example from TAXIE EV Rideshare|
|---|---|
|**Refine and narrow down the hypothesis based on market research and feedback**|After conducting initial market research and ride interviews, TAXIE realized that their hypothesis about EV rideshare appeal was more applicable to full-time drivers seeking to maximize earnings. This refinement helped in reducing the approximation bias by focusing on drivers who would most value lower operating costs.|
|**Increase testing sample**|Initially, TAXIE conducted interviews with Uber riders and airport drivers. After observing promising feedback, they expanded their testing by becoming Uber drivers themselves to gather more comprehensive data on driver needs and actual range requirements.|
|**Specialize customer segment**|Initially targeting general rideshare drivers, TAXIE refined their target segment to full-time rideshare drivers who could benefit most from the $1,518 in additional earnings. They collaborated with experienced drivers to create a service specifically appealing to this segment, ensuring the offering matched current rideshare driver financial needs.|
|**Increase experiment fidelity or resource**|TAXIE initially offered limited testing with interviews and research. To optimize their service offering and understand driver preferences better, they invested in two actual Tesla vehicles with a buyback agreement to test real-world operations and collected detailed operational data over several months.|
|**Design experiments with low upfront costs utilizing reachable resource**|Instead of immediately investing in a large fleet of EVs, TAXIE initially structured a buyback agreement with Tesla owners to secure two vehicles for their trial. They also recruited an experienced rideshare CFO to analyze their existing operational data, reducing upfront costs. This allowed them to test the market demand without a significant initial investment in a 50+ vehicle fleet.|

## Experimental Bias Cost Components in TAXIE's Approach

|Cost Component|Definition|TAXIE Application|
|---|---|---|
|**ValidApproxBiasCost(φ)**|Cost of approximation bias caused by approximating utility with testing hypothesis φ|TAXIE's initial hypothesis that 200-mile range would be sufficient for rideshare shifts was biased. Real-world testing revealed at least 260 miles was needed, showing the cost of their approximate hypothesis.|
|**ValidStatBiasCost(φ,N)**|Cost of statistical bias caused by approximating utility of beachhead customer population with that of N sampled customers|TAXIE's early interviews and ride-alongs provided limited statistical validity. By testing with actual rideshare operations across multiple drivers and shifts, they reduced statistical bias in understanding driver needs and behavior.|
|**VerifApproxBiasCost(θ\|φ)**|Cost of approximation bias caused by approximate testing hypothesis φ with designed experiment θ|TAXIE's two-Tesla experiment had limitations in testing the full hypothesis about profitability at scale. The small fleet operation didn't fully approximate how a larger fleet would operate, creating verification bias.|
|**VerifConvgBiasCost(θ\|φ,M)**|Cost of optimization bias caused by limited resource (represented as time M) early stops experiment θ to test φ before reaching the optimal|TAXIE's 6-month testing timeframe imposed convergence constraints. A longer testing period might have revealed different patterns in maintenance costs or charging infrastructure constraints that weren't apparent in the limited time window.|
|**OpportunityCost(θ,φ,N,M)**|Resource, time, and strategic costs of an experiment θ to test hypothesis φ|By structuring Tesla purchases with buyback agreements, TAXIE minimized opportunity costs. If they had purchased vehicles outright, the opportunity cost would have been much higher. Recruiting an experienced CFO instead of scaling to test profitability also reduced opportunity costs.|

## TAXIE's Key Learning Outcomes

After analyzing their experimental data through this framework, TAXIE determined:

1. The true range requirement (260+ miles vs. hypothesized 200 miles)
2. Driver profitability was validated (~$1,518 in additional earnings)
3. Willingness to pay ($400/week) was confirmed
4. Charging infrastructure would be inadequate at scale (>50 cars)
5. Maintenance costs would be prohibitively high at scale
6. Competitive entry (including Hertz's 100,000 Tesla order) posed a significant threat

By systematically addressing each bias cost component and designing resource-rational experiments, TAXIE made the evidence-based decision to not pursue the venture despite initially promising results from early testing phases.

2025-04-10

| Proposition                                                     | Plot Name                 | Mathematical Core                     | Key Message                                                                                                                                | Technical Notes                                                            |
| --------------------------------------------------------------- | ------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Prop 1: Prior Mean Effect on Test Choice                        | 👥dGMT/dmu plot           | ∂(ΔEU)/∂μ > 0                         | Higher optimism drives go to market testing                                                                                                | c_phi = n * c_y ensures crossing at mu=phi_true, p=0.5                     |
| Prop 2: Confidence Effect on Test Choice                        | 🤜dGMT/dalpha plot        | sign(∂(ΔEU)/∂α) = sign(μ - φ_true)    | Confidence pushes optimists to GMT, pessimists to MVT                                                                                      | Shows divergent effects based on μ vs φ_true                               |
| Prop 2: Confidence Effect on Willingness to Pay for Experiments | 🔺🟢◼️plot                | Prior shape transformation            | Priors shape the ‘peaked vs.\ flat’ distribution for experimental payoffs, with high cost lines excluding more entrepreneurs from testing. | Two rows: High/low c^y; Red WTP line; α↓ transforms triangle→circle→square |
| Prop 3: Sample Size Choice                                      | 🤹‍♀️dGMT/dn plot         | ∂(ΔEU)/∂n = α²/(α+n)²(μ-φ_true) - c^y | Choosing sample size n involves balancing the incremental information gained against the cost of pilot testing.                            | Valid where EU_GMT > EU_MVT; φ_true=0.5                                    |
| Prop 3: Prior Mean and Confidence Effect on Test Choice         | 🤹‍♀️dGMT/d phi_test plot | 3D visualization of ΔEU               | A 3D view shows how \mu and \alpha jointly affect the advantage of GMT versus MVT.                                                         | z: ΔEU, x: \mu, y: \alpha; adjustable φ_true                               |

# TAXIE Case Analysis

| Hypothesis                                                                                                            | 2 Cars                                                                                                                                                                   | 3+ Cars                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| A 200-mile range would provide an electric vehicle enough range for a typical rideshare shift                         | The two vehicles had already proved their vehicles needed at least 260 miles of range                                                                                    | No additional information                                                             |
| Full-time rideshare drivers who adopt Taxie would make more money through lower operating costs and improved payments | Early data already suggests drivers were making more money; current customers were referring friends because of the benefit they saw                                     | No additional information                                                             |
| Rideshare drivers would be willing to pay $400/week for a bundled car service                                         | The first two vehicle and current marketing campaign were already informing that customers are willing to pay                                                            | No additional information                                                             |
| The current charging infrastructure in Boston was sufficient for rideshare drivers                                    | Current infrastructure had been sufficient up to now; however as the size of the fleet scales to >50 cars, this may not be the case                                      | Three cars would still not give much insight; would need a larger fleet               |
| The current systems can be used to operate a larger fleet (>50 vehicles)                                              | Taxie's current systems could manage their two vehicle fleet; needed to test their system at scale                                                                       | A third vehicle would add some insight; a much larger fleet would be more informative |
| Taxie's business model is profitable at scale                                                                         | The team had significant data about operating costs however they knew these costs would decrease at scale, needed a way of figuring out what these costs would look like | Three cars would still not give much insight; would need a larger fleet               |

## 1. Core Hypothesis Components

| Component | Description |
|-----------|-------------|
| Value Creation Hypothesis | Electric vehicles for rideshare drivers would create dual value through premium rides and environmental impact |
| Initial Priors (μφ) | High confidence in environmental impact and premium ride potential |
| Implementation Capability (μθ) | Moderate confidence in ability to manage EV fleet and operations |
| Correlation (ρ) | High correlation between operational execution and value creation |

## 2. Testing Sequence & Bias Mitigation

| Testing Phase                  | Description                                                                                                         | Analysis                                                                                                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Validation Testing (p(φ))      | 1. Uber ride interviews<br>2. Airport driver interviews<br>3. Becoming Uber drivers themselves                      | Criticality: High - direct market feedback<br>Fidelity: Medium - potential selection bias<br>Opportunity Cost: Low - minimal resource commitment         |
| Verification Testing (p(θ\|φ)) | 1. Two Tesla purchases with buyback agreement<br>2. Actual operation testing<br>3. CFO analysis of operational data | Criticality: High - full operational test<br>Fidelity: High - real-world implementation<br>Opportunity Cost: Medium - significant but protected downside |

## 3. Cost Components

| Cost Type | Mitigation Strategy | Actual Implementation |
|-----------|-------------------|----------------------|
| ValidApproxBiasCost | Progressive refinement of target market and value proposition | Multiple iterations of customer interviews and testing |
| ValidStatBiasCost | Diverse sampling methods (rides, airport, direct operation) | Gathered data from multiple channels and customer segments |
| VerifApproxBiasCost | Real-world testing with actual vehicles and operations | Two-Tesla test with full operational implementation |
| VerifConvgBiasCost | Time-boxed testing with clear evaluation metrics | Structured testing period with buyback agreement |
| OpportunityCost | Limited fleet size with buyback agreement | Protected downside through structured deals |

## 4. Learning Outcomes

| Aspect | Initial Belief | Testing Method | Final Learning |
|--------|---------------|----------------|----------------|
| Market Potential | High potential for premium rides with EVs | Customer interviews and direct operation | Market exists but margins insufficient |
| Implementation | Manageable operational challenges | Real vehicle operation and CFO analysis | High maintenance costs and operational complexity |
| Strategic Decision | Viable business model with environmental impact | Progressive testing with protected downside | Decision to not pursue due to margin and competition concerns |

