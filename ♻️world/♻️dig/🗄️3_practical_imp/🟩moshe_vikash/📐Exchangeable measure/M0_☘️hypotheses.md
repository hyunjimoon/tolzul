2025-04-10





| Hypothesis                                                                                                                     | Mathematical Form                                                                                                                   | Key Example                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1a: Higher prior mean of market potential increases relative value of modular learning                                        | $\color{blue}{\mu_\phi} \uparrow$ → $\color{brown}{\Delta EU^\phi} \uparrow$ relative to $\color{brown}{\Delta EU^{\phi\theta}}$    |                                                                                                                                                                 |
| H1b: Higher uncertainty in prior distribution of market potential increases relative value of modular learning                 | $\color{blue}{\sigma_\phi} \uparrow$ → $\color{brown}{\Delta EU^\phi} \uparrow$ relative to $\color{brown}{\Delta EU^{\phi\theta}}$ | Zappos: High uncertainty in online shoe market potential drove modular testing choice                                                                           |
| H2: Higher ratio of integrated to modular testing costs decreases relative value of integrated learning                        | $\frac{\color{brown}{c^{\phi\theta}}}{\color{brown}{c^\phi}} \uparrow$ → $\color{brown}{\Delta EU^{\phi\theta}} \downarrow$         | Tesla: High cost ratio of integrated testing drove initial modular approach before Fremont consolidation                                                        |
| H3: Higher correlation between $\color{green}{\phi}$ and $\color{red}{\theta}$ increases relative value of integrated learning | $\rho(\color{green}{\phi}, \color{red}{\theta}) \uparrow$ → $\color{brown}{\Delta EU^{\phi\theta}} \uparrow$                        | Commonwealth Fusion: High correlation between magnet performance ($\color{red}{\theta}$) and market viability ($\color{green}{\phi}$) led to integrated testing |


2025-02-11

[[📜gans20_choose(tech)]]

| Hypothesis                                                                                                                     | Mathematical Form                                                                                                                   | Key Example                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1a: Higher prior mean of market potential increases relative value of modular learning                                        | $\color{blue}{\mu_\phi} \uparrow$ → $\color{brown}{\Delta EU^\phi} \uparrow$ relative to $\color{brown}{\Delta EU^{\phi\theta}}$    |                                                                                                                                                                 |
| H1b: Higher uncertainty in prior distribution of market potential increases relative value of modular learning                 | $\color{blue}{\sigma_\phi} \uparrow$ → $\color{brown}{\Delta EU^\phi} \uparrow$ relative to $\color{brown}{\Delta EU^{\phi\theta}}$ | Zappos: High uncertainty in online shoe market potential drove modular testing choice                                                                           |
| H2: Higher ratio of integrated to modular testing costs decreases relative value of integrated learning                        | $\frac{\color{brown}{c^{\phi\theta}}}{\color{brown}{c^\phi}} \uparrow$ → $\color{brown}{\Delta EU^{\phi\theta}} \downarrow$         | Tesla: High cost ratio of integrated testing drove initial modular approach before Fremont consolidation                                                        |
| H3: Higher correlation between $\color{green}{\phi}$ and $\color{red}{\theta}$ increases relative value of integrated learning | $\rho(\color{green}{\phi}, \color{red}{\theta}) \uparrow$ → $\color{brown}{\Delta EU^{\phi\theta}} \uparrow$                        | Commonwealth Fusion: High correlation between magnet performance ($\color{red}{\theta}$) and market viability ($\color{green}{\phi}$) led to integrated testing |

  
In **all** cases:
- **No test** uses $\color{blue}{\mu_\phi}\cdot \color{blue}{\mu_\theta}$.  
- **Modular** uses $\color{green}{\phi_{\text{true}}}\cdot \color{blue}{\mu_\theta}$.  
- **Integrated** calls `integ.stan`, passing binomial data $(n, \text{successes} \approx \color{green}{\phi_{\text{true}}} \times \color{red}{\theta_{\text{true}}})$.  

Color code:  
- **No Test** = $\color{red}{\text{Red}}$  
- **Modular** = $\color{green}{\text{Green}}$  
- **Integrated** = $\color{blue}{\text{Blue}}$

# Testing Strategy Hypotheses

