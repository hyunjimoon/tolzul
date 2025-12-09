
2025-05-20
using [comparing practice and final exam cld](https://claude.ai/chat/2a1d7a3f-3da0-4237-b3a3-3032d916186f)
# 2025 Final Exam Last-Minute Cheatsheet

| Question # | Key Rule/Formula to Remember                                                                                                                                              | Module Connection | Concept Category                                 |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------ |
| 1.1        | Sociodemographic variables (income, gender) must be normalized - can only appear in (n-1) utility functions                                                               | Module III        | 14. Specification and estimation of logit models |
| 1.2        | Omitted variable bias occurs when omitted variable correlates with included variables, violating exogeneity assumption where cov(x,e)!=0  - check for confounding factors | Module II         | 9. Violations of OLS assumptions                 |
| 1.3        | Exogenous sampling → no weights needed; <br>Endogenous sampling → always apply weights when using in real-world applications                                              | Module IV         | 17. Model estimation with sampling strategies    |
| 1.4        | LR test statistic = 2(LL_unrestricted - LL_restricted) and is ALWAYS non-negative                                                                                         | Module IV         | 16. Statistical tests of model specification     |
| 1.5        | In nested logit, normalize ONE scale parameter (typically μ=1 at top level); others must satisfy μnest > μroot                                                            | Module III        | 18. Nested logit models                          |
| 1.6        | Bayesian with informative priors → smaller standard errors than MLE (tighter posterior distribution)                                                                      | Module VI         | 22. Bayesian estimation                          |
|            |                                                                                                                                                                           |                   |                                                  |
| 2.1        | FOC is necessary but not sufficient for max likelihood - local minima & saddle points also satisfy FOC                                                                    | Module VI         | 22. Likelihood functions & MLE                   |
| 2.2        | For simulation-based estimation: Always use largest possible number of draws for consistent results                                                                       | Module VI         | 21. Simulation based estimations                 |
| 2.3        | Logit mixture with alternative-specific error terms provides more flexibility than simple nested logit                                                                    | Module III/VI     | 20. Mixture models & 19. MEV models              |
| 2.4        | Different scales in RP/SP capture differences in variance of unobserved factors, NOT choice set differences                                                               | Module VI         | 24. Combining RP and SP data                     |
| 2.5        | Must have attributes for ALL alternatives (chosen + unchosen) to estimate discrete choice models                                                                          | Module IV         | 17. Data requirements                            |
|            |                                                                                                                                                                           |                   |                                                  |
| 3          | Discrete mixtures: P(choice) = π₁P₁ + π₂P₂ where π₁ + π₂ = 1; likelihood = product over all choices                                                                       | Module VI         | 20. Mixture models                               |
|            |                                                                                                                                                                           |                   |                                                  |
| 4(a-b)     | Duplicating observations: Preserves coefficient estimates, reduces standard errors by factor of √2                                                                        | Module II         | 6. Least squares regression                      |
| 4(c)       | Check for perfect multicollinearity when using transformed variables: ln(x²) = 2ln(x)                                                                                     | Module II         | 9. Multicollinearity                             |
| 4(d)       | Time series data often violates independence and homoscedasticity assumptions                                                                                             | Module II         | 9. Serial correlation & heteroscedasticity       |
|            |                                                                                                                                                                           |                   |                                                  |
| 5(a)       | To test gender effects: Add gender variable to utility function OR use market segmentation test                                                                           | Module IV         | 16. Testing group differences                    |
| 5(b)       | To test "don't care about cost": Filter data to specific segment, then test H₀: βcost = 0                                                                                 | Module IV         | 16. Testing sensitivities                        |
| 5(c)       | To test substitution patterns: Create nest for suspected alternatives, test if μnest ≠ 1                                                                                  | Module III/IV     | 18. Nested logit & correlation structures        |
| 5(d)       | To test income effects: Create income×time interaction OR segment by income and compare                                                                                   | Module IV         | 16. Testing interaction effects                  |

**Remember:**

- Identification requires normalization (ASCs, sociodemographics, scale parameters)
- Always check for endogeneity, multicollinearity, and proper data structure
- For hypothesis testing, identify if parameters are restricted, then use t-test or LR test
- In nested logit, scale parameters must satisfy μnest > μroot for consistency with utility maximization