| Hypothesis                                                                                                                                              | Mathematical Form                                                                                                                             | Key Example                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1: Higher correlation between $\color{green}{\phi}$ and $\color{red}{\theta}$ in $\color{blue}{\mu_0}$ increases relative value of integrated learning | $\rho(\color{green}{\phi}, \color{red}{\theta}) \uparrow$ → $\color{brown}{\Delta \Delta EU} \uparrow$                                        | Commonwealth Fusion: High correlation between magnet performance ($\color{red}{\theta}$) and market viability ($\color{green}{\phi}$) led to integrated testing |
| H2: Higher uncertainty in prior distribution $\color{blue}{\mu_0}$ of market potential increases relative value of modular learning                     | $Var(\color{green}{\phi}) \uparrow$ in $\color{blue}{\mu_0}$ → $\color{brown}{\Delta EU_1} \uparrow$ relative to $\color{brown}{\Delta EU_2}$ | Zappos: High uncertainty in online shoe market potential ($\color{green}{\phi}$) drove modular testing choice                                                   |
| H3: Higher ratio of integrated to modular testing costs decreases relative value of integrated learning                                                 | $\frac{\color{brown}{c^{\phi\theta}}}{\color{brown}{c^{\phi}}} \uparrow$ → $\color{brown}{\Delta \Delta EU} \downarrow$                       | Tesla: High cost ratio of integrated testing drove initial modular approach before Fremont consolidation                                                        |

*Independent Variables:*
- $\rho(\color{green}{\phi}, \color{red}{\theta})$: Correlation in prior distribution $\color{blue}{\mu_0}$
- $Var(\color{green}{\phi})$: Uncertainty in market potential in $\color{blue}{\mu_0}$
- $\frac{\color{brown}{c^{\phi\theta}}}{\color{brown}{c^{\phi}}}$: Ratio of integrated to modular testing costs

*Dependent Variable:*
- $\color{brown}{\Delta \Delta EU}$: Relative value of integrated vs. modular learning

| Hypothesis                                                                                                                                     | Mathematical Form                                                               | Key Example                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| H1: Higher correlation between market and implementation uncertainties increases the relative value of integrated testing over modular testing | ρ(φ,θ) ↑ → (ΔEU₂ - ΔEU₁) ↑                                                      | Commonwealth Fusion: High ρ(φ,θ) due to magnet performance directly determining market viability led to choice of integrated testing |
| H2: Resource efficiency of testing strategy depends on the ratio of statistical bias costs to opportunity costs                                | ValidStatBiasCost(φ,N)/OpportunityCost(θ,φ,N,M) → min                           | Zappos: Low ValidStatBiasCost through small inventory test with clear exit criteria minimized OpportunityCost                        |
| H3: The optimal testing strategy minimizes the sum of verification and validation costs given resource constraints                             | min[ValidApproxBiasCost(φ) + VerifConvgBiasCost(θ\|φ,M)] s.t. resource ≥ c_test | Tesla: High VerifConvgBiasCost from dispersed collaboration (8-week cycles) forced restructuring to integrated testing               |

2025-02-10

| Hypothesis                                                   | Mathematical Form                                                                                          | Key Example                                                                                                                                                   |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1: Higher idea value belief leads to implementation testing | $\text{If }\mu_0=\text{Beta}(a^\phi>b^\phi)\text{ then }EU_2>EU_1$                                         | Te (Tesla): Started with strong belief in pure EV market ($a^\phi>b^\phi$), chose full implementation despite high costs                                      |
| H2: Higher test cost ratio needs stronger market signals     | $\uparrow\frac{c^{\phi\theta}}{c^\phi}\implies\uparrow\text{ threshold for }EU_2>EU_1$                     | Juicero: Failed by ignoring high cost ratio ($\frac{c^{\phi\theta}}{c^\phi}\approx\frac{\$120M}{\$100K}$), rushed to implementation without market validation |
| H3: Incumbents prefer modular over integrated learning       | $\text{If }\sum(a^\phi+b^\phi)_{\text{incumbent}}\gg\sum(a^\phi+b^\phi)_{\text{entrant}}$ then $EU_1>EU_2$ | To (Toyota): Used existing hybrid knowledge ($\text{high }\sum(a^\phi+b^\phi)$) to test EV market incrementally before full commitment                        |
